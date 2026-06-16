#!/usr/bin/env python3
"""
Move Tibetan outline phrases from end of paragraphs to beginning of next paragraph.
"""

import re
import shutil

INPUT_PATH = r"C:\Users\tiger\Obsidian\bodhisattvacharyavatara-rails\1-SOURCES\Commentaries\bo-མཁན་པོ་ཀུན་དགའ་དབང་ཕྱུག.md"
BACKUP_PATH = INPUT_PATH + ".bak"

def process(content):
    lines = content.split('\n')
    result = []
    pending_outline = None
    moves = 0

    for line in lines:
        if pending_outline is not None and line.strip():
            line = pending_outline + ' ' + line
            pending_outline = None

        match = re.search(r'(།\s*།[^།\n]*?ནི།)\s*$', line)
        if match:
            outline = match.group(1)
            line = line[:match.start()].rstrip()
            pending_outline = outline
            moves += 1

        result.append(line)

    if pending_outline:
        result.append(pending_outline)

    print(f"Moved {moves} outline phrase(s).")
    return '\n'.join(result)

def main():
    with open(INPUT_PATH, 'r', encoding='utf-8') as f:
        original = f.read()

    shutil.copy2(INPUT_PATH, BACKUP_PATH)
    print(f"Backup saved to: {BACKUP_PATH}")

    processed = process(original)

    with open(INPUT_PATH, 'w', encoding='utf-8') as f:
        f.write(processed)

    print("Done.")

if __name__ == '__main__':
    main()
