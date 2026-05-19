#!/usr/bin/env python3
"""
tipitaka_org_atthakatha.py — converter for tipitaka.org Atthakatha / Tika book exports.

Produces a Markdown commentary file for 1-SOURCES/Commentaries/ following the
conventions in 4-SYSTEM/Guidelines/source-formatting.md.

OUTPUT STRUCTURE
================

  Namo tassa...                     <- plain text, no ID

  # Abhidhammatake (atthakatha) ^atthakatha-0   <- h1, pitaka
  ## <book title> ^1-0                          <- h2, this commentary book
  ### <chapter title> ^1-<ch>-0                 <- h3, JSON source chapter
  #### <sub-section> ^1-<ch>-<n>-0             <- h4, title/subhead within ch
  ##### <deeper section> ^1-<ch>-<n>-<m>-0     <- h5, subhead after a title

Body verses use a CONTINUOUS counter through the whole file:
  ^1-1, ^1-2, ..., ^1-N  (two-level: book = 1, verse = N)

INLINE ROOT-TEXT REFERENCES
============================

Commentary body segments often open with a number or range that references
the root text:

    "1. Kusala dhamma..."         <- single verse
    "1-6. Dukamatikayam..."       <- range of verses

These numbers are NOT the commentary's own verse numbers. They are root-text
verse IDs. The converter:
  1. Strips the leading "N." or "N-M." prefix from the content.
  2. Resolves each N to a root-text block ID using CHAPTER_ROOT_TEXT_CONTEXT.
  3. Inserts one ![[root_text#^id]] transclusion line per resolved verse,
     before the commentary paragraph.

Pass chapter_context dict to convert_json_to_commentary() to override the
module-level CHAPTER_ROOT_TEXT_CONTEXT for a specific file.

GATHA HANDLING
==============

CSS classes gatha1 / gatha2 / gatha3 / gathalast are verse lines. Lines
accumulate until gathalast, which closes the stanza. One block ID is placed
on the gathalast line.

LAYER HANDLING
==============

The h1 anchor slug and display label are derived from the JSON "layer" field:

  layer      -> anchor slug   -> display label
  atthakatha -> atthakatha    -> aṭṭhakathā
  tika       -> tika          -> ṭīkā
  tiika      -> tika          -> ṭīkā
  other      -> anutika       -> anuṭīkā   (used by Dhammasangani-anutika)

CONFIGURATION
=============

Edit CHAPTER_ROOT_TEXT_CONTEXT and BOOK_ID before running on a new file,
or pass chapter_context= kwarg to convert_json_to_commentary().

CLI:
    python tipitaka_org_atthakatha.py source.json output.md

    # avoid .pyc staleness on mounted filesystems:
    python3 -c "
    import sys, pathlib, types
    src = pathlib.Path('4-SYSTEM/Skills/json-to-commentary/scripts/converters/tipitaka_org_atthakatha.py').read_bytes().rstrip(b'\\x00').decode('utf-8')
    mod = types.ModuleType('conv')
    exec(compile(src, 'tipitaka_org_atthakatha.py', 'exec'), mod.__dict__)
    mod.convert_json_to_commentary(
        '0-INBOX/raw-data/abh01a.json',
        '0-INBOX/temp/pi-dhammasangani-atthakatha.md',
    )
    "
"""

from __future__ import annotations
import argparse
import json
import re
import sys
from pathlib import Path

# ---------------------------------------------------------------------------
# CONFIGURATION — edit before running on a new source file
# ---------------------------------------------------------------------------

