---
name: local-wiki-article
description: Create or update a Local-Wiki article in 2-RAILS/Local-Wiki/<term>.md for one key term explained in the commentaries. Populate with citations from the commentaries (in the original language) and a short contextual definition drafted from those citations. All content in the original language. Used as the reference of last resort when a bilingual glossary entry does not yet capture a term adequately.
---

# local-wiki-article

The Local-Wiki holds one article per **key term** explained in the commentary tradition of this text. Its purpose is narrow: when the per-track bilingual glossary does not yet have a satisfactory rendering for a term, the `glossary-select` skill consults the Local-Wiki article for that term to derive a better one. Local-Wiki articles are also the long-form definition that the translator falls back on when the bilingual glossary line alone is too compressed to disambiguate.

Local-Wiki articles are **monolingual** — they are in the original language of the commentaries (Pali for the Dhammasaṅgaṇī). They are not a translation aid in themselves; they are a primary-source-grounded definition of the term as the commentators use it.

---

## Inputs

- **Term** — the lemma to document, in the original language (e.g. `kusala`, `dhamma`, `citta`, `phassa`).
- **Commentary files** — `1-SOURCES/Commentaries/*.md` files that define or develop this term.

## Output

One file at:

```
2-RAILS/Local-Wiki/<term>.md
```

`<term>` is the lemma in lowercase, with diacritics preserved and underscores for spaces (e.g. `kusalā_dhammā.md`, `kāmāvacara.md`).

If the file already exists, **update**: add new citations, fold them into the existing structure, refine the definition if the new citations warrant it. Never silently overwrite existing content drawn from cited sources.

---

## Output file format

```markdown
---
term: <lemma in original-language script with diacritics>
language: <pi | sa | bo | zh>
text: <text-name, e.g. dhammasangani>
commentaries: [<commentary-name>, <commentary-name>, ...]
attested_blocks: [<commentary-name>:^<block-id>, ...]
status: draft
---

## <term>

### Contextual definition

<one short paragraph in the original language defining the term *as the
commentary tradition of this text uses it*. This is a synthesis of the
attestations below, not an external dictionary definition. Anything the
commentaries do not say is not in this paragraph.>

(<commentary-name>#^<block-id>)
(<commentary-name>#^<block-id>)

### Attestations

#### <commentary-name>

> <quotation from the commentary, in the original language, that defines or
> develops this term — verbatim, with the block ID inline at the end.>
> (1-SOURCES/Commentaries/<commentary-name>.md#^<block-id>)

> <next quotation, if the commentary develops the term further.>
> (1-SOURCES/Commentaries/<commentary-name>.md#^<block-id>)

#### <next commentary-name>

> <quotation>
> (1-SOURCES/Commentaries/<commentary-name>.md#^<block-id>)

### Divergences

<only include if commentaries treat the term differently. One bullet per
divergence, both readings flagged with ⚑, both cited.>

- **<aspect of meaning>** — <commentary-A> reads ... ⚑;
  <commentary-B> reads ... ⚑.
  (1-SOURCES/Commentaries/<commentary-A>.md#^<block-id>)
  (1-SOURCES/Commentaries/<commentary-B>.md#^<block-id>)

### Related terms

- [[<related-term-1>]] — <one-line note in original language on the relationship>
- [[<related-term-2>]] — <one-line note>
```

---

## Rules

1. **One article per term sense.** If the commentaries clearly distinguish two senses of the same lemma (e.g. *kusala* in the meaning "wholesome / skilful" vs. *kusala* in the meaning "blade of grass"), create two articles: `kusala_(wholesome).md` and `kusala_(grass).md`. The parenthetical sense disambiguator is the only English in any Local-Wiki filename.
2. **Original language only inside the file.** Definitions, quotations, divergence notes — everything is in the original language. The frontmatter is the only place where English (key names like `language`, `status`) appears.
3. **Citations everywhere.** The Contextual definition cites every commentary it draws on. Each Attestation block is a verbatim quotation with the block ID at the end. The Divergences cite both sides.
4. **Quote, don't paraphrase, inside Attestations.** Block quotations are verbatim from the commentary. If a quotation is long, take the most definitional sentence; the full passage remains accessible via the cited block ID.
5. **The Contextual definition does not exceed what the citations support.** If the commentaries do not address a particular nuance, the Local-Wiki article does not address it either. The Local-Wiki is not a Wiktionary entry — it is a record of this text's commentaries' usage.
6. **Sense disambiguators are added only when commentaries themselves distinguish senses.** Do not impose senses the tradition does not.

---

## Procedure

1. Search every commentary in `1-SOURCES/Commentaries/` for blocks that define, gloss, or develop the term. Use a literal text search for the lemma — and for inflected forms if the lemma is inflected.
2. Record the source block ID for each hit. Keep only blocks that *explain* the term — passing mentions go in `attested_blocks` frontmatter but not in Attestations.
3. If the explanations clearly distinguish multiple senses, create one file per sense; assign each Attestation to the right file.
4. For each file, write the **Attestations** section first, one subsection per commentary, every quotation verbatim with block ID.
5. Draft the **Contextual definition** as a synthesis of the Attestations. One short paragraph. Cite the Attestations it draws on.
6. If commentaries diverge on the term's scope, range, or precise meaning, write a **Divergences** section. Each line flagged with ⚑ on each side and cited.
7. Add **Related terms** as `[[...]]` links to other Local-Wiki articles, each with a one-line note (in the original language) on the relationship.
8. Fill frontmatter. Set `status: draft`.
9. Write the file to `2-RAILS/Local-Wiki/<term>.md`.

---

## Completion check

- [ ] Filename uses lowercase lemma with diacritics; sense disambiguator only if commentaries distinguish senses
- [ ] Frontmatter complete; `attested_blocks` lists every block that mentions the term, not just those quoted
- [ ] Every Attestation is a verbatim quotation with the block ID inline
- [ ] Contextual definition draws only on what the Attestations say
- [ ] All content (definition, quotes, divergences) is in the original language
- [ ] Related terms link to other Local-Wiki articles, not to external sources
