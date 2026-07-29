#!/usr/bin/env python3
"""Lint a verse-translation file for rails-to-verse-translation (Step 7).

Checks structure (verse count, numbering contiguity, lines per verse, caesura,
terminal mark, line-ending whitespace), termbase compliance (locked renderings
present, forbidden variants absent), and script hygiene (no stray Latin text,
no stray numerals that could be mistaken for verse markers).

Run from the vault root.

    python3 lint_verses.py --file <verse-file> --termbase <termbase.md> --range 2-25-2-50

Exit status 0 = clean, 1 = errors found.
"""
import argparse
import re
import sys

NUMERALS = {
    "devanagari": "०१२३४५६७८९",
    "latin": "0123456789",
    "bengali": "০১২৩৪৫৬৭৮৯",
    "tibetan": "༠༡༢༣༤༥༦༧༨༩",
}
TERMINALS = "॥|｜。"


def detect_numerals(text):
    for name, digits in NUMERALS.items():
        if re.search(r"\*\*\([" + re.escape(digits) + r"]+\)\*\*", text):
            return name, digits
    return None, None


def to_int(s, digits):
    return int("".join(str(digits.index(c)) for c in s))


def parse_range(spec):
    m = re.match(r"^(\d+)-(\d+)-(?:\1-)?(\d+)$", spec)
    if not m:
        sys.exit(f"could not parse --range {spec!r}; use e.g. 2-25-2-50")
    return int(m.group(1)), int(m.group(2)), int(m.group(3))


def parse_termbase(path):
    """Locked renderings from column 2, forbidden variants from a 'never write' table."""
    locked, forbidden = [], []
    if not path:
        return locked, forbidden
    for line in open(path, encoding="utf-8"):
        cells = [c.strip() for c in line.strip().strip("|").split("|")] if "|" in line else []
        if len(cells) < 2:
            continue
        m = re.search(r"\*\*(.+?)\*\*", cells[1])
        if not m:
            continue
        term = m.group(1).strip()
        if term.lower() in {"locked hindi", "gloss"}:
            continue
        # a "never write" column marks forbidden variants
        if len(cells) >= 3 and re.search(r"never|न लिखें", line, re.I):
            forbidden += [x.strip() for x in re.split(r"[,،]", cells[-1]) if x.strip()]
        for alt in re.split(r"\s*/\s*", term):
            alt = alt.strip()
            if alt:
                locked.append(alt)
    return sorted(set(locked)), sorted(set(forbidden))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--file", required=True)
    ap.add_argument("--termbase")
    ap.add_argument("--range", required=True, help="e.g. 2-25-2-50")
    ap.add_argument("--lines-per-verse", type=int, default=4)
    args = ap.parse_args()

    ch, first, last = parse_range(args.range)
    text = open(args.file, encoding="utf-8").read()
    body = text.split("---", 2)[2] if text.startswith("---") else text

    errors, warnings = [], []

    kind, digits = detect_numerals(body)
    if not kind:
        print("FAIL: no verse markers of the form **(N)** found")
        return 1
    print(f"numeral system    : {kind}")

    blocks = re.findall(
        r"\*\*\(([" + re.escape(digits) + r"]+)\)\*\*\n((?:.*\n)*?)(?=\n\*\*\(|\Z)", body
    )
    nums = [to_int(n, digits) for n, _ in blocks]
    expected = list(range(first, last + 1))

    print(f"verses found      : {len(blocks)} (expected {len(expected)})")
    if nums != expected:
        missing = [n for n in expected if n not in nums]
        extra = [n for n in nums if n not in expected]
        dupes = sorted({n for n in nums if nums.count(n) > 1})
        if missing:
            errors.append(f"missing verses: {missing}")
        if extra:
            errors.append(f"unexpected verses: {extra}")
        if dupes:
            errors.append(f"duplicate verse numbers: {dupes}")
        if not (missing or extra or dupes):
            errors.append(f"verses out of order: {nums}")

    for n, blk in blocks:
        i = to_int(n, digits)
        lines = [l for l in blk.strip("\n").split("\n") if l.strip()]
        lines = [re.sub(r"\s*\^\d+-\d+\s*$", "", l) for l in lines]
        if len(lines) != args.lines_per_verse:
            errors.append(f"verse {i}: {len(lines)} lines, expected {args.lines_per_verse}")
            continue
        if not re.search(r"[" + TERMINALS + r"]\s*$", lines[-1]):
            errors.append(f"verse {i}: final line lacks a terminal mark")
        for j, l in enumerate(lines[:-1]):
            if not l.endswith(" "):
                warnings.append(f"verse {i} line {j+1}: no trailing space (markdown line break)")
        for j, l in enumerate(lines):
            if "," not in l and "—" not in l and "|" not in l:
                warnings.append(f"verse {i} line {j+1}: no caesura")
        if re.search(r"[" + TERMINALS + r"]", "".join(lines[:-1])):
            errors.append(f"verse {i}: terminal mark appears before the final line")

    locked, forbidden = parse_termbase(args.termbase)
    if locked:
        absent = [t for t in locked if t not in body]
        print(f"termbase          : {len(locked)} locked renderings, {len(absent)} unused in range")
        present_forbidden = [f for f in forbidden if f and f in body]
        for f in present_forbidden:
            errors.append(f"forbidden variant present: {f!r}")

    latin = re.findall(r"[A-Za-z]{2,}", body)
    if latin:
        warnings.append(f"Latin-script words in verse body: {sorted(set(latin))[:8]}")

    stripped = re.sub(r"^\*\*\([^)]+\)\*\*$", "", body, flags=re.M)
    stripped = re.sub(r"^#.*$", "", stripped, flags=re.M)
    stray = re.findall(r"[" + re.escape(digits) + r"]+", stripped)
    if stray:
        warnings.append(f"stray {kind} numerals inside verse text: {sorted(set(stray))}")

    ids = re.findall(r"\^(\d+)-(\d+)", body)
    if ids:
        orphan = re.findall(r"^\^\d+-\d+\s*$", body, re.M)
        if orphan:
            errors.append(
                f"{len(orphan)} block ID(s) alone on a line -- these become separate "
                f"blocks and break transclusion (SKILL.md Rule 11)"
            )

    print()
    for e in errors:
        print(f"  ERROR   {e}")
    for w in warnings:
        print(f"  warn    {w}")
    print(f"\n{len(errors)} error(s), {len(warnings)} warning(s)")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