# Maps JSON source-chapter number -> root-text resolution context.
# "toc_a" -> ^1-0a-N  (Tikamatiká)
# "toc_b" -> ^1-0b-N  (Dukamatiká)
# "main"  -> ^1-N     (Cittuppadakanda and later main text)
# None    -> no transclusion (intro chapters, heading-only chapters)
#
# This is the DEFAULT context (for abh01a - Atthasalini).
# Pass chapter_context= to convert_json_to_commentary() to override per-file.
CHAPTER_ROOT_TEXT_CONTEXT: dict[int, str | None] = {
    # abh01a - Atthasalini (Dhammasangani-atthakatha)
    0: None,        # Nidanakatha - introductory, no root-text verse refs
    1: None,        # "1. Cittuppadakando" - chapter label only
    2: "toc_a",     # Tikamatikapadavannana -> Tikamatiká (^1-0a-N)
    3: "toc_b",     # Dukamatikapadavannana -> Dukamatiká (^1-0b-N)
    4: "main",      # Kamavacarakusalapadabhajaniyam -> main text (^1-N)
    5: "main",      # Rupakando
    6: "main",      # Nikkhepakando
    7: "main",      # Atthakathakando
}

# Chapter context for abh01t - Dhammasangani-mulatika (9 source chapters 0-8)
CHAPTER_ROOT_TEXT_CONTEXT_MULATIKA: dict[int, str | None] = {
    0: None,        # intro / Sumedhakathavannana
    1: None,        # "1. Cittuppadakandam" - chapter label only
    2: "toc_a",     # Tikamatikapadavannana
    3: "toc_b",     # Dukamatikapadavannana
    4: "main",      # Kamavacarakusalapadabhajaniyavannana
    5: "main",      # Kamavacarakusalam (continuation)
    6: "main",      # "2. Rupakandam"
    7: "main",      # "3. Nikkhepakandom"
    8: "main",      # "4. Atthakathakandom"
}

# Chapter context for abh04t - Dhammasangani-anutika (8 source chapters 0-7)
CHAPTER_ROOT_TEXT_CONTEXT_ANUTIKA: dict[int, str | None] = {
    0: None,        # intro / Nidanakathavannana
    1: None,        # "1. Cittuppadakandam" - chapter label only
    2: "toc_a",     # Tikamatikapadavannana
    3: "toc_b",     # Dukamatikapadavannana
    4: "main",      # Kamavacarakusalapadabhajaniyavannana
    5: "main",      # "2. Rupakandam"
    6: "main",      # "3. Nikkhepakandom"
    7: "main",      # "4. Atthakathakandom"
}

# Obsidian vault-relative path to the root text.
ROOT_TEXT_PATH = "1-SOURCES/Text/pi-dhammasangani.md"

# Book position within its pitaka (1 = Dhammasangani, 2 = Vibhanga, ...).
BOOK_ID = 1

# Layer "layer" field -> h1 anchor slug
LAYER_SLUG_MAP = {
    "atthakatha": "atthakatha",
    "tika":       "tika",
    "tiika":      "tika",
    "other":      "anutika",   # Dhammasangani-anutika uses layer="other"
}

# Proper Pali display names for layer codes
LAYER_DISPLAY_MAP = {
    "atthakatha": "aṭṭhakathā",
    "tika":       "ṭīkā",
    "tiika":      "ṭīkā",
    "other":      "anuṭīkā",   # Dhammasangani-anutika
}

# ---------------------------------------------------------------------------
# HELPERS
# ---------------------------------------------------------------------------

_leading_num_re   = re.compile(r"^\s*\d+\.\s*")
_verse_ref_re     = re.compile(r"^\s*(\d+)(?:-(\d+))?\.(?:\s|$)")
_leading_strip_re = re.compile(r"^\s*\d+(?:-\d+)?\.\s*")


def strip_leading_number(text: str) -> str:
    return _leading_num_re.sub("", text).strip()


def clean_text(s: str) -> str:
    return s.strip()


def format_frontmatter(meta: dict) -> str:
    lines = ["---"]
    for k, v in meta.items():
        if v is None:
            continue
        if isinstance(v, list):
            lines.append(f"{k}:")
            for item in v:
                lines.append(f"  - {item}")
        else:
            val = str(v)
            if any(c in val for c in (":", "#", "[", "]", "'")):
                lines.append(f'{k}: "{val}"')
            else:
                lines.append(f"{k}: {val}")
    lines.append("---")
    return "\n".join(lines) + "\n"


