#!/usr/bin/env python3
"""analyse_commentary.py

For every ####+ section in the commentary, locate verse transclusions
  ![[...#^N-M]]
map them to their line numbers in the root-text file (chinese-a.md),
determine whether the citation appears ABOVE or BELOW the surrounding
prose, and write the annotated section to an output file.

Annotation rules
  • verse ABOVE prose  (transclusion precedes commentary text in the section)
      → [line_number] appended to the end of the first commentary prose
        paragraph that FOLLOWS the transclusion (or group of transclusions).
  • verse BELOW prose  (transclusion follows commentary text)
      → [line_number] appended to the end of the prose paragraph that
        PRECEDES the transclusion.

Multiple consecutive transclusions before a prose block all annotate the
same prose paragraph.  Existing bare [] placeholders in the file are filled
instead of appending.

Usage
  python 0-INBOX/analyse_commentary.py [options]

Options
  --commentary PATH   default: 1-SOURCES/Commentaries/zh-入菩薩行論（宗薩蔣揚欽哲仁波切）.md
  --root PATH         default: 0-INBOX/root texts/chinese-a.md
  --out PATH          default: 0-INBOX/commentary_annotated.md
  --all-sections      include ####+ sections that have no transclusions
  --report            also write a TSV analysis to <out>.report.tsv
"""

import argparse
import re
import sys
from pathlib import Path

# ── defaults ─────────────────────────────────────────────────────────────────
_DEFAULT_COMMENTARY = Path(
    "1-SOURCES/Commentaries/zh-入菩薩行論（宗薩蔣揚欽哲仁波切）.md"
)
_DEFAULT_ROOT = Path("0-INBOX/root texts/chinese-a.md")
_DEFAULT_OUT  = Path("0-INBOX/commentary_annotated.md")

TRANSCLUDE_RE = re.compile(r"!\[\[.*?#\^(\d+-\d+)\]\]")
HEADING_RE    = re.compile(r"^(#{1,6})\s")


# ── 1. Build verse → root-text line-number index ─────────────────────────────
def build_verse_index(root_path: Path) -> dict[str, int]:
    """
    Parses lines like  [1.1]善逝具足法身及佛子...
    Returns {"1-1": 5, "1-2": 6, ...} where the key matches the block-ID
    format used in transclusions (^1-1 → "1-1").
    """
    idx: dict[str, int] = {}
    with open(root_path, encoding="utf-8") as fh:
        for lineno, raw in enumerate(fh, 1):
            m = re.match(r"^\[(\d+)\.(\d+)\]", raw)
            if m:
                idx[f"{m.group(1)}-{m.group(2)}"] = lineno
    return idx


# ── 2. Parse commentary into heading-delimited sections ──────────────────────
def parse_sections(commentary_path: Path) -> list[dict]:
    """
    Returns list of dicts: {heading, level, body: list[str]}.
    Each section spans from its heading line to the line before the next
    heading (of any level).
    """
    sections: list[dict] = []
    with open(commentary_path, encoding="utf-8") as fh:
        lines = [ln.rstrip("\n") for ln in fh]

    current: dict | None = None
    for line in lines:
        m = HEADING_RE.match(line)
        if m:
            if current is not None:
                sections.append(current)
            current = {"heading": line, "level": len(m.group(1)), "body": []}
        else:
            if current is not None:
                current["body"].append(line)
    if current is not None:
        sections.append(current)
    return sections


# ── 3. Line-level helpers ─────────────────────────────────────────────────────
def verse_id_of(line: str) -> str | None:
    """Return verse-id (e.g. '1-1') if the line is a transclusion, else None."""
    m = TRANSCLUDE_RE.search(line)
    return m.group(1) if m else None


def is_prose(line: str) -> bool:
    """True iff the line has visible text that is not a transclusion or heading."""
    s = line.strip()
    return bool(s) and not s.startswith("![[") and not HEADING_RE.match(s)


# ── 4. Compute annotation positions for one section ──────────────────────────
AnnotMap = dict[int, list[int]]   # body_index → [root_line_numbers]


def compute_annotations(body: list[str], verse_idx: dict) -> AnnotMap:
    """
    For each transclusion in the body:

      Step A – search backward (skip blank lines; stop at another transclusion
               or end of body):
               • lands on prose  →  prose_before = that index
               • lands on transclusion or exhausts  →  prose_before = None

      Step B:
        prose_before found  (verse BELOW prose):
          → annotate prose_before  (end of the prose paragraph above the verse)

        prose_before not found  (verse ABOVE prose):
          → skip forward past blanks and consecutive transclusions,
            then find the END of the first prose paragraph;
            annotate that line.

    If the same target line is chosen by multiple transclusions, all their
    line numbers accumulate in order.
    """
    annots: AnnotMap = {}

    def add(idx: int, lineno: int) -> None:
        annots.setdefault(idx, []).append(lineno)

    for T, line in enumerate(body):
        vid = verse_id_of(line)
        if vid is None:
            continue
        root_lineno = verse_idx.get(vid)
        if root_lineno is None:
            continue  # verse not in root text (different chapter range)

        # ── A: search backward for nearest prose ─────────────────────────
        prose_before: int | None = None
        for j in range(T - 1, -1, -1):
            s = body[j].strip()
            if not s:
                continue              # blank → keep going
            if is_prose(body[j]):
                prose_before = j
                break
            break                     # non-blank non-prose (transclusion / heading)

        # ── B: place annotation ──────────────────────────────────────────
        if prose_before is not None:
            # verse BELOW prose: annotate the prose that introduces it
            add(prose_before, root_lineno)
        else:
            # verse ABOVE prose: skip forward past blanks + transclusions
            start = T + 1
            while start < len(body):
                s = body[start].strip()
                if not s or verse_id_of(body[start]) is not None:
                    start += 1
                else:
                    break

            # walk to end of first prose paragraph (breaks on blank or non-prose)
            last_prose: int | None = None
            in_prose = False
            for j in range(start, len(body)):
                if is_prose(body[j]):
                    last_prose = j
                    in_prose = True
                elif not body[j].strip():
                    if in_prose:
                        break        # blank after prose → end of paragraph
                else:
                    break            # transclusion or heading → end

            if last_prose is not None:
                add(last_prose, root_lineno)

    return annots


