---
name: translate-zero-shot
description: >
  Zero-shot translation of the Bodhisattvacaryāvatāra from the Tibetan source
  (bo-བློ་ལྡན་ཤེས་རབ།.md), disambiguated by the Sanskrit root text
  (BCAV08_SH_sk.md) and triangulated per verse against three block-aligned
  human translations, into a localized audience track (children, plain, or
  scholar) when 2-RAILS/ verse packages are not yet complete. Builds the
  termbase empirically from attested renderings at each block ID, translates
  chapter by chapter, and merges into a full-text file with a bundled script.
  Use when the user asks for zero-shot translation, translate from
  Tibetan/Sanskrit sources, localize children-audience (or plain/scholar) for
  a target language, translate BCA by chapter, or merge chapter translation
  chunks.
---

# translate-zero-shot

Produces a full *Bodhisattvacaryāvatāra* translation track directly from `1-SOURCES/` when `2-RAILS/Verses/<verse-id>-summary.md` packages are not yet `status: complete`.

**Method: evidence-based triangulation.** Every decision is backed by something checkable at the exact verse, never by a pre-built table or parametric knowledge:

- **Meaning** — the Tibetan translation is the primary source; the Sanskrit root text resolves ambiguity (homonyms, pāda breaks, philosophical terms); three block-aligned human translations are compared at the same block ID. Consensus among them confirms a reading; divergence among them marks genuine ambiguity — check the Sanskrit and flag.
- **Terminology** — the termbase is built empirically as translation proceeds: when a key term first appears, its attested renderings are read from the aligned translations *at that block ID*, one is chosen for the track register, and appended with the verse citation as rationale. No glossary seeding.
- **Register** — from the track's existing `requirements.md` / `audience.md`, which are read, never overwritten.

Output matches the vault's transformation conventions: `requirements.md` / `audience.md` / `termbase.md`, one `Chapter-NN.md` per chapter, then one merged full-text file.

**Reference examples (this vault):**
- Track contracts: `3-TRANSFORMATIONS/Translations/en-plain-english/` (`requirements.md`, `audience.md`, `termbase.md`)
- Merged full-text outputs: `3-TRANSFORMATIONS/Translations/en-translate/BCA-Full-Children-English.md`, `BCA-Full-Plain-English.md`, `BCA-Full-Scholar-English.md`

---

## Inputs

| Input | Required | Description |
|---|---|---|
| **Target language** | ✓ | ISO-style code or short name, e.g. `en`, `hi`. Determines track folder prefix. |
| **Audience level** | ✓ | `children`, `plain`, or `scholar`. Determines register and track suffix. |
| **Chapter scope** | optional | Single chapter (`3`), range (`1-3`), or `all` (default: `all` = chapters 1–10). |
| **Merge** | optional | `yes` (default) or `no`. When `yes`, run merge after all requested chapters exist. |

If target language or audience level is missing, ask before proceeding.

### Fixed source files (this vault)

| Role | Path |
|---|---|
| Tibetan primary | `1-SOURCES/Translations/bo-བློ་ལྡན་ཤེས་རབ།.md` |
| Sanskrit reference | `1-SOURCES/Text/BCAV08_SH_sk.md` |

### Triangulation set (block-aligned with the Tibetan source)

The default set — always loaded, all three, for every chapter:

| Witness | Path |
|---|---|
| W1 | `1-SOURCES/Translations/en-Padmakara_2006.md` |
| W2 | `1-SOURCES/Translations/en-Wallace.md` |
| W3 | `1-SOURCES/Translations/en-David_Karma_Choephel.md` |

For non-English targets, additionally load block-aligned translations in the target language when they exist (e.g. `zh-隆蓮法師.md` and other `zh-*` files; `hi-बोधिचर्यावतारः.md`) — these take precedence for terminology evidence. Record the triangulation set in the track's `requirements.md`.

### Consolidated glossaries (optional hint only)

