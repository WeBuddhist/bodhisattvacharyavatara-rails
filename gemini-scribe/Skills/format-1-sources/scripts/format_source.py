#!/usr/bin/env python3
"""
format_source.py -- Mechanical formatting helper for 1-SOURCES/ files.

Usage:
  python scripts/format_source.py --audit /path/to/1-SOURCES/
  python scripts/format_source.py --file path/to/file.md [--add-block-ids] [--clean-line-numbers] [--fix-line-breaks] [--dry-run]
  python scripts/format_source.py --verify path/to/file.md
"""

import re
import sys
import argparse
from pathlib import Path


# -- Devanagari digit mapping -------------------------------------------------
DEVA_DIGITS = str.maketrans("01234567890123456789", "01234567890123456789")
DEVA_MAP = str.maketrans("०१२३४५६७८९",
                          "0123456789")

def deva_to_arabic(s: str) -> str:
    return s.translate(DEVA_MAP)


# -- Detect file language from content and filename --------------------------

def detect_lang(path: Path, content: str) -> str:
    """Return 'sk', 'bo', 'zh', or 'unknown'."""
    name = path.name
    if name.startswith("sk-") or re.search(r"[ऀ-ॿ]", content[:500]):
        return "sk"
    if name.startswith("bo-") or re.search(r"[ༀ-࿿]", content[:500]):
        return "bo"
    if re.search(r"[一-鿿]", content[:500]):
        return "zh"
    return "unknown"


def has_frontmatter(content: str) -> bool:
    return content.lstrip().startswith("---")


# -- Chapter tracking --------------------------------------------------------

CHAPTER_HEADING = re.compile(r"^##\s+(\d+)\b")

def current_chapter_from_headings(lines: list, line_idx: int) -> int:
    for i in range(line_idx, -1, -1):
        m = CHAPTER_HEADING.match(lines[i])
        if m:
            return int(m.group(1))
    return 0


# -- Block ID detection -------------------------------------------------------

BLOCK_ID_RE = re.compile(r"\^(\d+)-(\d+)\s*$")

def has_block_id(line: str) -> bool:
    return bool(BLOCK_ID_RE.search(line))


# -- Sanskrit processing -----------------------------------------------------

# Verse-closing numeral: \\N\\ (Devanagari or Arabic digits)
VERSE_END_SK = re.compile(r"॥([0-9०-९]+)॥\s*(?:\^[\d-]+)?\s*$")

# Stray line-number prefix: "7. " at start of line
STRAY_PREFIX_SK = re.compile(r"^\d+\.\s+")

# Hyphenated hemistichs
HYPHEN_BREAK = re.compile(r"(\S)-\s*([^\s])")


def process_sk(lines: list, add_block_ids: bool, clean_nums: bool,
               fix_breaks: bool) -> tuple:
    out = []
    notes = []

    for i, line in enumerate(lines):
        # 1. Remove stray line-number prefix
        if clean_nums:
            line = STRAY_PREFIX_SK.sub("", line)

        # 2. Add block ID first (before any line splitting, so the pattern is intact)
        if add_block_ids and not has_block_id(line):
            m = VERSE_END_SK.search(line)
            if m:
                verse_num = int(deva_to_arabic(m.group(1)))
                chapter = current_chapter_from_headings(lines, i)
                block_id = "^{}-{}".format(chapter, verse_num)
                line = line.rstrip() + " " + block_id

        # 3. Fix hyphenated hemistichs.
        #    Only apply when the text itself (before verse closer) contains a hyphen
        #    that looks like a PDF line-break artifact: word-break followed immediately
        #    by the next syllable with no space.
        if fix_breaks and VERSE_END_SK.search(line):
            end_m = VERSE_END_SK.search(line)
            bid_m = BLOCK_ID_RE.search(line)
            # Only examine the text BEFORE the verse closer to avoid matching ^N-M
            text_part = line[:end_m.start()] if end_m else line
            m = HYPHEN_BREAK.search(text_part)
            if m and len(text_part.strip()) > 80:
                # Rejoin the hyphen break in the text portion
                rejoined_text = text_part[:m.start()] + m.group(1) + m.group(2) + text_part[m.end():]
                text_only = rejoined_text.strip()
                mid = len(text_only) // 2
                split_at = text_only.rfind(" ", 0, mid + 20)
                if split_at < mid // 2:
                    split_at = text_only.find(" ", mid - 10)
                if split_at > 0:
                    first = text_only[:split_at].rstrip()
                    second = text_only[split_at:].lstrip()
                    # Rebuild suffix: verse closer + block ID
                    suffix = ""
                    if end_m:
                        suffix += "॥" + end_m.group(1) + "॥"
                    if bid_m:
                        suffix += " " + bid_m.group(0).strip()
                    line = first + "\n" + second + suffix

        out.append(line)

    return out, notes


# -- Tibetan processing -------------------------------------------------------

# A verse ends with double shad: [།] །
VERSE_END_BO = re.compile(r"། །\s*(?:\^[\d-]+)?\s*$")

