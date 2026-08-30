#!/usr/bin/env python3
"""
Task 2 of ABC-Commentary-Formator: find long body segments that could be
split into two.

This is a REPORT-ONLY script -- it never edits the file. It's meant to
surface candidates for a human (or a follow-up manual edit) to review;
splitting a segment changes its meaning boundaries and Obsidian Block ID
numbering, so it should never be done silently/automatically.

Method:

  1. Walk the file the same way tag_body_block_ids.py does (skip YAML
     frontmatter, treat every heading line as its own block, group
     everything else into blocks separated by blank lines).
  2. Keep only prose body blocks (skip headings, frontmatter, lone
     embeds, and verse/stanza quote blocks -- splitting a quoted verse
     doesn't make sense).
  3. For every prose segment at or above --min-length characters, look
     for a "། །" (double shad) roughly in the middle third-to-most of the
     segment (between 20% and 85% of its length) -- this is the normal
     Tibetan full-stop-equivalent, so one appearing well before the very
     end usually means two independent sentences/thoughts got merged
     into one segment. If more than one such break exists, pick the one
     closest to the exact midpoint.
  4. Segments with a qualifying break are reported as strong candidates
     with a preview of both halves. Segments without one are reported
     separately as "long but no obvious break point" -- still worth a
     human look, but the split point isn't mechanically obvious.

Usage:
    python3 find_long_segments.py <target.md> [--min-length 800] [--out report.md]

If --out is given, writes a full markdown table there (useful for very
large files where the console output would be unwieldy); otherwise
prints a summary and the top 30 of each category to stdout.
"""
import re
import sys
import argparse

HEADING_RE = re.compile(r'^(#+)\s*(.*)$')
ANCHOR_TAIL_RE = re.compile(r'^(.*?)(\s\^[\w-]+)\s*$')
EMBED_RE = re.compile(r'^!\[\[')
BREAK_RE = re.compile(r'། །')


def collect_segments(path):
    with open(path, encoding='utf-8') as f:
        lines = [l.rstrip('\n') for l in f.readlines()]
    n = len(lines)

    frontmatter_end = -1
    if lines and lines[0].strip() == '---':
        for idx in range(1, n):
            if lines[idx].strip() == '---':
                frontmatter_end = idx
                break
    start_idx = frontmatter_end + 1 if frontmatter_end >= 0 else 0

    blocks = []
    i = start_idx
    while i < n:
        if lines[i].strip() == '':
            i += 1
            continue
        if HEADING_RE.match(lines[i].strip()):
            i += 1
            continue
        s = i
        while i < n and lines[i].strip() != '' and not HEADING_RE.match(lines[i].strip()):
            i += 1
        blocks.append((s, i))

    segments = []
    for (s, e) in blocks:
        first = lines[s].strip()
        if (EMBED_RE.match(first) and s == e - 1) or first.startswith('>'):
            continue
        text = ' '.join(lines[s:e])
        m = ANCHOR_TAIL_RE.match(text)
        core, anchor = (m.group(1), m.group(2).strip()) if m else (text, None)
        segments.append({'start': s + 1, 'len': len(core), 'text': core, 'anchor': anchor})
    return segments


def find_break(text):
    L = len(text)
    best = None
    for m in BREAK_RE.finditer(text):
        pos = m.end()
        if 0.2 * L < pos < 0.85 * L:
            score = abs(pos - L / 2)
            if best is None or score < best[0]:
                best = (score, pos)
    return best[1] if best else None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('target')
    ap.add_argument('--min-length', type=int, default=800)
    ap.add_argument('--out')
    args = ap.parse_args()

    segments = collect_segments(args.target)
    long_segs = [s for s in segments if s['len'] >= args.min_length]
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


if __name__ == '__main__':
    main()
