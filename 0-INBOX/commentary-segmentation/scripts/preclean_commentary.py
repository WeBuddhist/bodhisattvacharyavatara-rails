#!/usr/bin/env python3
"""Stage-0 pre-clean for Tibetan commentary segmentation.

Reverts an already-formatted commentary back to continuous prose so that
Stage-1 (segment_commentary.py) can re-derive block boundaries from scratch.
Removes editorial scaffolding only, never a character of body text:

  - git conflict markers: lines beginning with 7+ consecutive '<', '=', or '>'
    characters (e.g. "<<<<<<< HEAD", "=======",
    ">>>>>>>> c4296023...:1-SOURCES/Commentaries/BCAC14_SMPLG_bo.md").
    Entire line is removed unconditionally — these are never body text.
  - blockquote prefixes: leading '>' characters (1–6) plus an optional space
    are stripped from each line. The text content of the line is kept and
    flows into the prose run.
  - bare heading markers: a line consisting solely of '#' characters (with no
    heading text) is dropped entirely — it is scaffolding, not a real heading.
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

# Git conflict marker lines: 7+ consecutive '<', '=', or '>' at line start,
# optionally followed by any text (commit hash, branch name, file path, etc.).
# Matches all three marker types:
#   <<<<<<< HEAD  /  <<<<<<< branch-name
#   =======
#   >>>>>>> commit:path  /  >>>>>>>> commit:path
GIT_MARKER_RE = re.compile(r"^(?:<{7,}|={7,}|>{7,}).*$", re.MULTILINE)

# Blockquote prefix: 1–6 '>' characters (anything beyond 6 is a git marker
# caught above) plus an optional single space. The text after is body content.
BLOCKQUOTE_RE = re.compile(r"^>{1,6} ?", re.MULTILINE)

# Bare heading markers — a line that is only '#' characters with no text body.
# These carry no content and must be dropped before the no-loss snapshot.
BARE_HEADING_RE = re.compile(r"^#{1,6}\s*$", re.MULTILINE)

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

    # --- Scaffolding removal (all before the no-loss snapshot) ---

    # 1. Git conflict markers — entire lines, never body text.
    n_git_markers = len(GIT_MARKER_RE.findall(body))
    body = GIT_MARKER_RE.sub("", body)

    # 2. Blockquote '>' prefixes — strip the prefix, keep the text content.
    n_blockquotes = len(BLOCKQUOTE_RE.findall(body))
    body = BLOCKQUOTE_RE.sub("", body)

    # 3. Bare heading markers ('#' with no text) — no content, drop entirely.
    n_bare_headings = len(BARE_HEADING_RE.findall(body))
    body = BARE_HEADING_RE.sub("", body)

    # 4. Obsidian block / verse IDs.
    n_block_ids = len(BLOCK_ID_RE.findall(body))
    body = BLOCK_ID_RE.sub("", body)

    # 5. Index / outline numbers.
    body, n_numbers, flagged_numbers = strip_numbers(body)

    expected_body = body  # snapshot for the no-loss check, before line-reflow

    blocks = []
    buf = []
    stats = {
        "numbers": n_numbers,
        "headings": 0,
        "block_ids": n_block_ids,
        "suspect_headings": 0,
        "bare_headings": n_bare_headings,
        "blockquotes": n_blockquotes,
        "git_markers": n_git_markers,
    }

    def flush():
        if buf:
            run = re.sub(r"\s+", " ", " ".join(s.strip() for s in buf)).strip()
            # Rule 1: remove spurious spaces after tsheg (་).
            # ་ connects syllables within a word; a space after it is always a
            # line-break artifact introduced by joining, never legitimate text.
            run = re.sub(r"་ +", "་", run)
            # Rule 2: insert space after shad/nyis-shad when followed directly
            # by Tibetan content (no space). OCR sources often omit this space.
            # ། །ན is handled correctly: the internal space is preserved by the
            # \s+ step above, and only the missing space after the second །
            # is inserted here. །། (no-space nyis-shad) is left untouched
            # because the character class excludes [།༎].
            # U+0F0D=shad, U+0F0E=nyis-shad, U+0F0B=tsheg, U+0F0C=delimiter.
            run = re.sub(r"([།༎])([^\s།༎་༌])", r"\1 \2", run)
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

    text = unicodedata.normalize("NFC", Path(args.input).read_text(encoding="utf-8"))
    cleaned, blocks, stats, expected_body = process(text)
    assert_no_loss(expected_body, cleaned)

    print(
        "{}: removed {} git-conflict markers, {} blockquote prefixes, "
        "{} bare headings, {} index/outline numbers, {} block IDs; "
        "kept markup on {} headings ({} suspect); emitted {} blocks.".format(
            args.input,
            stats["git_markers"], stats["blockquotes"], stats["bare_headings"],
            stats["numbers"], stats["block_ids"],
            stats["headings"], stats["suspect_headings"], len(blocks),
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
