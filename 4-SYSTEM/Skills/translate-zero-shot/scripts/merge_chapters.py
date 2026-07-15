#!/usr/bin/env python3
"""Deterministically merge Chapter-NN.md files of a zero-shot translation
track into one full-text file.

Usage:
    python merge_chapters.py <track_dir> --track <track> --title <title> \
        --output <filename> [--chapters 1-10]

Behaviour:
- Collects Chapter-NN.md files (NN = 01..10) in numeric order.
- Strips each chapter's YAML frontmatter and any preamble before the first
  "## " heading (removes the Chapter-1-only title block).
- Aggregates context_packages from all chapter frontmatters (unique, ordered).
- Refuses to merge if a requested chapter is missing or if any verse block ID
  (^N-V at end of line) appears more than once across the merged body.
- Writes <track_dir>/<output> with status: draft frontmatter.

Exit codes: 0 = merged, 1 = validation error.
"""

import argparse
import datetime
import re
import sys
from pathlib import Path

BLOCK_ID_RE = re.compile(r"\^([0-9A-Za-z]+-[0-9A-Za-z]+)\s*$", re.MULTILINE)


def parse_chapter(path: Path):
    """Return (frontmatter_lines, body) with frontmatter stripped."""
    text = path.read_text(encoding="utf-8")
    fm: list[str] = []
    body = text
    if text.startswith("---"):
        parts = text.split("---", 2)
        if len(parts) >= 3:
            fm = parts[1].strip().splitlines()
            body = parts[2]
    # Drop everything before the first "## " heading (chapter-1 title block).
    m = re.search(r"^## ", body, re.MULTILINE)
    if not m:
        sys.exit(f"ERROR: {path.name}: no '## ' chapter heading found.")
    return fm, body[m.start():].rstrip() + "\n"


def context_packages(fm_lines):
    """Extract '- ...' items under 'context_packages:' from frontmatter lines."""
    items, active = [], False
    for line in fm_lines:
        if line.strip().startswith("context_packages:"):
            active = True
            continue
        if active:
            s = line.strip()
            if s.startswith("- "):
                items.append(s[2:].strip())
            elif s and not line.startswith(" "):
                active = False
    return items


def parse_scope(scope: str):
    scope = scope.strip()
    if scope.lower() == "all":
        return list(range(1, 11))
    if "-" in scope:
        a, b = scope.split("-", 1)
        return list(range(int(a), int(b) + 1))
    return [int(scope)]


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("track_dir")
    ap.add_argument("--track", required=True)
    ap.add_argument("--title", required=True)
    ap.add_argument("--output", required=True)
    ap.add_argument("--chapters", default="all", help="e.g. 'all', '1-3', '7'")
    args = ap.parse_args()

    track_dir = Path(args.track_dir)
    if not track_dir.is_dir():
        sys.exit(f"ERROR: track dir not found: {track_dir}")

    chapters = parse_scope(args.chapters)
    missing = [n for n in chapters if not (track_dir / f"Chapter-{n:02d}.md").exists()]
    if missing:
        sys.exit(f"ERROR: missing chapter files: {', '.join(f'Chapter-{n:02d}.md' for n in missing)}")

    bodies, packages, seen_ids, dupes = [], [], {}, []
    for n in chapters:
        path = track_dir / f"Chapter-{n:02d}.md"
        fm, body = parse_chapter(path)
        for p in context_packages(fm):
            if p not in packages:
                packages.append(p)
        for bid in BLOCK_ID_RE.findall(body):
            if bid in seen_ids:
                dupes.append(f"^{bid} (in {seen_ids[bid]} and {path.name})")
            else:
                seen_ids[bid] = path.name
        bodies.append(body)
        print(f"  Chapter {n:02d}: {len(BLOCK_ID_RE.findall(body))} verse blocks")

    if dupes:
        sys.exit("ERROR: duplicate block IDs across chapters:\n  " + "\n  ".join(dupes))

    today = datetime.date.today().isoformat()
    fm_out = ["---",
              f'title: "{args.title}"',
              "transformation_type: translation",
              f"track: {args.track}",
              "context_packages:"]
    fm_out += [f"  - {p}" for p in packages]
    fm_out += [f"merged_chapters: {chapters[0]}-{chapters[-1]}",
               f"generation_date: {today}",
               "status: draft",
               "---", ""]

    out = "\n".join(fm_out) + f"# {args.title}\n\n---\n\n" + "\n\n---\n\n".join(bodies)
    out_path = track_dir / args.output
    out_path.write_text(out, encoding="utf-8")
    print(f"Merged {len(chapters)} chapters, {len(seen_ids)} verse blocks -> {out_path}")


if __name__ == "__main__":
    main()
