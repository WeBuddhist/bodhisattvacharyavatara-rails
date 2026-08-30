#!/usr/bin/env python3
"""STAGE 3 - Normalize blank-line spacing so exactly ONE blank line sits
immediately before AND immediately after every verse transclusion, wherever
Stage 2 left it (right before the verse's own sa-bcad block, or right before
the verse itself when it has none):

    <preceding line>

    ![[link-base#^N-V]]

    <following line>

NOTE ON THE FILENAME: this script used to only add a blank line before a
sa-bcad block. It has been rewritten to normalize spacing on both sides of
every transclusion instead (the sa-bcad-vs-verse decision now lives entirely
in Stage 2). The filename is kept for now so existing pipeline notes/commands
still work; rename it to 03_blank_around_transclusions.py next time you have
shell access to the vault if you want the name to match the new behaviour.

Multiple existing blank lines touching a transclusion are collapsed down to
exactly one; a missing blank is inserted. No text is touched, and no blank
line anywhere else in the file is affected. A transclusion at the very start
or very end of the file gets no leading/trailing blank (there is nothing on
that side to separate it from).

Idempotent: running this twice makes no further changes.

Usage:
  python3 03_blank_before_sachad.py --commentary <path>          # dry run
  python3 03_blank_before_sachad.py --commentary <path> --apply
"""
import re, argparse

def is_trans(line):
    return bool(line.strip().startswith('![[') and re.search(r'#\^([IVXLCDM]+|\d+)-(\d+)\]\]', line))

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--commentary', required=True)
    ap.add_argument('--apply', action='store_true')
    a = ap.parse_args()

    raw = open(a.commentary, 'rb').read().decode('utf-8', 'replace')
    ls = raw.split('\n')
    n = len(ls)

    out = []
    added_before = added_after = collapsed = 0
    i = 0
    while i < n:
        line = ls[i]
        if is_trans(line):
            # --- spacing before ---
            if out:
                if out[-1].strip() != '':
                    out.append('')
                    added_before += 1
                else:
                    while len(out) >= 2 and out[-2].strip() == '':
                        out.pop()
                        collapsed += 1
            out.append(line)
            # --- spacing after ---
            j = i + 1
            saw_blank = False
            blanks_seen = 0
            while j < n and ls[j].strip() == '':
                saw_blank = True
                blanks_seen += 1
                j += 1
            if j < n:
                out.append('')
                if not saw_blank:
                    added_after += 1
                elif blanks_seen > 1:
                    collapsed += 1
            i = j
            continue
        out.append(line)
        i += 1

    print("blank lines added before: %d   added after: %d   collapsed: %d" %
          (added_before, added_after, collapsed))
    if a.apply:
        open(a.commentary, 'w', encoding='utf-8').write('\n'.join(out))
        open(a.commentary, encoding='utf-8').read()  # validate decode
        print("APPLIED")

if __name__ == '__main__':
    main()
