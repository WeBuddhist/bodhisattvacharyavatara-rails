#!/usr/bin/env python3
"""
add_toc.py  -- Generate a clean nested TOC and prepend it to a Tibetan markdown file.

Depth rules
-----------
  Commentary (trailing -0):   ^1-0    -> strip 0 -> 1 seg  -> depth 1
                               ^1-1-0  -> strip 0 -> 2 segs -> depth 2
  Sa-bcad   (no trailing 0):  ^1-1    -> 2 segs - 1        -> depth 1
                               ^1-1-1  -> 3 segs - 1        -> depth 2

Output: 0-INBOX/temp/toc-{filename} inside the vault root.

Usage:  python add_toc.py <input_file> [--output-dir <dir>]
"""

import re
import sys
from pathlib import Path

# ---------------------------------------------------------------------------
# Text cleaning
# ---------------------------------------------------------------------------

_ORDINAL_PAT = re.compile(
    r"^(?:"
    r"\xe0\xbd\x91\xe0\xbd\xb2\xe0\xbc\x8b\xe0\xbd\x94\xe0\xbd\xbc|"  # fallback bytes
    r"དང་པོ|གཉིས་པ|གསུམ་པ|བཞི་པ|ལྔ་པ|དྲུག་པ|"
    r"བདུན་པ|བརྒྱད་པ|དགུ་པ|བཅུ་པ|བཅུ་གཅིག་པ|བཅུ་གཉིས་པ"
    r")[་།\s]*",
    re.UNICODE,
)

_BRACKET_NUM   = re.compile(r"^[༡༢༣༤༥༦༧༨༩༠]+༽\s*", re.UNICODE)
_BRACKET_ALPHA = re.compile(r"^[ཀ-ཬ]༽\s*", re.UNICODE)
_DECIMAL_LABEL = re.compile(r"^[༡༢༣༤༥༦༧༨༩༠]+\.[༡༢༣༤༥༦༧༨༩༠]+\s*", re.UNICODE)
_PAREN_NUM     = re.compile(r"^\([༡༢༣༤༥༦༧༨༩༠]+\)\s*", re.UNICODE)

_WIKI_LINK      = re.compile(r"\[\[#\^[^\]]*\|([^\]]*)\]\]")
_WIKI_LINK_BARE = re.compile(r"\[\[#\^[^\]]*\]\]")
_BLOCK_ID_TAIL  = re.compile(r"\s*\^[\w-]+\s*$")

# Strip double-shad section-enders (lo-nyis, nyis) but NOT lone shad
_DOUBLE_SHAD = re.compile(r"\s*།།\s*$")   # །།
_LO_SHAD     = re.compile(r"[་\s]*ལོ།།\s*$")  # ལོ།།


def clean_text(raw):
    t = raw
    t = _WIKI_LINK.sub(r"\1", t)
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
# Depth from block ID
# ---------------------------------------------------------------------------

def _id_depth(id_str):
    parts = id_str.split("-")
    if len(parts) > 1 and parts[-1] == "0":
        # Commentary: strip trailing 0, remaining count = depth
        parts = parts[:-1]
        return max(1, len(parts))
    else:
        # Sa-bcad: depth = total_segments - 1
        return max(1, len(parts) - 1)


def _indent_level(line):
    stripped = line.lstrip(" \t")
    prefix   = line[: len(line) - len(stripped)]
    return prefix.count("\t") + prefix.count(" ") // 2


# ---------------------------------------------------------------------------
# Format A  (existing ^toc-* TOC section)
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

    entries = []
    for line in lines[start:]:
        if line.startswith("## ") and entries:
            break
        m = _TOC_ENTRY.search(line)
        if not m:
            continue
        toc_id = m.group(1)
        depth  = len(toc_id.split("-"))
        text   = clean_text(line)
        if text:
            entries.append({"depth": depth, "text": text, "toc_id": toc_id})
    return entries or None


# ---------------------------------------------------------------------------
# Format B/C  (body block IDs)
# ---------------------------------------------------------------------------

_BODY_BLOCK_ID = re.compile(r"\^(\d+(?:-\d+)+)\s*$")


def _assign_toc_ids(entries):
    counters = {}
    for entry in entries:
        d = entry["depth"]
        for k in list(counters.keys()):
            if k > d:
                del counters[k]
        counters[d] = counters.get(d, 0) + 1
        toc_parts = [str(counters.get(i, 1)) for i in range(1, d + 1)]
        entry["toc_id"] = "-".join(toc_parts)
    return entries


def _extract_format_bc(lines):
    entries = []
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

        if depth_by_indent > 1 and depth_by_id <= 1:
            depth = depth_by_indent
        else:
            depth = depth_by_id

        entries.append({"depth": depth, "text": text, "raw_id": id_str})

    if not entries:
        return None
    return _assign_toc_ids(entries)


# ---------------------------------------------------------------------------
# Render
# ---------------------------------------------------------------------------

def render_toc(entries):
    lines = []
    for e in entries:
        indent = "   " * (e["depth"] - 1)
        lines.append(indent + "* " + e["text"] + " ^toc-" + e["toc_id"])
    return "\n".join(lines)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

# Fallback vault root — used only if find_vault_root() cannot auto-detect
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


def process_file(input_path, output_dir=None):
    src = Path(input_path).resolve()
    if not src.exists():
        print("ERROR: File not found: " + str(src), file=sys.stderr)
        return False

    text  = read_file(src)
    lines = text.splitlines()

    entries = _extract_format_a(lines)
    if not entries:
        entries = _extract_format_bc(lines)

    if not entries:
        print("ERROR: No TOC structure found in " + src.name, file=sys.stderr)
        print("The file needs a ## dkar-chag section with ^toc-* IDs,", file=sys.stderr)
        print("or lines with ^X-Y(-Z)* block IDs.", file=sys.stderr)
        return False

    toc_body    = render_toc(entries)
    toc_section = "## དཀར་ཆག / Table of Contents\n\n" + toc_body + "\n\n---\n\n"

    if output_dir:
        out_dir = Path(output_dir)
    else:
        vault   = find_vault_root(src)
        out_dir = vault / "0-INBOX" / "temp"

    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / ("toc-" + src.name)

    if text.startswith("---"):
        fm_end = text.find("\n---", 3)
        if fm_end != -1:
            fm_end = text.index("\n", fm_end + 1) + 1
            new_text = text[:fm_end] + "\n" + toc_section + text[fm_end:]
        else:
            new_text = toc_section + text
    else:
        new_text = toc_section + text

    out_path.write_text(new_text, encoding="utf-8")
    print("TOC added. Output: " + str(out_path))
    return True


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python add_toc.py <input_file> [--output-dir <dir>]")
        sys.exit(1)

    inp = sys.argv[1]
    out = None
    if "--output-dir" in sys.argv:
        idx = sys.argv.index("--output-dir")
        if idx + 1 < len(sys.argv):
            out = sys.argv[idx + 1]

    sys.exit(0 if process_file(inp, out) else 1)
