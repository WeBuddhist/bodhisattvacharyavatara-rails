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

# Pre-compiled Pattern for SHAD_CLUSTER — used directly in _split_clause_units,
# scan_segments, and _shad_bounds to avoid per-call re.compile() overhead.
_SHAD_CLUSTER_RE = re.compile(SHAD_CLUSTER)

# Order matters when two rules legitimately end at the exact same shad (e.g.
# the quote-closing formula also satisfies terminal-particle's generic
# "[consonant]+o-vowel + shad" pattern). starts/ends in find_cuts() keep only
# the first-registered name per position, so the more specific markers are
# listed first; terminal-particle -- the broad catch-all for whatever isn't
# claimed by a more specific rule -- is listed last.
#
# Each rule tuple is extended with a quick-check list (or None for the
# terminal-particle catch-all that cannot be pre-filtered). find_cuts() does a
# fast `any(q in line ...)` test before calling the expensive .finditer(); this
# skips ~82% of regex invocations on typical Tibetan commentary prose.
RULES = [
    # quote-close: standard closing formulas for citations.
    ("quote-close", "after",
     re.compile(rf"(?:ཞེས་སོ|ཅེས་སོ|ཞེས་གསུངས་སོ|ཞེས་བཤད་དོ|ཞེས་པའོ|ཅེས་པའོ|ཞེས་བྱ་བའོ){SHAD_CLUSTER}"),
     re.compile(r"ཞེས་སོ|ཅེས་སོ|ཞེས་གསུངས་སོ|ཞེས་བཤད་དོ|ཞེས་པའོ|ཅེས་པའོ|ཞེས་བྱ་བའོ")),
    # quote-open: source-attribution markers (ལས།, གསུངས།) cut AFTER the marker
    # so the quoted passage starts a new block. Direction "after" avoids the
    # valid_cut() rejection that "before" triggers (preceding char is always་ tsheg).
    ("quote-open", "after",
     re.compile(rf"(?:ལས|གསུངས){SHAD_CLUSTER}"),
     re.compile(r"ལས|གསུངས")),
    # enumeration-head: sa-bcad head closing after a number word + suffix.
    # Suffix required (ལས/སྟེ/སུ/དུ/ཡོད/ནས/པོ) to avoid bare number words mid-compound.
    ("enumeration-head", "after",
     re.compile(rf"(?:གཉིས|གསུམ|བཞི|ལྔ|དྲུག|བདུན|བརྒྱད|དགུ|བཅུ)་(?:ལས|སྟེ|སུ|དུ|ཡོད|ནས|པོ){SHAD_CLUSTER}"),
     re.compile(r"གཉིས་|གསུམ་|བཞི་|ལྔ་|དྲུག་|བདུན་|བརྒྱད་|དགུ་|བཅུ་")),
    # ordinal-open: standard section openers དང་པོ་, གཉིས་པ་, གསུམ་པ་ …
    ("ordinal-open", "before",
     re.compile(rf"(?:དང་པོ|གཉིས་པ|གསུམ་པ|བཞི་པ|ལྔ་པ|དྲུག་པ|བདུན་པ|བརྒྱད་པ|དགུ་པ|བཅུ་པ)་"),
     re.compile(r"དང་པོ|གཉིས་པ|གསུམ་པ|བཞི་པ|ལྔ་པ|དྲུག་པ|བདུན་པ|བརྒྱད་པ|དགུ་པ|བཅུ་པ")),
    # objection-close: question/objection final markers ཅེ་ན།, ཞེ་ན།, སྙམ་ན།
    ("objection-close", "after",
     re.compile(rf"(?:ཅེ་ན|ཞེ་ན|སྙམ་ན){SHAD_CLUSTER}"),
     re.compile(r"ཅེ་ན|ཞེ་ན|སྙམ་ན")),
    # objection-open: reply opener འོ་ན་
    ("objection-open", "before",
     re.compile(rf"འོ་ན་"),
     re.compile(r"འོ་ན་")),
    # terminal-particle: sentence-final linking particles. Generic catch-all,
    # listed last on purpose (see note above RULES).
    # Fix 1: .འོ (.འོ) catches བའོ (བའོ), དའོ (དའོ), etc.
    #        (consonants below U+0F60 were missed by the old [འ-ྼ]འོ range).
    # Fix 2: added ག (ག) and ལ (ལ) for གོ and ལོ.
    ("terminal-particle", "after",
     re.compile(rf"(?:.འོ|[ནདསཏརངབམགལ]ོ){SHAD_CLUSTER}"),
     None),  # catch-all — cannot be pre-filtered
]

