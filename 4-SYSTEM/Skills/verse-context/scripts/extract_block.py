#!/usr/bin/env python3
"""Extract the content of one or more `^block-id` blocks from an Obsidian markdown
file. Used by the LLM-fill step of the verse-context workflow so a sub-agent can
read just the commentary paragraphs it needs without loading the entire file.

Usage:
    python extract_block.py <file> <block-id> [<block-id> ...]
"""
import re
import sys
from pathlib import Path

def extract(text: str, block_id: str) -> str:
    """Return the paragraph (text between surrounding blank lines) that ends
    with `^<block_id>`. If the block ID appears mid-paragraph, returns the
    enclosing paragraph anyway. Returns an empty string if not found.
    """
    pat = re.compile(rf"\^{re.escape(block_id)}\b")
    m = pat.search(text)
    if not m:
        return ""
    # Find paragraph boundaries — blank lines on either side
    start = text.rfind("\n\n", 0, m.start())
    start = 0 if start == -1 else start + 2
    end = text.find("\n\n", m.end())
    end = len(text) if end == -1 else end
    return text[start:end].strip()

def main(argv: list[str]) -> int:
    if len(argv) < 3:
        print(__doc__, file=sys.stderr)
        return 2
    path = Path(argv[1])
    text = path.read_text(encoding="utf-8")
    for bid in argv[2:]:
        block = extract(text, bid)
        print(f"--- ^{bid} ---")
        if not block:
            print(f"(block ^{bid} not found in {path})")
        else:
            print(block)
        print()
    return 0

if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
