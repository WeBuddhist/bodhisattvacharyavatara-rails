---
name: translate-zero-shot
description: >
  Zero-shot translation of the Bodhisattvacaryāvatāra from the Tibetan source
  (bo-བློ་ལྡན་ཤེས་རབ།.md) cross-checked against the Sanskrit root text
  (BCAV08_SH_sk.md) into a localized audience track (children, plain, or
  scholar) when 2-RAILS/ verse packages are not yet complete. Sets up the
  track folder, translates chapter by chapter, updates termbase.md, and merges
  into a full-text file. Use when the user asks for zero-shot translation,
  translate from Tibetan/Sanskrit sources, localize children-audience (or
  plain/scholar) for a target language, translate BCA by chapter, or merge
  chapter translation chunks.
---

# translate-zero-shot

Produces a full *Bodhisattvacaryāvatāra* translation track directly from `1-SOURCES/` when `2-RAILS/Verses/<verse-id>.md` packages are not yet `status: complete`. The Tibetan translation is the primary meaning source; the Sanskrit root text resolves ambiguity (homonyms, pāda breaks, philosophical terms). Output matches the vault's transformation conventions: localized `requirements.md` / `audience.md` / `termbase.md`, one `Chapter-NN.md` per chapter, then one merged full-text file.

**Reference implementation:** `3-TRANSFORMATIONS/Translations/en-children-audience/` (Chapters 1–10 + `BCA-Full-Children-English.md`).

---

## Inputs

| Input | Required | Description |
|---|---|---|
| **Target language** | ✓ | ISO-style code or short name, e.g. `en`, `hi`. Determines track folder prefix. |
| **Audience level** | ✓ | `children`, `plain`, or `scholar`. Maps to template folder and track suffix. |
| **Chapter scope** | optional | Single chapter (`3`), range (`1-3`), or `all` (default: `all` = chapters 1–10). |
| **Merge** | optional | `yes` (default) or `no`. When `yes`, run merge after all requested chapters exist. |

If target language or audience level is missing, ask before proceeding.

### Fixed source files (this vault)

| Role | Path |
|---|---|
| Tibetan primary | `1-SOURCES/Translations/bo-བློ་ལྡན་ཤེས་རབ།.md` |
| Sanskrit reference | `1-SOURCES/Text/BCAV08_SH_sk.md` |

### Audience templates

| Audience | Template folder |
|---|---|
| `children` | `3-TRANSFORMATIONS/Translations/children-audience/` |
| `plain` | `3-TRANSFORMATIONS/Translations/plain-audience/` |
| `scholar` | `3-TRANSFORMATIONS/Translations/scholar-audience/` |

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

1. **Rails first, zero-shot second.** For each verse, check `2-RAILS/Verses/<verse-id>.md`. If `status: complete`, use it (plus `2-RAILS/Bilingual-Glossaries/bo-<lang>.md` and Local-Wiki as needed). If not complete, translate zero-shot from the two source files.
2. **Never modify `1-SOURCES/`.** Read only.
3. **Never set `status: complete`.** All generated files stay `status: draft` until a domain specialist reviews them (run `translation-qa` before sign-off).
4. **Termbase is law.** Every keyword rendering must match `termbase.md`. New terms discovered during translation are **appended** with rationale — never silently change an existing locked rendering once a chapter has shipped.
5. **One chapter per save.** Translate and write one `Chapter-NN.md` at a time. Long chapters (5, 8, 9) may be read in sections but must be written as one complete chapter file.
6. **Register fidelity.** Follow the localized `requirements.md` and `audience.md` strictly — sentence length, loanword policy, footnote ban, verse-as-prose rule.
7. **Sanskrit is reference only.** When Tibetan and Sanskrit diverge, prefer the Tibetan line as the meaning base; use Sanskrit to disambiguate, not to override the Tibetan translation file without flagging the issue in a comment.
8. **Sensitive verses.** Verses with outdated cultural assumptions (e.g. `^10-30`) get a brief bracketed editorial note in children/plain tracks; scholar track may use a footnote-style aside only if `requirements.md` allows it.
9. **Do not hallucinate.** Translate only what is in the source. No invented explanations, no dropped pādas, no merged verses.
10. **Merge is deterministic.** After all chapters exist, merge with the bundled script — do not hand-stitch the full text.