SEP = "\n\n"
HEADING_RE = re.compile(r"^#{1,6}\s")
FRONTMATTER_RE = re.compile(r"^---\n.*?\n---\n", re.DOTALL)

# --- verse-stanza (ཚིགས་བཅད) detection parameters ---
# scan_segments() peels a run of clause units out as one protected verse stanza
# when 2-4 consecutive units each carry PADA_MIN_SYL..PADA_MAX_SYL tsheg-
# delimited syllables, the counts are uniform across them (max-min <=
# PADA_UNIFORMITY_TOLERANCE), and each ends on a strong (double) shad. Detected
# stanzas are emitted whole — never run through the rule engine or cap_segment,
# never flagged STAGE2_REVIEW, regardless of total length.
#
# TOLERANCE is 2 (not 1) because real quatrains vary slightly across pādas
# (6 vs 8 syllables is attested) and a pāda closing on a single shad makes the
# counter under-count by one tsheg; 2 still discriminates against prose.
PADA_MIN_SYL = 6
PADA_MAX_SYL = 11
PADA_COUNT_RANGE = (2, 4)
PADA_UNIFORMITY_TOLERANCE = 2


def count_syllables(text: str) -> int:
    return text.count(TSHEG) + (1 if text.strip() else 0)


def _is_pada_unit(unit):
    stripped = unit.strip()
    # Real verse padas always end with a strong (double) shad cluster.
    # Handles both "།།" (consecutive) and "། །" (shad-space-shad) which
    # Tibetan OCR and digital sources commonly produce.
    # Outline/list sub-items end with a single shad — requiring double-shad
    # prevents them from being mistaken for verse.
    if not stripped:
        return False
    last = stripped[-1]
    if last == NYIS_SHAD:
        ends_double = True
    elif last == SHAD:
        # Walk backwards past any whitespace to find the preceding shad
        i = len(stripped) - 2
        while i >= 0 and stripped[i] in (" ", "\t", " "):
            i -= 1
        ends_double = i >= 0 and stripped[i] in (SHAD, NYIS_SHAD)
    else:
        ends_double = False
    if not ends_double:
        return False
    return PADA_MIN_SYL <= count_syllables(stripped) <= PADA_MAX_SYL


def _uniform(units):
    syls = [count_syllables(u.strip()) for u in units]
    return len(syls) >= PADA_COUNT_RANGE[0] and max(syls) - min(syls) <= PADA_UNIFORMITY_TOLERANCE


def _format_pada(p):
    p = p.strip()
    # Collapse multiple spaces to one.
    p = re.sub(r" {2,}", " ", p)
    # Remove space before a shad, but ONLY when the character immediately
    # before that space is NOT itself a shad.  This preserves the ། །
    # (shad-space-shad) punctuation sequence while still stripping stray
    # OCR spaces like "word །" → "word།".
    p = re.sub(r"(?<![" + SHAD + NYIS_SHAD + r"]) +([" + SHAD + NYIS_SHAD + r"])", r"\1", p)
    # Ensure a space after ། ། (or any shad) when followed directly by
    # Tibetan content with no separator.
    p = re.sub(r"([" + SHAD + NYIS_SHAD + r"])([^\s" + SHAD + NYIS_SHAD + TSHEG + r"])", r"\1 \2", p)
    return p


def _split_clause_units(text):
    units, last = [], 0
    for m in _SHAD_CLUSTER_RE.finditer(text):
        end = m.end()
        if text[last:end].strip():
            units.append(text[last:end])
        last = end
    if text[last:].strip():
        if units:
            units[-1] = units[-1] + text[last:]
        else:
            units.append(text[last:])
    return units


