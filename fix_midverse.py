#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
fix_midverse.py — Split mid-verse merged half-lines in the already-formatted
Tibetan translation file.

Applies ONLY the mid-verse line-break fix without touching block IDs or verse
numbers. Safe to run on an already-formatted file.

Run from the vault root:
    python fix_midverse.py

Pattern fixed: a single shad '།' preceded by a space and immediately followed
by a Tibetan syllable (no space or shad after it).  Examples:
    ཞིག །ནམ་   →   ཞིག །\n    ནམ་
    གི །སྡུག་   →   གི །\n    སྡུག་

The regex does NOT match:
  - '། །' (SHAD_PAIR): the space before the second shad is preceded by '།'
    (first shad), so the lookbehind '(?<![།])' blocks the match.
  - A shad at end-of-line or before whitespace/another shad: blocked by the
    positive lookahead '(?=[^\s།])'.
  - Lines beginning with '།' (no preceding space).
"""

import re, os, sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
BASE = os.path.join(SCRIPT_DIR, '1-SOURCES', 'Translations')
files = [f for f in os.listdir(BASE) if f.endswith('.md')]
if not files:
    sys.exit("No .md file found in " + BASE)
INPUT = os.path.join(BASE, files[0])
print(f"Processing: {INPUT}")

# Mid-verse line-break pattern (see SKILL.md → Root-Text-Structure)
MID_LINE_SHAD = re.compile(r'(?<![།]) །(?=[^\s།])')

with open(INPUT, 'r', encoding='utf-8') as f:
    lines = f.readlines()

print(f"Read {len(lines)} lines")

output = []
changed = 0
for i, line in enumerate(lines, 1):
    stripped = line.rstrip('\n')
    if MID_LINE_SHAD.search(stripped):
        fixed = MID_LINE_SHAD.sub(' །\n', stripped)
        output.append(fixed + '\n')
        changed += 1
        # Print first 10 changes for verification
        if changed <= 10:
            print(f"  Line {i}: split → {repr(fixed[:80])}")
    else:
        output.append(line)

with open(INPUT, 'w', encoding='utf-8') as f:
    f.writelines(output)

print(f"\nDone. {changed} lines split. File: {INPUT}")
