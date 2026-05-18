#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Process Tibetan commentary file:
Move section headings (ས་བཅད་) from end of paragraphs to beginning of next paragraph.
"""

import re
import shutil

SOURCE_FILE = r"C:\Users\tiger\Obsidian\bodhisattvacharyavatara-rails\1-SOURCES\Commentaries\bo-མཁན་པོ་ཀུན་དཔལ། 1.md"
BACKUP_FILE = SOURCE_FILE + ".bak"

# Read the file
print("Reading file...")
with open(SOURCE_FILE, 'r', encoding='utf-8') as f:
    content = f.read()

print(f"File size: {len(content)} bytes")

# Make backup
print("Creating backup...")
shutil.copy2(SOURCE_FILE, BACKUP_FILE)
print("Backup created.")

# Clean up any leftover artifacts from previous partial edits
# Remove lines that are just whitespace followed by a heading that was already moved
import re as _re
# Remove orphan duplicate-heading lines (lines like "  གསུམ་པ་ནི།DEDUP_2")
lines = content.split('\n')
cleaned_lines = []
for line in lines:
    # Skip lines that are whitespace + ordinal heading + DEDUP_2 marker (artifact)
    if 'DEDUP_2' in line:
        print(f"  Removing artifact line: {line!r}")
        continue
    cleaned_lines.append(line)
content = '\n'.join(cleaned_lines)

# Split into paragraphs
paragraphs = content.split('\n\n')
print(f"Total paragraphs: {len(paragraphs)}")

# Tibetan ordinals (these are the words that start section headings)
ORDINALS = [
    'དང་པོ',
    'གཉིས་པ',
    'གསུམ་པ',
    'བཞི་པ',
    'ལྔ་པ',
    'དྲུག་པ',
    'བདུན་པ',
    'བརྒྱད་པ',
    'དགུ་པ',
    'བཅུ་པ',
]

ordinals_alt = '|'.join(re.escape(o) for o in ORDINALS)

# Match a shad followed by optional space and an ordinal-starting phrase that ends with shad at end
# We want to find ALL such matches and take the LAST one
# Pattern: after a shad (།), optional whitespace, then ordinal word, then content (no shad allowed
# except at the very end), ends with shad at end of string
#
# Key constraint: the heading itself should not contain another "sentence-ending" double shad
# We allow single shads WITHIN the heading (e.g. "གཉིས་པ་འགྱུར་ཕྱག་ནི།")
# but we want to stop at the LAST ordinal occurrence

# Strategy: find all positions where an ordinal starts after a shad,
# and the text from there to end-of-paragraph ends with a shad and is < 130 chars.
# Take the LAST such position (rightmost ordinal heading at end of paragraph).

def find_heading_at_end(paragraph):
    """
    Check if a paragraph ends with a section heading.
    Returns (main_content, heading) or (paragraph, None).
    """
    stripped = paragraph.rstrip()
    if not stripped.endswith('།'):
        return paragraph, None

    # Find all positions where an ordinal word occurs after a shad+space
    # Pattern: shad, optional whitespace, then ordinal
    pattern = re.compile(r'།\s*(' + ordinals_alt + r')')

    # Find all matches
    all_matches = list(pattern.finditer(stripped))

    if not all_matches:
        return paragraph, None

    # Try from the last match backwards to find a valid heading
    for match in reversed(all_matches):
        heading_start = match.start(1)  # start of the ordinal word (inside match)
        heading_candidate = stripped[heading_start:]

        # Must end with shad (already confirmed paragraph ends with shad)
        # Must be short enough (< 130 chars)
        if len(heading_candidate) > 130:
            continue

        # The heading is valid - split the paragraph here
        # main_content ends with the shad that precedes the heading
        main_content = stripped[:match.start(1)].rstrip()
        heading = heading_candidate.strip()
        return main_content, heading

    return paragraph, None


# Process paragraphs
new_paragraphs = []
headings_moved = 0
heading_examples = []

i = 0
while i < len(paragraphs):
    para = paragraphs[i]
    main_content, heading = find_heading_at_end(para)

    if heading is not None and i + 1 < len(paragraphs):
        headings_moved += 1
        if len(heading_examples) < 30:
            snippet = main_content[-60:].replace('\n', ' ')
            heading_examples.append(
                f"  Para {i+1}: ...{snippet!r}\n           -> HEADING: {heading!r}"
            )

        new_paragraphs.append(main_content)

        # Prepend heading to next paragraph
        next_para = paragraphs[i + 1]
        next_para_stripped = next_para.lstrip('\n')
        leading_newlines = next_para[:len(next_para) - len(next_para_stripped)]
        new_next_para = leading_newlines + heading + '\n' + next_para_stripped
        paragraphs[i + 1] = new_next_para
    else:
        new_paragraphs.append(para)

    i += 1

new_content = '\n\n'.join(new_paragraphs)

print(f"\nHeadings moved: {headings_moved}")
print("\nExamples of headings found and moved:")
for ex in heading_examples:
    print(ex)

print(f"\nWriting modified content back to source file...")
with open(SOURCE_FILE, 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Done!")
print(f"\nOriginal size: {len(content)} bytes")
print(f"New size: {len(new_content)} bytes")
print(f"Difference: {len(new_content) - len(content)} bytes")