_QUOTE_FRAME_RE = re.compile(rf"(?:ལས|གསུངས){SHAD_CLUSTER}\s*$")


def _is_leadin(text: str) -> bool:
    if len(_split_clause_units(text)) != 1:
        return False
    return (count_syllables(text.strip()) < PADA_MIN_SYL
            or bool(_QUOTE_FRAME_RE.search(text.strip())))


def scan_segments(para):
    """Return an ordered list of ('verse', [padas]) and ('prose', text)
    segments. Only a run of >=2 uniform padas (a real stanza) is peeled out;
    isolated pada-length clauses are kept flowing with the surrounding prose so
    medium-length prose sentences are never mistaken for one-line verses."""
    units = _split_clause_units(para)
    flags = [_is_pada_unit(u) for u in units]

    # Gap-bridging pass: some texts mark pāda boundaries with a single shad
    # (།) rather than a double shad (། །), producing a False flag that breaks
    # an otherwise valid stanza run. Promote a single-shad unit to pada status
    # when it is sandwiched between two double-shad pada units and its syllable
    # count falls in the pada range. The surrounding double-shad requirement
    # keeps normal prose sentences (which almost always end with single shad)
    # from being mis-promoted.
    n = len(units)
    for i in range(1, n - 1):
        if not flags[i] and flags[i - 1] and flags[i + 1]:
            stripped = units[i].strip()
            if PADA_MIN_SYL <= count_syllables(stripped) <= PADA_MAX_SYL:
                flags[i] = True
    out = []
    pending = []  # prose units awaiting flush

    def flush():
        if pending:
            out.append(("prose", "".join(pending)))
            pending.clear()

    i, n = 0, len(units)
    while i < n:
        if flags[i]:
            j = i
            while j < n and flags[j]:
                j += 1
            run = units[i:j]
            k = 0
            while k < len(run):
                chunk = None
                for size in (4, 3, 2):  # prefer a full quatrain
                    cand = run[k:k + size]
                    if len(cand) == size and _uniform(cand):
                        chunk = cand
                        break
                if chunk is not None:
                    flush()
                    out.append(("verse", [_format_pada(u) for u in chunk]))
                    k += len(chunk)
                else:
                    pending.append(run[k])  # lone pada-length clause -> prose
                    k += 1
            i = j
        else:
            pending.append(units[i])
            i += 1
    flush()
    return out


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


def find_cuts(line: str, structural: bool = False):
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
    for name, kind, pat, quick in RULES:
        # Quick pre-filter: one compiled search() call (C-level) is cheaper
        # than running the full finditer() on lines that cannot possibly match.
        # Profiling showed this eliminates ~82% of finditer calls on typical
        # Tibetan commentary prose with negligible overhead.
        if quick is not None and not quick.search(line):
            continue
        for m in pat.finditer(line):
            if structural:
                # structural mode: only major boundaries -- strong (double-shad)
                # sentence ends, section heads, and citation frames. Single-shad
                # clause ends and objection markers do NOT force a break.
                if name in ("objection-close", "objection-open", "enumeration-head"):
                    continue
                if name == "terminal-particle" and (
                        m.group(0).count(SHAD) + m.group(0).count(NYIS_SHAD)) < 2:
                    continue
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
    rstripped_len = len(piece.rstrip())
    for m in _SHAD_CLUSTER_RE.finditer(piece):
        end = m.end()
        if 0 < end < rstripped_len:
            if strong_only:
                grp = m.group(0)
                if grp.count(SHAD) + grp.count(NYIS_SHAD) < 2:
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
    if max_syllables <= 0 or count_syllables(piece) <= max_syllables:
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


