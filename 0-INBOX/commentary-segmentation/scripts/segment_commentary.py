#!/usr/bin/env python3
"""Stage-1 deterministic boundary detection for Tibetan commentary segmentation.

Inserts paragraph boundaries at high-confidence functional boundaries in the
Tibetan (quotation frames, objection/answer markers, sa-bcad enumerations,
sentence-final terminal particles). After the rule-based pass it enforces a
syllable cap: any segment still longer than --max-syllables is split at shad
(clause) boundaries. It only ever *inserts* paragraph breaks, never edits a
character, and does NOT assign block IDs.

Usage:
    python3 segment_commentary.py INPUT.md OUTPUT.md [--report REPORT.tsv]
                                  [--max-syllables N] [--dry-run]
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

TSHEG     = "\u0f0b"  # U+0F0B TIBETAN MARK INTERSYLLABIC TSHEG
SHAD      = "\u0f0d"   # U+0F0D TIBETAN MARK SHAD
NYIS_SHAD = "\u0f0e"  # U+0F0E TIBETAN MARK NYIS SHAD
SHAD_CLUSTER = rf"[{SHAD}{NYIS_SHAD}](?:[\s{TSHEG}]*[{SHAD}{NYIS_SHAD}])*"

RULES = [
    # terminal-particle: sentence-final linking particles.
    # Fix 1: .\u0f60\u0f7c (.འོ) catches \u0f56\u0f60\u0f7c (བའོ), \u0f51\u0f60\u0f7c (དའོ), etc.
    #        (consonants below U+0F60 were missed by the old [\u0f60-\u0fbc]འོ range).
    # Fix 2: added \u0f42 (ག) and \u0f63 (ལ) for གོ and ལོ.
    ("terminal-particle", "after",
     re.compile(rf"(?:.\u0f60\u0f7c|[\u0f53\u0f51\u0f66\u0f4f\u0f62\u0f44\u0f56\u0f58\u0f42\u0f63]\u0f7c){SHAD_CLUSTER}")),
    # quote-close: standard closing formulas for citations.
    ("quote-close", "after",
     re.compile(rf"(?:\u0f5e\u0f7a\u0f66\u0f0b\u0f66\u0f7c|\u0f45\u0f7a\u0f66\u0f0b\u0f66\u0f7c|\u0f5e\u0f7a\u0f66\u0f0b\u0f42\u0f66\u0f74\u0f44\u0f66\u0f0b\u0f66\u0f7c|\u0f5e\u0f7a\u0f66\u0f0b\u0f56\u0f64\u0f51\u0f0b\u0f51\u0f7c|\u0f5e\u0f7a\u0f66\u0f0b\u0f54\u0f60\u0f7c|\u0f45\u0f7a\u0f66\u0f0b\u0f54\u0f60\u0f7c|\u0f5e\u0f7a\u0f66\u0f0b\u0f56\u0fb1\u0f0b\u0f56\u0f60\u0f7c){SHAD_CLUSTER}")),
    # quote-open: source-attribution markers (ལས།, གསུངས།) get their own block
    # before the cited passage. Rule fires BEFORE the marker.
    ("quote-open", "before",
     re.compile(rf"(?:\u0f63\u0f66|\u0f42\u0f66\u0f74\u0f44\u0f66){SHAD_CLUSTER}")),
    # enumeration-head: sa-bcad head closing after a number word + suffix.
    # Suffix required (ལས/སྟེ/སུ/དུ/ཡོད/ནས/པོ) to avoid bare number words mid-compound.
    ("enumeration-head", "after",
     re.compile(rf"(?:\u0f42\u0f49\u0f72\u0f66|\u0f42\u0f66\u0f74\u0f58|\u0f56\u0f5e\u0f72|\u0f63\u0f94|\u0f51\u0fb2\u0f74\u0f42|\u0f56\u0f51\u0f74\u0f53|\u0f56\u0f62\u0f92\u0fb1\u0f51|\u0f51\u0f42\u0f74|\u0f56\u0f45\u0f74)\u0f0b(?:\u0f63\u0f66|\u0f66\u0f9f\u0f7a|\u0f66\u0f74|\u0f51\u0f74|\u0f61\u0f7c\u0f51|\u0f53\u0f66|\u0f54\u0f7c){SHAD_CLUSTER}")),
    # ordinal-open: standard section openers དང་པོ་, གཉིས་པ་, གསུམ་པ་ …
    ("ordinal-open", "before",
     re.compile(rf"(?:\u0f51\u0f44\u0f0b\u0f54\u0f7c|\u0f42\u0f49\u0f72\u0f66\u0f0b\u0f54|\u0f42\u0f66\u0f74\u0f58\u0f0b\u0f54|\u0f56\u0f5e\u0f72\u0f0b\u0f54|\u0f63\u0f94\u0f0b\u0f54|\u0f51\u0fb2\u0f74\u0f42\u0f0b\u0f54|\u0f56\u0f51\u0f74\u0f53\u0f0b\u0f54|\u0f56\u0f62\u0f92\u0fb1\u0f51\u0f0b\u0f54|\u0f51\u0f42\u0f74\u0f0b\u0f54|\u0f56\u0f45\u0f74\u0f0b\u0f54)\u0f0b")),
    # objection-close: question/objection final markers ཅེ་ན།, ཞེ་ན།, སྙམ་ན།
    ("objection-close", "after",
     re.compile(rf"(?:\u0f45\u0f7a\u0f0b\u0f53|\u0f5e\u0f7a\u0f0b\u0f53|\u0f66\u0f99\u0f58\u0f0b\u0f53){SHAD_CLUSTER}")),
    # objection-open: reply opener འོ་ན་
    ("objection-open", "before",
     re.compile(rf"\u0f60\u0f7c\u0f0b\u0f53\u0f0b")),
]

SEP = "\n\n"
HEADING_RE = re.compile(r"^#{1,6}\s")
FRONTMATTER_RE = re.compile(r"^---\n.*?\n---\n", re.DOTALL)


def count_syllables(text: str) -> int:
    return text.count(TSHEG) + (1 if text.strip() else 0)


def valid_cut(line: str, pos: int) -> bool:
    """Reject cuts that would break mid-phrase.

    A cut is only legal at a real clause/enumeration boundary, marked in
    Tibetan by a shad. A position whose preceding non-space character is a
    tsheg sits inside a phrase and would strand a dangling syllable
    (e.g. sa|dang-po, dpe|dang-po); such cuts are forbidden.
    """
    if not (0 < pos < len(line.rstrip())):
        return False
    return not line[:pos].rstrip().endswith(TSHEG)


def find_cuts(line: str):
    cuts = {}
    for name, kind, pat in RULES:
        for m in pat.finditer(line):
            pos = m.end() if kind == "after" else m.start()
            if valid_cut(line, pos):
                cuts.setdefault(pos, name)
    return sorted(cuts.items())


def _shad_bounds(piece: str, strong_only: bool):
    bounds = []
    for m in re.finditer(SHAD_CLUSTER, piece):
        end = m.end()
        if 0 < end < len(piece.rstrip()):
            strength = m.group(0).count(SHAD) + m.group(0).count(NYIS_SHAD)
            if strong_only and strength < 2:
                continue
            bounds.append(end)
    return bounds


def _greedy_wrap(piece: str, max_syllables: int, strong_only: bool):
    bounds = _shad_bounds(piece, strong_only)
    if not bounds:
        return [piece]
    bounds = bounds + [len(piece)]
    result = []
    start = 0
    last_ok = None
    for p in bounds:
        if count_syllables(piece[start:p]) <= max_syllables:
            last_ok = p
        else:
            if last_ok is not None and last_ok > start:
                result.append(piece[start:last_ok])
                start = last_ok
                last_ok = None
            if count_syllables(piece[start:p]) <= max_syllables:
                last_ok = p
            else:
                result.append(piece[start:p])
                start = p
                last_ok = None
    if start < len(piece):
        result.append(piece[start:])
    return [r for r in result if r.strip()]


def cap_segment(piece: str, max_syllables: int):
    if count_syllables(piece) <= max_syllables:
        return [piece]
    out = []
    for p in _greedy_wrap(piece, max_syllables, strong_only=True):
        if count_syllables(p) > max_syllables:
            out.extend(_greedy_wrap(p, max_syllables, strong_only=False))
        else:
            out.append(p)
    return out


def segment_line(line: str, max_syllables: int):
    cuts = find_cuts(line)
    raw = []
    start = 0
    for pos, name in cuts:
        piece = line[start:pos]
        if piece.strip():
            raw.append((piece, name))
        start = pos
    tail = line[start:]
    if tail.strip():
        raw.append((tail, "line-end"))
    segments = []
    report = []
    for piece, name in raw:
        for i, sub in enumerate(cap_segment(piece, max_syllables)):
            trigger = name if i == 0 else name + "+maxcap"
            syl = count_syllables(sub)
            segments.append(sub)
            preview = sub.strip()[:80].replace("\t", " ").replace("\n", "\u21b5")
            report.append({"trigger": trigger, "syllables": syl,
                           "flag": "STAGE2_REVIEW" if syl > max_syllables else "",
                           "preview": preview})
    return segments, report


def process(text: str, max_syllables: int):
    out_parts = []
    report = []
    fm = FRONTMATTER_RE.match(text)
    if fm:
        out_parts.append(fm.group(0).rstrip("\n"))
        body = text[fm.end():]
    else:
        body = text
    for para in re.split(r"\n\s*\n", body):
        if not para.strip():
            continue
        if HEADING_RE.match(para.strip()):
            out_parts.append(para.strip())
            continue
        segments, rows = segment_line(para, max_syllables)
        out_parts.extend(seg.strip() for seg in segments)
        report.extend(rows)
    return SEP.join(out_parts) + "\n", report


def assert_no_loss(original: str, segmented: str):
    squeeze = lambda s: re.sub(r"\s+", "", s)
    if squeeze(original) != squeeze(segmented):
        sys.exit("ABORT: segmentation altered non-whitespace content. No file written.")


def main(argv):
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("input")
    ap.add_argument("output")
    ap.add_argument("--report", help="write a TSV segmentation report here")
    ap.add_argument("--max-syllables", type=int, default=50)
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args(argv[1:])
    text = Path(args.input).read_text(encoding="utf-8")
    segmented, report = process(text, args.max_syllables)
    assert_no_loss(text, segmented)
    n_segments = len(report)
    n_flagged = sum(1 for r in report if r["flag"])
    print(f"{args.input}: {n_segments} segments, {n_flagged} flagged for Stage-2 review.")
    if args.report:
        with Path(args.report).open("w", encoding="utf-8") as fh:
            fh.write("index\ttrigger\tsyllables\tflag\tpreview\n")
            for i, r in enumerate(report, 1):
                fh.write(f"{i}\t{r['trigger']}\t{r['syllables']}\t{r['flag']}\t{r['preview']}\n")
        print(f"Report: {args.report}")
    if not args.dry_run:
        out = Path(args.output)
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(segmented, encoding="utf-8")
        print(f"Wrote {args.output}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
