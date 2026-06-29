#!/usr/bin/env python3
"""STAGE 2 - Remove the blank line that sits immediately ABOVE each verse
transclusion, so the transclusion sits directly under the preceding commentary
line (commentary line -> transclusion -> verse text, no gap).

Only the single blank line directly before a  ![[...]]  line is removed. No other
blank lines and no text are touched.

Usage:
  python3 02_remove_blank_before_transclusions.py --commentary <path> [--apply]
"""
import argparse

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--commentary', required=True)
    ap.add_argument('--apply', action='store_true')
    a = ap.parse_args()

    # read leniently so a stray truncated final byte does not abort the run
    raw = open(a.commentary, 'rb').read().decode('utf-8', 'replace')
    lines = raw.split('\n')

    out = []; removed = 0
    for l in lines:
        if l.strip().startswith('![[') and out and out[-1].strip() == '':
            out.pop(); removed += 1
        out.append(l)

    print("blank lines that would be removed: %d" % removed)
    if a.apply:
        open(a.commentary, 'w', encoding='utf-8').write('\n'.join(out))
        open(a.commentary, encoding='utf-8').read()  # validate
        print("APPLIED")

if __name__ == '__main__':
    main()
