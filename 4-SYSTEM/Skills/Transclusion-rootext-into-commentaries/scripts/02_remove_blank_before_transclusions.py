#!/usr/bin/env python3
"""STAGE 2 - Reposition each verse transclusion to sit right before that
verse's OWN sa-bcad (ས་བཅད) block, when the verse has one; otherwise leave
it right before the verse (Stage 1's placement).

NOTE ON THE FILENAME: this script used to just delete the blank line above a
transclusion. It has been rewritten to reposition the transclusion itself.
The filename is kept for now so existing pipeline notes/commands still work;
rename it to 02_reposition_before_sachad.py next time you have shell access
to the vault if you want the name to match the new behaviour.

A "sa-bcad block" is the contiguous run of structural lines directly above
the transclusion:
  - an ordinal-led line (དང་པོ, གཉིས་པ, གསུམ་པ, ... བཅུ་པ) - but ONLY when it
    is heading-anchored or does not itself read as a conclusion (see the
    "ordinal-priority" note below - this is the part that changed after a
    real placement bug was found and fixed);
  - a heading ending ནི། / ནི། །  (short, <= 60 collapsed syllables);
  - an enumeration opener ending ལ། / ལ་ཡང་། / ལས། / ཏེ། / སྟེ།  (short);
  - an enumeration member/closer ending དང་། / a closing member
    (…པའོ།/…བའོ།/…ནོ།/…ལོ།) / a count word  (short).

Ordinary commentary prose, connectors (དེའི་རྗེས་སུ།, དེའི་འཐད་པར།,
དེའི་འཐད་པ་ནི།), quotation/commentary conclusions (containing ཞེས/ཅེས), and
root-verse-line fragments (ending དང་། །  or  དང་ནི། །) are NOT structural
and stop the walk - this is the exact classification Stage 3 used to use to
decide where to drop a blank line; Stage 2 now reuses it to decide where to
move the transclusion itself.

ORDINAL-PRIORITY, AND WHY IT NOW REQUIRES A HEADING ANCHOR
------------------------------------------------------------
An ordinal-led block is usually a sa-bcad announcement even when it folds its
own extended explanation into the same paragraph (e.g. "བཞི་པ་...ནི། <several
sentences> ཞེས་པའི་དོན་ནོ།"), so trailing ཞེས/ཅེས text should not by itself
mask an ordinal opener at the front of a block. BUT a real placement bug
(caught by a human reviewer against the ^5-49 / ^5-50 pair, then confirmed
against several more instances in the same file - ^9-79, ^9-110, ^9-154)
showed that an ordinal word at the front of a paragraph is NOT always a fresh
sa-bcad for the verse that follows. Two recurring false-positive shapes:

  1. A commentary announces a flat numbered list once in prose ("there are
     27 gateways for faults... first: X, second: Y...") and then walks
     through the list's items one by one across several verses' worth of
     exposition, sometimes packing several list items into ONE verse's
     gloss. Every item still starts a fresh paragraph with its ordinal word,
     but most of them are explaining a WORD OR CLAUSE of the verse that was
     JUST quoted, not introducing the verse that comes next. (^5-49's
     "གཉིས་པ" continues the prior verse's own explanation; ^5-50's "ལྔ་པ"
     glosses a word ("ང་རྒྱལ") that is already inside the verse quoted
     immediately above it.)
  2. An opponent's objection is elaborated with its own internal step
     numbering ("...so they say: second, applying analysis to the analysis
     itself, third, and so on, it would never end") - again ordinal-led,
     again not a sa-bcad for what follows. (^9-110.)

The one structural feature that reliably distinguishes a GENUINE sa-bcad
resumption from these false positives in this vault is a true markdown
heading (any #...# line ending in a block ID like ^1-2-3-...-0) sitting a
short distance above the ordinal line, restating the same topic - see ^1-3,
^8-120, ^9-118 for confirmed-genuine examples of this shape. So: an
ordinal-led block is trusted unconditionally (kept as an 'open' sa-bcad
opener even if it contains ཞེས/ཅེས) only when such a heading is found within
the last few structural blocks above it. Without a heading anchor, an
ordinal-led block that itself contains a ཞེས/ཅེས conclusion falls back to the
plain conclusion test and is treated as 'none' (not a sa-bcad opener) - the
transclusion then stays right before the verse, which is always the safe
default when a sa-bcad can't be confidently identified.

This is a heuristic, not certainty - a handful of genuinely fresh
transitional arguments (an ordinal opening a new causal point with no
repeated heading text, e.g. ^6-25 in this file) will also fall back to
"stays before verse" under this rule when they contain ཞེས/ཅེས. That is the
intended, conservative trade-off: a missed sa-bcad placement (verse quoted a
few lines later than ideal) is a much smaller error than a WRONG sa-bcad
placement (root verse displaced across another verse's own commentary
material). Cases like this are exactly what --report is for: skim the
"stays before verse" list for chapters with heavy enumeration/debate prose
and hand-place any genuine sa-bcad the heuristic was too conservative about.

Rule:
  * If the line immediately above the transclusion is structural (per the
    ordinal-priority rule above), walk up the contiguous structural run, trim
    any leading member-only lines so the block begins at a genuine
    opener/heading/ordinal, and move the transclusion to sit immediately
    before that first line - i.e. right before the verse's own sa-bcad.
  * If the line immediately above is NOT structural (prose / connector /
    conclusion / root-verse fragment / an unanchored ordinal ending in
    ཞེས/ཅེས), or the contiguous run above contains no genuine
    opener/heading/ordinal (so it isn't really a sa-bcad block), the
    transclusion is left exactly where Stage 1 put it: right before the
    verse.

Only the ![[...]] line itself is ever moved. No commentary text is added,
removed, reordered, or rephrased, and no blank lines are touched here -
blank-line spacing around the (possibly moved) transclusion is Stage 3's job
(03_blank_before_sachad.py, which now normalizes one blank line before AND
after every transclusion).

Idempotent: running this twice does not move an already-repositioned
transclusion again, because the line now sitting directly above it (whatever
preceded the sa-bcad block) is no longer itself structural.

Usage:
  python3 02_remove_blank_before_transclusions.py --commentary <path> [--chapter N|all] --report   # dry run
  python3 02_remove_blank_before_transclusions.py --commentary <path> [--chapter N|all] --apply
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
def has_zhes(s): return 'ཞེས' in s or 'ཅེས' in s

def is_heading(line):
    """True markdown heading line (#... **text** ^...-0). A heading is always
    classified 'none' by kind() - it never counts as sa-bcad prose itself -
    but one sitting a short distance above an ordinal-led block is the
    strongest available signal that the block is a genuine sa-bcad resuming
    that heading's topic, rather than mid-exposition prose that merely
    happens to start a paragraph with an ordinal word. See the
    ORDINAL-PRIORITY note at the top of this file."""
    s = line.strip()
    return bool(re.match(r'^#{1,12}\s', s)) and bool(re.search(r'-0\s*$', s))

def prev_nonblank(ls, idx):
    """Index of the nearest non-blank line before idx, skipping blank lines
    (every block in this vault's segmented commentaries sits on its own
    paragraph, separated by a blank line, so 'immediately above' has to be
    read at the block level, not the raw-line level). Returns -1 if none."""
    p = idx - 1
    while p >= 0 and ls[p].strip() == '':
        p -= 1
    return p

def heading_anchor_nearby(ls, idx, steps=3):
    """True if a true markdown heading sits within the last `steps`
    structural/non-blank blocks above idx (skipping blanks via
    prev_nonblank). Transclusion lines break the search (a heading is
    meaningful context only if it is still "current", i.e. nothing else has
    been transcluded from a different verse in between)."""
    q = prev_nonblank(ls, idx)
    for _ in range(steps):
        if q < 0:
            return False
        if is_heading(ls[q]):
            return True
        if ls[q].strip().startswith('!['):
            return False
        q = prev_nonblank(ls, q)
    return False

def kind(ls, idx):
    """'open' (block-opener: heading/opener/ordinal), 'mem' (member), or
    'none', for the line at ls[idx]."""
    s = ls[idx].strip()
    if not s or s.startswith('![['): return 'none'
    if s in CONNECTORS: return 'none'
    if starts_ord(s):
        # Ordinal-priority, gated by a heading anchor - see the top-of-file
        # note. Anchored: trust it unconditionally (even with a trailing
        # ཞེས/ཅེས conclusion folded into the same paragraph). Unanchored:
        # fall through to the plain conclusion/length tests below, same as
        # any other line - a bare ordinal word with no heading nearby and no
        # ཞེས/ཅེස conclusion can still qualify as 'open' via HEAD_END/OPEN_END.
        if heading_anchor_nearby(ls, idx) or not has_zhes(s):
            return 'open'
    if has_zhes(s): return 'none'        # quotation / conclusion
    if s.endswith('དང་། །') or s.endswith('དང་ནི། །'): return 'none'  # verse fragment
    L = clen(s)
    if ends_any(s, HEAD_END) and L <= 60: return 'open'
    if ends_any(s, OPEN_END) and L <= 60: return 'open'
    if ends_any(s, MEM_END)  and L <= 60: return 'mem'
    return 'none'

def find_block_start(ls, i):
    """Index of the first line of the sa-bcad block directly above the
    transclusion at i (skipping intervening blank lines), or None if there
    is no immediate sa-bcad."""
    j = prev_nonblank(ls, i)
    if j < 0 or kind(ls, j) == 'none':
        return None
    # walk up the contiguous (blank-agnostic) run of structural blocks
    run = [j]
    p = prev_nonblank(ls, j)
    while p >= 0 and kind(ls, p) != 'none':
        run.append(p)
        p = prev_nonblank(ls, p)
    run.reverse()  # topmost structural block first, closest-to-transclusion last
    # trim leading member-only blocks: the block must START at an opener/heading
    for k in run:
        if kind(ls, k) == 'open':
            return k
    return None

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--commentary', required=True)
    ap.add_argument('--chapter', default='all')
    ap.add_argument('--report', action='store_true')
    ap.add_argument('--apply', action='store_true')
    a = ap.parse_args()

    ls = open(a.commentary, 'rb').read().decode('utf-8', 'replace').split('\n')

    trans = []  # (original index, vid)
    for i, l in enumerate(ls):
        m = re.search(r'#\^([IVXLCDM]+|\d+)-(\d+)\]\]', l)
        if l.strip().startswith('![[') and m:
            if a.chapter != 'all' and m.group(1) != str(a.chapter): continue
            trans.append((i, "%s-%s" % (m.group(1), m.group(2))))

    targets = {}   # original transclusion index -> index to insert-before
    pending = {}   # target index -> [transclusion line text, ...], in original order
    moved = 0
    for i, vid in trans:
        s = find_block_start(ls, i)
        target = s if s is not None else i
        targets[i] = target
        pending.setdefault(target, []).append(ls[i])
        if s is not None:
            moved += 1

    print("transclusions=%d  moved-before-sachad=%d  left-before-verse=%d" %
          (len(trans), moved, len(trans) - moved))
    if a.report:
        for i, vid in trans:
            t = targets[i]
            if t == i:
                print("  ^%-7s stays before verse (line %d)" % (vid, i + 1))
            else:
                print("  ^%-7s moves before sa-bcad '%s...' (line %d -> %d)" %
                      (vid, ls[t].strip()[:30], i + 1, t + 1))

    if a.apply and trans:
        trans_idx = {i for i, _ in trans}
        out = []
        for idx in range(len(ls)):
            if idx in pending:
                out.extend(pending[idx])
            if idx not in trans_idx:
                out.append(ls[idx])
        if len(ls) in pending:  # edge case: target is end-of-file
            out.extend(pending[len(ls)])
        open(a.commentary, 'w', encoding='utf-8').write('\n'.join(out))
        open(a.commentary, encoding='utf-8').read()  # validate decode
        print("APPLIED")

if __name__ == '__main__':
    main()
