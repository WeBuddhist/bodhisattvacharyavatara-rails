#!/usr/bin/env python3
"""
Task 2 of ABC-Commentary-Formator: find (and, with --apply, actually fix)
long body segments that read as two or more merged thoughts.

WHY THIS THRESHOLD AND THIS BREAK RULE (learned from this vault's own
segmentation convention, studied directly on
0-INBOX/BCAC20_NKW_bo_segmented_tagged.md): body segments in this file
family are NOT "one sentence per block" -- most segments (in a sample of
1402 prose blocks in that file, ~84%) legitimately contain more than one
"| |"-terminated sentence merged into one coherent explanatory unit, with a
median length around 420 characters. The file's own practical ceiling is
around 800 characters: blocks at or above that are rare (~10% of prose
blocks) and are exactly the ones worth a second look. So "too long" is
judged against that file's own real distribution, not against a
grammar-book notion of "a paragraph is one sentence" -- do not lower
--min-length "to be thorough"; that would fight the vault's actual
convention and over-split perfectly normal blocks.

The split point itself uses the same signal this vault's own text does at
every genuine paragraph break: a double shad (the normal Tibetan full
stop) with more text after it before the segment's end. Different
digitized editions in this vault write the double shad differently --
BCAC20_NKW spaces the two "།" apart ("། །"), while BCAC16_PK glues them
with no space ("།།") -- so the break pattern matches either spacing
("།\s*།") rather than assuming one convention vault-wide; a lone "།" is
only a clause-internal pause and is deliberately NOT treated as a break
point, or every clause would get split. Splitting at the break nearest the
exact midpoint (among those falling within the middle 65% of the segment
-- between 20% and 85% of its length, so a split is never forced right at
either edge) reproduces a plausible two-thought division without ever
inventing a break where the text itself doesn't mark one.

Two modes:

  1. REPORT (default, no --apply): never edits the file. Lists candidates
     for a human (or a follow-up --apply run) to review. This is the
     original Task 2 behaviour -- unchanged.

  2. APPLY (--apply): actually re-segments the file. For every prose body
     segment at or above --min-length, recursively finds the best interior
     "| |" break, splits there, and repeats on each half -- so one
     600-character block over-merged from three sentences can become three
     blocks in one pass, not just two. A half that is still too long but
     has no more interior "| |" to split at is left as one piece (exactly
     the "long segment without an obvious break point" case the report
     mode already surfaces) -- this script never invents a split point
     without a genuine sentence-boundary anchor, matching the report mode's
     own caution.

     --apply is meant for TWO situations:
       a. Cleaning up a handful of over-long segments in an
          already-segmented file (the original use case) -- most calls
          will change very few blocks.
       b. Segmenting a RAW or barely-segmented commentary from scratch --
          point it at a file where whole chapters sit in one giant
          paragraph and it will recursively cut every such blob down to
          this vault's normal block granularity, using the exact same
          break rule throughout. This is what makes Task 2 usable on OTHER
          commentary texts, not just as a QC pass on this one.

     A segment's existing Obsidian Block ID (if any) is DROPPED when that
     segment is split -- a single id can no longer identify a specific one
     of the resulting pieces, and every piece needs its own fresh id. Run
     Task 3b (tag_body_block_ids.py) again after any --apply run that
     reports changes, to (re)stamp ids on the new block boundaries. A
     segment that was NOT split keeps its existing id untouched.

     Headings, frontmatter, lone image-embed lines, and verse/stanza quote
     blocks (consecutive ">" lines) are never touched or counted in either
     mode -- splitting a quoted verse doesn't make sense, and this task is
     scoped to prose only.

Usage:
    python3 find_long_segments.py <target.md> [--min-length 800] [--out report.md]
    python3 find_long_segments.py <target.md> [--min-length 800] --apply
"""
import re
import sys
import shutil
import argparse
from datetime import datetime

