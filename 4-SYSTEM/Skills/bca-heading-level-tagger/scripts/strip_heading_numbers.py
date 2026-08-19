#!/usr/bin/env python3
"""
Strip the ས་བཅད outline numbering (`1.1`, `1.1.1.2.2.4`, ...) back off of
sub-headings, once it's no longer needed as a machine-readable anchor.

Run this LAST, after both scripts/tag_headings.py (step 1) and
scripts/update_block_ids.py (step 2) have already run on the file. By the
time this runs, the outline numbering has already done its job -- step 1
used it to pick heading depth, step 2 used the *chapter*-level number
(`## N. ...`) to know which chapter each block id belongs to -- so the
numbers on sub-headings are now redundant clutter: Obsidian's heading
levels and bullet indentation already carry the same structure, foldably.

What gets stripped
-------------------
Only sub-heading levels below the chapter: `###` through `######`, and the
depth-6+ outline bullets tag_headings.py produces (`* 1.2.2.1.1.1 ...`,
optionally indented, optionally hand-tagged with `-` instead of `*`). For
each of these, the leading number token (and the single space after it)
is removed, leaving the heading marker and the Tibetan heading text.

What is deliberately left alone
--------------------------------
- Top-level `## N. ...` chapter headings keep their number. It reads as a
  human chapter label ("Chapter 1"), and scripts/update_block_ids.py
  needs it to auto-detect chapter boundaries -- if this script also
  stripped it, a future re-run of the block-id step on this file would no
  longer be able to find chapter starts. If you ever DO need to strip
  chapter numbers too, do it by hand and expect step 2 to no longer be
  re-runnable without restoring from a backup first.
- Any Obsidian block reference (`^1-0`, `^I-0`, `^6-42`, ...) on a heading
  line -- these aren't touched by this script, only the leading outline
  number is.
- Ordinary content lines. This script only ever touches lines that are
  already heading-shaped (### through ######, or a numbered outline
  bullet) -- it does not scan prose for numbers.

Usage:
    python3 strip_heading_numbers.py <path-to-tagged-and-numbered-file>

The original file is backed up alongside itself using this vault's
existing convention (e.g. BCAC19_KKP_bo_segmented.BACKUP-20260630-053157.md)
before being overwritten in place.
"""

import re
import sys
import shutil
from datetime import datetime
from pathlib import Path

# ### through ###### only -- level-2 (##) chapter headings are excluded on
# purpose (see module docstring).
SUBHEADING_RE = re.compile(r'^(#{3,6}\s+)\d+(?:\.\d+)*\.?\s+(.+)$')

# Depth-6+ outline bullets tag_headings.py produces, optionally indented,
# with either bullet character (hand-tagged leftovers sometimes use '-').
BULLET_RE = re.compile(r'^(\s*[-*]\s+)\d+(?:\.\d+)*\.?\s+(.+)$')


def strip_line(line):
    """Return (new_line, stripped_bool)."""
    stripped_line = line.rstrip('\n')
    had_nl = line.endswith('\n')

    m = SUBHEADING_RE.match(stripped_line)
    if m:
        new = f"{m.group(1)}{m.group(2)}"
        return (new + '\n' if had_nl else new), True

    m = BULLET_RE.match(stripped_line)
    if m:
        new = f"{m.group(1)}{m.group(2)}"
        return (new + '\n' if had_nl else new), True

    return line, False


def process_file(path):
    path = Path(path)
    lines = path.read_text(encoding='utf-8').splitlines(keepends=True)

    out = []
    by_level = {}
    for line in lines:
        new_line, did_strip = strip_line(line)
        out.append(new_line)
        if did_strip:
            marker = line.lstrip()[0:6]
            hashes = len(line) - len(line.lstrip('#'))
            key = f"{'#' * hashes}" if hashes >= 3 else 'bullet'
            by_level[key] = by_level.get(key, 0) + 1

    timestamp = datetime.now().strftime('%Y%m%d-%H%M%S')
    backup_path = path.with_name(f"{path.stem}.BACKUP-{timestamp}{path.suffix}")
    shutil.copy2(path, backup_path)

    path.write_text(''.join(out), encoding='utf-8')

    return {
        'lines_processed': len(lines),
        'backup_path': str(backup_path),
        'output_path': str(path),
        'by_level': by_level,
        'total_stripped': sum(by_level.values()),
    }


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python3 strip_heading_numbers.py <path-to-tagged-and-numbered-file>", file=sys.stderr)
        sys.exit(1)

    result = process_file(sys.argv[1])
    print(f"Processed {result['lines_processed']} lines")
    print(f"Backup written to: {result['backup_path']}")
    print(f"Tagged file written to: {result['output_path']}")
    print(f"\nTotal headings/bullets with numbers stripped: {result['total_stripped']}")
    for key in sorted(result['by_level'], key=lambda k: (k != 'bullet', k)):
        print(f"  {key}: {result['by_level'][key]}")
