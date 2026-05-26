#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Format Gyaltsab Dharma Rinchen's Tibetan commentary according to the format-commentary skill.
Input/Output: 1-SOURCES/Commentaries/bo-རྒྱལ་ཚབ་དར་མ་རིན་ཆེན།.md
Updates links in: 2-RAILS/Sections/Raw/རྒྱལ་ཚབ་དར་མ་རིན་ཆེན།/1-0.md
"""

import re
import os
import sys
import shutil

# Define paths relative to this script
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
VAULT_ROOT = os.path.abspath(os.path.join(SCRIPT_DIR, "..", ".."))
FILE_PATH = os.path.join(VAULT_ROOT, "1-SOURCES", "Commentaries", "bo-རྒྱལ་ཚབ་དར་མ་རིན་ཆེན།.md")
BACKUP_PATH = FILE_PATH + ".bak"
SECTIONS_PATH = os.path.join(VAULT_ROOT, "2-RAILS", "Sections", "Raw", "རྒྱལ་ཚབ་དར་མ་རིན་ཆེན།", "1-0.md")
SECTIONS_BACKUP_PATH = SECTIONS_PATH + ".bak"

print(f"Vault root: {VAULT_ROOT}")
print(f"File path: {FILE_PATH}")
print(f"Sections path: {SECTIONS_PATH}")

if not os.path.exists(FILE_PATH):
    sys.exit(f"Error: File not found at {FILE_PATH}")

# Create backups
print("Creating backups...")
shutil.copy2(FILE_PATH, BACKUP_PATH)
print(f"Backup of commentary created at {BACKUP_PATH}")
if os.path.exists(SECTIONS_PATH):
    shutil.copy2(SECTIONS_PATH, SECTIONS_BACKUP_PATH)
    print(f"Backup of sections created at {SECTIONS_BACKUP_PATH}")

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

# Process blocks
formatted_blocks = []
current_chapter = 0
subheading_counter = 0
block_counter = 0
id_map = {}  # Map original paragraph ID to new block ID

for block in raw_paragraphs:
    # Check if block is a heading
    if block.startswith("#"):
        # Determine heading level
        if block.startswith("## "):
            heading_text = block[3:].strip()
            # Determine chapter number
            if "སྔོན་འགྲོ" in heading_text:
                current_chapter = 0
            elif "མཇུག་གི་དོན" in heading_text:
                current_chapter = 11
            else:
                # Try to find number at start of heading
                num_match = re.match(r"^(\d+)\.", heading_text)
                if num_match:
                    current_chapter = int(num_match.group(1))
                else:
                    current_chapter = 0
            subheading_counter = 0
            block_counter = 0
        elif block.startswith("### "):
            subheading_counter += 1
            block_counter = 0  # Restart sequence under new Level 3 heading
            
        formatted_blocks.append(block)
        continue

    # It's a text paragraph.
    # Check if it ends with a block ID
    para_id = None
    para_text = block
    id_match = re.search(r'\s*\^(\d+)$', block)
    if id_match:
        para_id = int(id_match.group(1))
        para_text = block[:id_match.start()].strip()
        
    # Determine chapter if para_id is present
    if para_id is not None:
        ch = get_chapter(para_id)
        if ch != current_chapter:
            current_chapter = ch
            # We don't write a new chapter heading here because they are already written in the source
            subheading_counter = 0
            block_counter = 0

    # Clean up Latin prefixes
    para_text = clean_latin_prefixes(para_text)
    
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
            
        # Map original paragraph ID to the first sub-block's ID
        if idx == 0 and para_id is not None:
            id_map[para_id] = bid[1:]  # strip the caret for mapping
            
        # Prepend original paragraph number to the first block
        prefix = f"{para_id}. " if (idx == 0 and para_id is not None) else ""
        
        # Append block ID to the very end of the text block
        lines = block_text.split('\n')
        lines[-1] = f"{lines[-1]} {bid}"
        formatted_block_text = "\n".join(lines)
        
        formatted_blocks.append(f"{prefix}{formatted_block_text}")

# Join blocks with double newlines
formatted_body = "\n\n".join(formatted_blocks)

# Write formatted commentary
with open(FILE_PATH, "w", encoding="utf-8") as f:
    f.write(frontmatter + "\n\n" + formatted_body + "\n")

print(f"Successfully formatted commentary and saved to {FILE_PATH}")
print(f"Original size: {len(raw_content)} bytes")
print(f"New size: {len(formatted_body)} bytes")

# Update links in sections file if it exists
if os.path.exists(SECTIONS_PATH):
    print(f"Updating links in {SECTIONS_PATH}...")
    with open(SECTIONS_PATH, "r", encoding="utf-8") as f:
        sections_content = f.read()
        
    updated_sections_content = sections_content
    # Find all links of the form bo-རྒྱལ་ཚབ་དར་མ་རིན་ཆེན།.md#^para_id
    # and replace them with the new block IDs
    link_pattern = r'bo-རྒྱལ་ཚབ་དར་མ་རིན་ཆེན།\.md#\^(\d+)'
    matches = re.findall(link_pattern, sections_content)
    
    replacements_made = 0
    for para_str in set(matches):
        para_id = int(para_str)
        if para_id in id_map:
            old_link = f"bo-རྒྱལ་ཚབ་དར་མ་རིན་ཆེན།.md#^{para_id}"
            new_link = f"bo-རྒྱལ་ཚབ་དར་མ་རིན་ཆེན།.md#^{id_map[para_id]}"
            updated_sections_content = updated_sections_content.replace(old_link, new_link)
            replacements_made += 1
            
    with open(SECTIONS_PATH, "w", encoding="utf-8") as f:
        f.write(updated_sections_content)
        
    print(f"Successfully updated {replacements_made} links in {SECTIONS_PATH}")
else:
    print(f"Sections file not found at {SECTIONS_PATH}, skipping link updates.")