HEADING_RE = re.compile(r'^(#+)\s*(.*)$')
ANCHOR_TAIL_RE = re.compile(r'^(.*?)(\s\^[\w-]+)\s*$')
EMBED_RE = re.compile(r'^!\[\[')
# Double shad (Tibetan full stop): different digitized editions space the two
# "།" characters apart ("། །", this vault's BCAC20_NKW reference file) or glue
# them with no space ("།།", e.g. BCAC16_PK) -- \s* covers both without also
# matching a single lone "།" (which is only a clause-internal pause, not a
# sentence boundary, and would over-split if used here).
BREAK_RE = re.compile(r'།\s*།')


def frontmatter_end_index(lines):
    n = len(lines)
    if lines and lines[0].strip() == '---':
        for idx in range(1, n):
            if lines[idx].strip() == '---':
                return idx
    return -1


def collect_blocks(lines, start_idx):
    """Same grouping tag_body_block_ids.py uses: a heading line is always
    its own block; everything else groups into maximal blank-line-bounded
    runs."""
    n = len(lines)
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
    return blocks


def is_prose_block(lines, s, e):
    first = lines[s].strip()
    if HEADING_RE.match(first):
        return False
    if EMBED_RE.match(first) and s == e - 1:
        return False
    if first.startswith('>'):
        return False
    return True


def collect_segments(path):
    with open(path, encoding='utf-8') as f:
        lines = [l.rstrip('\n') for l in f.readlines()]
    fe = frontmatter_end_index(lines)
    start_idx = fe + 1 if fe >= 0 else 0
    blocks = collect_blocks(lines, start_idx)

    segments = []
    for (s, e) in blocks:
        if not is_prose_block(lines, s, e):
            continue
        text = ' '.join(lines[s:e])
        m = ANCHOR_TAIL_RE.match(text)
        core, anchor = (m.group(1), m.group(2).strip()) if m else (text, None)
        segments.append({'start': s + 1, 'end': e, 'block': (s, e), 'len': len(core),
                          'text': core, 'anchor': anchor})
    return lines, segments


def find_break(text):
    """Best single interior break: the '| |' closest to the midpoint,
    among those strictly between 20% and 85% of the text's length."""
    L = len(text)
    best = None
    for m in BREAK_RE.finditer(text):
        pos = m.end()
        if 0.2 * L < pos < 0.85 * L:
            score = abs(pos - L / 2)
            if best is None or score < best[0]:
                best = (score, pos)
    return best[1] if best else None


