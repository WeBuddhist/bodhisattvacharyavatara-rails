#!/usr/bin/env python3
"""Align root-text and translation files by Obsidian block ID.

Reads two markdown files that share an Obsidian block-ID scheme (``^<id>`` at
the end of a paragraph) and emits a CSV with one row per block ID, paired
source and target text. Block IDs present in only one file are emitted with
an empty cell on the missing side and flagged in ``notes``.

Usage:

    python3 align_blocks.py <root-text>.md <translation>.md <output>.csv

The CSV has four columns: ``block_id``, ``source_text``, ``target_text``,
``notes``. It is intended as the working table for the
``glossary-extract-raw`` skill.
"""
from __future__ import annotations

import csv
import re
import sys
from pathlib import Path


# Match a block at the end of a paragraph: ``... text. ^1-0a-1``.
# We split paragraphs on blank lines, then look at the last token of each
# paragraph for a ``^<id>`` marker.
BLOCK_ID_RE = re.compile(r"\^([0-9A-Za-z][0-9A-Za-z\-]*)\s*$")
# Strip Obsidian heading hashes when capturing block text.
HEADING_RE = re.compile(r"^#{1,6}\s")


def parse_blocks(path: Path) -> dict[str, str]:
    """Return {block_id: paragraph_text_without_id} for ``path``.

    Headings (#, ##, ...) are skipped — they may have their own IDs but they
    are not translation-block content. Frontmatter is also skipped.
    """
    text = path.read_text(encoding="utf-8")
    # Strip frontmatter if present.
    if text.startswith("---\n"):
        end = text.find("\n---", 4)
        if end != -1:
            text = text[end + 4 :]

    blocks: dict[str, str] = {}
    for paragraph in re.split(r"\n\s*\n", text):
        paragraph = paragraph.strip()
        if not paragraph:
            continue
        if HEADING_RE.match(paragraph):
            continue
        # Look for ^<id> at the end of the paragraph.
        match = BLOCK_ID_RE.search(paragraph)
        if not match:
            continue
        block_id = match.group(1)
        body = paragraph[: match.start()].rstrip()
        blocks[block_id] = body
    return blocks


def align(
    source_path: Path, target_path: Path, output_path: Path
) -> tuple[int, int, int]:
    """Write the aligned CSV. Return (paired, source_only, target_only)."""
    source_blocks = parse_blocks(source_path)
    target_blocks = parse_blocks(target_path)

    all_ids = sorted(set(source_blocks) | set(target_blocks), key=_sort_key)

    paired = source_only = target_only = 0
    with output_path.open("w", encoding="utf-8", newline="") as fh:
        writer = csv.writer(fh)
        writer.writerow(["block_id", "source_text", "target_text", "notes"])
        for block_id in all_ids:
            src = source_blocks.get(block_id, "")
            tgt = target_blocks.get(block_id, "")
            if src and tgt:
                notes = ""
                paired += 1
            elif src and not tgt:
                notes = "target-only-missing"
                source_only += 1
            else:
                notes = "source-only-missing"
                target_only += 1
            writer.writerow([block_id, src, tgt, notes])

    return paired, source_only, target_only


def _sort_key(block_id: str) -> tuple:
    """Sort block IDs numerically where the segments are numeric."""
    parts = []
    for segment in block_id.split("-"):
        try:
            parts.append((0, int(segment)))
        except ValueError:
            parts.append((1, segment))
    return tuple(parts)


def main(argv: list[str]) -> int:
    if len(argv) != 4:
        print(__doc__, file=sys.stderr)
        return 2
    source_path = Path(argv[1])
    target_path = Path(argv[2])
    output_path = Path(argv[3])
    output_path.parent.mkdir(parents=True, exist_ok=True)
    paired, source_only, target_only = align(source_path, target_path, output_path)
    print(
        f"Wrote {output_path}: paired={paired} "
        f"source-only={source_only} target-only={target_only}"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
