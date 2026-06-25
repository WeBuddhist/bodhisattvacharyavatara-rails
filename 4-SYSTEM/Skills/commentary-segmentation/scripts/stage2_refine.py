#!/usr/bin/env python3
"""Stage-2 semantic refinement for Tibetan commentary segmentation.

Reusable, text-agnostic refinement of a Stage-1 (`segment_commentary.py`)
draft. Stage 1 leaves two kinds of residue that no lexical rule can resolve
safely on its own; this tool handles both deterministically and leaves
everything genuinely ambiguous for a human:

  1. NEWLINE EXPANSION (default, the primary documented Stage-2 action).
     `merge_short_segments` in Stage 1 joins consecutive source lines that
     were each below the syllable cap, leaving internal `\\n` inside a block.
     For any block longer than --max-syllables that contains an internal
     `\\n`, every `\\n` is promoted to a paragraph break (`\\n\\n`) — each
     original source line becomes its own block. This never guesses a cut
     point; it only restores boundaries the source itself already marked.

  2. CITATION LEAD-IN / VERSE SPLIT (default).
     A short source-frame line (e.g. `…ལས།`, < PADA_MIN_SYL syllables, or
     ending in a single shad) that was glued onto the following verse stanza
     is peeled back onto its own paragraph, so the citation marker and the
     stanza occupy separate blocks (format-commentary §3).

  3. CONNECTOR SPLIT (opt-in: --split-connectors).
     Over-long *single-line* prose blocks (no internal `\\n`) are split at
     strong sub-clause connector particles (cing/zhing/ste/te/ne/le), greedily,
     never producing a piece below MIN_PIECE_SYL. Off by default because a
     connector boundary is a weaker signal than a source-marked line break —
     prefer leaving an over-long block whole (and flagged) over a wrong cut.

Anything still over the cap after the enabled passes is reported as
STAGE2_MANUAL: a human must read it and decide. Over-long is safer than wrong.

No character of body text is ever altered — only paragraph boundaries are
inserted. Before writing, the output (whitespace-squeezed) is asserted equal
to the input; if --source is given, it is also asserted equal to the original
source, so any deviation inherited from Stage 1 is caught here rather than
silently passed downstream (SKILL.md Stage-2 note).

Usage:
    python3 stage2_refine.py INPUT.md OUTPUT.md [options]

Options:
    --max-syllables N    Blocks above this are candidates for refinement (40).
    --split-connectors   Also split long single-line prose at connectors.
    --source FILE        Original source file; output is no-loss-checked against
                         it as well as against INPUT.
    --report FILE.tsv    Write a per-block TSV report.
    --dry-run            Validate but write nothing.
"""
from __future__ import annotations

import argparse
import sys
import unicodedata
from pathlib import Path

TSHEG     = "་"   # tsheg
SHAD      = "།"   # single shad
NYIS_SHAD = "༎"   # nyis-shad

import re

FRONTMATTER_RE = re.compile(r"^---\n.*?\n---\n", re.DOTALL)

# Verse-pada syllable window (kept consistent with segment_commentary.py).
PADA_MIN_SYL = 6
PADA_MAX_SYL = 11

# Strong connectors: reliable Tibetan sub-clause boundary markers, used only
# when --split-connectors is requested.
STRONG_CONNECTORS = [
    "ཅིང་",   # cing / jing  (gerundive coordinator)
    "ཞིང་",   # zhing        (alternate spelling)
    "སྟེ་",   # ste          (coordinative)
    "ཏེ་",         # te           (alternate spelling)
    "ནས་",         # ne           (sequential)
    "ལས་",         # le           (ablative / causal)
]
# Sequences whose tail coincides with a connector but is not one (e.g. ga-la,
# the interrogative particle, ends in "la" but must not be split).
_CONNECTOR_EXCLUSIONS = ["ག་ལ་"]  # ga-la
MIN_PIECE_SYL = 8

# Same whitespace-squeeze table as segment_commentary.py, so the no-loss check
# here agrees byte-for-byte with the Stage-1 check (SKILL.md warns that a
# different squeeze can report phantom mismatches).
_WS_TABLE = str.maketrans("", "", "".join(chr(c) for c in (
    0x20, 0x09, 0x0A, 0x0D, 0x0C, 0x0B,
    0xA0, 0x1680,
    0x2000, 0x2001, 0x2002, 0x2003, 0x2004,
    0x2005, 0x2006, 0x2007, 0x2008, 0x2009, 0x200A,
    0x2028, 0x2029,
    0x202F, 0x205F,
    0x3000,
)))


def squeeze(s: str) -> str:
    return s.translate(_WS_TABLE)


def count_syllables(text: str) -> int:
    return text.count(TSHEG) + (1 if text.strip() else 0)


def _is_pada_unit(s: str) -> bool:
    return PADA_MIN_SYL <= count_syllables(s.strip()) <= PADA_MAX_SYL


def _ends_double_shad(s: str) -> bool:
    s = s.strip()
    return s.endswith(SHAD + SHAD) or s.endswith(SHAD + " " + SHAD) or s.endswith(NYIS_SHAD)


def _is_citation_leadin_verse(block: str):
    """If block = [citation/short lead-in line] + [>=1 verse pada lines],
    return (lead, verse_text); else None.

    The lead-in is recognised as a first line that is NOT itself a pada
    (either shorter than a pada, or ending in a single shad rather than a
    double shad) while every following line IS a verse pada ending in a
    double shad / nyis-shad. Covers both stage2 predecessors' patterns."""
    lines = [l for l in block.split("\n") if l.strip()]
    if len(lines) < 2:
        return None
    first, rest = lines[0].strip(), [l.strip() for l in lines[1:]]
    if not all(_ends_double_shad(l) and _is_pada_unit(l) for l in rest):
        return None
    # First line is a lead-in if it is short, or a single-shad citation frame.
    first_is_leadin = (
        count_syllables(first) < PADA_MIN_SYL
        or (first.endswith(SHAD) and not _ends_double_shad(first))
    )
    if not first_is_leadin:
        return None
    return first, "\n".join(rest)


