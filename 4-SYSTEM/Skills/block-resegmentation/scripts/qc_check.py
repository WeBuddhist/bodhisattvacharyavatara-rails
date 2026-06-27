#!/usr/bin/env python3
"""
qc_check.py — Quality-control pass for block-resegmented Tibetan commentaries.

Mirrors the QC pattern in toc_tree_extractor/extract_toc_tree.py:

  Step 1  Deterministic checks — scan every block for known boundary violations.
          No API call; instant.

  Step 2  LLM repair — send the issues list + flagged blocks (with context) to
          Gemini. Gemini outputs correction operations (same JSON format as
          resegment.py). Script applies them and verifies text integrity.

  Step 3  Re-check — run the deterministic checks again on the repaired output
          to count remaining issues.

  Step 4  Write QC report — flags_before, corrections applied, flags_after.

By default, Steps 1–4 all run. Use --no-fix to run detection only (Steps 1 + 4).

Pipeline position:
    resegment.py  →  qc_check.py  →  human approval

Usage:
    # full QC (detect + repair + re-check):
    python3 4-SYSTEM/Skills/block-resegmentation/scripts/qc_check.py \\
        "0-INBOX/resegmented/bo-kunpal.reseg.md"

    # detection only (no LLM repair):
    python3 4-SYSTEM/Skills/block-resegmentation/scripts/qc_check.py \\
        "0-INBOX/resegmented/bo-kunpal.reseg.md" --no-fix

    # dry run (compute corrections but do not write files):
    python3 4-SYSTEM/Skills/block-resegmentation/scripts/qc_check.py \\
        "0-INBOX/resegmented/bo-kunpal.reseg.md" --dry-run

Set GEMINI_API_KEY before running (not needed with --no-fix).
"""

import argparse
import json
import os
import random
import re
import sys
import time
from datetime import date
from pathlib import Path

# ── defaults ─────────────────────────────────────────────────────────────────

DEFAULT_MODEL          = "gemini-2.5-flash"
DEFAULT_FALLBACK_MODEL = "gemini-2.0-flash"
MAX_RETRIES            = 8
RETRY_BACKOFF_BASE     = 8
MAX_BACKOFF            = 120

OVER_LENGTH_THRESHOLD  = 60   # syllables
SHORT_FRAGMENT_MIN     = 4    # syllables

# Surrounding blocks shown to the LLM per flagged block
CONTEXT_WINDOW = 2

# ── QC system prompt ──────────────────────────────────────────────────────────

QC_SYSTEM_PROMPT = """\
You are an expert in classical Tibetan Buddhist commentary (འགྲེལ་པ་) structure.

A deterministic checker has scanned a block-resegmented Tibetan commentary and
produced a list of issues. Your job is to review each flagged block in context,
decide whether it is a real issue or a false positive, and output correction
operations for real issues only.

━━━ ISSUE TYPES ━━━

CONNECTOR_ENDING
  The block ends with a connector particle (དང་། / ཞིང་། / ཅིང་། / ནས། / ལས། /
  སྟེ། / ཏེ།) that grammatically requires continuation. Real issue if the next
  block is the grammatical continuation. False positive if this is a closing verse
  pāda or a deliberate short citation frame.

OBJECTION_REPLY_FUSED
  The block contains both an objection marker (ཅེ་ན། / ཞེ་ན། / སྙམ་ན།) and a reply
  opener (འོ་ན།). These should always be two separate blocks. Almost always a
  real issue.

OVER_LENGTH
  The block exceeds the syllable threshold. Not always wrong — check whether a
  topic boundary (terminal particle སོ། །/འོ། །/ནོ། །/དོ། །  followed by a new
  ordinal opener) is buried mid-block.

SHORT_FRAGMENT
  The block is suspiciously short — may be a stray split artifact that should be
  merged with an adjacent block.

━━━ CORRECTION OPERATIONS ━━━

[
  {"op": "merge", "blocks": [N, M]},
  {"op": "merge", "blocks": [N, M, P]},
  {"op": "split", "block": N, "after": "<verbatim unique substring ending at split point>"},
  {"op": "split", "block": N, "after": ["<sub1>", "<sub2>"]}
]

Rules:
- Only output corrections for REAL issues. Skip false positives entirely.
- Block numbers are CONTINUOUS and include heading blocks. Only merge blocks with
  consecutive numbers (N and N+1); never merge across a heading or skip a number.
- "after" must be verbatim from the block and unique within it. To break one long
  block into 3+ units, set "after" to a LIST of substrings in document order.
- Each block number appears in AT MOST ONE operation.
- Heading blocks (lines starting with #) are NEVER touched.
- If no corrections are needed, output: []
- Output ONLY the JSON array. No commentary, no code fences.
"""