def resolve_root_text_ids(book_id: int, context: str,
                          n_start: int, n_end: int) -> list[str]:
    """Return root-text block IDs for verse numbers n_start..n_end."""
    ids: list[str] = []
    for n in range(n_start, n_end + 1):
        if context == "toc_a":
            ids.append(f"{book_id}-0a-{n}")
        elif context == "toc_b":
            ids.append(f"{book_id}-0b-{n}")
        elif context == "main":
            ids.append(f"{book_id}-{n}")
    return ids


def make_transclusions(root_ids: list[str], root_text_path: str) -> str:
    return "\n".join(f"![[{root_text_path}#^{rid}]]" for rid in root_ids)


# ---------------------------------------------------------------------------
# ROLES
# ---------------------------------------------------------------------------

ROLE_CHAPTER    = "chapter"
ROLE_TITLE      = "title"
ROLE_SUBHEAD    = "subhead"
ROLE_SUBSUBHEAD = "subsubhead"
ROLE_VERSE      = "verse"
ROLE_GATHA      = "gatha"
ROLE_GATHALAST  = "gathalast"
ROLE_SKIP       = "skip"

CATEGORY_TO_ROLE: dict[str, str] = {
    "chapter":    ROLE_CHAPTER,
    "title":      ROLE_TITLE,
    "subhead":    ROLE_SUBHEAD,
    "subsubhead": ROLE_SUBSUBHEAD,
    "bodytext":   ROLE_VERSE,
    "indent":     ROLE_VERSE,
    "unindented": ROLE_VERSE,
    "gatha1":     ROLE_GATHA,
    "gatha2":     ROLE_GATHA,
    "gatha3":     ROLE_GATHA,
    "gathalast":  ROLE_GATHALAST,
    "centered":   ROLE_VERSE,   # section-closing summaries
    "nikaya":     ROLE_SKIP,    # handled in pre-chapter extraction
    "book":       ROLE_SKIP,    # handled in pre-chapter extraction
}

# ---------------------------------------------------------------------------
# METADATA
# ---------------------------------------------------------------------------


def extract_metadata(data: dict, source_path: Path, book_id: int) -> dict:
    title_pali = data.get("title_pali") or source_path.stem
    breadcrumb = data.get("title_breadcrumb", "")
    pitaka     = data.get("pitaka", "")
    layer      = data.get("layer", "")
    source_id  = data.get("id", "")
    source_fn  = data.get("source_filename", "")
    total_segs = data.get("total_segments", "")

    desc_parts = []
    if breadcrumb:
        desc_parts.append(breadcrumb)
    if total_segs:
        desc_parts.append(f"{total_segs} segments in source")
    description = "Tipitaka.org Atthakatha/Tika edition export."
    if desc_parts:
        description += " " + "; ".join(desc_parts) + "."

    # Derive layer slug for URL
    layer_lower = layer.lower()
    layer_type  = data.get("layer_type", "")
    url_ext = layer_type if layer_type else {"atthakatha": "att", "tika": "tik", "tiika": "tik"}.get(layer_lower, layer_lower[:3])
    source_url = (
        f"https://tipitaka.org/romn/cscd/{source_id}.{url_ext}.html"
        if source_id and url_ext
        else None
    )

    return {
        "title":              title_pali,
        "language":           "Pali",
        "script":             "Roman (PTS diacritics)",
        "file_type":          "commentary",
        "lang_tag":           "pi",
        "verse_id_format":    "book-verse",
        "pitaka":             pitaka,
        "layer":              layer,
        "root_text":          ROOT_TEXT_PATH,
        "source_description": description,
        "source_filename":    source_fn,
        "source_url":         source_url,
        "other_ids": [f"tipitaka.org: {source_id}"] if source_id else None,
    }


# ---------------------------------------------------------------------------
# MAIN CONVERTER
# ---------------------------------------------------------------------------


