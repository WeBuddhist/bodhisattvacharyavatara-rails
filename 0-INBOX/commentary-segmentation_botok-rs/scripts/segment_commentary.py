#!/usr/bin/env python3
"""Stage-1 botok-rs segmentation for Tibetan commentary.

Segmentation is driven entirely by botok_rs.WordTokenizer + sentence_tokenize():
each botok-rs sentence becomes one block. No rule-based post-processing is
applied — quote frames, ordinal/enumeration splits, verse detection, and
syllable-cap splitting are intentionally NOT performed here.

Requires:
    pip install git+https://github.com/OpenPecha/botok-rs.git

Usage:
    python3 segment_commentary.py INPUT.md OUTPUT.md [--report REPORT.tsv]
                                  [--dry-run]
"""
from __future__ import annotations

import argparse
import re
import sys
import unicodedata
from pathlib import Path

try:
    from botok_rs import WordTokenizer, sentence_tokenize
except ImportError:
    sys.exit(
        "ERROR: botok_rs is not installed.\n"
        "Install it with:\n"
        "  pip install git+https://github.com/OpenPecha/botok-rs.git"
    )

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------
TSHEG = "་"   # U+0F0B

SEP = "\n\n"
HEADING_RE     = re.compile(r"^#{1,6}\s")
FRONTMATTER_RE = re.compile(r"^---\n.*?\n---\n", re.DOTALL)


def count_syllables(text: str) -> int:
    return text.count(TSHEG) + (1 if text.strip() else 0)


# ---------------------------------------------------------------------------
# No-loss assertion
# ---------------------------------------------------------------------------

_WS_TABLE = str.maketrans("", "", "".join(chr(c) for c in (
    0x20, 0x09, 0x0A, 0x0D, 0x0C, 0x0B,
    0xA0, 0x1680,
    0x2000, 0x2001, 0x2002, 0x2003, 0x2004,
    0x2005, 0x2006, 0x2007, 0x2008, 0x2009, 0x200A,
    0x2028, 0x2029,
    0x202F, 0x205F,
    0x3000,
)))


def _squeeze(s: str) -> str:
    return s.translate(_WS_TABLE)


def assert_no_loss(original: str, segmented: str):
    if _squeeze(original) != _squeeze(segmented):
        sys.exit("ABORT: segmentation altered non-whitespace content. No file written.")


# ---------------------------------------------------------------------------
# Module-level tokenizer — initialised lazily on first process() call
# ---------------------------------------------------------------------------
_wt: WordTokenizer | None = None


def _get_tokenizer() -> WordTokenizer:
    global _wt
    if _wt is None:
        _wt = WordTokenizer()   # auto-downloads "general" dialect pack on first use
    return _wt


# ---------------------------------------------------------------------------
# Main processing
# ---------------------------------------------------------------------------

def process(text: str):
    """Segment *text* by botok-rs sentence boundaries only.

    Returns (segmented_text, report). *report* is a list of dicts:
    trigger, syllables, preview.
    """
    wt = _get_tokenizer()

    out_parts: list[str] = []
    report: list[dict] = []

    fm = FRONTMATTER_RE.match(text)
    if fm:
        out_parts.append(fm.group(0).rstrip("\n"))
        body = text[fm.end():]
    else:
        body = text

    for para in re.split(r"\n\s*\n", body):
        if not para.strip():
            continue
        if HEADING_RE.match(para.strip()):
            out_parts.append(para.strip())
            continue

        tokens = wt.tokenize(para)
        sentences = sentence_tokenize(tokens)
        raw_sentences = [s.text() for s in sentences] if sentences else [para]

        for sent_text in raw_sentences:
            sent_text = sent_text.strip()
            if not sent_text:
                continue
            out_parts.append(sent_text)
            report.append({
                "trigger": "botok-sentence",
                "syllables": count_syllables(sent_text),
                "preview": sent_text[:80].replace("\t", " ").replace("\n", "↵"),
            })

    return SEP.join(out_parts) + "\n", report


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main(argv):
    ap = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    ap.add_argument("input")
    ap.add_argument("output")
    ap.add_argument("--report", help="write a TSV segmentation report here")
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args(argv[1:])

    text = unicodedata.normalize("NFC", Path(args.input).read_text(encoding="utf-8"))
    segmented, report = process(text)
    assert_no_loss(text, segmented)

    n_segments = len(report)
    print(f"{args.input}: {n_segments} segments (botok-rs sentences).")

    if args.report:
        with Path(args.report).open("w", encoding="utf-8") as fh:
            fh.write("index\ttrigger\tsyllables\tpreview\n")
            for i, r in enumerate(report, 1):
                fh.write(f"{i}\t{r['trigger']}\t{r['syllables']}\t{r['preview']}\n")
        print(f"Report: {args.report}")

    if not args.dry_run:
        out = Path(args.output)
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(segmented, encoding="utf-8")
        print(f"Wrote {args.output}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
