#!/usr/bin/env python3
"""Build a single reader text with verse character spans from source markdown.

Transforms the markdown into ``metadata``, one ``content`` string, and a ``verse``
array. Each segment gets a verse entry with ``start``/``end`` character offsets
inside ``content`` (headers included). Spans tile the full ``content`` string
from offset 0 with no gaps.

- Parses YAML frontmatter into a ``metadata`` object
- Converts markdown headings to HTML: # -> <h2>, ## -> <h3>, …, #####/###### -> <h6>
- Removes leading item numbers (e.g. ``1. ``, ``142. ``)
- Removes trailing block ids (``^1-0a-1``) from visible text; ids live in ``verse``
- Inserts `` ⤵`` between consecutive ``(A)``/``(B)``/``(C)``/``(D)`` sub-clause lines
- Segments without a ``^`` block id get ``id: null`` in ``verse``
"""

from __future__ import annotations

import argparse
import html
import json
import re
import sys
from pathlib import Path

DEFAULT_INPUT = (
    Path(__file__).resolve().parent.parent
    / "1-SOURCES/Translations/zh-隆蓮法師a.md"
)
DEFAULT_OUTPUT = Path(__file__).resolve().parent / "data/zh-隆蓮法師a.json"

CONTRIBUTION_FIELDS = (
    ("author", "author"),
    ("translator", "translator"),
    ("commentary_by", "commentator"),
    ("reviewed_by", "reviewer"),
    ("preface_by", "preface_author"),
    ("editors", "editor"),
)

METADATA_COPYRIGHT = "Public domain"
METADATA_LICENSE = "CC0"

HEADER_RE = re.compile(r"^(#{1,6})\s+(.+)$")
BLOCK_ID_RE = re.compile(r"\s+\^([\w]+(?:-[\w]+)*)\s*$")
VERSE_NUMBER_RE = re.compile(r"^\d+\.\s+")
SUBCLAUSE_LINE_RE = re.compile(r"^\([A-D]\)")
SUBCLAUSE_JOINER = " ⤵"

# Markdown # is book-level here; shift down so # -> h2 … ##### -> h6.
HEADER_TAG = {1: "h2", 2: "h3", 3: "h4", 4: "h5", 5: "h6", 6: "h6"}

SEGMENT_JOINER = "\n\n"


def split_frontmatter(text: str) -> tuple[dict[str, str], str]:
    if not text.startswith("---"):
        return {}, text

    end = text.find("\n---", 3)
    if end == -1:
        return {}, text

    block = text[3:end].lstrip("\n")
    body = text[end + 4 :].lstrip("\n")
    frontmatter: dict[str, str] = {}

    for line in block.splitlines():
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        if ":" not in line:
            continue
        key, _, value = line.partition(":")
        key = key.strip()
        value = value.strip()
        if not key:
            continue
        if len(value) >= 2 and value[0] == value[-1] and value[0] in "\"'":
            value = value[1:-1]
        frontmatter[key] = value

    return frontmatter, body


def _metadata_type(file_type: str | None) -> str:
    if file_type in {"root-text", "root"}:
        return "root"
    if file_type:
        return file_type
    return "text"


def _metadata_language(frontmatter: dict[str, str]) -> str:
    if lang_tag := frontmatter.get("lang_tag"):
        return lang_tag
    language = frontmatter.get("language", "")
    language_map = {
        "sanskrit": "sk",
        "chinese": "zh",
        "tibetan": "bo",
        "english": "en",
    }
    return language_map.get(language.lower(), language.lower() or "und")


def _metadata_title(frontmatter: dict[str, str]) -> dict[str, str]:
    title = frontmatter.get("title")
    if not title:
        return {}

    language = _metadata_language(frontmatter)
    titles = {language: title}

    if "en" not in titles:
        titles["en"] = "Bodhisattvacaryāvatāra"

    return titles


def _metadata_contributions(
    frontmatter: dict[str, str],
    person_ids: dict[str, str],
) -> list[dict[str, str]]:
    contributions: list[dict[str, str]] = []

    for field, role in CONTRIBUTION_FIELDS:
        name = frontmatter.get(field)
        if not name:
            continue
        entry: dict[str, str] = {"role": role}
        person_id = person_ids.get(field) or person_ids.get(role)
        if person_id:
            entry["person_id"] = person_id
        else:
            entry["name"] = name
        contributions.append(entry)

    return contributions


def build_text_metadata(
    frontmatter: dict[str, str],
    *,
    person_ids: dict[str, str] | None = None,
    category_id: str | None = None,
) -> dict:
    person_ids = person_ids or {}
    metadata: dict = {
        "type": _metadata_type(frontmatter.get("file_type")),
        "title": _metadata_title(frontmatter),
        "language": _metadata_language(frontmatter),
        "copyright": METADATA_COPYRIGHT,
        "license": METADATA_LICENSE,
    }

    contributions = _metadata_contributions(frontmatter, person_ids)
    if contributions:
        metadata["contributions"] = contributions

    for source_key, target_key in (
        ("translation_date", "date"),
        ("publication_history", "date"),
        ("bdrc_work_id", "bdrc"),
    ):
        value = frontmatter.get(source_key)
        if value and target_key not in metadata:
            metadata[target_key] = value

    if category_id:
        metadata["category_id"] = category_id

    if cbeta_id := frontmatter.get("cbeta_id"):
        metadata["cbeta"] = cbeta_id

    return metadata


