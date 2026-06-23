#!/usr/bin/env python3
"""
segment_table_to_commentary.py
================================
Converts Monlam/Pecha segment-table Markdown files into formatted
1-SOURCES commentary files for the Railroads vault.

INPUT FORMAT: markdown table with | segment_number | segment_id | content | tags |

OUTPUT FORMAT:
  - YAML frontmatter (draft status; fill in author/registered_id after)
  - Segment content preserved verbatim - no whitespace reshaping at all.
    Each segment is written exactly as it appears in the table cell, one
    segment per line. A no-loss check before writing asserts every
    non-whitespace character is preserved.
  - Empty-content segments are skipped entirely
  - No block IDs, no inserted headings, no title heading - pure original text
  - Output written to 0-INBOX/temp/ for review before moving to 1-SOURCES/

USAGE:
  python3 segment_table_to_commentary.py path/to/file.md
  python3 segment_table_to_commentary.py file1.md file2.md
  python3 segment_table_to_commentary.py path/to/folder/
  python3 segment_table_to_commentary.py path/to/folder/ --recursive
  python3 segment_table_to_commentary.py file.md --outdir path/to/output/
"""

import argparse
import pathlib
import re
import sys


def squeeze(s):
    """Collapse all whitespace (spaces, tabs, newlines) out of a string,
    leaving only non-whitespace characters - used to verify no body text
    was lost when assembling segment content."""
    return re.sub(r"\s+", "", s)


def parse_segment_table(path):
    raw = path.read_bytes().rstrip(b"\x00").decode("utf-8")
    rows = []
    text_id = ""
    for line in raw.splitlines():
        if text_id == "" and "text_id" in line:
            m = re.search(r'`([0-9a-f-]{36})`', line)
            if m:
                text_id = m.group(1)
        if not line.startswith("|"):
            continue
        parts = [p.strip() for p in line.split("|")]
        if len(parts) < 5:
            continue
        seg_num_str = parts[1]
        seg_id_raw  = parts[2]
        content     = parts[3]
        if seg_num_str in ("segment_number", "---", "", " ") or not seg_num_str.isdigit():
            continue
        seg_num = int(seg_num_str)
        seg_id  = seg_id_raw.strip("`")
        rows.append((seg_num, seg_id, content))
    return text_id, rows


def extract_title_from_filename(path):
    stem = path.stem
    if re.match(r'^[a-z]{2}-', stem):
        stem = stem[3:]
    return stem


def make_output_filename(input_path):
    return input_path.stem + ".md"


def build_frontmatter(title, text_id, input_filename, total_segments):
    return (
        "---\n"
        "title: " + title + "\n"
        'title_in_english: "[FILL IN]"\n'
        'author: "[FILL IN - check colophon near end of file]"\n'
        'author_in_english: "[FILL IN]"\n'
        'registered_id: "[FILL IN - add to 4-SYSTEM/Guidelines/vault-annex.md]"\n'
        "file_type: commentary\n"
        "language_tag: bo\n"
        "root_text: 1-SOURCES/Text/sk-dev-root-text.md\n"
        'covers_verses: "[FILL IN e.g. 1-1-10-58]"\n'
        "source_description: >\n"
        "  Digital segment export (text_id " + text_id + "),\n"
        "  " + str(total_segments) + " segments. Converted from 0-INBOX/" + input_filename + "\n"
        "status: draft\n"
        "verse_id_format: chapter-verse\n"
        "---\n"
    )


