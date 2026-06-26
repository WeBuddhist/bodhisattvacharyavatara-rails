#!/usr/bin/env python3
"""
toc_tree_ingest.py -- TOC Tree Ingestion Tool

Two modes:

  parse   Parse a toc-tree-*.md file into a JSON node list.
          Run once per commentary; output cached for all subsequent ingest runs.

          python3 toc_tree_ingest.py parse \
              --input  0-INBOX/temp/TOC-X/toc-tree-X.md \
              --out    /tmp/toc-tree-X.json

  ingest  Insert ALL headings into the commentary in a single pass,
          processing ALL depth levels in document order.

          python3 toc_tree_ingest.py ingest \
              --tree        /tmp/toc-tree-X.json \
              --commentary  1-SOURCES/Commentaries/commentaries_with_toc/X.toc.md

Anchor strategy:
  The [[...]] context snippet (first 60 chars, trailing tshegs stripped) is the
  primary search anchor. Nodes are processed in strict document order (doc_order).
  A running cursor tracks the line of the last successfully placed heading.

  For each node:
    - If the anchor appears exactly once → insert before that line.
    - If the anchor appears more than once → take the FIRST occurrence AT OR
      AFTER the cursor (document-order disambiguation). This handles repeated
      structural phrases (e.g. chapter-title lines that appear in every chapter).
    - If the anchor appears zero times → flag as not-found for manual resolution.

  The cursor advances every time a heading is successfully inserted, ensuring
  later nodes always search ahead of earlier ones.

Node JSON schema:
  {
    "decimal_id":     "1.3.2",        # dot-separated path
    "depth":          3,              # number of segments
    "label":          "Tibetan...",   # heading label text
    "block_id":       "^1-3-2-0",    # derived block id
    "context":        "first 200 chars of [[...]]",
    "context_anchor": "first 60 chars, tsheg-stripped",
    "doc_order":      42              # 0-based position in toc-tree file
  }
"""

import argparse
import json
import re
import sys
from pathlib import Path
from collections import Counter


# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

HEADING_LEVELS = {1: "##", 2: "###", 3: "####", 4: "#####"}
DEFAULT_HEADING = "######"
ANCHOR_LENGTH = 60       # chars from context used as primary anchor
CONTEXT_MAX = 200        # chars stored in JSON context field


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def depth_to_heading(depth: int) -> str:
    return HEADING_LEVELS.get(depth, DEFAULT_HEADING)


def decimal_to_block_id(decimal_id: str) -> str:
    """'1.3.2.2' -> '^1-3-2-2-0'"""
    segments = decimal_id.rstrip(".").split(".")
    return "^" + "-".join(segments) + "-0"


def parse_toc_line(line: str):
    """
    Parse one line of the toc-tree-*.md file.

    Expected format (any leading whitespace):
        * N.N.N. Tibetan label [[context text]]
        * N.N.N Tibetan label [[context text]]

    Returns a dict or None if the line is not a node line.
    """
    stripped = line.lstrip()
    if not stripped.startswith("* "):
        return None

    content = stripped[2:].strip()
    parts = content.split(None, 1)
    if not parts:
        return None

    raw_id = parts[0].rstrip(".")
    if not re.fullmatch(r"[\d]+(?:\.[\d]+)*", raw_id):
        return None

    rest = parts[1].strip() if len(parts) > 1 else ""

    if "[[" in rest:
        label_part, context_part = rest.split("[[", 1)
        label = label_part.strip()
        context = context_part.rstrip("]").rstrip("]").strip()
    else:
        label = rest.strip()
        context = ""

    depth = raw_id.count(".") + 1

    # Strip trailing tshegs (U+0F0B ་): context snippets end mid-syllable with
    # a tsheg that appears as a shad or other particle in running prose.
    raw_anchor = context[:ANCHOR_LENGTH]
    context_anchor = raw_anchor.strip().rstrip("་")

    return {
        "decimal_id":     raw_id,
        "depth":          depth,
        "label":          label,
        "block_id":       decimal_to_block_id(raw_id),
        "context":        context[:CONTEXT_MAX],
        "context_anchor": context_anchor,
    }


# ---------------------------------------------------------------------------
# parse command
# ---------------------------------------------------------------------------

def cmd_parse(args):
    input_path = Path(args.input)
    out_path = Path(args.out)

    if not input_path.exists():
        print(f"ERROR: input file not found: {input_path}", file=sys.stderr)
        sys.exit(1)

    nodes = []
    with input_path.open(encoding="utf-8") as fh:
        for line in fh:
            node = parse_toc_line(line)
            if node:
                node["doc_order"] = len(nodes)
                nodes.append(node)

    if not nodes:
        print("ERROR: no nodes parsed — check input file format.", file=sys.stderr)
        sys.exit(1)

    max_depth = max(n["depth"] for n in nodes)
    output = {
        "source":      str(input_path),
        "total_nodes": len(nodes),
        "max_depth":   max_depth,
        "nodes":       nodes,
    }

    out_path.parent.mkdir(parents=True, exist_ok=True)
    with out_path.open("w", encoding="utf-8") as fh:
        json.dump(output, fh, ensure_ascii=False, indent=2)

    print(f"Parsed {len(nodes)} nodes, max depth {max_depth}.")
    print(f"JSON cache written to: {out_path}")

    depth_counts = Counter(n["depth"] for n in nodes)
    for d in sorted(depth_counts):
        print(f"  depth {d:2d}: {depth_counts[d]} nodes")


