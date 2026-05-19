import re

def clean_text(text):
    # Remove numbering like "1. ", "2. "
    text = re.sub(r'^\s*\d+\.\s*', '', text, flags=re.MULTILINE)
    # Split into lines
    lines = text.split('\n')
    phrases = []
    for line in lines:
        # Split by spaces (2 or more)
        parts = re.split(r'\s{2,}', line.strip())
        for p in parts:
            if p:
                phrases.append(p.strip())
    return phrases

# Read root text
with open('1-SOURCES/Translations/zh-隆蓮法師.md', 'r', encoding='utf-8') as f:
    root_content = f.read()

# Extract segments
# The segments are usually 7 or 9 characters.
# Let's just use the space-separated parts.
root_phrases = clean_text(root_content)

# Filter out very short things or headers
root_phrases = [p for p in root_phrases if len(p) >= 4]

# Read commentary
with open('1-SOURCES/Commentaries/zh-賈曹傑 入菩薩行論廣解.md', 'r', encoding='utf-8') as f:
    comm_lines = f.readlines()

new_lines = []
for line in comm_lines:
    stripped = line.strip()
    if not stripped:
        new_lines.append(line)
        continue
    
    # Check if the line is an outline (starts with 甲, 乙, 丙, 丁, 戊, 己, 庚, 辛, 壬, 癸, 子, 丑, 寅, 卯, 辰, 巳, 午, 未, 申, 酉, 戌, 亥)
    if re.match(r'^[甲乙丙丁戊己庚辛壬癸子丑寅卯辰巳午未申酉戌亥]\s*[一二三四五六七八九十百]+、', stripped):
        new_lines.append(line)
        continue
    
    # Check if the line is purely composed of root phrases
    # Remove punctuation for comparison
    clean_line = re.sub(r'[，。？！；：、「」『』（）\s]', '', stripped)
    
    is_verse = False
    # If the line is short and matches a phrase
    if clean_line in [re.sub(r'\s', '', p) for p in root_phrases]:
        is_verse = True
    else:
        # Check if it's a combination of phrases
        temp_line = clean_line
        matched_any = False
        while temp_line:
            found = False
            for p in root_phrases:
                cp = re.sub(r'\s', '', p)
                if temp_line.startswith(cp):
                    temp_line = temp_line[len(cp):]
                    found = True
                    matched_any = True
                    break
            if not found:
                break
        if matched_any and not temp_line:
            is_verse = True
            
    if is_verse:
        # Don't add to new_lines
        continue
    else:
        new_lines.append(line)

# Write result
with open('1-SOURCES/Commentaries/zh-賈曹傑 入菩薩行論廣解_cleaned.md', 'w', encoding='utf-8') as f:
    f.writelines(new_lines)
