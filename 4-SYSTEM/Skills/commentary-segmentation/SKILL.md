---
name: commentary-segmentation
description: Segment an OCR-clean but under-segmented Tibetan commentary in 1-SOURCES/Commentaries into short, individually-referenceable blocks (prose paragraphs, verse stanzas, quotations) based on the functional content of the text — quotation frames, objection/answer markers, sa-bcad outline enumerations, sentence-final particles, and verse stanza detection. Use when a commentary's text is one continuous run (or has overly long paragraphs) and needs breaking into citation-sized units before block IDs are applied. Runs AFTER format-commentary's OCR cleanup and BEFORE block-ID stamping and verse-context. Does not interpret, translate, or alter a single character of the source.
---

**Role:** Expert editor in classical Tibetan Buddhist commentary (`འགྲེལ་པ་`) structure and Obsidian markdown.

**Task:** Insert block boundaries into a Tibetan commentary so each block is a citation-sized unit (a prose sentence or two, one verse stanza, or one quotation) — without adding, removing, reordering, or re-spelling any character of the source.

The boundaries follow the text's own functional signals: quotation frames, objection/answer markers, sa-bcad enumerations, sentence-final particles, and verse meter. Most of this is done deterministically by the scripts in `scripts/`; you only hand-finish what the rules cannot resolve.

**Scope and the citation chain.** This skill operates on files in `1-SOURCES/Commentaries/`. Per `4-SYSTEM/CLAUDE.md` §6, the only permitted edits to a source file are structural (block boundaries, block IDs, navigation, factual `[Ed:...]` notes). Inserting a paragraph break is structural; rewording, glossing, or "fixing" the text is interpretation and is forbidden here. If the text needs OCR repair, that belongs to `format-commentary`, which runs first. Every script here enforces this with a no-loss assertion: the output minus whitespace must equal the input minus whitespace, or it aborts and writes nothing.

---

**What good output looks like**

- **Granularity:** 1–2 sentences of prose per block; one stanza per verse block; one quotation per quote block — small enough that a downstream rail can cite exactly the span it needs. A prose block that exceeds ~40 tsheg-delimited syllables should be split unless it is a single indivisible clause, quotation, or stanza.
- **Verses (ཚིགས་བཅད):** one independent stanza per block. Keep a stanza's pādas together; never merge two independent stanzas into one block.
- **Quotes (ལུང་འདྲེན):** the source attribution (e.g. `སྡུད་པ་ལས།`) on its own block above the quote, and the closing formula (e.g. `ཞེས་སོ། །`) on its own block below it (format-commentary §3).

---

**Pipeline position**

```
format-commentary            →  commentary-segmentation  →  verse-context / verse-context-batch
(OCR clean, heading structure)   (this skill: boundaries)     (rails consume the blocks)
```

Do not run this skill on text that is not yet OCR-clean.

```
[Stage 0]                   [Stage 1]               [Stage 2]              [check]        [human]
preclean_commentary.py  →  segment_commentary.py  →  stage2_refine.py  →  no-loss vs  →  approval
(strip scaffolding,         (deterministic            (mechanical            source         + hand review
 optional)                  boundaries)               refinement)
```

---

**Scripts at a glance**

| Script | Stage | Role |
|---|---|---|
| `preclean_commentary.py` | 0 | Strip prior scaffolding (index numbers, block IDs, heading IDs, per-line breaks) back to continuous prose. Optional. |
| `segment_commentary.py`  | 1 | Deterministic boundary insertion. The core of the skill. |
| `stage2_refine.py`       | 2 | Mechanical refinement of the Stage-1 draft (newline expansion, citation/lead-in splits, optional connector splits). |
| `batch_segment.py`       | 0+1 | Run Stage 0 + Stage 1 over a whole directory in parallel; emits per-file reports plus a batch summary and a combined flagged-rows file. |

All scripts share `--dry-run` (validate, write nothing) and a `--report` TSV. Paths below are relative to the vault root.

---

**Stage 0 — pre-clean already-formatted files (optional, run first when needed)**

Some commentary files arrive already carrying scaffolding from an earlier pass: standalone OCR index numbers (a line that is just `1`, `2`, `3`…), Obsidian block / verse IDs (`^0-1`, `^1-2`, `^1-2-0`), markdown heading markers (`##`, `###`), and line breaks that wrap verses and split sentences across lines. Segmentation re-derives boundaries from continuous prose, so this scaffolding must be removed **before** Stage 1. If a file is already plain, under-segmented running text, skip this stage.

```
python3 scripts/preclean_commentary.py \
    "1-SOURCES/Commentaries/<file>.md" \
    "0-INBOX/<file>.preclean.md" \
    --report "0-INBOX/<file>.preclean.tsv"
```

What it removes (editorial scaffolding only — never a character of body text):

