---
name: rails-to-verse-translation
description: >
  Translate a batch of BCA verses into metrical or rhymed verse in any target
  language, working from `2-RAILS/Verses/<id>-summary.md` packages rather than
  the bare root line. Derives the style contract from whatever partial
  translation already exists in that language, builds a locked termbase from
  the rails' `གནད་ཚིག` key-term tables, resolves every `⚑` commentary
  divergence to the broadest attested reading, and records the alternatives in
  a divergence log. Produces a full track (requirements, audience, termbase,
  divergence log, verse file) plus optional block-ID-stamped append into an
  existing translation file. Use when the user asks to translate verses into
  poetry/verse for a language track, continue an existing verse translation,
  build a termbase from rails, or add verses to a partial poetic translation.
---

# rails-to-verse-translation

Produces verse-form translations of the *Bodhisattvacaryāvatāra* that are **rail-grounded rather than root-grounded**. The raw root line is terse and frequently ambiguous; the verse rail's `བསྡུས་དོན།` synthesis carries the commentators' disambiguated reading, their key-term glosses, and their explicit disagreements. Translating from the synthesis produces verses with content the bare root line does not state — attested similes, the referents of pronouns, the scope of technical terms.

This skill exists to prevent four specific failures: (1) inventing imagery to complete a rhyme, (2) rendering the same Tibetan lemma two different ways across a chapter, (3) silently flattening a commentary divergence by picking one reading and losing the rest, and (4) breaking Obsidian block references by misplacing block IDs.

Correct output is a verse batch where every image traces to a rail citation, every locked term renders identically throughout, every `⚑` is logged with the reading taken and the readings dropped, and the verse file passes `scripts/lint_verses.py` with zero errors.

---

## Inputs

Gather all of the following before starting. If any is missing, stop and ask the human contributor — do not guess.

| Input | Description | Example |
|---|---|---|
| `verse-range` | The chapter and verse span to translate | `2-25 to 2-50` |
| `target-language` | Language and its `lang_tag` | Hindi, `hi` |
| `track-name` | Folder name under `3-TRANSFORMATIONS/Translations/` | `hi-poetic` |
| `style-source` | An existing partial translation in this language whose form the new verses must match, **or** an explicit statement that none exists | `1-SOURCES/Translations/translation-ai/bca-hi-poetic.md` (verses 1-1 to 2-24) |
| `append-target` | The file to append finished verses to, or `none` | `1-SOURCES/Translations/translation-ai/bca-hi-poetic.md` |
| `divergence-policy` | How to resolve `⚑`: broadest reading, single-commentary tiebreaker, or ask per case | broadest + log |
| `doc-language` | Language for `requirements.md` / `audience.md` / `divergence-log.md` | English |

Required source files, all of which must exist:

- `2-RAILS/Verses/<chapter>-<verse>-summary.md` for every verse in range
- `1-SOURCES/Translations/bo-བློ་ལྡན་ཤེས་རབ།.md` — Tibetan root, the basis of meaning
- `1-SOURCES/Text/BCAV08_SH_sk.md` — Sanskrit, for disambiguation
- Human translations for triangulation: `en-Padmakara_2006.md`, `en-Wallace.md`, `en-David_Karma_Choephel.md`

---

## Output

Track folder `3-TRANSFORMATIONS/Translations/<track-name>/`:

| Path | Contents |
|---|---|
| `requirements.md` | Style contract derived from `style-source` |
| `audience.md` | Reader profile: prior knowledge, use cases, tone |
| `termbase.md` | One locked target-language rendering per lemma, each citing a rail |
| `divergence-log.md` | Every `⚑`: reading taken, readings dropped, rail citations |
| `Chapter-NN-verses-A-B.md` | The verses, with `context_packages:` frontmatter |

If `append-target` is not `none`, the verses are also appended there and block IDs stamped across the whole file.

---

## Output file format

The verse file:

```markdown
---
title: "<work title> — <chapter/verse range> (<language> verse translation)"
transformation_type: translation
track: <track-name>
lang_tag: <tag>
language: <language>
status: draft
covers_verses: "<A>–<B>"
contracts:
  - 3-TRANSFORMATIONS/Translations/<track-name>/requirements.md
  - 3-TRANSFORMATIONS/Translations/<track-name>/audience.md
  - 3-TRANSFORMATIONS/Translations/<track-name>/termbase.md
context_packages:
  - 2-RAILS/Verses/<id>-summary.md      # one line per verse in range
rails_status_note: "<if any rail is not status: complete, record the human approval that authorised generation>"
divergence_log: 3-TRANSFORMATIONS/Translations/<track-name>/divergence-log.md
---

# <chapter heading in target language>

**(<verse number in target-language numerals>)**
<line 1, trailing space>
<line 2, trailing space>
<line 3, trailing space>
<line 4><terminal mark>
```

The termbase table shape — the gloss column is mandatory so a reader who knows neither script can audit it:

```markdown
| Tibetan lemma | Locked <language> | Gloss | Rail source |
|---|---|---|---|
| སྡིག་པ | **<rendering>** † | misdeed / sin | 2-28, 2-32, 2-37 |
```

`†` = already used in `style-source`, locked for continuity. `⚑` = commentators diverge, see divergence log.

The divergence log entry shape — one block per `⚑`:

```markdown
## <verse-id> — <lemma or phrase> (<gloss>)

| Commentary | Reading | In the verse? |
|---|---|---|
| <ids> | <the wide reading> | **✓ taken** |
| <ids> | <the narrow reading> | ✗ dropped (too narrow) |

**<language>:** `<the rendered line>`
Source: `2-RAILS/Verses/<id>-summary.md`
```

---

## Rules

1. **Translate from the rail synthesis, not the root line.** The `བསྡུས་དོན།` section is the semantic source. The root line fixes syntax and verse boundaries.
2. **The English translations are witnesses only.** Where all agree, a reading is confirmed; where they split, the rail decides. Never translate from the English.
3. **Verify witness alignment before relying on a witness.** Verse numbering in the human translations can be offset (Wallace is missing 2-32 and shifts by one from 2-33 onward). Check, and record any offset in the divergence log.
4. **Build the termbase before translating the first verse.** Extract from every `གནད་ཚིག` table in range, then cross-check against `style-source` so pre-existing renderings win. Renderings are append-only: never silently change a locked form.
5. **No synonyms for locked lemmas.** A new rendering requires a termbase entry first.
6. **Add nothing absent from the rail.** Not for rhyme, not for metre, not for flow. Rhyme is subordinate to meaning. No parametric knowledge — no story, name, number, or taxonomy from the model's own memory.
7. **Never add, drop, merge, or split verses.** One verse in the root is one verse in the target.
8. **Resolve every `⚑` per `divergence-policy` and log it.** Never reconcile two readings by cramming both into one line. Exception: if the rail itself states two glosses are complementary rather than contradictory, both may be carried — say so in the log.
9. **Prefer the accessible reading over the technical one** when both are attested and the audience profile lacks the background. Log the dropped technical reading.
10. **Batch 5–6 verses per pass.** Each pass receives the trailing 3 verses of the previous pass as a metre and register anchor. Longer batches degrade prosody.
11. **Block IDs attach to the verse's final line**, same line, no blank line before them. An ID separated by a blank line becomes its own block and silently breaks every `![[file#^id]]` transclusion pointing at it.
12. **All output stays `status: draft`.** Only a human subject-matter expert sets `complete`.
13. **Respect `1-SOURCES/` write permissions.** Only block IDs, frontmatter, navigation links, and `[Ed:...]` notes may be added there (CLAUDE.md §6). Appending a translation into a `1-SOURCES/` file requires explicit human approval — record it in frontmatter.
14. **If any rail in range is not `status: complete`, stop and ask.** CLAUDE.md §9 forbids generating from incomplete rails. Proceed only on explicit human approval, and record that approval in `rails_status_note:`.

---

## Procedure

### Step 1 — Pre-flight

1. Confirm every `2-RAILS/Verses/<id>-summary.md` in range exists. Report any gap and stop.
2. Read the `status:` field of each. If any is not `complete`, stop and ask for approval per Rule 14.
3. Confirm the verse count in range matches the root text (`grep -o "\^<ch>-[0-9]*"` on the Tibetan file). A chapter may run past where the rails stop.
4. Verify witness alignment per Rule 3 at three sample points.

### Step 2 — Derive the style contract

