---
name: commentary-resegment
description: >
  Re-paragraph a Tibetan commentary that has ONE CLAUSE PER LINE into readable
  sense-unit paragraphs. An LLM (Gemini) reads each section and decides, BY MEANING
  (content and context — NOT grammar rules or particles), which adjacent lines form
  one paragraph (about 2–4 lines); a Python script joins each group onto a single
  line, separates paragraphs with a blank line, and verifies the source text is
  byte-identical. The source is read-only ground truth: only newlines and spaces are
  added or removed — no word or character is altered, reordered, added, or deleted.

  Use when the input is a one-clause-per-line commentary (e.g. *_segmented.md,
  *.toc.md) that needs to be grouped into meaningful paragraphs.

  Trigger when the user says things like: "re-paragraph the commentary",
  "group the clause lines into meaningful paragraphs", "resegment by sense",
  or "run commentary-resegment".
---

# commentary-resegment

**Role:** Expert editor of classical Tibetan Buddhist commentary (འགྲེལ་པ་).

**Task:** Group a one-clause-per-line commentary into short, coherent paragraphs —
**by meaning, decided by the LLM**, not by hard grammar rules — while changing not one
word or character of the source.

---

## What changed from the old skill

This replaces the earlier rule-based `block-resegmentation-linewise`. The old version
merged lines only when a **grammatical signal** fired (connector particles
`དང་།/ཤིང་།/སྟེ།`, verse-stanza shape, enumeration heads). That was rejected as too
mechanical. The new version lets the **LLM judge sense units from content and context**,
targeting paragraphs of about 2–4 lines. The plumbing (windowing, staging, validation,
apply, integrity gate) is unchanged.

---

## The model

```
unit            = one non-blank, non-heading line (atomic; never altered)
default state   = every unit is its own paragraph
GROUP n..m      = lines n..m form ONE paragraph, joined onto a single line
headings        = pass through untouched, framed by blank lines
output          = paragraphs separated by exactly one blank line
```

The LLM only points at line numbers (`{"op":"merge","lines":[14,15,16]}`); the script
does all text handling. Lines the LLM does not group default to their own paragraph.

---

## Integrity rule — pure whitespace-only

The source is read-only ground truth. The only edits are added/removed newlines and
spaces (no `>` or other markers are introduced). The gate is therefore exact:

```
strip_all_whitespace(source) == strip_all_whitespace(output)
```

If the two character streams differ, the output is **not written**.

---

## How the LLM decides (content-based, not rules)

For each section the model reads the lines **and their context** and groups adjacent
lines into one paragraph when they form a single sense unit — one idea, one narrative
beat, one objection-and-reply exchange. It starts a new paragraph when the topic, the
actor, or the move in the argument shifts. Target length is about **2–4 lines**, leaning
shorter when unsure. There are no particle/verse/enumeration rules.

Mechanical guardrails the script still enforces (not judgments about the text): a group's
lines must be consecutive, must not cross a heading, and no line is used twice.

---

## Architecture

```
[Phase 1]  Number lines; slice into sections on TOC headings. A file with no headings is
           cut into windows of <= --window-lines lines at sentence-final particles, so no
           sense unit is split across a window boundary.
[Phase 2]  LLM returns paragraph groups by line number for each window.
[Phase 3]  Script validates (consecutive, no heading crossed, no overlap) and joins each
           group onto one line; uncovered lines become their own paragraph.
[Phase 4]  Integrity gate (whitespace-only). On mismatch, nothing is written.
```

---

## Script — `resegment.py`

```
# one file:
python3 4-SYSTEM/Skills/commentary-resegment/scripts/resegment.py \
    "1-SOURCES/commentaries/Raw/BCAC14_GDR_bo.toc.md" --commentary-id BCAC14_GDR_bo
```

**Setup:** `pip install google-genai`; key from `GEMINI_API_KEY` env **or** repo-root
`.env` (read automatically).

| Flag | Default | Purpose |
|---|---|---|
| `--commentary-id` | filename stem | Output id |
| `--window-lines` | 60 | Max content lines per LLM window (paragraph granularity) |
| `--model` | `gemini-2.5-flash` | Gemini model |
| `--fallback-model` | `gemini-2.0-flash` | Fallback if overloaded |
| `--force` | off | Reprocess all windows even if staged |
| `--apply-only` | off | Skip LLM calls; apply staged decisions |
| `--dry-run` | off | Integrity check only; write nothing |

**Outputs:**

| File | Purpose |
|---|---|
| `0-INBOX/resegmented/<id>.reseg.md` | Re-paragraphed commentary (one line per paragraph) |
| `0-INBOX/resegmented/<id>.ops.md` | Log of paragraph groups applied |
| `0-INBOX/temp/RESEG-<id>/windows/window-NNNN.json` | Per-window staging (resumable) |

Resumable (re-run skips staged windows); `--apply-only` re-applies staged decisions
without new LLM calls.

---

## Procedure

1. **Pilot one file**, then read `0-INBOX/resegmented/<id>.reseg.md`. Confirm
   `✓ Integrity check passed`.
2. **Tune** `--window-lines` if paragraphs feel too long/short.
3. **Repeat** for the other files (loop over the folder in your shell).

---

## Rules

- **No text changes.** The whitespace-only integrity gate must pass or nothing is written.
- **Only whitespace is added/removed.** No `>`, `#`, or other characters are introduced.
- **Headings untouched; paragraphs never cross a heading.**
- **Output goes to `0-INBOX/resegmented/`**, leaving the read-only source intact.
- **Judgment, not rules.** Grouping is interpretive (content/context), so paragraph
  breaks are not perfectly identical across runs.
