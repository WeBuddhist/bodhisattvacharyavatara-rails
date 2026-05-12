#!/usr/bin/env python3
"""
add_toc.py  -- Generate a decimal-numbered nested TOC from a Tibetan markdown file.

Strategy
--------
1. Isolate the "draft" structural items from the document:
     a) If the document has an existing TOC section (## dkar-chag with ^toc-* IDs) → use it.
     b) If the document is a sa-bcad / structural outline → read from the top, collecting
        every line that carries a ^X-Y(-Z)* block ID; the ordering and ID structure encode
        the hierarchy.
     c) Commentary bodies: pick up section-opening paragraphs (block IDs ending in -0).

2. Build the hierarchy in two passes:
     Pass 1 — collect all depth-1 (main section) entries.
     Pass 2 — slot each deeper entry under its parent.

3. Render as a decimal-numbered nested * list:
     * 1. main section title                    ^toc-1
        * 1.1 first subsection                  ^toc-1-1
           * 1.1.1 sub-subsection               ^toc-1-1-1

Depth rules
-----------
  Commentary (trailing -0):   ^1-0   -> depth 1   ^1-1-0 -> depth 2
  Sa-bcad   (no trailing 0):  ^1-1   -> depth 1   ^1-1-1 -> depth 2

Output: 0-INBOX/temp/toc-{filename} inside the vault root.
Usage:  python add_toc.py <input_file> [<output_dir>]
"""

import re
import sys
from pathlib import Path


# ---------------------------------------------------------------------------
# Text cleaning
# ---------------------------------------------------------------------------

_ORDINAL_PAT = re.compile(
    r"^(?:དང་པོ|གཉིས་པ|གསུམ་པ|བཞི་པ|ལྔ་པ|དྲུག་པ|"
    r"བདུན་པ|བརྒྱད་པ|དགུ་པ|བཅུ་པ|བཅུ་གཅིག་པ|བཅུ་གཉིས་པ)[་།\s]*",
    re.UNICODE,
)
_BRACKET_NUM   = re.compile(r"^[༡༢༣༤༥༦༧༨༩༠]+༽\s*", re.UNICODE)
_BRACKET_ALPHA = re.compile(r"^[ཀ-ཬ]༽\s*", re.UNICODE)
_DECIMAL_LABEL = re.compile(r"^[༡༢༣༤༥༦༧༨༩༠]+\.[༡༢༣༤༥༦༧༨༩༠]+\s*", re.UNICODE)
_PAREN_NUM     = re.compile(r"^\([༡༢༣༤༥༦༧༨༩༠]+\)\s*", re.UNICODE)

_WIKI_LINK      = re.compile(r"\[\[#\^[^\]]*\|([^\]]*)\]\]")
_WIKI_LINK_BARE = re.compile(r"\[\[#\^[^\]]*\]\]")
_BLOCK_ID_TAIL  = re.compile(r"\s*\^[\w-]+\s*$")
_LO_SHAD        = re.compile(r"[་\s]*ལོ།།\s*$")
_DOUBLE_SHAD    = re.compile(r"\s*།།\s*$")


def clean_text(raw):
    t = _WIKI_LINK.sub(r"\1", raw)
    t = _WIKI_LINK_BARE.sub("", t)
    t = _BLOCK_ID_TAIL.sub("", t)
    t = re.sub(r"^[\s\-\*]+", "", t)
    t = _ORDINAL_PAT.sub("", t)
    t = _DECIMAL_LABEL.sub("", t)
    t = _BRACKET_NUM.sub("", t)
    t = _BRACKET_ALPHA.sub("", t)
    t = _PAREN_NUM.sub("", t)
    t = _LO_SHAD.sub("།", t)
    t = _DOUBLE_SHAD.sub("།", t)
    return t.strip()


# ---------------------------------------------------------------------------
# Depth calculation
# ---------------------------------------------------------------------------

def _id_depth(id_str):
    """
    Commentary (ends -0): strip trailing 0, count remaining segments.
    Sa-bcad   (no  -0  ): depth = total_segments - 1.
    """
    parts = id_str.split("-")
    if len(parts) > 1 and parts[-1] == "0":
        parts = parts[:-1]
        return max(1, len(parts))
    return max(1, len(parts) - 1)


def _indent_level(line):
    stripped = line.lstrip(" \t")
    prefix   = line[: len(line) - len(stripped)]
    return prefix.count("\t") + prefix.count(" ") // 2


# ---------------------------------------------------------------------------
# Pass 1/2: two-pass hierarchy builder
# ---------------------------------------------------------------------------

def _two_pass_build(raw_entries):
    """
    Pass 1: collect depth-1 entries (main sections).
    Pass 2: insert each deeper entry under its nearest shallower parent,
            preserving document order.

    Returns the same list in document order with toc_ids assigned.
    """
    # Pass 1 — identify the main sections (depth 1)
    # The minimum depth in the document becomes the effective "depth 1"
    if not raw_entries:
        return []
    min_depth = min(e["depth"] for e in raw_entries)

    # Normalise so the shallowest level is always 1
    for e in raw_entries:
        e["depth"] = e["depth"] - min_depth + 1

    # Pass 2 — assign positional toc-IDs by walking through in order
    counters = {}
    for entry in raw_entries:
        d = entry["depth"]
        # Reset all deeper counters whenever we come back to a shallower level
        for k in list(counters.keys()):
            if k > d:
                del counters[k]
        counters[d] = counters.get(d, 0) + 1
        entry["toc_id"] = "-".join(str(counters.get(i, 1)) for i in range(1, d + 1))

    return raw_entries


