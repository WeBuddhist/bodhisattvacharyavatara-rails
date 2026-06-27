#!/usr/bin/env python3
"""
resegment.py — meaningful block re-segmentation for Tibetan commentaries.

Takes a Stage-1 rule-segmented commentary (with TOC headings embedded by a
separate TOC-inclusion step) and uses an LLM to flag merge/split operations
that produce semantically coherent, citation-sized blocks. A deterministic
script applies the operations and verifies text integrity.

Pipeline:
    commentary-segmentation Stage 1
         ↓
    [TOC inclusion — headings embedded]
         ↓
    resegment.py   ← THIS SCRIPT
         ↓
    block-ID stamping

Setup:
    pip install google-genai
    set GEMINI_API_KEY=...   (Windows)
    export GEMINI_API_KEY=... (macOS / Linux)

Usage:
    # basic run (commentary-id inferred from filename):
    python3 4-SYSTEM/Skills/block-resegmentation/scripts/resegment.py \\
        "0-INBOX/segmented/bo-kunpal.md"

    # explicit id:
    python3 4-SYSTEM/Skills/block-resegmentation/scripts/resegment.py \\
        "0-INBOX/segmented/bo-kunpal.md" --commentary-id kunpal

    # resume interrupted run (skips windows already staged):
    python3 ... "0-INBOX/segmented/bo-kunpal.md" --commentary-id kunpal

    # force reprocess all windows:
    python3 ... "0-INBOX/segmented/bo-kunpal.md" --commentary-id kunpal --force

    # apply already-staged ops without new LLM calls:
    python3 ... "0-INBOX/segmented/bo-kunpal.md" --commentary-id kunpal --apply-only

    # integrity check only, write nothing:
    python3 ... "0-INBOX/segmented/bo-kunpal.md" --commentary-id kunpal --dry-run
"""

import argparse
import json
import os
import random
import re
import sys
import time
from pathlib import Path

# ── defaults ─────────────────────────────────────────────────────────────────

DEFAULT_MODEL          = "gemini-2.5-flash"
DEFAULT_FALLBACK_MODEL = "gemini-2.0-flash"
DEFAULT_WINDOW_SIZE    = 40    # blocks per LLM window
DEFAULT_OVERLAP        = 5     # overlap blocks between adjacent windows
MAX_RETRIES            = 8
RETRY_BACKOFF_BASE     = 8     # seconds; grows exponentially per attempt
MAX_BACKOFF            = 120   # cap on a single wait

TEMP_BASE   = "0-INBOX/temp"
OUTPUT_BASE = "0-INBOX/resegmented"

# ── prompts ───────────────────────────────────────────────────────────────────

