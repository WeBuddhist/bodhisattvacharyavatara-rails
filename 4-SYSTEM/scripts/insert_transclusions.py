#!/usr/bin/env python3
"""
insert_transclusions.py

For each verse block ID in a translation file, insert a transclusion of the
matching root-text verse immediately before the verse paragraph, if the ID
exists in the root text and a transclusion is not already present.

Idempotent: handles multi-line verses correctly.
Skips heading lines (## Chapter ^N-0) — those are editorial structure.

Usage:
    python insert_transclusions.py <translation_file> [--root <root_text>] [--dry-run]

Example:
    python 4-SYSTEM/Scripts/insert_transclusions.py 1-SOURCES/Translations/en-Wallace.md
"""

import argparse
import re
import sys
from pathlib import Path

BLOCK_ID_RE = re.compile(r"\^([\w]+-\d+(?:-\d+)*)$")
HEADING_RE   = re.compile(r"^#{1,4}\s")


def collect_root_ids(root_path):
    ids = set()
    for line in root_path.read_text(encoding="utf-8").splitlines():
        m = BLOCK_ID_RE.search(line.rstrip())
        if m:
            ids.add(m.group(1))
    return ids


def line_before_paragraph(out):
    """
    Walk back through out[] to find the line immediately before the blank-line
    gap that precedes the current paragraph. Handles multi-line verses.
    """
    j = len(out) - 1
    # skip blank lines trailing in out (space between prev block and this one)
    while j >= 0 and not out[j].strip():
        j -= 1
    # skip the paragraph body (non-empty lines)
    while j >= 0 and out[j].strip():
        j -= 1
    # skip blank lines before the paragraph
    while j >= 0 and not out[j].strip():
        j -= 1
    return out[j].rstrip() if j >= 0 else ""


def insert_transclusions(translation_path, root_path, root_ids, vault_root, dry_run):
    try:
        root_rel = root_path.relative_to(vault_root).as_posix()
    except ValueError:
        root_rel = root_path.as_posix()

    lines = translation_path.read_text(encoding="utf-8").splitlines(keepends=False)
    out = []
    inserted = 0

    for line in lines:
        stripped = line.rstrip()
        # Never insert before heading lines (editorial structure, not verse content)
        if not HEADING_RE.match(stripped):
            m = BLOCK_ID_RE.search(stripped)
            if m:
                bid = m.group(1)
                if bid in root_ids:
                    transclusion = "![[" + root_rel + "#^" + bid + "]]"
                    if line_before_paragraph(out) != transclusion:
                        if out and out[-1].strip():
                            out.append("")
                        out.append(transclusion)
                        out.append("")
                        inserted += 1
        out.append(line)

    result = "\n".join(out)
    if not result.endswith("\n"):
        result += "\n"

    if dry_run:
        sys.stdout.write(result)
    else:
        translation_path.write_text(result, encoding="utf-8")

    return inserted


def find_vault_root(start):
    candidate = start
    for _ in range(12):
        candidate = candidate.parent
        if (candidate / "1-SOURCES").is_dir():
            return candidate
    raise RuntimeError("Could not locate vault root (no 1-SOURCES/ ancestor)")


def main():
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("translation", help="Path to the translation file")
    parser.add_argument("--root", default=None, help="Path to the root text file")
    parser.add_argument("--dry-run", action="store_true",
                        help="Print result to stdout, do not write")
    args = parser.parse_args()

    translation_path = Path(args.translation).resolve()
    if not translation_path.exists():
        sys.exit("Error: translation file not found: " + str(translation_path))

    try:
        vault_root = find_vault_root(translation_path)
    except RuntimeError as e:
        sys.exit("Error: " + str(e))

    if args.root:
        root_path = Path(args.root).resolve()
    else:
        content = translation_path.read_text(encoding="utf-8")
        fm = re.search(r"^root_text:\s*(.+)$", content, re.MULTILINE)
        if fm:
            root_path = (vault_root / fm.group(1).strip()).resolve()
        else:
            root_path = (vault_root / "1-SOURCES/Text/BCAV08_SH_sk.md").resolve()

    if not root_path.exists():
        sys.exit("Error: root text not found: " + str(root_path))

    print("Root text  : " + str(root_path.relative_to(vault_root)), file=sys.stderr)
    print("Translation: " + str(translation_path.relative_to(vault_root)), file=sys.stderr)

    root_ids = collect_root_ids(root_path)
    print("Root IDs   : " + str(len(root_ids)), file=sys.stderr)

    count = insert_transclusions(
        translation_path, root_path, root_ids, vault_root, args.dry_run
    )
    verb = "Would insert" if args.dry_run else "Inserted"
    print(verb + " " + str(count) + " transclusion(s).", file=sys.stderr)


if __name__ == "__main__":
    main()
