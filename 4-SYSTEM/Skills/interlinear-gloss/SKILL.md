---
name: interlinear-gloss
description: For one root text + one translation, build an interlinear gloss file at 2-RAILS/Bilingual-Glossaries/Raw/<source>-<target>-gloss.md. Each verse becomes a ```gloss``` block in the Obsidian Interlinear Glossing plugin format (\gla / \glb / \ex), pairing source tokens against token-by-token target glosses and the translator's free translation. Run once per translation. The output is what glossary-extract-raw reads to catalogue keyword renderings.
---

# interlinear-gloss

This skill creates the **interlinear gloss file** that pairs one root text against one translation, verse by verse. Each verse is rendered as a three-line `gloss` block:

- `\gla` — source-language tokens (Pali, in PTS Roman diacritics). Long compounds may be split into their component parts when that helps the alignment.
- `\glb` — token-by-token gloss in the target language, one entry per `\gla` token, lined up by position. **Every word used in `\glb` must come verbatim from the translator's `\ex` line — do not introduce new terminology or paraphrase.**
- `\ex` — the translator's free translation of the verse, verbatim from the translation file.

A gloss block is the **token-level alignment** that all downstream bilingual glossary work depends on. `glossary-extract-raw` reads these files to find keyword renderings; `local-wiki-article` cites them when documenting how a term is rendered across translations; `glossary-select` consults them when judging whether an attested rendering meets a track's requirements.

This skill is run **once per translation**. Four translations → four gloss files.

---

## Inputs

- **Root text** — `1-SOURCES/Text/<root-text>.md` (e.g. `pi-dhammasangani.md`).
- **Translation** — one file from `1-SOURCES/Translations/<translation>.md`. Must be block-aligned with the root text (same `^block-id` scheme).

## Output

One file at:

```
2-RAILS/Bilingual-Glossaries/Raw/<source-lang>-<target-lang-tag>-gloss.md
```

`<source-lang>` is the root text's `lang_tag` (`pi` for Dhammasaṅgaṇī).
`<target-lang-tag>` is the translation's `lang_tag` exactly (e.g. `en-rd` for the Rhys Davids translation, `en` for the modern English, `bn`, `sin`).

Examples:

| Translation | Output file |
|---|---|
| `en-dhammasangani-rd.md` (lang_tag `en-rd`) | `2-RAILS/Bilingual-Glossaries/Raw/pi-en-rd-gloss.md` |
| `en-dhammasangani.md` (lang_tag `en`) | `2-RAILS/Bilingual-Glossaries/Raw/pi-en-gloss.md` |
| `bn-dhammasangani.md` (lang_tag `bn`) | `2-RAILS/Bilingual-Glossaries/Raw/pi-bn-gloss.md` |
| `sin-dhammasangani.md` (lang_tag `sin`) | `2-RAILS/Bilingual-Glossaries/Raw/pi-sin-gloss.md` |

If the file already exists, update in place: keep manually filled `\glb` lines, and only refresh `\gla` and `\ex` from the underlying source files (so re-running this skill after the root text or translation is re-formatted does not lose token-gloss work).

---

## Output file format

```markdown
---
source_file: 1-SOURCES/Text/<root-text>.md
source_language: <pi>
target_file: 1-SOURCES/Translations/<translation>.md
target_language: <en | bn | sin | ...>
target_lang_tag: <en-rd | en | bn | sin | ...>
translator: <from the translation's frontmatter>
total_verses: <count of gloss blocks>
status: draft
---

# Interlinear gloss — <source-lang> → <target-lang> (<translator short name>)

## ^<block-id>

`​`​`​gloss
\gla    <source token 1>   <source token 2>   <source token 3>   ...
\glb    <target gloss 1>   <target gloss 2>   <target gloss 3>   ...
\ex     <free translation, verbatim from the translation file>
`​`​`

## ^<next block-id>

`​`​`​gloss
...
`​`​`
```

One `##` heading per verse block, using the block ID with the caret. One `gloss` code block per `##` heading. Verse order matches root-text order.

---

## Format rules — Obsidian Interlinear Glossing plugin

