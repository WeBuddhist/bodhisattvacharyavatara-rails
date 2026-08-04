#!/usr/bin/env python3
"""
extract_tags.py — Parse a Tibetan hashtag/tag-list file into structured JSON.

The tag list is organized as one or more sections, each starting with a
markdown heading (###) that names a category (usually Tibetan + an English
gloss in parentheses), followed by a short description paragraph, followed
by a two-column pipe table:

    | མཚན་རྟགས། (Tags) | གང་ལ་སྦྱར་བའི་གནས་སྐབས། (Application) |
    | --- | --- |
    | `#ཚིག་ངན་བཟོད་པ།` | གཞན་གྱིས་ཚིག་རྩུབ་... |

Blank lines are sometimes present between table rows (an Obsidian export
quirk) — this parser tolerates that by matching table rows anywhere in the
file rather than requiring contiguous lines.

Usage:
    python extract_tags.py <tags_file.md> -o tags.json
"""
import argparse
import json
import re
import sys
from pathlib import Path

HEADING_RE = re.compile(r"^#{2,4}\s+(.+?)\s*$")
# A table row that isn't the header/separator row. Captures the tag cell and
# the application/context cell. Tag cell may or may not be backtick-quoted.
ROW_RE = re.compile(
    r"^\|\s*`?(#\S+?)`?\s*\|\s*(.+?)\s*\|\s*$"
)
SEPARATOR_RE = re.compile(r"^\|\s*-+\s*\|")
HEADER_ROW_RE = re.compile(r"^\|\s*.*Tags.*\|")


def parse_tags(text: str):
    lines = text.splitlines()
    current_category = None
    tags = []
    seen = set()

    for line in lines:
        h = HEADING_RE.match(line)
        if h:
            current_category = h.group(1).strip()
            continue

        if SEPARATOR_RE.match(line) or HEADER_ROW_RE.match(line):
            continue

        m = ROW_RE.match(line)
        if m:
            tag = m.group(1).strip()
            application = m.group(2).strip()
            # Skip accidental matches on the header row itself
            if "Tags" in tag or "Application" in application and tag.startswith("#") is False:
                pass
            key = (current_category, tag)
            if tag.startswith("#") and key not in seen:
                seen.add(key)
                tags.append({
                    "category": current_category,
                    "tag": tag,
                    "application": application,
                })
    return tags


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("tags_file", help="Path to the hashtag list markdown file")
    ap.add_argument("-o", "--output", default=None, help="Output JSON path (default: stdout)")
    args = ap.parse_args()

    path = Path(args.tags_file)
    text = path.read_text(encoding="utf-8")
    tags = parse_tags(text)

    if not tags:
        print(f"WARNING: no tags parsed from {path}. Check the table format.", file=sys.stderr)

    categories = sorted(set(t["category"] for t in tags if t["category"]))
    result = {
        "source_file": str(path),
        "tag_count": len(tags),
        "categories": categories,
        "tags": tags,
    }

    out_text = json.dumps(result, ensure_ascii=False, indent=2)
    if args.output:
        Path(args.output).write_text(out_text, encoding="utf-8")
        print(f"Wrote {len(tags)} tags across {len(categories)} categories to {args.output}", file=sys.stderr)
    else:
        print(out_text)


if __name__ == "__main__":
    main()
