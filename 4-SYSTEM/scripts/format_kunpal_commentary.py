#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Format Khenpo Kunpal's Tibetan commentary according to the format-commentary skill.
Input/Output: 1-SOURCES/Commentaries/bo-མཁན་པོ་ཀུན་དཔལ།.md
"""

import re
import os
import sys
import shutil

# Define paths relative to this script
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
VAULT_ROOT = os.path.abspath(os.path.join(SCRIPT_DIR, "..", ".."))
FILE_PATH = os.path.join(VAULT_ROOT, "1-SOURCES", "Commentaries", "bo-མཁན་པོ་ཀུན་དཔལ།.md")
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

# Split body into lines/paragraphs
paragraphs = body.split("\n\n")
print(f"Read {len(paragraphs)} raw paragraphs.")

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
    if 2 <= paragraph_id <= 9:
        return 0
    elif 10 <= paragraph_id <= 41:
        return 1
    elif 42 <= paragraph_id <= 109:
        return 2
    elif 110 <= paragraph_id <= 145:
        return 3
    elif 146 <= paragraph_id <= 196:
        return 4
    elif 197 <= paragraph_id <= 309:
        return 5
    elif 310 <= paragraph_id <= 450:
        return 6
    elif 451 <= paragraph_id <= 530:
        return 7
    elif 531 <= paragraph_id <= 718:
        return 8
    elif 719 <= paragraph_id <= 894:
        return 9
    elif 895 <= paragraph_id <= 955:
        return 10
    elif 956 <= paragraph_id <= 961:
        return 11
    return 0

def clean_latin_prefixes(text):
    # Remove Latin prefixes immediately preceding Tibetan letters
    return re.sub(r'([a-zA-Z])([\u0F00-\u0FFF])', r'\2', text)

def split_paragraph_to_blocks(text):
    # Normalize spaces
    text = re.sub(r'\s+', ' ', text).strip()
    
    # Split by '། །' or '།།' to detect verse lines vs prose
    parts = re.split(r'(?<=[།])\s+', text)
    
    blocks = []
    current_stanza = []
    
    for part in parts:
        part = part.strip()
        if not part:
            continue
        
        # A verse line is typically short (< 65 chars) and ends with a shad '།'
        is_verse_line = len(part) < 65 and part.endswith('།')
        
        if is_verse_line:
            current_stanza.append(part)
            if len(current_stanza) == 4:
                blocks.append(("\n".join(current_stanza), "verse"))
                current_stanza = []
        else:
            if current_stanza:
                blocks.append((" ".join(current_stanza), "prose"))
                current_stanza = []
            blocks.append((part, "prose"))
            
    if current_stanza:
        blocks.append((" ".join(current_stanza), "prose"))
        
    # Group adjacent prose blocks into sentences, or split them if they are too long
    final_blocks = []
    current_prose_parts = []
    
    for block_text, block_type in blocks:
        if block_type == "verse":
            if current_prose_parts:
                final_blocks.append((" ".join(current_prose_parts), "prose"))
                current_prose_parts = []
            final_blocks.append((block_text, "verse"))
        else:
            current_prose_parts.append(block_text)
            if block_text.endswith('། །') or block_text.endswith('།།') or block_text.endswith('།'):
                accumulated_text = " ".join(current_prose_parts)
                # Flush if accumulated text is reasonably long
                if len(accumulated_text) > 150 or any(block_text.endswith(end) for end in ['ལོ། །', 'སོ། །', 'གསུངས། །', 'ཞེས་སོ། །', 'ཞེས་བྱའོ། །']):
                    final_blocks.append((accumulated_text, "prose"))
                    current_prose_parts = []
                    
    if current_prose_parts:
        final_blocks.append((" ".join(current_prose_parts), "prose"))
        
    return final_blocks

def format_quotes(text):
    """
    Format quotes by putting source references and concluding remarks on their own lines.
    """
    # Pattern to find source reference like "སྡུད་པ་ལས།" or "ཇི་སྐད་དུ།"
    # and concluding remarks like "ཞེས་སོ། །" or "ཞེས་བྱ་བའོ། །"
    text = re.sub(r'(ཇི་སྐད་དུ།|སྡུད་པ་ལས།|ལས།|གསུངས་པ།)\s*', r'\1\n', text)
    text = re.sub(r'\s*(ཞེས་སོ། །|ཞེས་བྱ་བའོ། །|ཞེས་པ་བཞིན་ནོ། །)', r'\n\1', text)
    return text

# Process paragraphs
formatted_blocks = []
current_chapter = -1
block_counters = {}  # Track relative block IDs per chapter

# Add main title
formatted_blocks.append("# བྱང་ཆུབ་སེམས་དཔའི་སྤྱོད་པ་ལ་འཇུག་པའི་ཚིག་འགྲེལ་འཇམ་དབྱངས་བླ་མའི་ཞལ་ལུང་བདུད་རྩིའི་ཐིག་པ།")

for para in paragraphs:
    para = para.strip()
    if not para:
        continue
    
    # Try to match leading paragraph number (e.g. "2. ༄༅། །...")
    match = re.match(r"^(\d+)\.\s*(.*)", para, re.DOTALL)
    if not match:
        # Verbatim line (e.g. headings or empty lines)
        if para.startswith("#"):
            formatted_blocks.append(para)
        else:
            cleaned = clean_latin_prefixes(para)
            formatted_blocks.append(cleaned)
        continue
    
    para_id = int(match.group(1))
    para_text = match.group(2).strip()
    
    # Check chapter boundary
    ch = get_chapter(para_id)
    if ch != current_chapter:
        current_chapter = ch
        formatted_blocks.append(CHAPTER_HEADINGS[ch])
        block_counters[ch] = 0
        
    # Split paragraph into logical blocks
    sub_blocks = split_paragraph_to_blocks(para_text)
    
    for idx, (block_text, block_type) in enumerate(sub_blocks):
        block_counters[current_chapter] += 1
        seq = block_counters[current_chapter]
        
        # Clean up Latin prefixes and format quotes
        block_text = clean_latin_prefixes(block_text)
        if block_type == "prose":
            block_text = format_quotes(block_text)
            
        # Add relative block ID
        bid = f"^{current_chapter}-{seq}"
        
        # If it's the first sub-block, prepend the original paragraph number
        prefix = f"{para_id}. " if idx == 0 else ""
        
        # Ensure the block ID is at the very end of the text block
        # For multiline blocks (like verses or formatted quotes), we append to the last line
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
