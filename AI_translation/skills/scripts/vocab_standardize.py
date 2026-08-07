#!/usr/bin/env python3
"""
vocab_standardize.py
=====================

Step 6 of the AI_translation pipeline ("vocab standardization with the termbase"):
audit -- and optionally fix -- an already-written translation's word choices
against its locked termbase.

This is a *consistency* check, not a translation-quality check: it does not judge
whether a rendering is good English, only whether it matches the vocabulary that
was already locked in the termbase for that source word.

Ground truth chain (paths per AI_translation/skills/requirements.md §5):
  - tibetan-<language>-termbase-<level>.md
        LOCKED: word -> {sense_tag: term}, exactly one term per sense, no " / " alternates.
  - keywords-by-reference-tibetan-<language>-<level>.md
        ACTUAL USAGE: "[segment_id] word=used_term, word=used_term, ..." -- what the
        translation actually rendered each source word as, per segment.
  - <text>-<language>-<level>.md
        the translation file itself (only touched in --apply mode).

For every (word, used_term) pair recorded per segment, this script checks whether
used_term matches (exactly, or as a plain inflection of) any of the termbase's
locked sense-terms for that word.

Severity:
  - UNAMBIGUOUS DRIFT: the word has exactly one sense in the termbase, the used
    term does not match it even loosely, so there is exactly one correct fix.
    Eligible for --apply.
  - AMBIGUOUS DRIFT: the word has 2+ senses in the termbase. Reported only --
    picking the right sense requires reading the verse, so this is never
    auto-applied.
  - INFLECTION (not drift): the used term is a plausible inflected form of a
    locked term (e.g. "attained" for locked "attain", "cultivating" for locked
    "cultivate"). Listed separately, low priority, never auto-applied, and not
    counted as a script "problem" -- inflection is normal, correct usage.
  - UNTRACKED: the source word has no termbase entry at all. Informational only.

Known caveat: keywords-by-reference-*.md is a *snapshot* of an earlier extraction
pass. If the translation file has been hand-edited since (e.g. by a fact-check
pass), entries for the touched verses will be stale until keyword-equivalence-mapper
is re-run. This script does not re-run it -- it audits what the snapshot says,
and --apply verifies the literal string is still present before touching anything,
so staleness causes missed fixes, never wrong ones.

Usage:
    python3 vocab_standardize.py \\
        --termbase AI_translation/english/tibetan-english-termbase-plain.md \\
        --keywords AI_translation/english/keywords-by-reference-tibetan-english-plain.md \\
        --translation AI_translation/english/bca-english-plain.md \\
        --chapters 1,2,3,4 \\
        --report /tmp/vocab-drift-report.md
        [--apply]   # also rewrite UNAMBIGUOUS DRIFT directly into --translation.
                    # Only applies a fix when the used_term occurs exactly once in
                    # that verse's block, the replacement wouldn't duplicate an
                    # adjacent word, and the locked term's coarse part-of-speech
                    # doesn't clash with the used term's. Everything else is
                    # skipped and reported with a specific reason -- see
                    # apply_fixes() for what changed after the 2026-08-07
                    # corruption incident and revert.
"""
import argparse
import difflib
import re
from collections import defaultdict
from pathlib import Path


# ---------------------------------------------------------------------------
# Termbase parsing:  word: {sense_tag: term; sense_tag2: term2}
# ---------------------------------------------------------------------------

def parse_termbase(path):
    """Return {word: [(sense_tag, term), ...]} preserving declaration order."""
    termbase = {}
    for lineno, line in enumerate(Path(path).read_text(encoding="utf-8").splitlines(), 1):
        line = line.rstrip()
        if not line.strip():
            continue
        m = re.match(r"^(.*?):\s*\{(.*)\}\s*$", line)
        if not m:
            continue
        word, body = m.group(1).strip(), m.group(2)
        senses = []
        for clause in body.split(";"):
            clause = clause.strip()
            if not clause or ":" not in clause:
                continue
            sense_tag, term = clause.rsplit(":", 1)
            term = term.strip()
            if " / " in term:
                print(f"WARNING termbase.md:{lineno}: uncollapsed alternate in locked term for {word!r}: {term!r}")
            senses.append((sense_tag.strip(), term))
        if senses:
            termbase[word] = senses
    return termbase


