#!/usr/bin/env python3
"""
structure.py — parse a block-ID'd Railroads source file into an addressable tree.

Every file in `1-SOURCES/` follows the vault convention documented in
`4-SYSTEM/CLAUDE.md` §5 and §5a:

    ---
    <yaml frontmatter>
    ---

    # <title> ^0

    ## 0. <intro heading> ^I-0

    <text> ^I-1

    ## 1. <chapter heading> ^1-0

    ![[1-SOURCES/Text/BCAV08_SH_sk.md#^1-1]]      <- optional transclusion
    <line 1>
    <line 2>
    <line 3>
    <line 4> ^1-1

This module turns that into `Document` -> `Section` -> `Block`, so the
translation driver can address any block by ID, know exactly how many lines it
must produce, and reassemble output in source order.

Nothing here is BCA-specific: any source file that follows the convention parses.
"""

from __future__ import annotations

import re
from dataclasses import dataclass, field
from pathlib import Path

# A block ID is the last token on a line: `^1-1`, `^I-3`, `^10-a`, `^0`.
BLOCK_ID_RE = re.compile(r"\^([0-9A-Za-z]+(?:-[0-9A-Za-z]+)*)\s*$")
HEADING_RE = re.compile(r"^(#{1,6})\s+(.*)$")
TRANSCLUSION_RE = re.compile(r"^!\[\[.*\]\]\s*$")

TIBETAN_RE = re.compile(r"[ༀ-࿿]")
DEVANAGARI_RE = re.compile(r"[ऀ-ॿ]")
CJK_RE = re.compile(r"[一-鿿]")


@dataclass
class Block:
    """One addressable content block: a verse stanza or a prose unit."""

    block_id: str
    lines: list[str]                 # content lines, transclusion stripped
    transclusions: list[str] = field(default_factory=list)
    is_heading: bool = False
    heading_level: int = 0
    heading_prefix: str = ""         # e.g. "1." from "## 1. Chapter ^1-0"

    @property
    def line_count(self) -> int:
        return len(self.lines)

    @property
    def text(self) -> str:
        return "\n".join(self.lines)

    def stripped_lines(self) -> list[str]:
        """Content lines with the trailing block ID removed from the last one."""
        out = [ln.rstrip() for ln in self.lines]
        if out:
            out[-1] = BLOCK_ID_RE.sub("", out[-1]).rstrip()
        return out


@dataclass
class Section:
    """A `##`-level division: front matter, a chapter, or back matter."""

    key: str                         # "I", "1" .. "10", "a", "b"
    heading: Block | None
    blocks: list[Block] = field(default_factory=list)

    @property
    def is_chapter(self) -> bool:
        return self.key.isdigit()

    @property
    def chapter_number(self) -> int | None:
        return int(self.key) if self.key.isdigit() else None

    @property
    def block_ids(self) -> list[str]:
        return [b.block_id for b in self.blocks]

    @property
    def char_count(self) -> int:
        return sum(len(b.text) for b in self.blocks)


@dataclass
class Document:
    path: Path
    frontmatter: str                 # raw YAML text, without the `---` fences
    title: Block | None              # the `# … ^0` line
    sections: list[Section] = field(default_factory=list)

    def section(self, key: str) -> Section | None:
        for s in self.sections:
            if s.key == key:
                return s
        return None

    def chapters(self) -> list[Section]:
        return [s for s in self.sections if s.is_chapter]

    def block_map(self) -> dict[str, Block]:
        out: dict[str, Block] = {}
        if self.title:
            out[self.title.block_id] = self.title
        for s in self.sections:
            if s.heading:
                out[s.heading.block_id] = s.heading
            for b in s.blocks:
                out[b.block_id] = b
        return out


# ---------------------------------------------------------------------------
# parsing
# ---------------------------------------------------------------------------


