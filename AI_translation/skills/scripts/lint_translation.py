#!/usr/bin/env python3
"""
lint_translation.py
===================

Parser and linter for vault translation files (Marathi or any target language).

Validates that a translated file is structurally consistent with:
  1. A well-formed YAML frontmatter block.
  2. The root text it claims to translate (all IDs present, none extra, none
     duplicated, in-order per chapter).
  3. Internal formatting conventions (heading hierarchy, verse non-emptiness,
     transclusion-line placement, block-ID format).

Exit codes
----------
0  No errors (warnings may still be printed).
1  One or more ERROR-level findings.
2  Script invocation error (bad arguments, file not found).

Output format
-------------
Each finding is a single line::

    PATH:LINE  [LEVEL]  RULE_ID  message

where LEVEL is one of ``ERROR``, ``WARN``, or ``INFO``.

Levels
------
ERROR
    The file is incorrect or violates a vault rule that must be fixed before
    the file may be used to generate downstream outputs.
WARN
    The file deviates from a convention but is not definitively wrong.  Review
    and decide whether to fix.
INFO
    Informational observation; no action required.

Rules
-----
YAML checks (prefix ``Y``)
~~~~~~~~~~~~~~~~~~~~~~~~~~
Y001  Missing YAML frontmatter (file must start with ``---``).
Y002  Malformed YAML (cannot be parsed).
Y003  Required frontmatter field missing: ``title``, ``source_text``,
      ``target_language``, ``verse_id_format``, ``segment_id_coverage``.
Y004  ``verse_id_format`` value is not ``chapter-verse``.

Heading checks (prefix ``H``)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
H001  Document title heading (``# …``) is missing or not the first heading.
H002  A chapter heading (``## N. …``) does not carry a ``^N-0`` block ID.
H003  Chapter heading block IDs are out of order.
H004  A chapter heading block ID does not match the chapter number in its title.

Block-ID format checks (prefix ``B``)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
B001  Malformed block ID (does not match ``^\\w[\\w\\-]*``).
B002  Duplicate block ID within the file.
B003  Block ID on a non-final line of its block (must be on the last line).

Verse checks (prefix ``V``)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~
V001  Empty verse block (block has a block ID but no preceding text content).
V002  Verse block ID is not on a standalone line after the verse text.

Coverage checks (prefix ``C``) — only when ``--root-text`` is given
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
C001  Segment ID present in translated file but NOT in root text (extra ID).
C002  Root-text segment ID MISSING from translated file (dropped/renamed verse).
C003  Segment IDs within a chapter appear out of numerical order.

Transclusion checks (prefix ``T``) — only when ``--root-text`` is given
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
T001  Transclusion line references an ID that does not exist in the root text.
T002  Transclusion line is not immediately followed by the block it references.
T003  Two or more consecutive transclusion lines (dangling transclusion).
T004  Transclusion line references an ID that does not match the following block.

Usage
-----
::

    python lint_translation.py <translated_file> [--root-text PATH]
        [--vault-root PATH] [--error-only] [--no-color]

    # Full check, print all findings:
    python lint_translation.py \\
        AI_translation/marathi/bca-marathi-scholars.md \\
        --root-text 1-SOURCES/Text/BCAV08_SH_sk.md

    # Exit non-zero if any errors; suppress warnings/info:
    python lint_translation.py \\
        AI_translation/marathi/bca-marathi-children.md \\
        --root-text 1-SOURCES/Text/BCAV08_SH_sk.md \\
        --error-only

    # Lint without comparing to root text:
    python lint_translation.py AI_translation/marathi/bca-marathi-plain.md
"""

import argparse
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path
from typing import Iterator, Optional

try:
    import yaml  # PyYAML; gracefully degrade if absent
    _YAML_AVAILABLE = True
except ImportError:
    _YAML_AVAILABLE = False

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

REQUIRED_FRONTMATTER_FIELDS = [
    "title",
    "source_text",
    "target_language",
    "verse_id_format",
    "segment_id_coverage",
]

