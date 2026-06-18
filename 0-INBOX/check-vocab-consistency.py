#!/usr/bin/env python3
"""
check-vocab-consistency.py
==========================
Checks a translated .md file for vocabulary inconsistencies against:
  1. The track termbase  (locked renderings that MUST be used)
  2. A forbidden-terms list  (transliterations and alternative renderings that must NOT appear)

Usage:
    python check-vocab-consistency.py --file BCA-Chapters-1-3-Plain-English.md --track en-plain-english
    python check-vocab-consistency.py --file "3-TRANSFORMATIONS/Translations/en-ai/Chapter two (Claude AI).md" --track en-ai

Output:
    Prints a report to stdout. Exit code 0 = clean, 1 = issues found.
"""

import re
import os
import sys
import argparse

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT       = os.path.dirname(SCRIPT_DIR)

# ---------------------------------------------------------------------------
# Forbidden terms per track
# These are words that should NEVER appear in the translation output.
# Add more as the termbase grows.
# ---------------------------------------------------------------------------
FORBIDDEN = {
    "en-plain-english": [
        # Sanskrit / Tibetan transliterations
        "bodhicitta", "bodhisattva", "samsara", "nirvana", "dharma",
        "dharmakaya", "dharmakāya", "sugata", "tathagata", "tathāgata",
        "sunyata", "śūnyatā", "shunyata", "karma", "bodhi",
        # Disallowed English renderings
        "merit",        # → goodness / helpful deeds
        "virtue",       # → goodness
        "sin",          # → harmful deeds
        "vice",         # → harmful deeds
        "vow",          # → commitment / promise
        "leisure and endowment",  # → precious human life
        "Samsara",
        "Nirvana",
        "Dharma",
        "Bodhicitta",
        "Bodhisattva",
    ],
    "en-ai": [
        # No transliteration of common terms; Sanskrit proper names in italics are OK
        "samsara",   # → cycle of life / cycle of existence
        "nirvana",   # → liberation / final peace (unless as a technical term in context)
        # en-ai allows more Sanskrit; forbidden list is shorter
    ],
}

# ---------------------------------------------------------------------------
# Required renderings per track
# For each concept, check that AT LEAST ONE of the approved forms appears
# in the file (rough check — not verse-aligned).
# ---------------------------------------------------------------------------
REQUIRED_RENDERINGS = {
    "en-plain-english": {
        "Mind of Enlightenment":   "bodhicitta rendering",
        "Hero of Enlightenment":   "bodhisattva rendering",
        "cycle of life":           "samsara rendering",
        "the Blissful Ones":       "sugata rendering",
        "harmful deeds":           "papa/duskrta rendering",
        "goodness":                "punya/kusala rendering",
    },
    "en-ai": {
        "mind of enlightenment":   "bodhicitta rendering",
        "cycle of":                "samsara rendering",
    },
}

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def read_file(path: str) -> str:
    with open(path, encoding="utf-8") as f:
        return f.read()


def strip_frontmatter(text: str) -> str:
    """Remove YAML frontmatter if present."""
    if text.startswith("---"):
        end = text.find("\n---", 3)
        if end != -1:
            return text[end + 4:]
    return text


def strip_block_ids(text: str) -> str:
    """Remove ^N-N block ID tags so they don't confuse the checks."""
    return re.sub(r'\^[\w-]+', '', text)


def find_forbidden(text: str, forbidden: list[str]) -> list[tuple[int, str, str]]:
    """
    Returns list of (line_number, term, context_snippet) for each hit.
    Case-insensitive, whole-word match.
    """
    hits = []
    lines = text.splitlines()
    for lineno, line in enumerate(lines, 1):
        # Skip markdown headings, notes, and the footer
        if line.startswith("#") or line.startswith("*[Note:") or line.startswith("*Source:"):
            continue
        for term in forbidden:
            pattern = r'\b' + re.escape(term) + r'\b'
            if re.search(pattern, line, re.IGNORECASE):
                snippet = line.strip()[:80]
                hits.append((lineno, term, snippet))
    return hits


def check_required(text: str, required: dict[str, str]) -> list[str]:
    """Returns list of missing required renderings."""
    missing = []
    text_lower = text.lower()
    for rendering, label in required.items():
        if rendering.lower() not in text_lower:
            missing.append(f"{label}: expected rendering '{rendering}' not found anywhere in file")
    return missing