---

## Procedure

### Step 1 — Confirm inputs

Resolve:
- `track` = `<lang>-<audience>-audience`
- `track_dir` = `3-TRANSFORMATIONS/Translations/<track>/`
- `template_dir` = `3-TRANSFORMATIONS/Translations/<audience>-audience/`
- Chapter list from scope (`all` → 1..10)

### Step 2 — Set up track folder (if new)

If `track_dir` does not exist:

1. Create `track_dir`.
2. Copy `template_dir/requirements.md` → `track_dir/requirements.md` and **localize** for the target language:
   - Replace `[target language]`, `[lang]`, reading-level placeholders.
   - Add **§ Zero-shot source pair** (after bilingual glossary section):
     - Primary: `1-SOURCES/Translations/bo-བློ་ལྡན་ཤེས་རབ།.md`
     - Reference: `1-SOURCES/Text/BCAV08_SH_sk.md`
     - Fallback rule: use zero-shot when verse rails are not `status: complete`.
3. Copy and localize `template_dir/audience.md` → `track_dir/audience.md`.
4. Seed `track_dir/termbase.md` with core terms (bodhichitta, bodhisattva, Buddha epithets, dharma, samsara, kleśa, śūnyatā, karma, nirvana, Three Jewels). Use `en-children-audience/termbase.md` as a structural example.

If the track folder already exists, read its three governing files and continue — do not overwrite them.

### Step 3 — Translate each chapter

For each chapter `N` in scope:

**a. Load sources**

- Read Tibetan chapter: lines from `^N-0` through the line before `^(N+1)-0` (chapter 10 through end of file).
- Read matching Sanskrit chapter from `BCAV08_SH_sk.md` for the same verse IDs.
- Load `termbase.md` and scan for terms appearing in this chapter.

**b. Check rails (optional per verse)**

For each verse ID in the chapter, if `2-RAILS/Verses/<id>.md` exists with `status: complete`, consult its disambiguated restatement before translating that verse.

**c. Translate**

- Render each verse-block as one prose paragraph per `requirements.md`.
- Apply termbase renderings; gloss loanwords on first use per chapter only (if required by requirements).
- End each paragraph with `^N-V`.

**d. Write chapter file**

Save to `track_dir/Chapter-NN.md` using the format above. Set `generation_date` to today.

**e. Update termbase**

Append any new locked terms from this chapter (source lemma, chosen rendering, rationale). Never edit prior rows.

**f. Report progress**

After each chapter, state which chapter finished and which remain.

### Step 4 — Merge full text (when scope is complete)

When all chapters in scope exist and `merge` is not `no`:

```bash
python 4-SYSTEM/Skills/translate-zero-shot/scripts/merge_chapters.py \
  "3-TRANSFORMATIONS/Translations/<track>" \
  --track "<track>" \
  --title "Entering the Bodhisattva's Way of Life — Full Text (<Audience> <Language>)" \
  --output "BCA-Full-<Audience>-<Language>.md"
```

Example (English children):

```bash
python 4-SYSTEM/Skills/translate-zero-shot/scripts/merge_chapters.py \
  "3-TRANSFORMATIONS/Translations/en-children-audience" \
  --track "en-children-audience" \
  --title "Entering the Bodhisattva's Way of Life — Full Text (Children English)" \
  --output "BCA-Full-Children-English.md"
```

### Step 5 — Self-check before handoff

- Count verse block IDs in each chapter file; compare against Tibetan source verse count for that chapter.
- Spot-check termbase consistency across chapters.
- Recommend running `translation-qa` on the merged file or per-chapter files.

---

## Completion check

- [ ] Target language and audience level confirmed.
- [ ] Track folder exists with localized `requirements.md`, `audience.md`, and `termbase.md`.
- [ ] Every requested chapter saved as `Chapter-NN.md` with correct frontmatter and `status: draft`.
- [ ] Every verse in scope has exactly one `^N-V` block ID in the output.
- [ ] `termbase.md` updated with new terms (append only).
- [ ] Merged full-text file written when scope is complete (unless user opted out).
- [ ] User told which chapters remain if scope was partial.
- [ ] User reminded to run `translation-qa` before promoting to `status: complete`.