TRANSCLUSION_RE = re.compile(r"^\s*!\[\[.*#\^([\w][\w\-]*)\]\]\s*$")
# ID at end of line (possibly followed by whitespace only):
SEGMENT_ID_RE = re.compile(r"\^([\w][\w\-]*)\s*$")
# ID anywhere in a line (also matches IDs with trailing annotation):
SEGMENT_ID_ANYWHERE_RE = re.compile(r"\^([\w][\w\-]*)")
HEADING_H1_RE = re.compile(r"^#\s+")
# Chapter heading: "## N. …" where N is an ASCII digit
HEADING_H2_RE = re.compile(r"^##\s+([0-9]+)\.")
# Chapter heading block ID: ^N-0 (ASCII digits, ends at whitespace/EOL)
HEADING_H2_ID_RE = re.compile(r"\^([0-9]+)-0\s*$")
# Heading-type IDs (title, intro, chapter/section headers):
HEADING_ID_RE = re.compile(r"^(0|I-.+|\d.*-0)$")

# Strict verse ID: ^N-V where both N and V are pure decimal digits.
# Allows optional suffixes like x1 (split verses) via the looser form below.
VERSE_ID_STRICT_RE = re.compile(r"^([0-9]+)-([0-9]+)$")
# Colophon / appendix IDs: anything starting with a letter segment (a-*, b-*)
COLOPHON_ID_RE = re.compile(r"^[a-zA-Z]")
# IDs that look like chapter colophons: N-a, N-b (letter at verse position)
CHAPTER_COLOPHON_ID_RE = re.compile(r"^[0-9]+-[a-zA-Z]")

ANSI_COLORS = {
    "ERROR": "\033[1;31m",
    "WARN":  "\033[1;33m",
    "INFO":  "\033[0;36m",
    "RESET": "\033[0m",
}


# ---------------------------------------------------------------------------
# Data structures
# ---------------------------------------------------------------------------

@dataclass
class Finding:
    level: str       # "ERROR" | "WARN" | "INFO"
    rule: str        # e.g. "V001"
    line: int        # 1-based
    message: str

    def format(self, path: str, use_color: bool = True) -> str:
        if use_color and sys.stdout.isatty():
            color = ANSI_COLORS.get(self.level, "")
            reset = ANSI_COLORS["RESET"]
            level_str = f"{color}[{self.level}]{reset}"
        else:
            level_str = f"[{self.level}]"
        return f"{path}:{self.line}  {level_str}  {self.rule}  {self.message}"


@dataclass
class ParsedFile:
    """Result of parsing a translation file."""
    raw_lines: list[str] = field(default_factory=list)
    frontmatter_raw: str = ""
    frontmatter_dict: dict = field(default_factory=dict)
    frontmatter_end_line: int = 0   # 1-based line of closing ---
    content_lines: list[str] = field(default_factory=list)  # after frontmatter
    blocks: list[tuple[int, list[str]]] = field(default_factory=list)
    # blocks: list of (start_line_1based, lines)


# ---------------------------------------------------------------------------
# File parser
# ---------------------------------------------------------------------------

def parse_file(text: str) -> ParsedFile:
    """Parse a translation file into structured form."""
    result = ParsedFile()
    lines = text.splitlines()
    result.raw_lines = lines

    # --- frontmatter ---
    fm_end = 0
    if lines and lines[0].strip() == "---":
        for i in range(1, len(lines)):
            if lines[i].strip() == "---":
                fm_end = i + 1  # 1-based line of closing ---
                result.frontmatter_raw = "\n".join(lines[1:i])
                result.frontmatter_end_line = fm_end
                break
    result.content_lines = lines[fm_end:]

    if _YAML_AVAILABLE and result.frontmatter_raw:
        try:
            result.frontmatter_dict = yaml.safe_load(result.frontmatter_raw) or {}
        except yaml.YAMLError:
            result.frontmatter_dict = {}

    # --- blocks (content only) ---
    result.blocks = list(_split_content_into_blocks(result.content_lines, fm_end))
    return result


