#!/usr/bin/env python3
"""
qc_check_tree.py — deterministic QC checker for a ས་བཅད (sa bcad) decimal TOC tree.

This is the NON-LLM half of the toc-tree-extraction skill, lifted verbatim from the
original `extract_toc_tree.py`. Claude does the four inference passes; this script does
the mechanical checking so the numbering/attestation logic is identical every run and
never has to be redone by hand.

Two kinds of checks:
  (a) internal consistency — indentation, decimal-vs-Tibetan-ordinal agreement,
      duplicate decimals, and gap-free sibling sequences.
  (b) attestation — every node's TITLE and leading ORDINAL must correspond to an actual
      string in the candidates + enumerations corpus. This catches hallucinations:
      invented sections, reworded-away titles, or ordinals the source never attached.

--------------------------------------------------------------------------------
Usage
--------------------------------------------------------------------------------
    # check a tree against the candidates+enumerations corpus, print issues:
    python qc_check_tree.py TREE.md --corpus CANDIDATES.md ENUMERATIONS.md

    # internal-consistency checks only (no attestation):
    python qc_check_tree.py TREE.md

    # write a markdown QC report instead of printing:
    python qc_check_tree.py TREE.md --corpus CANDIDATES.md --out QC-REPORT.md

Exit code is the number of issues found (0 = clean), so it can gate a loop.
"""

import argparse
import re
import sys
from pathlib import Path

# ------------------------------------------------------------------------------
# Tibetan ordinals -> integer, longest forms first so e.g. བཅུ་གཅིག་པ matches before བཅུ་པ.
# ------------------------------------------------------------------------------
_TIB_ORDINALS = [
    ("བཅུ་གསུམ་པ", 13), ("བཅུ་གཉིས་པ", 12), ("བཅུ་གཅིག་པ", 11),
    ("དང་པོ", 1), ("གཉིས་པ", 2), ("གསུམ་པ", 3), ("བཞི་པ", 4), ("ལྔ་པ", 5),
    ("དྲུག་པ", 6), ("བདུན་པ", 7), ("བརྒྱད་པ", 8), ("དགུ་པ", 9), ("བཅུ་པ", 10),
]
_TREE_LINE_RE = re.compile(
    r"^(?P<indent>\s*)\*\s+(?P<dec>\d+(?:\.\d+)*)\.?\s+"
    r"(?P<text>.*?)(?:\s*\^toc-[\d-]+)?\s*$"
)

# Min fraction of a title's Tibetan-syllable bigrams that must be found in the
# candidates+enumerations corpus before we accept a reworded (non-verbatim) title
# as "attested". Below this, the title is flagged as a possible hallucination.
TITLE_COVERAGE_MIN = 0.5

# Tsheg (syllable separator) and the shad / danda family we strip when canonicalising.
_TSHEG = "་"
_SHAD_CHARS = "།༎༏༐༑༒༔༺༻༼༽༄༅"
# Trailing grammatical particles a tree title may carry that the source string need
# not — stripped (once) only for the purpose of fuzzy matching, never from the tree.
_TRAILING_PARTICLES = ["ནི", "ལ", "འོ", "པོ", "པ", "སྟེ", "ཏེ", "དང", "གོ", "ངོ", "ནོ", "བོ", "མོ"]


def _leading_tibetan_ordinal_word(text: str):
    """Return (word, int) for the leading Tibetan ordinal, or (None, None)."""
    t = text.lstrip(" *#\t")
    for word, num in _TIB_ORDINALS:
        if t.startswith(word):
            return word, num
    return None, None


# Sentinel marking a shad / line boundary in canonical form (a place where one
# title cannot continue into the next). Kept so the ordinal check only credits
# WHOLE-title occurrences, never a title that is merely the prefix of a longer one.
_BOUND = "§"
_SHAD_OR_NEWLINE_RE = "[" + _SHAD_CHARS + "\r\n]+"
_TSHEG_BOUND_CLASS = "[" + _TSHEG + _BOUND + "]"


