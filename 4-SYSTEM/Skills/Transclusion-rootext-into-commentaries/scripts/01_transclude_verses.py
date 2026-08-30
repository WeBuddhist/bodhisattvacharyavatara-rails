#!/usr/bin/env python3
"""STAGE 1 - Insert root-verse transclusions into a Tibetan commentary.

For each root-text verse stanza, find its first FULL inline quotation in the
commentary and insert  ![[<link-base>#^N-V]]  on the line immediately before it
(short Obsidian link form). Full stanza is preferred over a partial/illustrative
quotation; a verse quoted in passing (single line + closer) is matched
only when no fuller quotation exists.

Matching tolerates minor orthographic variants via a character-overlap ratio.
Also handles commentaries that quote the full stanza on a single bold line
(**line1 line2 line3 line4**).

This stage always places the transclusion right before the verse's own quoted
text. Whether it then stays there or gets moved up to sit before the verse's
own sa-bcad (ས་བཅད) heading is decided by Stage 2
(02_remove_blank_before_transclusions.py, which now repositions rather than
just trimming blanks - see its docstring). Blank-line spacing around the
transclusion, wherever it ends up, is handled entirely by Stage 3
(03_blank_before_sachad.py, which now normalizes spacing on both sides). This
stage itself does not add or remove any blank lines.

Usage:
  python3 01_transclude_verses.py \\
      --root  1-SOURCES/Translations/<root>.md \\
      --commentary 1-SOURCES/Commentaries/Raw/<comm>.md \\
      --link-base "bo-blo-ldan-shes-rab" \\
      [--chapter N | --chapter all] [--apply]

Without --apply it prints a per-verse placement report (dry run). With --apply it
writes the transclusions into the commentary in place. Re-running is safe: verses
already transcluded are skipped.
"""
import re, sys, io, argparse, unicodedata
from difflib import SequenceMatcher
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

def norm(s):
    s = unicodedata.normalize("NFC", s)
    s = re.sub(r'!\[\[.*?\]\]', '', s)
    s = re.sub(r'\^[\w-]+', '', s)
    s = s.replace('**', '')          # strip Markdown bold markers
    for ch in ['།','༎','་',' ','༅','༄','༈']:
        s = s.replace(ch, '')
    return s.strip()

def ratio(a, b):
    if not a or not b: return 0.0
    return SequenceMatcher(None, a, b).ratio()

def line_match(v, c):
    if not v or not c: return False
    if v == c: return True
    if ratio(v, c) >= 0.80: return True
    if len(v) >= 8 and v in c: return True
    return False

CLOSERS = ['zes-pa-ni', 'ces-pa-ni']  # not used for Tibetan matching here

def is_closer(cn):
    # Tibetan closers in normalised (stripped) form
    closers = ['zespa ni', 'cespani', 'zesgsung']
    for c in closers:
        if cn.startswith(c): return True
    return False

def stanza_score(stanza, comm_norm, start):
    n = len(stanza)
    if start < 0 or start >= len(comm_norm): return 0, 0
    matched = 0; ci = start; si = 0; misses = 0
    while si < n and ci < len(comm_norm):
        if line_match(stanza[si], comm_norm[ci]):
            matched += 1; si += 1; ci += 1
        else:
            misses += 1
            if misses > 1: break
            si += 1; ci += 1
    return matched, ci - start

def build_cand_index(comm_norm):
    idx = {}
    for i, cn in enumerate(comm_norm):
        if len(cn) < 5: continue
        idx.setdefault(cn[:5], []).append(i)
        idx.setdefault(cn[1:6], []).append(i)
    return idx

def stanza_concat_match(stanza, comm_norm_line):
    """Return True if the stanza lines concatenated match a single commentary line.
    Handles commentaries that quote the full stanza on one bold line."""
    if not stanza or not comm_norm_line: return False
    cat = ''.join(stanza)
    if not cat: return False
    if cat == comm_norm_line: return True
    r = ratio(cat, comm_norm_line)
    if r >= 0.78: return True
    return False

