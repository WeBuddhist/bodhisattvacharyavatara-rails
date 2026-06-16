#!/usr/bin/env python3
"""Get text from reader JSON by character offset (content[start:end])."""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

DEFAULT_JSON = Path(__file__).resolve().parent / "data" / "zh-隆蓮法師a.json"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Return text for a character span in reader JSON content."
    )
    parser.add_argument("start", type=int, help="Start offset (inclusive)")
    parser.add_argument("end", type=int, help="End offset (exclusive)")
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

    if args.start < 0 or args.end < 0:
        print("start and end must be non-negative.", file=sys.stderr)
        raise SystemExit(1)
    if args.start > args.end:
        print(
            f"Invalid span: start ({args.start}) must be <= end ({args.end}).",
            file=sys.stderr,
        )
        raise SystemExit(1)

    try:
        payload = json.loads(args.json.read_text(encoding="utf-8"))
    except OSError as exc:
        print(f"Failed to read file: {exc}", file=sys.stderr)
        raise SystemExit(1) from exc
    except json.JSONDecodeError as exc:
        print(f"Invalid JSON: {exc}", file=sys.stderr)
        raise SystemExit(1) from exc

    content = payload.get("content")
    if not isinstance(content, str):
        print("JSON must contain: content (str)", file=sys.stderr)
        raise SystemExit(1)

    if args.end > len(content):
        print(
            f"Span end ({args.end}) exceeds content length ({len(content)}).",
            file=sys.stderr,
        )
        raise SystemExit(1)

    text = content[args.start : args.end]
    print(f"span: {args.start}-{args.end}")
    print(f"length: {len(text)}")
    print("text:")
    print(text)


if __name__ == "__main__":
    main()
