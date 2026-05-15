#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generate 365-day Bodhicaryavatara (སྤྱོད་འཇུག) study plan.

Run this script once from any terminal:
    python generate_study_plan.py

It reads both source files and writes all 365 day-files into:
    3-TRANSFORMATIONS/སྤྱོད་འཇུག་སློབ་སྦྱོང། ཉིན་ ༣༦༥།/

Each file is named  ཉིན་ [TIBETAN_NUM]།.md
"""

import re
import os

# ── Paths (relative to this script's location) ─────────────────────────────────
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

ROOT_PATH = os.path.join(
    SCRIPT_DIR,
    "0-INBOX", "bo-root versions",
    "bo-བློ་ལྡན་ཤེས་རབ།-ཀུན་དཔལ་སྤྱོད་འཇུག་རྩ་བ།.md"
)
COMMENTARY_PATH = os.path.join(
    SCRIPT_DIR,
    "1-SOURCES", "Commentaries",
    "bo-མཁན་པོ་ཀུན་དཔལ།.md"
)
OUTPUT_DIR = os.path.join(
    SCRIPT_DIR,
    "3-TRANSFORMATIONS",
    "སྤྱོད་འཇུག་སློབ་སྦྱོང། ཉིན་ ༣༦༥།"
)

# ── Tibetan digit conversion ───────────────────────────────────────────────────
TDIG = str.maketrans("0123456789", "༠༡༢༣༤༥༦༧༨༩")

def to_tib(n: int) -> str:
    return str(n).translate(TDIG)


# ── Patterns ───────────────────────────────────────────────────────────────────
# Colophon: matches "ལེའུ" + up to 15 chars + "འོ།།"
COLOPHON_PAT  = re.compile(r"ལེའུ.{1,15}འོ།།")
# Words that indicate a non-verse line to skip
EXCLUDE_WORDS = ["རྒྱ་གར་གྱི་མཁན་པོ", "རྫོགས་སོ།།"]
# Heading pattern: "## text", "### text", "#### text"
HEADING_PAT   = re.compile(r"^(#{2,4})\s+(.+)$")
# Item line pattern: "NNN. text"
ITEM_PAT      = re.compile(r"^(\d+)\.\s*(.*)")


# ── Parse root text ────────────────────────────────────────────────────────────

def parse_root(path: str):
    """
    Returns list of dicts:
        { 'num': int, 'text': str, 'heading': str }

    Rules:
    - Track the most recent markdown heading (## / ### / ####) as context.
    - Skip items before any heading appears (title/translator lines).
    - Skip items with empty text.
    - Skip items containing EXCLUDE_WORDS.
    - Skip items matching COLOPHON_PAT.
    - Items 2–5 appearing before any heading are pre-text (excluded).
      Items 2–5 appearing after the first ## heading are intro verses (included).
    """
    verses = []
    current_heading = ""
    heading_seen = False

    with open(path, encoding="utf-8") as fh:
        lines = fh.readlines()

    for raw in lines:
        stripped = raw.strip()

        # Track headings
        m = HEADING_PAT.match(stripped)
        if m:
            current_heading = stripped
            heading_seen = True
            continue

        # Item lines
        im = ITEM_PAT.match(stripped)
        if not im:
            continue

        num  = int(im.group(1))
        text = im.group(2).strip()

        # Skip blank items
        if not text:
            continue

        # Skip pre-heading items
        if not heading_seen:
            continue

        # Skip lines with excluded words
        if any(w in text for w in EXCLUDE_WORDS):
            continue

        # Skip colophons
        if COLOPHON_PAT.search(text):
            continue

        verses.append({
            "num":     num,
            "text":    text,
            "heading": current_heading,
        })

    return verses


# ── Parse commentary ────────────────────────────────────────────────────────────

def parse_commentary(path: str):
    """
    Returns dict { item_num: str }.
    Root text item N maps to commentary item N+4.
    """
    items = {}
    with open(path, encoding="utf-8") as fh:
        lines = fh.readlines()

    for raw in lines:
        stripped = raw.strip()
        im = ITEM_PAT.match(stripped)
        if im:
            num  = int(im.group(1))
            text = im.group(2).strip()
            if text:
                items[num] = text

    return items


# ── Format a verse ─────────────────────────────────────────────────────────────

def format_verse(text: str) -> str:
    """Split on '། །' and place each pāda on its own line."""
    parts = text.split("། །")
    lines = []
    for idx, part in enumerate(parts):
        part = part.strip()
        if not part:
            continue
        if idx < len(parts) - 1:
            lines.append(part + "། །")
        else:
            lines.append(part)
    return "\n".join(lines)


# ── Build one day's file content ───────────────────────────────────────────────

def build_day(day_num: int, verses: list, comm_map: dict) -> str:
    tib  = to_tib(day_num)
    out  = [f"# ཉིན་ {tib}། — སྤྱོད་འཇུག་སློབ་སྦྱོང་།", ""]

    for v in verses:
        # Section heading
        out.append(v["heading"])
        out.append("")
        # Verse with pāda breaks
        out.append(format_verse(v["text"]))
        out.append("")
        out.append("---")
        out.append("")
        # Commentary (offset +4)
        comm = comm_map.get(v["num"] + 4, "")
        out.append(comm if comm else "*(commentary not found)*")
        out.append("")

    return "\n".join(out)


# ── Main ───────────────────────────────────────────────────────────────────────

def main():
    print(f"Reading root text from:\n  {ROOT_PATH}")
    verses = parse_root(ROOT_PATH)
    total  = len(verses)
    print(f"  → {total} verses found.\n")

    print(f"Reading commentary from:\n  {COMMENTARY_PATH}")
    comm_map = parse_commentary(COMMENTARY_PATH)
    print(f"  → {len(comm_map)} commentary items found.\n")

    # Distribution: days 1..extra get (base+1) verses; rest get base.
    base  = total // 365
    extra = total % 365
    print(f"Verse distribution: {base}–{base+1} per day "
          f"({extra} days get {base+1}, {365-extra} days get {base}).\n")

    os.makedirs(OUTPUT_DIR, exist_ok=True)

    idx = 0
    for day in range(1, 366):
        count      = base + (1 if day <= extra else 0)
        day_verses = verses[idx: idx + count]
        idx       += count

        content  = build_day(day, day_verses, comm_map)
        tib      = to_tib(day)
        filename = f"ཉིན་ {tib}།.md"
        filepath = os.path.join(OUTPUT_DIR, filename)

        with open(filepath, "w", encoding="utf-8") as fh:
            fh.write(content)

        if day % 50 == 0 or day == 365:
            print(f"  Written: day {day:3d} / 365  "
                  f"(verse index {idx}/{total})")

    print(f"\n✓ Done. 365 files written to:\n  {OUTPUT_DIR}")


if __name__ == "__main__":
    main()
