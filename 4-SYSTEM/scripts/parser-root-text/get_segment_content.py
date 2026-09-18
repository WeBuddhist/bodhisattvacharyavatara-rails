#!/usr/bin/env python3
"""
get_segment_content.py

Two directions on the same data:

1. Segment -> content: extract segment text from a parser-root-text
   edition JSON file (output/<stem>.edition.json), using each segment's
   line-level start/end character offsets into the edition's `content`
   string.
2. Content -> span: given a piece of text (e.g. copied from a plain
   content file like edition.txt, or from an edition JSON's "content"),
   find its start/end character offsets within that content.

Edition JSON shape (see build_edition / _build_content_and_segmentation
in parser.py):

    {
        "metadata": {...},
        "content": "<all segment text concatenated, no separators>",
        "segmentation": {
            "segments": [
                {
                    "lines": [{"start": int, "end": int}, ...],
                    "type": "title" | "front_matter" | "verse" | "back_matter" | ...,
                    "reference": "1-1"
                },
                ...
            ]
        }
    }

Important: `content` is built with "".join(parts) — there is NO separator
between one line's text and the next, even across segments. So to read a
single line, slice content[start:end] directly. To reconstruct a whole
segment that has multiple lines (e.g. a 4-line verse), each line must be
sliced separately and then joined with "\n" (or another separator) —
slicing straight from the first line's start to the last line's end would
run the lines together with no boundary between them. The same fact means
that when searching for a piece of text inside `content`, a `\n`-joined
multi-line snippet won't match directly — find_text_spans() falls back to
the newline-stripped version automatically.

The <stem>.edition.json's "content" field, and a plain content text file
(e.g. edition.txt containing just that same concatenated text with no
JSON wrapper) are interchangeable as a source of content for this script
— load_content() reads either.

This script can also emit each matched segment's span as a text-operations
API payload (see openpecha-backend/docs/text-operations-spec.md,
PATCH /v2/editions/{edition_id}/content):

    {
        "type": "delete",
        "start": 132231,
        "end": 132245
    }

Usage as a library:

    from get_segment_content import (
        load_edition,
        load_content,
        get_segment_content,
        get_segment_span,
        find_segment_by_reference,
        filter_segments_starting_with_number,
        find_text_spans,
        build_operation_payload,
    )

    edition = load_edition("output/en-David_Karma_Choephel.edition.json")
    content = edition["content"]

    # By raw character range (single line/span):
    text = content[86:139]

    # By segment reference (handles multi-line segments correctly):
    seg = find_segment_by_reference(edition["segmentation"]["segments"], "1-1")
    text = get_segment_content(content, seg)
    start, end = get_segment_span(seg)  # overall span across all of the segment's lines

    # Every segment whose reconstructed text starts with a digit, using
    # each segment's own predefined line start/end offsets. Each match
    # also carries the segment's overall "start"/"end" span:
    numbered = filter_segments_starting_with_number(edition)

    # Turn a match (or any segment dict) into a text-operations payload:
    payload = build_operation_payload(numbered[0])
    # -> {"type": "delete", "start": ..., "end": ...}

    # The other direction: given a piece of text, find where it sits in a
    # plain content file (or an edition JSON's "content"):
    content = load_content("edition.txt")
    spans = find_text_spans(content, "10. Dedication")
    # -> [(116943, 116957)]

Usage from the command line:

    python3 get_segment_content.py output/en-David_Karma_Choephel.edition.json --reference 1-1
    python3 get_segment_content.py output/en-David_Karma_Choephel.edition.json --range 86 139
    python3 get_segment_content.py output/en-David_Karma_Choephel.edition.json --all
    python3 get_segment_content.py output/en-David_Karma_Choephel.edition.json --starts-with-number
    python3 get_segment_content.py output/en-David_Karma_Choephel.edition.json --starts-with-number --payload

    # Content -> span, from a plain text file or an edition JSON's "content":
    python3 get_segment_content.py edition.txt --find "10. Dedication"
    python3 get_segment_content.py edition.txt --find-file segment_snippet.txt --payload
"""

import argparse
import json
from typing import List, Optional, Tuple


def load_edition(path: str) -> dict:
    """Load an edition JSON file (output/<stem>.edition.json)."""
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def load_content(path: str) -> str:
    """
    Load a `content` string from either an edition JSON file (its
    "content" field) or a plain text file (the whole file, e.g.
    edition.txt) — whichever `path` points to. This lets --find /
    --find-file work against either kind of file interchangeably.
    """
    with open(path, encoding="utf-8") as f:
        raw = f.read()
    if raw.lstrip().startswith("{"):
        try:
            data = json.loads(raw)
        except json.JSONDecodeError:
            data = None
        if isinstance(data, dict) and "content" in data:
            return data["content"]
    return raw