def _canon(s: str) -> str:
    """Canonical form for robust Tibetan substring matching.

    Removes wiki-link wrappers and block IDs and all whitespace, KEEPS the tsheg
    (་) as a syllable separator, and REPLACES every shad/danda (line/clause
    boundary) with a single sentinel `§`. Matching is then insensitive to spacing
    while still knowing where one title stops and the next begins.
    """
    if not s:
        return ""
    # [[#^id|display]] / [[file#^id|display]] -> display
    s = re.sub(r"\[\[[^\]|]*\|([^\]]*)\]\]", r"\1", s)
    s = re.sub(r"\[\[([^\]]*)\]\]", r"\1", s)
    # trailing / inline block IDs
    s = re.sub(r"\^[\w\-]+", "", s)
    # shad/danda family and newlines become a boundary sentinel
    s = re.sub(_SHAD_OR_NEWLINE_RE, _BOUND, s)
    # drop remaining whitespace; keep tsheg + letters/digits + sentinel
    s = re.sub(r"[ \t]+", "", s)
    # collapse runs of tsheg / sentinels; drop tsheg adjacent to a sentinel
    s = re.sub(_TSHEG + "+", _TSHEG, s)
    s = re.sub(f"{_TSHEG}*{_BOUND}+{_TSHEG}*", _BOUND, s)
    return s.strip(_TSHEG + _BOUND)


def _strip_leading_ordinal(text: str) -> str:
    """Return the title text with its leading Tibetan ordinal word removed."""
    word, _ = _leading_tibetan_ordinal_word(text)
    if not word:
        return text.strip()
    t = text.lstrip(" *#\t")
    t = t[len(word):]
    return t.lstrip(_TSHEG + " ")


def _strip_trailing_particle(canon_topic: str) -> str:
    """Strip one trailing grammatical particle (for fuzzy matching only)."""
    for p in _TRAILING_PARTICLES:
        if canon_topic.endswith(_TSHEG + p) or canon_topic == p:
            return canon_topic[: -len(p)].rstrip(_TSHEG)
    return canon_topic


def _title_bigram_coverage(topic_canon: str, corpus_canon: str) -> float:
    """Fraction of the topic's syllables covered by a contiguous bigram present in
    the corpus. Tolerates a legitimately inserted qualifier while scoring an
    invented title near zero."""
    sylls = [x for x in topic_canon.split(_TSHEG) if x]
    if not sylls:
        return 0.0
    if len(sylls) == 1:
        return 1.0 if sylls[0] in corpus_canon else 0.0
    covered = set()
    for i in range(len(sylls) - 1):
        if (sylls[i] + _TSHEG + sylls[i + 1]) in corpus_canon:
            covered.add(i)
            covered.add(i + 1)
    return len(covered) / len(sylls)


def _title_boundary_after(corpus_canon: str, j: int) -> bool:
    """True if position `j` (just past a title occurrence) is a legitimate title end:
    end-of-corpus, a shad boundary, or a trailing grammatical particle."""
    if j >= len(corpus_canon):
        return True
    if corpus_canon[j] == _BOUND:
        return True
    if corpus_canon[j] == _TSHEG:
        rest = corpus_canon[j + 1:]
        nxt = re.split(_TSHEG_BOUND_CLASS, rest, maxsplit=1)[0]
        return nxt in _TRAILING_PARTICLES
    return False


def _observed_ordinals_before(topic_canon: str, corpus_canon: str):
    """Return the set of ordinal integers the source actually attaches to this
    WHOLE title (header-position occurrences only). Empty set => never directly
    ordinal-led, so we do NOT flag (ordinal may come from a parent announcement)."""
    observed = set()
    if not topic_canon:
        return observed
    L = len(topic_canon)
    start = 0
    while True:
        i = corpus_canon.find(topic_canon, start)
        if i == -1:
            break
        start = i + 1
        if not _title_boundary_after(corpus_canon, i + L):
            continue
        before = corpus_canon[:i].rstrip(_TSHEG)
        for word, num in _TIB_ORDINALS:          # longest-first
            if before.endswith(word):
                k = len(before) - len(word)
                if k == 0 or before[k - 1] != _TSHEG:
                    observed.add(num)
                break
    return observed


