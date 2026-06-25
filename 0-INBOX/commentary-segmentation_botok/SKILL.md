---
name: commentary-segmentation
description: Segment an OCR-clean but under-segmented Tibetan commentary in 1-SOURCES/Commentaries into short, individually-referenceable blocks using botok sentence boundaries only. Use when a commentary's text is one continuous run (or has overly long paragraphs) and needs breaking into citation-sized units before block IDs are applied. Runs AFTER format-commentary's OCR cleanup and BEFORE block-ID stamping and verse-context. Does not interpret, translate, or alter a single character of the source.
---

**Role:** Expert editor in classical Tibetan Buddhist commentary (`འགྲེལ་པ་`) structure and Obsidian markdown.

**Task:** Insert block boundaries into a Tibetan commentary so each block is a single botok sentence — without adding, removing, reordering, or re-spelling any character of the source.

Sentence boundaries are detected entirely by **botok** (`WordTokenizer` + `sentence_tokenizer()`), the pure-Python Tibetan word tokenizer (`pip install botok`). It uses POS tags and a dictionary trie to identify terminal particles, clause boundaries, and verb endings. Each botok sentence becomes one block. No rule-based post-processing is applied: there is no quote-frame, sa-bcad enumeration, ordinal-opener, verse-meter, or syllable-cap logic — segmentation is botok and nothing else.

**Scope and the citation chain.** This skill operates on files in `1-SOURCES/Commentaries/`. Per `4-SYSTEM/CLAUDE.md` §6, the only permitted edits to a source file are structural (block boundaries, block IDs, navigation, factual `[Ed:...]` notes). Inserting a paragraph break is structural; rewording, glossing, or "fixing" the text is interpretation and is forbidden here. If the text needs OCR repair, that belongs to `format-commentary`, which runs first. The script enforces this with a no-loss assertion: the output minus whitespace must equal the input minus whitespace, or it aborts and writes nothing. Because botok's own `norm_sent` rewrites spaces and punctuation, each block's text is reconstructed from the original paragraph using the tokens' character offsets, so nothing but whitespace ever changes.

---

**What good output looks like**

- **Granularity:** one botok sentence per block — small enough that a downstream rail can cite the span it needs. The boundary is wherever botok detects a sentence end (terminal particle, clause-boundary particle, or verb followed by a shad); nothing finer is imposed.
- **Verses and quotes:** these are NOT specially detected. A verse or quotation is broken wherever botok places a sentence boundary inside it, like any other text. Splitting a stanza or separating an attribution onto its own block is a hand-review decision (see below), not something the script does.

---

**Pipeline position**

```
format-commentary            →  commentary-segmentation  →  (block-ID stamping)  →  verse-context / verse-context-batch
(OCR clean, heading structure)   (this skill: boundaries)     (mechanical)            (rails consume the blocks)
```

Do not run this skill on text that is not yet OCR-clean. Do not run the block-ID pass until a domain specialist has approved the boundaries.

```
[Stage 0]                   [Stage 1 — botok]               [check]        [human]      [next skill]
preclean_commentary.py  →  segment_commentary.py  →  no-loss vs  →  approval  →  block-ID
(strip scaffolding,         (botok sentence                   source                     stamping
 optional)                  tokenization only)
```

---

**Installation**

botok must be installed before running Stage 1:

```bash
pip install botok
```

On first init the `WordTokenizer` downloads the `"general"` Tibetan dialect pack (cached under your home directory) and builds a trie (~10–15 s). Subsequent runs reuse the cache and trie. botok is pure Python, so it is noticeably slower than botok-rs — for large batches the trie build is paid once per worker process.

---

**Scripts at a glance**

| Script | Stage | Role |
|---|---|---|
| `preclean_commentary.py` | 0 | Strip prior scaffolding (index numbers, block IDs, heading IDs, per-line breaks) back to continuous prose. Optional. |
| `segment_commentary.py`  | 1 | botok sentence tokenization. The core of the skill. Output is the final segmented draft. |
| `batch_segment.py`       | 0+1 | Run Stage 0 + Stage 1 over a whole directory in parallel; emits per-file reports plus a batch summary. |

