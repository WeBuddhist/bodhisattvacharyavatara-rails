#!/usr/bin/env python3
"""
insert_tags.py — Insert hashtags under specific verses in a root-text file.

Given the original root-text markdown file and a JSON mapping of
verse_id -> [tags], this writes a new file with each listed verse's tags
inserted as their own paragraph directly below that verse's block
reference (^chapter-verse line), e.g.:

    བྱང་ཆུབ་སེམས་ཞེས་བྱ་བ་རབ་བརྟན་ཟུང་། ། ^1-10

    #ཚིག་ངན་བཟོད་པ། #མི་ཁ་བཟོད་པ།

    ![[.../root-source.md#^1-11]]
    ...

Only verses present in the mapping are touched. Everything else in the
file — frontmatter, headings, transclusion embeds, verse text, spacing —
is left byte-for-byte identical. This script never overwrites the input
file; it always writes to -o/--output.

mapping.json format:
    { "1-1": ["#tag_a", "#tag_b"], "6-14": ["#tag_c"] }

Usage:
    python insert_tags.py <root_file.md> <mapping.json> -o <output_file.md>
"""
import argparse
import json
import sys
from pathlib import Path

# Reuse the same block-boundary parser as extract_verses.py so insertion
# points are always computed identically to how verses were identified.
sys.path.insert(0, str(Path(__file__).parent))
from extract_verses import parse_verses


def insert_tags(text: str, mapping: dict):
    lines = text.splitlines()
    verses = parse_verses(text)
    by_id = {v["verse_id"]: v for v in verses}

    missing = [vid for vid in mapping if vid not in by_id]
    if missing:
        print(f"WARNING: these verse_ids in the mapping were not found in the file and will be skipped: {missing}", file=sys.stderr)

    # Insert from the bottom of the file upward so earlier line indices stay valid.
    insertions = []  # (end_line, [new_lines])
    for vid, tags in mapping.items():
        if vid not in by_id or not tags:
            continue
        clean_tags = [t if t.startswith("#") else f"#{t}" for t in tags]
        insertions.append((by_id[vid]["end_line"], ["", " ".join(clean_tags)]))

    insertions.sort(key=lambda x: x[0], reverse=True)

    for end_line, new_lines in insertions:
        insert_at = end_line + 1
        lines[insert_at:insert_at] = new_lines

    return "\n".join(lines) + "\n", len(insertions), len(mapping) - len(insertions)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("root_file", help="Path to the original root-text translation markdown file")
    ap.add_argument("mapping_file", help="Path to a JSON file mapping verse_id -> [tags]")
    ap.add_argument("-o", "--output", required=True, help="Output path for the tagged file (never overwrites the input)")
    args = ap.parse_args()

    root_path = Path(args.root_file)
    mapping_path = Path(args.mapping_file)
    out_path = Path(args.output)

    if out_path.resolve() == root_path.resolve():
        print("ERROR: output path must differ from the input root file (this script never edits in place).", file=sys.stderr)
        sys.exit(1)

    text = root_path.read_text(encoding="utf-8")
    mapping = json.loads(mapping_path.read_text(encoding="utf-8"))

    new_text, applied, skipped = insert_tags(text, mapping)
    out_path.write_text(new_text, encoding="utf-8")
    print(f"Inserted tags for {applied} verse(s) into {out_path} ({skipped} skipped/not found).", file=sys.stderr)


if __name__ == "__main__":
    main()
