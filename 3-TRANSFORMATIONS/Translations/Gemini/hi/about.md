---
title: "hi — Gemini zero-shot (hindi)"
track_type: machine-baseline
target_language: hindi
lang_tag: hi
source_language: tibetan
generator: gemini-3.1-pro-preview
endpoint: https://generativelanguage.googleapis.com/v1beta/models/gemini-3.1-pro-preview:generateContent
rails_used: none
termbase: none
status: draft
seeded: 2026-10-07
---

# Gemini/hi — about this track

A **machine baseline**, not a rails-governed translation track.

Every file here is raw output of Google Gemini (model `gemini-3.1-pro-preview`, recorded per
block in the ledger as `model_version`), produced by
`4-SYSTEM/Skills/machine-translate/scripts/gm_translate.py`, which sends a small
batch of adjacent block IDs per call and asks for a JSON object holding one
array of lines per block. Nothing in it passed through `2-RAILS/`: no
verse-context package, no consolidated bilingual glossary, no per-track
`termbase.md`, no human review. It therefore does **not** satisfy the
Translation-track contract in
[`../../About Transformations.md`](../../About%20Transformations.md) §3, and it is
not eligible to be marked `status: complete` or to be cited by any other
transformation.

**Source.** Every block is translated from the Tibetan in `1-SOURCES/Text/`,
which is the closest thing to the original that exists. `translation_of` and the
segment alignment therefore point at the Tibetan text. If a run was given an
existing machine translation as *reference* (`--reference-track`), that fact is
recorded in the frontmatter (`reference_translation`) and on every ledger
record (`reference_used`); the reference was context, not source.

## What it is for

- A first display translation for the app in a language no track covers yet.
- A comparison baseline against which a rails-governed translation can be judged.
- A drafting aid and a source of candidate renderings for
  `2-RAILS/Bilingual-Glossaries/` (via `glossary-extract-raw`).

## What governs it

| File | Role |
| --- | --- |
| `style.md` | The style instruction, sent **verbatim** as the system prompt on every call (followed by the fixed output contract). Edit it, then re-run with `--force` to regenerate. |
| `context-header.md` | A work-NEUTRAL, track-wide preamble prepended to every call. The per-text `Work: …` line is derived from each source's own metadata and appended after it. |
| `work/<text>-hi.jsonl` | Append-only ledger, one per source text: one record per block, holding source, translation, the exact context sent, model version, token usage, line-parity result and timings. The audit trail and the resume point. |
| `<text>-hi.md` | The rendered translation, block-ID aligned to the source. |

## Line parity

The whole point of a block-ID-aligned track is that block `^N` here renders
block `^N` of the Tibetan, line for line. The script checks every block's line
count against its source before recording it; a block that comes back wrong is
re-run alone with the required count stated, and only an exact match is
accepted silently. Anything still divergent is recorded with
`line_parity: false` and listed in the run report for human attention.

Regenerate or extend with:

```bash
python3 4-SYSTEM/Skills/machine-translate/scripts/gm_translate.py \
  --source "1-SOURCES/Text/<text>.md" --lang hindi
python3 4-SYSTEM/Skills/machine-translate/scripts/gm_translate.py \
  --source "1-SOURCES/Text/<text>.md" --lang hindi --headings     # section headings
```

The renderer carries the researched title, backend ids and import provenance
over from the file it overwrites (see `PRESERVE_FM_KEYS` in `dm_translate.py`),
so no separate stamping pass is needed in this vault.