SYSTEM_PROMPT = """\
You are an expert in classical Tibetan Buddhist commentary (འགྲེལ་པ་) structure.

You are given a numbered list of text blocks from a Tibetan commentary. These blocks
were produced by a rule-based segmenter that fires on syntactic signals (terminal
particles, syllable caps). Some blocks are over-split — adjacent blocks that together
form one complete thought. Some are under-split — one block that spans two distinct
thoughts.

YOUR TASK: output a JSON list of merge and split operations to produce semantically
coherent blocks. Each block should be one citable thought unit — the minimum
self-contained passage a downstream context file would want to cite independently.

━━━ MERGE — when adjacent blocks form one complete thought ━━━

M1  INCOMPLETE SENTENCE
    A block ends with a connector particle that grammatically requires continuation
    in the next block: དང་། / ཞིང་། / ཅིང་། / ནས། / ལས། / སྟེ། / ཏེ།
    Merge it with the next block.

M2  BROKEN VERSE STANZA
    A standard Tibetan verse stanza has 4 pādas (~7–9 syllables each, ending with །).
    If a block has only 1–2 pādas and the stanza continues into the next block,
    merge all pādas of the stanza into one block.
    NEVER merge two independent stanzas. NEVER split a stanza across blocks.

M3  LEAD-IN ORPHANED FROM CONTENT
    A block ends with a transition phrase that introduces the following block:
    e.g. བོད་སྐད་དུ། / འདི་ལྟར། / topic-opener དེ་ལ།
    Merge the lead-in block with the block it introduces.

M4  INCOMPLETE ENUMERATION
    A block opens an enumeration (གཉིས་ཏེ། / གསུམ་སྟེ། / བཞི་ལས། etc.) and the
    remaining enumerated items continue in the next block(s).
    Merge until the enumeration is complete.

━━━ SPLIT — when one block spans two distinct thoughts ━━━

S1  OBJECTION + REPLY IN ONE BLOCK
    A block contains both an objection marker (ཅེ་ན། / ཞེ་ན། / སྙམ་ན།) and a reply
    opener (འོ་ན། / དེ་ལར་ན།). Split between them.

S2  TERMINAL PARTICLE + NEW TOPIC
    A block has a sentence-final marker (སོ། །/ འོ། །/ ནོ། །/ དོ། །) mid-block,
    immediately followed by a new ordinal opener (དང་པོ་ / གཉིས་པ་ / གསུམ་པ་) or
    a new subject. Split after the terminal particle.

S3  SOURCE ATTRIBUTION FUSED TO QUOTE
    A block opens with a source attribution phrase (…ལས། or …གསུངས།) fused directly
    to the quoted passage. Split after the attribution so it stands alone.

━━━ HEADING BLOCKS — always KEEP ━━━

Any block that begins with # (a markdown heading) is a structural TOC marker.
NEVER include it in a merge or split operation.

━━━ OUTPUT FORMAT ━━━

A JSON array of operations. Blocks not mentioned are kept as-is.

[
  {"op": "merge", "blocks": [N, M]},
  {"op": "merge", "blocks": [N, M, P]},
  {"op": "split", "block": N, "after": "<verbatim unique substring ending at split point>"},
  {"op": "split", "block": N, "after": ["<sub1>", "<sub2>", "<sub3>"]}
]

Rules for the output:
- Block numbers are CONTINUOUS and INCLUDE heading blocks. You may only merge blocks
  with consecutive numbers (e.g. N and N+1). If a heading block sits between two
  content blocks they are NOT consecutive — never merge across a heading, and never
  propose a merge whose numbers skip over one (e.g. [1, 3]).
- Each block number appears in AT MOST ONE operation.
- A single split block may have MORE THAN ONE cut point: set "after" to a LIST of
  substrings, in document order, to break one long block into 3 or more thought units.
- For each "after" substring: copy a verbatim slice from the block that ends exactly
  at the split point and is UNIQUE within that block (10–20 characters is usually enough).
- If nothing needs to change in this window, output: []
- Output ONLY the JSON array. No explanation, no commentary, no code fences.
"""

USER_PROMPT_TEMPLATE = """\
Review the following blocks from a Tibetan commentary and output the merge/split \
operations needed to make each block a single citable thought unit. Block numbers \
are global (file-level).

--- BEGIN BLOCKS ---
{blocks_text}
--- END BLOCKS ---
"""

# ── block parsing ─────────────────────────────────────────────────────────────

FRONTMATTER_RE = re.compile(r'^---[ \t]*\r?\n.*?\r?\n---[ \t]*\r?\n', re.DOTALL)


def parse_file(path: Path):
    """
    Return (frontmatter: str, blocks: list[str]).
    Frontmatter is the YAML block; blocks are split on double newlines.
    """
    text = path.read_text(encoding="utf-8")
    frontmatter = ""
    body = text
    m = FRONTMATTER_RE.match(text)
    if m:
        frontmatter = m.group(0)
        body = text[m.end():]
    raw = re.split(r'\n{2,}', body)
    blocks = [b.strip() for b in raw if b.strip()]
    return frontmatter, blocks


def is_heading(block: str) -> bool:
    return block.lstrip().startswith('#')


def squeeze(text: str) -> str:
    """Strip all whitespace — used for integrity comparison."""
    return re.sub(r'\s+', '', text)


# ── windowing ─────────────────────────────────────────────────────────────────

def make_windows(blocks, window_size, overlap):
    """
    Return a list of window dicts:
      {idx, start (0-based inclusive), end (0-based exclusive), blocks}
    Block numbers shown to the LLM are 1-based (start+1 .. end).
    """
    total = len(blocks)
    windows = []
    start = 0
    idx = 0
    while start < total:
        end = min(start + window_size, total)
        windows.append({
            "idx":    idx,
            "start":  start,
            "end":    end,
            "blocks": blocks[start:end],
        })
        idx += 1
        if end >= total:
            break
        start = end - overlap
    return windows


