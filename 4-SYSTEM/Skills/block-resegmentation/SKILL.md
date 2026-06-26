---
name: block-resegmentation
description: >
  Re-draw block boundaries in a Stage-1 segmented Tibetan commentary to produce
  semantically coherent, citation-sized units. Use after commentary-segmentation
  (Stage 1) and after the TOC-inclusion step. The LLM flags merge/split operations;
  a Python script applies them and verifies text integrity. No character is added,
  removed, or reordered — only blank-line boundaries change.

  Trigger this skill when the user says things like:
  "run meaningful segmentation", "re-segment the commentary", "fix the block
  boundaries", "merge and split blocks semantically", or "run block-resegmentation".
---

# block-resegmentation

**Role:** Expert editor in classical Tibetan Buddhist commentary (འགྲེལ་པ་) structure.

**Task:** Identify which adjacent blocks should be merged into one thought unit and
which single blocks should be split at a topic boundary — then apply those operations
via script, preserving every character of the source.

---

## Pipeline position

```
commentary-segmentation Stage 1     ← rule-based boundary detection
         ↓
[TOC inclusion by friend]           ← headings inserted into segmented file
         ↓
block-resegmentation                ← THIS SKILL: semantic merge/split
```

**Input:** a Stage-1 segmented file with TOC headings embedded, in `0-INBOX/segmented/`
or wherever the TOC step wrote its output.

**Do not run** on a file that has block IDs already. Do not run before TOC headings
are included (the headings give the LLM section context).

---

## What good output looks like

- **One block = one citable thought.** A downstream rail file should be able to cite
  exactly the span it needs — no more, no less.
- **Verse stanzas are whole.** A 4-pāda stanza is one block. Never merge two
  independent stanzas; never leave half a stanza as a block.
- **Enumerations are complete.** An enumeration head plus all its items form one block
  (unless individual items are long enough to cite independently).
- **Lead-ins stay with their content.** A transition phrase like `བོད་སྐད་དུ།` is in
  the same block as the text it introduces.
- **Objections and replies are separate.** `ཅེ་ན།`/`ཞེ་ན།` block and `འོ་ན།` block are
  always two blocks.
- **Source attributions are separate.** A `…ལས།` attribution line is its own block;
  the quoted passage is its own block; the closing `ཞེས་སོ། །` is its own block.
- **Headings are untouched.** Markdown heading lines (`#`, `##`, `###`, …) pass
  through unchanged and are never part of a merge or split operation.

---

## Architecture — LLM flags, script applies

```
[Phase 1]  Script chunks the file into overlapping block windows
[Phase 2]  LLM reads each window, outputs a JSON operation list
           {"op": "merge", "blocks": [3, 4]}
           {"op": "split", "block": 7, "after": "<unique substring>"}
[Phase 3]  Script combines windows, deduplicates overlap zone, applies ops
[Phase 4]  Script runs squeeze(input) == squeeze(output); aborts on mismatch
[Phase 5]  QC pass — deterministic checks + optional LLM correction
[Phase 6]  Human reviews ops log + QC report; approves output
```

The LLM **never retypes Tibetan**. It only points at block numbers and verbatim
substrings. All text manipulation is done by the script.

---

## Scripts

Two scripts bundled in `scripts/`:

| Script | Purpose |
|---|---|
| `resegment.py` | Main resegmentation: chunk → LLM flag → apply → integrity check |
| `qc_check.py` | QC pass: deterministic checks → optional LLM correction → integrity check |

---

### `resegment.py`

```
python3 4-SYSTEM/Skills/block-resegmentation/scripts/resegment.py \
    "0-INBOX/segmented/<file>.md" \
    --commentary-id <id>
```

**Setup:** `pip install google-genai` and set `GEMINI_API_KEY` in the environment.

**Key flags:**

| Flag | Default | Purpose |
|---|---|---|
| `--commentary-id` | inferred from filename | Short ID for output filenames and staging folder |
| `--window-size` | 40 | Blocks per LLM call |
| `--overlap` | 5 | Overlap blocks between adjacent windows |
| `--model` | `gemini-2.5-flash-preview-05-20` | Gemini model to use |
| `--fallback-model` | `gemini-2.0-flash` | Fallback if primary is overloaded |
| `--force` | off | Reprocess all windows even if staging files exist |
| `--apply-only` | off | Skip LLM calls; apply already-staged operations |
| `--dry-run` | off | Run integrity check only; write nothing |

**Outputs:**

| File | Purpose |
|---|---|
| `0-INBOX/resegmented/<id>.reseg.md` | Resegmented commentary |
| `0-INBOX/resegmented/<id>.ops.md` | Human-readable operations log |
| `0-INBOX/temp/RESEG-<id>/windows/window-NNNN.json` | Per-window staging (resumable) |

---

### `qc_check.py`

Mirrors the QC pattern in `toc_tree_extractor`: detect → repair → re-check → report.
By default all four steps run automatically. Run after `resegment.py`.

```
python3 4-SYSTEM/Skills/block-resegmentation/scripts/qc_check.py \
    "0-INBOX/resegmented/<id>.reseg.md"
```

Use `--no-fix` to run detection only (no LLM repair):

```
python3 4-SYSTEM/Skills/block-resegmentation/scripts/qc_check.py \
    "0-INBOX/resegmented/<id>.reseg.md" --no-fix
```

**Steps:**

