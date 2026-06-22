import re

src = "/sessions/modest-happy-brown/mnt/bodhisattvacharyavatara-rails/1-SOURCES/Commentaries/bo-སྤྱོད་འཇུག་སྒྲུང་འགྲེལ།.md"
dst = "/sessions/modest-happy-brown/mnt/bodhisattvacharyavatara-rails/0-INBOX/temp/sgrung-grel-split.md"

with open(src, encoding='utf-8', errors='replace') as f:
    lines = f.readlines()

orig_count = len(lines)
text = ''.join(lines)

# Patterns to split onto new lines — longer combos first to avoid partial matches
chapter_markers = [
    'ཀ༡༠', 'ཀ༡༡', 'ཀ༡༢',
    'ཀ༡', 'ཀ༢', 'ཀ༣', 'ཀ༤', 'ཀ༥', 'ཀ༦', 'ཀ༧', 'ཀ༨', 'ཀ༩',
]

ordinal_announcements = [
    'དང་པོ་ནི།', 'གཉིས་པ་ནི།', 'གསུམ་པ་ནི།',  # connectors first (longer)
    'དང་པོ།', 'གཉིས་པ།', 'གསུམ་པ།', 'བཞི་པ།', 'ལྔ་པ།',
    'དྲུག་པ།', 'བདུན་པ།', 'བརྒྱད་པ།', 'དགུ་པ།', 'བཅུ་པ།',
]

auspicious = ['༈']

all_markers = chapter_markers + ordinal_announcements + auspicious

for marker in all_markers:
    escaped = re.escape(marker)
    text = re.sub(r'(?<!\n)(' + escaped + r')', r'\n\1', text)

# Arabic/Indic numbered-entry patterns: digit(s) followed by ". "
text = re.sub(r'(?<!\n)(\d+\. )', r'\n\1', text)

# Collapse 4+ consecutive newlines to 3 (= 2 blank lines)
text = re.sub(r'\n{4,}', '\n\n\n', text)

new_count = text.count('\n')

with open(dst, 'w', encoding='utf-8') as f:
    f.write(text)

print(f"Original line count: {orig_count}")
print(f"New line count:      {new_count}")
print(f"Written to: {dst}")
