#!/usr/bin/env python3
"""
Renumber Obsidian Block IDs (^N-M) -- the block references stamped on every
content segment of a Bodhicaryavatara-style commentary file -- restarting
the counter at ^N-1 for each chapter.

Run this AFTER scripts/tag_headings.py has converted the file's bare
ས་བཅད outline numbering into real markdown headings (##...######) and
indented bullet lists -- this script relies on that heading structure to
know what NOT to number and where each chapter starts.

Segment definition
-------------------
A "segment" is a maximal run of non-blank lines that are NOT heading-like
(see below), bounded by blank lines. This includes:
  - ordinary prose paragraphs
  - multi-line verse/stanza blocks (`>` blockquote lines) -- a whole stanza
    gets exactly ONE Obsidian Block ID, appended to its last line, same as any
    paragraph
  - a short lead-in line glued directly to a following stanza with no
    blank line between them (e.g. "དང་པོ་ནི།" immediately followed by a
    `>` quote) -- since nothing blank separates them, they are one segment
    and get one Obsidian Block ID together, per this vault's segmentation
    convention

Headings never get numbered or counted as segments:
  - markdown headings `#` through `######`
  - the outline-bullet pseudo-headings tag_headings.py produces for depth
    6+ (`* **1.2.2.1.1.1 ...**`, possibly indented with 4 spaces per level,
    bolded -- recognized whether the number is still there or has already
    been stripped by strip_heading_numbers.py, so this script's chapter
    detection keeps working even after step 3 has run)

A block can legitimately mix a content run and a heading run with NO blank
line between them (a known quirk in this vault: an outline heading
sometimes sits directly under the sentence that introduces it). This
script splits on every heading/content boundary, not just on blank lines,
so each side is handled correctly: the content run gets numbered, the
heading run is skipped and, if it's a top-level chapter heading, resets
the counter.

Chapter detection
------------------
A top-level chapter heading looks like `## 0. ...`, `## 1. ...`, ...
(exactly what tag_headings.py produces for 1-digit-group numbering). The
captured number is used verbatim as the chapter label, so chapter 0 gets
`^0-1, ^0-2, ...`, chapter 1 gets `^1-1, ^1-2, ...`, and so on. Existing
Obsidian Block IDs already sitting on chapter/sub-heading lines (like `^I-0`,
`^1-0`) are never touched -- only content-run segments are numbered.

Any pre-existing Obsidian Block ID at the end of a segment's last line is
stripped and replaced with the freshly computed one, so this script is
safe to re-run on a file that already has (possibly stale or partial)
Obsidian Block IDs.

Usage:
    python3 update_segment_ids.py <path-to-tagged-markdown-file>

The original file is backed up alongside itself using this vault's
existing convention (e.g. BCAC19_KKP_bo_segmented.BACKUP-20260630-053157.md)
before being overwritten in place.
"""

import re
import sys
import shutil
from datetime import datetime
from pathlib import Path

HEADING_RE = re.compile(r'^#{1,6}\s')
# Depth-6+ outline bullets, either as tag_headings.py currently produces them
# (bolded, e.g. "* **1.2.2.1.1.1 text**") or already stripped of their number
# by strip_heading_numbers.py while keeping the bold (e.g. "* **text**") --
# matched by requiring the whole rest of the line to be a **...** span.
BULLET_BOLD_RE = re.compile(r'^\s*[-*]\s+\*\*.*\*\*\s*$')
# Legacy un-bolded numbered bullets, from files tagged before bolding was
# added, or hand-tagged leftovers ("* 1.2.2.1.1.1 text", no "**").
BULLET_PLAIN_RE = re.compile(r'^\s*[-*]\s+\d+(\.\d+)*\.?\s')
CHAPTER_RE = re.compile(r'^##\s+(\d+)\.')
TRAILING_ID_RE = re.compile(r'\s*\^[\w-]+\s*$')


def is_headingish(line):
    return bool(HEADING_RE.match(line)) or bool(BULLET_BOLD_RE.match(line)) or bool(BULLET_PLAIN_RE.match(line))


def find_frontmatter_end(lines):
    """Return the index of the closing '---' of YAML frontmatter, or None."""
    if not lines or lines[0].rstrip('\n') != '---':
        return None
    for i in range(1, len(lines)):
        if lines[i].rstrip('\n') == '---':
            return i
    return None