def segment_line(line: str, max_syllables: int, structural: bool = False):
    positions, starts, ends, candidates = find_cuts(line, structural)
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
            if max_syllables > 0 and syl > max_syllables:
                # Distinguish "no internal shad to split on at all" (needs a
                # full hand-read to find a break) from "had shads, capping
                # still couldn't fit everything under budget".
                flag = ("STAGE2_REVIEW" if re.search(SHAD_CLUSTER, sub)
                        else "STAGE2_REVIEW:NO_SHAD_FOUND")
            else:
                flag = ""
            report.append({"trigger": trigger, "syllables": syl,
                           "flag": flag, "preview": preview})
    if max_syllables > 0:
        segments, report = merge_short_segments(segments, report, max_syllables)
    for c in candidates:
        # Weak-context match: not auto-cut, just surfaced for human judgement.
        report.append({"trigger": c["name"] + "-candidate", "syllables": 0,
                       "flag": "STAGE2_REVIEW", "preview": c["preview"]})
    return segments, report


def process(text: str, max_syllables: int, structural: bool = False):
    out_parts = []
    report = []
    fm = FRONTMATTER_RE.match(text)
    if fm:
        out_parts.append(fm.group(0).rstrip("\n"))
        body = text[fm.end():]
    else:
        body = text
    blocks = []  # list of (is_verse, text)
    for para in re.split(r"\n\s*\n", body):
        if not para.strip():
            continue
        if HEADING_RE.match(para.strip()):
            blocks.append((False, para.strip()))
            continue
        for kind, payload in scan_segments(para):
            if kind == "verse":
                block = "\n".join(payload)
                blocks.append((True, block))
                preview = block[:80].replace("\t", " ").replace("\n", "↵")
                report.append({"trigger": "verse-stanza",
                               "syllables": count_syllables(block),
                               "flag": "", "preview": preview})
            else:
                if not payload.strip():
                    continue
                segments, rows = segment_line(payload, max_syllables, structural)
                for seg in segments:
                    seg = seg.strip()
                    if structural:
                        seg = re.sub(r"([" + SHAD + NYIS_SHAD + r"])\s+([" + SHAD + NYIS_SHAD + r"])", r"\1\2", seg)
                    blocks.append((False, seg))
                report.extend(rows)
    # Citation-marker split (structural mode only).
    # After Stage 0 joins source lines with spaces, a citation marker that was
    # on its own source line arrives as "[prose] [source]ལས།" (with a space
    # marking the original line boundary). Split it off into its own block so
    # the source reference, the quoted passage, and the closing formula each
    # occupy separate blocks.  The regex requires whitespace before the marker
    # so that in-sentence grammatical ལས། (no preceding space) is never split.
    if structural:
        # Split citation markers from the prose block they landed in.
        # Stage 0 joined source lines with spaces, so a citation marker that
        # was its own source segment arrives as "...prose [marker]las/sungs."
        # We detect it by: last-space exists, everything after the last space
        # has no further spaces, and that tail ends with las/sungs + a shad.
        # Pure ASCII / Unicode-escape constants avoid encoding issues.
        _LAS   = "\u0f63\u0f66"   # las (unicode escapes - no Tibetan in source)
        _SUNGS = "\u0f42\u0f66\u0f74\u0f44\u0f66"  # sungs
        _SHADS = SHAD + NYIS_SHAD
        split_blocks = []
        for is_verse, txt in blocks:
            if not is_verse:
                # Prose block: citation marker may trail prose after a space.
                stripped = txt.strip()
                last_sp = stripped.rfind(" ")
                if last_sp > 0:
                    tail = stripped[last_sp + 1:]
                    core = tail.rstrip(_SHADS)
                    if (" " not in tail
                            and len(core) < len(tail)   # at least one shad
                            and (core.endswith(_LAS) or core.endswith(_SUNGS))):
                        split_blocks.append((False, stripped[:last_sp].strip()))
                        split_blocks.append((False, tail))
                        continue
            elif is_verse:
                # Verse block: citation marker may be its first line because
                # scan_segments sees pada-length syllables and groups it into
                # the stanza. Peel it off as a separate prose block.
                lines = txt.split("\n")
                if len(lines) >= 2:
                    first = lines[0].strip()
                    core = first.rstrip(_SHADS)
                    if (len(core) < len(first)  # ends in a shad
                            and (core.endswith(_LAS) or core.endswith(_SUNGS))):
                        split_blocks.append((False, first))
                        split_blocks.append((True, "\n".join(lines[1:])))
                        continue
            split_blocks.append((is_verse, txt))
        blocks = split_blocks

    # Closer attachment (structural mode only).
    # Closing formulas like zhe-s-pa-ltar-ro (as it is said) end with double-shad
    # and are cut into their own block by the terminal-particle rule. They should
    # be re-joined to the preceding block with a space.
    # Detection: no internal space (single source line), starts with zhe-s or
    # ce-s, and short (<=10 syllables) -- avoids prose that begins with zhe-s.
    if structural:
        _ZHE = "\u0f5e\u0f7a\u0f66\u0f0b"   # zhe-s-tsheg
        _CE  = "\u0f45\u0f7a\u0f66\u0f0b"   # ce-s-tsheg
        CLOSER_MAX_SYL = 10
        merged = []
        for is_verse, txt in blocks:
            stripped = txt.strip()
            if (not is_verse
                    and merged
                    and not merged[-1][0]   # attach only to prose, not verse
                    and " " not in stripped
                    and (stripped.startswith(_ZHE) or stripped.startswith(_CE))
                    and count_syllables(stripped) <= CLOSER_MAX_SYL):
                prev_verse, prev_txt = merged[-1]
                merged[-1] = (prev_verse, prev_txt.rstrip() + " " + stripped)
            else:
                merged.append((is_verse, txt))
        blocks = merged

    # lead-in attachment: a lone invocation / source-frame line immediately
    # before a stanza becomes that stanza block's first line (format-commentary
    # §3). Done here, after prose has been split into individual blocks.
    # Skipped in structural mode — citation markers, verses, and closers each
    # keep their own block there.
    i = 0
    while i < len(blocks):
        is_verse, txt = blocks[i]
        if (not structural
                and not is_verse and i + 1 < len(blocks)
                and blocks[i + 1][0] and _is_leadin(txt)):
            out_parts.append(_format_pada(txt) + "\n" + blocks[i + 1][1])
            i += 2
        else:
            out_parts.append(txt)
            i += 1
    return SEP.join(out_parts) + "\n", report