1. Read `style-source` and extract, by observation rather than assumption:
   a. lines per verse
   b. rhyme scheme and how strictly it is kept
   c. caesura position
   d. line-ending whitespace and terminal marks
   e. verse-number format and whether numbering restarts per chapter
   f. register: which loanwords appear, how technical terms are handled, whether glosses are parenthesised
   g. spelling variants already in use — including inconsistencies between chapters
2. Write `requirements.md` and `audience.md` in `doc-language`. If `doc-language` differs from the target language, record why in a `doc_language_note:` field — CLAUDE.md §9 expects the target language.

### Step 3 — Extract rails context

Run:

```
python3 4-SYSTEM/Skills/rails-to-verse-translation/scripts/extract_rails_context.py \
    --range <A>-<B> --batch-size 6 --out <workdir>
```

This writes one bundle per batch, each verse carrying: Tibetan root, Sanskrit, the witnesses, the rail synthesis, the key-term table, and the divergence block. Report any verse whose rail is missing a section.

### Step 4 — Build the termbase

1. Aggregate every `གནད་ཚིག` row in range; group by lemma; note where a lemma has multiple conflicting glosses (these are the `⚑` candidates).
2. Cross-check each proposed rendering against `style-source`. A rendering already in use there wins — mark it `†`.
3. Check for collisions: a word already used in `style-source` in a *different* sense must not be reused.
4. Write `termbase.md` with the gloss column per the format above, plus a note under each `⚑` lemma explaining which reading was locked and why.

### Step 5 — Translate, batch by batch

For each batch of 5–6:

1. Load the batch bundle, `termbase.md`, `requirements.md`, and the trailing 3 verses already written.
2. For each verse: read the synthesis → identify locked lemmas → resolve any `⚑` → compose to the derived form.
3. Before moving on, self-check each verse against Rules 5, 6, 7, and the derived line/rhyme shape.
4. Append the batch to the verse file. Do not proceed to the next batch until the current one is written.

### Step 6 — Write the divergence log

One block per `⚑`, per the format above. Include a count of how many divergences actually changed the rendering versus how many were structural or orthographic with no effect. Close with translator's notes on witness limitations and any rail incompleteness found.

### Step 7 — Lint

```
python3 4-SYSTEM/Skills/rails-to-verse-translation/scripts/lint_verses.py \
    --file <verse-file> --termbase <termbase> --range <A>-<B>
```

Fix every reported error and re-run until clean.

### Step 8 — Fidelity audit

Dispatch a subagent to check each verse against its rail for **additions** (content not in the rail) and **omissions** (load-bearing elements dropped). Instruct it to return only flagged verses with severity, not praise or summary. Fix what it finds, then re-run Step 7.

### Step 9 — Append and stamp (only if `append-target` is not `none`)

1. Confirm human approval if the target is in `1-SOURCES/` (Rule 13).
2. Back up the target file.
3. Append the verses, preserving the target's existing verse-number format.
4. Stamp block IDs:

```
python3 4-SYSTEM/Skills/rails-to-verse-translation/scripts/stamp_block_ids.py \
    --file <append-target> --numerals <devanagari|latin|tibetan>
```

5. Confirm the script's report: IDs contiguous per chapter, none orphaned, none duplicated, verse text unchanged apart from the added IDs.

---

## Completion check

- [ ] Every rail in range exists; any non-`complete` status was approved and is recorded in `rails_status_note:`
- [ ] Witness alignment verified; any numbering offset recorded in the divergence log
- [ ] `requirements.md` derived from `style-source` by observation, not assumption
- [ ] `audience.md` states prior knowledge, use cases, and tone
- [ ] `termbase.md` covers every lemma in range, has a gloss column, and marks `†` continuity and `⚑` divergences
- [ ] Verse file has correct frontmatter with one `context_packages:` line per verse
- [ ] Verse count equals the range; no verse added, dropped, merged, or split
- [ ] Every `⚑` in range appears in `divergence-log.md` with reading taken and readings dropped
- [ ] `lint_verses.py` passes with zero errors
- [ ] Fidelity audit run; all critical and major findings resolved
- [ ] If appended: backup taken, block IDs attached to verse-final lines, contiguous, no orphans, no duplicates
- [ ] All outputs `status: draft`
