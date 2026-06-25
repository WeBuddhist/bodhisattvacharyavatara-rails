#!/usr/bin/env python3
"""
chunk_file.py — Plan overlapping line windows over a large markdown file.

Two modes:

  --index-only  (recommended for toc-tree-extraction)
      Write ONLY a tiny index of chunk -> (start_line, end_line). No chunk bodies are
      materialised, so the source text is never duplicated on disk. Each pass-1/pass-2
      subagent reads its own line range directly from the source file, e.g.
          sed -n 'START,ENDp' <source>
      The 1-based line numbers in the index are inclusive and match sed exactly.

  (default)
      Also write each window to <output_dir>/chunk_NNN.md (the old behaviour), for callers
      that want physical chunk files.

Usage:
    python chunk_file.py <input_file> [--chunk-size 150] [--overlap 25] \
        [--output-dir DIR] [--index-only]

The index is always written to <output_dir>/chunk-index.tsv with columns:
    chunk_id <TAB> start_line <TAB> end_line
plus comment header lines (prefixed with '#') recording source, totals, and parameters.
"""

import argparse
import sys
from pathlib import Path


def plan_chunks(total_lines: int, chunk_size: int, overlap: int):
    """Return a list of (chunk_id, start_line, end_line) 1-based inclusive ranges."""
    ranges = []
    start = 0          # 0-based internally
    idx = 0
    while start < total_lines:
        end = min(start + chunk_size, total_lines)
        ranges.append((idx, start + 1, end))   # convert to 1-based inclusive
        idx += 1
        if end >= total_lines:
            break
        start = end - overlap   # overlap: next window re-reads the last N lines
    return ranges


def chunk_file(input_path: str, chunk_size: int = 150, overlap: int = 25,
               output_dir: str = None, index_only: bool = False):
    input_path = Path(input_path)
    if not input_path.exists():
        print(f"Error: file not found: {input_path}", file=sys.stderr)
        sys.exit(1)

    lines = input_path.read_text(encoding="utf-8").splitlines(keepends=True)
    total_lines = len(lines)

    output_dir = Path(output_dir) if output_dir else input_path.parent / "chunks"
    output_dir.mkdir(parents=True, exist_ok=True)

    ranges = plan_chunks(total_lines, chunk_size, overlap)

    # Always write the index (cheap; this is the single source of truth).
    index_path = output_dir / "chunk-index.tsv"
    with open(index_path, "w", encoding="utf-8") as f:
        f.write(f"# source: {input_path}\n")
        f.write(f"# total_lines: {total_lines}\n")
        f.write(f"# chunk_size: {chunk_size}\n")
        f.write(f"# overlap: {overlap}\n")
        f.write(f"# total_chunks: {len(ranges)}\n")
        f.write("# columns: chunk_id\tstart_line\tend_line  (1-based, inclusive; "
                "read with: sed -n 'START,ENDp' <source>)\n")
        for cid, start, end in ranges:
            f.write(f"{cid:03d}\t{start}\t{end}\n")

    # Optionally also materialise the chunk bodies (old behaviour).
    if not index_only:
        for cid, start, end in ranges:
            out_file = output_dir / f"chunk_{cid:03d}.md"
            with open(out_file, "w", encoding="utf-8") as f:
                f.write(f"<!-- CHUNK {cid} | lines {start}-{end} of {total_lines} "
                        f"| source: {input_path.name} -->\n\n")
                f.writelines(lines[start - 1:end])

    mode = "index only" if index_only else "index + chunk bodies"
    print(f"OK {len(ranges)} chunks planned ({mode}) -> {output_dir}/")
    print(f"  Index: {index_path}")
    return output_dir, ranges


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Plan overlapping chunks over a markdown file.")
    parser.add_argument("input_file", help="Path to the input .md file")
    parser.add_argument("--chunk-size", type=int, default=150, help="Lines per chunk (default: 150)")
    parser.add_argument("--overlap", type=int, default=25, help="Overlap lines between chunks (default: 25)")
    parser.add_argument("--output-dir", default=None, help="Directory for the index (and chunk bodies, unless --index-only)")
    parser.add_argument("--index-only", action="store_true",
                        help="Write only chunk-index.tsv; do NOT duplicate text into chunk_NNN.md files")
    args = parser.parse_args()

    chunk_file(args.input_file, args.chunk_size, args.overlap, args.output_dir, args.index_only)
