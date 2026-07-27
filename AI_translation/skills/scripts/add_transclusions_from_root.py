#!/usr/bin/env python3
"""
add_transclusions_from_root.py
==============================

Insert Obsidian-style root-text transclusion lines into a translated file,
derived directly from the root text's own block IDs — no intermediary
"already-transcluded" file required.

For every block ID found in the root text (e.g. ``^1-1``, ``^6-33``), this
script inserts the line::

    ![[<root_text_vault_path>#^<id>]]

immediately before the block in the translated file whose last line carries
that same segment ID.  Verse-heading IDs (anything ending in ``-0``), the
document title ID (``^0``), and intro IDs (``^I-*``) are skipped by default
because transclusing headings is rarely useful — see ``--include-headings``.

The vault path written into the ``![[...]]`` is derived automatically from
``--vault-root`` and ``--root-text``:

    vault_path = relative_path(root_text, vault_root)

This means you do **not** need to hard-code the path — just pass the absolute
(or CWD-relative) paths and the script handles the rest.

Algorithm
---------
1. Parse the root text into blocks (same algorithm as ``add_transclusions.py``).
2. Collect every segment ID from the root text → build the set of IDs to
   transclude (filtering heading / intro IDs unless ``--include-headings``).
3. Parse the translated file into blocks.
4. Walk the translated file's blocks:
   a. If a block already starts with a transclusion line, strip it (idempotent).
   b. If the block's segment ID is in the root-text ID set, prepend the
      appropriate ``![[...#^id]]`` block.
5. Rejoin and write/print the result.

Diagnostics (written to stderr, never stdout)
---------------------------------------------
* How many transclusion lines were inserted.
* Segment IDs in the translated file that are NOT in the root text
  ("extra" IDs — possible typos or additions).
* Root-text IDs that are NOT in the translated file ("missing" IDs — verses
  that were dropped or renamed in the translation).

Usage
-----
::

    python add_transclusions_from_root.py \\
        --root-text    "1-SOURCES/Text/BCAV08_SH_sk.md" \\
        --translated   "AI_translation/marathi/bca-marathi-scholars.md" \\
        [--vault-root  "/path/to/vault"]   # defaults to CWD \\
        [--output PATH | --in-place]       # defaults to stdout \\
        [--include-headings]               # also transclude ^N-0 / ^I-* IDs \\
        [--skip-pattern REGEX]             # additional IDs to skip (repeatable)

Options
-------
``--root-text PATH``
    Path to the root text file (the authoritative segment-ID source).
    Required.

``--translated PATH``
    Path to the translated file to modify.  Required.

``--vault-root PATH``
    Root of the Obsidian vault; used to compute the vault-relative path that
    appears inside ``![[...]]``.  Defaults to the current working directory.

``--output PATH``
    Write the result to PATH.  Mutually exclusive with ``--in-place``.

``--in-place``
    Overwrite the translated file with the result.  Mutually exclusive with
    ``--output``.

``--include-headings``
    Also generate transclusion lines for heading / intro IDs (``^0``,
    ``^I-*``, ``^*-0``).  Off by default.

``--skip-pattern REGEX``
    Additional regex pattern(s) for segment IDs to skip (matched against the
    raw ID string, e.g. ``"^a-"`` to skip author-colophon IDs).  Repeatable.

Examples
--------
::

    # Dry-run (print to stdout)
    python add_transclusions_from_root.py \\
        --root-text "1-SOURCES/Text/BCAV08_SH_sk.md" \\
        --translated "AI_translation/marathi/bca-marathi-scholars.md"

    # Overwrite in place
    python add_transclusions_from_root.py \\
        --root-text "1-SOURCES/Text/BCAV08_SH_sk.md" \\
        --translated "AI_translation/marathi/bca-marathi-scholars.md" \\
        --vault-root "/Users/me/repos/bodhisattvacharyavatara-rails" \\
        --in-place

    # Also add transclusions for children's translation
    python add_transclusions_from_root.py \\
        --root-text "1-SOURCES/Text/BCAV08_SH_sk.md" \\
        --translated "AI_translation/marathi/bca-marathi-children.md" \\
        --in-place
"""

import argparse
import re
import sys
from pathlib import Path

# ---------------------------------------------------------------------------
# Regex constants
# ---------------------------------------------------------------------------

# Matches any Obsidian transclusion line: ![[...]]
TRANSCLUSION_RE = re.compile(r"^\s*!\[\[.*\]\]\s*$")

