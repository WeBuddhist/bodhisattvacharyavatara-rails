#!/usr/bin/env python3
"""STAGE 1 - Insert root-verse transclusions into a Tibetan commentary.

For each root-text verse stanza, find its first FULL inline quotation in the
commentary and insert  ![[<link-base>#^N-V]]  on the line immediately before it
(short Obsidian link form). Full stanza is preferred over a partial/illustrative
quotation; a verse quoted in passing (single line + ཞེས་པ་ནི། closer) is matched
only when no fuller quotation exists.

Matching tolerates minor orthographic variants (e.g. བསྒོམ/སྒོམ, དེང/དེ, ཟློག/བཟློག)
via a character-overlap ratio and anchors on ANY stanza line, so a variant first
line does not block the match.

Usage:
  python3 01_transclude_verses.py \
      --root  1-SOURCES/Translations/<root>.md \
      --commentary 1-SOURCES/Commentaries/Raw/<comm>.md \
      --link-base "bo-བློ་ལྡན་ཤེས་རབ།" \
      [--chapter N | --chapter all] [--apply]

Without --apply it prints a per-verse placement report (dry run). With --apply it
writes the transclusions into the commentary in place. Re-running is safe: verses
already transcluded are skipped.
"""
import re, sys, argparse, unicodedata
from difflib import SequenceMatcher

def norm(s):
    s = unicodedata.normalize("NFC", s)
    s = re.sub(r'!\[\[.*?\]\]', '', s)
    s = re.sub(r'\^[\w-]+', '', s)
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

CLOSERS = ['ཞེསཔནི','ཅེསཔནི','ཞེསཔ','ཅེསཔ','ཞེསགསུངས','ཞེསབྱབ']
def is_closer(cn): return any(cn.startswith(c) for c in CLOSERS)

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

def find_best(stanza, comm_norm, taken, cand_idx):
    cand_starts = set()
    for p, sl in enumerate(stanza):
        if len(sl) < 5: continue
        for k in (sl[:5], sl[1:6]):
            for ci in cand_idx.get(k, ()):
                st = ci - p
                if st >= 0: cand_starts.add(st)
    best = None
    for start in cand_starts:
        if start in taken: continue
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
                    help='base of the transclusion link, e.g. bo-བློ་ལྡན་ཤེས་རབ།')
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
            unplaced.append((vid, 'already-transcluded')); continue
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
        print("  ^%-7s -> line %d: %s" % (vid, li + 1, comm_raw[li][:34]))
    if unplaced:
        print("UNPLACED (resolve by hand if a genuine quotation exists):")
        for vid, why in unplaced:
            print("  ^%s: %s" % (vid, why))

    if a.apply and insertions:
        out = comm_raw[:]
        for li, vid in sorted(insertions, reverse=True):
            ins = []
            prev = out[li-1] if li > 0 else ''
            if prev.strip() != '':
                ins.append('')
            ins.append("![[%s#^%s]]" % (a.link_base, vid))
            out[li:li] = ins
        open(a.commentary, 'w', encoding='utf-8').write('\n'.join(out))
        open(a.commentary, encoding='utf-8').read()  # validate decode
        print("APPLIED %d insertions" % len(insertions))

if __name__ == '__main__':
    main()
