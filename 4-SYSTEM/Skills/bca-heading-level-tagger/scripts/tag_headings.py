#!/usr/bin/env python3
"""
Tag numbered outline headings (ས་བཅད) in a Bodhicaryavatara-style commentary
file with Obsidian-native markdown heading levels, so the outline can be
folded/unfolded natively.

Numbering depth -> heading level:
    1 digit   (0, 1)                  -> ##
    2 digits  (1.1)                   -> ###
    3 digits  (1.1.1)                 -> ####
    4 digits  (1.1.1.1)               -> #####
    5 digits  (1.1.1.1.1)             -> ######
    6+ digits (1.1.1.1.1.1, ...)      -> bullet list, indented 4 spaces per
                                          level beyond 6 digits (Obsidian
                                          folds bullet lists at any depth)

A line only counts as a heading to tag if it is a BARE numbered line: it
starts (after optional leading whitespace) with digits separated by dots,
then whitespace, then the heading text, and nothing else before it. This
means:

  - Chapter markers already hand-tagged like "## 1. ལེའུ་དང་པོ།" are left
    alone, because the line starts with "#" not a digit.
  - Six-plus-digit lines someone already prefixed with "-" or "*" are left
    alone, because the line starts with that bullet character, not a digit.
    (Worth checking for these after a run -- inconsistent leftover "-" vs
    "*" bullets from partial manual tagging are a known quirk of this
    vault's files and may need a manual pass to normalize.)
  - YAML frontmatter (the block between the first two "---" lines) is
    always skipped untouched, even if some value happens to start with a
    digit.

Before tagging, the script also repairs a data quirk seen in this vault's
files: a heading number sometimes gets glued directly onto the end of the
PRECEDING heading's prose with no line break in between, e.g.:

    ...བསྟན་པ།1.2.2.1.1.1.2.1.3.1 དང་པོ། ...

That heading number is invisible to the bare-line rule above since it
doesn't start its own line. The script detects this pattern -- three or
more dot-separated digit groups, immediately preceded by a non-whitespace
character (no space) and followed by whitespace -- and splits it onto its
own line before tagging proceeds, so it gets picked up like any other
heading. The 3-group-minimum and no-space-before requirement are there to
keep this narrow: an incidental number mentioned in running prose won't
match unless it's actually glued onto adjacent text with no space, which
is what makes it a broken heading rather than ordinary content. Any line
the script splits this way is reported in the summary so it's easy to spot
check afterward.

Usage:
    python3 tag_headings.py <path-to-markdown-file>

The original file is backed up alongside itself using this vault's existing
convention (e.g. BCAC19_KKP_bo_segmented.BACKUP-20260630-053157.md) before
being overwritten in place.
"""

import re
import sys
import shutil
from datetime import datetime
from pathlib import Path

# Matches a bare numbered heading line: digits, optionally dot-separated,
# then required whitespace, then the rest of the line as heading text.
HEADING_RE = re.compile(r'^(\d+(?:\.\d+)*)\s+(.+)$')

# Matches any maximal dot-separated number token in a line. Used to find
# heading numbers (3+ digit groups) glued onto the end of prior text with
# no separating whitespace/newline -- the "concatenated heading" data
# quirk. Matching the *maximal* token first (rather than searching for the
# glued-on suffix directly) avoids accidentally matching a substring of a
# legitimate leading number, e.g. mistaking "2.1.4" inside "1.2.1.4" at the
# very start of a line for a glued-on heading.
NUMBER_TOKEN_RE = re.compile(r'\d+(?:\.\d+)*')


def count_digit_groups(numbering):
    """1 -> 1, 1.1 -> 2, 1.1.1.2.2.4 -> 6, etc."""
    return numbering.count('.') + 1


def split_embedded_headings(line):
    """
    If a heading number is glued onto the end of the preceding text with no
    line break, split it onto its own line. Returns (list_of_lines, split_count).
    Most lines have no match and come back as a 1-element list unchanged.
    """
    text = line.rstrip('\n')

    split_points = []
    for m in NUMBER_TOKEN_RE.finditer(text):
        start, end = m.start(), m.end()
        if start == 0:
            continue  # this is the line's own leading number, not glued-on
        if count_digit_groups(m.group()) < 3:
            continue  # too short to distinguish from an incidental number
        if text[start - 1].isspace():
            continue  # a space precedes it -- not glued on, leave it alone
        if end < len(text) and not text[end].isspace():
            continue  # not immediately followed by whitespace/EOL -- not a clean heading token
        split_points.append(start)

    if not split_points:
        return [line], 0
    segments = []
    prev = 0
    for sp in split_points:
        segments.append(text[prev:sp])
        prev = sp
    segments.append(text[prev:])

    pieces = [seg.rstrip() for seg in segments if seg.strip()]

    result = []
    for i, piece in enumerate(pieces):
        if i > 0:
            result.append('\n')  # blank line between the split-apart pieces
        result.append(piece + '\n')
    return result, len(split_points)


def tag_line(line):
    """Return the tagged version of a line, or the line unchanged."""
    stripped = line.rstrip('\n')
    match = HEADING_RE.match(stripped)
    if not match:
        return line

    numbering, content = match.group(1), match.group(2)
    depth = count_digit_groups(numbering)

    if depth <= 5:
        marker = '#' * (depth + 1)  # 1 digit -> ##, 5 digits -> ######
        return f"{marker} {numbering} {content}\n"

    indent_level = depth - 6  # 6 digits -> no indent, 7 -> one level, etc.
    indent = '    ' * indent_level
    return f"{indent}* {numbering} {content}\n"


def process_file(path):
    path = Path(path)
    lines = path.read_text(encoding='utf-8').splitlines(keepends=True)

    # Pass 1: repair concatenated headings and tag headings, skipping
    # YAML frontmatter throughout.
    out = []
    in_frontmatter = False
    frontmatter_delims_seen = 0
    split_report = []

    for i, line in enumerate(lines):
        if line.rstrip('\n') == '---' and (i == 0 or frontmatter_delims_seen == 1):
            frontmatter_delims_seen += 1
            in_frontmatter = frontmatter_delims_seen == 1
            out.append(line)
            continue
        if in_frontmatter:
            out.append(line)
            continue

        expanded, split_count = split_embedded_headings(line)
        if split_count:
            split_report.append((i + 1, line.rstrip('\n')[:80]))
        for piece in expanded:
            out.append(tag_line(piece))

    # Back up the original using this vault's existing naming convention
    # before overwriting it in place.
    timestamp = datetime.now().strftime('%Y%m%d-%H%M%S')
    backup_path = path.with_name(f"{path.stem}.BACKUP-{timestamp}{path.suffix}")
    shutil.copy2(path, backup_path)

    path.write_text(''.join(out), encoding='utf-8')

    return {
        'lines_processed': len(lines),
        'backup_path': str(backup_path),
        'output_path': str(path),
        'split_report': split_report,
    }


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python3 tag_headings.py <path-to-markdown-file>", file=sys.stderr)
        sys.exit(1)

    result = process_file(sys.argv[1])
    print(f"Processed {result['lines_processed']} lines")
    print(f"Backup written to: {result['backup_path']}")
    print(f"Tagged file written to: {result['output_path']}")
    if result['split_report']:
        print(f"\nRepaired {len(result['split_report'])} concatenated-heading line(s) -- worth a quick spot check:")
        for line_no, preview in result['split_report']:
            print(f"  original line {line_no}: {preview}...")
    else:
        print("\nNo concatenated-heading lines found.")
