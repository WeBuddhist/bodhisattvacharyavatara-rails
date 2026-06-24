#!/usr/bin/env python3
"""
extract_toc_candidates.py — ས་བཅད (sa bcad) structural-outline candidate extraction
using Google Gemini Flash.

This is a runnable version of the `toc-candidate-extraction` skill
(4-SYSTEM/Skills/toc-candidate-extraction). It does the whole pipeline end to end:

    1. Chunk the input file into overlapping line windows.
    2. Send each chunk to Gemini with the sa-bcad extraction prompt.
    3. Save one result file per chunk under 0-INBOX/temp/<commentary-id>/ (resumable).
    4. Combine all chunk results into 0-INBOX/toc-candidates-<commentary-id>.md.
    5. Send the merged candidates back to Gemini and build a full nested,
       decimal-numbered TOC tree (with ^toc-X-Y-Z block IDs) saved to
       0-INBOX/toc-tree-<commentary-id>.md.  (skip with --no-tree)

The extraction step prioritises RECALL: it is better to extract too many
candidates than to miss one.

--------------------------------------------------------------------------------
Setup
--------------------------------------------------------------------------------
    pip install google-genai
    set GEMINI_API_KEY=...        (Windows)   /   export GEMINI_API_KEY=...  (mac/Linux)

--------------------------------------------------------------------------------
Usage
--------------------------------------------------------------------------------
    python 4-SYSTEM/scripts/extract_toc_candidates.py <input_file> [options]

    # commentary-id is inferred from the filename if not given:
    python 4-SYSTEM/scripts/extract_toc_candidates.py 1-SOURCES/Commentaries/bo-kunpal.md

    # explicit id, custom chunking:
    python 4-SYSTEM/scripts/extract_toc_candidates.py input.md \
        --commentary-id kunpal --chunk-size 150 --overlap 25

    # re-run: existing chunk result files are skipped automatically, so an
    # interrupted run resumes from the first missing chunk. Use --force to redo all.

Run with --help for the full option list.
"""

import argparse
import os
import re
import sys
import time
from datetime import date
from pathlib import Path

# ------------------------------------------------------------------------------
# Defaults
# ------------------------------------------------------------------------------
DEFAULT_MODEL = "gemini-flash-latest"
DEFAULT_CHUNK_SIZE = 150
DEFAULT_OVERLAP = 25
MAX_RETRIES = 4
RETRY_BACKOFF_SECONDS = 5

# Where outputs go, relative to the vault root (the dir that contains 4-SYSTEM/).
TEMP_SUBDIR = "0-INBOX/temp"
FINAL_SUBDIR = "0-INBOX"


# ------------------------------------------------------------------------------
# The extraction prompt — lifted from the toc-candidate-extraction SKILL.md
# ------------------------------------------------------------------------------
SYSTEM_PROMPT = """\
You are an expert in classical Tibetan Buddhist texts specialising in ས་བཅད (sa bcad) — \
the structural outlining system used in Tibetan commentarial literature.

Your task is to extract EVERY ས་བཅད candidate from the input text chunk.
Prioritise RECALL over precision. Never miss a candidate. It is better to extract too
many candidates than to miss one.

THREE CANDIDATE TYPES — extract all three independently:

Type A — Announcement
A passage where the author declares a division: a topic is split into N named parts.
  e.g. དང་པོ་ལ་གཉིས་ཏེ། མཚན་དོན་དང་། འགྱུར་ཕྱག་གོ།

Type B — Node header
A short label opening a section, signalling "now treating part N."
  e.g. གཉིས་པ་འགྱུར་ཕྱག་ནི།

Type C — Closing count
A number word appearing after a list, summarising how many items were just given.
  e.g. ཞེས་རྣམ་པ་གསུམ་མོ། / གནས་བརྒྱད་དོ། / ཚུལ་བཞི་པོ་དེ་དག

RECOGNITION — meaning first, markers second.
Do not pattern-match on surface markers alone. For each passage ask: is this text
dividing a topic into named parts, labelling a sub-section, or counting items just
listed? If yes — regardless of exact wording — extract it.

Common signals — any one is enough:
- Topic announced then split into named sub-parts
- Ordinal labels: དང་པོ། / གཉིས་པ། / གསུམ་པ། (even scattered across paragraphs)
- Division words: སྟེ། / ལ། / དབྱེ་ན། following a topic heading
- Number word near a list of named items
- Verse listing items that prose then unpacks
- ལ་སོགས་པ། closing a partial list with a nearby number
- རྣམ་པ་ / གནས་ / ཚུལ་ / ཞེས་བྱ་བ་ within 30 words of a number

DO NOT MISS THESE:
- དང་པོ་ / གཉིས་པ་ / གསུམ་པ་ labels even when they appear alone as a single line
- Enumerations embedded inside verse (།-separated units)
- Closing counts even when the number is the only signal
- Nested candidates — extract both inner and outer separately
- Candidates in the overlap zone — extract once only

OUTPUT FORMAT — for each candidate output EXACTLY this block, nothing more:

[TYPE: A / B / C]
CANDIDATE: [exact Tibetan text as it appears in the source]
CONTEXT: [10 Tibetan words before + 10 Tibetan words after the candidate]
ITEMS: [each named item on its own line, numbered, in Tibetan]

No commentary. No analysis. No linking. If items cannot be determined, write
ITEMS: [implicit]. Separate candidate blocks with a single blank line.
If the chunk contains NO candidates at all, output exactly: NO CANDIDATES
"""

