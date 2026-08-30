#!/usr/bin/env python3
"""
Task 1 of ABC-Commentary-Formator: heading-level tagging via outline alignment.

Given a segmented commentary file and its bare ས་བཅད outline file (a bullet
list whose entries carry ^TOC-N-N-N... anchors, one number-segment per
nesting depth), this script:

  1. Parses the outline into an ordered list of (depth, title) entries.
     depth = (number of dash-separated segments in the TOC id) + 1, e.g.
     ^TOC-1        -> depth 2   (a level-2 "##" heading)
     ^TOC-1-1      -> depth 3   (###)
     ^TOC-1-1-1-1  -> depth 5   (#####)

  2. Scans the target file for every "heading-candidate" line: already a
     markdown heading (# .. #############), a "* **bold**" bullet, or a
     bare "**bold**" line. These are the forms this vault's commentary
     files use for outline nodes before they're correctly hashed.

  3. Normalizes both sides' titles (strips a leading ordinal word like
     དང་པོ་/གཉིས་པ་/གསུམ་པ་..., trailing shad/punctuation, wrapping "**"),
     then aligns the two sequences with a Needleman-Wunsch global alignment
     (order-preserving, similarity-scored) so that headings match their
     outline entries even when wording differs slightly and even when some
     outline nodes have no heading of their own in the body (folded into
     prose) or some body headings don't appear in the outline at all
     (e.g. hand-added "## N. Chapter N" title lines).

  4. Rewrites every matched heading line with "#" * depth, keeping the
     original title text (including any "**bold**"), any pre-existing
     trailing Obsidian Block ID, exactly as-is. Unmatched heading-candidate
     lines are left completely untouched -- never guess.

  5. Detects and repairs one known data quirk: two headings accidentally
     glued onto a single line with a stray outline-number code stuck
     between them, e.g.:
         **A།1.2.2.1.1.1.2.1.3.1 དང་པོ། B।**
     This is split into two separate heading lines at the correct depths
     (parent depth for A, child depth for B) before alignment/rewriting.

Usage:
    python3 align_headings.py <target.md> <outline.md>

Writes a timestamped backup next to <target.md> before overwriting it in
place. Prints a summary: how many headings matched (and at what
confidence), which outline entries had no matching heading in the body
(expected for implicit/folded nodes -- not an error), and which existing
heading-candidate lines in the body didn't match anything in the outline
(also expected for hand-added chapter titles -- also not an error). Always
skim the low-confidence matches (similarity < 0.8) before trusting the
result on a new file family.
"""
import re
import sys
import shutil
import difflib
from datetime import datetime

ORDINALS = ['དང་པོ', 'གཉིས་པ', 'གསུམ་པ', 'བཞི་པ', 'ལྔ་པ',
            'དྲུག་པ', 'བདུན་པ', 'བརྒྱད་པ', 'དགུ་པ', 'བཅུ་པ']

HEADING_RE = re.compile(r'^(#+)\s*(.*)$')
OUTLINE_RE = re.compile(r'^(\t*)-\s*(.*?)\s*\^TOC-([\d-]+)\s*$')
ANCHOR_RE = re.compile(r'\s*(\^[\w-]+)\s*$')
GLUED_NUM_RE = re.compile(r'(\d+(?:\.\d+){2,})\s*(.+)$')


def normalize(title: str) -> str:
    t = title.strip().strip('*').strip()
    t = re.sub(r'[།༎༏༐༑\s]+$', '', t)
    for o in sorted(ORDINALS, key=len, reverse=True):
        if t.startswith(o):
            t = t[len(o):].lstrip('་ ')
            break
    t = re.sub(r'^\d+\.\s*', '', t)
    return t.strip()


def parse_outline(path):
    with open(path, encoding='utf-8') as f:
        lines = f.readlines()
    entries = []
    for line in lines:
        m = OUTLINE_RE.match(line.rstrip('\n'))
        if m:
            _, title, tocid = m.groups()
            depth = tocid.count('-') + 1 + 1  # +1 for TOC segments, +1 for level offset
            entries.append({'title': title, 'depth': depth, 'norm': normalize(title)})
    return entries


def repair_glued_headings(lines):
    """Split 'A।NUMCODE B।' onto two heading lines. Returns (lines, n_repairs)."""
    out = []
    n = 0
    for line in lines:
        stripped = line.rstrip('\n')
        core = stripped.strip()
        is_bullet_bold = core.startswith('*') and '**' in core
        is_hash = HEADING_RE.match(core)
        if not (is_bullet_bold or is_hash):
            out.append(line)
            continue
        m = GLUED_NUM_RE.search(core)
        if not m or m.start() == 0:
            out.append(line)
            continue
        before = core[:m.start()]
        after_num, after_text = m.group(1), m.group(2)
        if not before or before[-1].isspace():
            out.append(line)
            continue
        # before ends a heading (strip trailing ** / whitespace); after_text starts a new one
        before_clean = before.rstrip('*').rstrip()
        if before_clean.startswith('*') or '**' in stripped[:m.start()]:
            out.append(f"{before_clean}**\n")
            out.append("\n")
            out.append(f"**{after_text.strip()}\n")
        else:
            hm = HEADING_RE.match(core)
            hashes = hm.group(1) if hm else '#'
            out.append(f"{hashes} {before_clean}\n")
            out.append("\n")
            out.append(f"{hashes} {after_text.strip()}\n")
        n += 1
    return out, n


