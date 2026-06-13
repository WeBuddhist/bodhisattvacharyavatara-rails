#!/usr/bin/env python3
"""Get verse text from reader JSON by span start/end."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

DEFAULT_JSON = Path(__file__).resolve().parent / "data" / "zh-隆蓮法師a.json"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Return verse text for a matching span start/end."
    )
    parser.add_argument("start", type=int, help="Span start offset")
    parser.add_argument("span_end", type=int, help="Span end offset")
    parser.add_argument(
        "--json",
        type=Path,
        default=DEFAULT_JSON,
        help=f"Reader JSON path (default: {DEFAULT_JSON})",
    )
    return parser.parse_args()


def main() -> None:
    # Avoid Windows console encoding errors when printing Sanskrit text.
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    if hasattr(sys.stderr, "reconfigure"):
        sys.stderr.reconfigure(encoding="utf-8", errors="replace")

    args = parse_args()

    try:
        payload = json.loads(args.json.read_text(encoding="utf-8"))
    except OSError as exc:
        print(f"Failed to read file: {exc}", file=sys.stderr)
        raise SystemExit(1) from exc
    except json.JSONDecodeError as exc:
        print(f"Invalid JSON: {exc}", file=sys.stderr)
        raise SystemExit(1) from exc

    content = payload.get("content")
    verses = payload.get("verse")
    if not isinstance(content, str) or not isinstance(verses, list):
        print("JSON must contain: content (str), verse (list)", file=sys.stderr)
        raise SystemExit(1)

    for verse_index, verse in enumerate(verses, start=1):
        if not isinstance(verse, dict):
            continue
        span = verse.get("span")
        if not isinstance(span, dict):
            continue

        start = span.get("start")
        end = span.get("end")
        if start == args.start and end == args.span_end:
            text = content[start:end]
            print(f"verse_index: {verse_index}")
            print(f"span: {start}-{end}")
            print("text:")
            print(text)
            return

    print(
        f"No verse found for start={args.start}, span_end={args.span_end}.",
        file=sys.stderr,
    )
    raise SystemExit(1)


if __name__ == "__main__":
    main()