The plugin (`Interlinear Glossing` by the Obsidian community) renders ```` ```gloss ```` blocks as aligned columns where every token on the `\gla` line lines up with the token at the same position on `\glb`. For the rendering to be correct:

1. **One token per column.** Splitting is by whitespace on the `\gla` line. The number of whitespace-separated tokens on `\glb` must match `\gla` exactly.
2. **Compounds may be split on `\gla`.** When a Pali compound is long enough that splitting it produces a cleaner alignment, write its parts as separate space-separated tokens on `\gla` (and add the corresponding gloss cells on `\glb`). For short or familiar compounds, keep them as a single token.
3. **Multi-word concepts are joined with hyphens, not spaces.** If "having paid homage" glosses a single Pali token, write it as `having-paid-homage` on `\glb` so it occupies one column.
4. **Missing glosses and particles use `--`, never the Pali original.** When no word in `\ex` corresponds to a `\gla` token (common for particles like *kho*, *pana*, *ca* when they are not translated or are folded into another word), write `--`. Never copy the Pali token itself into `\glb` as a fallback — a Pali word in `\glb` looks like a gloss but is not one, and it corrupts downstream glossary extraction.
5. **No trailing punctuation on `\gla`.** Period, comma, semicolon, question mark — strip from the token. They re-appear in the `\ex` line via the translation.
6. **`\ex` is verbatim from the translator.** Do not paraphrase, do not normalise punctuation, do not strip footnote markers. This line is what `glossary-extract-raw` reads as the canonical rendering of the verse.
7. **`\glb` draws exclusively from `\ex` — no exceptions.** Every `\glb` cell must be a word (or hyphen-joined phrase) whose component words all appear verbatim in the `\ex` line for that same block. This means: no synonyms, no paraphrases, no knowledge-based translations, and no Pali originals. The only permitted departure is `--`. When the translator's wording does not map cleanly to a source token, `--` is the correct and complete answer — it honestly records the gap rather than filling it with an invented equivalent.

   **Example 1** — `\ex States that are good, bad, indeterminate.`

   | `\gla` | correct `\glb` | wrong `\glb` |
   |---|---|---|
   | `kusalā` | `good` | `wholesome` ← not in `\ex` |
   | `dhammā` | `states` | `states` ✓ |
   | `akusalā` | `bad` | `unwholesome` ← not in `\ex` |
   | `dhammā` | `states` | `states` ✓ |
   | `abyākatā` | `indeterminate` | `indeterminate` ✓ |
   | `dhammā` | `states` | `states` ✓ |

   **Example 2** — Handling particles and split concepts.
   `\ex States that are dissociated from ties; but may or may not be favourable to ties.`

   | `\gla` | correct `\glb` | wrong `\glb` |
   |---|---|---|
   | `ganthavippayuttā` | `dissociated-from-ties` | `dissociated-from-ties` ✓ |
   | `kho` | `but` | `but` ✓ |
   | `pana` | `--` | `pana` ← never copy Pali |
   | `dhammā` | `states` | `states` ✓ |
   | `ganthaniyāpi` | `may-be-favourable-to-ties` | `may-or-may-not-be-favourable-to-ties` ← column mismatch |
   | `aganthaniyāpi` | `may-not-be-favourable-to-ties` | `--` ← less precise |

---

## Procedure

The recommended path is the scaffold helper followed by an LLM pass for the `\glb` line.

1. **Run the scaffold script:**

   ```bash
   python3 4-SYSTEM/Skills/interlinear-gloss/scripts/scaffold_gloss.py \
       1-SOURCES/Text/pi-dhammasangani.md \
       1-SOURCES/Translations/en-dhammasangani-rd.md \
       2-RAILS/Bilingual-Glossaries/Raw/pi-en-rd-gloss.md
   ```

   The script aligns blocks by `^block-id`, emits one `##` heading per paired block, and scaffolds each `gloss` block with `\gla` populated from the source tokens and `\ex` populated verbatim from the translation. The `\glb` line is scaffolded with `--` placeholders at the right column count.

2. **Spot-check the scaffold.** Confirm: every block in the source has a matching `##` heading; `\gla` tokens look clean (no stray punctuation); the `\ex` line matches the translation file's body. The frontmatter `total_verses` matches the heading count.

3. **Fill `\glb`, verse by verse or in batches.** This is the LLM-driven half. The procedure for each cell is:
   a. Read the `\ex` line for the block.
   b. Find the word or phrase in `\ex` that most directly corresponds to this `\gla` token. Use only words that appear verbatim in `\ex`; join multi-word phrases with hyphens.
   c. If no word in `\ex` corresponds to this token, write `--`. Do not substitute the Pali token, do not use a synonym, do not use background knowledge of what the Pali means.
   - Where a scaffold token on `\gla` is a long compound that would be clearer split, replace the single compound token with its space-separated parts and extend `\glb` with one cell per part.
   - For particles like *kho pana*, if only one word in `\ex` (like "but") covers the pair, assign it to the first and use `--` for the second.
   - If a phrase in `\ex` maps to multiple Pali words (like "may or may not be..." mapping to `ganthaniyāpi aganthaniyāpi`), split the phrase across the tokens to maintain one-to-one alignment.

4. **Verify column count.** Run the scaffold script with `--validate` to re-check that `\glb` has the same number of whitespace-separated tokens as `\gla` for every block:

   ```bash
   python3 4-SYSTEM/Skills/interlinear-gloss/scripts/scaffold_gloss.py \
       --validate 2-RAILS/Bilingual-Glossaries/Raw/pi-en-rd-gloss.md
   ```

5. **Set `status: draft`.** A domain specialist marks the file `complete` after review.

---

## Re-running this skill

The scaffold script can be re-run safely:

- Existing `\glb` lines are preserved if their token count still matches `\gla` after the source text is re-read.
- If the source text was re-formatted (e.g. a verse was retokenised), the affected `\glb` lines are reset to `--` placeholders and the change is flagged in stderr so you can review.
- `\gla` and `\ex` are always refreshed from the underlying source files.

---

## How downstream skills consume this file

- `glossary-extract-raw` walks every `gloss` block in this file, pairs `\gla` tokens against `\glb` cells, and records every distinct `(source-token, target-gloss)` rendering. Frequencies are counts of distinct verses where the rendering occurs.
- `glossary-combine` does not read this file directly — it works on the rendering tables that `glossary-extract-raw` produces.
- `local-wiki-article` may transclude individual gloss blocks (`![[pi-en-rd-gloss.md#^1-15]]`) when documenting how a term is rendered across translations.
- `verse-context` may transclude a gloss block as part of the Commentary passages section for the verse, when token-level renderings clarify a reading.

---

## Completion check

- [ ] One `##` heading per source-text block, in source order
- [ ] One `gloss` code block per `##` heading
- [ ] `\gla`, `\glb`, `\ex` all present in every block
- [ ] Token count matches across `\gla` and `\glb` for every block (use `--validate`)
- [ ] `\ex` is verbatim from the translation file
- [ ] Frontmatter `total_verses` matches the heading count
- [ ] No 