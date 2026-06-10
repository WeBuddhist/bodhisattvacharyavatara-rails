#!/usr/bin/env python3
# Removes every non-blank line that contains NO Tibetan character
# (Tibetan Unicode block U+0F00-U+0FFF).
# This deletes:
#   - garbage OCR transliteration lines, e.g.  uôh-ºWâG-Vïm-¤ôºÛ-z;º-FÛh-¸Ûm-ƒÛÅü
#   - page-number lines, e.g.  -486-
# Lines containing at least one Tibetan character are kept byte-for-byte.
# Blank lines are kept (preserves paragraph spacing).

import re, shutil, sys
from pathlib import Path

TARGET = Path(r"C:\Users\tiger\Obsidian\bodhisattvacharyavatara-rails\1-SOURCES\Commentaries\bo-རྒྱལ་བ་རིན་པོ་ཆེ།.md")

tibetan = re.compile(r"[ༀ-࿿]")

text = TARGET.read_text(encoding="utf-8")
lines = text.split("\n")

kept, removed = [], []
for ln in lines:
    if ln.strip() == "" or tibetan.search(ln):
        kept.append(ln)          # blank, or contains Tibetan -> keep
    else:
        removed.append(ln)       # non-blank, no Tibetan -> drop

# Safety backup next to the original
backup = TARGET.with_suffix(".md.bak")
shutil.copy2(TARGET, backup)

TARGET.write_text("\n".join(kept), encoding="utf-8")

print(f"Removed {len(removed)} lines. Kept {len(kept)} lines.")
print(f"Backup saved to: {backup}")
print("--- sample of removed lines ---")
for s in removed[:20]:
    print(repr(s))
