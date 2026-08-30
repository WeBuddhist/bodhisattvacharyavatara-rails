#!/usr/bin/env python3
"""
Task 3a of ABC-Commentary-Formator: Obsidian Block IDs for HEADINGS only.

Run this only after align_headings.py has given every heading line its
correct "#" depth. This script never touches body text -- see
tag_body_block_ids.py for that (a separate, independently-restarting ID
sequence).

ID scheme (matches this vault's existing hand-set anchors, e.g.
^I-0, ^I-1-0, ^I-1-1-0, ^I-1-1-2-0):

  - Every heading's Obsidian Block ID is a path of sibling-position
    numbers, one segment per level below the very first level-2 heading,
    always ending in a constant "-0". The number of "-N-" segments in the
    id always equals (heading level - 1), so the id's shape alone tells
    you the heading's depth.
  - The three (or however many) level-2 ("##") headings in the file get
    special root labels rather than plain numbers: the FIRST level-2
    heading is labeled "I" (matching this vault's convention of using a
    roman numeral for the introduction/front matter); every level-2
    heading after that gets plain arabic numbers starting at 1 (2nd
    level-2 heading -> "1", 3rd -> "2", ...). This mirrors the existing
    "I / 1 / 2" labels already used for a 3-part intro/body/colophon
    commentary; if a file has a different number of top-level parts the
    same rule still applies (2nd part is always "1", 3rd is "2", etc.).
  - Every heading below that gets its 1-based sibling index among
    headings under the same nearest-shallower-level ancestor, appended
    to the ancestor's own path (with the ancestor's trailing "-0"
    dropped), then a trailing "-0" of its own.
  - Skipped levels (the ss-bcad outline sometimes has an implicit parent
    node that never got its own heading line in the body -- e.g. a level
    5 heading is directly followed by a level 7 heading with no level 6
    heading anywhere) are padded with an implicit sibling-index of 1 for
    each missing intermediate level, so the id depth still matches the
    heading's own level even across the gap. This is a deliberate,
    self-healing convention -- do not "fix" it by inventing heading text
    for the missing node.

This script is idempotent and safe to re-run: it always recomputes every
heading's id from scratch (ignoring whatever id, if any, is already
there) and overwrites it, so re-running it after further heading edits
just refreshes the numbering.

Usage:
    python3 tag_heading_block_ids.py <target.md>
"""
import re
import sys
import shutil
from datetime import datetime

HEADING_RE = re.compile(r'^(#+)\s*(.*)$')
ANCHOR_RE = re.compile(r'\s*\^[\w-]+\s*$')


def compute_id(counters: dict, level: int) -> str:
    for lv in list(counters.keys()):
        if lv > level:
            del counters[lv]
    counters[level] = counters.get(level, 0) + 1
    for lv in range(2, level):
        if lv not in counters:
            counters[lv] = 1
    parts = []
    for lv in range(2, level + 1):
        c = counters[lv]
        parts.append("I" if (lv == 2 and c == 1) else str(c - 1) if lv == 2 else str(c))
    return "-".join(parts) + "-0"


def main():
    if len(sys.argv) != 2:
        print("usage: tag_heading_block_ids.py <target.md>")
        sys.exit(1)
    path = sys.argv[1]
    with open(path, encoding='utf-8') as f:
        lines = f.readlines()

    counters = {}
    out = []
    report = []
    for line in lines:
        s = line.rstrip('\n')
        m = HEADING_RE.match(s.strip())
        if not m or not s.strip().startswith('#'):
            out.append(line)
            continue
        hashes, rest = m.groups()
        level = len(hashes)
        if level == 1:
            out.append(line)  # document title stays as-is (not part of this vault's I/1/2 scheme)
            continue
        rest_core = ANCHOR_RE.sub('', rest).rstrip()
        new_id = compute_id(counters, level)
        out.append(f"{hashes} {rest_core} ^{new_id}\n")
        report.append((level, rest_core, new_id))

    ts = datetime.now().strftime('%Y%m%d-%H%M%S')
    backup = re.sub(r'\.md$', f'.BACKUP-{ts}.md', path)
    shutil.copyfile(path, backup)
    with open(path, 'w', encoding='utf-8') as f:
        f.writelines(out)

    # sanity: depth-consistency and duplicate check
    ids = [r[2] for r in report]
    bad_depth = [r for r in report if len(r[2].split('-')) - 1 != r[0] - 1]
    dups = {x for x in ids if ids.count(x) > 1}
    print(f"headings tagged: {len(report)}")
    print(f"depth mismatches (should be 0): {len(bad_depth)}")
    for r in bad_depth[:20]:
        print("  MISMATCH", r)
    print(f"duplicate ids (should be 0): {len(dups)}")
    for d in list(dups)[:20]:
        print("  DUP", d)
    print(f"backup written to: {backup}")
    print(f"updated file written to: {path}")


if __name__ == '__main__':
    main()