# ── 5. Render annotated section ───────────────────────────────────────────────
def render_section(heading: str, body: list[str], annots: AnnotMap) -> list[str]:
    """Produce heading + annotated body lines."""
    out = [heading]
    for idx, line in enumerate(body):
        if idx in annots:
            tag = "[" + ", ".join(str(n) for n in annots[idx]) + "]"
            if "[]" in line:           # fill pre-existing placeholder
                out.append(line.replace("[]", tag, 1))
            else:
                out.append(f"{line} {tag}")
        else:
            out.append(line)
    return out


# ── 6. Build report rows for one section ─────────────────────────────────────
def build_report_rows(
    heading: str,
    body: list[str],
    annots: AnnotMap,
    verse_idx: dict,
) -> list[tuple]:
    """Return list of (heading, verse_id, position, commentary_snippet, root_lineno)."""
    rows = []
    for T, line in enumerate(body):
        vid = verse_id_of(line)
        if vid is None:
            continue
        root_lineno = verse_idx.get(vid)
        if root_lineno is None:
            continue

        # Determine position by re-examining backward search result
        prose_before: int | None = None
        for j in range(T - 1, -1, -1):
            s = body[j].strip()
            if not s:
                continue
            if is_prose(body[j]):
                prose_before = j
                break
            break

        position = "below" if prose_before is not None else "above"

        # Pick the target prose snippet for display
        if prose_before is not None:
            snippet = body[prose_before].strip()[:80]
        else:
            # first prose line after
            for j in range(T + 1, len(body)):
                if is_prose(body[j]):
                    snippet = body[j].strip()[:80]
                    break
            else:
                snippet = "(no prose found)"

        rows.append((heading.strip(), vid, position, root_lineno, snippet))
    return rows


# ── 7. Main ───────────────────────────────────────────────────────────────────
def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--commentary", type=Path, default=_DEFAULT_COMMENTARY)
    ap.add_argument("--root",       type=Path, default=_DEFAULT_ROOT)
    ap.add_argument("--out",        type=Path, default=_DEFAULT_OUT)
    ap.add_argument("--min-level", type=int, default=3,
                    help="minimum heading depth to include (default: 3 = ### and deeper)")
    args = ap.parse_args()

    # ── index
    verse_idx = build_verse_index(args.root)
    print(f"[info] {len(verse_idx)} verses indexed from {args.root}", file=sys.stderr)

    # ── parse
    sections = parse_sections(args.commentary)
    target   = [s for s in sections if s["level"] >= args.min_level]
    print(f"[info] {len(target)} sections (level >= {args.min_level}) found", file=sys.stderr)

    # ── annotate & render
    output_blocks: list[str] = []
    report_rows:   list[tuple] = []

    for sec in target:
        annots = compute_annotations(sec["body"], verse_idx)
        if not annots:
            continue  # skip sections with no verse citations

        rendered = render_section(sec["heading"], sec["body"], annots)
        output_blocks.append("\n".join(rendered))

        report_rows.extend(
            build_report_rows(sec["heading"], sec["body"], annots, verse_idx)
        )

    # ── write annotated markdown
    args.out.parent.mkdir(parents=True, exist_ok=True)
    with open(args.out, "w", encoding="utf-8") as fh:
        fh.write("\n\n---\n\n".join(output_blocks))
    print(f"[info] annotated output → {args.out}", file=sys.stderr)

    # ── write TSV report (always generated alongside the markdown)
    report_path = args.out.with_suffix(".report.tsv")
    with open(report_path, "w", encoding="utf-8") as fh:
        fh.write("section\tverse_id\tposition\troot_line\tprose_snippet\n")
        for heading, vid, position, root_lineno, snippet in report_rows:
            fh.write(f"{heading}\t^{vid}\t{position}\t{root_lineno}\t{snippet}\n")
    print(f"[info] report          → {report_path}", file=sys.stderr)

    # ── summary
    print(f"[info] sections with citations : {len(output_blocks)}/{len(target)}", file=sys.stderr)
    print(f"[info] total verse citations   : {len(report_rows)}", file=sys.stderr)


if __name__ == "__main__":
    main()