USER_PROMPT_TEMPLATE = """\
Extract every ས་བཅད candidate from the following text chunk. Output only the candidate \
blocks in the required format.

--- BEGIN CHUNK ---
{chunk_text}
--- END CHUNK ---
"""


# ------------------------------------------------------------------------------
# The tree-building prompt — converts the merged candidates into a nested,
# decimal-numbered TOC tree (matches the `add-toc` skill conventions).
# ------------------------------------------------------------------------------
TREE_SYSTEM_PROMPT = """\
You are an expert in classical Tibetan Buddhist ས་བཅད (sa bcad) structural outlines.

You are given a list of extracted ས་བཅད candidates from a single commentary, in
document order. Each candidate block looks like:

    [TYPE: A / B / C]
    CANDIDATE: <exact Tibetan>
    CONTEXT: <surrounding Tibetan>
    ITEMS: <numbered named sub-parts, or [implicit]>

Your task: reconstruct the FULL hierarchical table of contents (dkar-chag) as a
single nested tree, and emit it with hierarchical decimal numbering and Obsidian
block IDs.

HOW TO INFER HIERARCHY (read the Tibetan, do not guess from candidate order alone):

1. Ordinal prefixes mark sibling rank within one parent's enumeration:
   དང་པོ་=1, གཉིས་པ་=2, གསུམ་པ་=3, བཞི་པ་=4, ལྔ་པ་=5, དྲུག་པ་=6, བདུན་པ་=7, ...
   Bracket/parenthetical markers (༡༽, ༢༽, ཀ༽, ཁ༽) follow the same logic.
   A series restarts when a new parent is introduced.

2. An "announcement" candidate that introduces sub-items (ends in a count such as
   གཉིས་ཏེ། / གསུམ་སྟེ། / བཞི་ལས། / ...ལ།) is a PARENT. Its named ITEMS become its
   direct children, one level deeper. Each child that is itself later announced and
   subdivided becomes a parent in turn — match a child to the announcement that
   re-states and divides it.

3. When a peer ordinal reappears (e.g. གཉིས་པ་ after a run of children), return to
   the depth of the matching དང་པོ་ that opened that sibling series.

4. A short candidate that merely names one element of an enumeration (no trailing
   count phrase) is a leaf at its depth.

CLEAN each display string:
   - strip leading bullets, ordinal prefixes (དང་པོ། གཉིས་པ་ ...), bracket markers,
     and Tibetan decimal labels
   - strip trailing block IDs (^...) and wiki-link wrappers ([[#^id|text]] -> text)
   - convert trailing ལོ།། or །། to a single །
   - keep the full descriptive phrase otherwise — do not over-truncate

OUTPUT — emit ONLY the TOC block, exactly in this shape and nothing else:

## དཀར་ཆག / Table of Contents

* 1. <clean text> ^toc-1
   * 1.1 <clean text> ^toc-1-1
      * 1.1.1 <clean text> ^toc-1-1-1
   * 1.2 <clean text> ^toc-1-2
* 2. <clean text> ^toc-2

---

FORMAT RULES (follow exactly):
   - indent = 3 spaces × (depth − 1); depth-1 items have no indent
   - decimal = 1. for depth-1, 1.1 for depth-2, 1.1.1 for depth-3, etc.
   - block ID = ^toc- + the decimal with dots replaced by hyphens (1.1.1 -> ^toc-1-1-1)
   - one entry per line, no blank lines between entries
   - counters reset for deeper levels whenever you move up to a shallower level
   - cover the whole document; do not drop branches. Output Tibetan, no English,
     no commentary, no code fences.
"""

