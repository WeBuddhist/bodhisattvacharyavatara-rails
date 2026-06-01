#!/usr/bin/env python3
"""analyse_commentary.py

Reads the full commentary file and outputs it unchanged except that,
in every ###+ section that contains verse transclusions ![[...#^N-M]],
the root-text line numbers are appended (as [n1, n2, ...]) to the last
line of every prose paragraph in that section.

Everything else — headings, blank lines, ![[...]] lines, frontmatter,
TOC, Q&A sections without citations — is written out verbatim.

Usage
  python 0-INBOX/analyse_commentary.py

Options
  --commentary PATH   default: 1-SOURCES/Commentaries/zh-入菩薩行論（宗薩蔣揚欽哲仁波切）.md
  --root PATH         default: 0-INBOX/root texts/chinese-a.md
  --out PATH          default: 0-INBOX/commentary_annotated.md
  --min-level N       minimum heading depth to annotate (default 3)
"""

import argparse
import re
import sys
from pathlib import Path

_DEFAULT_COMMENTARY = Path(
    "1-SOURCES/Commentaries/zh-入菩薩行論（宗薩蔣揚欽哲仁波切）.md"
)
_DEFAULT_ROOT = Path("0-INBOX/root texts/chinese-a.md")
_DEFAULT_OUT  = Path("0-INBOX/commentary_annotated.md")

TRANSCLUDE_RE = re.compile(r"!\[\[.*?#\^(\d+-\d+)\]\]")
HEADING_RE    = re.compile(r"^(#{1,6})\s")


# ── 1. Verse index ────────────────────────────────────────────────────────────
def build_verse_index(root_path: Path) -> dict[str, int]:
    idx: dict[str, int] = {}
    with open(root_path, encoding="utf-8") as fh:
        for lineno, raw in enumerate(fh, 1):
            m = re.match(r"^\[(\d+)\.(\d+)\]", raw)
            if m:
                idx[f"{m.group(1)}-{m.group(2)}"] = lineno
    return idx


# ── 2. Helpers ────────────────────────────────────────────────────────────────
def verse_id_of(line: str) -> str | None:
    m = TRANSCLUDE_RE.search(line)
    return m.group(1) if m else None

def is_prose(line: str) -> bool:
    s = line.strip()
    return bool(s) and not s.startswith("![[") and not HEADING_RE.match(s)


# ── 3. Collect root line numbers from a block of lines ───────────────────────
def collect_root_lines(lines: list[str], verse_idx: dict) -> list[int]:
    seen: set[int] = set()
    result: list[int] = []
    for line in lines:
        vid = verse_id_of(line)
        if vid is None:
            continue
        lineno = verse_idx.get(vid)
        if lineno is not None and lineno not in seen:
            seen.add(lineno)
            result.append(lineno)
    return result


# ── 4. Annotate a list of lines: append tag to last line of each paragraph ───
def annotate_lines(lines: list[str], tag: str) -> list[str]:
    """
    Return lines with `tag` appended to the last line of every prose paragraph.
    Non-prose lines (blank, transclusions, headings) pass through unchanged.
    """
    result: list[str] = []
    i = 0
    while i < len(lines):
        line = lines[i]
        if not line.strip() or not is_prose(line):
            result.append(line)
            i += 1
        else:
            # collect the whole prose paragraph (consecutive prose lines)
            para: list[str] = []
            while i < len(lines) and lines[i].strip() and is_prose(lines[i]):
                para.append(lines[i])
                i += 1
            para[-1] = f"{para[-1]} {tag}"
            result.extend(para)
    return result


# ── 5. Post-processing ────────────────────────────────────────────────────────
_FOOTNOTE_RE = re.compile(r"^\[\^\d+\]:")

def _post_process(lines: list[str]) -> list[str]:
    """
    1. Remove footnote lines (starting with [^n]:).
    2. Remove non-blank lines that contain no word characters (standalone
       symbols such as --- horizontal rules), but preserve YAML front-matter
       delimiters (the two opening/closing --- lines at the top of the file).
    3. Collapse consecutive blank lines down to a single blank line.
    """
    WORD = re.compile(r"\w")

    # ── passes 1 & 2: filter footnotes and standalone symbols ────────────────
    filtered: list[str] = []
    frontmatter_dashes = 0          # count of --- lines seen while in frontmatter
    frontmatter_closed = False

    for line in lines:
        s = line.strip()

        # Track YAML front-matter (first two bare --- lines)
        if not frontmatter_closed and s == "---":
            frontmatter_dashes += 1
            if frontmatter_dashes == 2:
                frontmatter_closed = True
            filtered.append(line)
            continue

        # Remove footnote lines
        if _FOOTNOTE_RE.match(s):
            continue

        # Remove standalone-symbol lines (non-blank, zero word chars)
        if s and not WORD.search(s):
            continue

        filtered.append(line)

    # ── pass 3: collapse consecutive blank lines to one ──────────────────────
    result: list[str] = []
    prev_blank = False
    for line in filtered:
        is_blank = not line.strip()
        if is_blank:
            if not prev_blank:
                result.append(line)
            prev_blank = True
        else:
            result.append(line)
            prev_blank = False

    return result