# ---------------------------------------------------------------------------
# Format A — existing ^toc-* TOC section
# ---------------------------------------------------------------------------

_TOC_HEADING = re.compile(r"^##\s*(དཀར་ཆག|Table of Contents|TOC)", re.IGNORECASE)
_TOC_ENTRY   = re.compile(r"\^toc-([\d][\d\-]*)")


def _extract_format_a(lines):
    start = None
    for i, line in enumerate(lines):
        if _TOC_HEADING.match(line):
            start = i + 1
            break
    if start is None:
        return None

    raw = []
    for line in lines[start:]:
        if line.startswith("## ") and raw:
            break
        m = _TOC_ENTRY.search(line)
        if not m:
            continue
        toc_id = m.group(1)
        depth  = len(toc_id.split("-"))
        text   = clean_text(line)
        if text:
            raw.append({"depth": depth, "text": text, "toc_id": toc_id})

    return raw or None


# ---------------------------------------------------------------------------
# Format B/C — body block IDs (sa-bcad and commentary)
# ---------------------------------------------------------------------------

_BODY_BLOCK_ID = re.compile(r"\^(\d+(?:-\d+)+)\s*$")


def _extract_format_bc(lines):
    raw = []
    for line in lines:
        m = _BODY_BLOCK_ID.search(line.rstrip())
        if not m:
            continue
        id_str = m.group(1)
        if "toc" in id_str:
            continue
        text = clean_text(line)
        if not text or len(text) < 2:
            continue

        depth_by_id     = _id_depth(id_str)
        depth_by_indent = max(1, _indent_level(line) + 1)
        depth = depth_by_indent if (depth_by_indent > 1 and depth_by_id <= 1) else depth_by_id

        raw.append({"depth": depth, "text": text, "raw_id": id_str})

    if not raw:
        return None
    return _two_pass_build(raw)


# ---------------------------------------------------------------------------
# Render — decimal-numbered nested list
# ---------------------------------------------------------------------------

def _decimal_prefix(toc_id):
    """
    Convert toc_id to a decimal label:
      '1'     -> '1.'
      '1-1'   -> '1.1'
      '1-1-1' -> '1.1.1'
    """
    parts = toc_id.split("-")
    if len(parts) == 1:
        return parts[0] + "."
    return ".".join(parts)


def render_toc(entries):
    lines = []
    for e in entries:
        indent  = "   " * (e["depth"] - 1)
        decimal = _decimal_prefix(e["toc_id"])
        lines.append(indent + "* " + decimal + " " + e["text"] + " ^toc-" + e["toc_id"])
    return "\n".join(lines)


# ---------------------------------------------------------------------------
# File I/O helpers
# ---------------------------------------------------------------------------

_WIN_ROOT = Path(r"C:\Users\trinley\Obsidian\bodhisattvacharyavatara-rails")
_LIN_ROOT = Path("/sessions/eloquent-laughing-gates/mnt/bodhisattvacharyavatara-rails")
VAULT_ROOT = _WIN_ROOT if _WIN_ROOT.exists() else _LIN_ROOT


def find_vault_root(start):
    p = start if start.is_dir() else start.parent
    while p != p.parent:
        if (p / "0-INBOX").exists():
            return p
        p = p.parent
    return VAULT_ROOT


def read_file(path):
    try:
        return path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        return path.read_text(encoding="utf-8", errors="replace")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def process_file(input_path, output_dir=None):
    src = Path(input_path).resolve()
    if not src.exists():
        print("ERROR: File not found: " + str(src), file=sys.stderr)
        return False

    text  = read_file(src)
    lines = text.splitlines()

    # Step 1 — isolate draft entries (Format A first, then B/C)
    entries = _extract_format_a(lines)
    source  = "existing TOC section"
    if not entries:
        entries = _extract_format_bc(lines)
        source  = "body block IDs"

    if not entries:
        print("ERROR: No structural items found in " + src.name, file=sys.stderr)
        return False

    print("Extracted " + str(len(entries)) + " TOC entries from " + source + ".")

    # Step 2 — build numbered TOC
    toc_body    = render_toc(entries)
    toc_section = "## དཀར་ཆག / Table of Contents\n\n" + toc_body + "\n\n---\n\n"

    # Output path
    if output_dir:
        out_dir = Path(output_dir)
    else:
        vault   = find_vault_root(src)
        out_dir = vault / "0-INBOX" / "temp"
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / ("toc-" + src.name)

    # Splice TOC after YAML frontmatter (if present)
    if text.startswith("---"):
        close = text.find("\n---", 3)
        if close != -1:
            fm_end   = text.index("\n", close + 1) + 1
            new_text = text[:fm_end] + "\n" + toc_section + text[fm_end:]
        else:
            new_text = toc_section + text
    else:
        new_text = toc_section + text

    out_path.write_text(new_text, encoding="utf-8")
    print("TOC written to: " + str(out_path))
    return True


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python add_toc.py <input_file> [<output_dir>]")
        sys.exit(1)
    out = sys.argv[2] if len(sys.argv) > 2 else None
    sys.exit(0 if process_file(sys.argv[1], out) else 1)
