#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generate 365 daily study files for the Bodhicaryavatara (སྤྱོད་འཇུག).

Run from anywhere:
    python generate_study_files.py

Requires no dependencies beyond the Python standard library.
"""

import re
import os

# ── Paths ────────────────────────────────────────────────────────────────────
ROOT_TEXT = (
    r"C:\Users\tiger\Obsidian\bodhisattvacharyavatara-rails"
    r"\0-INBOX\bo-root versions"
    r"\bo-བློ་ལྡན་ཤེས་རབ།-ཀུན་དཔལ་སྤྱོད་འཇུག་རྩ་བ།.md"
)
COMMENTARY = (
    r"C:\Users\tiger\Obsidian\bodhisattvacharyavatara-rails"
    r"\1-SOURCES\Commentaries"
    r"\bo-མཁན་པོ་ཀུན་དཔལ།.md"
)
OUTPUT_DIR = (
    r"C:\Users\tiger\Obsidian\bodhisattvacharyavatara-rails"
    r"\3-TRANSFORMATIONS\སྤྱོད་འཇུག་སློབ་སྦྱོང། ཉིན་ ༣༦༥།"
)

# ── Tibetan digit conversion ──────────────────────────────────────────────────
_TDIG = str.maketrans("0123456789", "༠༡༢༣༤༥༦༧༨༩")

def to_tib(n: int) -> str:
    return str(n).translate(_TDIG)

# ── Parse the root text ───────────────────────────────────────────────────────
ITEM_RE   = re.compile(r"^(\d+)\.\s+(.*)", re.DOTALL)
HEADING_RE = re.compile(r"^(#{2,4})\s+(.+)")
COLOPHON_RE = re.compile(r"ལེའུ.{1,20}འོ།།")
SKIP_PATTERNS = [
    "རྒྱ་གར་གྱི་མཁན་པོ",
    "རྫོགས་སོ།།",
]

def parse_root_text(path):
    """
    Return a list of dicts:
      { 'num': int, 'text': str, 'heading': str }
    Only items AFTER the first heading, with non-empty text,
    that don't match skip/colophon patterns.
    """
    with open(path, encoding="utf-8") as f:
        lines = f.readlines()

    verses = []
    current_heading = ""
    first_heading_seen = False

    for line in lines:
        line = line.rstrip("\n")

        # Track headings
        hm = HEADING_RE.match(line)
        if hm:
            current_heading = hm.group(2).strip()
            if not first_heading_seen:
                first_heading_seen = True
            continue

        if not first_heading_seen:
            continue

        # Match numbered items
        im = ITEM_RE.match(line)
        if not im:
            continue

        num  = int(im.group(1))
        text = im.group(2).strip()

        # Skip empty items
        if not text:
            continue

        # Skip if any skip pattern matches
        skip = False
        for pat in SKIP_PATTERNS:
            if pat in text:
                skip = True
                break
        if skip:
            continue

        # Skip colophon items (chapter endings)
        if COLOPHON_RE.search(text):
            continue

        verses.append({
            "num":     num,
            "text":    text,
            "heading": current_heading,
        })

    return verses

# ── Format a verse with pāda line-breaks ─────────────────────────────────────
def format_verse(text):
    """
    Split on '། །' to get pādas, one per line, each ending '། །'
    except the final pāda which keeps its original ending.
    """
    # Normalise any trailing whitespace inside the text
    text = text.strip()

    # Split on pāda marker – keep the separator attached to the preceding pāda
    parts = re.split(r"(། །)", text)
    # parts alternates: segment, separator, segment, separator, ...
    lines = []
    i = 0
    while i < len(parts):
        seg = parts[i].strip()
        sep = parts[i + 1] if i + 1 < len(parts) else ""
        i += 2
        if seg:
            lines.append(seg + (sep if sep else ""))

    if not lines:
        return text

    # Remove trailing empty strings
    while lines and not lines[-1].strip():
        lines.pop()

    return "\n".join(lines)

# ── Parse the commentary ──────────────────────────────────────────────────────
COMM_ITEM_RE = re.compile(r"^(\d+)\.\s+(.*)", re.DOTALL)

def parse_commentary(path):
    """
    Return dict {item_num: text}.
    Commentary item N corresponds to root verse N-4.
    So root verse V → commentary item V+4.
    """
    comm = {}
    with open(path, encoding="utf-8") as f:
        lines = f.readlines()

    for line in lines:
        line = line.rstrip("\n")
        m = COMM_ITEM_RE.match(line)
        if not m:
            continue
        num  = int(m.group(1))
        text = m.group(2).strip()
        if text:
            comm[num] = text

    return comm

# ── Assign verses to 365 days ─────────────────────────────────────────────────
def assign_days(verses):
    """
    Returns list of 365 lists, each containing verse dicts for that day.
    Days 1..extra get (base+1) verses; days (extra+1)..365 get base verses.
    """
    total = len(verses)
    base  = total // 365
    extra = total % 365

    days = []
    idx  = 0
    for day in range(1, 366):
        count = base + (1 if day <= extra else 0)
        days.append(verses[idx : idx + count])
        idx += count

    return days

# ── Build output file content ─────────────────────────────────────────────────
def build_file(day_num, verse_list, comm_dict):
    tnum = to_tib(day_num)
    lines = [f"# ཉིན་ {tnum}། — སྤྱོད་འཇུག་སློབ་སྦྱོང་།", ""]

    for v in verse_list:
        heading = v["heading"]
        num     = v["num"]
        text    = v["text"]

        # Section heading
        if heading:
            lines.append(f"## {heading}")
            lines.append("")

        # Formatted verse
        lines.append(format_verse(text))
        lines.append("")
        lines.append("---")
        lines.append("")

        # Commentary (offset +4)
        comm_key = num + 4
        if comm_key in comm_dict:
            lines.append(comm_dict[comm_key])
        else:
            lines.append("*(commentary not found)*")

        lines.append("")

    return "\n".join(lines)

# ── Tibetan-numbered filename ─────────────────────────────────────────────────
def day_filename(day_num):
    return f"ཉིན་ {to_tib(day_num)}།.md"

# ── Main ──────────────────────────────────────────────────────────────────────
def main():
    print("Parsing root text …")
    verses = parse_root_text(ROOT_TEXT)
    print(f"  → {len(verses)} verses found.")

    print("Parsing commentary …")
    comm = parse_commentary(COMMENTARY)
    print(f"  → {len(comm)} commentary items found.")

    print("Assigning verses to 365 days …")
    days = assign_days(verses)

    os.makedirs(OUTPUT_DIR, exist_ok=True)

    print("Writing files …")
    for day_num, verse_list in enumerate(days, start=1):
        content  = build_file(day_num, verse_list, comm)
        filename = day_filename(day_num)
        filepath = os.path.join(OUTPUT_DIR, filename)
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)

        if day_num % 50 == 0 or day_num == 365:
            print(f"  … wrote day {day_num}/365")

    print(f"\nDone. 365 files written to:\n  {OUTPUT_DIR}")
    print(f"\nSummary:")
    print(f"  Total verses : {len(verses)}")
    print(f"  Commentary items loaded : {len(comm)}")
    base  = len(verses) // 365
    extra = len(verses) % 365
    print(f"  Verses per day : {base} (days {extra+1}–365) or {base+1} (days 1–{extra})")


if __name__ == "__main__":
    main()
