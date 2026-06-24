#!/usr/bin/env python3
"""Stage-2 refinement for \u0f62\u0f71\u0f56\u0f0b\u0f42\u0f66\u0f63 commentary segmentation.

Splits long segments by detecting sub-clause connector particles in Tibetan
prose. Also splits citation lead-ins from verse blocks so rendered markdown
does not collapse padas into a single run-on line.

Strong connectors (reliable clause-boundary markers):
  \u0f45\u0f72\u0f44\u0f0b  jing/cing  gerundive coordinator
  \u0f5e\u0f72\u0f44\u0f0b  zhing      alternate spelling
  \u0f66\u0f9f\u0f7a\u0f0b  ste        coordinative
  \u0f4f\u0f7a\u0f0b         te         alternate spelling
  \u0f53\u0f66\u0f0b         ne         sequential
  \u0f63\u0f66\u0f0b         le         ablative/causal

No character of body text is altered; only paragraph boundaries are inserted.

Usage:
    python3 stage2_rabsal.py INPUT.md OUTPUT.md [options]

Options:
    --max-syllables N    Syllable cap (default: 40)
    --report FILE.tsv    Write a TSV report
    --dry-run            Parse and validate but do not write files
"""
from __future__ import annotations

import argparse
import re
import sys
import unicodedata
from pathlib import Path

TSHEG     = "\u0f0b"   # tsheg
SHAD      = "\u0f0d"   # single shad
NYIS_SHAD = "\u0f0e"   # nyis-shad

FRONTMATTER_RE = re.compile(r"^---\n.*?\n---\n", re.DOTALL)

# Strong connectors: reliable Tibetan sub-clause boundary markers
STRONG_CONNECTORS = [
    "\u0f45\u0f72\u0f44\u0f0b",   # cing/jing
    "\u0f5e\u0f72\u0f44\u0f0b",   # zhing
    "\u0f66\u0f9f\u0f7a\u0f0b",   # ste
    "\u0f4f\u0f7a\u0f0b",           # te
    "\u0f53\u0f66\u0f0b",           # ne
    "\u0f63\u0f66\u0f0b",           # le
]

MIN_PIECE_SYL = 8


def count_syllables(text):
    return text.count(TSHEG) + (1 if text.strip() else 0)


def _squeeze(s):
    return re.sub(r"\s+", "", s)


_LA_EXCLUSIONS = [
    "\u0f42\u0f0b\u0f63\u0f0b",   # ga-la (interrogative particle)
]


def _connector_positions(text, connectors):
    excluded_ends = set()
    for excl in _LA_EXCLUSIONS:
        start = 0
        while True:
            idx = text.find(excl, start)
            if idx == -1:
                break
            excluded_ends.add(idx + len(excl))
            start = idx + 1
    positions = []
    for conn in connectors:
        start = 0
        while True:
            idx = text.find(conn, start)
            if idx == -1:
                break
            end = idx + len(conn)
            if end not in excluded_ends:
                positions.append(end)
            start = idx + 1
    positions.sort()
    return positions


def _greedy_split_at(text, max_syl, positions):
    pieces = []
    start = 0
    while start < len(text):
        remaining = text[start:]
        if count_syllables(remaining) <= max_syl:
            pieces.append(remaining)
            break
        best = None
        for pos in positions:
            if pos <= start:
                continue
            chunk_syl = count_syllables(text[start:pos])
            if MIN_PIECE_SYL <= chunk_syl <= max_syl:
                best = pos
            elif chunk_syl > max_syl:
                break
        if best is not None:
            pieces.append(text[start:best])
            start = best
        else:
            first_after = next((p for p in positions if p > start), None)
            if first_after:
                pieces.append(text[start:first_after])
                start = first_after
            else:
                pieces.append(remaining)
                break
    return [p for p in pieces if p.strip()]


def _valid_split(pieces):
    return all(count_syllables(p) >= MIN_PIECE_SYL for p in pieces)


