#!/usr/bin/env python3
"""
inject_toc.py - inject a TOC tree into a Tibetan commentary source file.

Reads a toc-tree-<id>.md produced by extract_toc_tree.py, adds Obsidian
^toc-N-N-N block IDs to every entry, then splices the TOC block into the
source commentary file.

Placement rules:
  - If an existing TOC block is present -> replace it in-place
  - Otherwise -> insert immediately after the YAML frontmatter closing ---
  - No frontmatter -> prepend to the file

Output goes to 0-INBOX/temp/toc-<input-filename> by default.
Override with --out.

Usage:
    python 4-SYSTEM/scripts/toc_tree_extractor/inject_toc.py \
        1-SOURCES/Commentaries/bo-kunpal.md \
        0-INBOX/toc-tree-kunpal.md

    # explicit output:
    python 4-SYSTEM/scripts/toc_tree_extractor/inject_toc.py \
        1-SOURCES/Commentaries/bo-kunpal.md \
        0-INBOX/toc-tree-kunpal.md \
        --out 0-INBOX/temp/toc-bo-kunpal.md
"""

import argparse
import re
import sys
from pathlib import Path

# ---------------------------------------------------------------------------
# Regexes
# ---------------------------------------------------------------------------
# Matches a TOC entry line at any depth, with optional trailing dot after decimal
_TOC_ENTRY_RE = re.compile(
    r"^(?P<indent>\s*)\*\s+(?P<dec>\d+(?:\.\d+)*)\.?\s+(?P<text>.+)$"
)
_FRONTMATTER_RE = re.compile(r"^---\s*$")
_TOC_HEADING_RE = re.compile(r"^\s*##\s+[^\n]*Table of Contents")
# Strip YAML frontmatter from the top of the tree file
_YAML_BLOCK_RE = re.compile(r"^---\n.*?^---\n", re.DOTALL | re.MULTILINE)


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------
def _add_block_ids(tree_body):
    """Append ^toc-N-N-N block IDs to every TOC entry line.

    Converts:  * 1.2.3 text
    Into:      * 1.2.3. text ^toc-1-2-3
    Strips any stale ^toc-... IDs before adding fresh ones.
    """
    out = []
    for line in tree_body.splitlines():
        m = _TOC_ENTRY_RE.match(line)
        if m:
            block_id = "^toc-" + m.group("dec").replace(".", "-")
            text = re.sub(r"\s*\^toc-[\d-]+$", "", m.group("text")).rstrip()
            line = m.group("indent") + "* " + m.group("dec") + ". " + text + " " + block_id
        out.append(line)
    return "\n".join(out)


def _strip_yaml_frontmatter(text):
    """Remove YAML frontmatter (--- ... ---) from the top of text."""
    return _YAML_BLOCK_RE.sub("", text, count=1).lstrip("\n")


def _build_toc_block(tree_body):
    """Return a ready-to-inject TOC block: heading + ID-tagged entries + --- rule."""
    # Strip any trailing --- rule the tree file may already carry
    body = re.sub(r"\n+---\s*$", "", tree_body.rstrip())
    toc_with_ids = _add_block_ids(body)
    if not _TOC_HEADING_RE.match(toc_with_ids.lstrip()):
        toc_with_ids = "## དཀར་ཆག / Table of Contents\n\n" + toc_with_ids
    return toc_with_ids.rstrip() + "\n\n---\n"


def inject_toc(tree_path, commentary_path, output_path):
    """Read tree_path, add block IDs, splice into commentary_path, write output_path."""

    raw_tree = tree_path.read_text(encoding="utf-8")
    tree_body = _strip_yaml_frontmatter(raw_tree)
    if not tree_body.strip():
        sys.exit("Error: " + str(tree_path) + " appears empty after stripping frontmatter.")

    toc_block = _build_toc_block(tree_body)

    source = commentary_path.read_text(encoding="utf-8")
    lines = source.splitlines(keepends=True)

    # locate YAML frontmatter end
    fm_end = None
    if lines and _FRONTMATTER_RE.match(lines[0]):
        for i, ln in enumerate(lines[1:], 1):
            if _FRONTMATTER_RE.match(ln):
                fm_end = i
                break

    # find existing TOC block to replace
    toc_start = toc_end = None
    for i, ln in enumerate(lines):
        if _TOC_HEADING_RE.match(ln.rstrip()):
            toc_start = i
            j = i + 1
            while j < len(lines):
                stripped = lines[j].rstrip()
                if stripped == "---":
                    toc_end = j + 1
                    break
                if stripped and not stripped.startswith("*") and not stripped.startswith("#"):
                    break
                j += 1
            toc_end = toc_end if toc_end is not None else j
            break

    if toc_start is not None:
        before = "".join(lines[:toc_start])
        after = "".join(lines[toc_end:])
        result = before + toc_block + after
        action = "replaced existing TOC block (lines " + str(toc_start + 1) + "-" + str(toc_end) + ")"
    elif fm_end is not None:
        before = "".join(lines[:fm_end + 1])
        after = "".join(lines[fm_end + 1:])
        result = before + "\n" + toc_block + after
        action = "inserted after frontmatter (line " + str(fm_end + 1) + ")"
    else:
        result = toc_block + source
        action = "prepended (no frontmatter found)"

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(result, encoding="utf-8")

    entry_count = len(re.findall(r"^\s*\*\s+\d", toc_block, re.MULTILINE))
    print(str(entry_count) + " TOC entries injected (" + action + ")")
    print("  Output: " + str(output_path))


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------
def find_vault_root(start):
    for parent in [start] + list(start.parents):
        if (parent / "4-SYSTEM").is_dir():
            return parent
    return start.parent if start.is_file() else start


def main():
    parser = argparse.ArgumentParser(
        description="Inject a TOC tree into a Tibetan commentary source file.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument("commentary", help="Path to the source commentary .md file")
    parser.add_argument("toc_tree", help="Path to toc-tree-<id>.md")
    parser.add_argument(
        "--out", default=None,
        help="Output path (default: <vault-root>/0-INBOX/temp/toc-<commentary-filename>)",
    )
    parser.add_argument(
        "--vault-root", default=None,
        help="Vault root (dir containing 4-SYSTEM/). Default: auto-detect.",
    )
    args = parser.parse_args()

    commentary_path = Path(args.commentary).expanduser().resolve()
    toc_path = Path(args.toc_tree).expanduser().resolve()

    if not commentary_path.exists():
        sys.exit("Error: commentary file not found: " + str(commentary_path))
    if not toc_path.exists():
        sys.exit("Error: TOC tree file not found: " + str(toc_path))

    vault_root = (
        Path(args.vault_root).resolve() if args.vault_root
        else find_vault_root(commentary_path)
    )

    if args.out:
        output_path = Path(args.out).expanduser().resolve()
    else:
        output_path = vault_root / "0-INBOX" / "temp" / ("toc-" + commentary_path.name)

    inject_toc(toc_path, commentary_path, output_path)


if __name__ == "__main__":
    main()