def split_into_blocks(lines, start):
    """Blank-line-delimited runs of non-blank lines, each as a list of lines."""
    blocks = []
    cur = []
    for idx in range(start, len(lines)):
        line = lines[idx]
        if line.strip() == '':
            if cur:
                blocks.append(cur)
                cur = []
        else:
            cur.append(line)
    if cur:
        blocks.append(cur)
    return blocks


def split_block_into_runs(block):
    """Split a block into consecutive (is_heading, [lines]) runs."""
    runs = []
    cur_run = []
    cur_flag = None
    for line in block:
        flag = is_headingish(line)
        if cur_flag is None or flag == cur_flag:
            cur_run.append(line)
        else:
            runs.append((cur_flag, cur_run))
            cur_run = [line]
        cur_flag = flag
    if cur_run:
        runs.append((cur_flag, cur_run))
    return runs


def renumber(text):
    lines = text.splitlines(keepends=True)
    n = len(lines)

    fm_end = find_frontmatter_end(lines)
    start = fm_end + 1 if fm_end is not None else 0

    out_lines = lines[:start]
    blocks = split_into_blocks(lines, start)

    current_chapter = None
    counter = 0
    segment_total = 0
    heading_total = 0
    per_chapter = {}
    warnings = []

    for block in blocks:
        for flag, run in split_block_into_runs(block):
            if flag:
                heading_total += 1
                for line in run:
                    m = CHAPTER_RE.match(line)
                    if m:
                        current_chapter = m.group(1)
                        counter = 0
                        per_chapter.setdefault(current_chapter, 0)
                out_lines.extend(run)
            else:
                if current_chapter is None:
                    warnings.append(
                        f"content segment before any chapter heading: {run[0].rstrip()[:60]!r}"
                    )
                    out_lines.extend(run)
                    continue
                counter += 1
                segment_total += 1
                per_chapter[current_chapter] = counter
                new_id = f"^{current_chapter}-{counter}"
                last = run[-1].rstrip('\n')
                had_nl = run[-1].endswith('\n')
                stripped = TRAILING_ID_RE.sub('', last).rstrip()
                new_last = f"{stripped} {new_id}" + ('\n' if had_nl else '')
                out_lines.extend(run[:-1] + [new_last])
        out_lines.append('\n')

    # Restore original trailing-newline behavior (blank-line-splitting adds
    # one extra blank line at the very end; drop it if the source didn't
    # end in a blank line).
    if lines and lines[-1].strip() != '' and out_lines and out_lines[-1] == '\n':
        out_lines.pop()

    return ''.join(out_lines), {
        'segment_total': segment_total,
        'heading_total': heading_total,
        'per_chapter': per_chapter,
        'warnings': warnings,
    }


def process_file(path):
    path = Path(path)
    text = path.read_text(encoding='utf-8')
    new_text, stats = renumber(text)

    timestamp = datetime.now().strftime('%Y%m%d-%H%M%S')
    backup_path = path.with_name(f"{path.stem}.BACKUP-{timestamp}{path.suffix}")
    shutil.copy2(path, backup_path)

    path.write_text(new_text, encoding='utf-8')

    stats['backup_path'] = str(backup_path)
    stats['output_path'] = str(path)
    return stats


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python3 update_segment_ids.py <path-to-tagged-markdown-file>", file=sys.stderr)
        sys.exit(1)

    result = process_file(sys.argv[1])
    print(f"Backup written to: {result['backup_path']}")
    print(f"Tagged file written to: {result['output_path']}")
    print(f"Total content segments numbered: {result['segment_total']}")
    print(f"Total heading/sub-heading runs skipped: {result['heading_total']}")
    print("\nSegments per chapter:")
    for ch in sorted(result['per_chapter'], key=lambda x: int(x)):
        print(f"  chapter {ch}: {result['per_chapter'][ch]} segments (^{ch}-1 .. ^{ch}-{result['per_chapter'][ch]})")
    if result['warnings']:
        print(f"\n{len(result['warnings'])} WARNING(S) -- content found before any chapter heading:")
        for w in result['warnings']:
            print(f"  {w}")
