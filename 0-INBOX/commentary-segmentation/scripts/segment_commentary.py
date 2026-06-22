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
import unicodedata
from pathlib import Path

TSHEG     = "་"  # U+0F0B TIBETAN MARK INTERSYLLABIC TSHEG
SHAD      = "།"   # U+0F0D TIBETAN MARK SHAD
NYIS_SHAD = "༎"  # U+0F0E TIBETAN MARK NYIS SHAD
SHAD_CLUSTER = rf"[{SHAD}{NYIS_SHAD}](?:[\s{TSHEG}]*[{SHAD}{NYIS_SHAD}])*"

# Order matters when two rules legitimately end at the exact same shad (e.g.
# the quote-closing formula also satisfies terminal-particle's generic
# "[consonant]+o-vowel + shad" pattern). starts/ends in find_cuts() keep only
# the first-registered name per position, so the more specific markers are
# listed first; terminal-particle -- the broad catch-all for whatever isn't
# claimed by a more specific rule -- is listed last.
RULES = [
    # quote-close: standard closing formulas for citations.
    ("quote-close", "after",
     re.compile(rf"(?:ཞེས་སོ|ཅེས་སོ|ཞེས་གསུངས་སོ|ཞེས་བཤད་དོ|ཞེས་པའོ|ཅེས་པའོ|ཞེས་བྱ་བའོ){SHAD_CLUSTER}")),
    # quote-open: source-attribution markers (ལས།, གསུངས།) get their own block
    # before the cited passage. Rule fires BEFORE the marker.
    ("quote-open", "before",
     re.compile(rf"(?:ལས|གསུངས){SHAD_CLUSTER}")),
    # enumeration-head: sa-bcad head closing after a number word + suffix.
    # Suffix required (ལས/སྟེ/སུ/དུ/ཡོད/ནས/པོ) to avoid bare number words mid-compound.
    ("enumeration-head", "after",
     re.compile(rf"(?:གཉིས|གསུམ|བཞི|ལྔ|དྲུག|བདུན|བརྒྱད|དགུ|བཅུ)་(?:ལས|སྟེ|སུ|དུ|ཡོད|ནས|པོ){SHAD_CLUSTER}")),
    # ordinal-open: standard section openers དང་པོ་, གཉིས་པ་, གསུམ་པ་ …
    ("ordinal-open", "before",
     re.compile(rf"(?:དང་པོ|གཉིས་པ|གསུམ་པ|བཞི་པ|ལྔ་པ|དྲུག་པ|བདུན་པ|བརྒྱད་པ|དགུ་པ|བཅུ་པ)་")),
    # objection-close: question/objection final markers ཅེ་ན།, ཞེ་ན།, སྙམ་ན།
    ("objection-close", "after",
     re.compile(rf"(?:ཅེ་ན|ཞེ་ན|སྙམ་ན){SHAD_CLUSTER}")),
    # objection-open: reply opener འོ་ན་
    ("objection-open", "before",
     re.compile(rf"འོ་ན་")),
    # terminal-particle: sentence-final linking particles. Generic catch-all,
    # listed last on purpose (see note above RULES).
    # Fix 1: .འོ (.འོ) catches བའོ (བའོ), དའོ (དའོ), etc.
    #        (consonants below U+0F60 were missed by the old [འ-ྼ]འོ range).
    # Fix 2: added ག (ག) and ལ (ལ) for གོ and ལོ.
    ("terminal-particle", "after",
     re.compile(rf"(?:.འོ|[ནདསཏརངབམགལ]ོ){SHAD_CLUSTER}")),
]

SEP = "\n\n"
HEADING_RE = re.compile(r"^#{1,6}\s")
FRONTMATTER_RE = re.compile(r"^---\n.*?\n---\n", re.DOTALL)

# --- verse-stanza detection (documented in SKILL.md, previously unimplemented) ---
# A paragraph counts as one protected verse stanza when: it ends in a strong
# (double) shad cluster; splitting on every shad cluster yields 2-4 non-empty
# pieces (padas); every pada has 6-11 tsheg-delimited syllables; and the
# syllable counts are uniform across padas (max-min <= 1). Detected stanzas
# are emitted whole, are never run through the rule engine or cap_segment,
# and are never flagged STAGE2_REVIEW regardless of total length.
PADA_MIN_SYL = 6
PADA_MAX_SYL = 11
PADA_COUNT_RANGE = (2, 4)
PADA_UNIFORMITY_TOLERANCE = 1


