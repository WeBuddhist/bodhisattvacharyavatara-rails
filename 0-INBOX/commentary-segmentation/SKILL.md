---
name: commentary-segmentation
description: Segment an OCR-clean but under-segmented Tibetan commentary in 1-SOURCES/Commentaries into short, individually-referenceable blocks (prose paragraphs, verse stanzas, quotations) based on the functional content of the text — quotation frames, objection/answer markers, sa-bcad outline enumerations, sentence-final particles, and verse stanza detection. Use when a commentary's text is one continuous run (or has overly long paragraphs) and needs breaking into citation-sized units before block IDs are applied. Runs AFTER format-commentary's OCR cleanup and BEFORE block-ID stamping and verse-context. Does not interpret, translate, or alter a single character of the source.
---

**Role:** Expert editor in classical Tibetan Buddhist commentary (`འགྲེལ་པ་`) structure and Obsidian markdown.

**Task:** Process Tibetan commentaries by structuring the text with specific hierarchical logic — without adding, removing, reordering, or re-spelling any character of the source.

**1. Text Reconstruction**

- **No Deletions:** Strictly preserve the entire source text. Do not omit any analysis or citations.
    
- **Continuous Flow:** Remove arbitrary line numbers within sentences to form smooth, logically grouped text.
    
- **Continuous Flow:** Remove arbitrary line breaks within sentences to form smooth, logically grouped text.

**2. Paragraph & Verse Formatting**

- **Logical Blocks (Granularity):** Break long prose sections into very short, discrete paragraphs (ideally 1–2 sentences). Blocks must be kept short to ensure they are highly optimized for referencing. If a paragraph exceeds 3-4 lines of Tibetan text, you must find a logical break point to split it.
    
- **Verses (ཚིགས་བཅད):** Count and separate blocks by each independent stanza. An independent stanza is defined by its context. Keep verse lines together within a single stanza, but do not group multiple independent stanzas into the same block.
    
- **Quotes (ལུང་འདྲེན):** Place source references (e.g., སྡུད་པ་ལས།) on their own separate line above the quote. Place concluding remarks (e.g., ཞེས་སོ། །) on their own separate line below the quote.
    

**Scope and the citation chain.** This skill operates on files in `1-SOURCES/Commentaries/`. Per `4-SYSTEM/CLAUDE.md` §6, the only permitted edits to a source file are structural (block boundaries, block IDs, navigation, factual `[Ed:...]` notes). Inserting a paragraph break is structural; rewording, glossing, or "fixing" the text is interpretation and is forbidden here. If the text needs OCR repair, that belongs to `format-commentary`, which runs first.

---

**Pipeline position**

```
format-commentary            →  commentary-segmentation  →  (block-ID stamping)  →  verse-context / verse-context-batch
(OCR clean, heading structure)   (this skill: boundaries)     (mechanical)            (rails consume the blocks)
```

Do not run this skill on text that is not yet OCR-clean. Do not run the block-ID pass until a domain specialist has approved the boundaries.

---

**Stage 0 — pre-clean already-formatted files (optional, run first when needed)**

Some commentary files arrive already carrying scaffolding from an earlier pass: standalone OCR index numbers (a line that is just `1`, `2`, `3`…), Obsidian block / verse IDs (`^0-1`, `^1-2`, `^1-2-0`), markdown headings (`##`, `###`), and line breaks that wrap verses and split sentences across lines. Segmentation needs to re-derive boundaries from continuous prose, so this scaffolding must be removed **before** Stage 1. If a file is already plain, under-segmented running text, skip this stage.

Run `scripts/preclean_commentary.py`:

```
python3 scripts/preclean_commentary.py \
    "1-SOURCES/Commentaries/<file>.md" \
    "0-INBOX/<file>.preclean.md" \
    --report "0-INBOX/<file>.preclean.tsv"
```

What it removes (editorial scaffolding only — never a character of body text):

- **Index / outline numbers** — any whitespace-bounded token consisting solely of digits (ASCII `0-9` or Tibetan `༠-༩`) with optional internal dots (hierarchical numbers such as `4.11`, `1.2.3`) and an optional trailing `.` or `)`, is removed unconditionally. Covers simple counters (`1`, `2`, `3`), terminated counters (`1.`, `2.`), and hierarchical section labels (`4.11`, `1.2.3.`). Catches both an OCR line counter on its own line *and* an inline outline number sitting before a sa-bcad opener (e.g. `…ཏོ། །19. དང་པོ་ནི།…`). Numbers fused to body text (e.g. `ལོ16`) are left untouched — Tibetan never delimits a real syllable with a bare space.
- **Block / verse IDs** — `^N`, `^N-N`, `^N-N-N` … wherever they appear.
- **Heading block IDs** — only the heading's trailing block ID is stripped. The leading `#`/`##`/`###` markup and the heading text are **both kept**, on their own line, acting as a separator between prose runs.
- **Intra-section line breaks** — consecutive content lines within a section are joined into one continuous run, so the rule-based segmenter starts from raw prose. Kept heading-text lines act as run separators, so a title or section head never fuses onto neighbouring prose.

Frontmatter (the leading `--- … ---` block) is preserved verbatim.

Like Stage 1, the script **never** edits body text: before writing it asserts that the output, with whitespace removed, is identical to the input with *only* the removed scaffolding (index lines, block IDs, heading hashes) and whitespace removed — and aborts otherwise. Write the cleaned draft to `0-INBOX/`, then feed it into Stage 1.

