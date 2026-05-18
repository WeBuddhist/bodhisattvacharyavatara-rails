#!/usr/bin/env python3
"""
english_paired_translation.py — converter for tipitaka.org-paired English
translation JSONs.

This JSON format is a top-level array of objects with fields:
    text        — Pāli text (may contain <h1>/<h2>/<h3> structural tags,
                  or be a numbered "N. (Ka) … ⤵ (Kha) …" verse)
    original    — Pāli original (often same as `text` minus the leading number)
    rys_davids  — Rhys Davids 1900 English translation (often empty)
    ai          — AI-generated English translation (typically populated)

Mapping:
    h1 occurrences:
        #1 → pitaka heading (e.g. "Abhidhammapiṭake")
        #2 → book heading  (e.g. "Dhammasaṅgaṇīpāḷi")
        #3+ → title-level (h4 in our output) — what abh01m.json calls
              css_class="title"
    h2 → subhead (h5 if seen after a title in the same h3; otherwise h4)
    h3 → chapter (h3 in our output) — what abh01m.json calls css_class="chapter"
    no tag, leading "<digit>+. " → numbered verse
    no tag, no leading number, before any heading → homage
    no tag, no leading number, mid-text → continuation / trailing marker;
        merged into the current verse if one is buffered, else dropped

Output: Bible-style numbering matching the Pāli source-text convention
(see source-formatting.md §5 "Pāli — Tipiṭaka root texts"). Verse IDs are
identical to those produced by tipitaka_org_book.py for the same book.

CLI:
    python english_paired_translation.py english.json en-<book-slug>.md \
        [--book-id N] [--pitaka SLUG] [--root-text PATH]
"""
from __future__ import annotations
import argparse
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from json_to_source_text import format_frontmatter  # noqa: E402

_h_tag_re = re.compile(r"^<h([1-3])>(.*?)</h\1>\s*$", re.DOTALL)
_verse_opening_re = re.compile(r"^\s*(\d+)\.\s")
_leading_num_re = re.compile(r"^\s*\d+\.\s*")


def strip_leading_number(s: str) -> str:
    return _leading_num_re.sub("", s).strip()


def expand_arrows(text: str) -> str:
    """The translation uses '⤵' (U+2935) as a soft line-break between (Ka), (Kha) etc."""
    parts = [p.strip() for p in text.split("⤵")]
    return "\n".join(p for p in parts if p)


def pick_translation(entry: dict) -> str:
    """Prefer the AI translation; fall back to Rhys Davids; then the Pāli original."""
    for key in ("ai", "rys_davids", "original", "text"):
        v = (entry.get(key) or "").strip()
        if v:
            return v
    return ""


