#!/usr/bin/env python3
"""
ingest_toc_commentary.py - inject TOC headings into an existing commentary file.

Reads a commentary (read-only) and writes a headed copy to 0-INBOX/.
Never modifies the source file.

Primary strategy — LINE NUMBER (fast, exact):
  Each TOC entry carries a [[N]] suffix (source line number from the extraction
  pass). When N is a valid integer the heading is inserted directly above that
  line — no text search needed.

Fallback strategy (when suffix is [[?]] or absent):
  Title match - search for the title text in the source, starting AFTER the
  parent entry's position.

Heading format (all depths):
    ### <decimal> <title> ^<decimal-with-dashes>-0

Fixes applied:
  - Sibling constraint: fallback search starts after the previous sibling's
    located line, preventing matches in early enumeration/preview blocks.
  - Clamped sort order: when multiple entries share the same insertion line,
    they are sorted by their natural (pre-clamp) order.

Usage:
    python 4-SYSTEM/scripts/toc_tree_extractor/ingest_toc_commentary.py \\
        0-INBOX/toc-tree-BCAC20_TG_bo.md \\
        1-SOURCES/Commentaries/BCAC20_TG_bo.md

Output defaults to: 1-SOURCES/Commentaries/commentaries_with_toc/<source_stem>.toc.md
"""

import argparse
import re
import sys
from pathlib import Path

# ---------------------------------------------------------------------------
# Tibetan canonicalisation
# ---------------------------------------------------------------------------
_TSHEG = "འ"  # U+0F60 TIBETAN LETTER -A  (tsheg: U+0F0B)
_TSHEG = "་"  # actual tsheg
_SHAD_CHARS = "།༎༏༐༑༒༔"
_SHAD_OR_WS_RE = re.compile("[" + _SHAD_CHARS + r"\s]+")


def tib_canon(s):
    """Strip shad/whitespace, keep tsheg as syllable separator."""
    if not s:
        return ""
    s = _SHAD_OR_WS_RE.sub(_TSHEG, s)
    s = re.sub(re.escape(_TSHEG) + "+", _TSHEG, s)
    return s.strip(_TSHEG)


# ---------------------------------------------------------------------------
# TOC tree parser
# ---------------------------------------------------------------------------
_TREE_RE = re.compile(
    r"^\s*\*\s+(?P<dec>\d+(?:\.\d+)*)\.?\s+"
    r"(?P<title>[^\[]+?)(?:\s*\[\[(?P<suffix>[^\]]*)\]\])?\s*$"
)


def parse_toc(path):
    """Return list of (dec, title, line_no) where line_no is an int (1-based
    source line number from [[N]]) or None when the suffix is [[?]] or absent."""
    entries = []
    for line in path.read_text(encoding="utf-8").splitlines():
        m = _TREE_RE.match(line)
        if not m:
            continue
        dec = m.group("dec")
        title = m.group("title").strip().rstrip("།").strip()
        suffix = (m.group("suffix") or "").strip()
        line_no = None
        if suffix and suffix != "?":
            try:
                line_no = int(suffix)
            except ValueError:
                pass   # non-numeric suffix — treat as no line number
        entries.append((dec, title, line_no))
    return entries


# ---------------------------------------------------------------------------
# Source text index
# ---------------------------------------------------------------------------

def build_index(lines):
    """Return (canon_text, offsets) where offsets[i] = (line_idx, char_pos)."""
    parts = []
    offsets = []
    pos = 0
    for i, line in enumerate(lines):
        c = tib_canon(line)
        offsets.append((i, pos))
        if c:
            parts.append(c)
            pos += len(c) + 1  # +1 for joining tsheg
    canon_text = _TSHEG.join(p for p in parts if p)
    return canon_text, offsets


def canon_pos_to_line(offsets, char_pos):
    best = 0
    for line_idx, canon_start in offsets:
        if canon_start <= char_pos:
            best = line_idx
        else:
            break
    return best


def line_to_canon_pos(offsets, line_idx):
    for li, cp in offsets:
        if li >= line_idx:
            return cp
    return offsets[-1][1] if offsets else 0


