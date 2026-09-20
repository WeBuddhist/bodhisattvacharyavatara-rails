#!/usr/bin/env python3
"""Strip the ordinal prefix from TOC headings, keeping the block ID intact.

    ## 1. ལེའུ་དང་པོ། བྱང་ཆུབ་སེམས་ཀྱི་ཕན་ཡོན་བཤད་པ། ^1-0
    ## ལེའུ་དང་པོ། བྱང་ཆུབ་སེམས་ཀྱི་ཕན་ཡོན་བཤད་པ། ^1-0

The numbering was display scaffolding. It is redundant once the table of
contents carries the structure itself, and it leaks into the TOC section
titles the backend stores. The heading, its wording and its block ID all stay
— only the leading `<digits>.` goes.

WHAT COUNTS AS A TOC HEADING. A markdown heading that carries a heading block
ID, per CLAUDE.md 5a. That block ID is the whole point of the restriction:
numbered headings are everywhere in this vault — day packages number their
session steps, the docs number their rules, rails notes number their points —
and none of those are TOC nodes. Requiring the block ID targets exactly the
headings a TOC is built from and nothing else.

DIGITS ARE MATCHED IN ANY SCRIPT. `\\d` covers every Unicode decimal digit, so
Devanagari `१०.` and Tibetan `༡༠.` strip the same as ASCII `10.`. The `.` is
required: a bare leading number without it is treated as part of the title.

Default scope is the text sources and translation tracks. 4-SYSTEM (rules and
docs, where these strings are examples), 0-INBOX (scratch), 2-RAILS,
Adaptations and the protected Day-Packages are all left alone.

Usage:
    strip_heading_numbers.py --dry-run
    strip_heading_numbers.py --dry-run --path 1-SOURCES/Translations
    strip_heading_numbers.py --apply
"""

from __future__ import annotations

import argparse
import os
import re
import sys

VAULT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

DEFAULT_PATHS = [
    "1-SOURCES/Text",
    "1-SOURCES/Translations",
    "1-SOURCES/Commentaries",
    "3-TRANSFORMATIONS/Translations",
]

SKIP_DIRS = {".git", "__pycache__", "node_modules", "output", ".obsidian"}

# heading hashes | ordinal | rest-of-line (which still holds the block ID)
NUMBERED = re.compile(r'^(#{1,6}[ \t]*)(\d+)\.[ \t]*(\S.*)$', re.UNICODE)
# a trailing Obsidian block ID, e.g. ^1-0 / ^I-0 / ^a-0 / ^0
BLOCK_ID = re.compile(r'(\^[A-Za-z0-9]+(?:-[A-Za-z0-9]+)?)[ \t]*$')


def rewrite_line(line):
    """Return (new_line, ordinal) or (None, None) if the line is not a target."""
    m = NUMBERED.match(line)
    if not m:
        return None, None
    ref = BLOCK_ID.search(line)
    if not ref:
        return None, None            # numbered heading, but not a TOC node
    hashes, ordinal, rest = m.groups()
    new = f"{hashes}{rest}"
    # The block ID must survive untouched, and nothing but the ordinal may go.
    assert BLOCK_ID.search(new) and BLOCK_ID.search(new).group(1) == ref.group(1)
    assert new.replace(" ", "") == line.replace(" ", "").replace(f"{ordinal}.", "", 1)
    return new, ordinal


def walk(paths):
    for rel in paths:
        base = os.path.join(VAULT, rel)
        if os.path.isfile(base):
            yield base
            continue
        for root, dirs, files in os.walk(base):
            dirs[:] = [d for d in dirs if d not in SKIP_DIRS]
            for fn in sorted(files):
                if fn.endswith(".md"):
                    yield os.path.join(root, fn)


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--path", action="append", default=[],
                    help="restrict to this vault-relative path (repeatable)")
    ap.add_argument("--apply", action="store_true")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--quiet", action="store_true", help="counts only, no per-line diff")
    args = ap.parse_args(argv)

    if args.apply and args.dry_run:
        print("--apply and --dry-run are mutually exclusive"); return 2
    if not args.apply:
        print("DRY RUN — nothing is written. Pass --apply to write.\n")

    files_changed = lines_changed = 0
    for path in walk(args.path or DEFAULT_PATHS):
        try:
            original = open(path, encoding="utf-8").read()
        except (UnicodeDecodeError, OSError):
            continue
        lines = original.split("\n")
        out, hits = [], []
        for line in lines:
            new, ordinal = rewrite_line(line)
            if new is None:
                out.append(line)
            else:
                out.append(new)
                hits.append((line, new))
        if not hits:
            continue
        files_changed += 1
        lines_changed += len(hits)
        rel = os.path.relpath(path, VAULT)
        print(f"{rel}  ({len(hits)} heading{'s' if len(hits) != 1 else ''})")
        if not args.quiet:
            for old, new in hits:
                print(f"    - {old.strip()}")
                print(f"    + {new.strip()}")
        if args.apply:
            with open(path, "w", encoding="utf-8") as fh:
                fh.write("\n".join(out))

    verb = "rewrote" if args.apply else "would rewrite"
    print(f"\n{verb} {lines_changed} headings in {files_changed} files")
    return 0


if __name__ == "__main__":
    sys.exit(main())
