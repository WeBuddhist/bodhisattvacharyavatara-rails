#!/usr/bin/env python3
"""Count Tibetan syllables in a text — used to enforce the syllable ceilings
in the BCA-Daily-Practice-Plan-HHDL skill (Section 4: <=300, Section 6
subsection 1: <=30).

Method: Tibetan syllables are tsheg-delimited units. This script strips
markdown scaffolding (headings, bold/italic markers, wikilinks, block-id
anchors) and Tibetan punctuation (tsheg, the various shad forms), then counts
the remaining whitespace/tsheg/shad-delimited chunks. This is an
approximation — good enough for a hard-ceiling check, but treat counts within
a syllable or two of the limit as "verify by eye", not gospel.

Usage:
    python3 count_syllables.py path/to/file.md
    python3 count_syllables.py -            # read from stdin
    echo "..." | python3 count_syllables.py -
"""
import sys
import re


def clean(text: str) -> str:
    text = re.sub(r"\[\[.*?\]\]", " ", text)          # wikilinks
    text = re.sub(r"\^[0-9]+-[0-9]+", " ", text)        # block-id anchors
    text = re.sub(r"[#>*_`]", " ", text)                # markdown scaffolding
    text = re.sub(r"^\s*-{3,}\s*$", " ", text, flags=re.MULTILINE)  # hr rules
    return text


def count_syllables(text: str) -> int:
    text = clean(text)
    # Tibetan tsheg U+0F0B, shad variants U+0F0D-U+0F0E, plus whitespace
    boundary = re.compile(r"[་།༎༌\s]+")
    parts = [p for p in boundary.split(text) if p.strip()]
    return len(parts)


def main() -> None:
    if len(sys.argv) != 2:
        print(__doc__)
        sys.exit(1)
    src = sys.argv[1]
    data = sys.stdin.read() if src == "-" else open(src, encoding="utf-8").read()
    print(count_syllables(data))


if __name__ == "__main__":
    main()
