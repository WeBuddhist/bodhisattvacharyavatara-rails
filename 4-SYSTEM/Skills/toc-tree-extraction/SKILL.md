---
name: toc-tree-extraction
description: >
  Build a full nested, decimal-numbered ས་བཅད (sa bcad) table-of-contents TREE from a
  Tibetan Buddhist commentary — the complete pipeline, not just candidates. Use this skill
  whenever the user wants the WHOLE structural outline reconstructed: "build the sa bcad
  tree", "extract the TOC tree", "make the dkar chag / dkar-chag", "reconstruct the outline
  hierarchy", or "give me the nested table of contents" for a Tibetan commentary or root
  text. This is the Claude-native equivalent of the bundled extract_toc_tree.py (which uses
  the Gemini API): each of the four inference passes — (1) section candidates, (2) verbatim
  enumeration blocks, (3) nested decimal tree, (4) QC repair — runs as an ISOLATED subagent
  with only its own prompt, mirroring the separate Gemini calls; two bundled Python helpers
  do the deterministic chunking and tree QC. For candidate-only extraction without building a
  tree, use toc-candidate-extraction instead.
---

# ས་བཅད TOC Tree Extraction (Claude-native)

This skill reconstructs the **full hierarchical table of contents** (དཀར་ཆག / *dkar chag*)
of a Tibetan commentary as a single nested, decimal-numbered tree. It is the Claude-native
port of `4-SYSTEM/Scripts/toc_tree_extractor/extract_toc_tree.py`.

## Why this is an orchestrator, not one big prompt — READ THIS FIRST

The Gemini script's precision comes from **task isolation**: each pass is a *separate API
call* with only that one task's system prompt and only the relevant input. The
candidate-extraction call never sees the tree-building instructions, so it cannot drift into
tree-building; the verbatim-copy call never sees the "interpret and reconcile" instructions,
so it stays literal. Merging the four jobs into one prompt/one context collapses that
isolation and precision drops.

**Therefore you (the orchestrating agent) must NOT perform the four passes yourself in this
context.** Each pass runs as its own **isolated subagent** (via the `Task` tool) whose entire
instruction set is one prompt file under `prompts/` plus its specific input.

**Each subagent reads its input by path and writes its own output file.** Do not paste chunk
text into the subagent prompt and do not funnel results back through your context to write
them yourself — that serialises the writes and bloats your context with every chunk's Tibetan.
Instead, hand each subagent the *paths* of its prompt file and its input, and the *path* it
must write. Distinct output filenames mean parallel subagents never collide. You only: chunk,
dispatch subagents, do the deterministic merge, run the checker, and dispatch the repair
subagent. Do not read the pass prompt files into your own context and do the work inline —
that re-merges what this design deliberately separates.

The four isolated prompts live in:

| File | Pass |
|---|---|
| `prompts/pass1-candidates.md` | section candidates (one subagent per chunk) |
| `prompts/pass2-enumerations.md` | verbatim enumeration blocks (one subagent per chunk) |
| `prompts/pass3-tree.md` | build nested decimal tree (one subagent) |
| `prompts/pass4-qc-repair.md` | repair flagged issues (one subagent per repair round) |

---

## Inputs

| Input | Description |
|---|---|
| `input-file` | Path to the commentary/root-text `.md`, normally under `1-SOURCES/Commentaries/` |
| `commentary-id` | Short id for output filenames (inferred from the filename if obvious) |

If the file path is missing, or the `commentary-id` is not obvious from the filename, **stop
and ask** before doing anything else.

## Outputs (all under `0-INBOX/`)

| File | Stage |
|---|---|
| `0-INBOX/temp/TOC-<id>/candidates/chunk_NNN.md` | per-chunk section candidates (resumable) |
| `0-INBOX/temp/TOC-<id>/enumerations/chunk_NNN.md` | per-chunk verbatim enumeration blocks |
| `0-INBOX/toc-candidates-<id>.md` | merged candidates |
| `0-INBOX/toc-tree-<id>.md` | the final nested decimal TOC tree |
| `0-INBOX/toc-tree-qc-<id>.md` | QC report (issues before / after repair) |

Drafts in `0-INBOX/` — scratch, never cited from `2-RAILS/`. The tree has **no `^toc` block
IDs**; the decimal numbering alone identifies each entry. (Inserting the tree into a
source/rails file with block IDs is a separate step — use `add-toc`.)

---

## Step 0 — Chunk the file (deterministic helper)

```bash
python 4-SYSTEM/Skills/toc-tree-extraction/scripts/chunk_file.py \
  "<input-file>" --chunk-size 150 --overlap 25 \
  --output-dir 0-INBOX/temp/TOC-<id>/chunks
```

The 25-line overlap guarantees every candidate appears in full in at least one chunk.
**Resumability:** before dispatching a pass-1 or pass-2 subagent for a chunk, check whether
its output file already exists and skip if so, so an interrupted run resumes from the first
missing chunk.

---

## Pass 1 — Section candidates · ISOLATED subagent per chunk

For each chunk file (that has no existing result), dispatch a **separate `Task` subagent**.
Give it nothing but the pass-1 prompt and that one chunk:

> Read `4-SYSTEM/Skills/toc-tree-extraction/prompts/pass1-candidates.md` and follow it
> exactly. Apply it to ONLY the chunk below. Return only the candidate blocks (or
> `NO CANDIDATES`). Do not do any other task.
>
> --- BEGIN CHUNK ---
> {chunk_text}
> --- END CHUNK ---

Write the returned text to `0-INBOX/temp/TOC-<id>/candidates/chunk_NNN.md` with a header:

```
<!-- chunk NNN | lines START–END | source: <id> -->

[returned candidate blocks, or: <!-- no candidates --> ]
```

Independent chunks have no dependencies, so you may dispatch several pass-1 subagents in
parallel (one message, multiple `Task` calls).

---

## Pass 2 — Verbatim enumerations · ISOLATED subagent per chunk

Run **separately** over the same chunks — a different isolated subagent, because verbatim
copying must not be contaminated by the interpretive instructions of the other passes.

> Read `4-SYSTEM/Skills/toc-tree-extraction/prompts/pass2-enumerations.md` and follow it
> exactly. Apply it to ONLY the chunk below. Return only the enumeration blocks (or
> `NO ENUMERATIONS`). Copy verbatim; add no interpretation.
>
> --- BEGIN CHUNK ---
> {chunk_text}
> --- END CHUNK ---

Write each result to `0-INBOX/temp/TOC-<id>/enumerations/chunk_NNN.md` (or `NO ENUMERATIONS`).
These may also run in parallel.

---

## Merge (deterministic, done by you)

Concatenate the per-chunk candidate files (keeping their `<!-- chunk NNN -->` headers) into
`0-INBOX/toc-candidates-<id>.md` with frontmatter:

```yaml
---
source: <id>
skill: toc-tree-extraction
stage: candidates
date: <YYYY-MM-DD>
total_candidates: <N>
---
```

Concatenate the non-`NO ENUMERATIONS` enumeration files (in document order) into a single
enumerations text block for the next pass. Merging is mechanical text assembly — fine to do
in this context; it is not an inference task.

---

## Pass 3 — Build the nested decimal tree · ISOLATED subagent

Dispatch ONE subagent with only the pass-3 prompt and the two merged inputs:

> Read `4-SYSTEM/Skills/toc-tree-extraction/prompts/pass3-tree.md` and follow it exactly.
> Build the full nested decimal TOC for commentary "<id>" from the candidates below,
> reconciled against the enumerations. Output only the tree block.
>
> --- BEGIN CANDIDATES ---
> {merged_candidates}
> --- END CANDIDATES ---
>
> --- BEGIN ENUMERATIONS ---
> {merged_enumerations}
> --- END ENUMERATIONS ---

Write the returned tree to `0-INBOX/toc-tree-<id>.md` with `stage: toc-tree` frontmatter.

---

## Pass 4 — Deterministic QC, then ISOLATED repair subagent

First run the bundled checker yourself (NOT by hand — it encodes the exact
numbering/attestation logic and must be identical every run):

```bash
python 4-SYSTEM/Skills/toc-tree-extraction/scripts/qc_check_tree.py \
  0-INBOX/toc-tree-<id>.md \
  --corpus 0-INBOX/toc-candidates-<id>.md 0-INBOX/temp/TOC-<id>/enumerations/*.md \
  --out 0-INBOX/toc-tree-qc-<id>.md
```

It flags indentation errors, Tibetan-ordinal vs decimal mismatch, duplicate decimals, sibling
gaps/dups, titles not attested (possible hallucination), and ordinals not attested for a
title. Exit code = issue count.

If issues remain, dispatch ONE **isolated repair subagent** with only the pass-4 prompt plus
the issue list, tree, and both sources:

> Read `4-SYSTEM/Skills/toc-tree-extraction/prompts/pass4-qc-repair.md` and follow it exactly.
> Correct the tree for commentary "<id>", fixing every listed issue against BOTH the
> enumerations and the candidates. Output only the corrected tree.
>
> --- BEGIN ISSUES ---
> {issues}
> --- END ISSUES ---
> --- BEGIN ENUMERATIONS ---
> {merged_enumerations}
> --- END ENUMERATIONS ---
> --- BEGIN SECTION CANDIDATES ---
> {merged_candidates}
> --- END SECTION CANDIDATES ---
> --- BEGIN TREE ---
> {tree}
> --- END TREE ---

Overwrite `0-INBOX/toc-tree-<id>.md` with the repaired tree, **re-run the checker**, and record
issues-before / issues-after in `0-INBOX/toc-tree-qc-<id>.md`. Iterate (a fresh isolated repair
subagent per round) until the count is 0 or only genuinely-ambiguous issues remain (note those
for the human). Keep the deterministic checker as the gate — never declare the tree clean on a
subagent's say-so.

---

## Execution summary

1. Confirm `input-file` and `commentary-id` (ask if not obvious).
2. `chunk_file.py` → overlapping chunks.
3. Pass 1: one isolated subagent per chunk → `candidates/chunk_NNN.md` (resumable, parallelisable).
4. Pass 2: one isolated subagent per chunk → `enumerations/chunk_NNN.md`.
5. Merge candidates → `0-INBOX/toc-candidates-<id>.md`; assemble enumerations text.
6. Pass 3: one isolated subagent → `0-INBOX/toc-tree-<id>.md`.
7. Pass 4: `qc_check_tree.py` → isolated repair subagent → re-check → `0-INBOX/toc-tree-qc-<id>.md`.
8. Report totals (candidates, enumeration blocks, issues before/after) and the output paths.

**Isolation is the whole point.** If you ever find yourself doing a pass's reasoning in this
orchestrating context instead of in its own subagent, stop and dispatch the subagent — that is
what preserves the per-task precision the Gemini pipeline was built around.

For candidate extraction only (no tree), use `toc-candidate-extraction`. For batch/headless
runs over many commentaries without a Claude session, the Gemini script
`4-SYSTEM/Scripts/toc_tree_extractor/extract_toc_tree.py` does the same pipeline autonomously.