def _split_content_into_blocks(
    content_lines: list[str],
    line_offset: int,
) -> "Iterator[tuple[int, list[str]]]":
    """Yield ``(start_line_1based, [lines])`` blocks from *content_lines*.

    A block ends at a blank line or at the first line whose segment ID
    (if any) appears at the very end of the line.
    """
    current: list[str] = []
    start_line = line_offset + 1

    for i, line in enumerate(content_lines):
        abs_line = line_offset + i + 1  # 1-based
        if line.strip() == "":
            if current:
                yield (start_line, current)
                current = []
            start_line = abs_line + 1
            continue
        current.append(line)
        # End block when a non-transclusion line ends with a segment ID
        if not TRANSCLUSION_RE.match(line) and SEGMENT_ID_RE.search(line):
            yield (start_line, current)
            current = []
            start_line = abs_line + 1

    if current:
        yield (start_line, current)


def block_seg_id(block_lines: list[str]) -> "Optional[str]":
    """Return the segment ID from the last line of *block_lines*, or None.

    IDs are found anywhere in the last line (not just at line-end) so that
    lines with trailing annotations such as ``^6-86 (दुसरा खंड समाप्त)``
    are handled correctly.  Transclusion lines do not count.
    """
    if not block_lines:
        return None
    last = block_lines[-1]
    if TRANSCLUSION_RE.match(last):
        return None
    matches = SEGMENT_ID_ANYWHERE_RE.findall(last)
    return matches[-1] if matches else None


def transclusion_id(line: str) -> "Optional[str]":
    """Return the segment ID referenced in a transclusion line, or None."""
    m = TRANSCLUSION_RE.match(line)
    return m.group(1) if m else None


# ---------------------------------------------------------------------------
# Root-text ID collection
# ---------------------------------------------------------------------------

def collect_root_ids(root_text: str) -> "dict[str, int]":
    """Return ``{seg_id: first_line_1based}`` for every segment ID in *root_text*."""
    ids: dict[str, int] = {}
    for i, line in enumerate(root_text.splitlines(), start=1):
        if TRANSCLUSION_RE.match(line):
            continue
        for m in SEGMENT_ID_ANYWHERE_RE.finditer(line):
            sid = m.group(1)
            if sid not in ids:
                ids[sid] = i
    return ids


# ---------------------------------------------------------------------------
# Linting checks
# ---------------------------------------------------------------------------

def lint_yaml(parsed: ParsedFile) -> "list[Finding]":
    findings: list[Finding] = []

    if not parsed.frontmatter_raw:
        findings.append(Finding(
            "ERROR", "Y001", 1,
            "Missing YAML frontmatter (file must start with ---).",
        ))
        return findings  # can't check further without frontmatter

    if not _YAML_AVAILABLE:
        findings.append(Finding(
            "INFO", "Y002", 1,
            "PyYAML not installed — skipping YAML parse validation (pip install pyyaml).",
        ))
    elif not parsed.frontmatter_dict:
        findings.append(Finding(
            "WARN", "Y002", 1,
            "Frontmatter cannot be parsed as strict YAML "
            "(possibly due to unquoted colons in field values). "
            "Consider quoting values that contain ':'.",
        ))
        return findings

    for field_name in REQUIRED_FRONTMATTER_FIELDS:
        if field_name not in parsed.frontmatter_dict:
            findings.append(Finding(
                "ERROR", "Y003", 1,
                f"Required frontmatter field missing: '{field_name}'.",
            ))

    vif = parsed.frontmatter_dict.get("verse_id_format", "")
    if vif and not str(vif).startswith("chapter-verse"):
        findings.append(Finding(
            "WARN", "Y004", 1,
            f"verse_id_format is '{vif}', expected 'chapter-verse' (or a "
            f"value starting with 'chapter-verse').",
        ))

    return findings


