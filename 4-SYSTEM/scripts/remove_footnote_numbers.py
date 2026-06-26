#!/usr/bin/env python3
"""
remove_footnote_numbers.py
==========================
STEP 2 of 2 — remove footnote numbers AFTER human validation.

Consumes the TSV produced by flag_footnote_numbers.py (with the human's
approve column reviewed) and deletes ONLY the approved digit runs from the
running text. It removes just the digits, leaving the surrounding word,
punctuation and spacing intact:

    "...go in bliss,25 the dharmakaya26 they..."  ->  "...go in bliss, the dharmakaya they..."
    "...and wealth28"                              ->  "...and wealth"

Safety guarantees:
  * Block IDs (^1-1, ^5-104) are NEVER in scope — each line's trailing block id
    is held aside and re-appended untouched.
  * Removal is driven entirely by the validated TSV (line + number + column),
    so nothing outside the approved list is altered.
  * Line count and block-ID count are asserted unchanged before writing.
  * A .bak backup is written next to the target unless --no-backup.
  * --dry-run reports what would change and writes nothing.

Usage:
    # preview
    python remove_footnote_numbers.py <source.md> <flags.tsv> --dry-run
    # apply in place (creates source.md.bak)
    python remove_footnote_numbers.py <source.md> <flags.tsv>
    # write a separate cleaned copy instead of editing in place
    python remove_footnote_numbers.py <source.md> <flags.tsv> --out cleaned.md
"""
import argparse
import csv
import os
import re
import sys

BLOCK_ID_RE = re.compile(r"(\s*\^[0-9A-Za-z\-]+\s*)$")


def load_approved(tsv_path):
    """Return {lineno: [number_str, ...]} for rows whose approve column is Y."""
    approved = {}
    total = 0
    with open(tsv_path, encoding="utf-8") as fh:
        reader = csv.DictReader(fh, delimiter="\t")
        for row in reader:
            total += 1
            if (row.get("approve") or "").strip().upper() != "Y":
                continue
            ln = int(row["line"])
            approved.setdefault(ln, []).append(row["number"].strip())
    return approved, total


def strip_block_id(line):
    """Split a line into (body, block_id_suffix). Suffix may be ''."""
    m = BLOCK_ID_RE.search(line)
    if m:
        return line[:m.start()], m.group(1)
    return line, ""


def remove_on_line(line, numbers):
    """Remove each approved attached digit-run on this line. Returns (new_line, removed_list)."""
    body, suffix = strip_block_id(line)
    removed = []
    for num in numbers:
        # match the number only when glued to a preceding non-space/non-^/non-hyphen char
        pat = re.compile(r"(?<=[^\s\^\-])" + re.escape(num) + r"(?![0-9])")
        m = pat.search(body)
        if not m:
            removed.append((num, False))
            continue
        body = body[:m.start()] + body[m.end():]
        removed.append((num, True))
    return body + suffix, removed


def count_block_ids(text):
    return len(re.findall(r"\^[0-9A-Za-z\-]+\b", text))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("source")
    ap.add_argument("tsv")
    ap.add_argument("--out", default=None,
                    help="write cleaned text here instead of editing source in place")
    ap.add_argument("--no-backup", action="store_true",
                    help="do not write a .bak when editing in place")
    ap.add_argument("--dry-run", action="store_true",
                    help="report changes but write nothing")
    args = ap.parse_args()

    for p in (args.source, args.tsv):
        if not os.path.isfile(p):
            sys.exit(f"File not found: {p}")

    with open(args.source, encoding="utf-8") as fh:
        original = fh.read()
    lines = original.split("\n")
    block_ids_before = count_block_ids(original)

    approved, total_rows = load_approved(args.tsv)
    approved_count = sum(len(v) for v in approved.values())

    applied, misses = 0, []
    for ln, numbers in approved.items():
        idx = ln - 1
        if idx < 0 or idx >= len(lines):
            misses.append((ln, "line out of range"))
            continue
        new_line, removed = remove_on_line(lines[idx], numbers)
        for num, ok in removed:
            if ok:
                applied += 1
            else:
                misses.append((ln, f"number {num} not found attached on line"))
        lines[idx] = new_line

    cleaned = "\n".join(lines)
    block_ids_after = count_block_ids(cleaned)
    line_count_ok = original.count("\n") == cleaned.count("\n")
    block_ids_ok = block_ids_before == block_ids_after

    print(f"TSV rows           : {total_rows}")
    print(f"approved markers   : {approved_count}")
    print(f"removed            : {applied}")
    print(f"not found / skipped: {len(misses)}")
    for ln, why in misses:
        print(f"   line {ln}: {why}")
    print(f"block IDs before/after: {block_ids_before}/{block_ids_after}  ({'OK' if block_ids_ok else 'MISMATCH'})")
    print(f"line count unchanged  : {'OK' if line_count_ok else 'MISMATCH'}")

    if not block_ids_ok or not line_count_ok:
        sys.exit("ABORT: integrity check failed — nothing written.")

    if args.dry_run:
        print("\n[dry-run] no files written.")
        return

    target = args.out or args.source
    if not args.out and not args.no_backup:
        bak = args.source + ".bak"
        with open(bak, "w", encoding="utf-8") as fh:
            fh.write(original)
        print(f"backup written: {bak}")
    with open(target, "w", encoding="utf-8") as fh:
        fh.write(cleaned)
    print(f"cleaned text written: {target}")


if __name__ == "__main__":
    main()