def find_candidates(lines):
    candidates = []
    for i, line in enumerate(lines):
        s = line.rstrip('\n').strip()
        if not s:
            continue
        am = ANCHOR_RE.search(s)
        anchor = am.group(1) if am else None
        core = s[:am.start()].strip() if am else s
        if core.startswith('#'):
            title = core.lstrip('#').strip()
            candidates.append({'line': i, 'title': title, 'anchor': anchor, 'norm': normalize(title)})
        elif core.startswith('* ') and '**' in core:
            title = core[2:].strip()
            candidates.append({'line': i, 'title': title, 'anchor': anchor, 'norm': normalize(title)})
        elif core.startswith('**') and core.endswith('**') and len(core) < 250:
            candidates.append({'line': i, 'title': core, 'anchor': anchor, 'norm': normalize(core)})
    return candidates


def sim(a, b):
    if not a or not b:
        return 0.0
    if a == b:
        return 1.0
    if a in b or b in a:
        return 0.9
    return difflib.SequenceMatcher(None, a, b).ratio()


def align(outline, candidates):
    n, m = len(outline), len(candidates)
    GAP = -0.3
    dp = [[0.0] * (m + 1) for _ in range(n + 1)]
    ptr = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        dp[i][0] = dp[i - 1][0] + GAP
        ptr[i][0] = 2
    for j in range(1, m + 1):
        dp[0][j] = dp[0][j - 1] + GAP
        ptr[0][j] = 3
    for i in range(1, n + 1):
        oi = outline[i - 1]['norm']
        for j in range(1, m + 1):
            cj = candidates[j - 1]['norm']
            s = sim(oi, cj)
            match_score = dp[i - 1][j - 1] + (s * 2 - 1)
            skip_o = dp[i - 1][j] + GAP
            skip_c = dp[i][j - 1] + GAP
            best = max(match_score, skip_o, skip_c)
            dp[i][j] = best
            ptr[i][j] = 1 if best == match_score else (2 if best == skip_o else 3)
    i, j = n, m
    alignment = []
    while i > 0 or j > 0:
        p = ptr[i][j]
        if i > 0 and j > 0 and p == 1:
            alignment.append((i - 1, j - 1)); i -= 1; j -= 1
        elif i > 0 and (p == 2 or j == 0):
            alignment.append((i - 1, None)); i -= 1
        else:
            alignment.append((None, j - 1)); j -= 1
    alignment.reverse()
    return alignment


def main():
    if len(sys.argv) != 3:
        print("usage: align_headings.py <target.md> <outline.md>")
        sys.exit(1)
    target_path, outline_path = sys.argv[1], sys.argv[2]

    outline = parse_outline(outline_path)
    print(f"outline entries: {len(outline)}")

    with open(target_path, encoding='utf-8') as f:
        raw_lines = f.readlines()

    repaired_lines, n_repairs = repair_glued_headings(raw_lines)
    if n_repairs:
        print(f"repaired {n_repairs} glued-together heading line(s) -- spot check these")

    candidates = find_candidates(repaired_lines)
    print(f"heading candidates in body: {len(candidates)}")

    alignment = align(outline, candidates)
    matched, low_conf, unmatched_outline, unmatched_cand = [], [], [], []
    matched_cand_idx = set()
    for oi, cj in alignment:
        if oi is not None and cj is not None:
            s = sim(outline[oi]['norm'], candidates[cj]['norm'])
            if s >= 0.55:
                matched.append((oi, cj, s))
                matched_cand_idx.add(cj)
                if s < 0.8:
                    low_conf.append((oi, cj, s))
                continue
            unmatched_outline.append(oi)
            unmatched_cand.append(cj)
        elif oi is not None:
            unmatched_outline.append(oi)
        else:
            unmatched_cand.append(cj)

    out_lines = repaired_lines[:]
    for oi, cj, s in matched:
        level = outline[oi]['depth']
        cand = candidates[cj]
        line_idx = cand['line']
        hashes = '#' * level
        suffix = f" {cand['anchor']}" if cand['anchor'] else ""
        out_lines[line_idx] = f"{hashes} {cand['title']}{suffix}\n"

    print(f"matched: {len(matched)}  (low-confidence <0.8: {len(low_conf)})")
    print(f"outline entries with no matching heading in body (expected for implicit/folded nodes): {len(unmatched_outline)}")
    print(f"body heading-candidates with no outline match (expected for hand-added chapter titles): {len(unmatched_cand)}")
    if low_conf:
        print("\nLow-confidence matches -- review these:")
        for oi, cj, s in low_conf:
            print(f"  {s:.2f}  outline='{outline[oi]['title']}'  body(line {candidates[cj]['line']+1})='{candidates[cj]['title']}'")

    ts = datetime.now().strftime('%Y%m%d-%H%M%S')
    backup = re.sub(r'\.md$', f'.BACKUP-{ts}.md', target_path)
    shutil.copyfile(target_path, backup)
    with open(target_path, 'w', encoding='utf-8') as f:
        f.writelines(out_lines)
    print(f"\nbackup written to: {backup}")
    print(f"updated file written to: {target_path}")


if __name__ == '__main__':
    main()
