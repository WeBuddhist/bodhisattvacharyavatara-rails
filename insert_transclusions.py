#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
insert_transclusions.py

Inserts Obsidian root-text verse transclusions into the Tibetan commentary file,
using the structural outline file as the mapping guide.
"""

import re
import os

# File paths
OUTLINE_FILE = (
    "/sessions/keen-adoring-pasteur/mnt/bodhisattvacharyavatara-rails/"
    "3-TRANSFORMATIONS/Adaptations/bo-kunpal-sa-bcad/"
    "bo-མཁན་པོ་ཀུན་དཔལ། སྤྱོད་འཇུག་ས་བཅད། ས་བཅད་རྩ་སྦྱར།.md"
)
COMMENTARY_FILE = (
    "/sessions/keen-adoring-pasteur/mnt/bodhisattvacharyavatara-rails/"
    "1-SOURCES/Commentaries/bo-མཁན་པོ་ཀུན་དཔལ།.md"
)
BACKUP_FILE = COMMENTARY_FILE + ".bak2"
LOG_FILE = (
    "/sessions/keen-adoring-pasteur/mnt/bodhisattvacharyavatara-rails/"
    "0-INBOX/transclusion-not-found.log"
)

TRANSCLUSION_RE = re.compile(
    r'^\s*!\[\[1-SOURCES/Translations/bo-བློ་ལྡན་ཤེས་རབ།\.md#\^[\d\-]+\]\]\s*$'
)
NODE_RE = re.compile(r'^\s*-\s+(.+?)\s+\^TOC-[\d\-]+\s*$')

# Tibetan shad character (།) – may appear at end of sa-bcad labels
SHAD = '།'


def strip_label_for_search(label):
    """
    Return a version of the label suitable for substring search in the commentary.
    The commentary often omits the trailing shad and adds a connecting particle instead.
    So we strip the trailing shad (and any trailing whitespace/particle characters)
    to get a more flexible search string.
    """
    # Strip trailing shad and trailing space
    stripped = label.rstrip()
    if stripped.endswith(SHAD):
        stripped = stripped[:-1].rstrip()
    return stripped


def parse_outline(filepath):
    """
    Parse outline file, return list of (label, search_label, [transclusion_lines]).
    Only includes nodes with at least one transclusion line.
    """
    with open(filepath, encoding='utf-8') as f:
        lines = f.readlines()

    result = []
    n = len(lines)
    i = 0

    while i < n:
        line = lines[i].rstrip('\n')
        m = NODE_RE.match(line)
        if m:
            label = m.group(1).strip()
            search_label = strip_label_for_search(label)
            transclusions = []
            j = i + 1
            while j < n:
                next_line = lines[j].rstrip('\n')
                if NODE_RE.match(next_line):
                    break
                if TRANSCLUSION_RE.match(next_line):
                    clean = next_line.strip()
                    transclusions.append(clean)
                j += 1

            if transclusions:
                result.append((label, search_label, transclusions))
        i += 1

    return result


def parse_commentary(filepath):
    """
    Parse commentary into units (paragraphs + blank separators).
    Each unit is a list of lines (no trailing newlines).
    """
    with open(filepath, encoding='utf-8') as f:
        content = f.read()

    lines = content.split('\n')
    units = []
    current = []

    for line in lines:
        if line.strip() == '':
            if current:
                units.append(current)
                current = []
            units.append([''])
        else:
            current.append(line)

    if current:
        units.append(current)

    return units


def unit_text(unit):
    return '\n'.join(unit)


def find_insertion_point(commentary_units, search_label):
    """
    Find the index of the first unit whose text contains search_label.
    Returns None if not found.
    """
    for i, unit in enumerate(commentary_units):
        text = unit_text(unit)
        if search_label in text:
            return i
    return None


def already_inserted(commentary_units, idx, transclusions):
    """
    Check if any transclusion is already present in units immediately before idx.
    """
    check_idx = idx - 1
    while check_idx >= 0:
        unit = commentary_units[check_idx]
        text = unit_text(unit)
        if text.strip() == '':
            check_idx -= 1
            continue
        for t in transclusions:
            if t in text:
                return True
        break
    return False


def rebuild_commentary(commentary_units):
    parts = []
    for unit in commentary_units:
        parts.append('\n'.join(unit))
    return '\n'.join(parts)


def main():
    # Step 1: Parse outline
    print("Parsing outline file...")
    nodes = parse_outline(OUTLINE_FILE)
    print(f"  Found {len(nodes)} nodes with transclusions.")

    # Step 2: Parse commentary
    print("Parsing commentary file...")
    commentary_units = parse_commentary(COMMENTARY_FILE)
    print(f"  Found {len(commentary_units)} units.")

    # Step 3: Match labels to paragraphs
    insertion_map = {}   # idx -> [(label, transclusions)]
    not_found = []
    matched = 0

    for label, search_label, transclusions in nodes:
        idx = find_insertion_point(commentary_units, search_label)
        if idx is None:
            not_found.append(label)
            continue
        matched += 1
        if idx not in insertion_map:
            insertion_map[idx] = []
        insertion_map[idx].append((label, transclusions))

    # Preview first 5 matches
    print("\n=== PREVIEW: First 5 matched insertions ===\n")
    preview_count = 0
    for label, search_label, transclusions in nodes:
        if preview_count >= 5:
            break
        idx = find_insertion_point(commentary_units, search_label)
        if idx is None:
            continue
        para_text = unit_text(commentary_units[idx])[:120]
        print(f"Label:        {label}")
        print(f"Search for:   {search_label!r}")
        print(f"Target para:  {para_text!r}")
        print(f"Transclusions:")
        for t in transclusions:
            print(f"  {t}")
        print()
        preview_count += 1

    print(f"\n=== SUMMARY BEFORE WRITING ===")
    print(f"Total nodes with transclusions: {len(nodes)}")
    print(f"Matched: {matched}")
    print(f"Not found: {len(not_found)}")
    print()

    # Step 4: Filter already-inserted, build new units
    skipped_already = 0
    filtered_insertion_map = {}
    for idx, label_transclusion_pairs in insertion_map.items():
        filtered_pairs = []
        for label, transclusions in label_transclusion_pairs:
            if already_inserted(commentary_units, idx, transclusions):
                skipped_already += 1
            else:
                filtered_pairs.append((label, transclusions))
        if filtered_pairs:
            filtered_insertion_map[idx] = filtered_pairs

    if skipped_already:
        print(f"Skipped {skipped_already} already-inserted labels.")

    # Build new units list by inserting in reverse index order
    new_units = list(commentary_units)

    for idx in sorted(filtered_insertion_map.keys(), reverse=True):
        label_transclusion_pairs = filtered_insertion_map[idx]

        # Collect all unique transclusion lines for this insertion point
        all_transclusions = []
        for _label, transclusions in label_transclusion_pairs:
            for t in transclusions:
                if t not in all_transclusions:
                    all_transclusions.append(t)

        # Build insertion block: blank + transclusion lines + blank
        insert_units = [[''] ]
        for t in all_transclusions:
            insert_units.append([t])
        insert_units.append([''])

        new_units = new_units[:idx] + insert_units + new_units[idx:]

    # Write backup (of current state)
    with open(COMMENTARY_FILE, encoding='utf-8') as f:
        original_content = f.read()

    print(f"Writing backup to: {BACKUP_FILE}")
    with open(BACKUP_FILE, 'w', encoding='utf-8') as f:
        f.write(original_content)

    # Write modified commentary
    new_content = rebuild_commentary(new_units)
    print(f"Writing modified commentary to: {COMMENTARY_FILE}")
    with open(COMMENTARY_FILE, 'w', encoding='utf-8') as f:
        f.write(new_content)

    # Write not-found log
    os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)
    print(f"Writing not-found log to: {LOG_FILE}")
    with open(LOG_FILE, 'w', encoding='utf-8') as f:
        f.write("# Transclusion insertion — labels not found in commentary\n\n")
        f.write(f"Total not found: {len(not_found)}\n\n")
        for label in not_found:
            f.write(f"- {label}\n")

    insertions_made = sum(len(v) for v in filtered_insertion_map.values())
    print("\n=== FINAL SUMMARY ===")
    print(f"Total nodes with transclusions: {len(nodes)}")
    print(f"Matched: {matched}")
    print(f"Insertion points used: {len(filtered_insertion_map)}")
    print(f"Labels actually inserted: {insertions_made}")
    print(f"Already present (skipped): {skipped_already}")
    print(f"Not found: {len(not_found)}")
    print(f"Backup: {BACKUP_FILE}")
    print(f"Commentary: {COMMENTARY_FILE}")
    print(f"Log: {LOG_FILE}")


if __name__ == '__main__':
    main()
