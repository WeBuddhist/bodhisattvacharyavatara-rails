#!/usr/bin/env python3
"""Stage-0 pre-clean for Tibetan commentary segmentation.

Reverts an already-formatted commentary back to continuous prose so that
Stage-1 (segment_commentary.py) can re-derive block boundaries from scratch.
Removes editorial scaffolding only, never a character of body text:

  - index / outline numbers: one or more dot-separated digit groups (ASCII
    0-9 or Tibetan U+0F20-29), e.g. "7", "1.1", "2.9", optional trailing "."
    or ")", standing alone between whitespace boundaries. Covers an OCR line
    counter on its own line AND an inline sequential outline number before a
    sa-bcad opener (including chapter.verse-style counters like "1.1"/"2.9").
    Numbers glued to text are left untouched.
  - block / verse IDs: Obsidian IDs such as ^0-1, ^1-2, ^1-2-0.
  - legacy running-header page markers: a scanned-page artifact of the form
    "-7-" (a page number wrapped in bare hyphens, never whitespace-bounded
    digits alone, so the index-number rule above can't see it). When the
    marker is immediately followed by a running-header token rendered in a
    legacy non-Unicode Tibetan font (surfaces as Latin-1/Latin-Extended
    mojibake, e.g. "-7- uôh-ºWâG-Vïm-¤ôºÛ-z;º-FÛh-¸Ûm-ƒÛÅü"), the marker and
    that token are removed together. A bare marker with no such token (or
    with real Tibetan text immediately after it) has only the marker
    removed -- the rule only ever deletes a token that contains zero
    Tibetan characters, so genuine body text immediately after a page break
    is never touched.
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

# Index / outline numbers: one or more dot-separated digit groups
# ("7", "1.1", "2.9", "11.1.2", ...), optional trailing "." or ")",
# standing alone between whitespace boundaries.
BARE_NUM_RE = re.compile(r"(?<!\S)[0-9༠-༩]+(?:\.[0-9༠-༩]+)*[.)]?(?!\S)")

# Tibetan Unicode block (U+0F00-U+0FFF) -- used to confirm a token is NOT
# genuine body text.
_TIBETAN = "ༀ-࿿"

# Codepoints that show up in this corpus's legacy (non-Unicode) Tibetan font
# encoding once mis-rendered as Latin text: Latin-1 Supplement (U+00A0-00FF),
# Latin Extended-A's Y-with-diaeresis (U+0178), Latin Extended-B's f-with-hook
# (U+0192), the spacing modifier circumflex (U+02C6), and the General
# Punctuation low-9 quote (U+201A). Real Tibetan commentary prose never
# contains these, so their presence -- combined with the total absence of
# any Tibetan character in the same token -- is the signal that a token is
# OCR page furniture, not content.
_LEGACY_GLYPH = " -ÿŸƒˆ‚"

# A legacy running-header token: a single whitespace-delimited run with zero
# Tibetan characters that contains at least one legacy-font glyph.
_LEGACY_TOKEN = (
    r"(?:[^{tib}\s])*[{glyph}](?:[^{tib}\s])*"
).format(tib=_TIBETAN, glyph=_LEGACY_GLYPH)

# Legacy running-header page marker: a bare "-N-" (hyphen-wrapped page
# number, so the whitespace-bounded BARE_NUM_RE above can't match it) with
# an optional immediately-following legacy-font header token. The header
# token is only consumed if it actually looks like legacy-font mojibake;
# real Tibetan text right after a page break is left untouched.
HEADER_MARKER_RE = re.compile(
    r"(?<!\S)-[0-9]{{1,4}}-(?:[ \t]+{token})?(?!\S)".format(token=_LEGACY_TOKEN)
)

SEP = "\n\n"


def count_syllables(text: str) -> int:
    return text.count(TSHEG) + (1 if text.strip() else 0)


def squeeze(s: str) -> str:
    return re.sub(r"\s+", "", s)


def strip_frontmatter(text: str) -> str:
    return FRONTMATTER_RE.sub("", text, count=1)


def reference_body(text: str) -> str:
    t = BLOCK_ID_RE.sub("", text)
    t = HEADER_MARKER_RE.sub("", t)
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
    n_headers = len(HEADER_MARKER_RE.findall(body))
    body = HEADER_MARKER_RE.sub("", body)
    n_numbers = len(BARE_NUM_RE.findall(body))
    body = BARE_NUM_RE.sub("", body)

    blocks = []
    buf = []
    stats = {
        "numbers": n_numbers,
        "headings": 0,
        "block_ids": n_block_ids,
        "headers": n_headers,
    }

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
        "{}: removed {} index/outline numbers, {} block IDs, {} legacy "
        "running-header markers; kept markup on {} headings; emitted {} "
        "blocks.".format(
            args.input, stats["numbers"], stats["block_ids"],
            stats["headers"], stats["headings"], len(blocks)
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