All scripts share `--dry-run` (validate, write nothing) and a `--report` TSV. Paths below are relative to the vault root.

---

**Stage 0 — pre-clean already-formatted files (optional, run first when needed)**

Some commentary files arrive already carrying scaffolding from an earlier pass: standalone OCR index numbers (a line that is just `1`, `2`, `3`…), Obsidian block / verse IDs (`^0-1`, `^1-2`, `^1-2-0`), markdown headings (`##`, `###`), and line breaks that wrap verses and split sentences across lines. Segmentation re-derives boundaries from continuous prose, so this scaffolding must be removed **before** Stage 1. If a file is already plain, under-segmented running text, skip this stage.

```
python3 scripts/preclean_commentary.py \
    "1-SOURCES/Commentaries/<file>.md" \
    "0-INBOX/<file>.preclean.md" \
    --report "0-INBOX/<file>.preclean.tsv"
```

What it removes (editorial scaffolding only — never a character of body text):

- **Index / outline numbers** — any whitespace-bounded token consisting solely of digits (ASCII `0-9` or Tibetan `༠-༩`) with optional internal dots (hierarchical numbers such as `4.11`, `1.2.3`) and an optional trailing `.` or `)`, removed unconditionally. Covers simple counters (`1`, `2`, `3`), terminated counters (`1.`, `2.`), and hierarchical section labels (`4.11`, `1.2.3.`). Catches both an OCR line counter on its own line *and* an inline outline number sitting before a sa-bcad opener (e.g. `…ཏོ། །19. དང་པོ་ནི།…`). Numbers fused to body text (e.g. `ལོ16`) are left untouched — Tibetan never delimits a real syllable with a bare space.
- **Block / verse IDs** — `^N`, `^N-N`, `^N-N-N` … wherever they appear.
- **Heading block IDs** — only the heading's trailing block ID is stripped. The leading `#`/`##`/`###` markup and the heading text are **both kept**, on their own line, acting as a separator between prose runs. A heading whose text is itself a bare number (likely OCR noise) is kept but flagged `heading-suspect` in the report.
- **Intra-section line breaks** — consecutive content lines within a section are joined into one continuous run, so Stage 1 starts from raw prose. Kept heading-text lines act as run separators, so a title or section head never fuses onto neighbouring prose.

Frontmatter (the leading `--- … ---` block) is preserved verbatim and excluded from the no-loss comparison.

---

**Stage 1 — botok sentence tokenization**

`scripts/segment_commentary.py` uses **botok** for sentence-level segmentation and does nothing else: each botok sentence becomes one block.

Each input paragraph is tokenised with `WordTokenizer` (dictionary-backed, POS-tagged). The token stream is passed to `sentence_tokenizer()`, which finds sentence boundaries at:

- **Terminal particles** (`འོ་`, `སོ་`, `ཏོ་`, `དོ་`, `ནོ་`, `གོ་`, `ལོ་`…) followed by punctuation (shad). The tokenizer uses POS tags (`PART`) so it distinguishes a genuine terminal particle from the same syllable occurring mid-compound.
- **Clause-boundary particles** (`སྟེ་`, `ཏེ་`, `ནས་`, `ན་`, `ལ་`, `ཞིང་`…) followed by punctuation.
- **Verbs** (and verb-like enders `ཡིན་`, `ཡོད་`, `མེད་`…) followed by punctuation.
- Short verb-less fragments are joined to a neighbour rather than left as isolated one-word blocks (botok's `join_no_verb_sentences`, threshold 4 tokens). In practice botok still leaves some one-word tails (e.g. a lone verb after `ནས་`); these are a hand-review item, not a script fix.

The exact original text of each sentence is recovered from its tokens' character offsets, so spaces, tshegs, and shads survive untouched (botok's lossy `norm_sent` is not used).