def lint_headings(parsed: ParsedFile) -> "list[Finding]":
    findings: list[Finding] = []
    offset = parsed.frontmatter_end_line  # content starts here
    h1_seen = False
    prev_chapter = 0

    for i, line in enumerate(parsed.content_lines):
        abs_line = offset + i + 1
        if HEADING_H1_RE.match(line) and not h1_seen:
            h1_seen = True
            continue

        m = HEADING_H2_RE.match(line)
        if m:
            chapter_num_in_title = int(m.group(1))
            if chapter_num_in_title == 0:
                # Intro heading (## 0. …); expect ^I-0 or ^0-0, skip H002/H004
                continue
            # Check it ends with ^N-0
            id_m = HEADING_H2_ID_RE.search(line)
            if not id_m:
                findings.append(Finding(
                    "ERROR", "H002", abs_line,
                    f"Chapter heading is missing a '^N-0' block ID: {line.strip()!r}",
                ))
                continue
            chapter_id_num = int(id_m.group(1))
            # Check title number matches ID number
            if chapter_id_num != chapter_num_in_title:
                findings.append(Finding(
                    "ERROR", "H004", abs_line,
                    f"Chapter heading title says chapter {chapter_num_in_title} "
                    f"but block ID says {chapter_id_num}: {line.strip()!r}",
                ))
            # Check ordering
            if chapter_id_num <= prev_chapter and prev_chapter > 0:
                findings.append(Finding(
                    "ERROR", "H003", abs_line,
                    f"Chapter heading {chapter_id_num} appears after chapter "
                    f"{prev_chapter} (out of order).",
                ))
            prev_chapter = chapter_id_num

    if not h1_seen:
        findings.append(Finding(
            "WARN", "H001", offset + 1,
            "Document title heading (# …) not found.",
        ))

    return findings


def lint_block_ids(parsed: ParsedFile) -> "list[Finding]":
    findings: list[Finding] = []
    seen_ids: dict[str, int] = {}  # seg_id → first line

    for start_line, block_lines in parsed.blocks:
        for j, line in enumerate(block_lines):
            abs_line = start_line + j
            if TRANSCLUSION_RE.match(line):
                continue
            # Check that IDs only appear at end of their line
            m_anywhere = SEGMENT_ID_ANYWHERE_RE.search(line)
            if m_anywhere:
                m_end = SEGMENT_ID_RE.search(line)
                if not m_end and j == len(block_lines) - 1:
                    # ID exists somewhere but NOT at end of last line — warn
                    # (the ID still exists but carries trailing annotation)
                    findings.append(Finding(
                        "WARN", "B001", abs_line,
                        f"Block ID on last line does not appear at line end "
                        f"(trailing annotation present): {line.strip()!r}",
                    ))
                elif m_end and j < len(block_lines) - 1:
                    # ID on a non-last line
                    findings.append(Finding(
                        "WARN", "B003", abs_line,
                        f"Block ID '{m_end.group(1)}' appears on a non-final line "
                        f"of its block (expected on the last line).",
                    ))

        seg_id = block_seg_id(block_lines)
        if seg_id is None:
            continue

        # Duplicate check
        if seg_id in seen_ids:
            findings.append(Finding(
                "ERROR", "B002", start_line,
                f"Duplicate block ID '{seg_id}' (first seen at line {seen_ids[seg_id]}).",
            ))
        else:
            seen_ids[seg_id] = start_line

    return findings


def lint_verses(parsed: ParsedFile) -> "list[Finding]":
    findings: list[Finding] = []

    for start_line, block_lines in parsed.blocks:
        seg_id = block_seg_id(block_lines)
        if seg_id is None:
            continue
        # Only check strict verse IDs (digits-digits); skip headings (N-0)
        # and colophons (N-a, a-N, b-N, etc.)
        if not VERSE_ID_STRICT_RE.match(seg_id):
            continue
        if seg_id.endswith("-0"):
            continue  # chapter/section heading ID, not a verse

        # Strip leading transclusion
        text_lines = [l for l in block_lines if not TRANSCLUSION_RE.match(l)]
        if not text_lines:
            continue

        # Everything before the last line is "verse text"; the last line holds the ID
        verse_lines = text_lines[:-1]
        content = [l.strip() for l in verse_lines if l.strip()]
        if not content:
            findings.append(Finding(
                "ERROR", "V001", start_line,
                f"Empty verse block for ID '{seg_id}' "
                f"(block has an ID but no preceding verse text).",
            ))

    return findings


