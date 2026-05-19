---
name: verse-context
description: Build the verse-level context file for one verse — transclude relevant commentary passages, synthesise commentators' interpretations in the original language, and write a disambiguated restatement of the verse in the original language (Pali) precise enough to exclude any mistranslation. Output goes to 2-RAILS/Verses/<verse-id>.md.
---

# verse-context

This skill produces the **verse-level factual context** that the translation skill works from. It is the single most important rail for defusing the hallucination failure mode: the translator never sees the raw verse alone, it sees a disambiguated version of the verse — a restatement in the original language so precise that no misreading of the Pali is possible.

The file has three sections, produced in order:

1. **Commentary passages** — transcluded directly from `1-SOURCES/` (no rewriting).
2. **Synthesis** — per-commentary interpretive prose in the original language, plus a divergences block where commentaries disagree.
3. **Disambiguated verse** — the verse restated in the original language with every ambiguity resolved according to the Synthesis.

---

## Inputs

- **Verse ID** — block ID of the verse in the root text, without the caret (e.g. `1-1`, `1-15`).
- **Root-text file** — `1-SOURCES/Text/<root-text>.md` (e.g. `pi-dhammasangani.md`).
- **Commentary files** — all relevant `1-SOURCES/Commentaries/*.md` files that discuss this verse. For Dhammasaṅgaṇī this typically includes the aṭṭhakathā, mūlaṭīkā, and anuṭīkā.

## Output

One file at:

```
2-RAILS/Verses/<verse-id>.md
```

If the file exists, update in place. Never overwrite a manually edited Synthesis without first checking that the manual edit is still supported by the underlying commentary transclusions.

---

## Output file format

```markdown
---
verse_id: <e.g. 1-1>
root_text: 1-SOURCES/Text/<root-text>.md
root_block: ^<verse-id>
language: <pi | sa | ...>
commentaries: [<commentary-name>, <commentary-name>, ...]
status: draft
---

## Verse

![[1-SOURCES/Text/<root-text>.md#^<verse-id>]]

## Commentary passages

### <commentary-name>

![[1-SOURCES/Commentaries/<commentary-name>.md#^<block-id>]]
![[1-SOURCES/Commentaries/<commentary-name>.md#^<block-id>]]

### <next commentary-name>

![[1-SOURCES/Commentaries/<commentary-name>.md#^<block-id>]]

## Synthesis (original language)

### <commentary-name>

<original-language prose summarising how this commentary reads the verse:
what each word refers to, which compound is read which way, which sense of
an ambiguous term is active, which referent each pronoun has. Every claim
ends with a citation to the source block.>
(1-SOURCES/Commentaries/<commentary-name>.md#^<block-id>)

### <next commentary-name>

<same shape, in the original language.>

### Consensus

<one paragraph in the original language stating what all commentaries agree
on for this verse — referents, sense selections, compound readings.>

### Divergences

<only if commentaries disagree. One bullet per divergence:>

- **<token or phrase>** — <commentary-A> reads ... ⚑; <commentary-B> reads ... ⚑.
  (1-SOURCES/Commentaries/<commentary-A>.md#^<block-id>)
  (1-SOURCES/Commentaries/<commentary-B>.md#^<block-id>)

## Disambiguated verse (original language)

<restatement of the verse in the original language. Every ambiguity that the
commentaries resolve is resolved here too. Where commentaries diverge, give
the Consensus reading and footnote the alternatives. This is the text the
translation skill works from — not the bare verse above.>

(1-SOURCES/Commentaries/<commentary-name>.md#^<block-id>)
(1-SOURCES/Commentaries/<commentary-name>.md#^<block-id>)
```

---

## Rules

1. **Three sections, fixed order: passages → synthesis → disambiguated verse.** The disambiguated verse is the output of the synthesis; never write it first.
2. **The Verse block transcludes the root text.** It never copies it. If the root-text file does not have the verse block ID, fix the root text first using `format-root-text` — do not work around it.
3. **Commentary passages are transclusions, not paraphrases.** Use `![[...#^block-id]]`. The translator can click through to the full block.
4. **Synthesis is one subsection per commentary, then a Consensus subsection, then Divergences if needed.** Per-commentary subsections preserve responsibility; Consensus collapses agreement; Divergences flag splits.
5. **All Synthesis prose is in the original language.** No English. No translation aside.
6. **The Disambiguated verse is in the original language only.** Pali for the Dhammasaṅgaṇī. The point of this section is to give the translator a version of the Pali in which no further interpretive decision is required — referents fixed, compounds parsed, ambiguous senses chosen.
7. **Every claim in the Synthesis and every choice in the Disambiguated verse is cited** to a source-block ID in `1-SOURCES/Commentaries/`.
8. **Divergences are not flattened.** If commentaries disagree on a referent and there is no consensus, the Disambiguated verse follows the most widely attested reading and footnotes the others as ⚑ alternatives — it never silently chooses.

---

## Procedure

1. Read the root-text verse block.
2. For each commentary file, locate every block that discusses this verse. The discussion may span several non-contiguous blocks. Record all relevant block IDs.
3. Draft the **Verse** section: one transclusion of the root block.
4. Draft the **Commentary passages** section: one subsection per commentary, transcluding every relevant block in source order.
5. Draft the **Synthesis** section, one commentary subsection at a time. Each subsection states, in the original language: what each word refers to, how each compound is parsed, which sense of ambiguous terms is active, what each pronoun's antecedent is. Cite every claim.
6. Write the **Consensus** subsection — the original-language paragraph that states what every commentary agrees on.
7. If genuine divergences exist, write the **Divergences** subsection. Both readings, both flags ⚑, both cited.
8. Draft the **Disambiguated verse**. Rewrite the verse in the original language so that every ambiguity the Synthesis resolved is explicit. Cite the commentary blocks that authorise each disambiguation.
9. Fill the frontmatter. Set `status: draft`.
10. Write the file to `2-RAILS/Verses/<verse-id>.md`.

---

## What "disambiguation" looks like in practice

Pali bare verse:

> *kusalā dhammā*

This phrase is famously underspecified — what counts as *kusalā*, what scope of *dhammā*, are they nominative or accusative here? A disambiguated version draws on the commentaries to fix all three:

> *kusalā dhammā* (nominative plural, masculine; *kusalā* in the sense of
> "free of fault and producing pleasant result" per the aṭṭhakathā ⚑; *dhammā*
> in the sense of "mental states classified by the Dhammasaṅgaṇī mātikā",
> excluding the meaning "doctrines" and excluding the meaning "phenomena
> generally" — the mūlaṭīkā confirms this scoping).

Every parenthetical above is grounded in a commentary citation. That is the level of resolution this section aims for.

---

## Completion check

- [ ] `verse_id`, `root_block`, and `language` set in frontmatter
- [ ] Verse block transcludes (does not copy) the root text
- [ ] Every commentary that mentions this verse appears as a subsection under Commentary passages
- [ ] Synthesis has one subsection per commentary + Consensus + (Divergences, if any)
- [ ] Every Synthesis claim ends with a `(1-SOURCES/Commentaries/...#^...)` citation
- [ ] Disambiguated verse is in the original language only
- [ ] Every disambiguating decision in the Disambiguated verse has a supporting citation
- [ ] Genuine commentary disagreements appear in Divergences with ⚑ on each position
