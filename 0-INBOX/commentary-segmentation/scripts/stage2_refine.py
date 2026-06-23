#!/usr/bin/env python3
"""Stage-2 semantic refinement for གཅེས་བཏུས commentary segmentation.

Applies two targeted changes to the Stage-1 output (གཅེས་བཏུས.segmented.md):

1. Lead-in + stanza splits (2 blocks):
   Blocks that have a short non-pāda lead-in (< 6 syllables) on the first line
   followed by 4 pāda-length lines (6-11 syl each, ±1 uniform) are the result
   of _attach_leadins() joining a citation lead-in to a verse stanza. These are
   split at the first \\n (lead-in on its own paragraph, stanza as its own paragraph).

2. Everything else: left intact.
   - Pure verse stanzas (4 × 11 syl, already ≤ 41 total): protected, leave whole.
   - Over-long prose blocks with single terminal shad: genuinely indivisible
     single clauses — no internal shad to split on. Over-long is safer than wrong.

No character of body text is altered — only paragraph boundaries are inserted.
"""
from __future__ import annotations

import re
import sys
import unicodedata
from pathlib import Path

TSHEG = "་"
SHAD = "།"
NYIS_SHAD = "༎"
FRONTMATTER_RE = re.compile(r"^---\n.*?\n---\n", re.DOTALL)

# Same squeeze function as segment_commentary.py for no-loss check
_WS_TABLE = str.maketrans("", "", "".join(chr(c) for c in (
    0x20, 0x09, 0x0A, 0x0D, 0x0C, 0x0B,
    0xA0, 0x1680,
    0x2000, 0x2001, 0x2002, 0x2003, 0x2004,
    0x2005, 0x2006, 0x2007, 0x2008, 0x2009, 0x200A,
    0x2028, 0x2029,
    0x202F, 0x205F,
    0x3000,
)))


def squeeze(s: str) -> str:
    return s.translate(_WS_TABLE)


def count_syllables(text: str) -> int:
    return text.count(TSHEG) + (1 if text.strip() else 0)


def is_pada_unit(s: str) -> bool:
    return 6 <= count_syllables(s.strip()) <= 11


def is_uniform_stanza(lines: list[str]) -> bool:
    if not (2 <= len(lines) <= 4):
        return False
    if not all(is_pada_unit(l) for l in lines):
        return False
    syls = [count_syllables(l.strip()) for l in lines]
    return max(syls) - min(syls) <= 1


def is_leadin_stanza(block: str) -> bool:
    """Return True if block = short lead-in + N-pāda stanza (should be split)."""
    lines = [l for l in block.strip().split("\n") if l.strip()]
    if len(lines) < 3:
        return False
    first = lines[0]
    rest = lines[1:]
    # First line must be a non-pāda (short) lead-in
    if is_pada_unit(first):
        return False
    # Rest must form a valid stanza
    return is_uniform_stanza(rest)


def process(text: str) -> tuple[str, int]:
    """Return (refined_text, n_splits)."""
    fm = FRONTMATTER_RE.match(text)
    if fm:
        head = fm.group(0).rstrip("\n")
        body = text[fm.end():]
    else:
        head = None
        body = text

    paras = re.split(r"\n\n", body)
    out = []
    n_splits = 0
    for para in paras:
        if not para.strip():
            out.append(para)
            continue
        if is_leadin_stanza(para):
            # Split at first \n: lead-in gets own paragraph, stanza keeps its own \n structure
            first_nl = para.index("\n")
            lead = para[:first_nl]
            stanza = para[first_nl + 1:]
            out.append(lead)
            out.append(stanza)
            n_splits += 1
        else:
            out.append(para)

    result = "\n\n".join(out)
    if head:
        return result + "\n", n_splits
    return result + "\n", n_splits


def main(argv: list[str]) -> int:
    if len(argv) < 3:
        print(f"Usage: {argv[0]} INPUT.md OUTPUT.md [--dry-run]", file=sys.stderr)
        return 1
    src = Path(argv[1])
    dst = Path(argv[2])
    dry_run = "--dry-run" in argv

    text = unicodedata.normalize("NFC", src.read_text(encoding="utf-8"))
    refined, n_splits = process(text)

    # No-loss check: squeeze of output must equal squeeze of input
    if squeeze(text) != squeeze(refined):
        print("ABORT: Stage-2 altered non-whitespace content. No file written.", file=sys.stderr)
        return 1

    print(f"Stage-2 complete: {n_splits} lead-in/stanza split(s) applied.")
    print("No-loss check: PASSED")

    if not dry_run:
        dst.parent.mkdir(parents=True, exist_ok=True)
        dst.write_text(refined, encoding="utf-8")
        print(f"Wrote {dst}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