QC_USER_PROMPT_TEMPLATE = """\
The deterministic checker found the following issues in a Tibetan commentary \
resegmentation. Review each flagged block in context and output correction \
operations for real issues only.

--- ISSUES ---
{issues_text}

--- FLAGGED BLOCKS WITH CONTEXT ---
{flagged_text}
"""

# ── shared utilities ──────────────────────────────────────────────────────────

FRONTMATTER_RE = re.compile(r'^---[ \t]*\r?\n.*?\r?\n---[ \t]*\r?\n', re.DOTALL)


def parse_file(path: Path):
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
    return re.sub(r'\s+', '', text)


def _normalize_tsheg(text: str) -> str:
    """Map the non-breaking tsheg (U+0F0C ༌) to the normal tsheg (U+0F0B ་)
    so regex and length checks match consistently across both forms."""
    return text.replace('༌', '་')


def count_syllables(block: str) -> int:
    """Rough syllable count: number of tsheg characters + 1."""
    return _normalize_tsheg(block).count('་') + 1


# ── deterministic checks ──────────────────────────────────────────────────────

_CONNECTOR_RE = re.compile(r'(དང་|ཞིང་|ཅིང་|ནས|ལས|སྟེ|ཏེ)།\s*$')
_OBJECTION_RE = re.compile(r'(ཅེ་ན|ཞེ་ན|སྙམ་ན)།')
_REPLY_RE     = re.compile(r'འོ་ན')


def run_deterministic_checks(blocks, over_length=OVER_LENGTH_THRESHOLD,
                             short_min=SHORT_FRAGMENT_MIN):
    """
    Scan every block and return a list of issue dicts:
      {block_n (1-based), flag, text, syllables (optional)}
    """
    issues = []
    for i, block in enumerate(blocks):
        if is_heading(block):
            continue
        bn = i + 1
        nblock = _normalize_tsheg(block)

        if _CONNECTOR_RE.search(nblock):
            issues.append({"block_n": bn, "flag": "CONNECTOR_ENDING", "text": block})

        if _OBJECTION_RE.search(nblock) and _REPLY_RE.search(nblock):
            issues.append({"block_n": bn, "flag": "OBJECTION_REPLY_FUSED", "text": block})

        syls = count_syllables(block)
        if syls > over_length:
            issues.append({"block_n": bn, "flag": "OVER_LENGTH",
                           "syllables": syls, "text": block})

        if syls < short_min:
            issues.append({"block_n": bn, "flag": "SHORT_FRAGMENT",
                           "syllables": syls, "text": block})

    return issues


def format_issues_list(issues):
    """Format issues as a plain list for the LLM prompt."""
    lines = []
    for item in issues:
        bn   = item["block_n"]
        flag = item["flag"]
        extra = f" ({item['syllables']} syllables)" if "syllables" in item else ""
        preview = item["text"][:80].replace("\n", " ")
        lines.append(f"- Block {bn} — {flag}{extra}: {preview}…")
    return "\n".join(lines)


def format_flagged_context(issues, blocks):
    """Format each flagged block with surrounding context for the LLM prompt."""
    total = len(blocks)
    parts = []
    seen  = set()

    for item in issues:
        bn = item["block_n"]
        if bn in seen:
            continue
        seen.add(bn)

        flag  = item["flag"]
        extra = f" ({item.get('syllables','?')} syllables)" if "syllables" in item else ""
        ctx_start = max(0, bn - 1 - CONTEXT_WINDOW)
        ctx_end   = min(total, bn - 1 + CONTEXT_WINDOW + 1)

        block_lines = []
        for j in range(ctx_start, ctx_end):
            gn    = j + 1
            label = f"[Block {gn}]"
            if gn == bn:
                label = f"[Block {gn} — {flag}{extra}]"
            if is_heading(blocks[j]):
                label += " [HEADING]"
            block_lines.append(f"{label}\n{blocks[j]}")

        parts.append("\n\n".join(block_lines))

    sep = "\n\n" + "─" * 50 + "\n\n"
    return sep.join(parts)


# ── Gemini API ────────────────────────────────────────────────────────────────

def get_client():
    try:
        from google import genai  # noqa: PLC0415
    except ImportError:
        sys.exit("Error: google-genai not installed. Run: pip install google-genai")
    api_key = os.environ.get("GEMINI_API_KEY") or os.environ.get("GOOGLE_API_KEY")
    if not api_key:
        sys.exit("Error: set GEMINI_API_KEY environment variable.")
    return genai.Client(api_key=api_key)