def detect_stanza(paragraph: str):
    """Return the list of pada strings if `paragraph` is one verse stanza,
    else None. Only matches when the *entire* paragraph is the stanza (no
    leftover prose after the closing double shad) -- a verse embedded inside
    a larger prose paragraph is out of scope here per SKILL.md and is left
    for Stage 2 to isolate by hand."""
    stripped = paragraph.strip()
    if not stripped:
        return None
    pieces = []
    last_end = 0
    final_cluster = ""
    for m in re.finditer(SHAD_CLUSTER, stripped):
        end = m.end()
        piece = stripped[last_end:end]
        if piece.strip():
            pieces.append(piece)
            final_cluster = m.group(0)
        last_end = end
    if stripped[last_end:].strip():
        return None  # trailing non-shad-terminated content -- not a clean stanza
    if not (PADA_COUNT_RANGE[0] <= len(pieces) <= PADA_COUNT_RANGE[1]):
        return None
    if final_cluster.count(SHAD) + final_cluster.count(NYIS_SHAD) < 2:
        return None  # must close on a strong (double) shad
    syllables = [count_syllables(p) for p in pieces]
    if any(not (PADA_MIN_SYL <= s <= PADA_MAX_SYL) for s in syllables):
        return None
    if max(syllables) - min(syllables) > PADA_UNIFORMITY_TOLERANCE:
        return None
    return pieces


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


# Rules with no shad/punctuation anchor of their own are prone to firing on
# a coincidental syllable sequence that isn't actually functioning as that
# marker in context (objection-open "འོ་ན་" is the clearest case: nothing in
# the pattern itself requires it to be starting a clause). Require these to
# sit close after a shad cluster to auto-cut; otherwise downgrade to a
# reported candidate and leave the text uncut, so a human decides instead of
# the script committing to a cut on weak evidence.
WEAK_CONTEXT_RULES = {"objection-open"}
WEAK_CONTEXT_WINDOW = 12


def _near_shad_before(line: str, pos: int, window: int) -> bool:
    return bool(re.search(SHAD_CLUSTER, line[max(0, pos - window):pos]))


def find_cuts(line: str):
    """Returns (split_positions, starts, ends, candidates).

    A "before" rule (quote-open, ordinal-open, objection-open) names the
    piece that BEGINS at its cut position -- e.g. quote-open's whole point is
    to give the citation marker its own block, so "ལས།" itself must carry
    the name, not whatever happened to end just before it. An "after" rule
    names the piece that ENDS at its cut position. Collecting these into two
    separate maps (instead of one dict keyed only by position) lets
    segment_line attach the correct name to each side of every cut, even
    when an after-cut and a before-cut land back to back at the same point.
    """
    split_positions = set()
    starts: dict = {}
    ends: dict = {}
    candidates = []
    for name, kind, pat in RULES:
        for m in pat.finditer(line):
            pos = m.end() if kind == "after" else m.start()
            if not valid_cut(line, pos):
                continue
            if name in WEAK_CONTEXT_RULES and not _near_shad_before(line, m.start(), WEAK_CONTEXT_WINDOW):
                preview = line[max(0, pos - 20):pos + 20].strip()[:80]
                candidates.append({"name": name, "preview": preview})
                continue
            split_positions.add(pos)
            (ends if kind == "after" else starts).setdefault(pos, name)
    return sorted(split_positions), starts, ends, candidates


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


# quote-open/quote-close must stay isolated on their own line per the
# citation-formatting rule (format-commentary §3) -- never merged into a
# neighbour even if both sides are short.
MERGE_PROTECTED_PREFIXES = ("quote-open", "quote-close")


def _is_merge_protected(trigger: str) -> bool:
    return trigger.startswith(MERGE_PROTECTED_PREFIXES)