def _attestation_issues(lineno, dec, text, ord_word, ordn, corpus_canon):
    """Check one node's title + ordinal against the candidates/enumerations corpus."""
    out = []
    disp_canon = _canon(text)
    if not disp_canon:
        return out

    # Tier 1 — exact display (ordinal + title) appears verbatim. Fully attested.
    if disp_canon in corpus_canon:
        return out

    topic_canon = _canon(_strip_leading_ordinal(text))
    topic_for_match = topic_canon
    found_topic = bool(topic_canon) and topic_canon in corpus_canon
    if not found_topic and topic_canon:
        trimmed = _strip_trailing_particle(topic_canon)
        if trimmed and trimmed in corpus_canon:
            topic_for_match, found_topic = trimmed, True

    # Tier 2 — title attested; verify the ordinal the source attaches to it.
    if found_topic:
        if ord_word is not None:
            observed = _observed_ordinals_before(topic_for_match, corpus_canon)
            if observed and ordn not in observed:
                shown = ", ".join(str(x) for x in sorted(observed))
                out.append(
                    f"L{lineno}: ordinal {ordn} ({ord_word}) not attested for this "
                    f"title in candidates/enumerations (source attaches: {shown})  "
                    f"->  {dec} {text[:40]}"
                )
        return out

    # Tier 3 — title not found verbatim. Fall back to fuzzy syllable coverage.
    coverage = _title_bigram_coverage(topic_canon or disp_canon, corpus_canon)
    if coverage < TITLE_COVERAGE_MIN:
        out.append(
            f"L{lineno}: title not attested in candidates/enumerations "
            f"(coverage {coverage:.0%}) — possible hallucination  ->  "
            f"{dec} {text[:50]}"
        )
    return out


def qc_check_tree(tree_text: str, corpus_text: str = ""):
    """Return a list of human-readable QC issue strings for a TOC tree (deterministic)."""
    issues = []
    seen = {}
    parsed = []  # (lineno, segs_tuple)
    corpus_canon = _canon(corpus_text) if corpus_text else ""
    for lineno, raw in enumerate(tree_text.splitlines(), 1):
        if not re.match(r"^\s*\*\s", raw):
            continue  # not a tree entry (header, ---, blank, etc.)
        m = _TREE_LINE_RE.match(raw)
        if not m:
            issues.append(f"L{lineno}: unparseable tree line: {raw.strip()}")
            continue
        dec = m.group("dec")
        text = m.group("text").strip()
        indent = len(m.group("indent").replace("\t", "   "))
        segs = dec.split(".")
        depth = len(segs)
        last = int(segs[-1])

        if indent != 3 * (depth - 1):
            issues.append(f"L{lineno}: indent {indent} spaces != expected "
                          f"{3 * (depth - 1)} for depth {depth} ({dec})")
        ord_word, ordn = _leading_tibetan_ordinal_word(text)
        if ordn is not None and ordn != last:
            issues.append(f"L{lineno}: Tibetan ordinal = {ordn} but decimal last "
                          f"segment = {last}  ->  {dec} {text[:40]}")
        if dec in seen:
            issues.append(f"L{lineno}: duplicate decimal {dec} (also at L{seen[dec]})")
        else:
            seen[dec] = lineno

        # ---- attestation against candidates + enumerations ----
        if corpus_canon:
            issues.extend(
                _attestation_issues(lineno, dec, text, ord_word, ordn, corpus_canon)
            )

        parsed.append((lineno, tuple(int(s) for s in segs)))

    # sibling-sequence check: each parent's children must be 1..n with no gaps/dups
    children = {}
    for lineno, segs in parsed:
        children.setdefault(segs[:-1], []).append(segs[-1])
    for parent, nums in children.items():
        expected = list(range(1, len(nums) + 1))
        if sorted(nums) != expected:
            pid = ".".join(map(str, parent)) or "(root)"
            issues.append(f"children of {pid}: numbered {sorted(nums)}, "
                          f"expected {expected}")
    return issues


def main():
    ap = argparse.ArgumentParser(
        description="Deterministic QC checker for a sa-bcad decimal TOC tree.")
    ap.add_argument("tree_file", help="TOC tree markdown file to check")
    ap.add_argument("--corpus", nargs="*", default=[],
                    help="Candidate / enumeration files to check attestation against "
                         "(omit for internal-consistency checks only)")
    ap.add_argument("--out", default=None,
                    help="Write a markdown QC report here instead of printing")
    args = ap.parse_args()

    tree_text = Path(args.tree_file).read_text(encoding="utf-8")
    corpus_text = "\n".join(
        Path(p).read_text(encoding="utf-8") for p in args.corpus if Path(p).exists()
    )

    issues = qc_check_tree(tree_text, corpus_text=corpus_text)

    if args.out:
        body = "\n".join(f"- {x}" for x in issues) if issues else "- (none)"
        Path(args.out).write_text(
            f"# TOC tree QC report\n\nissues: {len(issues)}\n\n## Issues\n\n{body}\n",
            encoding="utf-8")
        print(f"✓ {len(issues)} issue(s) → {args.out}")
    else:
        if not issues:
            print("✓ 0 issues — tree is clean.")
        else:
            print(f"{len(issues)} issue(s):")
            for x in issues:
                print(f"  - {x}")

    sys.exit(len(issues))


if __name__ == "__main__":
    main()