def _is_overloaded(err) -> bool:
    s = str(err).upper()
    return any(t in s for t in ("503","UNAVAILABLE","OVERLOADED","429","RESOURCE_EXHAUSTED"))


def _generate(client, model, user_prompt, fallback_model="", label="qc"):
    try:
        from google.genai import types  # noqa: PLC0415
    except ImportError:
        sys.exit("Error: google-genai not installed.")
    config = types.GenerateContentConfig(
        system_instruction=QC_SYSTEM_PROMPT,
        temperature=0.0,
        thinking_config=types.ThinkingConfig(thinking_budget=0),
    )
    models_to_try = [model]
    if fallback_model and fallback_model != model:
        models_to_try.append(fallback_model)

    last_err = None
    for mi, mdl in enumerate(models_to_try):
        if mi > 0:
            print(f"  -> '{model}' overloaded; falling back to '{mdl}'", file=sys.stderr)
        for attempt in range(1, MAX_RETRIES + 1):
            try:
                resp = client.models.generate_content(
                    model=mdl, contents=user_prompt, config=config)
                return (resp.text or "").strip()
            except Exception as e:  # noqa: BLE001
                last_err = e
                if attempt < MAX_RETRIES:
                    base = min(RETRY_BACKOFF_BASE * (2 ** (attempt - 1)), MAX_BACKOFF)
                    wait = base + random.uniform(0, base * 0.25)
                    kind = "overloaded" if _is_overloaded(e) else "error"
                    print(f"  ! {label} attempt {attempt}/{MAX_RETRIES} {kind}: {e}; "
                          f"retrying in {wait:.0f}s...", file=sys.stderr)
                    time.sleep(wait)
        if not _is_overloaded(last_err):
            break
    raise RuntimeError(f"Gemini QC call failed: {last_err}")


def call_llm_repair(client, model, issues, blocks, fallback_model=""):
    """Send issues list + flagged blocks to LLM; return parsed correction operations."""
    issues_text  = format_issues_list(issues)
    flagged_text = format_flagged_context(issues, blocks)
    user_prompt  = QC_USER_PROMPT_TEMPLATE.format(
        issues_text=issues_text,
        flagged_text=flagged_text,
    )
    raw = _generate(client, model, user_prompt,
                    fallback_model=fallback_model, label="qc-repair")
    raw = re.sub(r'^```(?:json)?\s*', '', raw.strip())
    raw = re.sub(r'\s*```$',          '', raw.strip())
    try:
        ops = json.loads(raw)
        if not isinstance(ops, list):
            print("  ! QC LLM returned non-list JSON — treating as []", file=sys.stderr)
            return []
        return ops
    except json.JSONDecodeError as e:
        print(f"  ! QC LLM JSON parse error ({e}) — treating as []", file=sys.stderr)
        return []


# ── validate + apply (mirrors resegment.py) ───────────────────────────────────

def validate_corrections(ops, blocks):
    total   = len(blocks)
    claimed: dict = {}
    errors  = []
    valid   = []

    for op in ops:
        if op["op"] == "merge":
            bns = sorted(op.get("blocks", []))
            if len(bns) < 2:
                errors.append(f"merge {bns}: need ≥2 blocks"); continue
            ok = all(bns[i+1] == bns[i]+1 for i in range(len(bns)-1))
            if not ok:
                errors.append(f"merge {bns}: not consecutive"); continue
            heading_hit = [b for b in bns if 1 <= b <= total and is_heading(blocks[b-1])]
            if heading_hit:
                errors.append(f"merge {bns}: heading block(s) {heading_hit} — skipped"); continue
            conflict = [b for b in bns if b in claimed]
            if conflict:
                errors.append(f"merge {bns}: block(s) {conflict} already claimed — skipped"); continue
            for b in bns:
                claimed[b] = op
            valid.append({**op, "blocks": bns})

        elif op["op"] == "split":
            bn    = op.get("block")
            after = op.get("after", "")
            if not bn:
                errors.append("split: missing 'block'"); continue
            afters = after if isinstance(after, list) else [after]
            if not afters or any(not a for a in afters):
                errors.append(f"split block {bn}: missing/empty 'after'"); continue
            if 1 <= bn <= total and is_heading(blocks[bn-1]):
                errors.append(f"split block {bn}: is heading — skipped"); continue
            if bn in claimed:
                errors.append(f"split block {bn}: already claimed — skipped"); continue
            claimed[bn] = op
            valid.append(op)

        else:
            errors.append(f"unknown op '{op.get('op')}' — skipped")

    return valid, errors