def format_window(window):
    """Format window blocks for the LLM, with 1-based global block numbers."""
    parts = []
    for i, block in enumerate(window["blocks"]):
        gn = window["start"] + i + 1  # 1-based global number
        tag = " [HEADING]" if is_heading(block) else ""
        parts.append(f"[Block {gn}{tag}]\n{block}")
    return "\n\n".join(parts)


# ── Gemini API ────────────────────────────────────────────────────────────────

def get_client():
    try:
        from google import genai  # noqa: PLC0415
    except ImportError:
        sys.exit(
            "Error: google-genai is not installed.\n"
            "  Run: pip install google-genai"
        )
    api_key = os.environ.get("GEMINI_API_KEY") or os.environ.get("GOOGLE_API_KEY")
    if not api_key:
        sys.exit(
            "Error: no API key found.\n"
            "  Set the GEMINI_API_KEY environment variable."
        )
    return genai.Client(api_key=api_key)


def _is_overloaded(err) -> bool:
    s = str(err).upper()
    return any(tok in s for tok in (
        "503", "UNAVAILABLE", "OVERLOADED", "HIGH DEMAND",
        "429", "RESOURCE_EXHAUSTED",
    ))


def _generate(client, model, user_prompt, fallback_model="", label="window"):
    try:
        from google.genai import types  # noqa: PLC0415
    except ImportError:
        sys.exit("Error: google-genai not installed.")

    config = types.GenerateContentConfig(
        system_instruction=SYSTEM_PROMPT,
        temperature=0.0,
        thinking_config=types.ThinkingConfig(thinking_budget=0),
    )
    models_to_try = [model]
    if fallback_model and fallback_model != model:
        models_to_try.append(fallback_model)

    last_err = None
    for mi, mdl in enumerate(models_to_try):
        if mi > 0:
            print(f"    -> '{model}' still overloaded; falling back to '{mdl}'",
                  file=sys.stderr)
        for attempt in range(1, MAX_RETRIES + 1):
            try:
                resp = client.models.generate_content(
                    model=mdl, contents=user_prompt, config=config,
                )
                return (resp.text or "").strip()
            except Exception as e:  # noqa: BLE001
                last_err = e
                if attempt < MAX_RETRIES:
                    base = min(RETRY_BACKOFF_BASE * (2 ** (attempt - 1)), MAX_BACKOFF)
                    wait = base + random.uniform(0, base * 0.25)
                    kind = "overloaded" if _is_overloaded(e) else "error"
                    print(f"    ! {label} attempt {attempt}/{MAX_RETRIES} {kind}: {e}; "
                          f"retrying in {wait:.0f}s...", file=sys.stderr)
                    time.sleep(wait)
        if not _is_overloaded(last_err):
            break
    raise RuntimeError(f"Gemini call failed after retries: {last_err}")


def call_llm_for_window(client, model, window, fallback_model=""):
    """Call the LLM for one window. Returns list of operation dicts."""
    blocks_text = format_window(window)
    user_prompt = USER_PROMPT_TEMPLATE.format(blocks_text=blocks_text)
    label = f"window-{window['idx'] + 1}"
    raw = _generate(client, model, user_prompt, fallback_model=fallback_model,
                    label=label)
    # strip code fences if the model wrapped the JSON
    raw = re.sub(r'^```(?:json)?\s*', '', raw.strip())
    raw = re.sub(r'\s*```$', '', raw.strip())
    try:
        ops = json.loads(raw)
        if not isinstance(ops, list):
            print(f"  ! {label}: LLM returned non-list JSON — treating as []",
                  file=sys.stderr)
            return []
        return ops
    except json.JSONDecodeError as e:
        print(f"  ! {label}: JSON parse error ({e}) — treating as []. Raw:\n{raw[:200]}",
              file=sys.stderr)
        return []


# ── staging ───────────────────────────────────────────────────────────────────

