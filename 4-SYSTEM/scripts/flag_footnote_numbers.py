#!/usr/bin/env python3
"""
flag_footnote_numbers.py
========================
STEP 1 of 2 — flag embedded footnote numbers for HUMAN VALIDATION.

Scans a block-aligned translation markdown file (e.g.
1-SOURCES/Translations/en-Padmakara_2006.md) for footnote reference numbers
that were flattened into the running text, e.g.

    To those who go in bliss,25 the dharmakaya26 they possess, ...

A footnote marker is a run of digits that is *attached* (no space) to the
preceding letter or punctuation. This deliberately does NOT match:

  * Obsidian block IDs at end of line  (^1-1, ^5-104, ^T-1)  -> stripped first
  * numbers preceded by whitespace      (verse counts, "1." headings)
  * digits inside YAML frontmatter      (dates, file IDs like BCAV08)
  * markdown heading lines (## 1. ...)

It writes TWO files:

  1. <stem>.footnote-flags.tsv   -- machine-readable, consumed by the remover.
                                     Column 1 "approve" defaults to Y; a human
                                     sets it to N to reject a false positive.
  2. <stem>.footnote-flags.md    -- human-readable review report with context.

A sequence sanity-check is printed: genuine footnotes are contiguous, so any
gap or duplicate is surfaced for the reviewer.

Usage:
    python flag_footnote_numbers.py <path-to-md> [--outdir DIR]

Nothing is modified in the source file. Run remove_footnote_numbers.py only
AFTER a human has reviewed the .tsv.
"""
import argparse
import os
import re
import sys

BLOCK_ID_RE = re.compile(r"\s*\^[0-9A-Za-z\-]+\s*$")
DIGIT_RE = re.compile(r"\d+")


def find_frontmatter_end(lines):
    """Return index of the closing '---' of YAML frontmatter, or -1."""
    if lines and lines[0].strip() == "---":
        for i in range(1, len(lines)):
            if lines[i].strip() == "---":
                return i
    return -1


def extract_candidates(lines):
    """Yield dicts for each attached digit-run in the body (footnote markers)."""
    fm_end = find_frontmatter_end(lines)
    out = []
    for idx, line in enumerate(lines):
        lineno = idx + 1
        if idx <= fm_end:                 # skip YAML frontmatter
            continue
        if line.lstrip().startswith("#"):  # skip markdown headings
            continue
        body = BLOCK_ID_RE.sub("", line)   # drop trailing block id from scope
        for m in DIGIT_RE.finditer(body):
            start = m.start()
            prev = body[start - 1] if start > 0 else ""
            # attached = immediately preceded by a non-space, non-caret, non-hyphen char
            if prev and prev not in " \t^-":
                # the word/punct the number is glued to (for the review report)
                left = body[:start]
                attached_to = re.search(r"\S+$", left)
                out.append({
                    "line": lineno,
                    "number": m.group(0),
                    "col": start,            # 0-based column in the de-block-id'd line
                    "attached_to": attached_to.group(0) if attached_to else prev,
                    "context": line.rstrip("\n"),
                })
    return out


def sequence_report(cands):
    nums = [int(c["number"]) for c in cands]
    if not nums:
        return "No candidates found."
    s = sorted(nums)
    missing = [n for n in range(s[0], s[-1] + 1) if n not in set(nums)]
    dups = sorted({n for n in nums if nums.count(n) > 1})
    msg = [f"count={len(nums)}  range={s[0]}-{s[-1]}"]
    msg.append("gaps in sequence: " + (", ".join(map(str, missing)) if missing else "none"))
    msg.append("duplicate numbers: " + (", ".join(map(str, dups)) if dups else "none"))
    return "\n".join(msg)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("path")
    ap.add_argument("--outdir", default=None,
                    help="where to write the flag files (default: alongside source)")
    args = ap.parse_args()

    if not os.path.isfile(args.path):
        sys.exit(f"File not found: {args.path}")

    with open(args.path, encoding="utf-8") as fh:
        lines = fh.read().split("\n")

    cands = extract_candidates(lines)
    outdir = args.outdir or os.path.dirname(os.path.abspath(args.path))
    stem = os.path.splitext(os.path.basename(args.path))[0]
    tsv_path = os.path.join(outdir, f"{stem}.footnote-flags.tsv")
    md_path = os.path.join(outdir, f"{stem}.footnote-flags.md")

    # machine-readable TSV
    with open(tsv_path, "w", encoding="utf-8") as fh:
        fh.write("approve\tline\tnumber\tcol\tattached_to\tcontext\n")
        for c in cands:
            ctx = c["context"].replace("\t", " ")
            fh.write(f"Y\t{c['line']}\t{c['number']}\t{c['col']}\t{c['attached_to']}\t{ctx}\n")

    # human-readable report
    report = sequence_report(cands)
    with open(md_path, "w", encoding="utf-8") as fh:
        fh.write(f"# Footnote-number flags — {os.path.basename(args.path)}\n\n")
        fh.write("Each row is a digit run found glued to the running text (a flattened\n")
        fh.write("footnote marker). Block IDs (`^1-1`) are excluded by construction.\n\n")
        fh.write("**Validation:** genuine footnotes form one unbroken ascending run, so\n")
        fh.write("any gap or duplicate below is a red flag to inspect.\n\n")
        fh.write("```\n" + report + "\n```\n\n")
        fh.write("To reject a false positive, set its `approve` column to `N` in\n")
        fh.write(f"`{os.path.basename(tsv_path)}`, then run the remover.\n\n")
        fh.write("| # | line | attached to | context |\n")
        fh.write("|---|------|-------------|---------|\n")
        for c in cands:
            ctx = c["context"].replace("|", "\\|")
            fh.write(f"| {c['number']} | {c['line']} | `{c['attached_to']}` | {ctx} |\n")

    print(f"candidates: {len(cands)}")
    print(report)
    print(f"\nwrote: {tsv_path}")
    print(f"wrote: {md_path}")


if __name__ == "__main__":
    main()