def apply_corrections(blocks, ops):
    block_to_op: dict = {}
    for op in ops:
        if op["op"] == "merge":
            for bn in op["blocks"]:
                block_to_op[bn] = op
        elif op["op"] == "split":
            block_to_op[op["block"]] = op

    new_blocks = []
    i = 0
    while i < len(blocks):
        bn = i + 1
        if bn not in block_to_op:
            new_blocks.append(blocks[i]); i += 1; continue
        op = block_to_op[bn]
        if op["op"] == "merge":
            if op["blocks"][0] == bn:
                new_blocks.append("\n".join(blocks[b-1] for b in op["blocks"]))
                i += len(op["blocks"])
            else:
                i += 1
        elif op["op"] == "split":
            text     = blocks[i]
            after    = op["after"]
            cut_strs = after if isinstance(after, list) else [after]
            cut_positions = []
            ok = True
            for a in cut_strs:
                occ = text.count(a)
                if occ == 0:
                    print(f"  ! QC split block {bn}: substring not found: {a!r}; "
                          f"keeping whole", file=sys.stderr)
                    ok = False; break
                if occ > 1:
                    print(f"  ! QC split block {bn}: substring not unique "
                          f"({occ} occurrences): {a!r}; keeping whole", file=sys.stderr)
                    ok = False; break
                cut_positions.append(text.find(a) + len(a))
            if not ok:
                new_blocks.append(text)
            else:
                parts = []
                prev = 0
                for pos in sorted(set(cut_positions)):
                    seg = text[prev:pos].strip()
                    if seg: parts.append(seg)
                    prev = pos
                tail = text[prev:].strip()
                if tail: parts.append(tail)
                new_blocks.extend(parts if parts else [text])
            i += 1

    return new_blocks


def check_integrity(input_path: Path, frontmatter: str, new_blocks: list):
    original  = input_path.read_text(encoding="utf-8")
    result    = frontmatter + "\n\n".join(new_blocks)
    orig_sq   = squeeze(original)
    result_sq = squeeze(result)
    if orig_sq == result_sq:
        return True, "OK"
    for i, (a, b) in enumerate(zip(orig_sq, result_sq)):
        if a != b:
            ctx_o = orig_sq[max(0,i-30):i+30]
            ctx_r = result_sq[max(0,i-30):i+30]
            return False, (f"Difference at char {i}:\n"
                           f"  original: ...{ctx_o!r}...\n"
                           f"  result:   ...{ctx_r!r}...")
    return False, f"Length mismatch: {len(orig_sq)} vs {len(result_sq)}"


# ── QC report ─────────────────────────────────────────────────────────────────

def write_qc_report(report_path: Path, commentary_id: str, model: str,
                    issues_before, issues_after, corrections_applied,
                    correction_errors, repaired: bool,
                    blocks_before, blocks_after):

    def preview(text, n=100):
        return text.replace("\n", " ")[:n] + ("…" if len(text) > n else "")

    def issue_list(items):
        if not items:
            return "- (none)\n"
        lines = []
        for item in items:
            bn   = item["block_n"]
            flag = item["flag"]
            extra = f" ({item['syllables']} syllables)" if "syllables" in item else ""
            lines.append(f"- Block {bn} — **{flag}**{extra}  "
                         f"`{preview(item['text'], 120)}`")
        return "\n".join(lines) + "\n"

    fm = (
        "---\n"
        f"source: {commentary_id}\n"
        "skill: block-resegmentation\n"
        "stage: qc\n"
        f"date: {date.today().isoformat()}\n"
        f"model: {model}\n"
        f"repaired: {str(repaired).lower()}\n"
        f"flags_before: {len(issues_before)}\n"
        f"flags_after: {len(issues_after)}\n"
        f"blocks_before: {len(blocks_before)}\n"
        f"blocks_after: {len(blocks_after)}\n"
        "---\n\n"
    )

    body = f"# Block QC Report — {commentary_id}\n\n"

    body += f"## Flags found{'  (before repair)' if repaired else ''}\n\n"
    body += issue_list(issues_before)

    if repaired:
        body += "\n## Corrections applied\n\n"
        if corrections_applied:
            for op in corrections_applied:
                if op["op"] == "merge":
                    body += f"- **MERGE** blocks {op['blocks']}\n"
                else:
                    body += f"- **SPLIT** block {op['block']}  after: `{op['after']}`\n"
        else:
            body += "- (none applied)\n"

        body += "\n## Flags remaining after repair\n\n"
        body += issue_list(issues_after)

    if correction_errors:
        body += "\n## Correction errors (skipped)\n\n"
        for e in correction_errors:
            body += f"- {e}\n"

    report_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.write_text(fm + body, encoding="utf-8")


