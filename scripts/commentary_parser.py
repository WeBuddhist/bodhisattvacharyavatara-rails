#!/usr/bin/env python3
"""Build a reader JSON file from a commentary markdown source.

Like ``build_reader_json.py``, this transforms markdown into ``metadata``,
one ``content`` string, and a ``verse`` array of character spans into
``content`` (headers included, tiling the full string with no gaps).

Differences from ``build_reader_json.py`` (commentary-specific):

- Frontmatter ``file_type: commentary`` -> ``metadata.type = "commentary"``.
- ``source_description`` frontmatter (e.g. copyright/attribution notice for
  the commentary) -> ``metadata.copyright``, instead of assuming the
  "Public domain" / "CC0" defaults used for root/translation texts.
- The top-level ``# Title`` heading is dropped (it duplicates
  ``metadata.title``).
- The "## 目次" (table of contents) section is skipped entirely, along with
  everything under it, up to the next top-level (``##``) heading.
- Root-text embed references such as
  ``![[1-SOURCES/Translations/zh-隆蓮法師a.md#^1-1]]`` are dropped -- they
  point at the translation, not the commentary's own text.
- Horizontal rules (``---``, ``***``, ``___`` on their own line) are dropped.
- Footnote definitions (``[^1]: …``, ``[^2]: …``, etc.) are dropped.
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
    / "1-SOURCES/Commentaries/zh-入菩薩行論（宗薩蔣揚欽哲仁波切）.md"
)
DEFAULT_OUTPUT = (
    Path(__file__).resolve().parent
    / "data/zh-commentary-入菩薩行論（宗薩蔣揚欽哲仁波切）.json"
)

CONTRIBUTION_FIELDS = (
    ("author", "author"),
    ("translator", "translator"),
    ("commentary_by", "commentator"),
    ("reviewed_by", "reviewer"),
    ("preface_by", "preface_author"),
    ("editors", "editor"),
)

HEADER_RE = re.compile(r"^(#{1,6})\s+(.+)$")
BLOCK_ID_RE = re.compile(r"\s+\^([\w]+(?:-[\w]+)*)\s*$")
VERSE_NUMBER_RE = re.compile(r"^\d+\.\s+")
SUBCLAUSE_LINE_RE = re.compile(r"^\([A-D]\)")
EMBED_RE = re.compile(r"^!\[\[.*\]\]$")
HR_RE = re.compile(r"^(-{3,}|\*{3,}|_{3,})$")
FOOTNOTE_DEF_RE = re.compile(r"^\[\^\d+\]:")
TOC_TITLES = {"目次", "目錄"}

# Markdown # is book-level here; shift down so # -> h2 … ##### -> h6.
HEADER_TAG = {1: "h2", 2: "h3", 3: "h4", 4: "h5", 5: "h6", 6: "h6"}


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
    return {language: title}


def _metadata_contributions(frontmatter: dict[str, str]) -> list[dict[str, str]]:
    contributions: list[dict[str, str]] = []

    for field, role in CONTRIBUTION_FIELDS:
        name = frontmatter.get(field)
        if not name:
            continue
        contributions.append({"role": role, "name": name})

    return contributions


def build_commentary_metadata(frontmatter: dict[str, str]) -> dict:
    metadata: dict = {
        "type": _metadata_type(frontmatter.get("file_type")),
        "title": _metadata_title(frontmatter),
        "language": _metadata_language(frontmatter),
    }

    contributions = _metadata_contributions(frontmatter)
    if contributions:
        metadata["contributions"] = contributions

    if source_description := frontmatter.get("source_description"):
        metadata["copyright"] = source_description

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
    if not lines:
        return ""
    if len(lines) == 1:
        return lines[0]
    return "⤵".join(lines)


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
        self.verse.append({"id": block_id, "span": {"start": start, "end": end}})

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

    def paragraph_break(self) -> None:
        """Called when a blank line is encountered in the source.

        Flushes the accumulated paragraph only when its last line ends with a
        sentence-final punctuation character (。！？), which indicates a genuine
        paragraph boundary.  A blank line whose preceding line ends mid-word or
        mid-clause is treated as a soft wrap and leaves the accumulator intact.
        """
        if not self._paragraph_lines:
            return
        last = self._paragraph_lines[-1]
        if last and last[-1] in "。！？":
            self._flush_paragraph()

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


def build_commentary_document(text: str) -> dict:
    frontmatter, body = split_frontmatter(text)
    builder = ReaderBuilder()

    skip_toc = False

    for raw_line in body.splitlines():
        line = raw_line.rstrip()
        if not line:
            builder.paragraph_break()
            continue

        header_match = HEADER_RE.match(line)
        if header_match:
            level = len(header_match.group(1))
            title = header_match.group(2).strip()

            if level <= 2:
                skip_toc = title in TOC_TITLES

            if level == 1:
                # Top-level document title duplicates metadata.title.
                continue
            if skip_toc:
                continue

            builder.add_header(level - 1, title)
            continue

        if skip_toc:
            continue

        if EMBED_RE.match(line):
            # Root-text embed reference, e.g.
            # ![[1-SOURCES/Translations/zh-隆蓮法師a.md#^1-1]]
            continue

        if HR_RE.match(line):
            continue

        if FOOTNOTE_DEF_RE.match(line):
            continue

        builder.add_body_line(line)

    document = builder.finish()
    document["metadata"] = build_commentary_metadata(frontmatter)
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
    args = parser.parse_args()

    try:
        source = args.input.read_text(encoding="utf-8")
    except OSError as exc:
        print(exc, file=sys.stderr)
        sys.exit(1)

    document = build_commentary_document(source)

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
    summary = (
        f"Wrote {args.output} "
        f"({len(document['content'])} chars, {len(document['verse'])} segments, "
        f"type={document['metadata']['type']})"
    )
    sys.stdout.buffer.write(summary.encode("utf-8"))
    sys.stdout.buffer.write(b"\n")


if __name__ == "__main__":
    main()