def split_frontmatter(text: str) -> tuple[str, str]:
    """Return (frontmatter_without_fences, body)."""
    if not text.lstrip().startswith("---"):
        return "", text
    stripped = text.lstrip("﻿")
    parts = stripped.split("---", 2)
    if len(parts) < 3:
        return "", text
    return parts[1].strip("\n"), parts[2].lstrip("\n")


def _section_key(block_id: str) -> str:
    """`^1-0` -> "1"; `^I-0` -> "I"; `^a-0` -> "a"."""
    return block_id.split("-", 1)[0]


def _make_heading_block(line: str) -> Block | None:
    m = HEADING_RE.match(line.strip())
    if not m:
        return None
    level = len(m.group(1))
    rest = m.group(2).strip()
    idm = BLOCK_ID_RE.search(rest)
    block_id = idm.group(1) if idm else ""
    text = BLOCK_ID_RE.sub("", rest).rstrip()
    prefix = ""
    pm = re.match(r"^(\d+\.)\s+", text)
    if pm:
        prefix = pm.group(1)
    return Block(
        block_id=block_id,
        lines=[line.rstrip()],
        is_heading=True,
        heading_level=level,
        heading_prefix=prefix,
    )


def parse_document(path: str | Path) -> Document:
    p = Path(path)
    raw = p.read_text(encoding="utf-8").replace("\r\n", "\n")
    fm, body = split_frontmatter(raw)

    doc = Document(path=p, frontmatter=fm, title=None)
    current: Section | None = None

    for para in re.split(r"\n\s*\n", body):
        lines = [ln for ln in para.split("\n") if ln.strip()]
        if not lines:
            continue

        # A heading paragraph.
        if HEADING_RE.match(lines[0].strip()):
            hb = _make_heading_block(lines[0])
            if hb is None:
                continue
            if hb.heading_level == 1:
                doc.title = hb
                continue
            if hb.heading_level == 2:
                current = Section(key=_section_key(hb.block_id), heading=hb)
                doc.sections.append(current)
                continue
            # `###`/`####` sub-headings ride along inside the current section
            if current is not None:
                current.blocks.append(hb)
            continue

        # A content paragraph.
        transclusions: list[str] = []
        while lines and TRANSCLUSION_RE.match(lines[0].strip()):
            transclusions.append(lines.pop(0).strip())
        if not lines:
            continue
        idm = BLOCK_ID_RE.search(lines[-1])
        if not idm:
            # Un-stamped prose; keep it addressable by position but do not
            # let it collide with real block IDs.
            continue
        block = Block(
            block_id=idm.group(1),
            lines=[ln.rstrip() for ln in lines],
            transclusions=transclusions,
        )
        if current is None:
            current = Section(key="_pre", heading=None)
            doc.sections.append(current)
        current.blocks.append(block)

    return doc


def parse_block_map(path: str | Path) -> dict[str, list[str]]:
    """Lightweight parse of a reference file: {block_id: [content lines]}."""
    doc = parse_document(path)
    out: dict[str, list[str]] = {}
    for section in doc.sections:
        for b in section.blocks:
            if not b.is_heading:
                out[b.block_id] = b.stripped_lines()
    return out


def script_report(text: str) -> dict[str, bool]:
    """Which non-Latin scripts appear in `text` — used by the output validator."""
    return {
        "tibetan": bool(TIBETAN_RE.search(text)),
        "devanagari": bool(DEVANAGARI_RE.search(text)),
        "cjk": bool(CJK_RE.search(text)),
    }


if __name__ == "__main__":  # quick structural audit
    import sys

    for arg in sys.argv[1:]:
        d = parse_document(arg)
        print(f"\n{d.path.name}")
        print(f"  frontmatter lines : {len(d.frontmatter.splitlines())}")
        print(f"  title             : {d.title.block_id if d.title else '—'}")
        print(f"  sections          : {len(d.sections)}")
        for s in d.sections:
            n_lines = sum(b.line_count for b in s.blocks if not b.is_heading)
            print(f"    ^{s.key:<4} blocks={len(s.blocks):<4} lines={n_lines:<5} "
                  f"chars={s.char_count}")
