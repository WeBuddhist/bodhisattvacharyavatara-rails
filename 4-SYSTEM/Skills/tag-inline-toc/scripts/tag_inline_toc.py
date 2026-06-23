#!/usr/bin/env python3
"""
tag_inline_toc.py — Phase-2 deterministic renderer + verifier for the
`tag-inline-toc` skill.

The skill is split into two phases:

  Phase 1 (model)  — read the commentary once and emit a compact *annotation*
                     (JSON): an ordered list of sa bcad sections, each with a
                     depth, a short heading title, an exact body-start context,
                     an optional self-restatement term, and an optional
                     "announced in parent" term. No block IDs, no headings,
                     no rewriting of prose.

  Phase 2 (this)   — take the original file + the annotation and do everything
                     deterministic: assign `^N-…-0` block IDs from depth,
                     insert heading lines, wrap the exact term substrings in
                     `[[#^id|term]]` wikilinks via anchored matching, and then
                     PROVE that no existing prose was altered before writing.

Because IDs are assigned by code, depth-skipping and numbering bugs are
impossible by construction. Because wraps are exact-substring/anchored and the
result is diffed back against the source, silent transcription drift is caught.

Usage
-----
  Render an annotated file:
      python3 tag_inline_toc.py render \
          --input  0-INBOX/segmentation/foo.md \
          --annot  annotation.json \
          --output 0-INBOX/temp/tagged-foo.md

  (If --output is omitted, the path is derived as
   0-INBOX/temp/tagged-<input-basename>, with -v2/-v3 suffixing if it exists.)

  Verify an already-tagged file against its untagged source:
      python3 tag_inline_toc.py verify \
          --input  0-INBOX/segmentation/foo.md \
          --tagged 0-INBOX/temp/tagged-foo.md

Annotation format: see annotation.schema.json and example-annotation.json in
this folder.

Exit status is non-zero on any error (ambiguous anchor, missing term, depth
skip, or prose-integrity violation) so the skill can fail loudly.
"""
from __future__ import annotations

import argparse
import json
import os
import re
import sys
from dataclasses import dataclass, field


# --------------------------------------------------------------------------- #
# Errors                                                                       #
# --------------------------------------------------------------------------- #
class TagError(Exception):
    """Any condition that should abort rendering with a clear message."""


# --------------------------------------------------------------------------- #
# Wikilink helpers                                                             #
# --------------------------------------------------------------------------- #
# [[target|display]]  or  [[display]]   — Obsidian wikilink, possibly with a
# block-ref target like  #^1-2-0  or  file#^1-2-0.
_WIKILINK_RE = re.compile(r"\[\[(?:[^\]|]*\|)?([^\]]*)\]\]")
# A heading line we are allowed to have inserted: "## ... ^N-...-0"
_HEADING_RE = re.compile(r"^#{2,6}\s.*\s\^[0-9]+(?:-[0-9]+)*-0\s*$")


def unwrap_links(text: str) -> str:
    """Replace every [[...|display]] / [[display]] with its display text."""
    return _WIKILINK_RE.sub(lambda m: m.group(1), text)


def heading_level(depth: int) -> str:
    """depth 1 -> '##', depth 2 -> '###', ... capped at 6 '#'s (###### )."""
    return "#" * min(depth + 1, 6)


# --------------------------------------------------------------------------- #
# Block-ID assignment (deterministic, depth-driven)                            #
# --------------------------------------------------------------------------- #
def assign_block_ids(depths: list[int]) -> list[str]:
    """
    Walk an ordered list of section depths and return the `N-...-0` block ID
    (without caret) for each, enforcing depth discipline.

    depth 1 -> '1-0', '2-0', ...
    depth 2 under section 1 -> '1-1-0', '1-2-0', ...
    A depth may only descend one level at a time; skipping raises TagError.
    """
    counters: list[int] = []
    ids: list[str] = []
    for i, d in enumerate(depths):
        if d < 1:
            raise TagError(f"section {i}: depth must be >= 1, got {d}")
        if d > len(counters) + 1:
            raise TagError(
                f"section {i}: depth {d} skips a level "
                f"(current depth {len(counters)}). Depth may only increase by 1."
            )
        if d == len(counters) + 1:
            counters.append(1)            # descend exactly one level
        else:
            counters = counters[:d]       # ascend / stay
            counters[d - 1] += 1
        ids.append("-".join(str(c) for c in counters) + "-0")
    return ids