Structural lines are handled but never segmented: the frontmatter (`--- … ---`) is preserved verbatim, markdown headings (`#`…`######`) pass through on their own line, and blank-line-separated paragraphs are tokenised independently. If botok returns no sentences for a paragraph, that paragraph is kept whole as a single block.

There is **no** commentary-specific post-processing — no quote-open/close handling, no ordinal or sa-bcad enumeration splitting, no verse-stanza detection, and no syllable cap. Every report row carries the trigger `botok-sentence`. Any further granularity (splitting a stanza, isolating a `…ལས།` attribution or a `ཞེས་སོ། །` closer) is left to hand-review.

Two ways to run it:

```
# Single file:
python3 scripts/segment_commentary.py \
    "0-INBOX/<file>.preclean.md" \
    "0-INBOX/<file>.segmented.md" \
    --report "0-INBOX/<file>.segreport.tsv"

# Batch (whole directory, parallel):
python3 scripts/batch_segment.py \
    "1-SOURCES/Commentaries" "0-INBOX/segmented" \
    --preclean
```

The Stage-1 output goes to `0-INBOX/` — never overwrite the source until boundaries are approved.

**Batch mode** runs Stage 0 (with `--preclean`) then Stage 1 per file across all CPUs, skips files whose output already exists (`--force` to redo), and writes `batch_summary.tsv` (one row per file) into the output directory.

---

**Hand-review**

botok gives sentence boundaries only; it does not know commentary structure. After Stage 1, scan the report (longest rows by syllable count are the usual candidates) for blocks that should be cut finer or rejoined. Insert a paragraph break only at a genuine topic shift — where the commentary moves from a position to its reason, from one objection to the next, or from gloss to scriptural support. Because no quote/verse logic runs in the script, the following are now entirely hand decisions:

- Only *insert* `\n\n` boundaries. Do not change, reorder, or delete any syllable.
- For a verse embedded inside a larger paragraph, break before the first pāda and after the final `།།`, keeping the stanza together. Never merge two independent stanzas.
- Keep a `…ལས།` attribution line and its closing `ཞེས་སོ། །` on their own blocks (format-commentary §3).
- When a passage genuinely cannot be cut without breaking sense, leave it whole. Over-long is safer than wrong.

After hand-review, re-run a no-loss check against the **original source file** before proceeding.

---

**Block-ID stamping (separate, mechanical pass — out of scope here, documented for the handoff)**

Once boundaries are approved, IDs are assigned exactly as `format-commentary` §4 specifies: a `^N-…` ID at the end of every block, numbering restarting under each `##` / `###` heading, no IDs on headings, max three segments. Keeping this as its own step lets segmentation be re-tuned and re-run without disturbing IDs already in use elsewhere in the vault.

---

**Procedure**

1. Confirm the file is OCR-clean (run `format-commentary` first if not).
2. If the file carries index numbers, block/verse IDs, headings, or per-line/per-verse breaks, run **Stage 0** (`preclean_commentary.py`) to `0-INBOX/`. Skip if it is already plain running text.
3. Run **Stage 1** (`segment_commentary.py`, on the Stage-0 output if you ran it) to `0-INBOX/`, producing the segmented draft and the TSV report. For many files at once, use `batch_segment.py`.
4. Hand-review the report for blocks needing a finer cut (verses, quotations, long runs).
5. Re-run the no-loss check against the **original source file**.
6. Have a domain specialist approve the boundaries.
7. Hand off to the block-ID pass, then copy the approved, ID-stamped file back into `1-SOURCES/Commentaries/`.

**Output**

- A boundary-segmented commentary draft in `0-INBOX/` (not the source — the source is only updated after approval and ID stamping).
- TSV reports listing each segment (trigger `botok-sentence`), its syllable count, and a preview.

**Rules recap**

- No character changes — boundaries only. The script enforces this; hand edits must honor it too.
- OCR repair and translation are out of scope (other skills own those).
- Never write block IDs in this step.
- When in doubt, under-cut rather than over-cut.