def convert_json_to_source_text(
    json_path,
    output_path,
    *,
    book_id: int = 1,
    pitaka_slug: str = "abhidhamma",
    root_text_ref: str = "1-SOURCES/Text/pi-dhammasangani.md",
    translator: str = "AI-assisted (CSCD-aligned); selected passages from Rhys Davids 1900",
) -> None:
    json_path = Path(json_path)
    output_path = Path(output_path)
    with json_path.open(encoding="utf-8") as fh:
        data = json.load(fh)

    # Frontmatter
    meta = {
        "title": "Dhammasaṅgaṇī (English translation)",
        "translator": translator,
        "language": "English",
        "script": "Roman",
        "file_type": "translation",
        "lang_tag": "en",
        "verse_id_format": "book-verse",
        "pitaka": pitaka_slug,
        "root_text": root_text_ref,
        "translation_basis": "Tipitaka.org Mūla edition (CSCD)",
        "source_description": (
            "AI-assisted English translation of the Pāli Dhammasaṅgaṇī, segment-aligned "
            "to the tipitaka.org Mūla edition. Selected verses incorporate Rhys Davids's "
            "1900 translation where the source JSON's `rys_davids` field is populated."
        ),
        "source_filename": json_path.name,
    }

    out: list[str] = [format_frontmatter(meta), "\n"]

    # State
    h1_count = 0
    h3_count = 0
    h3_position = -1  # 0 = Mātikā, 1 = Cittuppādakaṇḍaṃ, …
    is_toc = False
    toc_letter_index = -1
    toc_letter: str | None = None
    section_counter = 0      # for non-TOC h4
    subsection_counter = 0   # for h5
    seen_title = False
    homage_emitted = False
    main_verse_counter = [0]
    toc_verse_counter = [0]
    verse_buffer: list[str] = []

    def flush_verse():
        if not verse_buffer:
            return
        if is_toc and toc_letter is not None:
            toc_verse_counter[0] += 1
            vid = f"^{book_id}-{h3_position}{toc_letter}-{toc_verse_counter[0]}"
        else:
            main_verse_counter[0] += 1
            vid = f"^{book_id}-{main_verse_counter[0]}"
        body = "\n".join(verse_buffer)
        out.append(f"{body} {vid}\n\n")
        verse_buffer.clear()

    for entry in data:
        text = (entry.get("text") or "").strip()
        m = _h_tag_re.match(text)

        if m:
            flush_verse()
            level = int(m.group(1))
            # Prefer the AI version of the heading name; fall back to the Pāli
            ai = (entry.get("ai") or "").strip()
            heading_text = strip_leading_number(ai or m.group(2))
            if level == 1:
                h1_count += 1
                if h1_count == 1:
                    # Pitaka heading
                    out.append(f"# {heading_text} ^{pitaka_slug}-0\n\n")
                elif h1_count == 2:
                    # Book heading
                    out.append(f"## {heading_text} ^{book_id}-0\n\n")
                else:
                    # Title (h4 in our output)
                    seen_title = True
                    if is_toc:
                        toc_letter_index += 1
                        toc_letter = chr(ord("a") + toc_letter_index)
                        toc_verse_counter[0] = 0
                        hid = f"^{book_id}-{h3_position}{toc_letter}-0"
                    else:
                        section_counter += 1
                        subsection_counter = 0
                        hid = f"^{book_id}-{h3_position}-{section_counter}-0"
                    out.append(f"#### {heading_text} {hid}\n\n")
            elif level == 3:
                # New chapter (h3 in our output) — resets per-chapter state
                h3_count += 1
                h3_position = h3_count - 1
                is_toc = (h3_position == 0)
                section_counter = 0
                subsection_counter = 0
                toc_letter_index = -1
                toc_letter = None
                toc_verse_counter[0] = 0
                seen_title = False
                out.append(f"### {heading_text} ^{book_id}-{h3_position}-0\n\n")
            elif level == 2:
                # Subhead
                if seen_title:
                    # h5 — preserves verse path
                    subsection_counter += 1
                    if is_toc:
                        hid = f"^{book_id}-{h3_position}{toc_letter}-{subsection_counter}-0"
                    else:
                        hid = f"^{book_id}-{h3_position}-{section_counter}-{subsection_counter}-0"
                    out.append(f"##### {heading_text} {hid}\n\n")
                else:
                    # Standalone subhead before any title — promote to h4
                    if is_toc:
                        toc_letter_index += 1
                        toc_letter = chr(ord("a") + toc_letter_index)
                        toc_verse_counter[0] = 0
                        hid = f"^{book_id}-{h3_position}{toc_letter}-0"
                    else:
                        section_counter += 1
                        subsection_counter = 0
                        hid = f"^{book_id}-{h3_position}-{section_counter}-0"
                    out.append(f"#### {heading_text} {hid}\n\n")
            continue

        # Non-heading entry
        body_text = pick_translation(entry)
        if not body_text:
            continue
        ai_body = expand_arrows(body_text)

        # The very first non-heading entry, before any heading, is the homage.
        if not homage_emitted and h1_count == 0 and h3_count == 0:
            out.append(ai_body + "\n\n")
            homage_emitted = True
            continue

        # Numbered verse opens a new verse buffer (after flushing any pending)
        vm = _verse_opening_re.match(text)
        if vm:
            flush_verse()
            # Preserve the source's leading number on the first line for parallelism
            # with the Pāli file's "1. (Ka) …" style.
            num = vm.group(1)
            first_line = f"{num}. {ai_body}"
            verse_buffer.append(first_line)
        else:
            # Non-numbered, non-heading entry: append to the current verse
            # buffer. If the buffer is empty (we just flushed for a heading,
            # for example), this entry seeds a new verse — which matches the
            # Pāli converter's behaviour and keeps verse IDs aligned across
            # the parallel files.
            verse_buffer.append(ai_body)

    flush_verse()

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text("".join(out), encoding="utf-8")


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("json_path", type=Path)
    ap.add_argument("output_path", type=Path)
    ap.add_argument("--book-id", type=int, default=1)
    ap.add_argument("--pitaka", default="abhidhamma")
    ap.add_argument("--root-text", default="1-SOURCES/Text/pi-dhammasangani.md")
    args = ap.parse_args()
    convert_json_to_source_text(
        args.json_path,
        args.output_path,
        book_id=args.book_id,
        pitaka_slug=args.pitaka,
        root_text_ref=args.root_text,
    )
    print(f"Wrote {args.output_path}", file=sys.stderr)


if __name__ == "__main__":
    main()
