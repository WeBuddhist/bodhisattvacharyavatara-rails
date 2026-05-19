---
name: glossary-select
description: Build the per-track working bilingual glossary at 3-TRANSFORMATIONS/Translation/<track-name>/bilingual glossary.md by selecting the preferred rendering for each term from the consolidated 2-RAILS/Bilingual-Glossaries/<pair>.md, guided by the track's requirements.md. When no attested rendering satisfies the requirements, derive a new one from the term's Local-Wiki article and feed the new rendering back into the rails.
---

# glossary-select

This skill builds the **per-track bilingual glossary** that the translation skill reads on every run. It selects, for each keyword, one preferred rendering for the track from the menu of attested options in the consolidated bilingual glossary — using the track's `requirements.md` as the selection rubric. Where no attested rendering meets the requirements, it derives a new rendering from the keyword's Local-Wiki article and records the new rendering both in this per-track bilingual glossary and back into the consolidated bilingual glossary under `2-RAILS/Bilingual-Glossaries/`.

This is the only skill in the rails workflow that introduces target-language vocabulary into the project. Every other skill catalogues what already exists; this one chooses.

---

## Inputs

- **Track folder** — `3-TRANSFORMATIONS/Translation/<track-name>/`. The folder must already contain `requirements.md`. If it doesn't, run the `requirements-author` skill first (or write it manually) — selection cannot proceed without a rubric.
- **Consolidated bilingual glossary** — `2-RAILS/Bilingual-Glossaries/<source-lang>-<target-lang>.md` for the track's language pair.
- **Local-Wiki articles** — `2-RAILS/Local-Wiki/*.md`, consulted whenever no attested rendering satisfies the requirements.

## Output

Two artefacts:

1. **Per-track bilingual glossary** at:

   ```
   3-TRANSFORMATIONS/Translation/<track-name>/bilingual glossary.md
   ```

   One row per keyword, one chosen rendering per row, with the rationale recorded.

2. **Updates to the consolidated bilingual glossary** at `2-RAILS/Bilingual-Glossaries/<source-lang>-<target-lang>.md` for any new renderings this skill introduces — added as a new row in the keyword's rendering table with source `<track-name>` and frequency `0` (until the translation actually attests it).

If the per-track bilingual glossary already exists, update in place — preserve manually adjusted rationales unless the underlying consolidated bilingual glossary has changed.

---

## Output file format (per-track bilingual glossary)

```markdown
---
track: <track-name>
language_pair: <pi-en | pi-bn | ...>
source_language: <pi | sa | bo | zh>
target_language: <en | bn | sin | ...>
requirements: 3-TRANSFORMATIONS/Translation/<track-name>/requirements.md
consolidated_glossary: 2-RAILS/Bilingual-Glossaries/<source-lang>-<target-lang>.md
total_keywords: <count>
last_updated: <ISO date>
status: draft
---

# Translation bilingual glossary — <track-name>

| <source-lang keyword> | Chosen rendering | Origin | Rationale |
|-----------------------|------------------|--------|-----------|
| <keyword> | <rendering> | attested / derived | <one-line note pointing to the requirements clause or Local-Wiki article that decided it> |

## Notes on derivations

### <keyword>

<paragraph explaining why no attested rendering satisfied the requirements
and how the new rendering was derived from the Local-Wiki article. Cite
the Local-Wiki article and the requirements clause that drove the choice.>

(2-RAILS/Local-Wiki/<keyword>.md)
(3-TRANSFORMATIONS/Translation/<track-name>/requirements.md)
```

The main artefact is the table. The **Notes on derivations** section only contains entries for keywords with `Origin: derived` — attested selections need no extra prose.

---

## Rules

1. **Attested first, derived only when forced.** If any attested rendering in the consolidated bilingual glossary meets the requirements, prefer it. Derive a new rendering only when none does.
2. **One rendering per keyword.** This is a working bilingual glossary, not a thesaurus. If the track requires different renderings for different senses of one source keyword, treat them as two keywords with sense disambiguators (`kusala (wholesome)`, `kusala (skill)`) — matching the sense splits in the consolidated bilingual glossary.
3. **The rationale column is mandatory.** Every chosen rendering carries a one-line note that points to the part of `requirements.md` (or the Local-Wiki article, for derivations) that justifies the choice. The translation skill reads the rationale to decide edge cases.
4. **Derivations write back to the rails.** Any new rendering introduced by this skill is added to the consolidated bilingual glossary as a new row, source `<track-name>`, frequency `0`. This keeps the consolidated bilingual glossary a complete record of every rendering ever used or proposed for the language pair.
5. **No silent overrides.** If the requirements demand a rendering that the Local-Wiki article would not support (because the article documents the term differently), flag the conflict in the **Notes on derivations** section rather than silently overriding either source.
6. **Diacritics and script preserved.** Source-language keywords in the table use the same form as the consolidated bilingual glossary; target-language renderings use the script declared in `requirements.md`.

---

## Procedure

1. **Read `requirements.md`.** Note: the target register, the preferred-rendering directives, the style constraints, and any explicit term mappings. Treat directives as hard constraints; treat the rest as soft preferences.
2. **Read the consolidated bilingual glossary** for the track's language pair. The list of `##` headings is the working keyword set.
3. **For each keyword:**
   - Look at the rendering table. Sorted by total frequency descending, the top row is the default candidate.
   - Apply the requirements: does the top row satisfy register, the style constraints, and any explicit directives? If yes, select it.
   - If not, walk down the table to the next rendering that does. Select it. Note in the rationale why the more frequent rendering was rejected.
   - If no row satisfies the requirements, open the Local-Wiki article (`2-RAILS/Local-Wiki/<keyword>.md`). Read the Contextual definition and the Attestations. Derive a target-language rendering that captures the term's sense as documented and that meets the requirements. Mark the row `Origin: derived` and add a paragraph to **Notes on derivations**.
4. **Write back the new renderings** to the consolidated bilingual glossary as new rows (source = track name, frequency = 0). This step requires editing `2-RAILS/Bilingual-Glossaries/<pair>.md`. Set the per-keyword row order on re-sort by total frequency descending; the new row with frequency 0 lands at the bottom of its keyword's table.
5. **Write the per-track bilingual glossary** to `3-TRANSFORMATIONS/Translation/<track-name>/bilingual glossary.md`. Set `total_keywords` and `last_updated`. Set `status: draft`.

---

## Re-running this skill

The per-track bilingual glossary is regenerated whenever:

- `requirements.md` changes (e.g. register adjusted, new explicit term mapping added).
- The consolidated bilingual glossary gains new sources (e.g. a fresh `glossary-extract-raw` run added more attested renderings).
- A translation pass introduces a new rendering on the fly (the translation skill records it in the per-track bilingual glossary; the next `glossary-select` run promotes it back to the consolidated bilingual glossary).

In each case the existing per-track bilingual glossary is read first so manually edited rationales are preserved where the underlying selection still holds.

---

## Completion check

- [ ] Every keyword in the consolidated bilingual glossary appears as a row, or has a documented reason for exclusion in **Notes**
- [ ] Every row has an `Origin` (attested / derived) and a rationale
- [ ] Every `derived` row has a paragraph in **Notes on derivations** citing the Local-Wiki article and the requirements clause
- [ ] Every new derived rendering is written back to `2-RAILS/Bilingual-Glossaries/<pair>.md`
- [ ] Sense splits in the consolidated bilingual glossary are preserved in the per-track bilingual glossary
- [ ] Target-language renderings use the script declared in `requirements.md`
- [ ] Frontmatter `requirements` and `consolidated_glossary` paths resolve
