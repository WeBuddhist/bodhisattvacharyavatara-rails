#!/usr/bin/env python3
"""
fix-shad-spacing-bo-spyod-jug-srung-grel.py
Adds a space after every single shad (།) that is immediately followed
by a non-space, non-shad, non-newline character.
Does NOT touch double-shad sequences (།།) or shads already followed by a space.

Source:  1-SOURCES/Commentaries/bo-སྤྱོད་འཇུག་སྒྲུང་འགྲེལ།.md
Output:  0-INBOX/bo-spyod-jug-srung-grel-shad-fixed.md
"""
import re
from pathlib import Path

SOURCE = Path("/sessions/festive-funny-dirac/mnt/bodhisattvacharyavatara-rails/1-SOURCES/Commentaries/bo-སྤྱོད་འཇུག་སྒྲུང་འགྲེལ།.md")
OUTPUT = Path("/sessions/festive-funny-dirac/mnt/bodhisattvacharyavatara-rails/0-INBOX/bo-spyod-jug-srung-grel-shad-fixed.md")

# Match a single shad NOT followed by space, another shad, or newline
PATTERN = re.compile(r'།([^ །\n])')

def fix(text: str) -> tuple[str, int]:
    count = [0]
    def repl(m):
        count[0] += 1
        return '། ' + m.group(1)
    result = PATTERN.sub(repl, text)
    return result, count[0]

if __name__ == '__main__':
    text = SOURCE.read_text(encoding='utf-8')
    fixed, n = fix(text)
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(fixed, encoding='utf-8')
    print(f"Replacements made: {n}")
    print(f"Written to: {OUTPUT}")
