#!/usr/bin/env python3
"""Stage-0 pre-clean for Tibetan commentary segmentation.

Reverts an already-formatted commentary back to continuous prose so that
Stage-1 (segment_commentary.py) can re-derive block boundaries from scratch.
Removes editorial scaffolding only, never a character of body text:

  - index / outline numbers: any whitespace-bounded token that consists solely
    of digits (ASCII 0-9 or Tibetan U+0F20-29) with optional internal dots
    (hierarchical numbers such as 4.11, 1.2.3) and an optional trailing "."
    or ")", is treated as scaffolding and removed unconditionally. Covers
    simple counters (1, 2, 3), terminated counters (1., 2.), section labels
    (4.11, 1.2.3.), and Tibetan-digit equivalents. Numbers fused to body text
    (e.g. "ལོ16") are left untouched.
  - block / verse IDs: Obsidian IDs such as ^0-1, ^1-2, ^1-2-0.
  - heading block IDs: a heading's trailing block ID is stripped, but the
    leading #/##/### markup and the heading text are both kept, on their own
    line, acting as a separator between prose runs.
  - intra-section line breaks: consecutive content lines within a section are
    joined into one continuous run. Kept heading-text lines act as separators.

Frontmatter is preserved verbatim and excluded from the no-loss comparison.

Usage:
    python3 preclean_commentary.py INPUT.md OUTPUT.md [--report REPORT.tsv]
                                   [--dry-run]
"""
from __future__ import annotations

import argparse
import re
import sys
import unicodedata
from pathlib import Path

TSHEG = "་"

# ── Botok-derived space normalisation ──────────────────────────────────────
# Adapted from OpenPecha/Botok botok/utils/corpus_normalization.py (MIT)
# https://github.com/OpenPecha/Botok/blob/master/botok/utils/corpus_normalization.py

_LINEBREAKS_RE = re.compile(r"\r\n?|| | ")

_ZERO_WIDTH_STRIP = dict.fromkeys(map(ord, [
    "​",  # ZERO WIDTH SPACE
    "⁠",  # WORD JOINER
    "﻿",  # ZERO WIDTH NO-BREAK SPACE / BOM
    "᠎",  # MONGOLIAN VOWEL SEPARATOR (deprecated)
    "͏",  # COMBINING GRAPHEME JOINER
]))

_SPACE_TO_ASCII = {ord(ch): " " for ch in [
    " ",  # NO-BREAK SPACE
    " ", " ", " ", " ", " ", " ",
    " ", " ", " ", " ", " ", " ",
    " ", " ", "　",  # narrow, medium, ideographic spaces
    "\t", "\x0b", "\x0c",          # TAB, VT, FF
]}

# Space after tsheg (U+0F0B/0F0C/0FD2) when followed by initial letter or shad
_TSHEG_SPACE_INITIAL_RE = re.compile(
    r"([་༌࿒]) +([ཀ-ཬ།-༑])"
)
# Space between final letter (U+0F40-0FBC) and tsheg
_LETTER_SPACE_TSHEG_RE = re.compile(
    r"([ཀ-ྼ]) +([་༌࿒])"
)


def normalize_spaces_tibetan(text: str) -> tuple[str, dict]:
    """Apply Botok-derived space normalisation; return (text, log).

    Log keys (int counts):
      linebreaks_normalised       – CRLF/CR/NEL/LS/PS converted to LF
      zero_width_removed          – zero-width / BOM chars stripped
      unicode_spaces_mapped       – non-ASCII spaces/tabs mapped to ASCII space
      tsheg_space_removed         – spaces between tsheg and following letter/shad
      letter_tsheg_space_removed  – spaces between final letter and tsheg
    """
    log = dict(linebreaks_normalised=0, zero_width_removed=0,
               unicode_spaces_mapped=0, tsheg_space_removed=0,
               letter_tsheg_space_removed=0)

    # Normalise non-LF line endings to LF
    log["linebreaks_normalised"] = len(_LINEBREAKS_RE.findall(text))
    text = _LINEBREAKS_RE.sub("\n", text)

    # Strip zero-width / BOM characters
    before_len = len(text)
    text = text.translate(_ZERO_WIDTH_STRIP)
    log["zero_width_removed"] = before_len - len(text)

    # Map Unicode spaces and tabs to ASCII space
    before = text
    text = text.translate(_SPACE_TO_ASCII)
    log["unicode_spaces_mapped"] = sum(1 for a, b in zip(before, text) if a != b)

    # Tibetan-specific: remove space after tsheg before letter/shad
    log["tsheg_space_removed"] = len(_TSHEG_SPACE_INITIAL_RE.findall(text))
    text = _TSHEG_SPACE_INITIAL_RE.sub(r"\1\2", text)

    # Tibetan-specific: remove space between final letter and tsheg
    log["letter_tsheg_space_removed"] = len(_LETTER_SPACE_TSHEG_RE.findall(text))
    text = _LETTER_SPACE_TSHEG_RE.sub(r"\1\2", text)

    return text, log

# ───────────────────────────────────────────────────────────────────────────

FRONTMATTER_RE = re.compile(r"^---\n.*?\n---\n", re.DOTALL)
BLOCK_ID_RE = re.compile(r"\s*\^[A-Za-z0-9_-]+")
# Widened: space after the hashes is optional (catches "##Heading" with no
# space, which the old \s+ requirement silently dropped into prose) and
# leading whitespace is unbounded (was capped at 0-3).
HEADING_RE = re.compile(r"^\s*#{1,6}\s*(.*)$")
# A heading whose captured text is itself just a bare number ("#1", "## 12)")
# is most likely OCR noise (a stray hash glued to a page/line counter), not a
# real editorial heading. Still treated as a heading (safe — text is kept,
# never deleted) but surfaced in the report instead of passing silently.
SUSPECT_HEADING_TEXT_RE = re.compile(r"^[0-9༠-༩]+[.)]?$")
BARE_NUM_RE = re.compile(r"(?<!\S)[0-9༠-༩]+(?:\.[0-9༠-༩]+)*[.)]?(?!\S)")