# ---------------------------------------------------------------------------
# keywords-by-reference parsing: [id] word=term, word=term, bareword, word=term
# ---------------------------------------------------------------------------

LINE_RE = re.compile(r"^\[([^\]]+)\]\s*(.*)$")


def parse_keywords_by_reference(path):
    """Return {segment_id: [(word, used_term), ...]}.

    Handles the chained-key pattern this file uses when several source word-forms
    share one rendering: "wordA, wordB, wordC=value" means wordA, wordB and wordC
    all map to value. A run of comma-separated tokens without "=" is held pending
    until a token with "=" is reached, then the value is distributed back over the
    whole run.
    """
    entries = {}
    for lineno, line in enumerate(Path(path).read_text(encoding="utf-8").splitlines(), 1):
        line = line.rstrip()
        if not line.strip():
            continue
        m = LINE_RE.match(line)
        if not m:
            continue
        seg_id, body = m.group(1), m.group(2)
        pairs = []
        pending = []
        for token in body.split(","):
            token = token.strip()
            if not token:
                continue
            if "=" in token:
                key, val = token.split("=", 1)
                key, val = key.strip(), val.strip()
                for pk in pending:
                    pairs.append((pk, val))
                pairs.append((key, val))
                pending = []
            else:
                pending.append(token)
        if pending:
            print(f"WARNING keywords-by-reference:{lineno} [{seg_id}]: key(s) with no value, dropped: {pending}")
        entries[seg_id] = pairs
    return entries


# ---------------------------------------------------------------------------
# Drift classification
# ---------------------------------------------------------------------------

def looks_inflected(a, b):
    """True if a and b are plausibly the same word under English inflection
    (attain/attained/attains/attaining, bow/bows/bowing, cultivate/cultivating)."""
    a, b = a.lower().strip(), b.lower().strip()
    if a == b:
        return True
    if len(a) >= 3 and len(b) >= 3 and (a.startswith(b) or b.startswith(a)):
        return True
    return difflib.SequenceMatcher(None, a, b).ratio() >= 0.72


def classify(word, used_term, termbase):
    """Return (status, detail) where status is one of:
    OK, INFLECTION, UNAMBIGUOUS_DRIFT, AMBIGUOUS_DRIFT, UNTRACKED."""
    senses = termbase.get(word)
    if senses is None:
        return "UNTRACKED", None
    locked_terms = [t for _, t in senses]
    for t in locked_terms:
        if used_term.lower().strip() == t.lower().strip():
            return "OK", t
    for t in locked_terms:
        if looks_inflected(used_term, t):
            return "INFLECTION", t
    if len(senses) == 1:
        return "UNAMBIGUOUS_DRIFT", locked_terms[0]
    return "AMBIGUOUS_DRIFT", locked_terms


# ---------------------------------------------------------------------------
# Translation-file block parsing (for --apply), mirrors rails_fact_check_extract.py
# ---------------------------------------------------------------------------

ID_LINE_RE = re.compile(r"^(.*?)\s*\^([a-zA-Z0-9]+-[a-zA-Z0-9]+|[a-zA-Z0-9]+)\s*$")


def find_verse_blocks(content):
    """Return {verse_id: (start_offset, end_offset)} spans (character offsets
    into content) for every ^id-bearing block, id anywhere in the block (this
    file mixes id-at-start and id-at-end conventions across chapters)."""
    blocks = {}
    pos = 0
    # Capturing the separator keeps it in the split result; content chunks are
    # at even indices (0, 2, 4, ...), separators at odd indices.
    parts = re.split(r"(\r?\n\s*\r?\n)", content)
    for i, chunk in enumerate(parts):
        chunk_start = pos
        pos += len(chunk)
        if i % 2 == 1:
            continue  # this chunk is a blank-line separator, not content
        if not chunk.strip():
            continue
        vid = None
        for line in chunk.splitlines():
            m = ID_LINE_RE.match(line.strip())
            if m:
                candidate = m.group(2)
                if "-" in candidate and candidate.split("-")[1] == "0":
                    continue  # heading marker, not a verse
                vid = candidate
        if vid:
            blocks[vid] = (chunk_start, chunk_start + len(chunk))
    return blocks



