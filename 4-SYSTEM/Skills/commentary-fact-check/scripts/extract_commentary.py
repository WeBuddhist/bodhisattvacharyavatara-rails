#!/usr/bin/env python3
"""
Extract per-verse commentary passages from a transcluded Tibetan commentary file.

The commentary interleaves root-text transclusions with its own explanatory prose:

    ![[1-SOURCES/Translations/bo-...#^1-1]]
    <commentary prose for verse 1-1>
    ![[1-SOURCES/Translations/bo-...#^1-2]]
    <commentary prose for verse 1-2>
    ...

This script splits the file on the transclusion markers and attributes the text
between one marker and the next to that marker's verse ID.

Usage:
    python3 extract_commentary.py <commentary.md> [--link-base "1-SOURCES/Translations/bo-..."] [--json out.json]

If --link-base is omitted, the script auto-detects the transclusion base path from
the first transclusion marker found in the file.
"""
import argparse
import json
import re
from collections import defaultdict


def extract(content, link_base):
    if link_base is None:
        probe = re.search(r"!\[\[([^\]#]+)#\^", content)
        if not probe:
            raise ValueError("No transclusion markers found in file; pass --link-base explicitly.")
        link_base = probe.group(1)

    pattern = re.compile(r"!\[\[" + re.escape(link_base) + r"#\^([a-zA-Z0-9-]+)\]\]")
    matches = list(pattern.finditer(content))
    if not matches:
        raise ValueError(f"No transclusion markers matched link_base={link_base!r}")

    passages = {}
    order = []
    for i, m in enumerate(matches):
        vid = m.group(1)
        start = m.end()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(content)
        passages[vid] = content[start:end].strip()
        order.append(vid)

    return passages, order, link_base


def coverage_report(passages, order):
    chapters = defaultdict(list)
    for vid in order:
        ch = vid.split("-")[0]
        chapters[ch].append(vid)

    lines = []
    lines.append(f"Total transclusions: {len(order)}")
    empties = [vid for vid in order if not passages[vid]]
    lines.append(f"Empty passages (extraction artifacts, content merged into the *next* verse's bucket): {len(empties)}")
    if empties:
        lines.append("  " + ", ".join(empties))

    def sort_key(ch):
        return (0, int(ch)) if ch.isdigit() else (1, ch)

    for ch in sorted(chapters, key=sort_key):
        nums = [int(v.split("-")[1]) for v in chapters[ch] if v.split("-")[1].isdigit()]
        if nums:
            lines.append(f"  chapter {ch}: {len(chapters[ch])} verses, {min(nums)}-{max(nums)}")
        else:
            lines.append(f"  chapter {ch}: {len(chapters[ch])} verses (non-numeric ids: {chapters[ch][:5]})")
    return "\n".join(lines)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("commentary", help="Path to the transcluded commentary .md file")
    ap.add_argument("--link-base", default=None, help="Transclusion link base path (auto-detected if omitted)")
    ap.add_argument("--json", default=None, help="Write {verse_id: passage} JSON to this path")
    args = ap.parse_args()

    content = open(args.commentary, encoding="utf-8").read()
    passages, order, link_base = extract(content, args.link_base)

    print(f"link_base: {link_base}")
    print(coverage_report(passages, order))

    if args.json:
        with open(args.json, "w", encoding="utf-8") as f:
            json.dump(passages, f, ensure_ascii=False, indent=2)
        print(f"\nWrote {len(passages)} passages to {args.json}")


if __name__ == "__main__":
    main()