SEP = "\n\n"


def count_syllables(text: str) -> int:
    return text.count(TSHEG) + (1 if text.strip() else 0)


def squeeze(s: str) -> str:
    return re.sub(r"\s+", "", s)


def strip_frontmatter(text: str) -> str:
    return FRONTMATTER_RE.sub("", text, count=1)


def strip_numbers(body: str):
    """Return (new_body, n_stripped, flagged).

    All whitespace-bounded index/outline numbers matched by BARE_NUM_RE are
    removed unconditionally. This includes simple counters (1, 2.), terminated
    counters (3.), and hierarchical section labels (4.11, 1.2.3.). The
    `flagged` list is always empty (retained for API compatibility).
    """
    matches = list(BARE_NUM_RE.finditer(body))
    out, last = [], 0
    for m in matches:
        out.append(body[last:m.start()])
        last = m.end()
    out.append(body[last:])
    return "".join(out), len(matches), []


def process(text: str):
    fm = FRONTMATTER_RE.match(text)
    if fm:
        head = fm.group(0).rstrip("\n")
        body = text[fm.end():]
    else:
        head = None
        body = text

    n_block_ids = len(BLOCK_ID_RE.findall(body))
    body = BLOCK_ID_RE.sub("", body)
    body, n_numbers, flagged_numbers = strip_numbers(body)
    expected_body = body  # snapshot for the no-loss check, before line-reflow

    blocks = []
    buf = []
    stats = {"numbers": n_numbers, "headings": 0, "block_ids": n_block_ids,
              "suspect_headings": 0}

    def flush():
        if buf:
            run = re.sub(r"\s+", " ", " ".join(s.strip() for s in buf)).strip()
            # Normalize: insert space after shad/nyis-shad when followed directly
            # by Tibetan content (no space). OCR sources often omit this space.
            # U+0F0D=shad, U+0F0E=nyis-shad, U+0F0B=tsheg, U+0F0C=delimiter.
            run = re.sub("([།༎])([^\s།༎་༌])",
                         r"\1 \2", run)
            if run:
                blocks.append(("prose", run))
            buf.clear()

    for ln in body.split("\n"):
        m = HEADING_RE.match(ln)
        if m:
            flush()
            htext = ln.strip()
            if htext:
                if SUSPECT_HEADING_TEXT_RE.match(m.group(1).strip()):
                    blocks.append(("heading-suspect", htext))
                    stats["suspect_headings"] += 1
                else:
                    blocks.append(("heading", htext))
                stats["headings"] += 1
            continue
        if ln.strip():
            buf.append(ln)
    flush()

    out = []
    if head:
        out.append(head)
    out.extend(b[1] for b in blocks)
    text_out = SEP.join(out) + "\n"
    return text_out, blocks, stats, expected_body


def assert_no_loss(expected_body: str, cleaned: str):
    if squeeze(expected_body) != squeeze(strip_frontmatter(cleaned)):
        sys.exit("ABORT: pre-clean altered body text. No file written.")


def main(argv):
    ap = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    ap.add_argument("input")
    ap.add_argument("output")
    ap.add_argument("--report", help="write a TSV report of the cleaned blocks here")
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args(argv[1:])

    raw = Path(args.input).read_text(encoding="utf-8")
    raw, space_log = normalize_spaces_tibetan(raw)
    text = unicodedata.normalize("NFC", raw)
    cleaned, blocks, stats, expected_body = process(text)
    assert_no_loss(expected_body, cleaned)

    print(
        "{}: removed {} index/outline numbers, {} block IDs; "
        "kept markup on {} headings ({} suspect — bare-number heading text, "
        "check report); emitted {} blocks.".format(
            args.input, stats["numbers"], stats["block_ids"],
            stats["headings"], stats["suspect_headings"], len(blocks)
        )
    )
    print(
        "  space normalisation: {} linebreak(s) normalised, "
        "{} zero-width char(s) removed, "
        "{} unicode space(s) mapped to ASCII, "
        "{} tsheg-space(s) removed, "
        "{} letter-tsheg space(s) removed.".format(
            space_log["linebreaks_normalised"],
            space_log["zero_width_removed"],
            space_log["unicode_spaces_mapped"],
            space_log["tsheg_space_removed"],
            space_log["letter_tsheg_space_removed"],
        )
    )

    if args.report:
        with Path(args.report).open("w", encoding="utf-8") as fh:
            fh.write("index\tkind\tsyllables\tpreview\n")
            for i, (kind, txt) in enumerate(blocks, 1):
                preview = txt.strip()[:80].replace("\t", " ").replace("\n", "/")
                fh.write("{}\t{}\t{}\t{}\n".format(i, kind, count_syllables(txt), preview))
            # Append space-normalisation summary as a trailing comment block
            fh.write("\n# space_normalisation_summary\n")
            for k, v in space_log.items():
                fh.write("#\t{}\t{}\n".format(k, v))
        print("Report: " + args.report)

    if not args.dry_run:
        out = Path(args.output)
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(cleaned, encoding="utf-8")
        print("Wrote " + args.output)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