# ---------------------------------------------------------------------------
# Safety checks for --apply
#
# The first version of this function trusted "the literal string is still
# present in the block" as sufficient grounds to replace it. It isn't: a
# 2026-08-07 --apply run using that logic corrupted the translation with
# duplicated words ("kinds kinds of uncultivated crops"), part-of-speech
# breaks ("what is benefit in this life" for "beneficial"), and wrong-instance
# substitutions, and had to be reverted from backup (see the incident note in
# vocab-standardization-report.md). Every check below exists because it
# caught a real failure mode from that run.
# ---------------------------------------------------------------------------

WORD_RE = re.compile(r"[A-Za-z']+")


def _last_word(phrase):
    words = WORD_RE.findall(phrase)
    return words[-1] if words else phrase


def _first_word(phrase):
    words = WORD_RE.findall(phrase)
    return words[0] if words else phrase


def _pos_hint(word):
    """Coarse part-of-speech guess from suffix shape. Not linguistically
    rigorous -- just enough to catch gross mismatches like adjective-for-noun
    ('beneficial' -> 'benefit') before they're written into the text.
    Returns 'base' (no confident signal) rather than guessing wrong."""
    w = word.lower()
    if w.endswith("ing") and len(w) > 4:
        return "gerund"
    if w.endswith("ly"):
        return "adverb"
    if re.search(r"(tion|sion|ment|ness|ity|ance|ence)$", w):
        return "noun-abstract"
    if re.search(r"(ful|ive|ous|ical|able|ible)$", w):
        return "adjective"
    if w.endswith("ed") and len(w) > 4:
        return "past"
    if w.endswith("s") and not w.endswith("ss") and len(w) > 3:
        return "plural-or-3s"
    return "base"


def _pos_compatible(used_term, locked_term):
    """True unless both terms give a confident, *different* POS hint.
    'base' on either side means no signal -- don't block on it."""
    a, b = _pos_hint(_last_word(used_term)), _pos_hint(_last_word(locked_term))
    if a == "base" or b == "base":
        return True
    return a == b


def _word_before(text, idx):
    m = re.search(r"([A-Za-z']+)\s*$", text[:idx])
    return m.group(1) if m else None


def _word_after(text, idx):
    m = re.match(r"\s*([A-Za-z']+)", text[idx:])
    return m.group(1) if m else None


def apply_fixes(translation_path, fixes_by_segment):
    """fixes_by_segment: {segment_id: [(used_term, locked_term), ...]}.
    Returns (new_content, applied_log, skipped_log).

    Only applies a fix when ALL of these hold; anything else is skipped with
    a specific reason rather than forced through:
      1. used_term occurs exactly once (whole word/phrase) in the verse's
         block -- if it occurs more than once, we can't tell which instance
         the keywords-by-reference entry was actually recorded for.
      2. The replacement would not create an immediately duplicated word on
         either side of the edit (e.g. 'various kinds' -> 'kinds kinds').
      3. locked_term's coarse part-of-speech hint doesn't clash with
         used_term's (catches e.g. adjective 'beneficial' -> noun 'benefit').
      4. The edit's span doesn't overlap another edit already accepted in the
         same block (only possible with multi-word phrases).
    """
    raw = Path(translation_path).read_bytes()
    content = raw.decode("utf-8")
    blocks = find_verse_blocks(content)
    applied, skipped = [], []

    # Apply in reverse offset order so earlier edits don't shift later offsets.
    edits = []  # (start, end, seg_id, used_term, locked_term)
    for seg_id, fixes in fixes_by_segment.items():
        span = blocks.get(seg_id)
        if span is None:
            for used_term, locked_term in fixes:
                skipped.append((seg_id, used_term, locked_term, "verse block not found"))
            continue
        start, end = span
        block_text = content[start:end]
        accepted_spans = []  # local (start, end) offsets already claimed in this block

        for used_term, locked_term in fixes:
            wb = re.compile(r"\b" + re.escape(used_term) + r"\b")
            matches = list(wb.finditer(block_text))

            if not matches:
                skipped.append((seg_id, used_term, locked_term,
                                 "literal string not found in current block (stale keywords-by-reference entry?)"))
                continue
            if len(matches) > 1:
                skipped.append((seg_id, used_term, locked_term,
                                 f"'{used_term}' occurs {len(matches)} times in this block -- ambiguous which instance to fix; needs manual review"))
                continue

            m = matches[0]

            if any(not (m.end() <= s or m.start() >= e) for s, e in accepted_spans):
                skipped.append((seg_id, used_term, locked_term,
                                 "edit span overlaps another fix already accepted in this block; needs manual review"))
                continue

            before = _word_before(block_text, m.start())
            after = _word_after(block_text, m.end())
            if before and before.lower() == _first_word(locked_term).lower():
                skipped.append((seg_id, used_term, locked_term,
                                 f"would duplicate the preceding word ('{before} {locked_term}'); needs manual review"))
                continue
            if after and after.lower() == _last_word(locked_term).lower():
                skipped.append((seg_id, used_term, locked_term,
                                 f"would duplicate the following word ('{locked_term} {after}'); needs manual review"))
                continue

            if not _pos_compatible(used_term, locked_term):
                skipped.append((seg_id, used_term, locked_term,
                                 f"possible part-of-speech mismatch ('{used_term}' vs '{locked_term}'); needs manual review"))
                continue

            accepted_spans.append((m.start(), m.end()))
            edits.append((start + m.start(), start + m.end(), seg_id, used_term, locked_term))

    edits.sort(key=lambda e: e[0], reverse=True)
    for s, e, seg_id, used_term, locked_term in edits:
        content = content[:s] + locked_term + content[e:]
        applied.append((seg_id, used_term, locked_term))

    return content, applied, skipped