# ── main ──────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(
        description="QC pass for block-resegmented Tibetan commentaries.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument("input_file",
                        help="Resegmented commentary file (.reseg.md)")
    parser.add_argument("--commentary-id", default="",
                        help="Short ID (inferred from filename if omitted)")
    parser.add_argument("--no-fix", action="store_true",
                        help="Run detection only; skip LLM repair")
    parser.add_argument("--dry-run", action="store_true",
                        help="Compute corrections but do not write any files")
    parser.add_argument("--model", default=DEFAULT_MODEL)
    parser.add_argument("--fallback-model", default=DEFAULT_FALLBACK_MODEL)
    parser.add_argument("--over-length", type=int, default=OVER_LENGTH_THRESHOLD,
                        help=f"Syllable threshold for OVER_LENGTH (default: {OVER_LENGTH_THRESHOLD})")
    args = parser.parse_args()

    input_path = Path(args.input_file)
    if not input_path.exists():
        sys.exit(f"Error: file not found: {input_path}")

    cid = args.commentary_id or re.sub(r'\.reseg$', '', input_path.stem)
    report_path = input_path.parent / f"{cid}.qc.md"

    print(f"Input:  {input_path}")
    print(f"ID:     {cid}")
    print()

    # ── parse ──
    frontmatter, blocks = parse_file(input_path)
    print(f"Blocks: {len(blocks)}")

    # ── Step 1: deterministic check ──
    print("\nStep 1 — Deterministic checks...")
    issues_before = run_deterministic_checks(blocks,
                                             over_length=args.over_length)
    print(f"  {len(issues_before)} flag(s) found.")
    for item in issues_before:
        extra = f" ({item.get('syllables','?')} syl)" if "syllables" in item else ""
        print(f"  Block {item['block_n']} — {item['flag']}{extra}")

    repaired           = False
    issues_after       = issues_before
    corrections_applied = []
    correction_errors  = []
    blocks_after       = blocks

    # ── Step 2: LLM repair ──
    if issues_before and not args.no_fix:
        print("\nStep 2 — LLM repair...")
        client   = get_client()
        raw_ops  = call_llm_repair(client, args.model, issues_before, blocks,
                                   args.fallback_model)
        print(f"  LLM suggested {len(raw_ops)} correction(s):")
        for op in raw_ops:
            if op["op"] == "merge":
                print(f"    MERGE {op['blocks']}")
            else:
                print(f"    SPLIT block {op.get('block')} after: "
                      f"{op.get('after','')[:50]!r}")

        valid_ops, correction_errors = validate_corrections(raw_ops, blocks)
        if correction_errors:
            print(f"  Validation errors ({len(correction_errors)}):")
            for e in correction_errors:
                print(f"    - {e}")

        if valid_ops:
            new_blocks = apply_corrections(blocks, valid_ops)

            ok, detail = check_integrity(input_path, frontmatter, new_blocks)
            if not ok:
                print(f"\n  ✗ Integrity check FAILED: {detail}")
                print("  File NOT updated.")
                sys.exit(1)
            print(f"  ✓ Integrity check passed. "
                  f"Blocks: {len(blocks)} → {len(new_blocks)}")

            # ── Step 3: re-check after repair ──
            print("\nStep 3 — Re-checking after repair...")
            issues_after = run_deterministic_checks(new_blocks,
                                                    over_length=args.over_length)
            print(f"  {len(issues_after)} flag(s) remain after repair.")

            if not args.dry_run:
                output_text = frontmatter + "\n\n".join(new_blocks) + "\n"
                input_path.write_text(output_text, encoding="utf-8")
                print(f"  Updated: {input_path}")

            corrections_applied = valid_ops
            blocks_after        = new_blocks
            repaired            = True

    elif issues_before and args.no_fix:
        print("\n--no-fix: skipping LLM repair.")

    else:
        print("\n✓ No issues found — no repair needed.")

    # ── Step 4: write report ──
    if not args.dry_run:
        write_qc_report(report_path, cid, args.model,
                        issues_before, issues_after,
                        corrections_applied, correction_errors,
                        repaired, blocks, blocks_after)
        print(f"\nQC report: {report_path}")
    else:
        print("\n--dry-run: report not written.")

    # summary
    print(f"\n{'─'*40}")
    print(f"Flags before : {len(issues_before)}")
    if repaired:
        print(f"Flags after  : {len(issues_after)}")
        print(f"Corrections  : {len(corrections_applied)}")


if __name__ == "__main__":
    main()