def convert_file(input_path, output_dir, overwrite=False, dry_run=False):
    print("\n-> Processing: " + input_path.name)
    text_id, rows = parse_segment_table(input_path)
    if not rows:
        print("  x No segments found -- skipping.")
        return None
    print("  Parsed " + str(len(rows)) + " segments. text_id=" + (text_id or "(not found)"))
    out_filename = make_output_filename(input_path)
    out_path = output_dir / out_filename
    if out_path.exists() and not overwrite:
        print("  x Output already exists: " + str(out_path) + " (use --overwrite to replace)")
        return None
    if dry_run:
        print("  [dry-run] Would write -> " + str(out_path))
        return out_path
    title = extract_title_from_filename(input_path)
    frontmatter = build_frontmatter(title, text_id, input_path.name, len(rows))

    segments = []
    non_empty = 0
    for seg_num, seg_id, content in rows:
        if content.strip():
            # Preserve segment content verbatim, one segment per line.
            segments.append(content)
            non_empty += 1
        # Empty-content segments are dropped entirely
    body_text = "\n".join(segments)
    output_text = frontmatter + body_text + "\n"

    # No-loss guard: every non-whitespace character from the non-empty
    # segments must still be present in the output body.
    expected = squeeze("".join(c for _, _, c in rows if c.strip()))
    if squeeze(body_text) != expected:
        print("  x ABORT: body text altered. No file written.", file=sys.stderr)
        return None

    output_dir.mkdir(parents=True, exist_ok=True)
    out_path.write_bytes(output_text.encode("utf-8"))
    empty = len(rows) - non_empty
    kb = len(output_text.encode("utf-8")) / 1024
    print("  Written -> " + str(out_path) + "  ("
          + str(round(kb)) + " KB, " + str(non_empty) + " paragraphs, "
          + str(empty) + " empty segments dropped)")
    return out_path


def find_vault_root(start):
    p = start.resolve()
    for _ in range(10):
        if (p / "CLAUDE.md").exists() or (p / "4-SYSTEM").is_dir():
            return p
        p = p.parent
    return None


def collect_input_files(paths, recursive=False):
    result = []
    for p_str in paths:
        p = pathlib.Path(p_str).resolve()
        if p.is_dir():
            found = sorted(p.rglob("*.md") if recursive else p.glob("*.md"))
            scope = "recursively" if recursive else "(top level)"
            print("  Found " + str(len(found)) + " .md files " + scope + " in " + str(p))
            result.extend(found)
        elif p.is_file():
            result.append(p)
        else:
            print("  Warning: '" + p_str + "' not found -- skipping", file=sys.stderr)
    return result


def main():
    parser = argparse.ArgumentParser(
        description="Convert segment-table .md files to 1-SOURCES commentary files."
    )
    parser.add_argument("inputs", nargs="+")
    parser.add_argument("--outdir", default=None)
    parser.add_argument("--overwrite", action="store_true")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("-r", "--recursive", action="store_true",
                        help="Recurse into subfolders when a folder is given.")
    args = parser.parse_args()

    input_files = collect_input_files(args.inputs, recursive=args.recursive)
    if not input_files:
        print("No input files found.", file=sys.stderr)
        sys.exit(1)

    if args.outdir:
        output_dir = pathlib.Path(args.outdir).resolve()
    else:
        vault = find_vault_root(input_files[0])
        output_dir = vault / "0-INBOX" / "temp" if vault else input_files[0].parent / "temp"
        print("Output directory: " + str(output_dir))

    succeeded, skipped = [], []
    for f in input_files:
        result = convert_file(f, output_dir, overwrite=args.overwrite, dry_run=args.dry_run)
        if result:
            succeeded.append(result)
        else:
            skipped.append(f)

    print("\n" + "=" * 60)
    print("Done.  Converted: " + str(len(succeeded)) + "  Skipped: " + str(len(skipped)))
    if succeeded:
        print("\nNext steps:")
        print("  1. Fill in [FILL IN] frontmatter (author, registered_id, covers_verses)")
        print("  2. Check colophon (~last 20 segments) for author name")
        print("  3. Move file to 1-SOURCES/Commentaries/")
        print("  4. Add registered_id to 4-SYSTEM/Guidelines/vault-annex.md (human only)")


if __name__ == "__main__":
    main()