# Bare separator line: only digits
BARE_NUM_LINE = re.compile(r"^\s*\d+\s*$")


def is_verse_end_bo(lines: list, i: int) -> bool:
    """Return True only if line i is the LAST hemistich of a Tibetan verse."""
    if not VERSE_END_BO.search(lines[i]):
        return False
    for j in range(i + 1, len(lines)):
        next_line = lines[j].strip()
        if not next_line:
            return True
        if BARE_NUM_LINE.match(lines[j]):
            return True
        if next_line.startswith("#"):
            return True
        # If next non-empty line also ends with shad, this is a mid-stanza hemistich
        if VERSE_END_BO.search(next_line):
            return False
        return True
    return True


def process_bo(lines: list, add_block_ids: bool, clean_nums: bool) -> tuple:
    out = []
    notes = []

    # Seed counter from existing block IDs to avoid duplicates
    verse_counter = {}
    for line in lines:
        m = BLOCK_ID_RE.search(line)
        if m:
            ch, vs = int(m.group(1)), int(m.group(2))
            verse_counter[ch] = max(verse_counter.get(ch, 0), vs)

    for i, line in enumerate(lines):
        # 1. Remove bare separator lines
        if clean_nums and BARE_NUM_LINE.match(line):
            out.append("")
            continue

        # 2. Add block ID only to the last hemistich of each verse
        if add_block_ids and not has_block_id(line) and is_verse_end_bo(lines, i):
            chapter = current_chapter_from_headings(lines, i)
            verse_counter.setdefault(chapter, 0)
            verse_counter[chapter] += 1
            block_id = "^{}-{}".format(chapter, verse_counter[chapter])
            line = line.rstrip() + " " + block_id

        out.append(line)

    return out, notes


# -- Chinese processing -------------------------------------------------------

STRAY_PREFIX_ZH = re.compile(r"^\d+\.\s*")


def process_zh(lines: list, add_block_ids: bool, clean_nums: bool) -> tuple:
    out = []
    notes = []

    # Seed counter from existing block IDs
    verse_counter = {}
    for line in lines:
        m = BLOCK_ID_RE.search(line)
        if m:
            ch, vs = int(m.group(1)), int(m.group(2))
            verse_counter[ch] = max(verse_counter.get(ch, 0), vs)

    for i, line in enumerate(lines):
        orig_stripped = line.strip()
        has_prefix = bool(STRAY_PREFIX_ZH.match(orig_stripped))

        if clean_nums and has_prefix:
            line = STRAY_PREFIX_ZH.sub("", orig_stripped)

        if add_block_ids and orig_stripped and has_prefix and not has_block_id(line):
            chapter = current_chapter_from_headings(lines, i)
            verse_counter.setdefault(chapter, 0)
            verse_counter[chapter] += 1
            block_id = "^{}-{}".format(chapter, verse_counter[chapter])
            line = line.rstrip() + " " + block_id

        out.append(line)

    return out, notes


# -- Commentary processing ----------------------------------------------------

def process_commentary(lines: list, clean_nums: bool) -> tuple:
    """Remove bare separator numbers. Block IDs require manual assignment."""
    out = []
    notes = ["NOTE: Block IDs for commentary files require manual assignment -- see SKILL.md Step 4."]
    for line in lines:
        if clean_nums and BARE_NUM_LINE.match(line):
            out.append("")
        else:
            out.append(line)
    return out, notes


# -- Audit -------------------------------------------------------------------

def audit_dir(sources_path: Path):
    md_files = sorted(sources_path.rglob("*.md"))
    if not md_files:
        print("No .md files found under", sources_path)
        return

    print("{:<55} {:>3} {:>6} {:>8} {:>7}".format(
        "File", "FM", "IDs", "Missing", "Stray#"))
    print("-" * 85)

    for path in md_files:
        content = path.read_text(encoding="utf-8")
        lines = content.splitlines()
        lang = detect_lang(path, content)
        fm = "yes" if has_frontmatter(content) else "no"
        id_count = sum(1 for l in lines if BLOCK_ID_RE.search(l))

        if lang == "sk":
            verse_lines = [l for l in lines if VERSE_END_SK.search(l)]
            missing = max(0, len(verse_lines) - id_count)
            stray = sum(1 for l in lines if STRAY_PREFIX_SK.match(l))
        elif lang == "bo":
            verse_lines = [l for l in lines if VERSE_END_BO.search(l) and is_verse_end_bo(lines, lines.index(l))]
            missing = max(0, len(verse_lines) - id_count)
            stray = sum(1 for l in lines if BARE_NUM_LINE.match(l))
        elif lang == "zh":
            stray = sum(1 for l in lines if l.strip() and STRAY_PREFIX_ZH.match(l.strip()))
            missing = stray
        else:
            missing = 0
            stray = sum(1 for l in lines if BARE_NUM_LINE.match(l))

        rel = path.relative_to(sources_path)
        print("{:<55} {:>3} {:>6} {:>8} {:>7}".format(
            str(rel), fm, id_count, missing, stray))