TREE_USER_PROMPT_TEMPLATE = """\
Build the full nested decimal-numbered table of contents from the following \
ས་བཅད candidate list for commentary "{commentary_id}". Output only the TOC block.

--- BEGIN CANDIDATES ---
{candidates_text}
--- END CANDIDATES ---
"""


# ------------------------------------------------------------------------------
# Chunking
# ------------------------------------------------------------------------------
def make_chunks(lines, chunk_size, overlap):
    """Return a list of (index, start_line, end_line, text) tuples (1-based line numbers)."""
    total = len(lines)
    chunks = []
    start = 0
    idx = 0
    while start < total:
        end = min(start + chunk_size, total)
        text = "".join(lines[start:end])
        chunks.append((idx, start + 1, end, text))
        idx += 1
        if end >= total:
            break
        start = end - overlap
    return chunks


# ------------------------------------------------------------------------------
# Gemini call
# ------------------------------------------------------------------------------
def get_client():
    try:
        from google import genai  # type: ignore
    except ImportError:
        sys.exit(
            "Error: google-genai is not installed.\n"
            "  Install it with:  pip install google-genai"
        )

    api_key = os.environ.get("GEMINI_API_KEY") or os.environ.get("GOOGLE_API_KEY")
    if not api_key:
        sys.exit(
            "Error: no API key found.\n"
            "  Set the GEMINI_API_KEY environment variable to your Gemini API key."
        )
    return genai.Client(api_key=api_key)


def extract_from_chunk(client, model, chunk_text):
    """Call Gemini on one chunk, with retries. Returns the model's text output."""
    from google.genai import types  # type: ignore

    config = types.GenerateContentConfig(
        system_instruction=SYSTEM_PROMPT,
        temperature=0.0,
        thinking_config=types.ThinkingConfig(thinking_budget=0),
    )
    contents = USER_PROMPT_TEMPLATE.format(chunk_text=chunk_text)

    last_err = None
    for attempt in range(1, MAX_RETRIES + 1):
        try:
            resp = client.models.generate_content(
                model=model,
                contents=contents,
                config=config,
            )
            return (resp.text or "").strip()
        except Exception as e:  # noqa: BLE001 - surface any API/transport error
            last_err = e
            if attempt < MAX_RETRIES:
                wait = RETRY_BACKOFF_SECONDS * attempt
                print(f"    ! attempt {attempt} failed ({e}); retrying in {wait}s...",
                      file=sys.stderr)
                time.sleep(wait)
    raise RuntimeError(f"Gemini call failed after {MAX_RETRIES} attempts: {last_err}")


