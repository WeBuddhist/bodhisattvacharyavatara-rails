#!/usr/bin/env python3
"""Reorder commentator blocks so His Holiness the Dalai Lama's commentary
(`tenzin-gyatso`) comes FIRST in every "Commentary Explanations" section.

Works on both the English day packages (conformed: with `<!-- cm:* -->` anchors
and consolidated `Sources:` lines) and the Tibetan source packages (unconformed:
`#### དོན་འགྲེལ།` heading, inline `([[...]])` citations). Idempotent: if
tenzin-gyatso is already first, the file is left unchanged.
"""
import re
import sys

H5 = re.compile(r'^#####\s+(\S+)')
ANCHOR_BLOCK = re.compile(r'^<!--\s*(?:cm|story|div):')       # travels WITH its block
ANCHOR_ID = re.compile(r'^<!--\s*(?:cm|story|div):([A-Za-z0-9._:-]+)\s*-->')
ANCHOR_SECT = re.compile(r'^<!--\s*(?:sub|verse|sec):')       # marks the NEXT section
HEAD_LE4 = re.compile(r'^#{2,4}\s')
HHDL = "tenzin-gyatso"


def is_commentary_heading(line):
    return line.startswith("#### Commentary Explanations") or (
        line.startswith("#### ") and "དོན་འགྲེལ" in line)


def reorder_content(content):
    c = content[:]
    # peel trailing tail (blank lines / '---' / the next section's anchor)
    tail = []
    while c:
        s = c[-1].strip()
        if s == "" or s == "---" or ANCHOR_SECT.match(s):
            tail.insert(0, c.pop())
        else:
            break
    # locate H5 block starts (carry a preceding cm/story/div anchor into the block)
    starts = []
    for k, l in enumerate(c):
        if H5.match(l):
            start = k - 1 if (k > 0 and ANCHOR_BLOCK.match(c[k - 1].strip())) else k
            starts.append((start, k))
    if not starts:
        return content
    head = c[:starts[0][0]]
    blocks = []
    for bi, (start, h5) in enumerate(starts):
        end = starts[bi + 1][0] if bi + 1 < len(starts) else len(c)
        # the machine id lives in the cm/story/div anchor (headings are display-only);
        # fall back to the heading's first token for un-anchored legacy blocks.
        am = ANCHOR_ID.match(c[start].strip())
        bid = am.group(1) if am else H5.match(c[h5]).group(1)
        blocks.append((bid, c[start:end]))
    if blocks[0][0] == HHDL:
        return content                       # already first
    hhdl = [b for b in blocks if b[0] == HHDL]
    if not hhdl:
        return content                       # no HHDL block here
    rest = [b for b in blocks if b[0] != HHDL]
    new = list(head)
    for _bid, blk in hhdl + rest:
        new += blk
    new += tail
    return new


def reorder(path):
    text = open(path, encoding="utf-8").read()
    lines = text.split("\n")
    idx = 0
    while idx < len(lines):
        if is_commentary_heading(lines[idx]):
            j = idx + 1
            while j < len(lines) and not HEAD_LE4.match(lines[j]):
                j += 1
            lines[idx + 1:j] = reorder_content(lines[idx + 1:j])
            idx = idx + 1
        else:
            idx += 1
    new = "\n".join(lines)
    if new != text:
        open(path, "w", encoding="utf-8").write(new)
        print(f"reordered: {path}")
        return True
    print(f"unchanged: {path}")
    return False


if __name__ == "__main__":
    for p in sys.argv[1:]:
        reorder(p)