def staging_path(staging_dir: Path, window_idx: int) -> Path:
    return staging_dir / f"window-{window_idx:04d}.json"


def save_window_result(staging_dir: Path, window: dict, ops: list):
    staging_dir.mkdir(parents=True, exist_ok=True)
    data = {
        "window_idx":  window["idx"],
        "start_block": window["start"] + 1,   # 1-based
        "end_block":   window["end"],           # 1-based inclusive
        "operations":  ops,
    }
    staging_path(staging_dir, window["idx"]).write_text(
        json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8"
    )


def load_window_result(staging_dir: Path, window_idx: int):
    p = staging_path(staging_dir, window_idx)
    if not p.exists():
        return None
    return json.loads(p.read_text(encoding="utf-8"))


# ── combine operations ────────────────────────────────────────────────────────

def _op_key(op):
    """Hashable identity for an operation."""
    if op["op"] == "merge":
        return ("merge", tuple(sorted(op["blocks"])))
    else:
        after = op.get("after", "")
        after_key = tuple(after) if isinstance(after, list) else after
        return ("split", op["block"], after_key)


def combine_operations(window_results, blocks):
    """
    Merge per-window operation lists into one deduplicated list.

    For blocks in the overlap zone (appearing in two consecutive windows):
    - If both windows produce the same operation → include it once.
    - If they disagree → conflict: excluded from ops_to_apply.

    Returns (ops_to_apply: list, conflicts: list)
    """
    # block_n (1-based) -> list of (window_idx, op)
    block_claims: dict = {}

    for wr in window_results:
        w_idx = wr["window_idx"]
        for op in wr["operations"]:
            if op["op"] == "merge":
                for bn in op["blocks"]:
                    block_claims.setdefault(bn, []).append((w_idx, op))
            elif op["op"] == "split":
                bn = op["block"]
                block_claims.setdefault(bn, []).append((w_idx, op))

    seen_keys: set = set()
    ops_to_apply = []
    conflicts = []

    for bn, entries in block_claims.items():
        keys = [_op_key(e[1]) for e in entries]
        unique_keys = list(dict.fromkeys(keys))
        if len(unique_keys) == 1:
            key = unique_keys[0]
            if key not in seen_keys:
                seen_keys.add(key)
                ops_to_apply.append(entries[0][1])
        else:
            conflicts.append({
                "block":      bn,
                "operations": [e[1] for e in entries],
                "windows":    [e[0] for e in entries],
            })

    return ops_to_apply, conflicts


# ── validate operations ───────────────────────────────────────────────────────

def validate_operations(ops, blocks):
    """
    Validate:
    - Merge blocks are consecutive and in ascending order.
    - Split has a non-empty 'after' substring.
    - No block appears in more than one operation.
    - No operation touches a heading block.

    Returns (valid_ops: list, errors: list[str])
    """
    total = len(blocks)
    claimed: dict = {}   # block_n -> op
    errors = []
    valid_ops = []

    for op in ops:
        if op["op"] == "merge":
            bns = op.get("blocks", [])
            if len(bns) < 2:
                errors.append(f"merge {bns}: need at least 2 blocks")
                continue
            # ascending + consecutive check
            sorted_bns = sorted(bns)
            if sorted_bns != bns:
                errors.append(f"merge {bns}: not in ascending order — auto-sorted")
                bns = sorted_bns
                op = {**op, "blocks": bns}
            ok = True
            for i in range(len(bns) - 1):
                if bns[i + 1] != bns[i] + 1:
                    errors.append(f"merge {bns}: blocks are not consecutive")
                    ok = False
                    break
            if not ok:
                continue
            # heading check
            heading_hit = [b for b in bns if 1 <= b <= total and is_heading(blocks[b - 1])]
            if heading_hit:
                errors.append(f"merge {bns}: includes heading block(s) {heading_hit} — skipped")
                continue
            # claim check
            conflict = [b for b in bns if b in claimed]
            if conflict:
                errors.append(f"merge {bns}: block(s) {conflict} already claimed — skipped")
                continue
            for b in bns:
                claimed[b] = op
            valid_ops.append(op)

        elif op["op"] == "split":
            bn = op.get("block")
            after = op.get("after", "")
            if not bn:
                errors.append(f"split: missing 'block' field — skipped")
                continue
            afters = after if isinstance(after, list) else [after]
            if not afters or any(not a for a in afters):
                errors.append(f"split block {bn}: missing/empty 'after' substring — skipped")
                continue
            if 1 <= bn <= total and is_heading(blocks[bn - 1]):
                errors.append(f"split block {bn}: is a heading — skipped")
                continue
            if bn in claimed:
                errors.append(f"split block {bn}: already claimed by another op — skipped")
                continue
            claimed[bn] = op
            valid_ops.append(op)

        else:
            errors.append(f"unknown op type: {op.get('op')} — skipped")

    return valid_ops, errors


