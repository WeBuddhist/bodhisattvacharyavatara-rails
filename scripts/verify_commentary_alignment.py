#!/usr/bin/env python3
"""Verify commentary alignment by printing root text paired with commentary text.

Reads a ``<text-name>-commentary-alignment.json`` payload and resolves each
alignment_annotation span (commentary text) with its target_annotation span(s)
(root text), printing them side by side so a human can check the alignment is
correct.

With --output, writes a JSON array of pairs containing only span and content
for each root–commentary alignment.

Usage:
    python3 scripts/verify_commentary_alignment.py             # full output
    python3 scripts/verify_commentary_alignment.py --limit 10  # first 10 entries
    python3 scripts/verify_commentary_alignment.py --root-span 1-1  # filter by verse id
    python3 scripts/verify_commentary_alignment.py --output pairs.json
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

_HERE = Path(__file__).resolve().parent
_REPO = _HERE.parent

DEFAULT_ALIGNMENT = (
    _HERE / "data/zh-入菩薩行論（宗薩蔣揚欽哲仁波切）-commentary-alignment.json"
)
DEFAULT_ROOT_JSON = _HERE / "data/zh-隆蓮法師a.json"
DEFAULT_COMMENTARY_JSON = _HERE / "data/zh-commentary-入菩薩行論（宗薩蔣揚欽哲仁波切）.json"


def strip_html(text: str) -> str:
    """Remove simple HTML tags for display."""
    return re.sub(r"<[^>]+>", "", text).strip()


def clean_text(text: str) -> str:
    return strip_html(text).replace("⤵", " ").strip()


def build_verse_id_index(root_json: dict) -> dict[tuple[int, int], str]:
    """Map (start, end) → verse id for every root verse entry."""
    index: dict[tuple[int, int], str] = {}
    for entry in root_json.get("verse", []):
        vid = entry.get("id")
        span = entry.get("span", {})
        if vid and "start" in span and "end" in span:
            index[(span["start"], span["end"])] = vid
    return index


def load_json(path: Path) -> dict:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        sys.exit(f"Cannot load {path}: {exc}")


def build_pairs(
    commentary_entries: list[dict],
    root_content: str,
    commentary_content: str,
    root_by_index: dict[int, dict],
) -> list[dict]:
    """Return root–commentary pairs with only span and content."""
    pairs: list[dict] = []

    for ann in commentary_entries:
        comm_span = ann["span"]
        c_start, c_end = comm_span["start"], comm_span["end"]
        comm_text = clean_text(commentary_content[c_start:c_end])

        for ridx in ann.get("alignment_index", []):
            root = root_by_index.get(ridx)
            if root is None:
                continue
            r_span = root["span"]
            r_start, r_end = r_span["start"], r_span["end"]
            root_text = clean_text(root_content[r_start:r_end])
            pairs.append(
                {
                    "root": {
                        "span": {"start": r_start, "end": r_end},
                        "content": root_text,
                    },
                    "commentary": {
                        "span": {"start": c_start, "end": c_end},
                        "content": comm_text,
                    },
                }
            )

    return pairs


def format_pairs_text(
    pairs: list[dict],
    verse_id_index: dict[tuple[int, int], str],
    root_json_name: str,
    commentary_json_name: str,
) -> str:
    lines: list[str] = []
    total = len(pairs)

    lines.append(f"Alignment verification — {total} entries")
    lines.append(f"Root:       {root_json_name}")
    lines.append(f"Commentary: {commentary_json_name}")
    lines.append("=" * 72)

    for i, pair in enumerate(pairs, 1):
        root = pair["root"]
        commentary = pair["commentary"]
        r_start, r_end = root["span"]["start"], root["span"]["end"]
        t_start, t_end = commentary["span"]["start"], commentary["span"]["end"]
        verse_id = verse_id_index.get((r_start, r_end), "?")

        lines.append("")
        lines.append(f"[{i}/{total}]  root verse {verse_id}  span {r_start}–{r_end}")
        lines.append(f"  ROOT ▶  {root['content']}")
        lines.append("")
        lines.append(f"  COMMENTARY  span {t_start}–{t_end}")
        lines.append(f"  ▶  {commentary['content']}")
        lines.append("-" * 72)

    return "\n".join(lines) + "\n"


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--alignment", type=Path, default=DEFAULT_ALIGNMENT,
        help="commentary alignment JSON path",
    )
    parser.add_argument(
        "--root-json", type=Path, default=DEFAULT_ROOT_JSON,
        help="Root/translation reader JSON (spans source for target_annotation)",
    )
    parser.add_argument(
        "--commentary-json", type=Path, default=DEFAULT_COMMENTARY_JSON,
        help="Commentary reader JSON (spans source for alignment_annotation)",
    )
    parser.add_argument(
        "--limit", type=int, default=None,
        help="Show only the first N alignment entries",
    )
    parser.add_argument(
        "--root-span", type=str, default=None,
        help="Filter to entries whose root verse id matches (e.g. 1-1, 2-3)",
    )
    parser.add_argument(
        "--output", type=Path, default=None,
        help="Write JSON pairs (span + content only) to this file",
    )
    args = parser.parse_args()

    alignment_data = load_json(args.alignment)
    root_json = load_json(args.root_json)
    commentary_json = load_json(args.commentary_json)

    root_content = root_json["content"]
    commentary_content = commentary_json["content"]

    root_by_index: dict[int, dict] = {
        t["index"]: t for t in alignment_data["target_annotation"]
    }
    verse_id_index = build_verse_id_index(root_json)

    entries = alignment_data["alignment_annotation"]

    if args.root_span:
        root_spans = {
            (v["span"]["start"], v["span"]["end"])
            for v in root_json.get("verse", [])
            if v.get("id") == args.root_span
        }
        entries = [
            e for e in entries
            if any(
                (root_by_index[i]["span"]["start"], root_by_index[i]["span"]["end"])
                in root_spans
                for i in e.get("alignment_index", [])
                if i in root_by_index
            )
        ]

    if args.limit:
        entries = entries[: args.limit]

    pairs = build_pairs(entries, root_content, commentary_content, root_by_index)

    if args.output:
        args.output.write_text(
            json.dumps(pairs, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )
        print(f"Wrote {len(pairs)} pairs to {args.output}")
    else:
        output_text = format_pairs_text(
            pairs,
            verse_id_index,
            args.root_json.name,
            args.commentary_json.name,
        )
        sys.stdout.buffer.write(output_text.encode("utf-8"))


if __name__ == "__main__":
    main()
