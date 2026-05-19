#!/usr/bin/env python3
"""
json_to_source_text.py — shared formatting helpers for JSON-to-source-text
converters in this skill's `converters/` folder.

Each source schema (tipitaka.org, SuttaCentral, BDRC, …) gets its own
converter that imports these helpers and implements its own routing logic.

Exports:
    format_frontmatter(meta: dict) -> str
    format_chapter_heading(num: int, title: str) -> str
    format_subsection_heading(chapter: int, section: int, title: str) -> str
    format_subsubsection_heading(chapter: int, section: int, sub: int, title: str) -> str
    format_verse(content: str, chapter: int, verse: int) -> str
    clean_text(s: str) -> str
"""

from __future__ import annotations
import re


def format_frontmatter(meta: dict) -> str:
    """Render a YAML frontmatter block. Strips None/empty values."""
    lines = ["---"]
    for k, v in meta.items():
        if v is None or v == "":
            continue
        if isinstance(v, list):
            if not v:
                continue
            lines.append(f"{k}:")
            for item in v:
                lines.append(f"  - {item}")
        elif isinstance(v, (int, float, bool)):
            lines.append(f"{k}: {v}")
        else:
            s = str(v)
            if any(c in s for c in ":#\"'\n") or s.strip() != s:
                s = '"' + s.replace('"', '\\"') + '"'
            lines.append(f"{k}: {s}")
    lines.append("---")
    return "\n".join(lines) + "\n"


def format_chapter_heading(num: int, title: str) -> str:
    """## N. title ^N-0"""
    return f"## {num}. {title.strip()} ^{num}-0\n"


def format_subsection_heading(chapter: int, section: int, title: str) -> str:
    """### N.M title ^N-M-0"""
    return f"### {chapter}.{section} {title.strip()} ^{chapter}-{section}-0\n"


def format_subsubsection_heading(chapter: int, section: int, sub: int, title: str) -> str:
    """#### N.M.K title ^N-M-K-0

    For sources with three levels of structural hierarchy (e.g. tipitaka.org's
    chapter / title / subhead distinction). The 4-component block ID does not
    collide with verse IDs (verses are 2 or 3 components and never end in 0).
    """
    return f"#### {title.strip()} ^{chapter}-{section}-{sub}-0\n"


def format_verse(content: str, path, verse: int) -> str:
    """content ^path-verse

    `path` is a heading path: either an int (chapter only, e.g. 1) or a
    hyphen-joined string (any depth, e.g. "1-2-3"). Verse IDs carry the full
    path of the enclosing heading, so verses under heading ^1-2-3-0 are
    ^1-2-3-1, ^1-2-3-2, …, and a verse directly under chapter 0 is ^0-1.
    """
    return f"{content.rstrip()} ^{path}-{verse}\n"


_ws_re = re.compile(r"[ \t]+")


def clean_text(s: str) -> str:
    s = s.replace("\r\n", "\n").replace("\r", "\n")
    s = _ws_re.sub(" ", s)
    return s.strip()