# --------------------------------------------------------------------------- #
# Anchored matching                                                            #
# --------------------------------------------------------------------------- #
def find_unique_line(lines: list[str], context: str, what: str) -> int:
    """Return the index of the single line containing `context`; error if 0/>1."""
    hits = [i for i, ln in enumerate(lines) if context in ln]
    if not hits:
        raise TagError(f"{what}: context not found in source:\n    {context!r}")
    if len(hits) > 1:
        raise TagError(
            f"{what}: context is ambiguous (matches {len(hits)} lines: "
            f"{[h + 1 for h in hits]}). Lengthen the context so it is unique:\n"
            f"    {context!r}"
        )
    return hits[0]


# --------------------------------------------------------------------------- #
# Edit model                                                                   #
# --------------------------------------------------------------------------- #
@dataclass
class LineEdits:
    """Pending edits for one source line."""
    headings: list[str] = field(default_factory=list)   # inserted BEFORE the line
    wraps: list[tuple[str, str]] = field(default_factory=list)  # (term, block_id)


def apply_wraps(line: str, wraps: list[tuple[str, str]]) -> str:
    """
    Wrap each (term, block_id) in `line` as [[#^block_id|term]].

    Multiple distinct terms are matched at their first occurrence; identical
    repeated terms are assigned to successive occurrences in document order.
    Overlapping wraps abort. The display text is exactly `term`, so unwrapping
    restores the original byte-for-byte.
    """
    # Resolve a concrete (start, end, term, id) span for every requested wrap.
    spans: list[tuple[int, int, str, str]] = []
    cursor_by_term: dict[str, int] = {}
    for term, block_id in wraps:
        if not term:
            raise TagError(f"empty term for block id {block_id}")
        start = line.find(term, cursor_by_term.get(term, 0))
        if start == -1:
            raise TagError(
                f"term {term!r} (-> ^{block_id}) not found in line:\n    {line!r}"
            )
        end = start + len(term)
        cursor_by_term[term] = end          # next identical term picks next occ.
        spans.append((start, end, term, block_id))

    spans.sort()
    # Reject overlaps.
    for (s1, e1, t1, _), (s2, e2, t2, _) in zip(spans, spans[1:]):
        if s2 < e1:
            raise TagError(
                f"overlapping wraps in one line: {t1!r} and {t2!r}:\n    {line!r}"
            )

    out, prev = [], 0
    for start, end, term, block_id in spans:
        out.append(line[prev:start])
        out.append(f"[[#^{block_id}|{term}]]")
        prev = end
    out.append(line[prev:])
    return "".join(out)


# --------------------------------------------------------------------------- #
# Core render                                                                  #
# --------------------------------------------------------------------------- #
def render(source: str, annot: dict) -> tuple[str, dict]:
    """Return (tagged_text, report). Raises TagError on any inconsistency."""
    sections = annot.get("sections")
    if not isinstance(sections, list) or not sections:
        raise TagError("annotation has no 'sections' list")

    depths = [int(s["depth"]) for s in sections]
    block_ids = assign_block_ids(depths)

    lines = source.splitlines()
    edits: dict[int, LineEdits] = {}

    def edits_for(idx: int) -> LineEdits:
        return edits.setdefault(idx, LineEdits())

    n_headings = n_self = n_announce = 0

    for sec, block_id in zip(sections, block_ids):
        title = sec.get("heading_title", "").strip()
        if not title:
            raise TagError(f"section ^{block_id} missing heading_title")
        body_ctx = sec.get("body_start_context", "")
        if not body_ctx:
            raise TagError(f"section ^{block_id} missing body_start_context")

        body_idx = find_unique_line(lines, body_ctx, f"section ^{block_id} body")
        heading_line = f"{heading_level(sec['depth'])} {title} ^{block_id}"
        edits_for(body_idx).headings.append(heading_line)
        n_headings += 1

        # 6b — self-referential restatement wikilink, on the body line.
        restate = sec.get("restatement")
        if restate:
            if restate not in lines[body_idx]:
                raise TagError(
                    f"section ^{block_id}: restatement {restate!r} not on body "
                    f"line:\n    {lines[body_idx]!r}"
                )
            edits_for(body_idx).wraps.append((restate, block_id))
            n_self += 1

        # 5 — announcement wikilink in the PARENT's enumeration sentence, which
        # points forward to THIS section's id.
        announced = sec.get("announced_in_parent")
        if announced:
            ctx = announced.get("context", "")
            term = announced.get("term", "")
            if not ctx or not term:
                raise TagError(
                    f"section ^{block_id}: announced_in_parent needs both "
                    f"'context' and 'term'"
                )
            anc_idx = find_unique_line(
                lines, ctx, f"section ^{block_id} announcement"
            )
            edits_for(anc_idx).wraps.append((term, block_id))
            n_announce += 1

    # Build the output, applying wraps then prepending headings per line.
    out_lines: list[str] = []
    for i, line in enumerate(lines):
        le = edits.get(i)
        new_line = apply_wraps(line, le.wraps) if le and le.wraps else line
        if le and le.headings:
            if out_lines and out_lines[-1].strip() != "":
                out_lines.append("")          # blank line before heading
            for h in le.headings:
                out_lines.append(h)
            out_lines.append("")              # blank line after heading
        out_lines.append(new_line)

    tagged = "\n".join(out_lines)
    if source.endswith("\n"):
        tagged += "\n"

    verify_prose_unchanged(source, tagged)

    report = {
        "sections": len(sections),
        "headings_inserted": n_headings,
        "self_restatements_tagged": n_self,
        "announcements_tagged": n_announce,
        "max_depth": max(depths),
        "block_ids": block_ids,
    }
    return tagged, report


