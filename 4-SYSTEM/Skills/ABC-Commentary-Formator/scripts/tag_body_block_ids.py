#!/usr/bin/env python3
"""
Task 3b of ABC-Commentary-Formator: Obsidian Block IDs for BODY TEXT only.

Run this after tag_heading_block_ids.py. This script never touches
headings (their ids are a separate, tree-shaped sequence -- see
tag_heading_block_ids.py) or the YAML frontmatter block at the top of the
file. It only stamps/renumbers the "^label-N" anchor on prose paragraphs
and verse-quote blocks.

ID scheme:

  - Every body-text "segment" gets an id "<label>-<n>".
  - <label> is inherited from the nearest PRECEDING level-2 ("##")
    heading's own Obsidian Block ID, with its trailing "-0" dropped
    (e.g. a "##" heading tagged "^I-0" makes every body segment until the
    next "##" heading use label "I"; the next "##" heading, tagged
    "^1-0", switches the label to "1"; and so on).
  - <n> restarts at 1 immediately after each level-2 heading and counts
    up through everything -- across ALL chapters/sub-sections under that
    one level-2 heading -- until the next level-2 heading. This is
    deliberately NOT restarted at every chapter or every sub-heading;
    only level-2 headings reset the counter. (If your file's convention
    is chapter-level restarts instead, that is a different scheme --
    check with the user before assuming this script's convention applies.)
  - Content that appears BEFORE the very first level-2 heading (a title
    page / translator's preamble) uses label "0".

What counts as one "segment" (one id):

  - A "block" is a maximal run of non-blank lines, EXCEPT that a heading
    line always starts a new block by itself (even glued directly onto
    the previous block with no blank line between them -- this matters
    for the YAML-frontmatter-then-title-heading case and for any
    heading that immediately follows body text).
  - The YAML frontmatter block at the very top of the file (between the
    first two lines that are exactly "---") is skipped entirely -- never
    touched, never counted.
  - A pure image-embed line ("![[...]]") on its own is skipped entirely
    -- it references another file's block, not this file's content.
  - Anything else that isn't a heading and isn't a lone embed line is a
    body segment, INCLUDING a multi-line verse/stanza quote block
    (consecutive ">" lines) -- one id for the whole stanza, on its last
    line -- and INCLUDING a segment that currently has NO Obsidian Block
    ID at all (a paragraph a human split off from a bigger block by
    hand, for instance). Never skip a body block just because it lacks
    an existing anchor to renumber -- that was a real bug once and
    silently left a segment untagged. Every non-heading, non-frontmatter,
    non-lone-embed block must end up with exactly one id.

This script is idempotent: re-running it on an already-tagged file
recomputes every id from scratch (ignoring what, if anything, was there
before) in the same left-to-right order, so the result is unchanged
unless the file's content or heading structure changed since the last run.

Usage:
    python3 tag_body_block_ids.py <target.md>
"""
import re
import sys
import shutil
from collections import defaultdict
from datetime import datetime

HEADING_RE = re.compile(r'^(#+)\s*(.*)$')
ANCHOR_TAIL_RE = re.compile(r'^(.*?)(\s\^[\w-]+)\s*$')
EMBED_RE = re.compile(r'^!\[\[')


def main():
    if len(sys.argv) != 2:
        print("usage: tag_body_block_ids.py <target.md>")
        sys.exit(1)
    path = sys.argv[1]
    with open(path, encoding='utf-8') as f:
        lines = [l.rstrip('\n') for l in f.readlines()]
    n = len(lines)

    # 1. Skip YAML frontmatter
    frontmatter_end = -1
    if lines and lines[0].strip() == '---':
        for idx in range(1, n):
            if lines[idx].strip() == '---':
                frontmatter_end = idx
                break
    start_idx = frontmatter_end + 1 if frontmatter_end >= 0 else 0

    # 2. Group into blocks; a heading line is always its own block
    blocks = []
    i = start_idx
    while i < n:
        if lines[i].strip() == '':
            i += 1
            continue
        if HEADING_RE.match(lines[i].strip()):
            blocks.append((i, i + 1))
            i += 1
            continue
        s = i
        while i < n and lines[i].strip() != '' and not HEADING_RE.match(lines[i].strip()):
            i += 1
        blocks.append((s, i))

    current_label = "0"
    counter = 0
    out_lines = lines[:]
    newly_assigned = []
    label_counts = defaultdict(int)

    for (s, e) in blocks:
        first = lines[s].strip()
        hm = HEADING_RE.match(first)
        if hm:
            hashes, rest = hm.groups()
            if len(hashes) == 2:
                am = re.search(r'\^([\w-]+)\s*$', rest)
                if am:
                    anchor = am.group(1)
                    current_label = anchor[:-2] if anchor.endswith('-0') else anchor
                    counter = 0
            continue
        if EMBED_RE.match(first) and s == e - 1:
            continue
        last_idx = e - 1
        last_line = lines[last_idx]
        m = ANCHOR_TAIL_RE.match(last_line)
        if m:
            core = m.group(1)
        else:
            core = last_line
            newly_assigned.append(last_idx + 1)
        counter += 1
        label_counts[current_label] = counter
        out_lines[last_idx] = f"{core} ^{current_label}-{counter}"

    ts = datetime.now().strftime('%Y%m%d-%H%M%S')
    backup = re.sub(r'\.md$', f'.BACKUP-{ts}.md', path)
    shutil.copyfile(path, backup)
    with open(path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(out_lines) + '\n')

    total = sum(label_counts.values())
    print(f"body segments tagged: {total}")
    for label, count in label_counts.items():
        print(f"  label {label}: 1..{count}")
    print(f"segments that previously had NO Obsidian Block ID (now assigned one): {len(newly_assigned)}")
    for ln in newly_assigned:
        print(f"  line {ln}: {lines[ln-1][:70]}")
    print(f"backup written to: {backup}")
    print(f"updated file written to: {path}")


if __name__ == '__main__':
    main()
