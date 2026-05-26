#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Format Sazang Mati Panchen Lodro Gyaltsen's Tibetan commentary according to the format-commentary skill.
Input/Output: 1-SOURCES/Commentaries/bo-ས་བཟང་མ་ཏི་པཎ་ཆེན་བློ་གྲོས་རྒྱལ་མཚན།.md
"""

import re
import os
import sys
import shutil

# Define paths relative to this script
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
VAULT_ROOT = os.path.abspath(os.path.join(SCRIPT_DIR, "..", ".."))
FILE_PATH = os.path.join(VAULT_ROOT, "1-SOURCES", "Commentaries", "bo-ས་བཟང་མ་ཏི་པཎ་ཆེན་བློ་གྲོས་རྒྱལ་མཚན།.md")
BACKUP_PATH = FILE_PATH + ".bak"

print(f"Vault root: {VAULT_ROOT}")
print(f"File path: {FILE_PATH}")

if not os.path.exists(FILE_PATH):
    sys.exit(f"Error: File not found at {FILE_PATH}")

# Create backup
print("Creating backup...")
shutil.copy2(FILE_PATH, BACKUP_PATH)
print("Backup created.")

# Read the raw file
with open(FILE_PATH, "r", encoding="utf-8") as f:
    raw_content = f.read()

# Separate frontmatter
frontmatter_match = re.match(r"^---.*?---", raw_content, re.DOTALL)
frontmatter = ""
body = raw_content
if frontmatter_match:
    frontmatter = frontmatter_match.group(0)
    body = raw_content[len(frontmatter):]

# Split body into raw paragraphs based on double newlines
raw_paragraphs = [p.strip() for p in body.split("\n\n") if p.strip()]
print(f"Read {len(raw_paragraphs)} raw blocks.")

# Parse paragraph numbers and text
paragraphs = []
current_id = None
for p in raw_paragraphs:
    if p.isdigit():
        current_id = int(p)
    else:
        paragraphs.append((current_id, p))
        current_id = None

print(f"Parsed {len(paragraphs)} numbered paragraphs.")

CHAPTER_HEADINGS = {
    0: "## 0. སྔོན་འགྲོ།",
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
    if 1 <= paragraph_id <= 89:
        return 0
    elif 90 <= paragraph_id <= 176:
        return 1
    elif 177 <= paragraph_id <= 311:
        return 2
    elif 312 <= paragraph_id <= 372:
        return 3
    elif 373 <= paragraph_id <= 477:
        return 4
    elif 478 <= paragraph_id <= 745:
        return 5
    elif 746 <= paragraph_id <= 1009:
        return 6
    elif 1010 <= paragraph_id <= 1169:
        return 7
    elif 1170 <= paragraph_id <= 1539:
        return 8
    elif 1540 <= paragraph_id <= 2219:
        return 9
    elif 2220 <= paragraph_id <= 2347:
        return 10
    elif 2348 <= paragraph_id <= 2353:
        return 11
    return 0

def clean_latin_prefixes(text):
    # Remove Latin prefixes immediately preceding Tibetan letters
    return re.sub(r'([a-zA-Z])([\u0F00-\u0FFF])', r'\2', text)

def split_into_sentences(text):
    # Split by '། །' or '།།'
    parts = re.split(r'(?<=[།])\s+', text)
    sentences = []
    current = []
    for part in parts:
        part = part.strip()
        if not part:
            continue
        current.append(part)
        if part.endswith('། །') or part.endswith('།།') or any(part.endswith(end) for end in ['ལོ། །', 'སོ། །', 'གསུངས། །', 'ཞེས་སོ། །', 'ཞེས་བྱའོ། །', 'ཞེས་པའོ། །', 'འགྱུར་རོ། །', 'ཡིན་ནོ། །', 'ཤོག །']):
            sentences.append(" ".join(current))
            current = []
    if current:
        sentences.append(" ".join(current))
    return sentences

def split_paragraph_to_blocks(text):
    sentences = split_into_sentences(text)
    blocks = []
    current_block = []
    current_len = 0
    for s in sentences:
        current_block.append(s)
        current_len += len(s)
        if current_len > 150 or len(current_block) >= 2:
            blocks.append(" ".join(current_block))
            current_block = []
            current_len = 0
    if current_block:
        blocks.append(" ".join(current_block))
    return blocks

def format_quotes(text):
    text = re.sub(r'(ཇི་སྐད་དུ།|སྡུད་པ་ལས།|ལས།|གསུངས་པ།|མདོ་ལས།|རྒྱུད་བླ་མར།|བཤེས་སྤྲིང་དུའང༌།|མདོ་ལས་ཀྱང༌།)\s*', r'\1\n', text)
    text = re.sub(r'\s*(ཞེས་སོ། །|ཞེས་བྱ་བའོ། །|ཞེས་པ་བཞིན་ནོ། །|ཞེས་པ་ལྟར་རོ། །|ཞེས་གསུངས་པའི་ཕྱིར་རོ། །|ཞེས་བྱ་བའི་དོན་ཏོ། །|ཞེས་པའི་དོན་ཏོ། །)', r'\n\1', text)
    return text

# Process paragraphs
formatted_blocks = []
current_chapter = -1
subheading_counter = 0
block_counter = 0

# Add main title
formatted_blocks.append("# སྤྱོད་འཇུག་འགྲེལ་པ་གཞུང་དོན་རབ་གསལ་སྣང་བ།")

for para_id, para_text in paragraphs:
    para_text = para_text.strip()
    if not para_text:
        continue
    
    # Check chapter boundary
    ch = get_chapter(para_id)
    if ch != current_chapter:
        current_chapter = ch
        formatted_blocks.append(CHAPTER_HEADINGS[ch])
        subheading_counter = 0
        block_counter = 0
        
    # Clean up Latin prefixes
    para_text = clean_latin_prefixes(para_text)
    
    # Detect if paragraph is a sa-bcad heading
    is_heading = False
    heading_level = 3
    
    if len(para_text) < 150 and (para_text.endswith("།") or para_text.endswith("། །") or para_text.endswith("།།")):
        if any(pattern in para_text for pattern in ["ལ་གཉིས", "ལ་གསུམ", "ལ་བཞི", "ལ་ལྔ", "ལ་དྲུག", "ལ་བདུན", "ལ་བརྒྱད", "ལ་དགུ", "ལ་བཅུ", "དང་པོ་ལ།", "གཉིས་པ་ལ།", "གསུམ་པ་ལ།", "བཞི་པ་ལ།", "ལྔ་པ་ལ།", "དྲུག་པ་ལ།", "བདུན་པ་ལ།", "བརྒྱད་པ་ལ།", "དགུ་པ་ལ།", "བཅུ་པ་ལ།", "དང་པོ་ལའང༌།", "གཉིས་པ་ལའང༌།", "གསུམ་པ་ལའང༌།", "བཞི་པ་ལའང༌།"]):
            is_heading = True
            heading_level = 3
        elif any(para_text.startswith(prefix) for prefix in ["དང་པོ་ནི", "གཉིས་པ་ནི", "གསུམ་པ་ནི", "བཞི་པ་ནི", "ལྔ་པ་ནི", "དྲུག་པ་ནི", "བདུན་པ་ནི", "བརྒྱད་པ་ནི", "དགུ་པ་ནི", "བཅུ་པ་ནི", "ཐོག་མར་རྩོམ་པ་", "འཇུག་བྱ་བསྟན་", "ཞུགས་པ་མཐར་"]):
            is_heading = True
            heading_level = 4
        elif any(pattern in para_text for pattern in ["བཤད་པ་ལ", "བསམ་པ་ལ", "བསྒོམ་པ་ལ", "གདམས་པ་ལ", "བསྒྲུབ་པ་ལ", "བཤགས་ཚུལ་", "བསོད་ནམས་དཔག་", "ཀུན་ལས་མཆོག་", "བསོད་ནམས་ཆ་", "ཐར་པ་ཆ་", "རང་བཞིན་བསམས་"]):
            is_heading = True
            heading_level = 4
            
    if is_heading:
        if heading_level == 3:
            subheading_counter += 1
            block_counter = 0  # Restart sequence under new Level 3 heading
            prefix = f"{current_chapter}.{subheading_counter} " if current_chapter > 0 else ""
            formatted_blocks.append(f"### {prefix}{para_text}")
        else:
            formatted_blocks.append(f"#### {para_text}")
    else:
        # Split paragraph into logical blocks
        sub_blocks = split_paragraph_to_blocks(para_text)
        for idx, block_text in enumerate(sub_blocks):
            block_counter += 1
            
            # Format quotes
            block_text = format_quotes(block_text)
            
            # Generate block ID
            if subheading_counter == 0:
                bid = f"^{current_chapter}-{block_counter}"
            else:
                bid = f"^{current_chapter}-{subheading_counter}-{block_counter}"
                
            # Prepend original paragraph number to the first block
            prefix = f"{para_id}. " if idx == 0 else ""
            
            # Append block ID to the very end of the text block
            lines = block_text.split('\n')
            lines[-1] = f"{lines[-1]} {bid}"
            formatted_block_text = "\n".join(lines)
            
            formatted_blocks.append(f"{prefix}{formatted_block_text}")

# Join blocks with double newlines
formatted_body = "\n\n".join(formatted_blocks)

# Write output file
with open(FILE_PATH, "w", encoding="utf-8") as f:
    f.write(frontmatter + "\n\n" + formatted_body + "\n")

print(f"Successfully formatted commentary and saved to {FILE_PATH}")
print(f"Original size: {len(raw_content)} bytes")
print(f"New size: {len(formatted_body)} bytes")
