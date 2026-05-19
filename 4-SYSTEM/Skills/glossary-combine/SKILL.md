---
name: glossary-combine
description: Merge every raw per-source bilingual glossary in 2-RAILS/Bilingual-Glossaries/Raw/ that shares one language pair into a single consolidated bilingual glossary at 2-RAILS/Bilingual-Glossaries/<source-lang>-<target-lang>.md. Each keyword's row shows every attested rendering, side by side, with the source that uses it and a frequency count. This is what glossary-select reads.
---

# glossary-combine

This skill takes the raw bilingual glossaries that `glossary-extract-raw` produced — one per translation source — and merges them into a single **consolidated bilingual glossary** per language pair. The consolidated file is descriptive: it tells you, for each source-language keyword, every distinct rendering attested across the corpus and which sources use which rendering.

The consolidated bilingual glossary is the menu that `glossary-select` chooses from when building a per-track bilingual glossary.

---

## Inputs

- **Language pair** — e.g. `pi-en`, `pi-bn`, `pi-sin`. Determines which raw files to merge.
- **Raw bilingual glossaries** — all files under `2-RAILS/Bilingual-Glossaries/Raw/` whose `language_pair` frontmatter field matches the requested pair.

## Output

One file at:

```
2-RAILS/Bilingual-Glossaries/<source-lang>-<target-lang>.md
```

(e.g. `2-RAILS/Bilingual-Glossaries/pi-en.md`). If the file exists, regenerate it from the current raw inputs — manual edits to the consolidated file are discouraged; consolidate from raw instead.

---

## Output file format

```markdown
---
language_pair: <pi-en | pi-bn | ...>
source_language: <pi | sa | bo | zh>
target_language: <en | bn | sin | ...>
raw_sources:
  - 2-RAILS/Bilingual-Glossaries/Raw/<source-name>.md
  - 2-RAILS/Bilingual-Glossaries/Raw/<source-name>.md
total_keywords: <count>
total_distinct_renderings: <count>
generated: <ISO date>
status: draft
---

# Consolidated bilingual glossary — <source-language> → <target-language>

## <source-lang keyword>

| Rendering | Sources | Total frequency | Local-Wiki |
|-----------|---------|-----------------|------------|
| <rendering A> | <src-1> (n), <src-2> (n) | <sum> | [[<term>]] |
| <rendering B> | <src-3> (n) | <n> | [[<term>]] |

---

## <next keyword>

...
```

One `##` heading per keyword. Renderings within a keyword are sorted by total frequency descending — the most widely attested rendering at the top. Keywords are sorted alphabetically (by source-language form, diacritics preserved).

The **Local-Wiki** column links to the Local-Wiki article for the term, if one exists. The link is the same for every row of the keyword's table (it's a property of the keyword, not the rendering). If no Local-Wiki article exists, leave the cell as `—`.

---

## Rules

1. **One file per language pair.** Never mix pairs. `pi-en` is its own file, separate from `pi-bn`.
2. **Regenerate, don't edit.** The consolidated file is a derived artefact. If the data is wrong, fix the raw bilingual glossary, then re-run this skill. Manual edits get overwritten.
3. **Frequencies are summed across sources.** If three sources each use the rendering "states" five times, the total is 15. The `Sources` column makes the per-source breakdown visible.
4. **Renderings that differ only in capitalisation are merged.** `"states"` and `"States"` become one row. Renderings that differ in punctuation or footnote markers are also merged.
5. **Renderings that differ in glossing strategy are not merged.** `"states"` and `"phenomena (dhammā)"` are two distinct renderings — the second carries a transliteration the first does not.
6. **Local-Wiki link is populated automatically.** If `2-RAILS/Local-Wiki/<keyword>.md` exists, link to it. If not, leave `—`. Do not create the Local-Wiki article from this skill — that's the `local-wiki-article` skill's job.

---

## Procedure

The recommended path uses the helper script under `scripts/` followed by an LLM pass for sense-disambiguation edge cases.

1. **Run the merge script:**

   ```bash
   python3 4-SYSTEM/Skills/glossary-combine/scripts/combine_glossaries.py \
       pi-en \
       2-RAILS/Bilingual-Glossaries/Raw/ \
       2-RAILS/Bilingual-Glossaries/pi-en.md
   ```

   The script reads every raw bilingual glossary with `language_pair: pi-en`, merges renderings by keyword, sums frequencies, sorts, and writes the consolidated file with frontmatter.

2. **Spot-check sense splits.** Some source keywords have multiple senses in the commentary tradition, and renderings cluster by sense. For example, *kusala* (wholesome) and *kusala* (skill) may both appear; the renderings "wholesome / skilful" partly map to one sense and "good / virtuous" to the other. Where this matters and a sense-split Local-Wiki article exists, split the consolidated keyword heading into two: `## kusala (wholesome)` and `## kusala (skill)`, assigning each rendering row to the right one. The script will not do this automatically — the disambiguator is in the Local-Wiki, not the raw bilingual glossaries.

3. **Verify Local-Wiki links.** For each keyword, confirm that the linked Local-Wiki article (if any) actually documents the senses present in the rendering table. If not, either add a stub or split the keyword.

4. **Set `status: draft`.** A domain specialist marks the file `complete` after review.

---

## Combiner script

`scripts/combine_glossaries.py` reads the raw bilingual glossaries with the requested `language_pair`, walks each `##` heading (one per keyword) and its rendering table, merges them, and writes the consolidated output. It does not invent renderings, it does not invent sense splits, and it does not invent Local-Wiki links — those come from existing files.

Run with `--check` to dry-run: the script reports the keyword count and the distinct-rendering count without writing.

```bash
python3 4-SYSTEM/Skills/glossary-combine/scripts/combine_glossaries.py \
    pi-en \
    2-RAILS/Bilingual-Glossaries/Raw/ \
    /tmp/pi-en.md --check
```

---

## Completion check

- [ ] Frontmatter lists every raw file consumed in `raw_sources`
- [ ] `total_keywords` matches the number of `##` headings
- [ ] Renderings within each keyword are sorted by total frequency descending
- [ ] Keywords are sorted alphabetically with diacritics preserved
- [ ] Capitalisation-only duplicates have been merged
- [ ] Sense splits (where they matter) are reflected in separate `##` headings, with the Local-Wiki article for each sense linked
- [ ] Local-Wiki column is `—` for keywords with no article — not blank, not an empty link
