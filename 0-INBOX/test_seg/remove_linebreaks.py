#!/usr/bin/env python3
"""
remove_linebreaks.py
Removes soft PDF-extraction linebreaks from a Tibetan text file by joining
all non-blank lines directly (no space inserted — Tibetan syllables are
already delimited by tshegs).

Input:  bo-རྒྱལ་བ་རིན་པོ་ཆེ།_extracted.md
Output: bo-རྒྱལ་བ་རིན་པོ་ཆེ།_joined.md  (same folder)

Run from any directory:
    python remove_linebreaks.py
"""

from pathlib import Path

INPUT  = Path(__file__).parent / "bo-རྒྱལ་བ་རིན་པོ་ཆེ།_extracted.md"
OUTPUT = INPUT.with_name(INPUT.stem.replace("_extracted", "_joined") + INPUT.suffix)

text  = INPUT.read_text(encoding="utf-8")
lines = text.splitlines()

# Strip trailing/leading whitespace from each line; skip blank lines; join directly
joined = "".join(line.strip() for line in lines if line.strip())

OUTPUT.write_text(joined, encoding="utf-8")

print(f"Input : {INPUT.name}  ({len(lines):,} lines)")
print(f"Output: {OUTPUT.name}  (1 line, {len(joined):,} chars)")
