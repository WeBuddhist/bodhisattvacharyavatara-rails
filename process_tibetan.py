#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Process Tibetan text file: remove blank lines and concatenate all text
into a single continuous line (no separators, since Tibetan uses tshegs).
"""

filepath = r"C:\Users\tiger\Obsidian\bodhisattvacharyavatara-rails\1-SOURCES\Commentaries\bo-རྒྱལ་བ་རིན་པོ་ཆེ།.cleaned.md"

print(f"Reading: {filepath}")
with open(filepath, 'r', encoding='utf-8') as f:
    lines = f.readlines()

print(f"Total lines read: {len(lines)}")

# Filter out blank/empty lines (lines that are empty or contain only whitespace)
# Preserve trailing content within lines (don't strip trailing spaces from text lines)
# Only strip the line ending characters (\n, \r)
non_blank = []
for line in lines:
    stripped = line.strip()
    if stripped:  # line has non-whitespace content
        # Remove only the line ending, preserve any trailing spaces within the line
        content = line.rstrip('\n').rstrip('\r')
        non_blank.append(content)

print(f"Non-blank lines: {len(non_blank)}")

# Concatenate all non-blank lines with no separator
result = ''.join(non_blank)

print(f"Total characters in result: {len(result)}")

# Write back to the same file
with open(filepath, 'w', encoding='utf-8') as f:
    f.write(result)

print("Done! File written successfully.")