def get_content_by_range(content: str, start: int, end: int) -> str:
    """Return content[start:end] for a single raw start/end pair."""
    return content[start:end]


def get_segment_content(content: str, segment: dict, join: str = "\n") -> str:
    """
    Return the full text of one segment dict (as found in
    edition["segmentation"]["segments"]), joining its (possibly
    multiple) line start/end spans with `join`.
    """
    lines = segment.get("lines", [])
    parts = [content[line["start"]:line["end"]] for line in lines]
    return join.join(parts)


def get_segment_span(segment: dict) -> Tuple[Optional[int], Optional[int]]:
    """
    Return the overall (start, end) character span of a segment: the
    first line's start and the last line's end. For a single-line
    segment this is just that line's own (start, end); for a multi-line
    segment (e.g. a 4-line verse) it's the outer span covering every
    line, even though the lines themselves are what content is actually
    sliced from. Returns (None, None) if the segment has no lines.
    """
    lines = segment.get("lines", [])
    if not lines:
        return None, None
    return lines[0]["start"], lines[-1]["end"]


def find_segment_by_reference(segments: List[dict], reference: str) -> Optional[dict]:
    """Return the first segment whose "reference" matches, or None."""
    for seg in segments:
        if seg.get("reference") == reference:
            return seg
    return None


def iter_segments_content(edition: dict, join: str = "\n"):
    """
    Yield (reference, type, text, start, end) for every segment in the
    edition, in order. start/end are the segment's overall span (see
    get_segment_span).
    """
    content = edition["content"]
    for seg in edition["segmentation"]["segments"]:
        start, end = get_segment_span(seg)
        text = get_segment_content(content, seg, join=join)
        yield seg.get("reference"), seg.get("type"), text, start, end


def filter_segments_starting_with_number(edition: dict, join: str = "\n") -> List[dict]:
    """
    Return every segment whose reconstructed content starts with a digit
    (0-9), as a list of {"reference", "type", "text", "start", "end"}
    dicts. "start"/"end" are the segment's overall character span.

    Each segment's text is rebuilt from its own predefined "lines"
    start/end offsets (via get_segment_content), so this reflects exactly
    what the segment's start/end spans point at in `content` — not just a
    string match against the reference label.
    """
    matches = []
    for reference, seg_type, text, start, end in iter_segments_content(edition, join=join):
        if text.lstrip()[:1].isdigit():
            matches.append(
                {
                    "reference": reference,
                    "type": seg_type,
                    "text": text,
                    "start": start,
                    "end": end,
                }
            )
    return matches


def find_text_spans(content: str, text: str) -> List[Tuple[int, int]]:
    """
    Return every non-overlapping (start, end) span where `text` occurs in
    `content` — the reverse of get_segment_content: given a piece of
    text, find where it sits.

    If the exact text (as given) isn't found anywhere, this also tries
    the text with newlines stripped out (its lines concatenated with no
    separator), since `content` itself has no separator between one
    line's text and the next — a multi-line segment's text as produced
    by get_segment_content (joined with "\n") won't match `content`
    directly, but the same text with "\n" removed will.

    Returns an empty list if `text` isn't found either way.
    """
    def _all_spans(needle: str) -> List[Tuple[int, int]]:
        if not needle:
            return []
        spans = []
        start = 0
        while True:
            idx = content.find(needle, start)
            if idx == -1:
                break
            spans.append((idx, idx + len(needle)))
            start = idx + max(len(needle), 1)
        return spans

    spans = _all_spans(text)
    if spans:
        return spans
    collapsed = text.replace("\n", "")
    if collapsed != text:
        return _all_spans(collapsed)
    return []


def build_operation_payload(segment_or_match: dict, op_type: str = "delete", text: Optional[str] = None) -> dict:
    """
    Build a text-operations API payload (see
    openpecha-backend/docs/text-operations-spec.md,
    PATCH /v2/editions/{edition_id}/content) for one segment.

    Accepts either a raw segment dict (with a "lines" list, as found in
    edition["segmentation"]["segments"]) or a match/span dict that
    already has "start"/"end" (as returned by
    filter_segments_starting_with_number or find_text_spans).

    op_type:
        "delete"  -> {"type": "delete", "start": ..., "end": ...}
        "insert"  -> {"type": "insert", "position": <start>, "text": text}
        "replace" -> {"type": "replace", "start": ..., "end": ..., "text": text}
    """
    if "start" in segment_or_match and "end" in segment_or_match and "lines" not in segment_or_match:
        start, end = segment_or_match["start"], segment_or_match["end"]
    else:
        start, end = get_segment_span(segment_or_match)

    if op_type == "insert":
        return {"type": "insert", "position": start, "text": text or ""}
    if op_type == "replace":
        return {"type": "replace", "start": start, "end": end, "text": text or ""}
    return {"type": "delete", "start": start, "end": end}