# ── apply operations ──────────────────────────────────────────────────────────

def apply_operations(blocks, ops):
    """
    Apply validated merge and split operations to the block list.
    Returns a new block list. Original list is not modified.

    blocks: 0-based list of block strings
    ops:    operations with 1-based block numbers
    """
    # Build lookup: 1-based block_n -> op
    block_to_op: dict = {}
    for op in ops:
        if op["op"] == "merge":
            for bn in op["blocks"]:
                block_to_op[bn] = op
        elif op["op"] == "split":
            block_to_op[op["block"]] = op

    new_blocks = []
    i = 0  # 0-based index into blocks
    while i < len(blocks):
        bn = i + 1  # 1-based

        if bn not in block_to_op:
            new_blocks.append(blocks[i])
            i += 1
            continue

        op = block_to_op[bn]

        if op["op"] == "merge":
            if op["blocks"][0] == bn:
                # Start of merge group — consume all blocks in the group
                texts = [blocks[b - 1] for b in op["blocks"]]
                merged = "\n".join(texts)
                new_blocks.append(merged)
                i += len(op["blocks"])
            else:
                # Middle/tail of merge group — already consumed; skip
                i += 1

        elif op["op"] == "split":
            block_text = blocks[i]
            after_val  = op["after"]
            cut_strs   = after_val if isinstance(after_val, list) else [after_val]
            cut_positions = []
            ok = True
            for after_str in cut_strs:
                occ = block_text.count(after_str)
                if occ == 0:
                    print(f"  ! split block {bn}: substring not found: {after_str!r}; "
                          f"keeping block whole", file=sys.stderr)
                    ok = False
                    break
                if occ > 1:
                    print(f"  ! split block {bn}: substring not unique "
                          f"({occ} occurrences): {after_str!r}; "
                          f"keeping block whole", file=sys.stderr)
                    ok = False
                    break
                cut_positions.append(block_text.find(after_str) + len(after_str))
            if not ok:
                new_blocks.append(block_text)
            else:
                parts = []
                prev = 0
                for pos in sorted(set(cut_positions)):
                    seg = block_text[prev:pos].strip()
                    if seg:
                        parts.append(seg)
                    prev = pos
                tail = block_text[prev:].strip()
                if tail:
                    parts.append(tail)
                new_blocks.extend(parts if parts else [block_text])
            i += 1

    return new_blocks


# ── integrity check ───────────────────────────────────────────────────────────

def check_integrity(input_path: Path, frontmatter: str, new_blocks: list):
    """
    Verify squeeze(original file) == squeeze(reconstructed output).
    Returns (ok: bool, detail: str)
    """
    original_text = input_path.read_text(encoding="utf-8")
    result_text   = frontmatter + "\n\n".join(new_blocks)

    orig_sq   = squeeze(original_text)
    result_sq = squeeze(result_text)

    if orig_sq == result_sq:
        return True, "OK"

    # find first difference for a helpful error message
    for i, (a, b) in enumerate(zip(orig_sq, result_sq)):
        if a != b:
            ctx_o = orig_sq[max(0, i - 30): i + 30]
            ctx_r = result_sq[max(0, i - 30): i + 30]
            return False, (
                f"First difference at squeezed char {i}:\n"
                f"  original: ...{ctx_o!r}...\n"
                f"  result:   ...{ctx_r!r}..."
            )

    return False, (
        f"Length mismatch: original {len(orig_sq)} chars, result {len(result_sq)} chars"
    )


# ── output writers ────────────────────────────────────────────────────────────