# ---------------------------------------------------------------------------
# ingest command
# ---------------------------------------------------------------------------

def heading_line(node: dict) -> str:
    hashes = depth_to_heading(node["depth"])
    return f"{hashes} {node['label']} {node['block_id']}"


def cmd_ingest(args):
    tree_path = Path(args.tree)
    commentary_path = Path(args.commentary)

    if not tree_path.exists():
        print(f"ERROR: tree JSON not found: {tree_path}", file=sys.stderr)
        sys.exit(1)
    if not commentary_path.exists():
        print(f"ERROR: commentary file not found: {commentary_path}", file=sys.stderr)
        sys.exit(1)

    with tree_path.open(encoding="utf-8") as fh:
        tree_data = json.load(fh)

    # Process ALL nodes in strict document order (doc_order)
    all_nodes = sorted(tree_data["nodes"], key=lambda n: n["doc_order"])

    print(f"Ingesting {len(all_nodes)} nodes across {tree_data['max_depth']} depth levels.")
    print(f"Strategy: document-order cursor disambiguation for repeated anchors.\n")

    text = commentary_path.read_text(encoding="utf-8")
    lines = text.splitlines(keepends=True)

    inserted = 0
    skipped_present = 0
    not_found = []      # (decimal_id, label, reason)
    disambiguation = [] # (decimal_id, label, match_count, chosen_line)

    # cursor: line index of the last successfully placed heading.
    # All subsequent anchor searches start from this position.
    cursor = 0

    for node in all_nodes:
        anchor = node.get("context_anchor", "").strip()
        block_id = node["block_id"]
        h_line = heading_line(node)

        if not anchor:
            not_found.append((node["decimal_id"], node["label"],
                              "empty context_anchor — [[?]] in toc-tree"))
            continue

        # Find all lines containing the anchor
        matches = [i for i, ln in enumerate(lines) if anchor in ln]

        if len(matches) == 0:
            not_found.append((node["decimal_id"], node["label"],
                              f"anchor not found: {anchor[:60]!r}"))
            continue

        # Determine target line: unique → that line; multiple → first at/after cursor
        if len(matches) == 1:
            target_line_idx = matches[0]
        else:
            # Document-order disambiguation: take first match at or after cursor
            after_cursor = [m for m in matches if m >= cursor]
            if not after_cursor:
                not_found.append((node["decimal_id"], node["label"],
                                  f"anchor has {len(matches)} matches but none at/after cursor {cursor}"))
                continue
            target_line_idx = after_cursor[0]
            disambiguation.append((node["decimal_id"], node["label"],
                                   len(matches), target_line_idx))

        # Already-present check: look for block_id in 1–3 lines before anchor
        already = False
        for check_offset in (1, 2, 3):
            check_idx = target_line_idx - check_offset
            if check_idx >= 0 and block_id in lines[check_idx]:
                already = True
                break

        if already:
            # Advance cursor past this position so later nodes search ahead
            cursor = max(cursor, target_line_idx)
            skipped_present += 1
        else:
            lines.insert(target_line_idx, "\n")
            lines.insert(target_line_idx, h_line + "\n")
            # After inserting 2 lines, the anchor is now at target_line_idx + 2
            cursor = target_line_idx + 2
            inserted += 1

    commentary_path.write_text("".join(lines), encoding="utf-8")

    # --- Summary ---
    print(f"Summary")
    print(f"  Total nodes:           {len(all_nodes)}")
    print(f"  Inserted:              {inserted}")
    print(f"  Already present:       {skipped_present}")
    print(f"  Not found:             {len(not_found)}")
    print(f"  Disambiguated (multi): {len(disambiguation)}")

    if disambiguation:
        print(f"\nDisambiguated (placed using document-order cursor):")
        for decimal_id, label, count, line_idx in disambiguation:
            print(f"  [{decimal_id}] {label[:60]} — {count} matches, chose line {line_idx}")

    if not_found:
        print(f"\nNOT FOUND — insert manually then re-run to confirm:")
        for decimal_id, label, reason in not_found:
            print(f"  [{decimal_id}] {label[:70]}")
            print(f"       {reason}")

    print(f"\nCommentary updated: {commentary_path}")

    # Exit non-zero only if there are not-found nodes that need manual work
    if not_found:
        sys.exit(2)


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(description="TOC Tree Ingestion Tool")
    subparsers = parser.add_subparsers(dest="command", required=True)

    p_parse = subparsers.add_parser("parse", help="Parse toc-tree-*.md to JSON")
    p_parse.add_argument("--input", required=True, help="Path to toc-tree-*.md")
    p_parse.add_argument("--out",   required=True, help="Output JSON path")

    p_ingest = subparsers.add_parser("ingest", help="Ingest all nodes into commentary")
    p_ingest.add_argument("--tree",        required=True, help="Path to JSON cache")
    p_ingest.add_argument("--commentary",  required=True, help="Path to commentary .md file")

    args = parser.parse_args()

    if args.command == "parse":
        cmd_parse(args)
    elif args.command == "ingest":
        cmd_ingest(args)


if __name__ == "__main__":
    main()