def find_best(stanza, comm_norm, taken, cand_idx):
    cand_starts = set()
    # Candidate starts from individual stanza lines (multi-line match)
    for p, sl in enumerate(stanza):
        if len(sl) < 5: continue
        for k in (sl[:5], sl[1:6]):
            for ci in cand_idx.get(k, ()):
                st = ci - p
                if st >= 0: cand_starts.add(st)
    # Candidate starts from concatenated stanza (single-line bold match)
    cat = ''.join(stanza)
    if len(cat) >= 5:
        for k in (cat[:5], cat[1:6]):
            for ci in cand_idx.get(k, ()):
                cand_starts.add(ci)
    best = None
    for start in cand_starts:
        if start in taken: continue
        # Try single-line (bold) match first
        if stanza_concat_match(stanza, comm_norm[start]):
            matched, reach = len(stanza), 1
            key = (matched, -start)
            if best is None or key > best[0]:
                best = (key, start, reach)
            continue
        matched, reach = stanza_score(stanza, comm_norm, start)
        need = max(2, (len(stanza) + 1) // 2)
        ok = matched >= need
        if not ok and matched >= 1:
            endc = start + reach
            if endc < len(comm_norm) and is_closer(comm_norm[endc]):
                ok = reach >= 1
        if not ok: continue
        if any((start + k) in taken for k in range(reach)): continue
        key = (matched, -start)
        if best is None or key > best[0]:
            best = (key, start, reach)
    if best is None: return None, 0
    return best[1], best[2]

def parse_root_verses(path, chapter):
    lines = open(path, encoding='utf-8').read().split('\n')
    verses = {}; cur = []
    for ln in lines:
        m = re.search(r'\^(\d+)-(\d+)\s*$', ln)
        tp = re.sub(r'\^[\d-]+\s*$', '', ln).strip()
        if tp and not tp.startswith('#') and not tp.startswith('!['):
            cur.append(tp)
        if m:
            ch, v = int(m.group(1)), int(m.group(2))
            stanza = [norm(x) for x in cur if norm(x)]
            if (chapter == 'all' or ch == int(chapter)) and stanza:
                verses["%d-%d" % (ch, v)] = (ch, v, stanza)
            cur = []
        if ln.strip() == '' and not m:
            cur = []
    return dict(sorted(verses.items(), key=lambda kv: (kv[1][0], kv[1][1])))

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--root', required=True)
    ap.add_argument('--commentary', required=True)
    ap.add_argument('--link-base', required=True,
                    help='base of the transclusion link')
    ap.add_argument('--chapter', default='all')
    ap.add_argument('--apply', action='store_true')
    a = ap.parse_args()

    verses = parse_root_verses(a.root, a.chapter)
    comm_raw = open(a.commentary, encoding='utf-8').read().split('\n')
    comm_norm = [norm(x) for x in comm_raw]
    cand_idx = build_cand_index(comm_norm)

    existing = set()
    for ln in comm_raw:
        if '![[' in ln:
            for mm in re.finditer(r'\^(\d+-\d+)', ln):
                existing.add(mm.group(1))

    insertions = []; unplaced = []; taken = set()
    for vid, (ch, vn, stanza) in verses.items():
        if vid in existing:
            unplaced.append((vid, 'already-transcluded'))
            continue
        idx, span = find_best(stanza, comm_norm, taken, cand_idx)
        if idx is None:
            unplaced.append((vid, 'NO-MATCH (quoted with large variant / split / absent)'))
        else:
            insertions.append((idx, vid))
            for k in range(idx, idx + span):
                taken.add(k)

    insertions.sort()
    print("verses=%d  placed=%d  unplaced=%d" % (len(verses), len(insertions), len(unplaced)))
    for li, vid in insertions:
        print("  ^%-7s -> line %d" % (vid, li + 1))
    if unplaced:
        print("UNPLACED (resolve by hand if a genuine quotation exists):")
        for vid, why in unplaced:
            print("  ^%s: %s" % (vid, why))

    if a.apply and insertions:
        out = comm_raw[:]
        for li, vid in sorted(insertions, reverse=True):
            out[li:li] = ["![[%s#^%s]]" % (a.link_base, vid)]
        open(a.commentary, 'w', encoding='utf-8').write('\n'.join(out))
        open(a.commentary, encoding='utf-8').read()  # validate decode
        print("APPLIED %d insertions" % len(insertions))

if __name__ == '__main__':
    main()
