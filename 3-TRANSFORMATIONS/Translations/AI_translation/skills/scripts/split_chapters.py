#!/usr/bin/env python3
"""
split_chapters.py

Split a single source file into multiple files by explicit cut points.
The caller specifies exactly where each section starts and what to name
it -- this script just finds those start markers and cuts the file
between them. No heading-level guessing, no keyword matching.

Usage:
    python split_chapters.py <source_file> [output_dir] \\
        --section "MARKER_TEXT::output_name.md" \\
        --section "MARKER_TEXT_2::output_name_2.md" \\
        ...

    Each --section gives:
      - MARKER_TEXT: a literal substring (or regex, with --regex) that
        identifies the line where that section begins. The first line
        at or after the previous cut point that contains this marker is
        used as the start of the section.
      - output_name.md: the file to write that section's content to.

    Sections must be given in the order they appear in the source file.
    Each section runs from its marker line up to (but not including) the
    next section's marker line, or to the end of the file for the last
    section.

    Content before the first marker (if any) is discarded unless
    --keep-preamble is given, in which case it's written to
    preamble.md.

    Multiple --section entries can share the same output_name -- useful
    for small trailing sections (e.g. a composer's colophon and a
    translators' colophon) that should end up combined in one file
    rather than split across several tiny ones. The first section using
    a given name starts the file; every later section with that same
    name is appended to it (separated by a blank line), in the order
    given.

Where output goes:
    Either way, the script always creates a subfolder named
    "<source_file_stem>_split_chapters" and writes the split files
    inside it -- it never dumps loose files directly into an existing
    folder.
      - No output_dir given: that subfolder is created right next to the
        source file (i.e. in the source file's own directory).
        E.g. splitting "1-SOURCES/source.md" produces
        "1-SOURCES/source_split_chapters/ch1.md", etc.
      - output_dir given (relative or absolute): that same subfolder is
        created inside the given directory instead.
        E.g. splitting "1-SOURCES/source.md" with output_dir
        "AI_translation" produces
        "AI_translation/source_split_chapters/ch1.md", etc.

Options:
    --regex               Treat each MARKER_TEXT as a regular expression
                           instead of a plain substring.
    --keep-preamble        Write any content before the first marker to
                           preamble.md in the output dir (default: discard).
    --strip-frontmatter    If the file starts with a YAML frontmatter block
                           (delimited by "---" ... "---"), strip it out and
                           save it to frontmatter.txt, before applying the
                           cuts below.
    --keep-transclusions   By default, Obsidian-style transclusion lines
                           (e.g. "![[1-SOURCES/Text/BCAV08_SH_sk.md#^2-9]]")
                           are removed from every output section, since
                           they're references, not translatable content.
                           Pass this flag to keep them instead.

Example (default output location, combined colophon):
    python split_chapters.py "1-SOURCES/source.md" \\
        --strip-frontmatter \\
        --section "## 0. Introduction::intro.md" \\
        --section "## 1.::ch1.md" \\
        --section "## 2.::ch2.md" \\
        --section "## Composer's colophon::colophon.md" \\
        --section "## Translators' colophon::colophon.md"
    # writes to "1-SOURCES/source_split_chapters/" -- both colophon
    # sections end up combined in one colophon.md, in order.

Example (explicit output location):
    python split_chapters.py "1-SOURCES/source.md" "AI translation/tib_chapter_keywords" \\
        --section "## 1.::ch1.md" \\
        --section "## 2.::ch2.md"
    # writes to "AI translation/tib_chapter_keywords/"
"""

import argparse
import re
import sys
from pathlib import Path


def strip_frontmatter(text):
    """Return (frontmatter_or_None, remaining_text)."""
    stripped = text.lstrip("\n")
    if not stripped.startswith("---"):
        return None, text
    lines = stripped.split("\n")
    if lines[0].strip() != "---":
        return None, text
    for i in range(1, len(lines)):
        if lines[i].strip() == "---":
            frontmatter = "\n".join(lines[0:i + 1])
            remaining = "\n".join(lines[i + 1:])
            return frontmatter, remaining
    return None, text


TRANSCLUSION_PATTERN = re.compile(r"^\s*!\[\[.*\]\]\s*$")