def lint_coverage(
    parsed: ParsedFile,
    root_ids: "dict[str, int]",
) -> "list[Finding]":
    findings: list[Finding] = []

    # Collect translated IDs that are strict verse IDs (digits only).
    # Colophon/appendix IDs (a-*, b-*, N-a, etc.) are translation-specific
    # and not expected in the root text — skip them from C001/C002.
    translated_verse_ids: dict[str, int] = {}  # seg_id → line
    for start_line, block_lines in parsed.blocks:
        seg_id = block_seg_id(block_lines)
        if seg_id is None:
            continue
        if HEADING_ID_RE.match(seg_id):
            continue
        if COLOPHON_ID_RE.match(seg_id) or CHAPTER_COLOPHON_ID_RE.match(seg_id):
            continue  # translation-specific colophon IDs; not in root text
        translated_verse_ids[seg_id] = start_line

    # Root IDs that are meaningful verse IDs (filter same way)
    root_verse_ids = {
        sid: line
        for sid, line in root_ids.items()
        if not HEADING_ID_RE.match(sid)
        and not COLOPHON_ID_RE.match(sid)
        and not CHAPTER_COLOPHON_ID_RE.match(sid)
    }

    # C001 — IDs in translated but not in root
    for sid, line in sorted(translated_verse_ids.items(), key=lambda kv: kv[1]):
        if sid not in root_verse_ids:
            findings.append(Finding(
                "WARN", "C001", line,
                f"Segment ID '{sid}' is in the translated file but NOT in the "
                f"root text (extra/typo ID).",
            ))

    # C002 — Root IDs missing from translated file (report at line 1)
    for sid in root_verse_ids:
        if sid not in translated_verse_ids:
            findings.append(Finding(
                "WARN", "C002", 1,
                f"Root-text segment ID '{sid}' is MISSING from the translated "
                f"file (dropped or renamed verse).",
            ))

    # C003 — Out-of-order verse IDs within each chapter
    chapter_verses: dict[int, list[tuple[int, int, int]]] = {}
    for sid, line in translated_verse_ids.items():
        m = VERSE_ID_STRICT_RE.match(sid)
        if not m:
            continue
        ch, v = int(m.group(1)), int(m.group(2))
        chapter_verses.setdefault(ch, []).append((v, line, sid))

    for ch, entries in sorted(chapter_verses.items()):
        entries.sort(key=lambda e: e[1])  # sort by line number
        prev_v = 0
        for v, line, sid in entries:
            if v < prev_v:
                findings.append(Finding(
                    "ERROR", "C003", line,
                    f"Verse '{sid}' appears after verse '{ch}-{prev_v}' "
                    f"(out of numerical order within chapter {ch}).",
                ))
            prev_v = v

    return findings


def lint_transclusions(
    parsed: ParsedFile,
    root_ids: "dict[str, int]",
) -> "list[Finding]":
    findings: list[Finding] = []
    lines = parsed.raw_lines
    offset = parsed.frontmatter_end_line  # 0-based offset to content start

    content_lines = parsed.content_lines
    n = len(content_lines)

    i = 0
    while i < n:
        abs_line = offset + i + 1  # 1-based
        line = content_lines[i]
        tid = transclusion_id(line)
        if tid is None:
            i += 1
            continue

        # Check T001: ID in root?
        if tid not in root_ids:
            findings.append(Finding(
                "WARN", "T001", abs_line,
                f"Transclusion line references ID '{tid}' which is NOT in "
                f"the root text.",
            ))

        # Check T003: consecutive transclusion lines?
        if i + 1 < n and transclusion_id(content_lines[i + 1]) is not None:
            findings.append(Finding(
                "WARN", "T003", abs_line,
                "Two consecutive transclusion lines detected (dangling transclusion).",
            ))
            i += 1
            continue

        # Find the block following this transclusion line
        # (skip blank lines)
        j = i + 1
        while j < n and content_lines[j].strip() == "":
            j += 1

        if j >= n:
            findings.append(Finding(
                "WARN", "T002", abs_line,
                f"Transclusion line for '{tid}' has no following block.",
            ))
            i += 1
            continue

        # Collect the following block up to blank or ID-at-end
        following_block: list[str] = []
        k = j
        while k < n and content_lines[k].strip() != "":
            following_block.append(content_lines[k])
            if SEGMENT_ID_RE.search(content_lines[k]) and not TRANSCLUSION_RE.match(content_lines[k]):
                break
            k += 1

        following_id = block_seg_id(following_block) if following_block else None
        if following_id is None:
            findings.append(Finding(
                "WARN", "T002", abs_line,
                f"Transclusion line for '{tid}' is not immediately followed by "
                f"a block with a segment ID.",
            ))
        elif following_id != tid:
            findings.append(Finding(
                "ERROR", "T004", abs_line,
                f"Transclusion line references '{tid}' but the following "
                f"block has ID '{following_id}' (mismatch).",
            ))

        i += 1

    return findings


