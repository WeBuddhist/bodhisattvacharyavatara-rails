#!/usr/bin/env python3
"""
find_sa_bcad.py - Phase-1 assist for the `tag-inline-toc` skill.

Scans a formatted Tibetan commentary and prints a *shortlist* of candidate
structural-announcement (sa bcad) lines and section openings, so the model
adjudicates and fixes term boundaries on a handful of lines instead of reading
the whole document cold.

This is a heuristic surfacing tool only. It does NOT decide depth, assign block
IDs, or wrap anything - those stay with the model (boundaries) and with
tag_inline_toc.py (deterministic rendering). False positives are expected and
harmless; the model is the judge.

Usage:
    python3 find_sa_bcad.py path/to/commentary.md
    python3 find_sa_bcad.py path/to/commentary.md --json
"""
from __future__ import annotations

import argparse
import json
import re
import sys

# Closed set of Tibetan cardinal counts that close an enumeration.
COUNTS = ["གཉིས", "གསུམ", "བཞི", "ལྔ", "དྲུག", "བདུན", "བརྒྱད", "དགུ", "བཅུ"]
# Ordinals that typically open a section body.
ORDINALS = [
    "དང་པོ", "གཉིས་པ", "གསུམ་པ", "བཞི་པ", "ལྔ་པ",
    "དྲུག་པ", "བདུན་པ", "བརྒྱད་པ", "དགུ་པ", "བཅུ་པ",
]

_COUNT_ALT = "|".join(COUNTS)
_ORD_ALT = "|".join(ORDINALS)

# Form B (compact): "...la [yang] COUNT[ las / ste / yod]."  e.g.
# "gnyis pa la bzhi." or "dang po la bzhi las."
FORM_B_RE = re.compile(r"ལ་(?:ཡང་)?(?:" + _COUNT_ALT + r")(?:་ལས|་སྟེ|་ཡོད)?།")
# Form A (full sentence): contains la ... dang ... COUNT closing the clause.
# The count is followed by a short tail (yod pa las / ste / las / bare) then a shad.
FORM_A_RE = re.compile(r"ལ་.*དང་.*(?:" + _COUNT_ALT + r")[^།]{0,12}།")
# Section opening: STARTS with an ordinal, with a ni topic marker close behind.
OPENING_RE = re.compile(r"^(?:" + _ORD_ALT + r")[་\s].{0,40}?ནི[།་]")
# Editorial verse-section marker: a line that is just "N.N" (or "N").
MARKER_RE = re.compile(r"^\s*\d+(?:\.\d+)*\s*$")
# Chapter label line: starts with le'u - NOT sa bcad.
CHAPTER_RE = re.compile(r"^\s*ལེའུ")


def classify(line: str) -> list[str]:
    """Return zero or more candidate tags for a line."""
    if CHAPTER_RE.search(line):
        return ["chapter-label (skip: not sa bcad)"]
    if MARKER_RE.match(line):
        return ["editorial-marker (skip: tag the NEXT Tibetan line)"]
    tags = []
    if FORM_B_RE.search(line):
        tags.append("announcement:FormB(compact)")
    if FORM_A_RE.search(line):
        tags.append("announcement:FormA(full-sentence)")
    if OPENING_RE.match(line):
        tags.append("section-opening")
    return tags


def scan(text: str) -> list[dict]:
    out = []
    for i, raw in enumerate(text.splitlines()):
        line = raw.strip()
        if not line:
            continue
        tags = classify(line)
        if tags:
            out.append({"line": i + 1, "tags": tags, "text": line})
    return out


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    p.add_argument("path")
    p.add_argument("--json", action="store_true", help="emit JSON")
    args = p.parse_args(argv)

    with open(args.path, encoding="utf-8") as f:
        text = f.read()
    hits = scan(text)

    if args.json:
        json.dump(hits, sys.stdout, ensure_ascii=False, indent=2)
        sys.stdout.write("\n")
        return 0

    if not hits:
        print("No candidate sa bcad lines found (is the file formatted?).")
        return 0

    print(str(len(hits)) + " candidate line(s):")
    print("")
    for h in hits:
        print("  L" + str(h["line"]).rjust(5) + "  [" + ", ".join(h["tags"]) + "]")
        snippet = h["text"][:90] + ("..." if len(h["text"]) > 90 else "")
        print("         " + snippet)
    print("")
    print("These are HEURISTIC candidates. Confirm each, fix term boundaries,")
    print("then build the annotation JSON from the confirmed set.")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except BrokenPipeError:
        sys.exit(0)