def convert_json_to_commentary(
    json_path,
    output_path,
    chapter_context: dict[int, str | None] | None = None,
) -> None:
    """Convert a tipitaka.org JSON export to an Obsidian commentary Markdown file.

    Args:
        json_path:       Path to the source JSON file.
        output_path:     Path to write the Markdown output.
        chapter_context: Override for CHAPTER_ROOT_TEXT_CONTEXT.  Pass one of
                         CHAPTER_ROOT_TEXT_CONTEXT_MULATIKA or
                         CHAPTER_ROOT_TEXT_CONTEXT_ANUTIKA as appropriate, or
                         supply your own dict.  Defaults to the module-level
                         CHAPTER_ROOT_TEXT_CONTEXT (calibrated for abh01a).
    """
    json_path   = Path(json_path)
    output_path = Path(output_path)

    with json_path.open(encoding="utf-8") as fh:
        data = json.load(fh)

    segments = data.get("segments", [])
    meta     = extract_metadata(data, json_path, BOOK_ID)

    # Resolve layer slug for h1 anchor
    raw_layer   = str(meta.get("layer", "")).lower()
    layer_slug  = LAYER_SLUG_MAP.get(raw_layer, raw_layer or "commentary")
    layer_label = LAYER_DISPLAY_MAP.get(raw_layer, raw_layer)

    # Chapter-context to use (caller can override)
    ctx = chapter_context if chapter_context is not None else CHAPTER_ROOT_TEXT_CONTEXT

    # Phase 1: extract pre-chapter structural elements
    # -----------------------------------------------------------------------
    # We consume nikaya, title, book from the very start of the segment list.
    # We stop collecting title/book once we have found the book segment
    # (got_book=True) so that sub-section titles later in ch0 are not
    # mistakenly appended to the h2 heading.
    # -----------------------------------------------------------------------
    homage         = None
    pitaka_heading = None
    title_parts: list[str] = []
    got_book       = False
    saw_chapter    = False

    chapters: dict[int, list[tuple[str, str]]] = {}

    for seg in segments:
        css     = seg.get("css_class", "")
        content = clean_text(seg.get("content", ""))
        if not content:
            continue
        src_ch = seg.get("chapter", 0)

        # Collect structural preamble (nikaya / title / book) ONLY until
        # we have the book segment. After that, remaining title segments
        # belong to the chapter content and go into the chapters dict.
        if not saw_chapter and not got_book:
            if css == "centered" and homage is None:
                homage = content
                continue
            if css == "nikaya":
                pitaka_heading = content
                continue
            if css == "title":
                title_parts.append(content)
                continue
            if css == "book":
                title_parts.append(content)
                got_book = True   # stop collecting; later titles go to chapters
                continue

        role = CATEGORY_TO_ROLE.get(css, ROLE_VERSE)
        if role == ROLE_CHAPTER:
            saw_chapter = True
        if role == ROLE_SKIP:
            continue
        chapters.setdefault(src_ch, []).append((role, content))

    # Phase 2: assemble headings and emit
    # -----------------------------------------------------------------------
    book_heading = " ".join(title_parts) if title_parts else meta["title"]

    out: list[str] = [format_frontmatter(meta), "\n"]

    if homage:
        out.append(homage + "\n\n")

    if pitaka_heading:
        h1_title = f"{pitaka_heading} ({layer_label})" if layer_label else pitaka_heading
        out.append(f"# {h1_title} ^{layer_slug}-0\n\n")

    out.append(f"## {book_heading} ^{BOOK_ID}-0\n\n")

    # Continuous verse counter across the whole file
    verse_counter = [0]

    def next_verse_id() -> str:
        verse_counter[0] += 1
        return f"^{BOOK_ID}-{verse_counter[0]}"

    # Phase 3: emit each source chapter as a ### section
    # -----------------------------------------------------------------------
    for src_ch in sorted(chapters.keys()):
        items        = chapters[src_ch]
        root_context = ctx.get(src_ch)

        # Determine the h3 title for this chapter
        chapter_title_raw = next(
            (c for r, c in items if r == ROLE_CHAPTER), None
        )
        if chapter_title_raw is not None:
            h3_title = strip_leading_number(chapter_title_raw)
        else:
            # ch0: no chapter-class segment.
            # Prefer the first *subhead* (e.g. "Nidanakatha") over subsubhead
            # (e.g. "Gantharambhakatha") since the subhead names the section.
            h3_title = (
                next((c for r, c in items if r == ROLE_SUBHEAD), None)
                or next((c for r, c in items if r == ROLE_TITLE), None)
                or next((c for r, c in items if r == ROLE_SUBSUBHEAD), None)
                or f"Section {src_ch}"
            )
            h3_title = strip_leading_number(h3_title)

        out.append(f"### {h3_title} ^{BOOK_ID}-{src_ch}-0\n\n")

        # Per-chapter sub-section state
        h4_counter  = 0
        h5_counter  = 0
        seen_title  = False
        consumed_h3 = False   # True once chapter-level title is consumed

        # Gatha (verse stanza) accumulator
        gatha_buffer: list[str] = []

        def flush_gatha() -> None:
            if not gatha_buffer:
                return
            vid  = next_verse_id()
            body = "\n".join(gatha_buffer)
            out.append(f"{body} {vid}\n\n")
            gatha_buffer.clear()

        def emit_verse(content: str, root_ctx: str | None) -> None:
            """Detect inline root-text ref, emit transclusions, then paragraph."""
            m = _verse_ref_re.match(content)
            if m and root_ctx:
                n_start = int(m.group(1))
                n_end   = int(m.group(2)) if m.group(2) else n_start
                rt_ids  = resolve_root_text_ids(BOOK_ID, root_ctx, n_start, n_end)
                if rt_ids:
                    out.append(make_transclusions(rt_ids, ROOT_TEXT_PATH) + "\n\n")
                content = _leading_strip_re.sub("", content).strip()

            if not content:
                return
            vid = next_verse_id()
            out.append(f"{content} {vid}\n\n")

        for role, content in items:
            if role == ROLE_CHAPTER:
                if not consumed_h3:
                    consumed_h3 = True
                    continue
                # A second chapter-class segment inside the same source
                # chapter is treated as an h4 (rare edge case)
                role = ROLE_TITLE

            if role == ROLE_TITLE:
                flush_gatha()
                seen_title  = True
                h4_counter += 1
                h5_counter  = 0
                heading_id  = f"^{BOOK_ID}-{src_ch}-{h4_counter}-0"
                out.append(
                    f"#### {strip_leading_number(content)} {heading_id}\n\n"
                )
                continue

            if role in (ROLE_SUBHEAD, ROLE_SUBSUBHEAD):
                flush_gatha()
                text = strip_leading_number(content)

                # Skip this subhead if it was used as the synthesised h3 title
                if not consumed_h3 and text == h3_title:
                    consumed_h3 = True
                    continue

                if seen_title:
                    # h5: deeper sub-section under an h4 title
                    h5_counter += 1
                    heading_id  = f"^{BOOK_ID}-{src_ch}-{h4_counter}-{h5_counter}-0"
                    out.append(f"##### {text} {heading_id}\n\n")
                else:
                    # h4: sub-section before any h4 title in this chapter
                    h4_counter += 1
                    h5_counter  = 0
                    heading_id  = f"^{BOOK_ID}-{src_ch}-{h4_counter}-0"
                    out.append(f"#### {text} {heading_id}\n\n")
                continue

            if role == ROLE_GATHA:
                gatha_buffer.append(content)
                continue

            if role == ROLE_GATHALAST:
                gatha_buffer.append(content)
                flush_gatha()
                continue

            # ROLE_VERSE (bodytext, indent, unindented, centered)
            flush_gatha()
            emit_verse(content, root_context)

        flush_gatha()  # safety flush at chapter end

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text("".join(out), encoding="utf-8")
    print(
        f"Wrote {output_path}  ({verse_counter[0]} verses)",
        file=sys.stderr,
    )


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("json_path",   type=Path)
    ap.add_argument("output_path", type=Path)
    args = ap.parse_args()
    convert_json_to_commentary(args.json_path, args.output_path)


if __name__ == "__main__":
    main()