def find_in_canon(canon_text, query, after_pos=0, min_match=0.5):
    """Return (char_pos, score) for best match of query starting at after_pos."""
    if not query:
        return None, 0.0

    segment = canon_text[after_pos:]
    offset = after_pos

    # pass 1: verbatim
    idx = segment.find(query)
    if idx != -1:
        return offset + idx, 1.0

    # pass 2: longest matching syllable window
    q_sylls = [s for s in query.split(_TSHEG) if s]
    n = len(q_sylls)
    if not q_sylls:
        return None, 0.0

    best_pos = None
    best_len = 0
    for window in range(n, 0, -1):
        if window <= best_len:
            break
        for ci in range(n - window + 1):
            needle = _TSHEG.join(q_sylls[ci:ci + window])
            ti = segment.find(needle)
            if ti != -1 and window > best_len:
                best_len = window
                best_pos = offset + ti
        if best_len > 0 and best_len >= n * min_match:
            break

    if best_pos is None or best_len / n < min_match:
        return None, (best_len / n if best_len else 0.0)
    return best_pos, best_len / n


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    ap = argparse.ArgumentParser(
        description="Inject TOC headings into a commentary (output to 0-INBOX/).")
    ap.add_argument("toc_file",    help="toc-tree-<id>.md")
    ap.add_argument("source_file", help="Commentary .md")
    ap.add_argument("--out",       default=None,
                    help="Output file (default: 0-INBOX/<stem>.toc.md)")
    ap.add_argument("--min-match", type=float, default=0.5,
                    help="Min syllable-match fraction (default: 0.5)")
    args = ap.parse_args()

    toc_path = Path(args.toc_file).expanduser().resolve()
    src_path = Path(args.source_file).expanduser().resolve()

    for p in (toc_path, src_path):
        if not p.exists():
            sys.exit("Error: file not found: " + str(p))

    if args.out:
        out_path = Path(args.out).expanduser().resolve()
    else:
        vault_root = src_path.parent
        for parent in [src_path.parent] + list(src_path.parents):
            if (parent / "4-SYSTEM").is_dir():
                vault_root = parent
                break
        out_path = vault_root / "1-SOURCES" / "Commentaries" / "commentaries_with_toc" / (src_path.stem + ".toc.md")

    entries = parse_toc(toc_path)
    if not entries:
        sys.exit("No TOC entries found.")

    lines = src_path.read_text(encoding="utf-8").splitlines(keepends=True)
    canon_text, offsets = build_index(lines)

    print("TOC:    {} ({} entries)".format(toc_path, len(entries)))
    print("Source: {} ({} lines)".format(src_path, len(lines)))
    print("Out:    {}".format(out_path))
    print()

    # insertions[line_idx] = [(natural_line, heading), ...]
    # natural_line = where the entry was located (before clamping), used for sort order
    insertions = {}
    dec_line = {}        # dec -> located line index (for parent chaining)
    depth_last_line = {} # depth -> last natural line located at that depth (sibling constraint)

    def parent_dec(dec):
        parts = dec.split(".")
        return ".".join(parts[:-1]) if len(parts) > 1 else None

    def parent_line_for(dec):
        pdec = parent_dec(dec)
        while pdec:
            pl = dec_line.get(pdec)
            if pl is not None:
                return pl
            pdec = parent_dec(pdec)
        return None

    def after_pos_for(dec):
        pl = parent_line_for(dec)
        return line_to_canon_pos(offsets, pl + 1) if pl is not None else 0

    def _title_search(query, after, label):
        """Fuzzy title search with sibling/parent constraint and full-text retry."""
        cp, sc = find_in_canon(canon_text, query, after_pos=after,
                               min_match=args.min_match)
        if cp is not None:
            return cp, sc, label
        cp0, sc0 = find_in_canon(canon_text, query, after_pos=0,
                                 min_match=args.min_match)
        if cp0 is None:
            return None, sc0, label
        if cp0 < after:
            cp2, sc2 = find_in_canon(canon_text, query,
                                     after_pos=cp0 + 1,
                                     min_match=args.min_match)
            if cp2 is not None and cp2 >= after:
                return cp2, sc2, label + "(body)"
        return cp0, sc0, label + "(full)"

    for dec, title, line_no in entries:
        depth = len(dec.split("."))
        block_id = "^" + dec.replace(".", "-") + "-0"
        heading = "{} {} {}".format("#" * depth, title, block_id)

        parent_line = parent_line_for(dec)
        located_line = None
        natural_line = None
        score = 0.0
        method = ""

        # ── Strategy 1: use the [[N]] line number from the TOC tree ──────────
        if line_no is not None:
            # line_no is 1-based; convert to 0-based index and insert ABOVE that line
            located_line = max(0, line_no - 1)
            natural_line = located_line
            score = 1.0
            method = "line#"

        # ── Strategy 2: fallback title search (for [[?]] entries) ────────────
        if located_line is None:
            after_cp = after_pos_for(dec)
            prev_sib_line = depth_last_line.get(depth)
            if prev_sib_line is not None:
                prev_sib_cp = line_to_canon_pos(offsets, prev_sib_line + 1)
                if prev_sib_cp > after_cp:
                    after_cp = prev_sib_cp
            cp, score, method = _title_search(tib_canon(title), after_cp, "title")
            if cp is not None:
                located_line = canon_pos_to_line(offsets, cp)
                natural_line = located_line

        # clamp: never insert before parent
        if located_line is not None and parent_line is not None:
            if located_line < parent_line:
                located_line = parent_line + 1
                method += "+clamped"

        if natural_line is not None:
            depth_last_line[depth] = natural_line

        dec_line[dec] = located_line

        if located_line is not None:
            print("  [{}] score={:3.0%}  line {:4}  [{}]  {}".format(
                dec, score, located_line + 1, method, title[:50]))
            nat = natural_line if natural_line is not None else located_line
            insertions.setdefault(located_line, []).append((nat, heading))
        else:
            fallback_line = (parent_line + 1) if parent_line is not None else 0
            print("  [{}] NO MATCH  [fallback line {}]  {}".format(
                dec, fallback_line + 1, title[:50]))
            insertions.setdefault(fallback_line, []).append(
                (fallback_line, heading + "  <!-- not found -->"))

    # Rebuild file with headings injected (blank line before and after each block).
    # Multiple headings at the same line are sorted by natural (pre-clamp) position.
    out_lines = []
    for i, line in enumerate(lines):
        pairs = insertions.get(i, [])
        if pairs:
            heads = [h for _, h in sorted(pairs, key=lambda x: x[0])]
            if out_lines and out_lines[-1].strip():
                out_lines.append("\n")
            for h in heads:
                out_lines.append(h + "\n")
            out_lines.append("\n")
        out_lines.append(line)

    for i in sorted(k for k in insertions if k >= len(lines)):
        out_lines.append("\n")
        for _, h in sorted(insertions[i], key=lambda x: x[0]):
            out_lines.append(h + "\n")

    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text("".join(out_lines), encoding="utf-8")
    print()
    print("Written -> {}".format(out_path))


if __name__ == "__main__":
    main()