# --------------------------------------------------------------------------- #
# Prose-integrity proof                                                        #
# --------------------------------------------------------------------------- #
def prose_signature(text: str, drop_headings: bool) -> list[str]:
    """
    Reduce text to the ordered list of non-blank prose lines, with wikilinks
    unwrapped and (optionally) inserted heading lines removed. Two texts with
    the same signature contain identical prose in identical order.
    """
    sig = []
    for ln in text.splitlines():
        if drop_headings and _HEADING_RE.match(ln):
            continue
        ln = unwrap_links(ln)
        if ln.strip() == "":
            continue
        sig.append(ln)
    return sig


def verify_prose_unchanged(source: str, tagged: str) -> None:
    """Assert tagged differs from source only by headings + link wrappers."""
    before = prose_signature(source, drop_headings=False)
    after = prose_signature(tagged, drop_headings=True)
    if before == after:
        return
    # Pinpoint the first divergence for a useful error.
    for i, (a, b) in enumerate(zip(before, after)):
        if a != b:
            raise TagError(
                "PROSE INTEGRITY VIOLATION at prose line "
                f"{i + 1}:\n  source: {a!r}\n  output: {b!r}"
            )
    raise TagError(
        "PROSE INTEGRITY VIOLATION: line count differs "
        f"(source {len(before)} prose lines, output {len(after)})."
    )


# --------------------------------------------------------------------------- #
# Output path handling                                                         #
# --------------------------------------------------------------------------- #
def derive_output_path(input_path: str) -> str:
    base = os.path.basename(input_path)
    out_dir = os.path.join("0-INBOX", "temp")
    candidate = os.path.join(out_dir, f"tagged-{base}")
    if not os.path.exists(candidate):
        return candidate
    stem, ext = os.path.splitext(candidate)
    v = 2
    while os.path.exists(f"{stem}-v{v}{ext}"):
        v += 1
    return f"{stem}-v{v}{ext}"


# --------------------------------------------------------------------------- #
# CLI                                                                          #
# --------------------------------------------------------------------------- #
def cmd_render(args: argparse.Namespace) -> int:
    with open(args.input, encoding="utf-8") as f:
        source = f.read()
    with open(args.annot, encoding="utf-8") as f:
        annot = json.load(f)

    tagged, report = render(source, annot)

    out_path = args.output or derive_output_path(args.input)
    os.makedirs(os.path.dirname(out_path) or ".", exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(tagged)

    print("tag-inline-toc render OK")
    print(f"  output:                  {out_path}")
    print(f"  sections:                {report['sections']}")
    print(f"  headings inserted:       {report['headings_inserted']}")
    print(f"  self-restatements tagged:{report['self_restatements_tagged']}")
    print(f"  announcements tagged:    {report['announcements_tagged']}")
    print(f"  max depth:               {report['max_depth']}")
    print("  prose integrity:         VERIFIED (no existing prose altered)")
    return 0


def cmd_verify(args: argparse.Namespace) -> int:
    with open(args.input, encoding="utf-8") as f:
        source = f.read()
    with open(args.tagged, encoding="utf-8") as f:
        tagged = f.read()
    verify_prose_unchanged(source, tagged)
    print("prose integrity: VERIFIED — tagged file alters no existing prose.")
    return 0


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description=__doc__,
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = p.add_subparsers(dest="cmd", required=True)

    pr = sub.add_parser("render", help="render an annotated commentary")
    pr.add_argument("--input", required=True)
    pr.add_argument("--annot", required=True)
    pr.add_argument("--output", default=None)
    pr.set_defaults(func=cmd_render)

    pv = sub.add_parser("verify", help="verify a tagged file vs its source")
    pv.add_argument("--input", required=True)
    pv.add_argument("--tagged", required=True)
    pv.set_defaults(func=cmd_verify)

    args = p.parse_args(argv)
    try:
        return args.func(args)
    except TagError as e:
        print(f"ERROR: {e}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
