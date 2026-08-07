#!/usr/bin/env python3
"""
validate.py — structural conformance check for a model's translated window.

Style is checked by a human (and by `translation-qa`). This module checks only
what a machine can check without opinion:

  V1  block-ID set and order identical to the source window
  V2  per-block output line count == source line count
  V3  final line ends with a single space then the block ID
  V4  no source-script characters leaked into the output
  V5  no code fences, no model preamble, no `[Ed: …]` unless allowed
  V6  hard-break policy (two trailing spaces on non-final lines), when enabled

Errors are returned as strings, phrased so they can be fed straight back to the
model as a repair instruction.
"""

from __future__ import annotations

import re

from structure import BLOCK_ID_RE, Block, script_report

FENCE_RE = re.compile(r"^\s*```")
HEADING_RE = re.compile(r"^(#{1,6})\s+(.*)$")


def strip_wrapper(text: str) -> str:
    """Remove code fences and any leading/trailing model chatter."""
    lines = text.replace("\r\n", "\n").split("\n")
    # drop a leading fence and its closing partner
    if any(FENCE_RE.match(ln) for ln in lines[:3]):
        start = next(i for i, ln in enumerate(lines) if FENCE_RE.match(ln))
        lines = lines[start + 1:]
        for i in range(len(lines) - 1, -1, -1):
            if FENCE_RE.match(lines[i]):
                lines = lines[:i]
                break
    # drop leading lines before the first block/heading-looking line
    while lines and not lines[0].strip():
        lines.pop(0)
    while lines and not lines[-1].strip():
        lines.pop()
    return "\n".join(lines)


def parse_output_blocks(text: str) -> list[tuple[str, list[str]]]:
    """Split model output into (block_id, lines) in emitted order."""
    out: list[tuple[str, list[str]]] = []
    for para in re.split(r"\n\s*\n", strip_wrapper(text)):
        lines = [ln for ln in para.split("\n") if ln.strip()]
        if not lines:
            continue
        m = BLOCK_ID_RE.search(lines[-1])
        if not m:
            continue
        out.append((m.group(1), lines))
    return out


def normalise_hard_breaks(lines: list[str], enable: bool) -> list[str]:
    """Apply the two-trailing-spaces hard-break convention mechanically.

    This is a formatting fix, not a content fix, so it is safe to apply
    silently rather than spending a repair round-trip on it.
    """
    fixed = [ln.rstrip() for ln in lines]
    if not enable:
        return fixed
    for i in range(len(fixed) - 1):
        fixed[i] = fixed[i] + "  "
    return fixed


def validate_window(
    *,
    source_blocks: list[Block],
    output_text: str,
    source_scripts: tuple[str, ...] = ("tibetan", "devanagari"),
    hard_breaks: bool = True,
    allow_editorial: bool = False,
) -> tuple[list[tuple[str, list[str]]], list[str]]:
    """Return (normalised blocks, errors). Empty errors == the window is clean."""
    errors: list[str] = []
    emitted = parse_output_blocks(output_text)

    want_ids = [b.block_id for b in source_blocks]
    got_ids = [bid for bid, _ in emitted]
    want_lines = {b.block_id: b.line_count for b in source_blocks}
    heading_ids = {b.block_id for b in source_blocks if b.is_heading}

    # V1 — block-ID parity and order
    if got_ids != want_ids:
        missing = [b for b in want_ids if b not in got_ids]
        extra = [b for b in got_ids if b not in want_ids]
        dupes = sorted({b for b in got_ids if got_ids.count(b) > 1})
        if missing:
            errors.append(
                f"V1 missing block(s): {', '.join('^' + b for b in missing)} — "
                "every source block must appear exactly once"
            )
        if extra:
            errors.append(
                f"V1 block(s) not in the source: {', '.join('^' + b for b in extra)} — "
                "do not invent block IDs"
            )
        if dupes:
            errors.append(
                f"V1 duplicate block(s): {', '.join('^' + b for b in dupes)}"
            )
        if not (missing or extra or dupes):
            errors.append("V1 all blocks present but emitted out of source order")

    # V2/V3/V6 — per block
    normalised: list[tuple[str, list[str]]] = []
    for bid, lines in emitted:
        if bid in heading_ids:
            normalised.append((bid, [lines[0].rstrip()]))
            if len(lines) != 1:
                errors.append(f"V2 ^{bid}: a heading must be a single line, got {len(lines)}")
            elif not HEADING_RE.match(lines[0].strip()):
                errors.append(f"V2 ^{bid}: heading must start with markdown `#` markers")
            continue

        want = want_lines.get(bid)
        if want is not None and len(lines) != want:
            errors.append(
                f"V2 ^{bid}: emitted {len(lines)} line(s), the source block has "
                f"{want} — the counts must match exactly"
            )
        if not re.search(rf"\s\^{re.escape(bid)}\s*$", lines[-1]):
            errors.append(
                f"V3 ^{bid}: the final line must end with a single space then ^{bid}"
            )
        normalised.append((bid, normalise_hard_breaks(lines, hard_breaks)))

    body = "\n".join(ln for _, lns in normalised for ln in lns)

    # V4 — source-script leakage
    report = script_report(body)
    for script in source_scripts:
        if report.get(script):
            errors.append(
                f"V4 {script.capitalize()} script found in the output — the "
                "translation must be in the target language only"
            )

    # V5 — apparatus
    if not allow_editorial and re.search(r"\[Ed[:\]]", body):
        errors.append("V5 `[Ed: …]` editorial note found — this track permits none")
    if "[^" in body:
        errors.append("V5 footnote marker found — this track permits none")

    return normalised, errors


def render_blocks(blocks: list[tuple[str, list[str]]]) -> str:
    """Reassemble validated blocks into markdown, blank line separated."""
    return "\n\n".join("\n".join(lines) for _, lines in blocks)
