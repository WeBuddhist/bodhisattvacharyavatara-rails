#!/usr/bin/env python3
"""Stage-0 pre-clean for Tibetan commentary segmentation.

Reverts an already-formatted commentary back to continuous prose so that
Stage-1 (segment_commentary.py) can re-derive block boundaries from scratch.
Removes editorial scaffolding only, never a character of body text:

  - index / outline numbers: a run of digits (ASCII 0-9 or Tibetan U+0F20-29),
    optional trailing "." or ")", standing alone between whitespace boundaries.
    Covers an OCR line counter on its own line AND an inline sequential outline
    number before a sa-bcad opener. Numbers glued to text are left untouched.
    Only numbers that fit a non-decreasing counter sequence across the file
    are removed; one that breaks the sequence is left in place and reported
    as FLAGGED_NUMBER, since it may be real content rather than scaffolding.
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
BARE_NUM_RE = re.compile(r"(?<!\S)[0-9༠-༩]+[.)]?(?!\S)")

SEP = "\n\n"


def count_syllables(text: str) -> int:
    return text.count(TSHEG) + (1 if text.strip() else 0)


def squeeze(s: str) -> str:
    return re.sub(r"\s+", "", s)


def strip_frontmatter(text: str) -> str:
    return FRONTMATTER_RE.sub("", text, count=1)


# --- safer number handling -------------------------------------------------
# BARE_NUM_RE used to be stripped unconditionally on the assumption every
# whitespace-bounded number is OCR scaffolding (a line counter or inline
# outline index). That can't distinguish scaffolding from a genuine content
# numeral (e.g. a verse number cited inline), and the old no-loss check
# couldn't catch a wrongful deletion since it was designed to permit number
# removal. Now: only numbers that fit a non-decreasing sequence across the
# file (the OCR-counter signature) are silently removed; anything that
# breaks that sequence is left in the text and surfaced in the report for a
# human to judge.
TIB_DIGITS = "༠༡༢༣༤༥༦༧༨༩"


def _num_value(token: str):
    core = token.rstrip(".)")
    if not core:
        return None
    digits = []
    for ch in core:
        if ch.isdigit():
            digits.append(ch)
        elif ch in TIB_DIGITS:
            digits.append(str(TIB_DIGITS.index(ch)))
        else:
            return None
    return int("".join(digits)) if digits else None


def _longest_nondecreasing_run(values):
    """Index set (into `values`) of one longest non-decreasing subsequence —
    the most plausible single OCR-counter run threaded through the file."""
    n = len(values)
    if n == 0:
        return set()
    dp = [1] * n
    prev = [-1] * n
    for i in range(n):
        for j in range(i):
            if values[j] <= values[i] and dp[j] + 1 > dp[i]:
                dp[i] = dp[j] + 1
                prev[i] = j
    best = max(range(n), key=lambda i: dp[i])
    keep, i = set(), best
    while i != -1:
        keep.add(i)
        i = prev[i]
    return keep


def strip_numbers(body: str):
    """Return (new_body, n_stripped, flagged) where flagged is a list of
    (token, context_preview) for numbers left in place because they broke
    the file's counter sequence."""
    matches = list(BARE_NUM_RE.finditer(body))
    parsed = [_num_value(m.group(0)) for m in matches]
    parsable_idx = [i for i, v in enumerate(parsed) if v is not None]
    keep_local = _longest_nondecreasing_run([parsed[i] for i in parsable_idx])
    keep_global = {parsable_idx[i] for i in keep_local}

    out, flagged, last = [], [], 0
    for i, m in enumerate(matches):
        out.append(body[last:m.start()])
        if i in keep_global:
            pass  # scaffolding -- drop it
        else:
            out.append(m.group(0))  # not part of the counter run -- keep it
            ctx_start, ctx_end = max(0, m.start() - 20), min(len(body), m.end() + 20)
            preview = body[ctx_start:ctx_end].replace("\n", " ").strip()
            flagged.append((m.group(0), preview))
        last = m.end()
    out.append(body[last:])
    return "".join(out), len(keep_global), flagged


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
              "suspect_headings": 0, "flagged_numbers": flagged_numbers}

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

    flagged_numbers = stats["flagged_numbers"]
    print(
        "{}: removed {} index/outline numbers, {} block IDs; "
        "kept markup on {} headings ({} suspect — bare-number heading text, "
        "check report); emitted {} blocks.".format(
            args.input, stats["numbers"], stats["block_ids"],
            stats["headings"], stats["suspect_headings"], len(blocks)
        )
    )
    if flagged_numbers:
        print(f"  {len(flagged_numbers)} number(s) left in place — broke the file's "
              f"counter sequence, may be real content. See report.")

    if args.report:
        with Path(args.report).open("w", encoding="utf-8") as fh:
            fh.write("index\tkind\tsyllables\tpreview\n")
            for i, (kind, txt) in enumerate(blocks, 1):
                preview = txt.strip()[:80].replace("\t", " ").replace("\n", "/")
                fh.write("{}\t{}\t{}\t{}\n".format(i, kind, count_syllables(txt), preview))
            for token, ctx in flagged_numbers:
                fh.write("FLAGGED_NUMBER\t{}\t-\t{}\n".format(
                    token, ctx.replace("\t", " ")))
        print("Report: " + args.report)

    if not args.dry_run:
        out = Path(args.output)
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(cleaned, encoding="utf-8")
        print("Wrote " + args.output)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