Updated flow when a file is already formatted:

```
preclean_commentary.py  →  segment_commentary.py  →  Stage-2 review  →  no-loss check  →  approval  →  block-ID stamping
(Stage 0: strip scaffolding)  (Stage 1: boundaries)
```

---

**Two-stage method**

Segmentation is split into a deterministic stage that is always safe, and an LLM stage that handles only what the rules cannot.

**Stage 1 — deterministic boundary detection (script).**
Run `scripts/segment_commentary.py`. It inserts a paragraph break at every high-confidence *functional* boundary in the Tibetan, and only there:

- `terminal-particle` — a clause-final particle (འོ/ནོ/དོ/སོ/ཏོ…) plus `།` ends a prose sentence.
- `quote-close` — explicit closers `ཞེས་སོ། །`, `ཅེས་སོ། །`, `ཞེས་གསུངས་སོ། །`, `ཞེས་པའོ། །` end a citation.
- `enumeration-head` — a sa-bcad head such as `…ལ་གསུམ་སྟེ།` / `…ལ་གཉིས་ལས།` closes; the
- `ordinal-open` — `དང་པོ་…`, `གཉིས་པ་…`, `གསུམ་པ་…` opens a new topical node.
- `objection-close` / `objection-open` — `…ཅེ་ན།` / `…ཞེ་ན།` closes an objection; `འོ་ན་…` opens the reply or next objection.
- `verse-stanza` — a paragraph that is itself a complete verse stanza (ཚིགས་བཅད) is detected automatically and emitted as a single block without running the rule engine. Detection criteria: ends with a double shad (`།།` / `། །`); yields 2–4 pādas when split on shads; every pāda has 6–11 syllables; syllable counts are uniform across pādas (±1). Detected stanzas are never split by the syllable cap and are never flagged `STAGE2_REVIEW`.

```
python3 scripts/segment_commentary.py \
    "1-SOURCES/Commentaries/<file>.md" \
    "0-INBOX/<file>.segmented.md" \
    --report "0-INBOX/<file>.segreport.tsv" \
    --max-syllables 40
```

The script **never** edits content: before writing, it asserts that the output with all inserted blank lines removed is byte-identical to the input, and aborts otherwise. Write the Stage-1 output to `0-INBOX/` first — never overwrite the source until boundaries are approved.

**Stage 2 — semantic refinement (LLM, this prompt).**
Open the Stage-1 report and review only the segments flagged `STAGE2_REVIEW` (longer than `--max-syllables`). These are prose runs with no lexical cue. For each, insert a paragraph break at the genuine topic shift — typically where the commentary moves from stating a position to giving its reason, from one objection to the next, or from gloss to scriptural support. Constraints:

- Only *insert* `\n\n` boundaries. Do not change, reorder, or delete any syllable.
- Verse stanzas that form their own paragraph are already protected by the script (trigger `verse-stanza`). For verse embedded inside a larger prose paragraph — where the script could not isolate the stanza — do not split pādas; insert a break before the first pāda and after the final `།།`, keeping all pādas of one stanza together. Never merge two independent stanzas into one block.
- Place a source-attribution line (e.g. `…ལས།`) and its closing `ཞེས་སོ། །` on their own blocks around the quote, per `format-commentary` §3.
- When a passage genuinely cannot be cut without breaking sense, leave it whole and note it; over-long is safer than wrong.

After Stage 2, re-run the no-loss check (concatenate all blocks, strip whitespace, compare to the source) before proceeding.

---

**Granularity target**

- Aim for 1–2 sentences of prose per block, one stanza per verse block, one quotation per quote block — small enough that a downstream rail can cite exactly the span it needs.
- A block that still exceeds ~40 tsheg-delimited syllables after Stage 2 should be revisited unless it is a single indivisible quotation or stanza.

---

**Block-ID stamping (separate, mechanical pass — out of scope here but documented for the handoff)**

Once boundaries are approved, IDs are assigned exactly as `format-commentary` §4 specifies: a `^N-…` ID at the end of every block, numbering restarting under each `##` / `###` heading, no IDs on headings, max three segments. Keep this as its own step so segmentation can be re-tuned and re-run without disturbing IDs already in use elsewhere in the vault.

---

**Procedure**

1. Confirm the file is OCR-clean (run `format-commentary` first if not).
2. If the file already carries index numbers, block/verse IDs, headings, or per-line/per-verse breaks, run **Stage 0** (`preclean_commentary.py`) to `0-INBOX/` to strip the scaffolding back to continuous prose. Skip if the file is already plain running text.
3. Run Stage 1 (on the Stage-0 output, if you ran it) to `0-INBOX/`, producing the segmented draft and the TSV report.
4. Review `STAGE2_REVIEW`-flagged segments and refine boundaries by hand (Stage 2).
5. Re-run the no-loss check; confirm every non-whitespace character is preserved.
6. Have a domain specialist approve the boundaries.
7. Hand off to the block-ID pass, then copy the approved, ID-stamped file back into `1-SOURCES/Commentaries/`.

**Output**

- A boundary-segmented commentary draft in `0-INBOX/` (not the source — the source is only updated after approval and ID stamping).
- A TSV report listing each segment, the rule that triggered its boundary, its syllable count, and any `STAGE2_REVIEW` flag.

**Rules recap**

- No character changes — boundaries only. The script enforces this; Stage 2 must honor it too.
- OCR repair and translation are out of scope (other skills own those).
- Never write block IDs in this step.
- When in doubt, under-cut rather than over-cut.