def _is_citation_leadin_verse(block):
    """Return (True, lead, verse) if block = citation lead-in + verse padas.

    Pattern: first line ends in a single shad (citation marker, e.g.
    mdo las/) and all remaining lines are verse padas ending in \u0f0d\u0f0d
    or \u0f0e. The lead-in must be split off as its own paragraph so that
    rendered markdown does not collapse the newlines into a run-on line.
    Returns (False, "", "") if pattern does not match.
    """
    lines = [l for l in block.split("\n") if l.strip()]
    if len(lines) < 2:
        return False, "", ""
    first = lines[0].strip()
    rest = lines[1:]
    if not first.endswith(SHAD) or first.endswith(SHAD + SHAD):
        return False, "", ""
    if not all(
        l.strip().endswith(SHAD + SHAD) or l.strip().endswith(NYIS_SHAD)
        for l in rest
    ):
        return False, "", ""
    verse = "\n".join(l.strip() for l in rest)
    return True, first, verse


def split_segment(text, max_syl):
    stripped = text.strip()
    if count_syllables(stripped) <= max_syl:
        return [stripped], "none"
    positions = _connector_positions(stripped, STRONG_CONNECTORS)
    if positions:
        pieces = _greedy_split_at(stripped, max_syl, positions)
        if all(count_syllables(p) <= max_syl for p in pieces) and _valid_split(pieces):
            return pieces, "strong"
    return [stripped], "manual"


def process(text, max_syl=40):
    """Return (refined_text, report_rows)."""
    fm = FRONTMATTER_RE.match(text)
    if fm:
        head = fm.group(0).rstrip("\n")
        body = text[fm.end():]
    else:
        head = None
        body = text

    paras = re.split(r"\n\n", body)
    out = []
    report = []
    seg_idx = 0

    for para in paras:
        stripped = para.strip()
        if not stripped:
            out.append(para)
            continue
        seg_idx += 1
        syl = count_syllables(stripped)

        if syl > max_syl and "\n" not in stripped:
            pieces, method = split_segment(stripped, max_syl)
            out.extend(pieces)
            report.append({
                "index": seg_idx, "syl_before": syl,
                "pieces": len(pieces), "method": method,
                "preview": stripped[:80].replace("\t", " "),
            })
        elif "\n" in stripped:
            matched, lead, verse = _is_citation_leadin_verse(stripped)
            if matched:
                out.append(lead)
                out.append(verse)
                report.append({
                    "index": seg_idx, "syl_before": syl,
                    "pieces": 2, "method": "citation-split",
                    "preview": stripped[:80].replace("\t", " "),
                })
            else:
                out.append(para)
        else:
            out.append(para)

    refined = "\n\n".join(out)
    if head:
        refined = head + "\n\n" + refined.lstrip("\n")
    return refined + "\n", report


def main(argv):
    ap = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    ap.add_argument("input")
    ap.add_argument("output")
    ap.add_argument("--max-syllables", type=int, default=40)
    ap.add_argument("--report")
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args(argv[1:])

    text = unicodedata.normalize("NFC", Path(args.input).read_text(encoding="utf-8"))
    refined, report = process(text, args.max_syllables)

    if _squeeze(text) != _squeeze(refined):
        print("ABORT: Stage-2 altered non-whitespace content. No file written.",
              file=sys.stderr)
        return 1

    n_strong   = sum(1 for r in report if r["method"] == "strong")
    n_citation = sum(1 for r in report if r["method"] == "citation-split")
    n_manual   = sum(1 for r in report if r["method"] == "manual")
    print("Stage-2 complete: {} segments processed.".format(len(report)))
    print("  {} split via strong connectors".format(n_strong))
    print("  {} citation lead-in split from verse block".format(n_citation))
    print("  {} unchanged (STAGE2_MANUAL)".format(n_manual))
    print("No-loss check: PASSED")

    if args.report:
        with Path(args.report).open("w", encoding="utf-8") as fh:
            fh.write("index\tsyl_before\tpieces\tmethod\tpreview\n")
            for r in report:
                fh.write("{}\t{}\t{}\t{}\t{}\n".format(
                    r["index"], r["syl_before"], r["pieces"],
                    r["method"], r["preview"]))
        print("Report: {}".format(args.report))

    if not args.dry_run:
        out_path = Path(args.output)
        out_path.parent.mkdir(parents=True, exist_ok=True)
        out_path.write_text(refined, encoding="utf-8")
        print("Wrote {}".format(args.output))

    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