def strip_transclusion_lines(text):
    """Remove Obsidian-style transclusion lines (e.g. ![[file#^id]])."""
    kept = [ln for ln in text.split("\n") if not TRANSCLUSION_PATTERN.match(ln)]
    return "\n".join(kept)


def find_marker_line(lines, start_idx, marker, use_regex):
    """Find the index of the first line at/after start_idx matching marker."""
    if use_regex:
        pattern = re.compile(marker)
        test = lambda line: pattern.search(line) is not None
    else:
        test = lambda line: marker in line

    for i in range(start_idx, len(lines)):
        if test(lines[i]):
            return i
    return None


def parse_section_arg(arg):
    if "::" not in arg:
        print(f"Error: --section value must be 'MARKER::output_name.md', got: {arg!r}", file=sys.stderr)
        sys.exit(1)
    marker, output_name = arg.split("::", 1)
    if not marker or not output_name:
        print(f"Error: empty marker or output name in --section value: {arg!r}", file=sys.stderr)
        sys.exit(1)
    return marker, output_name


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("source_file")
    ap.add_argument("output_dir", nargs="?", default=None,
                     help="Optional. Defaults to '<source_stem>_split_chapters' next to the source file.")
    ap.add_argument("--section", action="append", default=[], required=True,
                     help="MARKER::output_name.md -- repeatable, in file order")
    ap.add_argument("--regex", action="store_true")
    ap.add_argument("--keep-preamble", action="store_true")
    ap.add_argument("--strip-frontmatter", action="store_true")
    ap.add_argument("--keep-transclusions", action="store_true")
    args = ap.parse_args()

    src_path = Path(args.source_file)

    if args.output_dir:
        base_dir = Path(args.output_dir)
    else:
        base_dir = src_path.parent

    out_dir = base_dir / f"{src_path.stem}_split_chapters"
    print(f"Writing split files to: {out_dir}")

    out_dir.mkdir(parents=True, exist_ok=True)

    text = src_path.read_text(encoding="utf-8")

    if args.strip_frontmatter:
        frontmatter, text = strip_frontmatter(text)
        if frontmatter:
            (out_dir / "frontmatter.txt").write_text(frontmatter + "\n", encoding="utf-8")
            print(f"Wrote frontmatter.txt ({len(frontmatter.splitlines())} lines)")

    lines = text.split("\n")
    sections = [parse_section_arg(a) for a in args.section]

    # Locate each marker's line index, in order, searching forward from
    # the previous marker's position so repeated/similar text earlier in
    # the file doesn't get matched twice.
    marker_positions = []
    search_from = 0
    for marker, output_name in sections:
        idx = find_marker_line(lines, search_from, marker, args.regex)
        if idx is None:
            print(f"Error: marker not found (searching from line {search_from + 1}): {marker!r}", file=sys.stderr)
            print("Check that --section markers are listed in the same order they appear in the source file.", file=sys.stderr)
            sys.exit(1)
        marker_positions.append(idx)
        search_from = idx + 1

    if args.keep_preamble and marker_positions[0] > 0:
        preamble = "\n".join(lines[0:marker_positions[0]])
        if not args.keep_transclusions:
            preamble = strip_transclusion_lines(preamble)
        if preamble.strip():
            (out_dir / "preamble.md").write_text(preamble.strip() + "\n", encoding="utf-8")
            print("Wrote preamble.md")

    written = []
    seen_names = set()
    for i, (marker, output_name) in enumerate(sections):
        start = marker_positions[i]
        end = marker_positions[i + 1] if i + 1 < len(marker_positions) else len(lines)
        section_text = "\n".join(lines[start:end])
        if not args.keep_transclusions:
            section_text = strip_transclusion_lines(section_text)
        section_text = section_text.strip() + "\n"
        out_path = out_dir / output_name

        if output_name in seen_names:
            with out_path.open("a", encoding="utf-8") as f:
                f.write("\n" + section_text)
            action = "appended to"
        else:
            out_path.write_text(section_text, encoding="utf-8")
            seen_names.add(output_name)
            action = "wrote"

        written.append(output_name)
        print(f"  {action} {output_name}: lines {start + 1}-{end} (marker: {marker!r})")

    print(f"\nWrote {len(seen_names)} file(s) to {out_dir} ({len(written)} section(s) total)")


if __name__ == "__main__":
    main()
