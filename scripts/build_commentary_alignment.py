#!/usr/bin/env python3
"""Build commentary-to-root alignment for 宗薩蔣揚欽哲仁波切 (and similar texts).

In the commentary markdown, blocks of commentary text are preceded by one or
more root-text embed references like:

    ![[1-SOURCES/Translations/zh-隆蓮法師a.md#^1-1]]

Alignment rules
---------------
* The commentary text that follows root embed(s) is aligned to those root
  verse(s), until the next root embed or markdown heading.
* Multiple consecutive root embeds before any commentary → one commentary
  block aligned to all of those root verses.
* target_annotation[*].span  = root verse character span
                                 (from the root reader JSON)
* alignment_annotation.span    = merged commentary character span
                                 (into the commentary JSON content string)

Outputs
-------
1. Commentary reader JSON (metadata, content, verse, alignment array).
2. ``<text-name>-commentary-alignment.json`` — API-ready alignment payload
   with indexed ``target_annotation`` (root) and ``alignment_annotation``
   (commentary).
"""

from __future__ import annotations

import argparse
import html
import json
import re
import sys
from pathlib import Path

# ── default paths ────────────────────────────────────────────────────────────

_HERE = Path(__file__).resolve().parent
_REPO = _HERE.parent

DEFAULT_COMMENTARY_MD = (
    _REPO / "1-SOURCES/Commentaries/zh-入菩薩行論（宗薩蔣揚欽哲仁波切）.md"
)
DEFAULT_ROOT_JSON = _HERE / "data/zh-隆蓮法師a.json"
DEFAULT_OUTPUT = _HERE / "data/zh-commentary-入菩薩行論（宗薩蔣揚欽哲仁波切）.json"

# ── regexes (same as commentary_parser.py) ──────────────────────────────────

HEADER_RE = re.compile(r"^(#{1,6})\s+(.+)$")
BLOCK_ID_RE = re.compile(r"\s+\^([\w]+(?:-[\w]+)*)\s*$")
VERSE_NUMBER_RE = re.compile(r"^\d+\.\s+")
ROOT_EMBED_RE = re.compile(
    r"^!\[\[1-SOURCES/Translations/zh-隆蓮法師a\.md#\^([\w-]+)\]\]$"
)
EMBED_ANY_RE = re.compile(r"^!\[\[.*\]\]$")   # catch-all (drop non-root embeds)
HR_RE = re.compile(r"^(-{3,}|\*{3,}|_{3,})$")
FOOTNOTE_DEF_RE = re.compile(r"^\[\^\d+\]:")
TOC_TITLES = {"目次", "目錄"}

# Heading level shift: markdown # is book-level here → h2 … ###### → h6
HEADER_TAG = {1: "h2", 2: "h3", 3: "h4", 4: "h5", 5: "h6", 6: "h6"}


# ── frontmatter ──────────────────────────────────────────────────────────────

def split_frontmatter(text: str) -> tuple[dict[str, str], str]:
    if not text.startswith("---"):
        return {}, text
    end = text.find("\n---", 3)
    if end == -1:
        return {}, text
    block = text[3:end].lstrip("\n")
    body = text[end + 4:].lstrip("\n")
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


def _metadata_language(fm: dict[str, str]) -> str:
    if lang_tag := fm.get("lang_tag"):
        return lang_tag
    lang = fm.get("language", "")
    return {"sanskrit": "sk", "chinese": "zh", "tibetan": "bo", "english": "en"}.get(
        lang.lower(), lang.lower() or "und"
    )


def build_metadata(fm: dict[str, str]) -> dict:
    file_type = fm.get("file_type", "text")
    if file_type in {"root-text", "root"}:
        file_type = "root"
    lang = _metadata_language(fm)
    meta: dict = {"type": file_type, "language": lang}
    if title := fm.get("title"):
        meta["title"] = {lang: title}
    contribs = []
    for field, role in [
        ("author", "author"), ("translator", "translator"),
        ("commentary_by", "commentator"), ("reviewed_by", "reviewer"),
        ("preface_by", "preface_author"), ("editors", "editor"),
    ]:
        if name := fm.get(field):
            contribs.append({"role": role, "name": name})
    if contribs:
        meta["contributions"] = contribs
    if src := fm.get("source_description"):
        meta["copyright"] = src
    return meta


# ── tracking builder ─────────────────────────────────────────────────────────

def split_block_id(line: str) -> tuple[str, str | None]:
    m = BLOCK_ID_RE.search(line)
    if not m:
        return line, None
    return line[:m.start()].rstrip(), m.group(1)


def join_paragraph_lines(lines: list[str]) -> str:
    if not lines:
        return ""
    if len(lines) == 1:
        return lines[0]
    return "⤵".join(lines)


