#!/usr/bin/env python3
"""Stage-0 pre-clean for Tibetan commentary segmentation.

Reverts an already-formatted commentary back to continuous prose so that
Stage-1 (segment_commentary.py) can re-derive block boundaries from scratch.
Removes editorial scaffolding only, never a character of body text:

  - index / outline numbers: a run of digits (ASCII 0-9 or Tibetan U+0F20-29),
    optional trailing "." or ")", standing alone between whitespace boundaries.
    Covers an OCR line counter on its own line AND an inline sequential outline
    number before a sa-bcad opener. Numbers glued to text are left untouched.
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
from pathlib import Path

TSHEG = "་"

FRONTMATTER_RE = re.compile(r"^---\n.*?\n---\n", re.DOTALL)
BLOCK_ID_RE = re.compile(r"\s*\^[A-Za-z0-9_-]+")
HEADING_RE = re.compile(r"^\s{0,3}#{1,6}\s+(.*)$")
BARE_NUM_RE = re.compile(r"(?<!\S)[0-9༠-༩]+[.)]?(?!\S)")

SEP = "\n\n"


def count_syllables(text: str) -> int:
    return text.count(TSHEG) + (1 if text.strip() else 0)


def squeeze(s: str) -> str:
    return re.sub(r"\s+", "", s)


def strip_frontmatter(text: str) -> str:
    return FRONTMATTER_RE.sub("", text, count=1)


def reference_body(text: str) -> str:
    t = BLOCK_ID_RE.sub("", text)
    t = BARE_NUM_RE.sub("", t)
    return squeeze(t)


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
    n_numbers = len(BARE_NUM_RE.findall(body))
    body = BARE_NUM_RE.sub("", body)

    blocks = []
    buf = []
    stats = {"numbers": n_numbers, "headings": 0, "block_ids": n_block_ids}

    def flush():
        if buf:
            run = re.sub(r"\s+", " ", " ".join(s.strip() for s in buf)).strip()
            if run:
                blocks.append(("prose", run))
            buf.clear()

    for ln in body.split("\n"):
        m = HEADING_RE.match(ln)
        if m:
            flush()
            htext = ln.strip()
            if htext:
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
    return text_out, blocks, stats


def assert_no_loss(original: str, cleaned: str):
    if reference_body(strip_frontmatter(original)) != squeeze(strip_frontmatter(cleaned)):
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

    text = Path(args.input).read_text(encoding="utf-8")
    cleaned, blocks, stats = process(text)
    assert_no_loss(text, cleaned)

    print(
        "{}: removed {} index/outline numbers, {} block IDs; "
        "kept markup on {} headings; emitted {} blocks.".format(
            args.input, stats["numbers"], stats["block_ids"],
            stats["headings"], len(blocks)
        )
    )

    if args.report:
        with Path(args.report).open("w", encoding="utf-8") as fh:
            fh.write("index\tkind\tsyllables\tpreview\n")
            for i, (kind, txt) in enumerate(blocks, 1):
                preview = txt.strip()[:80].replace("\t", " ").replace("\n", "/")
                fh.write("{}\t{}\t{}\t{}\n".format(i, kind, count_syllables(txt), preview))
        print("Report: " + args.report)

    if not args.dry_run:
        out = Path(args.output)
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(cleaned, encoding="utf-8")
        print("Wrote " + args.output)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
