#!/usr/bin/env python3
"""
remove_transclusions.py

Remove Obsidian transclusion lines (![[...]]) from a markdown file.
This is the inverse of insert_transclusions.py.

Removes any line whose only content is a transclusion embed, e.g.
    ![[1-SOURCES/Text/BCAV08_SH_sk.md#^1-1]]
and collapses the blank-line gap left behind so paragraphs stay
single-blank-line separated.

Idempotent: running it again on an already-cleaned file removes nothing.
Leaves all other content — headings, frontmatter, verse paragraphs,
inline wikilinks like [[...]] — untouched. Only embed lines (leading !)
that stand alone on their own line are removed.

Usage:
    python remove_transclusions.py <file> [<file> ...] [--dry-run]

Examples:
    python 4-SYSTEM/Scripts/remove_transclusions.py translated_hi-plain.md
    python 4-SYSTEM/Scripts/remove_transclusions.py translated_hi-plain.md translated_hi-plain_1.md
    python 4-SYSTEM/Scripts/remove_transclusions.py translated_hi-plain.md --dry-run
"""

import argparse
import re
import sys
from pathlib import Path

# A whole-line transclusion embed: optional leading whitespace, then ![[ ... ]]
TRANSCLUSION_RE = re.compile(r"^\s*!\[\[[^\]]*\]\]\s*$")


def remove_transclusions(text):
    """Return (new_text, removed_count). Collapses doubled blank lines that
    result from deleting an embed surrounded by blank lines."""
    lines = text.splitlines(keepends=False)
    out = []
    removed = 0

    for line in lines:
        if TRANSCLUSION_RE.match(line):
            removed += 1
            # If the embed sat on its own with a blank line before it, drop one
            # of the surrounding blanks so we don't leave a double gap.
            if out and not out[-1].strip():
                out.pop()
            continue
        out.append(line)

    # Collapse any remaining runs of 2+ blank lines into a single blank line.
    cleaned = []
    for line in out:
        if not line.strip() and cleaned and not cleaned[-1].strip():
            continue
        cleaned.append(line)

    result = "\n".join(cleaned)
    if text.endswith("\n") and not result.endswith("\n"):
        result += "\n"
    return result, removed


def main():
    parser = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument("files", nargs="+", help="Markdown file(s) to clean")
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Report counts only; do not write changes",
    )
    args = parser.parse_args()

    total = 0
    for f in args.files:
        path = Path(f).resolve()
        if not path.exists():
            print("Error: file not found: " + str(path), file=sys.stderr)
            continue

        original = path.read_text(encoding="utf-8")
        new_text, removed = remove_transclusions(original)
        total += removed

        verb = "Would remove" if args.dry_run else "Removed"
        print(verb + " " + str(removed) + " transclusion(s) from " + path.name,
              file=sys.stderr)

        if not args.dry_run and removed:
            path.write_text(new_text, encoding="utf-8")

    print(("Total to remove: " if args.dry_run else "Total removed: ")
          + str(total), file=sys.stderr)


if __name__ == "__main__":
    main()
