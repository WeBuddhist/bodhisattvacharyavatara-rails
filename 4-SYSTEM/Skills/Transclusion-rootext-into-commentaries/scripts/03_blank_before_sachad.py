#!/usr/bin/env python3
"""STAGE 3 - Insert a blank line before the sa-chad (ས་བཅད) block that introduces
each verse transclusion.

Rules implemented:
  * If the line immediately above the transclusion is a sa-chad (a structural
    announcement: an ordinal-led line, a ...ནི། heading, or a ...ལ།/...ལས།/...ཏེ།
    enumeration opener), insert ONE blank line before that sa-chad.
  * If a sa-chad ENUMERATION (a contiguous run of openers + member lines) sits
    right before the immediate sa-chad, insert the blank before the FIRST line of
    that whole run, not before the immediate sa-chad.
  * If there is NO immediate sa-chad above the transclusion (the line above is
    ordinary commentary prose, a connector such as དེའི་རྗེས་སུ། / དེའི་འཐད་པར།, a
    commentary conclusion such as ...ཞེས་པའོ། །, or a root-verse fragment), insert
    nothing.

The block-start is found by walking up the contiguous structural run above the
transclusion and trimming any leading member-only lines so the block begins at a
genuine opener/heading/ordinal. Prose is excluded by a ཞེས/ཅེས test and a length
cap; verse-line fragments (ending in དང་། །) are excluded.

Usage:
  python3 03_blank_before_sachad.py --commentary <path> [--chapter N|all] [--apply]
  python3 03_blank_before_sachad.py --commentary <path> --report   # show every decision
"""
import re, argparse

ORD = ['དང་པོ','གཉིས་པ','གསུམ་པ','བཞི་པ','ལྔ་པ','དྲུག་པ','བདུན་པ','བརྒྱད་པ','དགུ་པ','བཅུ་པ']
CONNECTORS = ['དེའི་རྗེས་སུ།','དེའི་འཐད་པར།','དེའི་འཐད་པ་ནི།']

HEAD_END = ('ནི།','ནི། །','ནི།།')
OPEN_END = ('ལ།','ལ་ཡང་།','ལ་ཡང༌།','ལས།','ཏེ།','སྟེ།')
MEM_END  = ('དང་།','དང༌།','དང་། །',
            'པའོ། །','པའོ།།','བའོ། །','བའོ།།',
            'ནོ། །','ནོ།།','ལོ། །','ལོ།།',
            'གཅིག།','གཉིས།','གསུམ།','བཞི།','ལྔ།','དྲུག།','བདུན།','བརྒྱད།','དགུ།','བཅུ།',
            'གསུམ་ལས།','གཉིས་ལས།','ཡོན།')

def clen(s):
    return len(s.replace('་','').replace('།','').replace(' ','').replace('༎','').strip())
def starts_ord(s): return any(s.startswith(o) for o in ORD)
def ends_any(s, group): return any(s.endswith(x) for x in group)

def kind(line):
    """'open' (block-opener: heading/opener/ordinal), 'mem' (member), or 'none'."""
    s = line.strip()
    if not s or s.startswith('![['): return 'none'
    if s in CONNECTORS: return 'none'
    if 'ཞེས' in s or 'ཅེས' in s: return 'none'        # quotation / conclusion
    if s.endswith('དང་། །') or s.endswith('དང་ནི། །'): return 'none'  # verse fragment
    L = clen(s)
    if starts_ord(s): return 'open'
    if ends_any(s, HEAD_END) and L <= 60: return 'open'
    if ends_any(s, OPEN_END) and L <= 60: return 'open'
    if ends_any(s, MEM_END)  and L <= 60: return 'mem'
    return 'none'

def find_block_start(ls, i):
    """Index where the blank goes (first line of the sa-chad block above the
    transclusion at i), or None if there is no immediate sa-chad."""
    if i == 0: return None
    if kind(ls[i-1]) == 'none':
        return None
    j = i - 1
    while j-1 >= 0 and kind(ls[j-1]) != 'none':
        j -= 1
    # trim leading member-only lines: the block must START at an opener/heading
    for k in range(j, i):
        if kind(ls[k]) == 'open':
            return k
    return None

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--commentary', required=True)
    ap.add_argument('--chapter', default='all')
    ap.add_argument('--apply', action='store_true')
    ap.add_argument('--report', action='store_true')
    a = ap.parse_args()

    ls = open(a.commentary, 'rb').read().decode('utf-8', 'replace').split('\n')

    decisions = []  # (vid, transclusion_line, block_start_or_None)
    for i, l in enumerate(ls):
        m = re.search(r'#\^(\d+)-(\d+)\]\]', l)
        if not (l.strip().startswith('![[') and m): continue
        if a.chapter != 'all' and m.group(1) != str(a.chapter): continue
        s = find_block_start(ls, i)
        decisions.append(("%s-%s" % (m.group(1), m.group(2)), i, s))

    inserts = sorted({s for _, _, s in decisions
                      if s is not None and (s == 0 or ls[s-1].strip() != '')})

    if a.report:
        for vid, i, s in decisions:
            if s is None:
                print("^%-7s NO-BLANK   | above: %s" % (vid, ls[i-1].strip()[:46]))
            else:
                print("^%-7s BLANK@%-5d | %s" % (vid, s+1, ls[s].strip()[:46]))
    print("blank lines to insert: %d  (verses with sa-chad: %d / %d)" %
          (len(inserts), sum(1 for _,_,s in decisions if s is not None), len(decisions)))

    if a.apply:
        out = ls[:]
        for s in sorted(inserts, reverse=True):
            out[s:s] = ['']
        open(a.commentary, 'w', encoding='utf-8').write('\n'.join(out))
        open(a.commentary, encoding='utf-8').read()  # validate
        print("APPLIED")

if __name__ == '__main__':
    main()