def write_output(output_path: Path, frontmatter: str, new_blocks: list):
    output_path.parent.mkdir(parents=True, exist_ok=True)
    text = frontmatter + "\n\n".join(new_blocks) + "\n"
    output_path.write_text(text, encoding="utf-8")


def write_ops_log(log_path: Path, ops_applied, errors, conflicts,
                  orig_blocks, new_blocks, commentary_id):
    log_path.parent.mkdir(parents=True, exist_ok=True)

    def preview(text, n=80):
        t = text.replace("\n", " ")
        return t[:n] + ("…" if len(t) > n else "")

    lines = [
        f"# Block Resegmentation Log — {commentary_id}",
        "",
        f"Original blocks : {len(orig_blocks)}",
        f"Result blocks   : {len(new_blocks)}",
        f"Ops applied     : {len(ops_applied)}",
        f"Errors skipped  : {len(errors)}",
        f"Conflicts       : {len(conflicts)}",
        "",
    ]

    if ops_applied:
        lines += ["## Applied Operations", ""]
        for op in ops_applied:
            if op["op"] == "merge":
                bns = op["blocks"]
                lines.append(f"**MERGE** blocks {bns}")
                for bn in bns:
                    lines.append(f"  Block {bn}: {preview(orig_blocks[bn - 1])}")
                lines.append("")
            elif op["op"] == "split":
                bn = op["block"]
                af = op['after']
                af_disp = af if isinstance(af, str) else " | ".join(af)
                lines.append(f"**SPLIT** block {bn}  after: `{af_disp}`")
                lines.append(f"  Block {bn}: {preview(orig_blocks[bn - 1])}")
                lines.append("")

    if errors:
        lines += ["## Skipped (Validation Errors)", ""]
        for e in errors:
            lines.append(f"- {e}")
        lines.append("")

    if conflicts:
        lines += ["## Conflicts — Manual Review Required", ""]
        lines += [
            "These blocks appeared in two overlapping windows with different operations.",
            "Edit the relevant `window-NNNN.json` staging file and re-run with `--apply-only`.",
            "",
        ]
        for c in conflicts:
            lines.append(f"Block {c['block']} — windows {c['windows']}:")
            for cop in c["operations"]:
                lines.append(f"  {cop}")
            lines.append("")

    log_path.write_text("\n".join(lines), encoding="utf-8")


