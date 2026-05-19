# 3-TRANSFORMATIONS — Prescriptive outputs

This folder holds the **AI-generated outputs** of the vault — and the per-track files that prescribe how each output is produced. Where `2-RAILS/` records what the commentary tradition *says*, this folder records what *each particular output* will do with it: this audience, this register, this set of locked keyword renderings, this calendar.

This README is the **authoritative document** for everything in `3-TRANSFORMATIONS/`: the three transformation categories, the per-track file convention (`requirements.md` / `termbase.md` / `requirements.md`), the citation rules into outputs, the status lifecycle, the checklist for a new track. The LLM-facing operational summary lives in [`../4-SYSTEM/CLAUDE.md`](../4-SYSTEM/CLAUDE.md) §9–11.

The split between descriptive rails and prescriptive transformations is what makes the vault scalable. A scholarly English translation, a children's Sinhala adaptation, a daily push-notification stream, and a year-long retreat plan can all run on the same rails — they differ only in their `requirements.md` (style), their `termbase.md` (vocabulary), and the per-track logic that wires them together.

---

## 1. The three categories

Every transformation falls into one of three categories. Each category is a top-level subfolder, and each transformation within a category is a **track** — one coherent output stream with one set of choices.

### `Translations/` — language-by-language translations

A translation track renders the source text into one target language at one register for one audience. The track's prescriptive rails are:

- **`requirements.md`** — the style contract (audience, register, sentence length, transliteration policy, source-rail dependencies). Written in the target language.
- **`termbase.md`** — the vocabulary contract (one chosen rendering per keyword that appears in the text, selected from the consolidated bilingual glossary in `2-RAILS/Bilingual-Glossaries/`).

The translation skill consumes both files plus the relevant rails in `2-RAILS/` and produces the translation file(s), section by section. See [`Translations/About Translations.md`](Translations/About Translations.md) for the full per-track workflow (rail fetching → batched translation → MQM QA) and the worked example tracks currently in this vault.

### `Adaptations/` — audience-targeted retellings

An adaptation track is a domain shift, not a language shift: a children's version, a scholarly summary, a meditation manual, a sermon series. Adaptations may or may not change the target language; what defines them is that they restructure or reframe the source for an audience that needs more (or less) than the source provides at face value.

The track's prescriptive rails are:

- **`requirements.md`** — audience, structural shape, what to keep, what to dissolve, what to footnote, what to omit entirely. Written in the working language of the adaptation team.
- **`termbase.md`** *(optional)* — only if the adaptation locks specific renderings; many adaptations work directly from the rails without a separate termbase.

See [`Adaptations/About Adaptations.md`](Adaptations/About Adaptations.md) for the convention.

### `Plans/` — calendar-driven study/practice arcs

A plan track organises engagement with the text along a calendar — daily readings, weekly retreat sessions, a year-long course, a chanting preparation arc. Each day or session is generated from rails (and often from completed Translation or Adaptation outputs), then arranged into a publishable schedule with surrounding communications and assets.

Plans are language-stratified: each published language gets its own subfolder inside the plan folder, with its own `requirements.md`, `termbase.md`, `schedule.md`, `days/`, `communications/`, and `assets/`. Language streams can be at different completion stages independently.

The plan's governing files are:

- **`About <plan-name>.md`** (plan root) — cross-language overview: purpose, per-session shape that all language streams share, list of languages, source-rail dependencies, and status rules.
- **`<lang>/requirements.md`** — style contract for one language stream, written in that language.
- **`<lang>/termbase.md`** — vocabulary contract for one language stream.
- **`<lang>/schedule.md`** — day-by-day calendar for one language stream.

See [`Plans/About Plans.md`](Plans/About Plans.md) for the full convention and per-file schemas.

---

## 2. Folder structure

