#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Format the Tibetan root text of Bodhisattvacharyavatara.
Input: 0-INBOX/bo-root versions/Bo align with sk.md
Output: 1-SOURCES/Text/bo-root-text.md
"""

import os, sys, re

# Define paths relative to the vault root
VAULT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
INPUT_PATH = os.path.join(VAULT_ROOT, "0-INBOX", "bo-root versions", "Bo align with sk.md")
OUTPUT_PATH = os.path.join(VAULT_ROOT, "1-SOURCES", "Text", "bo-root-text.md")

print(f"Vault root: {VAULT_ROOT}")
print(f"Input path: {INPUT_PATH}")
print(f"Output path: {OUTPUT_PATH}")

if not os.path.exists(INPUT_PATH):
    sys.exit(f"Error: Input file not found at {INPUT_PATH}")

# Chapter starts (list item numbers in the input file)
CHAPTER_STARTS = {
    1: 5,
    2: 42,
    3: 108,
    4: 142,
    5: 191,
    6: 301,
    7: 436,
    8: 513,
    9: 701,
    10: 869
}

# Colophon list item numbers
COLOPHONS = {
    1: 41,
    2: 107,
    3: 141,
    4: 190,
    5: 300,
    6: 435,
    7: 512,
    8: 700,
    9: 868,
    10: 927
}

CHAPTER_HEADINGS = {
    1: "## 1. ལེའུ་དང་པོ། བྱང་ཆུབ་སེམས་ཀྱི་ཕན་ཡོན་བཤད་པ། ^TOC-1",
    2: "## 2. ལེའུ་གཉིས་པ། སྡིག་པ་བཤགས་པ། ^TOC-2",
    3: "## 3. ལེའུ་གསུམ་པ། བྱང་ཆུབ་ཀྱི་སེམས་ཡོངས་སུ་བཟུང་བ། ^TOC-3",
    4: "## 4. ལེའུ་བཞི་པ། བག་ཡོད་བསྟན་པ། ^TOC-4",
    5: "## 5. ལེའུ་ལྔ་པ། ཤེས་བཞིན་བསྲུང་བར་བྱ་བ། ^TOC-5",
    6: "## 6. ལེའུ་དྲུག་པ། བཟོད་པ་བསྟན་པ། ^TOC-6",
    7: "## 7. ལེའུ་བདུན་པ། བརྩོན་འགྲུས་བསྟན་པ། ^TOC-7",
    8: "## 8. ལེའུ་བརྒྱད་པ། བསམ་གཏན་བསྟན་པ། ^TOC-8",
    9: "## 9. ལེའུ་དགུ་པ། ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ། ^TOC-9",
    10: "## 10. ལེའུ་བཅུ་པ། བསྔོ་བ། ^TOC-10"
}

def get_chapter_for_num(num):
    current_ch = 0
    for ch, start in sorted(CHAPTER_STARTS.items()):
        if num >= start:
            current_ch = ch
        else:
            break
    return current_ch

def split_stanza(text):
    text = text.strip()
    parts = text.split(' །')
    lines = []
    for part in parts:
        part = part.strip()
        if part:
            lines.append(part + ' །')
    return lines

# Read input file
with open(INPUT_PATH, 'r', encoding='utf-8') as f:
    raw_lines = f.readlines()

print(f"Read {len(raw_lines)} lines from input.")

LINE_PAT = re.compile(r'^(\d+)\.\s+(.*)$')

formatted_lines = []

# Write Frontmatter
formatted_lines.append("---")
formatted_lines.append("title: Bodhisattvacharyavatara — Tibetan Root Text")
formatted_lines.append("author: Śāntideva")
formatted_lines.append("language: Tibetan")
formatted_lines.append("file_type: root-text")
formatted_lines.append("lang_tag: bo")
formatted_lines.append("source_description: \"Tibetan root text of the Bodhisattvacharyavatara (སྤྱོད་འཇུག་), aligned with Sanskrit verses, formatted according to project standards.\"")
formatted_lines.append("verse_id_format: chapter-verse")
formatted_lines.append("---")
formatted_lines.append("")

current_chapter = 0

for line in raw_lines:
    line = line.strip()
    if not line:
        continue
    
    m = LINE_PAT.match(line)
    if not m:
        continue
    
    num = int(m.group(1))
    text = m.group(2).strip()
    
    # Chapter 0 (Introduction)
    if 1 <= num <= 4:
        if num == 1:
            formatted_lines.append("## 0. Introduction")
            formatted_lines.append("")
        # Clean ch-1 prefix
        text = re.sub(r'^ch-\d+\s+', '', text)
        formatted_lines.append(f"{text} ^0-{num}")
        formatted_lines.append("")
        continue
    
    # Check for chapter start
    ch = get_chapter_for_num(num)
    if ch != current_chapter and ch > 0:
        current_chapter = ch
        formatted_lines.append(CHAPTER_HEADINGS[ch])
        formatted_lines.append("")
    
    # Check if colophon line
    if num in COLOPHONS.values():
        formatted_lines.append(text)
        formatted_lines.append("")
        continue
    
    # Check if translator colophon (line 928)
    if num == 928:
        formatted_lines.append("## Translator Colophon")
        formatted_lines.append("")
        formatted_lines.append(text)
        formatted_lines.append("")
        continue
    
    # Otherwise, it's a standard verse in chapter `ch`
    if ch > 0:
        rel_v = num - CHAPTER_STARTS[ch] + 1
        # Clean ch-N prefix if present
        text = re.sub(r'^ch-\d+\s+', '', text)
        
        vlines = split_stanza(text)
        for i, vl in enumerate(vlines):
            if i == len(vlines) - 1:
                formatted_lines.append(f"{vl} ^{ch}-{rel_v}")
            else:
                formatted_lines.append(vl)
        formatted_lines.append("")

# Ensure output directory exists
os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)

# Write output file
with open(OUTPUT_PATH, 'w', encoding='utf-8') as f:
    f.write('\n'.join(formatted_lines))

print(f"Successfully formatted Tibetan root text and saved to {OUTPUT_PATH}")
