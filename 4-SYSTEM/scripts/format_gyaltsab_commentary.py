#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Format the Tibetan commentary of Gyaltsab Dharma Rinchen.
Input: 1-SOURCES/Commentaries/bo-རྒྱལ་ཚབ་དར་མ་རིན་ཆེན། 1.md
Output: 1-SOURCES/Commentaries/bo-རྒྱལ་ཚབ་དར་མ་རིན་ཆེན།.md
"""

import re
import os
import sys

# Define paths relative to this script
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
VAULT_ROOT = os.path.abspath(os.path.join(SCRIPT_DIR, "..", ".."))
INPUT_PATH = os.path.join(VAULT_ROOT, "1-SOURCES", "Commentaries", "bo-རྒྱལ་ཚབ་དར་མ་རིན་ཆེན། 1.md")
OUTPUT_PATH = os.path.join(VAULT_ROOT, "1-SOURCES", "Commentaries", "bo-རྒྱལ་ཚབ་དར་མ་རིན་ཆེན།.md")

print(f"Vault root: {VAULT_ROOT}")
print(f"Input path: {INPUT_PATH}")
print(f"Output path: {OUTPUT_PATH}")

if not os.path.exists(INPUT_PATH):
    sys.exit(f"Error: Input file not found at {INPUT_PATH}")

# Read the raw file
with open(INPUT_PATH, "r", encoding="utf-8") as f:
    raw_content = f.read()

# Separate frontmatter
frontmatter_match = re.match(r"^---.*?---", raw_content, re.DOTALL)
frontmatter = ""
body = raw_content
if frontmatter_match:
    frontmatter = frontmatter_match.group(0)
    body = raw_content[len(frontmatter):]

# Split body into lines
lines = body.split("\n")

# Process lines
formatted_blocks = []
current_id = None

# Chapter bounds based on original paragraph numbers
# Introduction: 1 to 92
# Chapter 1: 93 to 207
# Chapter 2: 208 to 366
# Chapter 3: 367 to 439
# Chapter 4: 440 to 563
# Chapter 5: 564 to 847
# Chapter 6: 848 to 1175
# Chapter 7: 1176 to 1376
# Chapter 8: 1377 to 1784
# Chapter 9: 1785 to 2437
# Chapter 10: 2438 to 2559
# Conclusion: 2560 to 2582

CHAPTER_HEADINGS = {
    1: "## 1. ལེའུ་དང་པོ། བྱང་ཆུབ་སེམས་ཀྱི་ཕན་ཡོན་བཤད་པ།",
    2: "## 2. ལེའུ་གཉིས་པ། སྡིག་པ་བཤགས་པ།",
    3: "## 3. ལེའུ་གསུམ་པ། བྱང་ཆུབ་ཀྱི་སེམས་ཡོངས་སུ་གཟུང་བ།",
    4: "## 4. ལེའུ་བཞི་པ། བག་ཡོད་བསྟན་པ།",
    5: "## 5. ལེའུ་ལྔ་པ། ཤེས་བཞིན་བསྲུང་བ།",
    6: "## 6. ལེའུ་དྲུག་པ། བཟོད་པ་བསྟན་པ།",
    7: "## 7. ལེའུ་བདུན་པ། བརྩོན་འགྲུས་བསྟན་པ།",
    8: "## 8. ལེའུ་བརྒྱད་པ། བསམ་གཏན་བསྟན་པ།",
    9: "## 9. ལེའུ་དགུ་པ། ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ།",
    10: "## 10. ལེའུ་བཅུ་པ། བསྔོ་བ།",
    11: "## མཇུག་གི་དོན།"
}

def get_chapter(paragraph_id):
    if paragraph_id is None:
        return 0
    if 1 <= paragraph_id <= 92:
        return 0
    elif 93 <= paragraph_id <= 207:
        return 1
    elif 208 <= paragraph_id <= 366:
        return 2
    elif 367 <= paragraph_id <= 439:
        return 3
    elif 440 <= paragraph_id <= 563:
        return 4
    elif 564 <= paragraph_id <= 847:
        return 5
    elif 848 <= paragraph_id <= 1175:
        return 6
    elif 1176 <= paragraph_id <= 1376:
        return 7
    elif 1377 <= paragraph_id <= 1784:
        return 8
    elif 1785 <= paragraph_id <= 2437:
        return 9
    elif 2438 <= paragraph_id <= 2559:
        return 10
    elif 2560 <= paragraph_id <= 2582:
        return 11
    return 0

# Track sub-heading counters to generate Level 3 numerical prefixes (e.g., 1.1)
subheading_counters = {}

current_chapter = 0

# Insert main title (Level 1) and Introduction heading (Level 2) at the start
formatted_blocks.append("# བྱང་ཆུབ་སེམས་དཔའི་སྤྱོད་པ་ལ་འཇུག་པའི་རྣམ་བཤད་རྒྱལ་སྲས་འཇུག་ངོགས་བཞུགས་སོ། །")
formatted_blocks.append("## 0. སྔོན་འགྲོ།")

for line in lines:
    line = line.strip()
    if not line:
        continue
    
    # Check if line is a paragraph ID (number)
    if line.isdigit():
        current_id = int(line)
        
        # Check if we crossed a chapter boundary
        ch = get_chapter(current_id)
        if ch != current_chapter and ch > 0:
            current_chapter = ch
            formatted_blocks.append(CHAPTER_HEADINGS[ch])
        continue
    
    # Clean up OCR errors and Latin prefixes
    # Remove Latin prefixes immediately preceding Tibetan letters
    line = re.sub(r'([a-zA-Z])([\u0F00-\u0FFF])', r'\2', line)
    
    # Fix common grammar / spelling issues
    line = line.replace("སཏེ་", "སྟེ་")
    
    # Detect if paragraph is a sa-bcad heading
    is_heading = False
    heading_level = 3
    
    # Heading patterns: short line ending with shad and containing ordinal or division words
    if len(line) < 150 and (line.endswith("།") or line.endswith("། །") or line.endswith("།།")):
        # Check for structural patterns
        if any(pattern in line for pattern in ["ལ་གཉིས", "ལ་གསུམ", "ལ་བཞི", "ལ་ལྔ", "ལ་དྲུག", "ལ་བདུན", "ལ་བརྒྱད", "ལ་དགུ", "ལ་བཅུ"]):
            is_heading = True
            heading_level = 3
        elif any(line.startswith(prefix) for prefix in ["དང་པོ་ནི", "གཉིས་པ་ནི", "གསུམ་པ་ནི", "བཞི་པ་ནི", "ལྔ་པ་ནི", "དྲུག་པ་ནི", "བདུན་པ་ནི", "བརྒྱད་པ་ནི", "དགུ་པ་ནི", "བཅུ་པ་ནི"]):
            is_heading = True
            heading_level = 4
        elif any(pattern in line for pattern in ["བཤད་པ་ལ", "བསམ་པ་ལ", "བསྒོམ་པ་ལ", "གདམས་པ་ལ", "བསྒྲུབ་པ་ལ"]):
            is_heading = True
            heading_level = 4
                
    if is_heading:
        if heading_level == 3:
            # Generate numerical prefix like "1.1 "
            subheading_counters[current_chapter] = subheading_counters.get(current_chapter, 0) + 1
            prefix = f"{current_chapter}.{subheading_counters[current_chapter]} " if current_chapter > 0 else ""
            formatted_blocks.append(f"### {prefix}{line}")
        else:
            formatted_blocks.append(f"#### {line}")
    else:
        # Standard paragraph: append block ID
        if current_id is not None:
            formatted_blocks.append(f"{line} ^{current_id}")
        else:
            formatted_blocks.append(line)

# Join blocks with double newlines
formatted_body = "\n\n".join(formatted_blocks)

# Write output file
with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
    f.write(frontmatter + "\n\n" + formatted_body + "\n")

print(f"Successfully formatted commentary and saved to {OUTPUT_PATH}")
print(f"Original size: {len(raw_content)} bytes")
print(f"New size: {len(formatted_body)} bytes")