# ── main ──────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(
        description="Meaningful block re-segmentation for Tibetan commentaries.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument("input_file",
                        help="Stage-1 segmented commentary with TOC headings embedded")
    parser.add_argument("--commentary-id", default="",
                        help="Short ID for output filenames (inferred from filename if omitted)")
    parser.add_argument("--window-size", type=int, default=DEFAULT_WINDOW_SIZE,
                        help=f"Blocks per LLM window (default: {DEFAULT_WINDOW_SIZE})")
    parser.add_argument("--overlap", type=int, default=DEFAULT_OVERLAP,
                        help=f"Overlap blocks between adjacent windows (default: {DEFAULT_OVERLAP})")
    parser.add_argument("--model", default=DEFAULT_MODEL,
                        help=f"Gemini model (default: {DEFAULT_MODEL})")
    parser.add_argument("--fallback-model", default=DEFAULT_FALLBACK_MODEL,
                        help=f"Fallback model if primary is overloaded (default: {DEFAULT_FALLBACK_MODEL})")
    parser.add_argument("--force", action="store_true",
                        help="Reprocess all windows even if staging files exist")
    parser.add_argument("--apply-only", action="store_true",
                        help="Skip LLM calls; apply already-staged operations")
    parser.add_argument("--dry-run", action="store_true",
                        help="Run integrity check only; write no output files")
    args = parser.parse_args()

    input_path = Path(args.input_file)
    if not input_path.exists():
        sys.exit(f"Error: input file not found: {input_path}")

    # resolve commentary id
    cid = args.commentary_id or input_path.stem

    # resolve vault root (walk up looking for 4-SYSTEM/)
    vault_root = input_path.resolve().parent
    for _ in range(8):
        if (vault_root / "4-SYSTEM").exists():
            break
        vault_root = vault_root.parent
    else:
        vault_root = Path(".").resolve()

    staging_dir  = vault_root / TEMP_BASE    / f"RESEG-{cid}" / "windows"
    output_path  = vault_root / OUTPUT_BASE  / f"{cid}.reseg.md"
    log_path     = vault_root / OUTPUT_BASE  / f"{cid}.ops.md"

    print(f"Input:      {input_path}")
    print(f"ID:         {cid}")
    print(f"Vault root: {vault_root}")
    print(f"Staging:    {staging_dir}")
    print(f"Output:     {output_path}")
    print()

    # ── parse ──
    frontmatter, blocks = parse_file(input_path)
    total = len(blocks)
    heading_count = sum(1 for b in blocks if is_heading(b))
    print(f"Blocks: {total}  (headings: {heading_count}, content: {total - heading_count})")

    windows = make_windows(blocks, args.window_size, args.overlap)
    print(f"Windows: {len(windows)}  (size={args.window_size}, overlap={args.overlap})")
    print()

    # ── LLM phase ──
    if not args.apply_only:
        client = get_client()
        for win in windows:
            label = (f"Window {win['idx'] + 1}/{len(windows)} "
                     f"(blocks {win['start'] + 1}–{win['end']})")
            already = load_window_result(staging_dir, win["idx"])
            if already and not args.force:
                n_ops = len(already.get("operations", []))
                print(f"  {label}: already staged ({n_ops} op(s)) — skipping")
                continue
            print(f"  {label}: calling LLM...")
            ops = call_llm_for_window(client, args.model, win, args.fallback_model)
            save_window_result(staging_dir, win, ops)
            print(f"    → {len(ops)} operation(s) flagged")
    else:
        print("--apply-only: skipping LLM calls, loading staged results.")

    # ── load staged results ──
    window_results = []
    missing = []
    for win in windows:
        result = load_window_result(staging_dir, win["idx"])
        if result is None:
            missing.append(win["idx"] + 1)
            window_results.append({"window_idx": win["idx"], "operations": []})
        else:
            window_results.append(result)
    if missing:
        print(f"\nWarning: missing staging files for window(s): {missing}")
        print("Re-run without --apply-only to process missing windows.\n")

    # ── combine ──
    ops_raw, conflicts = combine_operations(window_results, blocks)

    # ── validate ──
    ops_valid, validation_errors = validate_operations(ops_raw, blocks)

    # ── report ──
    print(f"\nOperations to apply: {len(ops_valid)}")
    for op in ops_valid:
        if op["op"] == "merge":
            print(f"  MERGE {op['blocks']}")
        else:
            af = op['after']
            af_disp = af if isinstance(af, str) else " | ".join(af)
            print(f"  SPLIT block {op['block']} after: {af_disp[:50]!r}")

    if validation_errors:
        print(f"\nValidation errors ({len(validation_errors)}) — skipped:")
        for e in validation_errors:
            print(f"  - {e}")

    if conflicts:
        print(f"\nConflicts in overlap zone ({len(conflicts)}) — not applied:")
        for c in conflicts:
            print(f"  - Block {c['block']}: windows {c['windows']}")

    # ── apply ──
    new_blocks = apply_operations(blocks, ops_valid)
    print(f"\nBlocks: {total} → {len(new_blocks)}")

    # ── integrity check ──
    ok, detail = check_integrity(input_path, frontmatter, new_blocks)
    if not ok:
        print(f"\n✗ INTEGRITY CHECK FAILED")
        print(f"  {detail}")
        print("\nOutput NOT written. Investigate the error above.")
        sys.exit(1)
    print("✓ Integrity check passed")

    if args.dry_run:
        print("\n--dry-run: no files written.")
        return

    # ── write output ──
    write_output(output_path, frontmatter, new_blocks)
    write_ops_log(log_path, ops_valid, validation_errors, conflicts,
                  blocks, new_blocks, cid)

    print(f"\nOutput:  {output_path}")
    print(f"Ops log: {log_path}")

    if conflicts:
        print(f"\n⚑ {len(conflicts)} conflict(s) require manual review — see ops log.")
        print("  Edit the relevant staging file(s) and re-run with --apply-only.")


if __name__ == "__main__":
    main()