def recursive_split(text, min_length):
    """Split text into pieces, each either under min_length or left whole
    because no further interior '| |' break is available. Never invents a
    break; only ever cuts at an actual '| |' in the text."""
    if len(text) < min_length:
        return [text]
    pos = find_break(text)
    if pos is None:
        return [text]
    left = text[:pos].rstrip()
    right = text[pos:].lstrip()
    if not left or not right:
        return [text]
    return recursive_split(left, min_length) + recursive_split(right, min_length)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('target')
    ap.add_argument('--min-length', type=int, default=800)
    ap.add_argument('--out')
    ap.add_argument('--apply', action='store_true',
                     help='Actually split qualifying segments in place (writes a timestamped '
                          'backup first). Without this flag the script only reports candidates.')
    args = ap.parse_args()

    lines, segments = collect_segments(args.target)
    long_segs = [s for s in segments if s['len'] >= args.min_length]

    if not args.apply:
        for s in long_segs:
            s['break_pos'] = find_break(s['text'])
        with_break = sorted([s for s in long_segs if s['break_pos']], key=lambda s: -s['len'])
        without_break = sorted([s for s in long_segs if not s['break_pos']], key=lambda s: -s['len'])

        print(f"total prose segments: {len(segments)}")
        print(f"segments >= {args.min_length} chars: {len(long_segs)}")
        print(f"  with a clean internal break point: {len(with_break)}")
        print(f"  without an obvious break point: {len(without_break)}")

        lines_out = ["# Long segments that could be split\n",
                     f"Scanned for prose body segments {args.min_length}+ characters "
                     f"(headings and verse quotes excluded). Found **{len(long_segs)}**; "
                     f"of those, **{len(with_break)}** have a clean sentence-boundary "
                     "(`། །`) near the middle.\n",
                     "\n## Segments with a clean split point\n",
                     "| Line | Length | Current ID | Before split | After split |",
                     "|---|---|---|---|---|"]
        for s in with_break:
            pos = s['break_pos']
            before = s['text'][max(0, pos - 60):pos].strip()
            after = s['text'][pos:pos + 60].strip()
            lines_out.append(f"| {s['start']} | {s['len']} | `{s['anchor']}` | …{before} | {after}… |")
        lines_out.append("\n## Long segments without an obvious break point\n")
        lines_out.append("| Line | Length | Current ID | Preview |")
        lines_out.append("|---|---|---|---|")
        for s in without_break:
            lines_out.append(f"| {s['start']} | {s['len']} | `{s['anchor']}` | {s['text'][:80]}… |")

        if args.out:
            with open(args.out, 'w', encoding='utf-8') as f:
                f.write('\n'.join(lines_out))
            print(f"full report written to: {args.out}")
        else:
            print("\nTop candidates with a clean break:")
            for s in with_break[:30]:
                print(f"  line {s['start']} (len {s['len']}, {s['anchor']}) -> split at char {s['break_pos']}")
            print("\nTop long segments without an obvious break:")
            for s in without_break[:30]:
                print(f"  line {s['start']} (len {s['len']}, {s['anchor']})")
        return

    # --apply mode: actually split, working bottom-to-top so earlier line
    # indices stay valid as later ones are replaced.
    out_lines = lines[:]
    split_report = []   # (orig_start_line, orig_len, num_pieces, dropped_anchor)
    unsplit_still_long = []
    for s in sorted(long_segs, key=lambda s: -s['start']):
        pieces = recursive_split(s['text'], args.min_length)
        block_s, block_e = s['block']
        if len(pieces) <= 1:
            unsplit_still_long.append(s)
            continue
        new_block_lines = []
        for k, piece in enumerate(pieces):
            new_block_lines.append(piece)
            if k != len(pieces) - 1:
                new_block_lines.append('')  # blank line between new sibling blocks
        out_lines[block_s:block_e] = new_block_lines
        split_report.append((s['start'], s['len'], len(pieces), s['anchor']))

    if not split_report:
        print(f"total prose segments: {len(segments)}")
        print(f"segments >= {args.min_length} chars: {len(long_segs)}")
        print("none had an interior break point to split at -- nothing changed.")
        if unsplit_still_long:
            print(f"{len(unsplit_still_long)} segment(s) remain long with no obvious break point "
                  "(same as the report mode's second table) -- these need a human read, not a "
                  "mechanical split:")
            for s in sorted(unsplit_still_long, key=lambda s: -s['len'])[:30]:
                print(f"  line {s['start']} (len {s['len']}, {s['anchor']})")
        return

    ts = datetime.now().strftime('%Y%m%d-%H%M%S')
    backup = re.sub(r'\.md$', f'.BACKUP-{ts}.md', args.target)
    shutil.copyfile(args.target, backup)
    with open(args.target, 'w', encoding='utf-8') as f:
        f.write('\n'.join(out_lines) + '\n')

    dropped_anchors = [r for r in split_report if r[3]]
    print(f"total prose segments (before): {len(segments)}")
    print(f"segments split: {len(split_report)}")
    print(f"new segments created: {sum(r[2] for r in split_report) }")
    print(f"segments with an existing Obsidian Block ID that was DROPPED by the split "
          f"(re-run Task 3b to re-stamp): {len(dropped_anchors)}")
    for start, length, n_pieces, anchor in sorted(split_report, key=lambda r: r[0]):
        print(f"  line {start} (was {length} chars, id {anchor}) -> {n_pieces} pieces")
    if unsplit_still_long:
        print(f"\n{len(unsplit_still_long)} segment(s) remain >= {args.min_length} chars with no "
              "interior break point -- left untouched, needs a human read:")
        for s in sorted(unsplit_still_long, key=lambda s: -s['len'])[:30]:
            print(f"  line {s['start']} (len {s['len']}, {s['anchor']})")
    print(f"backup written to: {backup}")
    print(f"updated file written to: {args.target}")
    print("Next: re-run tag_body_block_ids.py (Task 3b) to re-stamp ids on the new block boundaries.")


if __name__ == '__main__':
    main()