1. **Deterministic check** — scans every block for known violations; no API call.
2. **LLM repair** — sends the issues list + flagged blocks with context to Gemini,
   which outputs correction operations. Script applies them; integrity is verified.
3. **Re-check** — runs the deterministic checks again on the repaired output.
4. **Report** — written with `flags_before`, corrections applied, `flags_after`.

**What the deterministic checker flags:**

| Flag | Condition |
|---|---|
| `CONNECTOR_ENDING` | Block ends with `དང་།` / `ཞིང་།` / `ཅིང་།` / `ནས།` / `ལས།` / `སྟེ།` / `ཏེ།` — sentence incomplete |
| `OBJECTION_REPLY_FUSED` | Block contains both `ཅེ་ན།`/`ཞེ་ན།` and `འོ་ན།` — should be two blocks |
| `OVER_LENGTH` | Block exceeds 60 syllables — may contain a buried topic boundary |
| `SHORT_FRAGMENT` | Block is under 4 syllables — may be a split artifact |

**Outputs:**

| File | Purpose |
|---|---|
| `0-INBOX/resegmented/<id>.qc.md` | QC report with `flags_before` / `flags_after` |
| `.reseg.md` updated in place | (only when real issues found and `--no-fix` not set) |

**Key flags:**

| Flag | Default | Purpose |
|---|---|---|
| `--no-fix` | off | Detection only; skip LLM repair |
| `--over-length` | 60 | Syllable threshold for OVER_LENGTH flag |
| `--dry-run` | off | Compute corrections but write nothing |
| `--model` | `gemini-2.5-flash-preview-05-20` | Gemini model |
| `--fallback-model` | `gemini-2.0-flash` | Fallback model |

---

## How the LLM decides

### MERGE — adjacent blocks that form one thought

**M1 — Incomplete sentence.** A block ends with a connector particle that
grammatically requires continuation in the next block:
`དང་།` / `ཞིང་།` / `ཅིང་།` / `ནས།` / `ལས།` / `སྟེ།` / `ཏེ།`

**M2 — Broken verse stanza.** A standard stanza has 4 pādas (~7–9 syllables each,
ending with `།`). If a block has only 1–2 pādas and the stanza continues into the
next block, merge all pādas of the stanza. Never merge two independent stanzas.

**M3 — Lead-in orphaned from content.** A block ends with a transition phrase
(`བོད་སྐད་དུ།` / `འདི་ལྟར།` / topic-opener `དེ་ལ།`) that introduces the next block.
Merge the lead-in with the block it introduces.

**M4 — Incomplete enumeration.** A block opens an enumeration (`གཉིས་ཏེ།` /
`གསུམ་སྟེ།` / `བཞི་ལས།` etc.) and the remaining items continue in the next block.
Merge until the enumeration is complete.

### SPLIT — one block that spans two thoughts

**S1 — Objection + reply.** A block contains both an objection marker
(`ཅེ་ན།` / `ཞེ་ན།` / `སྙམ་ན།`) and a reply opener (`འོ་ན།`). Split between them.

**S2 — Terminal particle + new topic.** A block has a sentence-final marker
(`སོ། །` / `འོ། །` / `ནོ། །` / `དོ། །`) mid-block followed immediately by a new
ordinal opener (`དང་པོ་` / `གཉིས་པ་` / `གསུམ་པ་`) or a new subject. Split after
the terminal particle.

**S3 — Source attribution fused to quote.** A block opens with a source attribution
(`…ལས།` or `…གསུངས།`) fused directly to the quoted passage. Split after the
attribution so it stands alone.

---

## Procedure

**Step 1 — Resegment**

Confirm the input file has TOC headings embedded and no block IDs yet. Then run:

```
python3 4-SYSTEM/Skills/block-resegmentation/scripts/resegment.py \
    "0-INBOX/segmented/<file>.md" \
    --commentary-id <id>
```

The script processes all windows (resumable — re-run after interruption without
`--force` to pick up where it stopped). On completion it prints: block count
before → after, operations applied, any conflicts in the overlap zone, and the
integrity check result.

- If integrity check fails (`✗`): the output file is **not written**. Read the
  error, fix the staging JSON if needed, re-run with `--apply-only`.
- If overlap-zone conflicts are listed: edit the relevant `window-NNNN.json`
  staging file, then re-run with `--apply-only`.

**Step 2 — QC**

```
python3 4-SYSTEM/Skills/block-resegmentation/scripts/qc_check.py \
    "0-INBOX/resegmented/<id>.reseg.md"
```

Runs all four steps automatically: detect → LLM repair → re-check → write report.
The `.reseg.md` file is updated in place if real issues are found.
Review `0-INBOX/resegmented/<id>.qc.md` for the `flags_before` / `flags_after` summary.

To run detection only without repair: add `--no-fix`.

**Step 3 — Human review**

Review `0-INBOX/resegmented/<id>.ops.md` (main operations) and
`0-INBOX/resegmented/<id>.qc.md` (QC corrections). On approval the file is ready.

---

## Rules

- **No character changes.** The script enforces `squeeze(input) == squeeze(output)`.
  If this assertion fails, the output is not written.
- **Headings are never touched.** A block starting with `#` is always KEEP.
- **Output stays in `0-INBOX/`** until a domain specialist approves.
- **When in doubt, under-merge rather than over-merge.** A slightly fragmented block
  is safer than a wrongly merged one that spans two citable ideas.