# ---------------------------------------------------------------------------
# Report
# ---------------------------------------------------------------------------

def seg_sort_key(v):
    """Sort segment/chapter tokens naturally, numeric parts as numbers, mixed
    id shapes (1-1, b-1, 1-a, 0) all comparable to each other."""
    return [(0, int(x)) if x.isdigit() else (1, x) for x in re.split(r"-", v)]


def write_report(path, termbase_path, keywords_path, translation_path, chapters, results, applied=None, skipped=None):
    lines = []
    lines.append("---")
    lines.append("title: Vocabulary Standardization Report")
    lines.append(f"termbase: {termbase_path}")
    lines.append(f"keywords_by_reference: {keywords_path}")
    lines.append(f"translation: {translation_path}")
    lines.append(f"scope: {'all chapters' if not chapters else 'chapters ' + ','.join(sorted(chapters, key=seg_sort_key))}")
    lines.append("status: draft")
    lines.append("---")
    lines.append("")
    lines.append("# Vocabulary Standardization Report")
    lines.append("")
    lines.append("Checks every recorded (source word, used English term) pair against the locked")
    lines.append("termbase. UNAMBIGUOUS DRIFT has exactly one correct fix; AMBIGUOUS DRIFT needs a")
    lines.append("human to pick the right sense; INFLECTION is normal usage, not an error.")
    lines.append("")

    counts = defaultdict(int)
    by_word_unambiguous = defaultdict(list)
    by_word_ambiguous = defaultdict(list)

    for seg_id, word, used_term, status, detail in results:
        counts[status] += 1
        if status == "UNAMBIGUOUS_DRIFT":
            by_word_unambiguous[word].append((seg_id, used_term, detail))
        elif status == "AMBIGUOUS_DRIFT":
            by_word_ambiguous[word].append((seg_id, used_term, detail))

    lines.append("## Summary")
    lines.append("")
    lines.append("| Status | Count |")
    lines.append("|---|---|")
    for status in ("OK", "INFLECTION", "UNAMBIGUOUS_DRIFT", "AMBIGUOUS_DRIFT", "UNTRACKED"):
        lines.append(f"| {status} | {counts.get(status, 0)} |")
    lines.append("")

    lines.append("## Unambiguous drift (one locked term, translation used something else)")
    lines.append("")
    if not by_word_unambiguous:
        lines.append("None found.")
    else:
        lines.append("| Word | Locked term | Used instead | Segments |")
        lines.append("|---|---|---|---|")
        for word in sorted(by_word_unambiguous):
            entries = by_word_unambiguous[word]
            locked = entries[0][2]
            used_variants = sorted({e[1] for e in entries})
            segs = ", ".join(sorted({e[0] for e in entries}, key=seg_sort_key))
            lines.append(f"| {word} | {locked} | {', '.join(used_variants)} | {segs} |")
    lines.append("")

    lines.append("## Ambiguous drift (2+ locked senses; a human must pick the right one)")
    lines.append("")
    if not by_word_ambiguous:
        lines.append("None found.")
    else:
        lines.append("| Word | Locked senses | Used instead | Segments |")
        lines.append("|---|---|---|---|")
        for word in sorted(by_word_ambiguous):
            entries = by_word_ambiguous[word]
            locked = "; ".join(entries[0][2])
            used_variants = sorted({e[1] for e in entries})
            segs = ", ".join(sorted({e[0] for e in entries}, key=seg_sort_key))
            lines.append(f"| {word} | {locked} | {', '.join(used_variants)} | {segs} |")
    lines.append("")

    if applied is not None:
        lines.append("## Fixes applied")
        lines.append("")
        if not applied:
            lines.append("None.")
        else:
            lines.append("| Segment | Used | Fixed to |")
            lines.append("|---|---|---|")
            for seg_id, used_term, locked_term in applied:
                lines.append(f"| {seg_id} | {used_term} | {locked_term} |")
        lines.append("")
        lines.append("## Fixes skipped (needs manual attention)")
        lines.append("")
        if not skipped:
            lines.append("None.")
        else:
            lines.append("| Segment | Used | Locked | Reason |")
            lines.append("|---|---|---|---|")
            for seg_id, used_term, locked_term, reason in skipped:
                lines.append(f"| {seg_id} | {used_term} | {locked_term} | {reason} |")
        lines.append("")

    Path(path).write_text("\n".join(lines), encoding="utf-8")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--termbase", required=True)
    ap.add_argument("--keywords", required=True, help="keywords-by-reference-*.md")
    ap.add_argument("--translation", required=True)
    ap.add_argument("--chapters", default=None, help="Comma-separated chapter numbers to include (default: all)")
    ap.add_argument("--report", required=True)
    ap.add_argument("--apply", action="store_true", help="Rewrite UNAMBIGUOUS DRIFT directly into --translation. Safety-checked: skips (with a reason) any fix that isn't a single unambiguous occurrence, would duplicate an adjacent word, or looks like a part-of-speech mismatch. Never touches ambiguous-sense words.")
    args = ap.parse_args()

    chapters = set(args.chapters.split(",")) if args.chapters else None

    termbase = parse_termbase(args.termbase)
    keywords = parse_keywords_by_reference(args.keywords)

    def in_scope(seg_id):
        if not chapters:
            return True
        first = seg_id.split("-")[0]
        return first in chapters

    results = []
    fixes_by_segment = defaultdict(list)
    for seg_id, pairs in keywords.items():
        if not in_scope(seg_id):
            continue
        for word, used_term in pairs:
            status, detail = classify(word, used_term, termbase)
            results.append((seg_id, word, used_term, status, detail))
            if status == "UNAMBIGUOUS_DRIFT":
                fixes_by_segment[seg_id].append((used_term, detail))

    applied, skipped = None, None
    if args.apply:
        new_content, applied, skipped = apply_fixes(args.translation, fixes_by_segment)
        Path(args.translation).write_text(new_content, encoding="utf-8", newline="")
        print(f"Applied {len(applied)} fix(es); skipped {len(skipped)} (see report).")

    write_report(args.report, args.termbase, args.keywords, args.translation, chapters, results, applied, skipped)

    counts = defaultdict(int)
    for *_, status, _d in results:
        counts[status] += 1
    print(f"Checked {len(results)} (word, used_term) pairs across {len(keywords)} segments.")
    for status in ("OK", "INFLECTION", "UNAMBIGUOUS_DRIFT", "AMBIGUOUS_DRIFT", "UNTRACKED"):
        print(f"  {status}: {counts.get(status, 0)}")
    print(f"Report written to {args.report}")


if __name__ == "__main__":
    main()