# Matches a bare block/segment ID anywhere in a line: ^word-word ...
# Excludes transclusion lines (which contain ^id *inside* [[...]]).
SEGMENT_ID_RE = re.compile(r"\^([\w][\w\-]*)")

# Heading IDs: ^0 (title), ^I-anything (intro), ^N-0 (chapter heading),
# ^N-N-0 (section heading), ^N-N-N-0 (subsection heading).
# Pattern: ends with "-0" or is exactly "0", or starts with "I-".
_HEADING_ID_RE = re.compile(r"^(0|I-.+|\d.*-0)$")


# ---------------------------------------------------------------------------
# Core utilities (shared with add_transclusions.py)
# ---------------------------------------------------------------------------

def line_segment_id(line: str) -> "str | None":
    """Return the last segment ID found in *line*, or None.

    Transclusion lines are excluded even though they contain ``^id``
    inside the ``[[...]]`` — those are references, not segment markers.
    """
    if TRANSCLUSION_RE.match(line):
        return None
    matches = SEGMENT_ID_RE.findall(line)
    return matches[-1] if matches else None


def split_into_blocks(text: str) -> "list[list[str]]":
    """Split *text* into blocks.

    A block ends at a blank line **or** at the first line carrying a
    segment ID, whichever comes first.  This handles the edge case of
    colophon lines running straight into the next chapter heading with no
    blank line between them.
    """
    blocks: list[list[str]] = []
    current: list[str] = []
    for line in text.split("\n"):
        if line.strip() == "":
            if current:
                blocks.append(current)
                current = []
            continue
        current.append(line)
        if line_segment_id(line) is not None:
            blocks.append(current)
            current = []
    if current:
        blocks.append(current)
    return blocks


def block_segment_id(block: "list[str]") -> "str | None":
    """Return the segment ID from the last line of *block*, or None."""
    return line_segment_id(block[-1]) if block else None


def strip_leading_transclusion(block: "list[str]") -> "list[str]":
    """Drop the first line of *block* if it is a transclusion line."""
    if block and TRANSCLUSION_RE.match(block[0]):
        return block[1:]
    return block


# ---------------------------------------------------------------------------
# Root-text ID extraction
# ---------------------------------------------------------------------------

def collect_root_ids(
    root_blocks: "list[list[str]]",
    include_headings: bool,
    skip_patterns: "list[re.Pattern]",
) -> "dict[str, None]":
    """Return an ordered dict (preserving encounter order) of every segment
    ID found in the root text, after applying heading / skip filters.

    Using ``dict[str, None]`` rather than ``set`` preserves insertion order
    for deterministic output on Python 3.7+.
    """
    ids: dict[str, None] = {}
    for block in root_blocks:
        seg_id = block_segment_id(block)
        if seg_id is None:
            continue
        if not include_headings and _HEADING_ID_RE.match(seg_id):
            continue
        if any(p.search(seg_id) for p in skip_patterns):
            continue
        ids[seg_id] = None
    return ids


# ---------------------------------------------------------------------------
# Transclusion line builder
# ---------------------------------------------------------------------------

def make_transclusion_line(vault_path: str, seg_id: str) -> str:
    """Return the Obsidian transclusion string for *seg_id* in *vault_path*."""
    # Obsidian uses forward slashes regardless of OS
    clean_path = vault_path.replace("\\", "/")
    return f"![[{clean_path}#^{seg_id}]]"


# ---------------------------------------------------------------------------
# Main processing
# ---------------------------------------------------------------------------