# ── 6. Main ───────────────────────────────────────────────────────────────────
def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--commentary", type=Path, default=_DEFAULT_COMMENTARY)
    ap.add_argument("--root",       type=Path, default=_DEFAULT_ROOT)
    ap.add_argument("--out",        type=Path, default=_DEFAULT_OUT)
    ap.add_argument("--min-level",  type=int,  default=3)
    args = ap.parse_args()

    verse_idx = build_verse_index(args.root)
    print(f"[info] {len(verse_idx)} verses indexed", file=sys.stderr)

    with open(args.commentary, encoding="utf-8") as fh:
        raw_lines = [ln.rstrip("\n") for ln in fh]

    # ── split file into sections (any heading = boundary) ────────────────────
    # Each entry: (heading_line_idx, level, body_line_indices)
    sections: list[dict] = []
    current: dict | None = None

    for i, line in enumerate(raw_lines):
        m = HEADING_RE.match(line)
        if m:
            if current is not None:
                sections.append(current)
            current = {"start": i, "level": len(m.group(1)), "body_indices": []}
        else:
            if current is not None:
                current["body_indices"].append(i)

    if current is not None:
        sections.append(current)

    # ── for each qualifying section, compute its tag ─────────────────────────
    # annotated_lines[i] = replacement for raw_lines[i]   (or None = use original)
    annotated: dict[int, str] = {}   # line index → replacement text

    annotated_sections = 0
    total_citations = 0

    for sec in sections:
        if sec["level"] < args.min_level:
            continue
        body = [raw_lines[i] for i in sec["body_indices"]]
        root_lines = collect_root_lines(body, verse_idx)
        if not root_lines:
            continue

        tag = "[" + ", ".join(str(n) for n in root_lines) + "]"
        annotated_body = annotate_lines(body, tag)

        for orig_idx, new_line in zip(sec["body_indices"], annotated_body):
            if new_line != raw_lines[orig_idx]:
                annotated[orig_idx] = new_line

        annotated_sections += 1
        total_citations += len(root_lines)

    # ── collect output lines (annotations applied, transclusions removed) ────────
    out_lines: list[str] = []
    for i, line in enumerate(raw_lines):
        if verse_id_of(line) is not None:
            continue                         # remove ![[...#^N-M]] lines
        out_lines.append(annotated.get(i, line))

    # ── post-process ──────────────────────────────────────────────────────────
    out_lines = _post_process(out_lines)

    # ── write ─────────────────────────────────────────────────────────────────
    args.out.parent.mkdir(parents=True, exist_ok=True)
    with open(args.out, "w", encoding="utf-8") as fh:
        for line in out_lines:
            fh.write(line + "\n")

    print(f"[info] annotated output    → {args.out}", file=sys.stderr)
    print(f"[info] sections annotated  : {annotated_sections}", file=sys.stderr)
    print(f"[info] total citations     : {total_citations}", file=sys.stderr)

    # ── write TSV report ──────────────────────────────────────────────────────
    report_path = args.out.with_suffix(".report.tsv")
    with open(report_path, "w", encoding="utf-8") as fh:
        fh.write("section_line\theading\tverse_id\troot_line\n")
        for sec in sections:
            if sec["level"] < args.min_level:
                continue
            body = [raw_lines[i] for i in sec["body_indices"]]
            heading = raw_lines[sec["start"]].strip()
            for line in body:
                vid = verse_id_of(line)
                if vid is None:
                    continue
                lineno = verse_idx.get(vid)
                if lineno is not None:
                    fh.write(f"{sec['start']+1}\t{heading}\t^{vid}\t{lineno}\n")
    print(f"[info] report              → {report_path}", file=sys.stderr)


if __name__ == "__main__":
    main()