class TrackingBuilder:
    """Reproduces ReaderBuilder output and tags each verse with its root IDs."""

    def __init__(self) -> None:
        self.content = ""
        self.verse: list[dict] = []
        self.segment_roots: list[list[str]] = []   # parallel to self.verse
        self._paragraph_lines: list[str] = []
        self._current_root_ids: list[str] = []

    def _append_segment(self, text: str, block_id: str | None) -> None:
        if not text:
            return
        if self.content and self.verse:
            self.verse[-1]["span"]["end"] = len(self.content)
        start = len(self.content)
        self.content += text
        end = len(self.content)
        self.verse.append({"id": block_id, "span": {"start": start, "end": end}})
        self.segment_roots.append(list(self._current_root_ids))

    def _flush_paragraph(self, block_id: str | None = None) -> None:
        if not self._paragraph_lines:
            return
        text = join_paragraph_lines(self._paragraph_lines)
        self._append_segment(text, block_id)
        self._paragraph_lines = []

    def add_header(self, level: int, raw_title: str) -> None:
        self._flush_paragraph()
        title, block_id = split_block_id(raw_title)
        tag = HEADER_TAG[min(level, 6)]
        self._append_segment(f"<{tag}>{html.escape(title)}</{tag}>", block_id)

    def paragraph_break(self) -> None:
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

    def set_roots(self, root_ids: list[str]) -> None:
        """Flush pending paragraph, then change active root IDs."""
        self._flush_paragraph()
        self._current_root_ids = list(root_ids)

    def finish(self) -> None:
        self._flush_paragraph()


# ── parse commentary markdown ────────────────────────────────────────────────

def parse_commentary(md_text: str) -> tuple[dict, str, list[dict], list[list[str]]]:
    """
    Returns:
        metadata        – dict built from frontmatter
        content         – commentary content string (same as commentary_parser.py)
        verse           – list of {id, span} dicts (same as commentary_parser.py)
        segment_roots   – parallel list; each entry is the list of root verse
                          IDs that were "active" when that verse segment was
                          produced (empty list if no root context)
    """
    fm, body = split_frontmatter(md_text)
    builder = TrackingBuilder()

    skip_toc = False
    pending_roots: list[str] = []   # root IDs accumulating before commentary
    has_commentary = False           # have we produced commentary after current pending?

    for raw_line in body.splitlines():
        line = raw_line.rstrip()

        # ── blank line ──────────────────────────────────────────────────────
        if not line:
            builder.paragraph_break()
            continue

        # ── heading ─────────────────────────────────────────────────────────
        hm = HEADER_RE.match(line)
        if hm:
            level = len(hm.group(1))
            title = hm.group(2).strip()

            if level <= 2:
                skip_toc = title in TOC_TITLES

            if level == 1:
                # Drop document-level title; reset state
                builder.set_roots([])
                pending_roots = []
                has_commentary = False
                continue

            if skip_toc:
                continue

            # A heading ends the current root–commentary group.
            # The heading segment itself carries no root IDs.
            builder.set_roots([])
            builder.add_header(level - 1, title)
            pending_roots = []
            has_commentary = False
            continue

        if skip_toc:
            continue

        # ── root embed ──────────────────────────────────────────────────────
        rm = ROOT_EMBED_RE.match(line)
        if rm:
            verse_id = rm.group(1)
            if has_commentary:
                # Commentary already produced after current roots → start new group
                pending_roots = [verse_id]
                has_commentary = False
            else:
                # Accumulate multiple embeds before any commentary
                pending_roots.append(verse_id)
            builder.set_roots(pending_roots)
            continue

        # ── other embeds (non-root) ─────────────────────────────────────────
        if EMBED_ANY_RE.match(line):
            continue

        # ── horizontal rule ─────────────────────────────────────────────────
        if HR_RE.match(line):
            continue

        # ── footnote definition ─────────────────────────────────────────────
        if FOOTNOTE_DEF_RE.match(line):
            continue

        # ── commentary body line ────────────────────────────────────────────
        has_commentary = True
        builder.add_body_line(line)

    builder.finish()
    return build_metadata(fm), builder.content, builder.verse, builder.segment_roots


# ── build alignment entries ──────────────────────────────────────────────────

def build_root_index(root_json: dict) -> dict[str, dict]:
    """Return {verse_id: span} from the root JSON's verse array."""
    index: dict[str, dict] = {}
    for entry in root_json.get("verse", []):
        vid = entry.get("id")
        if vid:
            index[vid] = dict(entry["span"])
    return index


def merge_spans(spans: list[dict]) -> dict:
    return {
        "start": min(s["start"] for s in spans),
        "end": max(s["end"] for s in spans),
    }


