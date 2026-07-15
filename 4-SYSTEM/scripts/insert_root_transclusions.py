#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
insert_root_transclusions.py

Type 1 version-to-version transclusion insertion for targets whose verses
span *multiple* lines (a blank-line-separated paragraph per verse), unlike
the single-line-per-verse case handled by insert_transclusions.py.

For every block ID that exists in both the source root text and the target
file, inserts:

    ![[<source-path>#^N-V]]
    [blank line]
    <verse paragraph ...>  ^N-V

immediately before the target's verse paragraph (i.e. before its first
line, not before the line carrying the id). Structural ids are skipped by
design, matching vault precedent (the source file itself never transcludes
before its own chapter headings or title):

  - the bare title id `^0`
  - any chapter/section heading id `^<chapter>-0` (e.g. `^1-0`, `^I-0`)

Idempotent: an id already preceded by its transclusion line is skipped, so
the script is safe to re-run on a partially-transcluded file.

Usage:
    python insert_root_transclusions.py [--source PATH] [--target PATH] [--apply]

Without --apply, only a dry-run report is printed and no file is written.
"""

import argparse
import glob
import re
import sys

DEFAULT_TARGET = "3-TRANSFORMATIONS/Translations/en-translate/BCA-Full-Plain-English.md"


def default_source():
    """Resolve the canonical Tibetan translation file without hardcoding its
    non-ASCII filename (avoids escape-sequence transcription errors)."""
    candidates = [p.replace("\\", "/") for p in glob.glob("1-SOURCES/Translations/bo-*.md")]
    exact = [p for p in candidates if "WeBuddhist" not in p]
    return (exact or candidates)[0]

# Matches a block id at the end of a line: ^I-1, ^1-1, ^10-58, ^10-a, ^8-24x1, ^0
ID_RE = re.compile(r"\^([0-9IX]+(?:-[a-zA-Z0-9]+)?)\s*$")

# Structural ids to exclude from transclusion: bare title `0`, and any
# `<chapter>-0` heading id.
STRUCTURAL_RE = re.compile(r"^(0|[0-9IXa-z]+-0)$")

TRANSCLUSION_ID_RE = re.compile(r"!\[\[[^\]]*?#\^([0-9IXa-zA-Z\-]+)\]\]")


def load_lines(path):
    with open(path, "r", encoding="utf-8", newline="") as f:
        return f.read().splitlines(keepends=True)


def detect_eol(lines):
    for line in lines:
        if line.endswith("\r\n"):
            return "\r\n"
        if line.endswith("\n"):
            return "\n"
    return "\n"


def extract_ids(lines):
    ids = set()
    for line in lines:
        m = ID_RE.search(line.rstrip("\r\n"))
        if m:
            ids.add(m.group(1))
    return ids


def scan_blocks(lines):
    """Return list of (block_start_idx, block_end_idx, block_id_or_None)."""
    blocks = []
    block_start = 0
    n = len(lines)
    i = 0
    while i < n:
        stripped = lines[i].rstrip("\r\n")
        if stripped == "":
            block_start = i + 1
            i += 1
            continue
        m = ID_RE.search(stripped)
        if m:
            blocks.append((block_start, i, m.group(1)))
            block_start = i + 1
        i += 1
    return blocks


def existing_transclusion_ids_before(lines, block_start_idx):
    """Collect transclusion ids present in the blank-separated block(s)
    immediately preceding block_start_idx (walks back over blank lines and
    any contiguous transclusion-only lines)."""
    ids = set()
    j = block_start_idx - 1
    while j >= 0:
        stripped = lines[j].rstrip("\r\n")
        if stripped == "":
            j -= 1
            continue
        m = TRANSCLUSION_ID_RE.search(stripped)
        if m:
            ids.add(m.group(1))
            j -= 1
            continue
        break
    return ids


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", default=None, help="Root-text/translation source file")
    parser.add_argument("--target", default=DEFAULT_TARGET, help="Target file to receive transclusions")
    parser.add_argument("--apply", action="store_true", help="Write changes (default: dry-run only)")
    args = parser.parse_args()
    if args.source is None:
        args.source = default_source()

    source_lines = load_lines(args.source)
    target_lines = load_lines(args.target)
    eol = detect_eol(target_lines)

    source_ids = extract_ids(source_lines)
    target_ids = extract_ids(target_lines)

    matched_ids = source_ids & target_ids
    only_source = sorted(source_ids - target_ids)
    only_target = sorted(target_ids - source_ids)

    structural_ids = {i for i in matched_ids if STRUCTURAL_RE.match(i)}
    verse_ids = matched_ids - structural_ids

    blocks = scan_blocks(target_lines)
    block_ids = {b[2] for b in blocks if b[2]}
    unresolved = target_ids - block_ids
    if unresolved:
        print(f"WARNING: {len(unresolved)} target id(s) not resolved to a paragraph block: {sorted(unresolved)}")

    to_insert = []
    skipped_existing = []
    for (start_idx, _end_idx, block_id) in blocks:
        if block_id is None or block_id not in verse_ids:
            continue
        existing = existing_transclusion_ids_before(target_lines, start_idx)
        if block_id in existing:
            skipped_existing.append(block_id)
        else:
            to_insert.append((start_idx, block_id))

    print("=== Summary ===")
    print(f"Source ids:            {len(source_ids)}")
    print(f"Target ids:            {len(target_ids)}")
    print(f"Matched ids:           {len(matched_ids)}")
    print(f"  structural (excluded): {len(structural_ids)} -> {sorted(structural_ids)}")
    print(f"  verse-level (eligible): {len(verse_ids)}")
    print(f"Only in source (no target block, skipped): {only_source}")
    print(f"Only in target (no source, skipped):       {only_target}")
    print(f"To insert:             {len(to_insert)}")
    print(f"Already present (skipped): {len(skipped_existing)}")

    if to_insert:
        print("\nFirst 3 insertions:")
        for start_idx, block_id in to_insert[:3]:
            print(f"  before line {start_idx + 1} (^{block_id}): {target_lines[start_idx].strip()[:70]!r}")
        print("Last 3 insertions:")
        for start_idx, block_id in to_insert[-3:]:
            print(f"  before line {start_idx + 1} (^{block_id}): {target_lines[start_idx].strip()[:70]!r}")

    insert_map = {start_idx: block_id for start_idx, block_id in to_insert}
    out_lines = []
    for idx, line in enumerate(target_lines):
        if idx in insert_map:
            block_id = insert_map[idx]
            out_lines.append(f"![[{args.source}#^{block_id}]]{eol}")
            out_lines.append(eol)
        out_lines.append(line)

    added = len(out_lines) - len(target_lines)
    expected = 2 * len(to_insert)
    print(f"\nLines added: {added} (expected {expected})")
    if added != expected:
        print("ERROR: line delta mismatch, aborting write.")
        sys.exit(1)

    if args.apply:
        with open(args.target, "w", encoding="utf-8", newline="") as f:
            f.write("".join(out_lines))
        print(f"\nAPPLIED: wrote {len(to_insert)} transclusion(s) to {args.target}")
    else:
        print("\n[dry-run] No file written. Re-run with --apply to write changes.")


if __name__ == "__main__":
    main()
