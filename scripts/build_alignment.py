#!/usr/bin/env python3
"""Add verse-to-segment alignment entries to a reader JSON file.

For each verse id present in both the reader ``verse`` array and
``bodhisattva-verse-segment-texts.json``, writes an alignment object:

- ``alignment_annotation.span`` — character span from the reader file
- ``target_annotation`` — one or more segment spans from the segment file
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

DEFAULT_READER = Path(__file__).resolve().parent / "data/zh-隆蓮法師a.json"
DEFAULT_SEGMENTS = (
    Path(__file__).resolve().parent / "data/bodhisattva-verse-segment-texts.json"
)


def segment_spans(item: dict) -> list[dict]:
    segs = item["segments"]
    if isinstance(segs, list):
        return [s["span"] for s in segs]
    return [segs["span"]]


def load_segment_index(path: Path) -> dict[str, list[dict]]:
    items = json.loads(path.read_text(encoding="utf-8"))
    index: dict[str, list[dict]] = {}
    for item in items:
        verse_id = next(k for k in item if k != "segments")
        index[verse_id] = segment_spans(item)
    return index


def build_alignment(reader: dict, segment_index: dict[str, list[dict]]) -> list[dict]:
    alignment: list[dict] = []
    for entry in reader.get("verse", []):
        verse_id = entry.get("id")
        if not verse_id or verse_id not in segment_index:
            continue
        alignment.append(
            {
                "alignment_annotation": {"span": dict(entry["span"])},
                "target_annotation": [
                    {"span": dict(span)} for span in segment_index[verse_id]
                ],
            }
        )
    return alignment


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--reader", type=Path, default=DEFAULT_READER)
    parser.add_argument("--segments", type=Path, default=DEFAULT_SEGMENTS)
    parser.add_argument(
        "--output",
        type=Path,
        default=None,
        help="Output path (default: overwrite --reader)",
    )
    args = parser.parse_args()

    reader = json.loads(args.reader.read_text(encoding="utf-8"))
    segment_index = load_segment_index(args.segments)
    reader["alignment"] = build_alignment(reader, segment_index)

    out = args.output or args.reader
    out.write_text(
        json.dumps(reader, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )

    verse_ids = {v["id"] for v in reader["verse"] if v.get("id")}
    matched = len(reader["alignment"])
    summary = (
        f"Wrote {matched} alignment entries\n"
        f"  verses with id: {len(verse_ids)}\n"
        f"  segment ids: {len(segment_index)}\n"
        f"  unmatched reader ids: {len(verse_ids - segment_index.keys())}\n"
        f"  unmatched segment ids: {len(segment_index.keys() - verse_ids)}"
    )
    sys.stdout.buffer.write(summary.encode("utf-8"))
    sys.stdout.buffer.write(b"\n")


if __name__ == "__main__":
    main()