# -- Verify ------------------------------------------------------------------

def verify_file(path: Path):
    content = path.read_text(encoding="utf-8")
    lines = content.splitlines()
    errors = []

    if not has_frontmatter(content):
        errors.append("MISSING frontmatter")

    seen_ids = {}
    for i, line in enumerate(lines, 1):
        m = BLOCK_ID_RE.search(line)
        if m:
            bid = "^{}-{}".format(m.group(1), m.group(2))
            if bid in seen_ids:
                errors.append("DUPLICATE block ID {} at lines {} and {}".format(
                    bid, seen_ids[bid], i))
            seen_ids[bid] = i

    lang = detect_lang(path, content)
    stray_lines = []
    if lang == "sk":
        stray_lines = [i+1 for i, l in enumerate(lines) if STRAY_PREFIX_SK.match(l)]
    elif lang in ("bo", "unknown"):
        stray_lines = [i+1 for i, l in enumerate(lines) if BARE_NUM_LINE.match(l)]
    elif lang == "zh":
        stray_lines = [i+1 for i, l in enumerate(lines)
                       if l.strip() and STRAY_PREFIX_ZH.match(l.strip())]

    if stray_lines:
        sample = stray_lines[:10]
        suffix = "..." if len(stray_lines) > 10 else ""
        errors.append("STRAY line numbers at lines: {}{}".format(sample, suffix))

    bad_ids = []
    for i, line in enumerate(lines, 1):
        m = BLOCK_ID_RE.search(line)
        if m:
            ch, vs = m.group(1), m.group(2)
            if ch != ch.lstrip("0") or vs != vs.lstrip("0"):
                bad_ids.append("line {}: ^{}-{}".format(i, ch, vs))
    if bad_ids:
        errors.append("ZERO-PADDED block IDs: {}".format(bad_ids))

    if errors:
        print("ISSUES in {}:".format(path.name))
        for e in errors:
            print("  x {}".format(e))
    else:
        print("OK: {} looks good".format(path.name))


# -- Main --------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(description="Format 1-SOURCES files")
    parser.add_argument("--audit", metavar="DIR", help="Audit all .md files in DIR")
    parser.add_argument("--file", metavar="FILE", help="Process a single file")
    parser.add_argument("--verify", metavar="FILE", help="Verify a single file")
    parser.add_argument("--add-block-ids", action="store_true")
    parser.add_argument("--clean-line-numbers", action="store_true")
    parser.add_argument("--fix-line-breaks", action="store_true")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    if args.audit:
        audit_dir(Path(args.audit))
        return

    if args.verify:
        verify_file(Path(args.verify))
        return

    if not args.file:
        parser.print_help()
        sys.exit(1)

    path = Path(args.file)
    if not path.exists():
        print("Error: {} not found".format(path), file=sys.stderr)
        sys.exit(1)

    content = path.read_text(encoding="utf-8")
    bare_lines = content.splitlines()
    lang = detect_lang(path, content)
    print("File: {}  |  Detected language: {}".format(path.name, lang))

    notes = []
    if lang == "sk":
        out_lines, notes = process_sk(
            bare_lines,
            add_block_ids=args.add_block_ids,
            clean_nums=args.clean_line_numbers,
            fix_breaks=args.fix_line_breaks,
        )
    elif lang == "bo":
        out_lines, notes = process_bo(
            bare_lines,
            add_block_ids=args.add_block_ids,
            clean_nums=args.clean_line_numbers,
        )
    elif lang == "zh":
        out_lines, notes = process_zh(
            bare_lines,
            add_block_ids=args.add_block_ids,
            clean_nums=args.clean_line_numbers,
        )
    else:
        out_lines, notes = process_commentary(
            bare_lines,
            clean_nums=args.clean_line_numbers,
        )

    new_content = "\n".join(out_lines)
    if not new_content.endswith("\n"):
        new_content += "\n"

    orig_count = len(bare_lines)
    new_count = len(out_lines)
    changed = sum(1 for a, b in zip(bare_lines, out_lines) if a != b)
    added = new_count - orig_count
    print("Lines changed: {}  |  Lines added: {:+d}".format(changed, added))

    if args.dry_run:
        print("\n-- DRY RUN: first 40 changed lines --")
        shown = 0
        for i, (old, new) in enumerate(zip(bare_lines, out_lines)):
            if old != new and shown < 40:
                print("  [{}] - {!r}".format(i + 1, old))
                print("  [{}] + {!r}".format(i + 1, new))
                shown += 1
        if new_count > orig_count:
            print("  ... and {} new lines".format(new_count - orig_count))
        print("\nRun without --dry-run to apply.")
    else:
        path.write_text(new_content, encoding="utf-8")
        print("Written to {}".format(path))

    for note in notes:
        print(note)


if __name__ == "__main__":
    main()
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    