`2-RAILS/Bilingual-Glossaries/bo-en.md` (and `sk-en.md`, `sk-zh.md`, `sk-bo.md`) may be consulted for frequency data on a rendering, but they are draft, cover ~50 keywords, and are **never** used to seed or override the termbase. Terminology evidence comes from the triangulation set at the exact block ID.

### Track folder (output root)

```
3-TRANSFORMATIONS/Translations/<lang>-<audience>-audience/
```

Examples: `en-children-audience`, `en-plain-audience`, `hi-scholar-audience`.

---

## Output

| Artifact | Path |
|---|---|
| Localized requirements | `3-TRANSFORMATIONS/Translations/<track>/requirements.md` |
| Localized audience profile | `3-TRANSFORMATIONS/Translations/<track>/audience.md` |
| Track termbase (grows per chapter) | `3-TRANSFORMATIONS/Translations/<track>/termbase.md` |
| Per-chapter translation | `3-TRANSFORMATIONS/Translations/<track>/Chapter-NN.md` |
| Merged full text | `3-TRANSFORMATIONS/Translations/<track>/BCA-Full-<Label>.md` |

---

## Output file format

### Per-chapter file (`Chapter-NN.md`)

```markdown
---
ref: <N>
title: "Chapter <N> — <English chapter title>"
transformation_type: translation
track: <lang>-<audience>-audience
context_packages:
  - 1-SOURCES/Translations/bo-བློ་ལྡན་ཤེས་རབ།.md (^<N>-0–^<N>-a)
  - 1-SOURCES/Text/BCAV08_SH_sk.md (^<N>-0–^<N>-a)
  - 1-SOURCES/Translations/en-Padmakara_2006.md (^<N>-0–^<N>-a)
  - 1-SOURCES/Translations/en-Wallace.md (^<N>-0–^<N>-a)
  - 1-SOURCES/Translations/en-David_Karma_Choephel.md (^<N>-0–^<N>-a)
generation_date: <YYYY-MM-DD>
status: draft
---

# A Guide to the Bodhisattva's Way of Life   ← Chapter 1 only
### <Audience> <Language> Translation          ← Chapter 1 only
*Zero-shot translation from the Tibetan of Blo ldan shes rab, cross-checked against the Sanskrit of Śāntideva*   ← Chapter 1 only

---

## Chapter <N>: <Chapter title>

<One prose paragraph per verse-block, ending with block ID.> ^<N>-<V>

*Thus ends Chapter <N>: "<Chapter title>."*
```

Publishing metadata (`text_id`, `edition_id`, `category_id`, `license`, etc.) is added by human editors at publication time — do not invent it.

**Chapter titles (BCA):**

| Ch | Title |
|---|---|
| 1 | The Benefits of Bodhichitta |
| 2 | Confessing Wrongdoing |
| 3 | Taking Hold of Bodhichitta |
| 4 | Carefulness |
| 5 | Guarding Awareness |
| 6 | Patience |
| 7 | Diligence |
| 8 | Meditative Concentration |
| 9 | Wisdom |
| 10 | Dedication |

### Verse block rule

- One flowing prose paragraph per source verse-block.
- End every paragraph with the source block ID: `^chapter-verse` (e.g. `^3-12`).
- Preserve every verse ID present in the Tibetan source for that chapter — no skips, no duplicate IDs.
- Do not include Tibetan or Sanskrit source text in the output (target language only).

---

## Rules