- **Index / outline numbers** — any whitespace-bounded token consisting solely of digits (ASCII `0-9` or Tibetan `༠-༩`) with optional internal dots (hierarchical numbers such as `4.11`, `1.2.3`) and an optional trailing `.` or `)`, removed unconditionally. Covers simple counters (`1`, `2`, `3`), terminated counters (`1.`, `2.`), and hierarchical section labels (`4.11`, `1.2.3.`). Catches both an OCR line counter on its own line *and* an inline outline number sitting before a sa-bcad opener (e.g. `…ཏོ། །19. དང་པོ་ནི།…`). Numbers fused to body text (e.g. `ལོ16`) are left untouched — Tibetan never delimits a real syllable with a bare space.
- **Block / verse IDs** — `^N`, `^N-N`, `^N-N-N` … wherever they appear.
- **Heading markers** — all `#` characters are stripped from the body. Heading text is preserved as plain prose and acts as a natural separator between prose runs; a heading whose text is a bare number (likely OCR noise) is flagged `heading-suspect` in the report.
- **Intra-section line breaks** — consecutive content lines are joined into one continuous run, so Stage 1 starts from raw prose. Heading-text lines (now plain prose) still act as run separators, so a section title never fuses onto neighbouring content.

Frontmatter (the leading `--- … ---` block) is preserved verbatim and excluded from the no-loss comparison.

---

**Stage 1 — deterministic boundary detection (script)**

`scripts/segment_commentary.py` inserts a paragraph break at every high-confidence *functional* boundary, and only there:

- `terminal-particle` — a clause-final particle (`འོ`/`ནོ`/`དོ`/`སོ`/`ཏོ`/`གོ`/`ལོ`…) plus `།` ends a prose sentence. Broad catch-all; runs last so more specific markers claim a position first.
- `quote-close` — explicit closers (`ཞེས་སོ། །`, `ཅེས་སོ། །`, `ཞེས་གསུངས་སོ། །`, `ཞེས་པའོ། །`, `ཞེས་བྱ་བའོ། །`…) end a citation.
- `quote-open` — a source-attribution marker (`…ལས།`, `…གསུངས།`) gets its own block before the cited passage.
- `enumeration-head` — a sa-bcad head closing on a number-word + suffix (e.g. `…ལ་གསུམ་སྟེ།`, `…ལ་གཉིས་ལས།`) ends a node.
- `ordinal-open` — `དང་པོ་…`, `གཉིས་པ་…`, `གསུམ་པ་…` opens a new topical node.
- `objection-close` / `objection-open` — `…ཅེ་ན།` / `…ཞེ་ན།` / `…སྙམ་ན།` closes an objection; `འོ་ན་…` opens the reply. `objection-open` is a weak-context rule: it only auto-cuts when it sits just after a shad; otherwise it is reported as a `-candidate` for a human to judge rather than cut blindly.
- `verse-stanza` — a run of 2–4 consecutive clause units, each 6–11 syllables, uniform in length (max − min ≤ 2), each ending on a strong (double) shad, is peeled out as one protected stanza: emitted whole, never run through the rule engine or the syllable cap, never flagged `STAGE2_REVIEW`. A single-shad unit sandwiched between two stanza pādas is bridged into the run (some sources mark pāda ends with a single shad). An isolated pāda-length clause stays with the surrounding prose, so a medium prose sentence is never mistaken for a one-line verse.

After the rule pass it enforces a syllable cap: any segment still longer than `--max-syllables` is split at shad (clause) boundaries; over-cap segments with no internal shad are flagged `STAGE2_REVIEW:NO_SHAD_FOUND`. Over-fragmented adjacent segments are merged back while they fit the cap (citation boundaries are never merged away). The run also prints a **quote-balance** check (count of `quote-open` vs `quote-close`); a `MISMATCH` points to an unclosed or stray citation marker worth a look.

Two ways to run it:

```
# (a) cap-based — finer control, every over-cap block flagged for review:
python3 scripts/segment_commentary.py \
    "0-INBOX/<file>.preclean.md" \
    "0-INBOX/<file>.segmented.md" \
    --report "0-INBOX/<file>.segreport.tsv" \
    --max-syllables 40

# (b) structural — closest match to the canonical block layout:
python3 scripts/segment_commentary.py \
    "0-INBOX/<file>.preclean.md" \
    "0-INBOX/<file>.structural.md" \
    --report "0-INBOX/<file>.segreport.tsv" \
    --structural
```

`--structural` breaks prose only at strong (double-shad) sentence ends, section heads, and citation frames; emits verses one pāda per line; splits citation markers and re-attaches short closing formulas to their block; and implies **no syllable cap**. It is the best single-pass match for the layout downstream rails expect. Use the cap-based mode (a) when you want every long run surfaced for manual review instead.

Note the default for `--max-syllables` is **50** if you omit it; the granularity target is ~40, so pass `--max-syllables 40` explicitly (the batch runner already defaults to 40). The cap is ignored under `--structural`.

The Stage-1 output goes to `0-INBOX/` — never overwrite the source until boundaries are approved.

**Batch mode.** To process an entire directory in parallel:

```
python3 scripts/batch_segment.py \
    "1-SOURCES/Commentaries" "0-INBOX/segmented" \
    --preclean --max-syllables 40
```

It runs Stage 0 (with `--preclean`) then Stage 1 per file across all CPUs, skips files whose output already exists (`--force` to redo), and writes `batch_summary.tsv` (one row per file, including the quote-balance status) and `batch_flagged.tsv` (every `STAGE2_REVIEW` row across all files) into the output directory.

---

**Stage 2 — semantic refinement**

Most of the Stage-1 residue is mechanical and is handled by `scripts/stage2_refine.py`. Run it first, then hand-review only what it leaves behind.

```
python3 scripts/stage2_refine.py \
    "0-INBOX/<file>.segmented.md" \
    "0-INBOX/<file>.stage2.md" \
    --max-syllables 40 \
    --source "1-SOURCES/Commentaries/<file>.md" \
    --report "0-INBOX/<file>.stage2.tsv"
```

It performs, deterministically and no-loss:

- **Newline expansion** (default) — `merge_short_segments` in Stage 1 joins consecutive source lines that were each under the cap, leaving an internal `\n` inside a block. For any over-cap block containing an internal `\n`, every `\n` becomes a paragraph break — each original source line becomes its own block. This restores boundaries the source already marked; it never guesses.
- **Citation lead-in / verse split** (default) — a short source-frame line glued onto a following stanza is peeled back onto its own block.
- **Connector split** (opt-in, `--split-connectors`) — over-cap *single-line* prose is split at strong sub-clause connectors (`ཅིང་`/`ཞིང་`/`སྟེ་`/`ཏེ་`/`ནས་`/`ལས་`), never producing a piece below 8 syllables. Off by default: a connector is a weaker signal than a source-marked line break, so prefer leaving a block whole over a wrong cut.

Passing `--source` adds a second no-loss assertion against the **original source file**, so any deviation inherited from Stage 1 is caught here rather than passed downstream silently. Blocks still over the cap that the tool can't safely split are reported as `STAGE2_MANUAL`.

**Hand-review** the `STAGE2_MANUAL` rows (and any `STAGE2_REVIEW` rows from Stage 1). These are prose runs with no lexical cue. Insert a paragraph break only at a genuine topic shift — where the commentary moves from a position to its reason, from one objection to the next, or from gloss to scriptural support. Rules for hand edits:

- Only *insert* `\n\n` boundaries. Do not change, reorder, or delete any syllable.
- For a verse embedded inside a larger prose paragraph (the script couldn't isolate it), do not split pādas: break before the first pāda and after the final `།།`, keeping the stanza together. Never merge two independent stanzas.
- Keep a `…ལས།` attribution line and its closing `ཞེས་སོ། །` on their own blocks (format-commentary §3).
- When a passage genuinely cannot be cut without breaking sense, leave it whole. Over-long is safer than wrong.

If you write any bespoke refinement code, read `scripts/segment_commentary.py` first — two facts save rewrites:

- **TSV index ≠ paragraph index.** The TSV numbers segments as the script counts them internally; `merge_short_segments` then merges short adjacent segments, so TSV row N does not map to output paragraph N.
- **Use the script's `_squeeze`** (the whitespace-translate table in `segment_commentary.py` / `stage2_refine.py`, not `re.sub(r'\s+','',s)`) for any no-loss check, or you may see phantom mismatches. If a mismatch appears, first test `squeeze(source) == squeeze(stage1_output)` to see whether it predates your change.

After Stage 2, re-run a no-loss check against the **original source** (the `--source` flag does this automatically) before proceeding.

---

**Procedure**

1. Confirm the file is OCR-clean (run `format-commentary` first if not).
2. If the file carries index numbers, block/verse IDs, headings, or per-line/per-verse breaks, run **Stage 0** (`preclean_commentary.py`) to `0-INBOX/`. Skip if it is already plain running text.
3. Run **Stage 1** (`segment_commentary.py`, on the Stage-0 output if you ran it) to `0-INBOX/`, producing the segmented draft and the TSV report. Use `--structural` for the canonical layout, or `--max-syllables 40` for review-oriented output. For many files at once, use `batch_segment.py`.
4. Run **Stage 2** (`stage2_refine.py`) with `--source` pointing at the original. Then hand-review the `STAGE2_MANUAL` / `STAGE2_REVIEW` rows.
5. Re-run the no-loss check against the **original source file**.
6. Have a domain specialist approve the boundaries.

**Output**

- A boundary-segmented commentary draft in `0-INBOX/` (not the source — the source is only updated after human approval).
- TSV reports listing each segment, the rule that triggered its boundary, its syllable count, and any review flag.

**Rules recap**

- No character changes — boundaries only. The scripts enforce this; hand edits must honor it too.
- OCR repair and translation are out of scope (other skills own those).
- Never write block IDs in this step.
- When in doubt, under-cut rather than over-cut.
