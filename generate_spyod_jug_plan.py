#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generate 365-day Bodhicaryavatara (སྤྱོད་འཇུག) daily study plan.

Run from any directory:
    python generate_spyod_jug_plan.py

Reads:
  - Root text: 0-INBOX/bo-root versions/bo-བློ་ལྡན་ཤེས་རབ།-ཀུན་དཔལ་སྤྱོད་འཇུག་རྩ་བ།.md
  - Commentary: 1-SOURCES/Commentaries/bo-མཁན་པོ་ཀུན་དཔལ།.md

Writes 365 .md files to:
  3-TRANSFORMATIONS/སྤྱོད་འཇུག་སློབ་སྦྱོང། ཉིན་ ༣༦༥།/
"""

import re
import os
import sys

# ── Paths ──────────────────────────────────────────────────────────────────
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_TEXT  = os.path.join(SCRIPT_DIR,
    "0-INBOX", "bo-root versions",
    "bo-བློ་ལྡན་ཤེས་རབ།-ཀུན་དཔལ་སྤྱོད་འཇུག་རྩ་བ།.md")
COMMENTARY = os.path.join(SCRIPT_DIR,
    "1-SOURCES", "Commentaries",
    "bo-མཁན་པོ་ཀུན་དཔལ།.md")
# Second commentary file (split version) — merged if both exist
COMMENTARY2 = os.path.join(SCRIPT_DIR,
    "1-SOURCES", "Commentaries",
    "bo-མཁན་པོ་ཀུན་དཔལ། 1.md")
OUTPUT_DIR = os.path.join(SCRIPT_DIR,
    "3-TRANSFORMATIONS",
    "སྤྱོད་འཇུག་སློབ་སྦྱོང། ཉིན་ ༣༦༥།")

# ── Tibetan numerals ────────────────────────────────────────────────────────
TNUM = "༠༡༢༣༤༥༦༧༨༩"   # index 0-9

def to_tib(n: int) -> str:
    """Convert an integer to Tibetan digit string."""
    return "".join(TNUM[int(d)] for d in str(n))

# ── Filtering constants ─────────────────────────────────────────────────────
SHAD          = "།"
COLOPHON_RE   = re.compile(r"ལེའུ.{1,15}འོ།།")
EXCLUDE_STRS  = ["རྒྱ་གར་གྱི་མཁན་པོ", "རྫོགས་སོ།།"]

def is_valid_verse(text: str) -> bool:
    """
    Return True if the item text should be included as a verse.

    Rules (inclusive range 6-952 already enforced before calling):
      - must contain ། (shad)
      - must NOT match ལེའུ.{1,15}འོ།། (chapter colophon)
      - must NOT contain རྒྱ་གར་གྱི་མཁན་པོ or རྫོགས་སོ།།
    """
    if SHAD not in text:
        return False
    if COLOPHON_RE.search(text):
        return False
    for s in EXCLUDE_STRS:
        if s in text:
            return False
    return True

# ── Parse numbered items from a markdown file ────────────────────────────────
# Pattern: line begins with   NUMBER.   (possibly with leading spaces)
ITEM_RE = re.compile(r"^\s*(\d+)\.\s*(.*)")

def parse_items(filepath: str):
    """
    Return a dict {number: text} for all numbered items in the file.
    Multi-line items: if a numbered line is followed by non-numbered
    continuation lines, they are appended (separated by space).
    The commentary file has one item per line (very long), so this
    also works for that format.
    """
    items = {}
    current_num = None
    current_text_parts = []

    with open(filepath, encoding="utf-8") as fh:
        for line in fh:
            line = line.rstrip("\n")
            m = ITEM_RE.match(line)
            if m:
                # Save previous item
                if current_num is not None:
                    items[current_num] = " ".join(current_text_parts).strip()
                current_num = int(m.group(1))
                rest = m.group(2).strip()
                current_text_parts = [rest] if rest else []
            else:
                # Continuation or non-item line
                stripped = line.strip()
                if current_num is not None and stripped:
                    current_text_parts.append(stripped)

    # Save last item
    if current_num is not None:
        items[current_num] = " ".join(current_text_parts).strip()

    return items

# ── Section heading detection ─────────────────────────────────────────────────
# Headings in root text look like:  ## text  or  ### text  or  #### text
HEADING_RE = re.compile(r"^(#{1,6})\s+(.+)")

def parse_headings(filepath: str):
    """
    Return a dict {item_number: heading_text} where heading_text is the
    last Markdown heading seen before that numbered item.
    Also returns a dict {item_number: section} for the deepest heading.
    """
    # We want: for each item number, what is the most-recent heading seen
    # before it in the file?
    heading_map = {}   # item_num -> heading text (deepest/most recent)
    current_heading = "སྤྱོད་འཇུག"   # default

    with open(filepath, encoding="utf-8") as fh:
        for line in fh:
            line = line.rstrip("\n")
            hm = HEADING_RE.match(line)
            if hm:
                current_heading = hm.group(2).strip()
                continue
            im = ITEM_RE.match(line)
            if im:
                num = int(im.group(1))
                heading_map[num] = current_heading

    return heading_map

# ── Pāda splitting ────────────────────────────────────────────────────────────
# Split verse text on  ། །  (shad + space + shad with optional trailing །)
# Keep each pāda on its own line
PADA_SPLIT_RE = re.compile(r"། །|།།")

def format_verse(text: str) -> str:
    """
    Split verse text into pādas (one per line).
    Split on  ། །  boundaries.
    Clean up trailing/leading whitespace from each pāda.
    """
    # First strip any trailing double-shad or single shad
    text = text.strip()

    # Split on pāda boundaries
    # The text typically looks like:
    #   ཀ། །ཁ། །ག། །ང། །
    # or (shorter verses):
    #   ཀ། །ཁ།
    parts = re.split(r"། །", text)
    lines = []
    for p in parts:
        p = p.strip()
        if p:
            # Add the shad back if the part does not already end with །
            # (except the very last fragment which may already end with ། or be empty)
            lines.append(p)

    # Re-add ། at the end of each line that doesn't end with it
    formatted = []
    for i, line in enumerate(lines):
        if not line.endswith("།"):
            line = line + "།"
        if i < len(lines) - 1:
            line = line + " །"
        formatted.append(line)

    return "\n".join(formatted)

# ── Build verse list ──────────────────────────────────────────────────────────
def build_verse_list(root_items, heading_map):
    """
    Filter root_items for valid verses in range 6-952.
    Return list of (item_num, verse_text, section_heading).
    """
    verses = []
    for num in sorted(root_items.keys()):
        if num < 6 or num > 952:
            continue
        text = root_items[num]
        if not text:
            continue
        if not is_valid_verse(text):
            continue
        section = heading_map.get(num, "སྤྱོད་འཇུག")
        verses.append((num, text, section))
    return verses

# ── 365-day distribution ──────────────────────────────────────────────────────
def distribute(verses, days=365):
    """
    Distribute verses across `days` days.
    base = total // days
    extra = total % days
    Days 1..extra get (base+1) items; remaining days get base items.
    Returns list of lists (one list per day).
    """
    total = len(verses)
    base  = total // days
    extra = total % days

    distribution = []
    idx = 0
    for day in range(1, days + 1):
        count = base + (1 if day <= extra else 0)
        distribution.append(verses[idx: idx + count])
        idx += count

    return distribution

# ── Write one daily file ──────────────────────────────────────────────────────
def write_day_file(day_num, day_verses, commentary_items, output_dir):
    """
    Write one Markdown file for the given day.

    Filename:  ཉིན་ [TIBETAN_NUM]།.md
    Content:
      # ཉིན་ [TIBETAN_NUM]། — སྤྱོད་འཇུག་སློབ་སྦྱོང་།
      (for each verse:)
      ## [SECTION]ནི།
      [formatted verse text]
      ---
      [commentary text]
    """
    tnum = to_tib(day_num)
    filename = f"ཉིན་ {tnum}།.md"
    filepath = os.path.join(output_dir, filename)

    lines = []
    lines.append(f"# ཉིན་ {tnum}། — སྤྱོད་འཇུག་སློབ་སྦྱོང་།")
    lines.append("")

    for (item_num, verse_text, section) in day_verses:
        lines.append(f"## {section}ནི།")
        lines.append("")
        lines.append(format_verse(verse_text))
        lines.append("")
        lines.append("---")
        lines.append("")
        commentary = commentary_items.get(item_num, "")
        if commentary:
            lines.append(commentary)
        else:
            lines.append("*(འགྲེལ་བ་མེད།)*")
        lines.append("")

    content = "\n".join(lines)
    with open(filepath, "w", encoding="utf-8") as fh:
        fh.write(content)

# ── Main ──────────────────────────────────────────────────────────────────────
def main():
    print("Reading root text …")
    root_items  = parse_items(ROOT_TEXT)
    heading_map = parse_headings(ROOT_TEXT)
    print(f"  Root text items parsed: {len(root_items)}")

    print("Reading commentary …")
    commentary_items = parse_items(COMMENTARY)
    # Merge second file if it exists and has items the first lacks
    if os.path.exists(COMMENTARY2):
        commentary2 = parse_items(COMMENTARY2)
        before = len(commentary_items)
        for k, v in commentary2.items():
            if k not in commentary_items or not commentary_items[k]:
                commentary_items[k] = v
        print(f"  Commentary items parsed: {len(commentary_items)} "
              f"(merged {len(commentary_items)-before} from split file)")
    else:
        print(f"  Commentary items parsed: {len(commentary_items)}")

    print("Building verse list …")
    verses = build_verse_list(root_items, heading_map)
    total  = len(verses)
    print(f"  Valid verses: {total}")

    base  = total // 365
    extra = total % 365
    print(f"  Distribution: {extra} days with {base+1} verses, "
          f"{365-extra} days with {base} verses")

    print("Distributing across 365 days …")
    distribution = distribute(verses)

    os.makedirs(OUTPUT_DIR, exist_ok=True)
    print(f"Writing to: {OUTPUT_DIR}")

    for day_num, day_verses in enumerate(distribution, start=1):
        write_day_file(day_num, day_verses, commentary_items, OUTPUT_DIR)
        if day_num % 50 == 0 or day_num == 365:
            print(f"  Day {day_num}/365 written  "
                  f"(verses {day_verses[0][0]}–{day_verses[-1][0]})")

    print("Done! 365 files written.")

if __name__ == "__main__":
    main()