# Translate table that removes all Unicode whitespace in one pass —
# faster than re.sub(r"\s+", "", s) on large Tibetan files.
_WS_TABLE = str.maketrans("", "", "".join(chr(c) for c in (
    0x20, 0x09, 0x0A, 0x0D, 0x0C, 0x0B,  # ASCII whitespace
    0xA0,         # NO-BREAK SPACE
    0x1680,       # OGHAM SPACE MARK
    0x2000, 0x2001, 0x2002, 0x2003, 0x2004,  # EN/EM/THREE-PER-EM etc.
    0x2005, 0x2006, 0x2007, 0x2008, 0x2009, 0x200A,  # FOUR-PER-EM .. HAIR SPACE
    0x2028, 0x2029,  # LINE/PARAGRAPH SEPARATOR
    0x202F, 0x205F,  # NARROW NO-BREAK, MEDIUM MATHEMATICAL
    0x3000,         # IDEOGRAPHIC SPACE
)))


def _squeeze(s: str) -> str:
    return s.translate(_WS_TABLE)


def assert_no_loss(original: str, segmented: str):
    if _squeeze(original) != _squeeze(segmented):
        sys.exit("ABORT: segmentation altered non-whitespace content. No file written.")


def main(argv):
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("input")
    ap.add_argument("output")
    ap.add_argument("--report", help="write a TSV segmentation report here")
    ap.add_argument("--max-syllables", type=int, default=50)
    ap.add_argument("--structural", action="store_true",
                    help="prose breaks only at strong (double-shad) sentence "
                         "ends, section heads, and citation frames; verses one "
                         "pada per line; implies no syllable cap. Best match for "
                         "the canonical block layout.")
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args(argv[1:])
    text = unicodedata.normalize("NFC", Path(args.input).read_text(encoding="utf-8"))
    structural = args.structural
    max_syllables = 0 if structural else args.max_syllables
    segmented, report = process(text, max_syllables, structural)
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
