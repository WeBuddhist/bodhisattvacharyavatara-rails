#!/usr/bin/env python3
"""
extract_verses.py — Parse a root-text translation markdown file into
structured JSON, one entry per verse (stanza).

Expected file shape (Obsidian vault convention used by this project):

    ---
    ...yaml frontmatter, including verse_id_format: chapter-verse...
    ---
    # <title> ^0

    ## 1. <chapter title> ^1-0

    ![[.../root-source.md#^1-1]]

    <pada line 1>
    <pada line 2>
    <pada line 3>
    <pada line 4> ^1-1

    ![[.../root-source.md#^1-2]]
    ...

Each verse is identified by a `^<chapter>-<verse>` block reference at the
end of its final line. Everything else (frontmatter, headings, transclusion
embeds, blank lines) is structural scaffolding and is not treated as verse
text. Non-numeric anchors (e.g. `^I-1` used for front-matter/homage lines
before chapter 1) are recognized as block boundaries but are NOT emitted as
verses, since they are not root verses proper.

Usage:
    python extract_verses.py <root_file.md> -o verses.json [--chapter N]
"""
import argparse
import json
import re
import sys
from pathlib import Path

HEADING_RE = re.compile(r"^#{1,6}\s")
CHAPTER_HEADING_RE = re.compile(r"^##\s+(\d+)\.")
TRANSCLUSION_RE = re.compile(r"^!\[\[")
ANCHOR_RE = re.compile(r"\^([^\s\^]+)\s*$")
NUMERIC_ANCHOR_RE = re.compile(r"^(\d+)-(\d+)$")


def parse_verses(text: str):
    lines = text.splitlines()
    verses = []
    buffer = []  # list of (line_idx, text)
    in_frontmatter = False
    frontmatter_delims_seen = 0
    current_chapter = None

    for idx, raw_line in enumerate(lines):
        line = raw_line.rstrip("\n")
        stripped = line.strip()

        # Frontmatter handling: skip everything between the first two '---' lines.
        if stripped == "---" and frontmatter_delims_seen < 2:
            frontmatter_delims_seen += 1
            in_frontmatter = frontmatter_delims_seen == 1
            continue
        if in_frontmatter:
            continue

        if stripped == "":
            continue  # blank lines are pure separators

        if HEADING_RE.match(line):
            ch = CHAPTER_HEADING_RE.match(line)
            if ch:
                current_chapter = int(ch.group(1))
            buffer = []  # discard any dangling unanchored content (e.g. homage lines)
            continue

        if TRANSCLUSION_RE.match(stripped):
            continue  # source-text embed marker, not verse content

        # Otherwise: this is verse content.
        buffer.append((idx, line))

        m = ANCHOR_RE.search(line)
        if m:
            anchor = m.group(1)
            num = NUMERIC_ANCHOR_RE.match(anchor)
            if num:
                chapter, verse = int(num.group(1)), int(num.group(2))
                verse_id = f"{chapter}-{verse}"
                # strip the anchor off the last line's text
                last_idx, last_text = buffer[-1]
                clean_last = re.sub(r"\s*\^" + re.escape(anchor) + r"\s*$", "", last_text).rstrip()
                clean_lines = [t for _, t in buffer[:-1]] + [clean_last]
                verses.append({
                    "verse_id": verse_id,
                    "chapter": chapter,
                    "verse": verse,
                    "text": " ".join(l.strip() for l in clean_lines),
                    "lines": clean_lines,
                    "start_line": buffer[0][0],
                    "end_line": last_idx,
                })
            # Whether numeric or not, the anchor closes this block.
            buffer = []

    return verses


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("root_file", help="Path to the root-text translation markdown file")
    ap.add_argument("-o", "--output", default=None, help="Output JSON path (default: stdout)")
    ap.add_argument("--chapter", type=int, default=None, help="Only include verses from this chapter number")
    args = ap.parse_args()

    path = Path(args.root_file)
    text = path.read_text(encoding="utf-8")
    verses = parse_verses(text)

    if args.chapter is not None:
        verses = [v for v in verses if v["chapter"] == args.chapter]

    if not verses:
        print(f"WARNING: no verses parsed from {path}" + (f" for chapter {args.chapter}" if args.chapter else "") + ". Check the file format.", file=sys.stderr)

    chapters = sorted(set(v["chapter"] for v in verses))
    result = {
        "source_file": str(path),
        "verse_count": len(verses),
        "chapters": chapters,
        "verses": verses,
    }

    out_text = json.dumps(result, ensure_ascii=False, indent=2)
    if args.output:
        Path(args.output).write_text(out_text, encoding="utf-8")
        print(f"Wrote {len(verses)} verses (chapters {chapters}) to {args.output}", file=sys.stderr)
    else:
        print(out_text)


if __name__ == "__main__":
    main()