def merge_short_segments(segments: list, rows: list, max_syllables: int):
    """Counter over-fragmentation: when two or more trigger rules fire close
    together they can leave consecutive segments well under the 1-2-sentence
    target. Merge adjacent segments while the combined length still fits the
    cap and neither side is a protected citation boundary. Keeps every
    contributing rule name in the report (joined with "+") rather than
    collapsing to just the first one, so the audit trail of *why* each piece
    of the merged block was originally cut stays visible."""
    merged_segments, merged_rows = [], []
    i = 0
    while i < len(segments):
        seg = segments[i]
        triggers = [rows[i]["trigger"]]
        j = i + 1
        while (j < len(segments)
               and not _is_merge_protected(triggers[-1])
               and not _is_merge_protected(rows[j]["trigger"])
               and count_syllables(seg + segments[j]) <= max_syllables):
            seg = seg + segments[j]
            triggers.append(rows[j]["trigger"])
            j += 1
        if len(triggers) == 1:
            # Nothing merged -- keep the original row (and its flag) untouched.
            merged_segments.append(seg)
            merged_rows.append(rows[i])
        else:
            trigger = "+".join(triggers) + "(merged)"
            merged_segments.append(seg)
            merged_rows.append({"trigger": trigger, "syllables": count_syllables(seg),
                                "flag": "", "preview": seg.strip()[:80].replace("\t", " ").replace("\n", "↵")})
        i = j
    return merged_segments, merged_rows


def segment_line(line: str, max_syllables: int):
    positions, starts, ends, candidates = find_cuts(line)
    raw = []
    start = 0
    for pos in positions:
        piece = line[start:pos]
        if piece.strip():
            # Prefer the before-rule that begins this piece; otherwise fall
            # back to the after-rule that ends it.
            name = starts.get(start) or ends.get(pos) or "line-end"
            raw.append((piece, name))
        start = pos
    tail = line[start:]
    if tail.strip():
        raw.append((tail, starts.get(start) or "line-end"))
    segments = []
    report = []
    for piece, name in raw:
        for i, sub in enumerate(cap_segment(piece, max_syllables)):
            trigger = name if i == 0 else name + "+maxcap"
            syl = count_syllables(sub)
            segments.append(sub)
            preview = sub.strip()[:80].replace("\t", " ").replace("\n", "↵")
            if syl > max_syllables:
                # Distinguish "no internal shad to split on at all" (needs a
                # full hand-read to find a break) from "had shads, capping
                # still couldn't fit everything under budget".
                flag = ("STAGE2_REVIEW" if re.search(SHAD_CLUSTER, sub)
                        else "STAGE2_REVIEW:NO_SHAD_FOUND")
            else:
                flag = ""
            report.append({"trigger": trigger, "syllables": syl,
                           "flag": flag, "preview": preview})
    segments, report = merge_short_segments(segments, report, max_syllables)
    for c in candidates:
        # Weak-context match: not auto-cut, just surfaced for human judgement.
        report.append({"trigger": c["name"] + "-candidate", "syllables": 0,
                       "flag": "STAGE2_REVIEW", "preview": c["preview"]})
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
        stanza_padas = detect_stanza(para)
        if stanza_padas is not None:
            block = para.strip()
            out_parts.append(block)
            preview = block[:80].replace("\t", " ").replace("\n", "↵")
            report.append({"trigger": "verse-stanza", "syllables": count_syllables(block),
                           "flag": "", "preview": preview})
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
    text = unicodedata.normalize("NFC", Path(args.input).read_text(encoding="utf-8"))
    segmented, report = process(text, args.max_syllables)
    assert_no_loss(text, segmented)
    n_segments = len(report)
    n_flagged = sum(1 for r in report if r["flag"])
    n_quote_open = sum(1 for r in report if r["trigger"].startswith("quote-open"))
    n_quote_close = sum(1 for r in report if r["trigger"].startswith("quote-close"))
    quote_status = "OK" if n_quote_open == n_quote_close else "MISMATCH"
    print(f"{args.input}: {n_segments} segments, {n_flagged} flagged for Stage-2 review.")
    print(f"Quote balance: {n_quote_open} quote-open / {n_quote_close} quote-close -> {quote_status}"
          + ("" if quote_status == "OK" else " -- check citations for an unclosed or stray quote marker."))
    if args.report:
        with Path(args.report).open("w", encoding="utf-8") as fh:
            fh.write("index\ttrigger\tsyllables\tflag\tpreview\n")
            for i, r in enumerate(report, 1):
                fh.write(f"{i}\t{r['trigger']}\t{r['syllables']}\t{r['flag']}\t{r['preview']}\n")
            fh.write(f"SUMMARY\tquote-balance\t{n_quote_open}\t{quote_status}\topen={n_quote_open} close={n_quote_close}\n")
        print(f"Report: {args.report}")
    if not args.dry_run:
        out = Path(args.output)
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(segmented, encoding="utf-8")
        print(f"Wrote {args.output}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
