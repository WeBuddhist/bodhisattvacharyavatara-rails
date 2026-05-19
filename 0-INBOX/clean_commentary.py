import re

def clean_text(text):
    # Remove common punctuation and whitespace for comparison
    return re.sub(r'[，。！？；：、\s\t]', '', text)

def solve():
    # Read root text
    with open('1-SOURCES/Translations/zh-隆蓮法師.md', 'r', encoding='utf-8') as f:
        root_content = f.read()
    
    # Extract phrases from root text
    # Lines starting with numbers are verses
    root_phrases = set()
    lines = root_content.split('\n')
    for line in lines:
        line = line.strip()
        if not line: continue
        # Match lines like "1. text" or "10. text"
        match = re.match(r'^\d+\.\s*(.*)', line)
        if match:
            text = match.group(1)
            # Split by spaces to get phrases
            parts = re.split(r'\s+', text)
            for p in parts:
                p_clean = clean_text(p)
                if p_clean:
                    root_phrases.add(p_clean)
        else:
            # Also check for lines that don't start with numbers but might be verses (like in Chapter headers or if numbers are missing)
            # But based on the file content, they are numbered.
            pass

    # Read commentary
    with open('1-SOURCES/Commentaries/zh-賈曹傑 入菩薩行論廣解.md', 'r', encoding='utf-8') as f:
        comm_lines = f.readlines()

    new_comm_lines = []
    
    # Process commentary lines
    for line in comm_lines:
        stripped_line = line.strip()
        if not stripped_line:
            new_comm_lines.append(line)
            continue
        
        # Check if the line is a header (starts with # or 甲, 乙, etc.)
        if stripped_line.startswith('#') or re.match(r'^[甲乙丙丁戊己庚辛壬癸][一二三四五六七八九十]', stripped_line):
            new_comm_lines.append(line)
            continue

        # Check if the whole line consists of root phrases
        # We split the line by punctuation to check each part
        line_parts = re.split(r'([，。！？；：、\s\t]+)', stripped_line)
        
        is_verse_line = True
        has_phrase = False
        
        # A verse line should consist of known phrases + punctuation
        # If any part (that is not punctuation) is not a known phrase, then it's likely commentary
        for part in line_parts:
            p_clean = clean_text(part)
            if not p_clean: # Skip punctuation/whitespace
                continue
            
            if p_clean in root_phrases:
                has_phrase = True
            else:
                is_verse_line = False
                break
        
        if is_verse_line and has_phrase:
            # This is a verse line, skip it
            continue
        else:
            new_comm_lines.append(line)

    # Some lines might have been missed if they are long or have weird formatting.
    # Let's check the first few lines of the output to verify.
    
    output = "".join(new_comm_lines)
    
    # Write back to file
    with open('1-SOURCES/Commentaries/zh-賈曹傑 入菩薩行論廣解.md', 'w', encoding='utf-8') as f:
        f.write(output)

# solve() # This is a script, I will run the logic in my thought process and use tools.
