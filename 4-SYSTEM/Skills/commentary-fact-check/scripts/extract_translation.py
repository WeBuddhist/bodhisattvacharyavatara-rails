#!/usr/bin/env python3
"""
Parse a graded English BCA translation file (one verse per block, English text
followed by its block ID: `{text} ^{verse_id}`) into a {verse_id: text} dict,
optionally filtered to one chapter.

Usage:
    python3 extract_translation.py <bca-en-<grade>.md> [--chapter 1] [--json out.json]
"""
import argparse
import json
import re


def parse(content):
    verses = {}
    for line in content.splitlines():
        line = line.strip()
        if not line:
            continue
        m = re.search(r"^\s*(?:#+\s*)?(.*?)\s*\^([a-zA-Z0-9-]+)\s*$", line)
        if not m:
            continue
        text, vid = m.group(1).strip(), m.group(2)
        verses[vid] = text
    return verses


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("translation", help="Path to the graded translation .md file")
    ap.add_argument("--chapter", default=None, help="Restrict output to one chapter (e.g. 1, or 'a'/'b' for colophon)")
    ap.add_argument("--json", default=None, help="Write filtered {verse_id: text} JSON to this path")
    args = ap.parse_args()

    content = open(args.translation, encoding="utf-8").read()
    verses = parse(content)

    if args.chapter is not None:
        verses = {vid: t for vid, t in verses.items() if vid.split("-")[0] == args.chapter}

    print(f"Parsed {len(verses)} verse blocks" + (f" for chapter {args.chapter}" if args.chapter else ""))

    if args.json:
        with open(args.json, "w", encoding="utf-8") as f:
            json.dump(verses, f, ensure_ascii=False, indent=2)
        print(f"Wrote to {args.json}")
    else:
        for vid in sorted(verses, key=lambda v: [int(p) if p.isdigit() else p for p in v.split("-")]):
            print(f"{vid}: {verses[vid]}")


if __name__ == "__main__":
    main()