def _connector_positions(text: str):
    excluded_ends = set()
    for excl in _CONNECTOR_EXCLUSIONS:
        start = 0
        while (idx := text.find(excl, start)) != -1:
            excluded_ends.add(idx + len(excl))
            start = idx + 1
    positions = []
    for conn in STRONG_CONNECTORS:
        start = 0
        while (idx := text.find(conn, start)) != -1:
            end = idx + len(conn)
            if end not in excluded_ends:
                positions.append(end)
            start = idx + 1
    return sorted(positions)


def _split_at_connectors(text: str, max_syl: int):
    """Greedily split `text` at connector positions so each piece is between
    MIN_PIECE_SYL and max_syl syllables. Returns the piece list (>=1)."""
    positions = _connector_positions(text)
    if not positions:
        return [text]
    pieces, start = [], 0
    while start < len(text):
        if count_syllables(text[start:]) <= max_syl:
            pieces.append(text[start:])
            break
        best = None
        for pos in positions:
            if pos <= start:
                continue
            syl = count_syllables(text[start:pos])
            if MIN_PIECE_SYL <= syl <= max_syl:
                best = pos
            elif syl > max_syl:
                break
        if best is None:
            best = next((p for p in positions if p > start), None)
            if best is None:
                pieces.append(text[start:])
                break
        pieces.append(text[start:best])
        start = best
    pieces = [p for p in pieces if p.strip()]
    # Reject a split that stranded a sub-minimal fragment; keep the block whole.
    if any(count_syllables(p) < MIN_PIECE_SYL for p in pieces):
        return [text]
    return pieces or [text]


def process(text: str, max_syllables: int = 40, split_connectors: bool = False):
    """Return (refined_text, report_rows)."""
    fm = FRONTMATTER_RE.match(text)
    head = fm.group(0).rstrip("\n") if fm else None
    body = text[fm.end():] if fm else text

    out, report = [], []
    for idx, para in enumerate(re.split(r"\n\n", body), 1):
        stripped = para.strip()
        if not stripped:
            out.append(para)
            continue
        syl = count_syllables(stripped)
        has_nl = "\n" in stripped

        cited = _is_citation_leadin_verse(stripped)
        if cited:
            lead, verse = cited
            out.extend([lead, verse])
            report.append({"index": idx, "syl": syl, "pieces": 2,
                           "method": "citation-split", "preview": stripped[:60]})
            continue

        if has_nl and syl > max_syllables:
            # Newline expansion: each source line becomes its own block.
            parts = [p for p in stripped.split("\n") if p.strip()]
            out.extend(parts)
            report.append({"index": idx, "syl": syl, "pieces": len(parts),
                           "method": "newline-expand", "preview": stripped[:60]})
            continue

        if split_connectors and not has_nl and syl > max_syllables:
            parts = _split_at_connectors(stripped, max_syllables)
            if len(parts) > 1:
                out.extend(parts)
                report.append({"index": idx, "syl": syl, "pieces": len(parts),
                               "method": "connector-split", "preview": stripped[:60]})
                continue

        # Nothing safe to do.
        out.append(para)
        if syl > max_syllables:
            report.append({"index": idx, "syl": syl, "pieces": 1,
                           "method": "STAGE2_MANUAL", "preview": stripped[:60]})

    refined = "\n\n".join(out)
    if head:
        refined = head + "\n\n" + refined.lstrip("\n")
    return refined + "\n", report


def main(argv):
    ap = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("input")
    ap.add_argument("output")
    ap.add_argument("--max-syllables", type=int, default=40)
    ap.add_argument("--split-connectors", action="store_true",
                    help="also split long single-line prose at strong connectors")
    ap.add_argument("--source", help="original source file for an extra no-loss check")
    ap.add_argument("--report")
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args(argv[1:])

    text = unicodedata.normalize("NFC", Path(args.input).read_text(encoding="utf-8"))
    refined, report = process(text, args.max_syllables, args.split_connectors)

    if squeeze(text) != squeeze(refined):
        sys.exit("ABORT: Stage-2 altered non-whitespace content vs input. No file written.")
    if args.source:
        src = unicodedata.normalize("NFC", Path(args.source).read_text(encoding="utf-8"))
        if squeeze(src) != squeeze(refined):
            sys.exit("ABORT: output diverges from original source "
                     "(pre-existing Stage-1 deviation?). No file written.")

    n_nl   = sum(1 for r in report if r["method"] == "newline-expand")
    n_cit  = sum(1 for r in report if r["method"] == "citation-split")
    n_conn = sum(1 for r in report if r["method"] == "connector-split")
    n_man  = sum(1 for r in report if r["method"] == "STAGE2_MANUAL")
    print(f"{args.input}: {n_nl} newline-expanded, {n_cit} citation-split, "
          f"{n_conn} connector-split, {n_man} left for manual review.")
    print("No-loss check: PASSED" + (" (incl. --source)" if args.source else ""))

    if args.report:
        with Path(args.report).open("w", encoding="utf-8") as fh:
            fh.write("index\tsyllables\tpieces\tmethod\tpreview\n")
            for r in report:
                fh.write(f"{r['index']}\t{r['syl']}\t{r['pieces']}\t{r['method']}\t{r['preview']}\n")
        print(f"Report: {args.report}")

    if not args.dry_run:
        out = Path(args.output)
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(refined, encoding="utf-8")
        print(f"Wrote {args.output}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