def build_toc_tree(client, model, commentary_id, candidates_text):
    """Single Gemini call: turn the merged candidates into a nested TOC tree."""
    from google.genai import types  # type: ignore

    config = types.GenerateContentConfig(
        system_instruction=TREE_SYSTEM_PROMPT,
        temperature=0.0,
        thinking_config=types.ThinkingConfig(thinking_budget=0),
    )
    contents = TREE_USER_PROMPT_TEMPLATE.format(
        commentary_id=commentary_id,
        candidates_text=candidates_text,
    )

    last_err = None
    for attempt in range(1, MAX_RETRIES + 1):
        try:
            resp = client.models.generate_content(
                model=model,
                contents=contents,
                config=config,
            )
            text = (resp.text or "").strip()
            # defensively strip any stray code fences
            text = re.sub(r"^```[a-zA-Z]*\n?", "", text)
            text = re.sub(r"\n?```$", "", text)
            return text.strip()
        except Exception as e:  # noqa: BLE001
            last_err = e
            if attempt < MAX_RETRIES:
                wait = RETRY_BACKOFF_SECONDS * attempt
                print(f"    ! tree attempt {attempt} failed ({e}); retrying in {wait}s...",
                      file=sys.stderr)
                time.sleep(wait)
    raise RuntimeError(f"Tree-build call failed after {MAX_RETRIES} attempts: {last_err}")


# ------------------------------------------------------------------------------
# Helpers
# ------------------------------------------------------------------------------
def find_vault_root(start: Path) -> Path:
    """Walk upward looking for the vault root (the dir containing 4-SYSTEM/)."""
    for parent in [start, *start.parents]:
        if (parent / "4-SYSTEM").is_dir():
            return parent
    # Fallback: this script lives in <root>/4-SYSTEM/scripts/
    return Path(__file__).resolve().parents[2]


def infer_commentary_id(input_path: Path) -> str:
    stem = input_path.stem
    # strip a leading language tag like "bo-", "en-", "zh-"
    stem = re.sub(r"^(bo|en|zh|sk|pi|hi|ne|mn|ru)-", "", stem)
    # strip trailing helpers like "-toc", ".segmented"
    stem = re.sub(r"[-.](toc|segmented|raw)$", "", stem)
    return stem


def count_candidates(text: str) -> int:
    return len(re.findall(r"^\s*\[TYPE:", text, flags=re.MULTILINE))