def build_delete_payloads(matches: List[dict]) -> List[dict]:
    """Convenience wrapper: build a "delete" payload for each match/segment in `matches`."""
    return [build_operation_payload(m, op_type="delete") for m in matches]


def _print_segment_block(reference, seg_type, text, start, end, payload: bool):
    print(f"[{reference}] ({seg_type}) [{start}-{end}]:\n{text}\n")
    if payload:
        print(json.dumps(build_operation_payload({"start": start, "end": end}), indent=2))
        print()


def main():
    parser = argparse.ArgumentParser(
        description=(
            "Get segment content from a parser-root-text edition JSON file "
            "using segment start/end offsets, or (with --find/--find-file) "
            "find a piece of text's start/end offsets in a content file."
        )
    )
    parser.add_argument(
        "edition_json",
        help="Path to the <stem>.edition.json file, or (for --find/--find-file) "
             "a plain content text file such as edition.txt",
    )

    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument(
        "--reference", "-r", help="Segment reference to look up, e.g. '1-1'"
    )
    group.add_argument(
        "--range",
        "-n",
        nargs=2,
        type=int,
        metavar=("START", "END"),
        help="Raw start/end character offsets into `content` (single span)",
    )
    group.add_argument(
        "--all",
        action="store_true",
        help="Print reference, type, span, and content for every segment in order",
    )
    group.add_argument(
        "--starts-with-number",
        action="store_true",
        help="Print reference, type, span, and content for every segment "
             "whose content starts with a digit",
    )
    group.add_argument(
        "--find",
        metavar="TEXT",
        help="Find the start/end character span(s) of TEXT inside the content "
             "(loaded from an edition JSON's \"content\" field, or directly "
             "from a plain text file such as edition.txt)",
    )
    group.add_argument(
        "--find-file",
        metavar="PATH",
        help="Same as --find, but reads the text to search for from PATH "
             "(handy for a multi-line snippet you don't want to quote on "
             "the command line)",
    )

    parser.add_argument(
        "--join",
        default="\n",
        help="Separator used to join a segment's multiple lines (default: newline)",
    )
    parser.add_argument(
        "--payload",
        action="store_true",
        help="Also print a text-operations API payload "
             '({"type": "delete", "start": ..., "end": ...}) for each '
             "printed segment/span",
    )

    args = parser.parse_args()

    if args.find is not None or args.find_file is not None:
        if args.find_file is not None:
            with open(args.find_file, encoding="utf-8") as f:
                search_text = f.read()
        else:
            search_text = args.find

        content = load_content(args.edition_json)
        spans = find_text_spans(content, search_text)
        if not spans:
            raise SystemExit("Text not found in content")

        for start, end in spans:
            print(f"[{start}-{end}]:")
            print(content[start:end])
            if args.payload:
                print(json.dumps(build_operation_payload({"start": start, "end": end}), indent=2))
            print()

        if len(spans) > 1:
            print(f"-- warning: {len(spans)} occurrences found --")
        return

    edition = load_edition(args.edition_json)
    content = edition["content"]
    segments = edition["segmentation"]["segments"]

    if args.all:
        for reference, seg_type, text, start, end in iter_segments_content(edition, join=args.join):
            _print_segment_block(reference, seg_type, text, start, end, args.payload)
        return

    if args.starts_with_number:
        matches = filter_segments_starting_with_number(edition, join=args.join)
        for m in matches:
            _print_segment_block(m["reference"], m["type"], m["text"], m["start"], m["end"], args.payload)
        print(f"-- {len(matches)} segment(s) start with a number --")
        return

    if args.range:
        start, end = args.range
        print(f"[{start}-{end}]:")
        print(get_content_by_range(content, start, end))
        if args.payload:
            print(json.dumps(build_operation_payload({"start": start, "end": end}), indent=2))
        return

    seg = find_segment_by_reference(segments, args.reference)
    if seg is None:
        raise SystemExit(f"No segment found with reference {args.reference!r}")
    start, end = get_segment_span(seg)
    print(f"[{args.reference}] [{start}-{end}]:")
    print(get_segment_content(content, seg, join=args.join))
    if args.payload:
        print(json.dumps(build_operation_payload(seg), indent=2))


if __name__ == "__main__":
    main()
