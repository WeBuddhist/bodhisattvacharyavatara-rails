#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
generate_365_study.py
=====================
Reads the BCA root text and produces a single 365-day study Markdown file.

Run from inside your Obsidian vault root, e.g.:
    cd "C:\\Users\\tiger\\Obsidian\\bodhisattvacharyavatara-rails"
    python generate_365_study.py

Or open a terminal anywhere and run:
    python "C:\\Users\\tiger\\Obsidian\\bodhisattvacharyavatara-rails\\generate_365_study.py"
"""

import re
import os
import sys

# ---------------------------------------------------------------------------
# Paths (relative to the vault root — adjust only if you move this script)
# ---------------------------------------------------------------------------
VAULT_ROOT = os.path.dirname(os.path.abspath(__file__))

SOURCE_FILE = os.path.join(
    VAULT_ROOT,
    "0-INBOX",
    "bo-root versions",
    "bo-བློ་ལྡན་ཤེས་རབ།-ཀུན་དཔལ་སྤྱོད་འཇུག་རྩ་བ།.md",
)

OUTPUT_FILE = os.path.join(
    VAULT_ROOT,
    "3-TRANSFORMATIONS",
    "སྤྱོད་འཇུག་སློབ་སྦྱོང། ཉིན་ ༣༦༥།.md",
)

# ---------------------------------------------------------------------------
# Tibetan numeral helper
# ---------------------------------------------------------------------------
_TIB_DIGITS = "༠༡༢༣༤༥༦༧༨༩"

def to_tibetan(n: int) -> str:
    """Convert an integer to a Tibetan-numeral string, e.g. 365 → ༣༦༥"""
    return "".join(_TIB_DIGITS[int(d)] for d in str(n))

# ---------------------------------------------------------------------------
# Parse verse entries from the source file
# ---------------------------------------------------------------------------
COLOPHON_MARKER = "བྱང་ཆུབ་སེམས་དཔའི་སྤྱོད་པ་ལ་འཇུག་པ་ལས།"
VOLUME_MARKER   = "བམ་པོ་གཉིས་པའོ།"
# Verse lines always contain at least one shad (།)
VERSE_MARKER    = "།"

def extract_verses(source_path: str) -> list[str]:
    """Return an ordered list of verse strings, colophons stripped."""

    with open(source_path, encoding="utf-8") as fh:
        lines = fh.readlines()

    verses: list[str] = []
    entry_pattern = re.compile(r"^(\d+)\.\s*(.*)")

    for line in lines:
        line = line.rstrip()
        m = entry_pattern.match(line)
        if not m:
            continue

        num  = int(m.group(1))
        text = m.group(2).strip()

        # Skip translator colophon entries that come after the main text
        # (entries beyond the last chapter tend to lack verse shads)
        if num > 952:
            break

        # Skip blank entries
        if not text:
            continue

        # Skip the volume marker
        if VOLUME_MARKER in text:
            continue

        # Strip chapter-end colophon embedded in the same entry
        if COLOPHON_MARKER in text:
            text = text[: text.index(COLOPHON_MARKER)].strip()

        # Skip if still empty after stripping, or if it looks like
        # pure prose without any verse shads (e.g. translator notes)
        if not text or VERSE_MARKER not in text:
            continue

        verses.append(text)

    return verses


# ---------------------------------------------------------------------------
# Build day-assignment list (Bresenham-style even distribution)
# ---------------------------------------------------------------------------
DAYS = 365

def build_day_assignments(total: int, days: int = DAYS) -> list[int]:
    """
    Return a list of length `days` where each element is 2 or 3,
    and sum equals `total`.  Heavy days (3 verses) are spread as
    evenly as possible throughout the year.
    """
    if total < days * 2:
        sys.exit(
            f"ERROR: only {total} verses found — not enough for {days} days "
            f"at ≥2 verses/day."
        )

    heavy = total - days * 2   # extra days that get 3 instead of 2
    assignments: list[int] = []
    error = 0
    for _ in range(days):
        error += heavy
        if error >= days:
            assignments.append(3)
            error -= days
        else:
            assignments.append(2)

    assert sum(assignments) == total, "Distribution mismatch — please report this bug."
    return assignments


# ---------------------------------------------------------------------------
# Render the output Markdown
# ---------------------------------------------------------------------------
def render_output(verses: list[str], assignments: list[int]) -> str:
    title = "སྤྱོད་འཇུག་སློབ་སྦྱོང། ཉིན་ ༣༦༥།"
    lines: list[str] = [f"# {title}", ""]

    idx = 0
    for day_num, count in enumerate(assignments, start=1):
        tib_day = to_tibetan(day_num)
        lines.append(f"## ཉིན་ {tib_day}།")
        lines.append("")
        for _ in range(count):
            lines.append(verses[idx])
            lines.append("")
            idx += 1
        lines.append("---")
        lines.append("")

    return "\n".join(lines)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
def main() -> None:
    # Sanity checks
    if not os.path.isfile(SOURCE_FILE):
        sys.exit(f"Source file not found:\n  {SOURCE_FILE}")

    os.makedirs(os.path.dirname(OUTPUT_FILE), exist_ok=True)

    print(f"Reading source:  {SOURCE_FILE}")
    verses = extract_verses(SOURCE_FILE)
    print(f"Verses extracted: {len(verses)}")

    assignments = build_day_assignments(len(verses))
    heavy = assignments.count(3)
    light = assignments.count(2)
    print(f"Distribution:    {heavy} days × 3 verses  +  {light} days × 2 verses  =  {len(verses)} total")

    output = render_output(verses, assignments)

    with open(OUTPUT_FILE, "w", encoding="utf-8") as fh:
        fh.write(output)

    print(f"Output written:  {OUTPUT_FILE}")
    print("Done ✓")


if __name__ == "__main__":
    main()