def check_inconsistent_renderings(text: str) -> list[str]:
    """
    Heuristic: look for mixed usage of near-synonyms that suggest
    the translator switched renderings mid-file.
    """
    issues = []
    text_lower = text.lower()

    pairs = [
        # (term_a, term_b, note)
        ("mind of enlightenment", "awakening mind",
         "Two renderings for bodhicitta: 'mind of enlightenment' and 'awakening mind'"),
        ("cycle of life",         "cycle of existence",
         "Two renderings for samsara: 'cycle of life' and 'cycle of existence'"),
        ("hero of enlightenment", "son of the buddha",
         "Two renderings for bodhisattva-putra"),
        ("harmful deeds",         "negative deeds",
         "Two renderings for papa: 'harmful deeds' and 'negative deeds'"),
        ("harmful deeds",         "misdeeds",
         "Two renderings for papa: 'harmful deeds' and 'misdeeds'"),
        ("goodness",              "merit",
         "Two renderings for punya: 'goodness' and 'merit'"),
        ("the blissful ones",     "the sugatas",
         "Two renderings for sugata"),
        ("the teaching",          "the dharma",
         "Two renderings for dharma: 'the teaching' and 'the dharma'"),
    ]

    for a, b, note in pairs:
        if a in text_lower and b in text_lower:
            issues.append(note)

    return issues


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(description="Check translation vocabulary consistency.")
    parser.add_argument("--file",  "-f", required=True, help="Path to the translated .md file")
    parser.add_argument("--track", "-t", default="en-plain-english",
                        choices=["en-plain-english", "en-ai"],
                        help="Translation track (determines termbase rules)")
    args = parser.parse_args()

    # Resolve file path
    file_path = args.file
    if not os.path.isabs(file_path):
        # Try relative to project root first, then cwd
        candidate = os.path.join(ROOT, file_path)
        if os.path.exists(candidate):
            file_path = candidate

    if not os.path.exists(file_path):
        print(f"ERROR: File not found: {file_path}")
        sys.exit(1)

    print(f"\nVocabulary Consistency Check")
    print(f"File:  {os.path.basename(file_path)}")
    print(f"Track: {args.track}")
    print("=" * 60)

    raw_text  = read_file(file_path)
    clean     = strip_block_ids(strip_frontmatter(raw_text))
    forbidden = FORBIDDEN.get(args.track, [])
    required  = REQUIRED_RENDERINGS.get(args.track, {})

    total_issues = 0

    # --- 1. Forbidden terms ---
    forbidden_hits = find_forbidden(clean, forbidden)
    if forbidden_hits:
        print(f"\n[FAIL] Forbidden / disallowed terms found ({len(forbidden_hits)} hit(s)):")
        for lineno, term, snippet in forbidden_hits:
            print(f"  Line {lineno:>4}: '{term}'")
            print(f"           → {snippet}")
        total_issues += len(forbidden_hits)
    else:
        print("\n[PASS] No forbidden terms found.")

    # --- 2. Required renderings missing ---
    missing = check_required(clean, required)
    if missing:
        print(f"\n[WARN] Required renderings not found ({len(missing)}):")
        for m in missing:
            print(f"  - {m}")
        total_issues += len(missing)
    else:
        print("[PASS] All required renderings present.")

    # --- 3. Inconsistent rendering pairs ---
    inconsistencies = check_inconsistent_renderings(clean)
    if inconsistencies:
        print(f"\n[FAIL] Inconsistent renderings detected ({len(inconsistencies)}):")
        for issue in inconsistencies:
            print(f"  - {issue}")
        total_issues += len(inconsistencies)
    else:
        print("[PASS] No inconsistent rendering pairs detected.")

    # --- 4. Block ID coverage (are all expected verse IDs present?) ---
    block_ids = re.findall(r'\^(\d+)-(\d+)', raw_text)
    if block_ids:
        chapters_found = sorted(set(int(c) for c, v in block_ids))
        print(f"\n[INFO] Block IDs found for chapters: {chapters_found}")
        for ch in chapters_found:
            verses = sorted(int(v) for c, v in block_ids if int(c) == ch)
            if verses:
                expected = list(range(verses[0], verses[-1] + 1))
                missing_v = [v for v in expected if v not in verses]
                if missing_v:
                    print(f"  [WARN] Ch{ch}: missing verse IDs {missing_v}")
                else:
                    print(f"  [PASS] Ch{ch}: verses {verses[0]}–{verses[-1]} all present")
    else:
        print("\n[WARN] No block IDs (^N-N) found in file.")

    # --- Summary ---
    print("\n" + "=" * 60)
    if total_issues == 0:
        print("RESULT: CLEAN — no vocabulary issues found.")
        sys.exit(0)
    else:
        print(f"RESULT: {total_issues} issue(s) found. Review output above.")
        sys.exit(1)


if __name__ == "__main__":
    main()