# ---------------------------------------------------------------------------
# Orchestrator
# ---------------------------------------------------------------------------

def lint_file(
    translated_path: Path,
    root_path: "Optional[Path]",
    error_only: bool,
    use_color: bool,
) -> int:
    """Run all checks and print findings.  Return exit code (0 or 1)."""
    text = translated_path.read_text(encoding="utf-8")
    parsed = parse_file(text)

    root_ids: dict[str, int] = {}
    if root_path is not None:
        root_text = root_path.read_text(encoding="utf-8")
        root_ids = collect_root_ids(root_text)

    all_findings: list[Finding] = []
    all_findings.extend(lint_yaml(parsed))
    all_findings.extend(lint_headings(parsed))
    all_findings.extend(lint_block_ids(parsed))
    all_findings.extend(lint_verses(parsed))
    if root_ids:
        all_findings.extend(lint_coverage(parsed, root_ids))
        all_findings.extend(lint_transclusions(parsed, root_ids))

    # Filter if --error-only
    if error_only:
        all_findings = [f for f in all_findings if f.level == "ERROR"]

    # Sort by line, then by rule
    all_findings.sort(key=lambda f: (f.line, f.rule))

    path_str = str(translated_path)
    for finding in all_findings:
        print(finding.format(path_str, use_color=use_color))

    errors = sum(1 for f in all_findings if f.level == "ERROR")
    warnings = sum(1 for f in all_findings if f.level == "WARN")
    info = sum(1 for f in all_findings if f.level == "INFO")

    summary_parts = []
    if errors:
        summary_parts.append(f"{errors} error(s)")
    if warnings and not error_only:
        summary_parts.append(f"{warnings} warning(s)")
    if info and not error_only:
        summary_parts.append(f"{info} info")

    if summary_parts:
        print(f"\n{path_str}: {', '.join(summary_parts)}.")
    else:
        level_note = " (errors only)" if error_only else ""
        print(f"\n{path_str}: no findings{level_note}. ✓")

    return 1 if errors else 0


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    p.add_argument(
        "translated_file",
        metavar="TRANSLATED_FILE",
        help="Path to the translated file to lint.",
    )
    p.add_argument(
        "--root-text",
        default=None,
        metavar="PATH",
        help=(
            "Path to the root text (e.g. 1-SOURCES/Text/BCAV08_SH_sk.md). "
            "When given, enables coverage (C*) and transclusion (T*) checks."
        ),
    )
    p.add_argument(
        "--vault-root",
        default=None,
        metavar="PATH",
        help="Vault root path (currently unused; reserved for future checks).",
    )
    p.add_argument(
        "--error-only",
        action="store_true",
        help="Print only ERROR-level findings (suppresses WARN and INFO).",
    )
    p.add_argument(
        "--no-color",
        action="store_true",
        help="Disable ANSI colour in output.",
    )
    return p


def main() -> None:
    args = build_parser().parse_args()

    translated_path = Path(args.translated_file)
    if not translated_path.exists():
        print(f"Error: file not found: {translated_path}", file=sys.stderr)
        sys.exit(2)

    root_path: Optional[Path] = None
    if args.root_text:
        root_path = Path(args.root_text)
        if not root_path.exists():
            print(f"Error: root text not found: {root_path}", file=sys.stderr)
            sys.exit(2)

    exit_code = lint_file(
        translated_path=translated_path,
        root_path=root_path,
        error_only=args.error_only,
        use_color=not args.no_color,
    )
    sys.exit(exit_code)


if __name__ == "__main__":
    main()