1. **Rails first, zero-shot second.** For each verse, check `2-RAILS/Verses/<verse-id>-summary.md`. If `status: complete`, use its synthesis and disambiguated restatement (plus `2-RAILS/Bilingual-Glossaries/` and Local-Wiki as needed). If not complete, translate zero-shot per the workflow below.
2. **Never modify `1-SOURCES/`.** Read only.
3. **Never set `status: complete`.** All generated files stay `status: draft` until a domain specialist reviews them (run `translation-qa` before sign-off).
4. **Termbase is law, and evidence-built.** Every keyword rendering must match `termbase.md`. New terms are **appended** at first occurrence with the attested renderings observed in the triangulation set at that block ID, the chosen rendering, and the citation as rationale — never silently change an existing locked rendering once a chapter has shipped. Never re-seed or rewrite an existing termbase.
5. **One chapter per save.** Translate and write one `Chapter-NN.md` at a time. Long chapters (5, 8, 9) may be read in sections but must be written as one complete chapter file.
6. **Register fidelity.** Follow the localized `requirements.md` and `audience.md` strictly — sentence length, loanword policy, footnote ban, verse-as-prose rule.
7. **Sanskrit is reference only.** When Tibetan and Sanskrit diverge, prefer the Tibetan line as the meaning base; use Sanskrit to disambiguate, not to override. Flag real divergences with the editorial note format below.
8. **Triangulation is mandatory, copying is forbidden.** Compare every draft verse against all three witnesses for *meaning* (subject, object, negations, modality, imagery). If all witnesses agree and your draft disagrees, your parse is almost certainly wrong — re-examine the Tibetan. If the witnesses disagree *with each other*, the verse is genuinely ambiguous — resolve from the Sanskrit and flag. Never copy any witness's wording — each is under its own copyright and its register will not match the track.
9. **Divergence flag format.** When sources genuinely disagree or a reading is uncertain, append a bracketed editorial note after the block ID line: `[Ed: Skt reads "…"; Tibetan followed.]` or `[Ed: Padmakara and Wallace read this pāda as X; Choephel as Y; Sanskrit supports X.]` English, factual, one sentence.
10. **Sensitive verses.** Verses with outdated cultural assumptions (e.g. `^10-30`) get a brief bracketed editorial note in children/plain tracks; scholar track may use a footnote-style aside only if `requirements.md` allows it.
11. **Do not hallucinate.** Translate only what is in the source. No invented explanations, no dropped pādas, no merged verses.
12. **Merge is deterministic.** After all chapters exist, merge with the bundled script (`scripts/merge_chapters.py`) — do not hand-stitch the full text.

---

## Per-verse translation workflow

For each verse-block, in order:

1. **Rails check** — if `2-RAILS/Verses/<id>-summary.md` is `status: complete`, translate from its disambiguated restatement and skip to step 6.
2. **Parse the Tibetan** — identify agent, object, verb, negations, and particles; note any homonym or ambiguous syntax.
3. **Read the witnesses** — read all three triangulation translations at this block ID. Classify: **consensus** (all agree on meaning) or **split** (they diverge — record who reads what).
4. **Consult the Sanskrit** — resolve each ambiguity from step 2 and each split from step 3 against the Sanskrit pāda. Note (do not resolve silently) any real Tibetan/Sanskrit divergence.
5. **Resolve terminology** — apply locked termbase renderings. For a key term not yet in the termbase: list its renderings across the witnesses at this block ID, choose the one fitting the track register, and queue it for append with the citation (e.g. `བདེ་གཤེགས། → "the Blissful Ones" — Padmakara "Blissful Ones", Wallace "Sugatas", Choephel "sugatas" at ^1-1; register avoids loanwords`).
6. **Draft** — one prose paragraph in the track register per `requirements.md`, in your own wording.
7. **Verify against consensus** — if the witnesses were in consensus and your draft's meaning differs, return to step 2. If the split persists after step 4, keep the Sanskrit-supported reading and add a divergence note (Rule 9).
8. **Finalise** — append the block ID; add editorial note if flagged.

---

## Procedure

### Step 1 — Confirm inputs

Resolve:
- `track` = `<lang>-<audience>-audience`
- `track_dir` = `3-TRANSFORMATIONS/Translations/<track>/`
- Chapter list from scope (`all` → 1..10)
- Triangulation set (see Inputs)

### Step 2 — Track folder

**If the track folder already exists (the normal case):** read `requirements.md`, `audience.md`, and `termbase.md` and continue. Do not overwrite, re-localize, or re-seed any of them — an existing termbase grows append-only from this point, however thin it is.

**Only if `track_dir` does not exist:**