def process(
    root_text: str,
    translated_text: str,
    vault_path: str,
    include_headings: bool,
    skip_patterns: "list[re.Pattern]",
) -> "tuple[str, dict]":
    """Return ``(output_text, stats)`` where *stats* holds diagnostic counts."""
    root_blocks = split_into_blocks(root_text)
    translated_blocks = split_into_blocks(translated_text)

    root_ids = collect_root_ids(root_blocks, include_headings, skip_patterns)

    translated_ids: dict[str, None] = {}
    for b in translated_blocks:
        sid = block_segment_id(b)
        if sid is not None:
            translated_ids[sid] = None

    result_blocks: list[list[str]] = []
    inserted = 0
    extra_ids: list[str] = []  # in translated but not in root
    for block in translated_blocks:
        block = strip_leading_transclusion(block)
        seg_id = block_segment_id(block)
        if seg_id is not None:
            if seg_id in root_ids:
                transclusion_line = make_transclusion_line(vault_path, seg_id)
                result_blocks.append([transclusion_line])
                inserted += 1
            else:
                # Check whether it was intentionally skipped (heading/skip)
                # rather than truly extra.
                is_heading = _HEADING_ID_RE.match(seg_id)
                is_skipped = any(p.search(seg_id) for p in skip_patterns)
                if not is_heading and not is_skipped:
                    extra_ids.append(seg_id)
        result_blocks.append(block)

    missing_ids = [sid for sid in root_ids if sid not in translated_ids]

    output_text = "\n\n".join("\n".join(b) for b in result_blocks) + "\n"

    stats = {
        "inserted": inserted,
        "extra_ids": extra_ids,
        "missing_ids": missing_ids,
    }
    return output_text, stats


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    p.add_argument(
        "--root-text",
        required=True,
        metavar="PATH",
        help="Path to the root text file (e.g. 1-SOURCES/Text/BCAV08_SH_sk.md).",
    )
    p.add_argument(
        "--translated",
        required=True,
        metavar="PATH",
        help="Path to the translated file to process.",
    )
    p.add_argument(
        "--vault-root",
        default=None,
        metavar="PATH",
        help=(
            "Root of the Obsidian vault; used to compute the vault-relative "
            "path inside ![[...]].  Defaults to the current working directory."
        ),
    )
    p.add_argument(
        "-o", "--output",
        default=None,
        metavar="PATH",
        help="Write output to PATH.  Mutually exclusive with --in-place.",
    )
    p.add_argument(
        "--in-place",
        action="store_true",
        help="Overwrite the translated file.  Mutually exclusive with --output.",
    )
    p.add_argument(
        "--include-headings",
        action="store_true",
        help=(
            "Also generate transclusion lines for heading IDs "
            "(^0, ^I-*, ^*-0).  Off by default."
        ),
    )
    p.add_argument(
        "--skip-pattern",
        action="append",
        default=[],
        metavar="REGEX",
        dest="skip_patterns",
        help=(
            "Regex matched against segment ID strings to skip additional "
            "IDs (e.g. '^a-' skips author-colophon IDs).  Repeatable."
        ),
    )
    return p


def main() -> None:
    args = build_parser().parse_args()

    if args.output and args.in_place:
        print(
            "Error: --output and --in-place are mutually exclusive.",
            file=sys.stderr,
        )
        sys.exit(1)

    root_path = Path(args.root_text)
    translated_path = Path(args.translated)
    vault_root = Path(args.vault_root) if args.vault_root else Path.cwd()

    if not root_path.exists():
        print(f"Error: root text not found: {root_path}", file=sys.stderr)
        sys.exit(1)
    if not translated_path.exists():
        print(f"Error: translated file not found: {translated_path}", file=sys.stderr)
        sys.exit(1)

    # Compute vault-relative path for use inside ![[...]]
    try:
        vault_rel_path = str(root_path.resolve().relative_to(vault_root.resolve()))
    except ValueError:
        # root_text is outside vault_root — use the path as given
        vault_rel_path = str(root_path)

    skip_patterns = [re.compile(p) for p in args.skip_patterns]

    root_text = root_path.read_text(encoding="utf-8")
    translated_text = translated_path.read_text(encoding="utf-8")

    output_text, stats = process(
        root_text=root_text,
        translated_text=translated_text,
        vault_path=vault_rel_path,
        include_headings=args.include_headings,
        skip_patterns=skip_patterns,
    )

    # Diagnostics → stderr (never stdout, so stdout stays pipeable)
    print(f"Inserted {stats['inserted']} transclusion line(s).", file=sys.stderr)
    if stats["extra_ids"]:
        print(
            f"WARNING: {len(stats['extra_ids'])} ID(s) in translated file are "
            f"NOT in root text (possible typos/additions): {stats['extra_ids']}",
            file=sys.stderr,
        )
    if stats["missing_ids"]:
        print(
            f"WARNING: {len(stats['missing_ids'])} root-text ID(s) are MISSING "
            f"from translated file (dropped/renamed verses): {stats['missing_ids']}",
            file=sys.stderr,
        )

    if args.in_place:
        translated_path.write_text(output_text, encoding="utf-8")
        print(f"Wrote in place: {translated_path}", file=sys.stderr)
    elif args.output:
        out = Path(args.output)
        out.write_text(output_text, encoding="utf-8")
        print(f"Wrote: {out}", file=sys.stderr)
    else:
        sys.stdout.buffer.write(output_text.encode("utf-8"))


if __name__ == "__main__":
    main()
