#!/usr/bin/env python3
"""
add_transclusions.py

Insert Obsidian-style root-text transclusion lines (e.g.
"![[1-SOURCES/Text/BCAV08_SH_sk.md#^1-1]]") into a translated file, by
copying them from a source file that already has them in the right
places.

This is a purely mechanical operation: for every segment ID in the
source file that is immediately preceded by a bare transclusion line,
insert that exact same transclusion line immediately before the block
carrying the matching segment ID in the translated file (segments that
never had a transclusion in the source -- e.g. the intro, or chapter
headings -- are left untouched). The mapping is derived directly from
the source file itself, not hardcoded, so it automatically follows
whatever the source actually does (verse segments only, headings and
intro excluded, any future ID patterns like colophon "a-0"/"b-1" just
work without special-casing).

Algorithm:
    1. Split both files into blocks. A block ends either at a blank
       line, or at the first line that itself carries a segment ID
       (e.g. "...^1-a") -- whichever comes first. Ending a block on an
       ID-bearing line (not just on blank lines) matters because some
       source/translated files run a chapter's closing colophon line
       straight into the next chapter's heading with no blank line
       between them; without this, both lines would be merged into one
       block and the colophon's segment ID (only checked on a block's
       *last* line) would be missed entirely.
    2. Segment IDs are detected anywhere in a line, not just at the
       very end -- some colophon lines have trailing annotation after
       the ID (e.g. "...^6-86 (something)"). Transclusion lines
       themselves (which also contain a "^id" inside the [[...]]) are
       never treated as ID-bearing for this purpose, so they don't
       cause spurious block splits.
    3. In the source, find every block that is itself a single bare
       transclusion line and is immediately followed by a block whose
       last line carries a segment ID. Record {segment_id:
       transclusion_line}.
    4. Walk the translated file's blocks. For each block, if its first
       line is already a transclusion line, strip it (avoids
       duplicating one that's already there). Then, if the block's
       segment ID is in the map, insert the mapped transclusion line as
       its own block immediately before it.
    5. Rejoin all blocks with exactly one blank line between them.

Usage:
    python add_transclusions.py <source_file> <translated_file> [-o OUTPUT] [--in-place]

    With neither -o nor --in-place, the result is printed to stdout
    (diagnostics go to stderr, so stdout stays clean / pipeable).

Options:
    -o, --output PATH   Write the result to PATH instead of stdout.
    --in-place           Overwrite <translated_file> with the result.
                          Mutually exclusive with -o.

Example:
    python add_transclusions.py \
        "1-SOURCES/Translations/bo-source.md" \
        "AI_translation/marathi/bca-marathi-scholars.md" \
        --in-place
"""

import argparse
import re
import sys
from pathlib import Path

TRANSCLUSION_PATTERN = re.compile(r"^\s*!\[\[.*\]\]\s*$")
SEGMENT_ID_PATTERN = re.compile(r"\^([\w\-]+)")


def line_segment_id(line):
    """Return the last segment ID found anywhere in the line, or None.
    Transclusion lines are excluded even though they contain a "^id"
    inside the [[...]] -- that's a reference, not a segment marker."""
    if TRANSCLUSION_PATTERN.match(line):
        return None
    matches = SEGMENT_ID_PATTERN.findall(line)
    return matches[-1] if matches else None


def split_into_blocks(text):
    """Split text into blocks. A block ends at a blank line or at the
    first line carrying a segment ID, whichever comes first -- so a
    colophon line running straight into the next heading (no blank
    line between them) still ends up as two separate blocks."""
    blocks = []
    current = []
    for line in text.split("\n"):
        if line.strip() == "":
            if current:
                blocks.append(current)
                current = []
            continue
        current.append(line)
        if line_segment_id(line) is not None:
            blocks.append(current)
            current = []
    if current:
        blocks.append(current)
    return blocks


def block_segment_id(block):
    """Return the segment ID for a block (from its last line), or None."""
    return line_segment_id(block[-1]) if block else None


def is_transclusion_block(block):
    return len(block) == 1 and TRANSCLUSION_PATTERN.match(block[0]) is not None


def build_transclusion_map(source_blocks):
    """Map segment ID -> transclusion line, for every source block that
    is itself a bare transclusion line immediately followed by a block
    carrying that ID."""
    mapping = {}
    for i, block in enumerate(source_blocks):
        if not is_transclusion_block(block):
            continue
        if i + 1 >= len(source_blocks):
            continue
        next_block = source_blocks[i + 1]
        seg_id = block_segment_id(next_block)
        if seg_id is not None:
            mapping[seg_id] = block[0]
    return mapping


def strip_leading_transclusion(block):
    """If a block's first line is itself a transclusion line, drop it."""
    if block and TRANSCLUSION_PATTERN.match(block[0]):
        return block[1:]
    return block


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("source_file")
    ap.add_argument("translated_file")
    ap.add_argument("-o", "--output", default=None)
    ap.add_argument("--in-place", action="store_true")
    args = ap.parse_args()

    if args.output and args.in_place:
        print("Error: --output and --in-place are mutually exclusive.", file=sys.stderr)
        sys.exit(1)

    source_path = Path(args.source_file)
    translated_path = Path(args.translated_file)

    source_text = source_path.read_text(encoding="utf-8")
    translated_text = translated_path.read_text(encoding="utf-8")

    source_blocks = split_into_blocks(source_text)
    translated_blocks = split_into_blocks(translated_text)

    transclusion_map = build_transclusion_map(source_blocks)

    result_blocks = []
    inserted = 0
    no_source_transclusion = []
    for block in translated_blocks:
        block = strip_leading_transclusion(block)
        seg_id = block_segment_id(block)
        if seg_id is not None and seg_id in transclusion_map:
            result_blocks.append([transclusion_map[seg_id]])
            inserted += 1
        elif seg_id is not None:
            no_source_transclusion.append(seg_id)
        result_blocks.append(block)

    translated_ids = set()
    for b in translated_blocks:
        sid = block_segment_id(b)
        if sid is not None:
            translated_ids.add(sid)
    missing_ids = [seg_id for seg_id in transclusion_map if seg_id not in translated_ids]

    output_text = "\n\n".join("\n".join(b) for b in result_blocks) + "\n"

    print(f"Inserted {inserted} transclusion line(s).", file=sys.stderr)
    if no_source_transclusion:
        print(f"{len(no_source_transclusion)} segment(s) in translated file have no source transclusion "
              f"(expected for headings/intro): {no_source_transclusion}", file=sys.stderr)
    if missing_ids:
        print(f"WARNING: {len(missing_ids)} segment ID(s) had a source transclusion but are missing "
              f"from the translated file (possible dropped/renamed segment): {missing_ids}", file=sys.stderr)

    if args.in_place:
        translated_path.write_text(output_text, encoding="utf-8")
        print(f"Wrote in place: {translated_path}", file=sys.stderr)
    elif args.output:
        Path(args.output).write_text(output_text, encoding="utf-8")
        print(f"Wrote: {args.output}", file=sys.stderr)
    else:
        print(output_text)


if __name__ == "__main__":
    main()