```
3-TRANSFORMATIONS/
├── Translations/
│ └── [track-id]/ # e.g. en-contemporary-translation
│ ├── requirements.md # style contract
│ ├── termbase.md # vocabulary contract
│ ├── audience.md # audience profile
│ ├── <output>.md # the generated translation files
│ └── qa-report.md # MQM critique driving the next revision
├── Adaptations/
│ └── [track-id]/
│ ├── requirements.md # style contract for the adaptation
│ ├── termbase.md # (optional) locked renderings
│ ├── audience.md # audience profile
│ └── <output>.md # the generated files
└── Plans/
 └── <plan-name>/
 ├── About <plan-name>.md # cross-language overview and session shape
 └── <lang>/ # one folder per language (e.g. en/, bn/, pi/)
 ├── requirements.md # style contract (in target language)
 ├── termbase.md # vocabulary contract
 ├── schedule.md # day-by-day calendar
 ├── days/ # per-session output files
 │ ├── day-1.md # intro + text transclusion + notifications
 │ └── day-N.md
 ├── communications/ # cross-day outreach content
 │ └── announcements.md
 └── assets/
 └── images/
```

Each track is one coherent output stream. New tracks are added by creating a subfolder under the appropriate category and seeding it with the right governing file(s). New categories should be rare — they exist because the three current ones map cleanly onto the three different things AI-powered work on a classical text actually produces.

---

## 3. The governing files of every track

### `requirements.md` — the style contract

Required for Translation and Adaptation tracks. A binding contract that the generation skill reads on every run. Before any output is generated, the file must cover at minimum:

- **Target audience and register** (scholarly, lay, monastic, …) and reading level.
- **Bilingual Glossary reference path** — relative path to the per-track termbase.
- **Preferred rendering for structurally significant terms** that recur across the text and must never vary.
- **Style constraints** — sentence length, paragraph length, treatment of verse vs. prose, handling of lists, use vs. transliteration of technical terms, footnote vs. inline glossing policy.
- **Cultural-adaptation rules** — what to translate, what to gloss, what to leave untranslated.
- **Source-rail dependencies** — which rails (`Sections/`, `Verses/`, `Local-Wiki/`) the generation skill must consult before each batch.

The `requirements.md` is written **in the target language** of the track. If it is incomplete, the output will drift in style and the QA phase will catch it as MQM "style" or "locale convention" errors.

### `termbase.md` — the vocabulary contract

Required for every track. Contains one entry per keyword that appears in the text(s) the track translates, each with one chosen rendering and a one-line rationale. The termbase is sized to the text, not the corpus: the translation skill carries complete, consistent vocabulary inside its prompt — never an "I'll fall back to whatever fits" choice mid-sentence.

The termbase is built by the `glossary-select` skill from the consolidated `2-RAILS/Bilingual-Glossaries/<src>-<tgt>.md` file, guided by the track's `requirements.md`. If no existing rendering is satisfactory, derive one from the relevant Local-Wiki article and feed the new rendering back into the consolidated bilingual glossary as a new attested row.

### Plan governing files

Plans use a two-level contract rather than a single `requirements.md`:

- **`About <plan-name>.md`** (at plan root) — the cross-language brief: purpose, audience summary, per-session shape that all language streams share, list of published languages, source-rail dependencies, and status rules. Written in English regardless of which languages the plan publishes.
- **`<lang>/requirements.md`** — the per-language style contract, written *in that language*. Covers: target audience and register for this stream, rendering conventions for each session step, communications style, cultural-adaptation rules.
- **`<lang>/termbase.md`** — vocabulary contract for this language stream. Built by `glossary-select` from `2-RAILS/Bilingual-Glossaries/` plus the stream's `requirements.md`.
- **`<lang>/schedule.md`** — the day-by-day calendar for this language stream: date, day number, verse/section reference, language-specific notes.

### `audience.md` — the audience profile (Translations and Adaptations)

Required for Translation and Adaptation tracks. A binding profile of the reader the transformation is written for, covering four dimensions: demographics and region; prior knowledge and reading level; use cases and reading settings; motivations and pain points. Scaffold from the template at [`../4-SYSTEM/Templates/audience.md`](../4-SYSTEM/Templates/audience.md). Written in the target language alongside `requirements.md`.

For Plan tracks, audience coverage is part of `About <plan-name>.md` at the cross-language level and `<lang>/requirements.md` at the per-stream level.

---

## 4. The citation chain into outputs

Every output file's frontmatter records which `2-RAILS/` packages it was generated from:

```yaml
---
ref: 1-1
transformation_type: translation | adaptation | plan-session
context_packages:
 - 2-RAILS/Verses/1-1.md
 - 2-RAILS/Sections/1.md
 - 2-RAILS/Local-Wiki/[term]_([disambiguator]).md
generation_date: 2026-05-15
status: draft | partial | complete
---
```

Hard rules:

- An output may only cite `2-RAILS/`. It must never reach past the rails to cite `1-SOURCES/` directly.
- An output may only consume rails whose `status` is `complete`. Drafts and partials are not used.
- An output may not introduce a keyword rendering not in the per-track termbase. If a new term must be introduced, the termbase is updated first, *and* the new rendering is written back to the consolidated bilingual glossary in `2-RAILS/Bilingual-Glossaries/` as a new attestation row.
- Plan tracks may also cite completed outputs of other tracks (e.g. [plan-id] embeds the English Translation track's output for the Reading-for-Meaning step). Citation is recorded the same way in `context_packages:`.

---

## 5. Status lifecycle

Track outputs carry a `status` frontmatter field with the same lifecycle as rails:

| Status | Meaning |
| ---------- | ---------------------------------------------------------------------------------------- |
| `draft` | LLM-generated, not yet reviewed; may contain MQM critical or major errors |
| `partial` | reviewed in part; some sections reviewed, others still draft |
| `complete` | every claim cites a `2-RAILS/` package; no critical or major MQM errors outstanding |

Only `complete` outputs are published or referenced by other transformations. Domain specialists set `complete`; the LLM never marks its own output complete.

---

## 6. Skills that operate on this folder

See [`../4-SYSTEM/Skills/SKILLS-CATALOG.md`](../4-SYSTEM/Skills/SKILLS-CATALOG.md). The key skills are:

- `glossary-select` — builds the per-track `termbase.md` from the consolidated bilingual glossary plus `requirements.md`.
- `requirements-author` *(planned)* — authors or audits a track's `requirements.md`.
- `translate-section` *(planned)* — translates a small batch of TOC nodes for a Translation track.
- `translation-qa` *(planned)* — reviews a translated section against MQM, the track requirements, and the source rails.
- `style-consistency-check` *(planned)* — catches style drift across many sections of a track.

Adaptation and Plan skills are not yet catalogued; they will be added as those tracks come online.

---

## 7. Checklist for a new track

**Translation or Adaptation track:**
- [ ] Create the folder under `Translations/` or `Adaptations/`.
- [ ] Author `requirements.md` (in the target language) covering all required sections (§3).
- [ ] Scaffold `audience.md` from [`../4-SYSTEM/Templates/audience.md`](../4-SYSTEM/Templates/audience.md) and fill in the four dimensions.
- [ ] Ensure the consolidated `2-RAILS/Bilingual-Glossaries/<src>-<tgt>.md` exists and is `status: complete`.
- [ ] Run `glossary-select` to produce the initial `termbase.md`.
- [ ] Confirm the rails covering the first batch are `status: complete`.
- [ ] Generate the first batch as `draft`; run QA; iterate until `complete`.

**Plan track:**
- [ ] Create `Plans/<plan-name>/`.
- [ ] Author `About <plan-name>.md` — define the session shape and list of languages before any stream begins.
- [ ] For each language stream: create `Plans/<plan-name>/<lang>/` and author `<lang>/requirements.md` (in that language).
- [ ] Run `glossary-select` to produce `<lang>/termbase.md` for each stream.
- [ ] Build `<lang>/schedule.md` for each stream.
- [ ] Generate day-1 for each stream as `draft`; review; iterate until `complete` before proceeding to day-2.
- [ ] Add communications content to `<lang>/communications/` as the plan rolls out.

---

## 8. Checklist for a new output file

- [ ] Frontmatter lists every `2-RAILS/` package consulted in `context_packages:`.
- [ ] Every keyword rendering is in the per-track `termbase.md` (or has been added to it before generation, and to the consolidated bilingual glossary as a new attestation row).
- [ ] `transformation_type:`, `generation_date:`, and `status:` set.
- [ ] No claim that cannot be traced back to a `2-RAILS/` package. If a needed clai