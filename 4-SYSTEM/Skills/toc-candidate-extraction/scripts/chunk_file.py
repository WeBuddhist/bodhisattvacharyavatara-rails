#!/usr/bin/env python3
"""
chunk_file.py — Split a large markdown file into overlapping chunks for LLM processing.

Usage:
    python chunk_file.py <input_file> [--chunk-size 150] [--overlap 20] [--output-dir /tmp/chunks]

Each chunk is written to <output_dir>/chunk_NNN.md with a header showing its position.
Chunks overlap by --overlap lines so candidates at boundaries are never split across reads.
"""

import argparse
import os
import sys
from pathlib import Path


def chunk_file(input_path: str, chunk_size: int = 150, overlap: int = 25, output_dir: str = None):
    input_path = Path(input_path)
    if not input_path.exists():
        print(f"Error: file not found: {input_path}", file=sys.stderr)
        sys.exit(1)

    lines = input_path.read_text(encoding="utf-8").splitlines(keepends=True)
    total_lines = len(lines)

    if output_dir is None:
        output_dir = Path(input_path).parent / "chunks"
    else:
        output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    chunks = []
    start = 0
    chunk_index = 0

    while start < total_lines:
        end = min(start + chunk_size, total_lines)
        chunk_lines = lines[start:end]

        out_file = output_dir / f"chunk_{chunk_index:03d}.md"
        with open(out_file, "w", encoding="utf-8") as f:
            f.write(f"<!-- CHUNK {chunk_index} | lines {start + 1}–{end} of {total_lines} | source: {input_path.name} -->\n\n")
            f.writelines(chunk_lines)

        chunks.append(str(out_file))
        chunk_index += 1

        if end >= total_lines:
            break
        start = end - overlap  # overlap: re-read last N lines in next chunk

    # Write manifest
    manifest_path = output_dir / "manifest.txt"
    with open(manifest_path, "w", encoding="utf-8") as f:
        f.write(f"source: {input_path}\n")
        f.write(f"total_lines: {total_lines}\n")
        f.write(f"chunk_size: {chunk_size}\n")
        f.write(f"overlap: {overlap}\n")
        f.write(f"total_chunks: {chunk_index}\n\n")
        for c in chunks:
            f.write(c + "\n")

    print(f"✓ {chunk_index} chunks written to {output_dir}/")
    print(f"  Manifest: {manifest_path}")
    return output_dir, chunks


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Chunk a markdown file for LLM processing.")
    parser.add_argument("input_file", help="Path to the input .md file")
    parser.add_argument("--chunk-size", type=int, default=150, help="Lines per chunk (default: 150)")
    parser.add_argument("--overlap", type=int, default=25, help="Overlap lines between chunks (default: 25)")
    parser.add_argument("--output-dir", default=None, help="Directory to write chunks (default: <input_dir>/chunks/)")
    args = parser.parse_args()

    chunk_file(args.input_file, args.chunk_size, args.overlap, args.output_dir)
