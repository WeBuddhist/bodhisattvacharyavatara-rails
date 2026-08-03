#!/usr/bin/env python3
"""
apply.py — commentary-verse-id skill

Adds Obsidian-style block IDs (^{chapter}-{n}) to commentary segments in a
segmented Tibetan commentary markdown file, based on the chapter number
found in the nearest preceding root-text transclusion.

Pattern recognized:
    ![[bo-<root-title>#^<chapter>-<verse>]]
    > <root verse line(s)>
    <commentary paragraph(s)...>

Rules:
- Transclusion lines (![[...]]) are never modified and never receive an id.
- The "chapter" number is the first number in the transclusion's block ref
  (e.g. ^1-1 -> chapter 1, ^2-1 -> chapter 2).
- Before the first transclusion in the file (no root text transcluded yet),
  segments are tagged with chapter "0" (^0-1, ^0-2, ...) instead of being
  left untagged. As soon as the first transclusion is encountered, the
  chapter switches to its real number and the counter resets to 1.
- A running per-chapter counter starts at 1 the first time a chapter number
  is seen (or changes from the previous transclusion's chapter number, or
  from the initial "0" pre-transclusion zone). It does NOT reset on every
  transclusion — multiple transclusions within the same chapter (e.g.
  #^1-2, #^1-3) continue the same running counter.
- Every non-blank, non-transclusion, non-heading line gets
  " ^{chapter}-{counter}" appended to its end, and the counter increments
  by 1 for the next such line. This includes root-quote lines (> ...) and
  commentary paragraphs alike, and applies from the very first content line
  of the file (chapter "0" if no transclusion has appeared yet).
- Blank lines, YAML frontmatter, and markdown headings (#, ##, ...) are
  left untouched and do not consume a counter value.
- Lines that already end with a block id (matching / \^\d+-\d+$/) are left
  untouched (idempotent re-runs won't double-tag).
- Original line endings (CRLF or LF) and total line count are preserved.

Usage:
    python apply.py audit <path-to-file.md>
    python apply.py apply <path-to-file.md> [output.md]

`audit` reports how many segments would be tagged and the chapter/counter
ranges it detects, without writing anything.
`apply` writes the tagged output. If output.md is omitted, the input file
is overwritten in place.
"""
import re
import sys

TRANSCLUSION_RE = re.compile(r'^!\[\[.*#\^(\d+)-(\d+)\]\]\s*$')
EXISTING_ID_RE = re.compile(r'\s\^\d+-\d+\s*$')
HEADING_RE = re.compile(r'^#{1,6}\s')


def process(lines):
    """lines: list of str (no line-ending chars).
    Returns (new_lines, stats) where stats is a list of
    (chapter, first_counter, last_counter) per contiguous chapter run.
    """
    out = []
    chapter = '0'  # pre-transclusion zone until the first transclusion sets a real chapter
    counter = 1
    in_frontmatter = False
    stats = []
    current_run = None  # [chapter, first, last]

    for i, line in enumerate(lines):
        stripped = line.strip()

        if i == 0 and stripped == '---':
            in_frontmatter = True
            out.append(line)
            continue
        if in_frontmatter:
            out.append(line)
            if stripped == '---':
                in_frontmatter = False
            continue

        m = TRANSCLUSION_RE.match(stripped)
        if m:
            new_chapter = m.group(1)
            if new_chapter != chapter:
                if current_run is not None:
                    stats.append(tuple(current_run))
                chapter = new_chapter
                counter = 1
                current_run = [chapter, None, None]
            out.append(line)
            continue

        if stripped == '' or HEADING_RE.match(stripped):
            out.append(line)
            continue

        if EXISTING_ID_RE.search(line):
            out.append(line)
            continue

        if current_run is None:
            current_run = [chapter, None, None]
        if current_run[1] is None:
            current_run[1] = counter
        current_run[2] = counter

        tagged = f"{line} ^{chapter}-{counter}"
        counter += 1
        out.append(tagged)

    if current_run is not None:
        stats.append(tuple(current_run))

    return out, stats


def read_lines(path):
    data = open(path, encoding='utf-8', newline='').read()
    eol = '\r\n' if '\r\n' in data else '\n'
    return data.split(eol), eol


def cmd_audit(path):
    lines, eol = read_lines(path)
    _, stats = process(lines)
    if not stats:
        print("No transclusions found — nothing to tag.")
        return
    print(f"{'chapter':<10}{'first_id':<12}{'last_id':<12}{'count'}")
    for chapter, first, last in stats:
        if first is None:
            continue
        count = last - first + 1
        print(f"{chapter:<10}^{chapter}-{first:<10}^{chapter}-{last:<10}{count}")


def cmd_apply(infile, outfile):
    lines, eol = read_lines(infile)
    new_lines, stats = process(lines)
    new_data = eol.join(new_lines)
    open(outfile, 'w', encoding='utf-8', newline='').write(new_data)
    print(f"Wrote {outfile}")
    cmd_audit(outfile)


def main():
    if len(sys.argv) < 3:
        print(__doc__)
        sys.exit(1)
    mode = sys.argv[1]
    infile = sys.argv[2]
    if mode == 'audit':
        cmd_audit(infile)
    elif mode == 'apply':
        outfile = sys.argv[3] if len(sys.argv) > 3 else infile
        cmd_apply(infile, outfile)
    else:
        print(__doc__)
        sys.exit(1)


if __name__ == '__main__':
    main()