def split_block_id(line: str) -> tuple[str, str | None]:
    match = BLOCK_ID_RE.search(line)
    if not match:
        return line, None
    return line[: match.start()].rstrip(), match.group(1)


def header_html(level: int, title: str) -> str:
    tag = HEADER_TAG[level]
    return f"<{tag}>{html.escape(title)}</{tag}>"


def join_paragraph_lines(lines: list[str]) -> str:
    """Join paragraph lines, marking consecutive (A)/(B)/(C)/(D) sub-clauses."""
    if not lines:
        return ""
    if len(lines) == 1:
        return lines[0]

    parts: list[str] = []
    for index, line in enumerate(lines):
        stripped = line.lstrip()
        next_line = lines[index + 1] if index + 1 < len(lines) else None
        parts.append(line)
    return "⤵".join(parts)


class ReaderBuilder:
    def __init__(self) -> None:
        self.content = ""
        self.verse: list[dict] = []
        self._paragraph_lines: list[str] = []

    def _append_segment(self, text: str, block_id: str | None) -> None:
        if not text:
            return
        if self.content and self.verse:
            self.verse[-1]["span"]["end"] = len(self.content)
        start = len(self.content)
        self.content += text
        end = len(self.content)
        self.verse.append(
            {"id": block_id, "span": {"start": start, "end": end}}
        )

    def _flush_paragraph(self, block_id: str | None = None) -> None:
        if not self._paragraph_lines:
            return
        text = join_paragraph_lines(self._paragraph_lines)
        self._append_segment(text, block_id)
        self._paragraph_lines = []

    def add_header(self, level: int, raw_title: str) -> None:
        self._flush_paragraph()
        title, block_id = split_block_id(raw_title)
        self._append_segment(header_html(level, title), block_id)

    def add_body_line(self, raw_line: str) -> None:
        if VERSE_NUMBER_RE.match(raw_line):
            self._flush_paragraph()
            raw_line = VERSE_NUMBER_RE.sub("", raw_line)
        text, block_id = split_block_id(raw_line)
        self._paragraph_lines.append(text)
        if block_id is not None:
            self._flush_paragraph(block_id)

    def finish(self) -> dict[str, object]:
        self._flush_paragraph()
        return {"content": self.content, "verse": self.verse}


def build_reader_document(
    text: str,
    *,
    person_ids: dict[str, str] | None = None,
    category_id: str | None = None,
) -> dict:
    frontmatter, body = split_frontmatter(text)
    builder = ReaderBuilder()

    for raw_line in body.splitlines():
        line = raw_line.rstrip()
        if not line:
            continue

        header_match = HEADER_RE.match(line)
        if header_match:
            builder.add_header(len(header_match.group(1)), header_match.group(2))
            continue

        builder.add_body_line(line)

    document = builder.finish()
    document["metadata"] = build_text_metadata(
        frontmatter,
        person_ids=person_ids,
        category_id=category_id,
    )
    return document


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--input",
        type=Path,
        default=DEFAULT_INPUT,
        help=f"Source markdown file (default: {DEFAULT_INPUT.name})",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=DEFAULT_OUTPUT,
        help=f"Destination JSON file (default: {DEFAULT_OUTPUT.name})",
    )
    parser.add_argument(
        "--category-id",
        help="Category identifier for metadata.category_id",
    )
    parser.add_argument(
        "--person-id",
        action="append",
        default=[],
        metavar="ROLE=ID",
        help="Map a contribution role or frontmatter field to a person_id "
        "(e.g. author=P12345678, translator=P87654321)",
    )
    args = parser.parse_args()

    person_ids: dict[str, str] = {}
    for item in args.person_id:
        if "=" not in item:
            print(f"Invalid --person-id (expected ROLE=ID): {item}", file=sys.stderr)
            sys.exit(1)
        role, person_id = item.split("=", 1)
        person_ids[role.strip()] = person_id.strip()

    try:
        source = args.input.read_text(encoding="utf-8")
    except OSError as exc:
        print(exc, file=sys.stderr)
        sys.exit(1)

    document = build_reader_document(
        source,
        person_ids=person_ids,
        category_id=args.category_id,
    )

    args.output.parent.mkdir(parents=True, exist_ok=True)
    ordered = {
        "metadata": document["metadata"],
        "content": document["content"],
        "verse": document["verse"],
    }
    args.output.write_text(
        json.dumps(ordered, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    print(
        f"Wrote {args.output} "
        f"({len(document['content'])} chars, {len(document['verse'])} verses, "
        f"type={document['metadata']['type']})"
    )


if __name__ == "__main__":
    main()