# ------------------------------------------------------------------------------
# Main
# ------------------------------------------------------------------------------
def main():
    parser = argparse.ArgumentParser(
        description="Extract ས་བཅད (sa bcad) TOC candidates from Tibetan commentary "
                    "using Gemini Flash.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument("input_file", help="Path to the input .md/.txt file")
    parser.add_argument("--commentary-id", default=None,
                        help="Short id for output paths (default: inferred from filename)")
    parser.add_argument("--model", default=DEFAULT_MODEL,
                        help=f"Gemini model (default: {DEFAULT_MODEL})")
    parser.add_argument("--chunk-size", type=int, default=DEFAULT_CHUNK_SIZE,
                        help=f"Lines per chunk (default: {DEFAULT_CHUNK_SIZE})")
    parser.add_argument("--overlap", type=int, default=DEFAULT_OVERLAP,
                        help=f"Overlap lines between chunks (default: {DEFAULT_OVERLAP})")
    parser.add_argument("--vault-root", default=None,
                        help="Vault root (dir containing 4-SYSTEM/). Default: auto-detect.")
    parser.add_argument("--temp-dir", default=None,
                        help="Override per-chunk staging dir "
                             "(default: <root>/0-INBOX/temp/<commentary-id>/)")
    parser.add_argument("--out", default=None,
                        help="Override combined candidates file "
                             "(default: <root>/0-INBOX/toc-candidates-<commentary-id>.md)")
    parser.add_argument("--tree-out", default=None,
                        help="Override TOC-tree output file "
                             "(default: <root>/0-INBOX/toc-tree-<commentary-id>.md)")
    parser.add_argument("--no-tree", action="store_true",
                        help="Stop after merging candidates; skip the TOC-tree step")
    parser.add_argument("--force", action="store_true",
                        help="Re-process all chunks even if result files already exist")
    parser.add_argument("--dry-run", action="store_true",
                        help="Chunk and set up paths but do NOT call Gemini")
    args = parser.parse_args()

    input_path = Path(args.input_file).expanduser().resolve()
    if not input_path.exists():
        sys.exit(f"Error: file not found: {input_path}")

    commentary_id = args.commentary_id or infer_commentary_id(input_path)
    vault_root = Path(args.vault_root).resolve() if args.vault_root else find_vault_root(input_path)

    temp_dir = Path(args.temp_dir).resolve() if args.temp_dir \
        else vault_root / TEMP_SUBDIR / commentary_id
    out_file = Path(args.out).resolve() if args.out \
        else vault_root / FINAL_SUBDIR / f"toc-candidates-{commentary_id}.md"
    tree_file = Path(args.tree_out).resolve() if args.tree_out \
        else vault_root / FINAL_SUBDIR / f"toc-tree-{commentary_id}.md"

    temp_dir.mkdir(parents=True, exist_ok=True)
    out_file.parent.mkdir(parents=True, exist_ok=True)

    lines = input_path.read_text(encoding="utf-8").splitlines(keepends=True)
    chunks = make_chunks(lines, args.chunk_size, args.overlap)

    print(f"Input:        {input_path}")
    print(f"Commentary:   {commentary_id}")
    print(f"Lines:        {len(lines)}  ->  {len(chunks)} chunks "
          f"(size={args.chunk_size}, overlap={args.overlap})")
    print(f"Model:        {args.model}")
    print(f"Staging dir:  {temp_dir}")
    print(f"Candidates:   {out_file}")
    if not args.no_tree:
        print(f"TOC tree:     {tree_file}")
    print()

    if args.dry_run:
        print("Dry run — no API calls made. Chunk plan:")
        for idx, start, end, _ in chunks:
            print(f"  chunk_{idx:03d}: lines {start}–{end}")
        return

    client = get_client()

    # ---- Step 3: per-chunk extraction (resumable) ----
    for idx, start, end, text in chunks:
        chunk_out = temp_dir / f"chunk_{idx:03d}.md"
        if chunk_out.exists() and not args.force:
            print(f"  chunk_{idx:03d} (lines {start}–{end})  [skip — exists]")
            continue

        print(f"  chunk_{idx:03d} (lines {start}–{end})  → Gemini ...", flush=True)
        result = extract_from_chunk(client, args.model, text)

        header = f"<!-- chunk {idx:03d} | lines {start}–{end} | source: {commentary_id} -->\n\n"
        if not result or result.strip().upper() == "NO CANDIDATES":
            body = "<!-- no candidates -->\n"
        else:
            body = result.rstrip() + "\n"
        chunk_out.write_text(header + body, encoding="utf-8")

    # ---- Step 4: combine ----
    combined_parts = []
    total_candidates = 0
    for idx, start, end, _ in chunks:
        chunk_out = temp_dir / f"chunk_{idx:03d}.md"
        if not chunk_out.exists():
            print(f"  ! missing {chunk_out.name}; skipping in combine", file=sys.stderr)
            continue
        content = chunk_out.read_text(encoding="utf-8")
        total_candidates += count_candidates(content)
        combined_parts.append(content.rstrip() + "\n")

    frontmatter = (
        "---\n"
        f"source: {commentary_id}\n"
        "skill: toc-candidate-extraction\n"
        f"date: {date.today().isoformat()}\n"
        f"model: {args.model}\n"
        f"total_candidates: {total_candidates}\n"
        "---\n\n"
    )
    candidates_doc = frontmatter + "\n".join(combined_parts)
    out_file.write_text(candidates_doc, encoding="utf-8")

    print()
    print(f"✓ Candidates merged: {total_candidates} candidates across {len(chunks)} chunks.")
    print(f"  {out_file}")

    # ---- Step 5: build the nested decimal TOC tree ----
    if args.no_tree:
        return

    print()
    print("Building TOC tree from candidates → Gemini ...", flush=True)
    tree_body = build_toc_tree(client, args.model, commentary_id, candidates_doc)

    tree_frontmatter = (
        "---\n"
        f"source: {commentary_id}\n"
        "skill: toc-candidate-extraction\n"
        "stage: toc-tree\n"
        f"date: {date.today().isoformat()}\n"
        f"model: {args.model}\n"
        "---\n\n"
    )
    tree_file.write_text(tree_frontmatter + tree_body.rstrip() + "\n", encoding="utf-8")

    print()
    print("✓ Done.")
    print(f"  Candidates: {out_file}")
    print(f"  TOC tree:   {tree_file}")


if __name__ == "__main__":
    main()
