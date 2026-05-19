---
name: section-summary-combined
description: Combine all per-commentary raw summaries for one TOC node into a single 2-RAILS/Sections/<node-id>.md, preserving original-language terminology and adding an English translation. This is what the translate-section skill loads to orient itself before tackling a section.
---

# section-summary-combined

This skill produces the **combined section summary** for one node in the table of contents. It reads every raw per-commentary summary that exists for the node under `2-RAILS/Sections/Raw/`, synthesises them into a single original-language summary, flags interpretive divergences across commentaries, and adds an English translation underneath.

The output is one of the three context layers loaded by `translate-section` (alongside `verse-context` and the per-track bilingual glossary).

---

## Inputs

- **Node ID** — the TOC node to combine (e.g. `1-1-0`).
- **All raw summary files** for that node under `2-RAILS/Sections/Raw/*/<node-id>.md`. Run `glob` for `2-RAILS/Sections/Raw/*/<node-id>.md` to discover them.

If only one commentary covers the node, this skill still runs — it produces a single-source combined summary and adds the English translation.

## Output

One file at:

```
2-RAILS/Sections/<node-id>.md
```

If the file already exists, update it in place. Preserve any manual edits to existing paragraphs unless the underlying raw summaries have changed.

---

## Output file format

```markdown
---
node_id: <e.g. 1-1-0>
node_heading: <original-language heading text>
language: <primary original language, e.g. pi>
commentaries: [<commentary-name>, <commentary-name>, ...]
raw_sources:
  - 2-RAILS/Sections/Raw/<commentary-name>/<node-id>.md
  - 2-RAILS/Sections/Raw/<commentary-name>/<node-id>.md
status: draft
---

## <node-heading verbatim>

### Synthesis (original language)

<one or more paragraphs in the original language that state what every
commentary agrees on for this node. Use the commentary tradition's own
terminology. Each paragraph ends with citations to the raw summaries it
draws on, e.g. (Raw/dhammasangani-atthakatha/1-1-0.md), and through them
to the original commentary block IDs.>

### Divergences

<only include this section if commentaries differ on what this node does
or how it should be read. Each divergence is one line:>

- **<topic>** — <commentary-A> reads ... ⚑; <commentary-B> reads ... ⚑.
  (Raw/<commentary-A>/<node-id>.md) (Raw/<commentary-B>/<node-id>.md)

### English translation

<English translation of the Synthesis paragraphs above, in the same order.
This is the only English content in the file. The translation preserves
the technical Pali (or other source-language) terms in italics on first
mention, glossed parenthetically, and as-is thereafter.>
```

---

## Rules

1. **Original-language synthesis comes first; the English translation is downstream.** Never draft the English first and back-translate.
2. **Synthesis states only what every raw summary supports.** Anything attested in only one commentary, or contested across commentaries, goes in **Divergences**, never in Synthesis.
3. **Cite the raw summaries, not the source files directly.** The raw summaries already carry the source-block citations; the combined file cites the raw layer to keep responsibility traceable.
4. **Preserve original-language terminology.** The Synthesis paragraphs use the same vocabulary as the raw summaries. Do not substitute a commentator's term with a synonym.
5. **The English translation is faithful, not paraphrastic.** Translate the Synthesis sentence-for-sentence. Preserve the technical terms; gloss them parenthetically on first mention; never replace them with English equivalents that erase distinctions the original-language summary makes.
6. **Divergence flag ⚑** marks every genuine interpretive split. The translation skill needs to see these — they often mark passages that require a translator decision rather than a default rendering.

---

## Procedure

1. Glob `2-RAILS/Sections/Raw/*/<node-id>.md`. If no files match, abort with an error — `section-summary-raw` must run first.
2. Read each raw summary. Note the commentary name, the language, and every claim asserted.
3. Identify the claims that every raw summary supports (consensus) and the claims that appear in only some, or that conflict between commentaries (divergence).
4. Draft the Synthesis in the primary source language. Each paragraph closes with citations to the raw files that support it.
5. If divergences exist, write the **Divergences** section. One bullet per divergence, both commentary positions marked with ⚑, both raw files cited.
6. Translate the Synthesis into English. Preserve technical terms (italicised on first mention with a parenthetical gloss; bare thereafter). Do not translate the Divergences.
7. Fill the frontmatter. Set `status: draft`.
8. Write the file to `2-RAILS/Sections/<node-id>.md`.

---

## Example

For node `1-1-0`:

```markdown
---
node_id: 1-1-0
node_heading: Ganthārambhakathā
language: pi
commentaries: [dhammasangani-atthakatha, dhammasangani-mulatiika]
raw_sources:
  - 2-RAILS/Sections/Raw/dhammasangani-atthakatha/1-1-0.md
  - 2-RAILS/Sections/Raw/dhammasangani-mulatiika/1-1-0.md
status: draft
---

## Ganthārambhakathā

### Synthesis (original language)

Imissā ganthārambhakathāya ācariyo paṭhamaṃ ratanattayassa namassanaṃ
karoti, tato Dhammasaṅgaṇī-aṭṭhakathāya nāmaṃ niyameti.
(Raw/dhammasangani-atthakatha/1-1-0.md)
(Raw/dhammasangani-mulatiika/1-1-0.md)

### English translation

In this opening section the commentator first pays homage to the Triple
Gem, then fixes the name of the *Dhammasaṅgaṇī-aṭṭhakathā* (commentary to
the Dhammasaṅgaṇī).
```

---

## Completion check

- [ ] Every raw summary under `2-RAILS/Sections/Raw/*/<node-id>.md` is listed in `raw_sources`
- [ ] Synthesis contains only consensus claims
- [ ] Every divergence is flagged with ⚑ and cited to both raw files
- [ ] English translation tracks the Synthesis paragraph-for-paragraph
- [ ] Technical source-language terms are preserved (italicised, glossed on first mention)
- [ ] Heading matches `node_heading` exactly
- [ ] Frontmatter complete