def build_alignment(
    verse: list[dict],
    segment_roots: list[list[str]],
    root_index: dict[str, dict],
) -> list[dict]:
    """
    Group consecutive verse segments that share the same non-empty root IDs,
    then emit one alignment entry per commentary block.

    target_annotation[*].span  ← root verse span(s) (from root JSON)
    alignment_annotation.span  ← merged commentary span for the group
    """
    alignment: list[dict] = []

    # Walk segments, collecting runs with identical non-empty roots
    i = 0
    n = len(verse)
    while i < n:
        roots = segment_roots[i]
        if not roots:
            i += 1
            continue

        # Collect all consecutive segments with the same root list
        j = i + 1
        while j < n and segment_roots[j] == roots:
            j += 1

        group_spans = [verse[k]["span"] for k in range(i, j)]
        commentary_span = merge_spans(group_spans)

        root_targets: list[dict] = []
        for root_id in roots:
            root_span = root_index.get(root_id)
            if root_span is None:
                print(
                    f"  Warning: root verse id '{root_id}' not found in root JSON",
                    file=sys.stderr,
                )
                continue
            root_targets.append({"span": root_span})

        if root_targets:
            alignment.append(
                {
                    "target_annotation": root_targets,
                    "alignment_annotation": {"span": commentary_span},
                }
            )

        i = j

    return alignment


def build_alignment_payload(
    alignment: list[dict],
    *,
    target_manifestation_id: str,
) -> dict:
    """Flatten pairwise alignment entries into an API-ready payload."""
    target_annotation: list[dict] = []
    target_index_by_span: dict[tuple[int, int], int] = {}
    alignment_annotation: list[dict] = []

    for align_index, entry in enumerate(alignment):
        alignment_index: list[int] = []

        for target in entry.get("target_annotation", []):
            span = target["span"]
            key = (span["start"], span["end"])
            target_index = target_index_by_span.get(key)
            if target_index is None:
                target_index = len(target_annotation)
                target_index_by_span[key] = target_index
                target_annotation.append({"span": span, "index": target_index})
            alignment_index.append(target_index)

        aa = entry.get("alignment_annotation")
        if not isinstance(aa, dict) or not aa.get("span"):
            continue

        alignment_annotation.append(
            {
                "span": dict(aa["span"]),
                "index": align_index,
                "alignment_index": alignment_index,
            }
        )

    return {
        "type": "alignment",
        "target_manifestation_id": target_manifestation_id,
        "target_annotation": target_annotation,
        "alignment_annotation": alignment_annotation,
    }


def default_alignment_output(commentary_md: Path) -> Path:
    return _HERE / "data" / f"{commentary_md.stem}-commentary-alignment.json"


# ── main ─────────────────────────────────────────────────────────────────────

def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--commentary-md",
        type=Path,
        default=DEFAULT_COMMENTARY_MD,
        help="Commentary markdown source",
    )
    parser.add_argument(
        "--root-json",
        type=Path,
        default=DEFAULT_ROOT_JSON,
        help="Root/translation reader JSON with verse spans",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=DEFAULT_OUTPUT,
        help="Output commentary JSON (default overwrites existing)",
    )
    parser.add_argument(
        "--alignment-output",
        type=Path,
        default=None,
        help="Alignment payload JSON "
        "(default: data/<commentary-md-stem>-commentary-alignment.json)",
    )
    parser.add_argument(
        "--target-manifestation-id",
        default="MNF_PLACEHOLDER",
        help="Root text manifestation id for the alignment payload",
    )
    args = parser.parse_args()

    # Load inputs
    try:
        md_text = args.commentary_md.read_text(encoding="utf-8")
    except OSError as exc:
        sys.exit(f"Cannot read commentary markdown: {exc}")

    try:
        root_json = json.loads(args.root_json.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        sys.exit(f"Cannot read root JSON: {exc}")

    # Parse commentary (single pass)
    metadata, content, verse, segment_roots = parse_commentary(md_text)

    # Build root span index
    root_index = build_root_index(root_json)

    # Build alignment
    alignment = build_alignment(verse, segment_roots, root_index)
    alignment_payload = build_alignment_payload(
        alignment,
        target_manifestation_id=args.target_manifestation_id,
    )

    alignment_output = args.alignment_output or default_alignment_output(
        args.commentary_md
    )

    # Write outputs
    args.output.parent.mkdir(parents=True, exist_ok=True)
    document = {
        "metadata": metadata,
        "content": content,
        "verse": verse,
        "alignment": alignment,
    }
    args.output.write_text(
        json.dumps(document, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )

    alignment_output.parent.mkdir(parents=True, exist_ok=True)
    alignment_output.write_text(
        json.dumps(alignment_payload, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )

    # Summary
    summary = (
        f"Wrote {args.output.name}\n"
        f"Wrote {alignment_output.name}\n"
        f"  content chars       : {len(content)}\n"
        f"  verse segments      : {len(verse)}\n"
        f"  alignment groups    : {len(alignment)}\n"
        f"  root target spans   : {len(alignment_payload['target_annotation'])}\n"
        f"  commentary alignments: {len(alignment_payload['alignment_annotation'])}\n"
    )
    sys.stdout.buffer.write(summary.encode("utf-8"))
    sys.stdout.buffer.write(b"\n")


if __name__ == "__main__":
    main()