1. Create `track_dir`.
2. Write `track_dir/requirements.md`, using `3-TRANSFORMATIONS/Translations/en-plain-english/requirements.md` as the structural model. Localize for the target language and audience level (register, reading level, loanword policy, sentence length). Include **§ Zero-shot sources**: Primary: `1-SOURCES/Translations/bo-བློ་ལྡན་ཤེས་རབ།.md`; Reference: `1-SOURCES/Text/BCAV08_SH_sk.md`; Triangulation set: the three witnesses (plus any target-language translations). Fallback rule: use zero-shot when verse rails are not `status: complete`.
3. Write `track_dir/audience.md` (model: `en-plain-english/audience.md`), localized for the audience level.
4. Create `track_dir/termbase.md` **empty** — header and table columns only (source lemma | chosen rendering | rationale with block-ID citation), modeled on `en-plain-english/termbase.md`. Do not seed it: entries are added at first occurrence during translation, from witness evidence (per-verse workflow step 5).

### Step 3 — Translate each chapter

For each chapter `N` in scope:

**a. Load sources**

- Read Tibetan chapter: lines from `^N-0` through the line before `^(N+1)-0` (chapter 10 through `^a-0`).
- Read matching Sanskrit chapter from `BCAV08_SH_sk.md` for the same verse IDs.
- Read the same chapter from **all three** triangulation translations (and any target-language translations).
- Load `termbase.md` and scan for terms appearing in this chapter.

**b–c. Translate**

Apply the **per-verse translation workflow** above to every verse-block in the chapter.

**d. Write chapter file**

Save to `track_dir/Chapter-NN.md` using the format above. Set `generation_date` to today.

**e. Update termbase**

Append the terms queued during this chapter (source lemma, chosen rendering, rationale with witness renderings and block-ID citation). Never edit prior rows.

**f. Report progress**

After each chapter, state which chapter finished, which remain, and how many divergence notes were added.

### Step 4 — Merge full text (when scope is complete)

When all chapters in scope exist and `merge` is not `no`:

```bash
python 4-SYSTEM/Skills/translate-zero-shot/scripts/merge_chapters.py \
  "3-TRANSFORMATIONS/Translations/<track>" \
  --track "<track>" \
  --title "Entering the Bodhisattva's Way of Life — Full Text (<Audience> <Language>)" \
  --output "BCA-Full-<Audience>-<Language>.md" \
  --chapters all
```

The script fails on missing chapters or duplicate block IDs — fix the chapter files and rerun; never hand-edit the merged output.

### Step 5 — Self-check before handoff

Run all of these; fix and rerun until clean:

1. **Verse coverage** — for each chapter, extract the unique `^N-V` IDs from the Tibetan source chapter and from `Chapter-NN.md`; the sets must be identical (no skips, no extras, no duplicates).
2. **Termbase consistency** — for each locked rendering, grep the chapter files to confirm no competing rendering of the same lemma slipped through; every termbase row added this run cites at least one block ID.
3. **Divergence notes** — every `[Ed: …]` note names its source; no unresolved `⚑` or TODO markers remain.
4. **Frontmatter** — every chapter file has `status: draft` and complete `context_packages`.
5. **QA skill** — run `translation-qa` on the per-chapter files (it includes `mqm_mechanical_checks.py`). Iterate until no critical/major errors. This step is required, not optional.

---

## Completion check

- [ ] Target language, audience level, and triangulation set confirmed.
- [ ] Track folder exists; existing `requirements.md`, `audience.md`, `termbase.md` were read, not overwritten or re-seeded.
- [ ] Every requested chapter saved as `Chapter-NN.md` with correct frontmatter and `status: draft`.
- [ ] Every verse in scope has exactly one `^N-V` block ID in the output (verified against source, not just counted).
- [ ] Every verse triangulated against all three witnesses; splits resolved from the Sanskrit and flagged with `[Ed: …]` notes.
- [ ] `termbase.md` updated append-only, each new row citing witness renderings at a block ID.
- [ ] Merged full-text file written via `scripts/merge_chapters.py` when scope is complete (unless user opted out).
- [ ] `translation-qa` run with no remaining critical/major errors.
- [ ] User told which chapters remain if scope was partial.
- [ ] User reminded that only a domain specialist may promote files to `status: complete`.
