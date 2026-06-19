# Session Handoff — BCA Railroads Project
*Generated: 2026-06-15*

---

## What this project is

**Railroads** is a pipeline for AI-assisted translation of the *Bodhisattvacaryāvatāra* (BCA) by Śāntideva. The pipeline has three stages:

```
1-SOURCES/ → 2-RAILS/ → 3-TRANSFORMATIONS/
```

- `1-SOURCES/` — read-only human material (root texts, commentaries, translations)
- `2-RAILS/` — per-verse context packages synthesising 4 Tibetan commentaries
- `3-TRANSFORMATIONS/` — AI-generated translation outputs

**Write permissions (from 4-SYSTEM/CLAUDE.md):**

| Folder | LLM may write? |
|---|---|
| `0-INBOX/` | yes |
| `1-SOURCES/` | **NO** |
| `2-RAILS/` | yes |
| `3-TRANSFORMATIONS/` | yes, only when explicitly instructed |
| `4-SYSTEM/` | **NO** |

**Before any task:** Read `4-SYSTEM/CLAUDE.md` in full, then check `4-SYSTEM/Skills/SKILLS-CATALOG.md` for a matching skill before proceeding.

---

## Active translation tracks

### Track A — en-ai (scholarly, college-level)
- Source: Tibetan root text + 4 commentaries via 2-RAILS
- Files: `3-TRANSFORMATIONS/Translations/en-ai/`
- Status: **Ch1 complete** (`Chapter one (Claude AI).md`). Ch2 in progress — rails exist (65 verse files in `2-RAILS/Verses/2-*.md`) but the translation file has NOT been written yet.
- To resume: read `3-TRANSFORMATIONS/Translations/en-ai/requirements.md` + `termbase.md`, then generate `Chapter two (Claude AI).md` verse by verse using the Ch2 verse rails.

### Track B — en-plain-english (Grade 8, general readers)
- Source: Sanskrit root text (`1-SOURCES/Text/sk-dev.md`) + 2-RAILS synthesis
- Files: `3-TRANSFORMATIONS/Translations/en-plain-english/`
- Status: **Ch1–3 complete** as standalone file `BCA-Chapters-1-3-Plain-English.md` at project root. Passed vocabulary QA.
- Automation script: `0-INBOX/translate-plain-english.py` (see below)

---

## Key files created in recent sessions

### `0-INBOX/translate-plain-english.py`
Python script that automates Grade 8 translation via the Claude API.

**How it works:**
1. Parses Sanskrit verses from `1-SOURCES/Text/sk-dev.md` by block ID
2. For each verse, reads `2-RAILS/Verses/{ch}-{v}.md` and extracts the `## Synthesis` section (actual Tibetan summary text, skipping Obsidian transclusion lines `![[...]]`)
3. Checks `status: complete` in rail frontmatter before using it; falls back to Sanskrit-only if absent or not complete
4. Bundles Sanskrit + Tibetan synthesis into one API call per chapter
5. Outputs a `.md` file to the project root

**Usage:**
```bash
pip install anthropic
export ANTHROPIC_API_KEY=sk-...
python 0-INBOX/translate-plain-english.py --chapter 2
python 0-INBOX/translate-plain-english.py --chapter 1-3
python 0-INBOX/translate-plain-english.py --chapter all
```

**Rail coverage:** Ch1–3 have verse rails (`status: complete`). Ch4–10 will use Sanskrit-only until verse-context-batch is run for those chapters.

**Important:** Ch1 rails use heading `## Synthesis (Tibetan)`; Ch2–3 use `## Synthesis (original language)`. The script handles both.

### `0-INBOX/check-vocab-consistency.py`
QA script to verify translated output against the termbase.

**Usage:**
```bash
python 0-INBOX/check-vocab-consistency.py --file BCA-Chapters-1-3-Plain-English.md --track en-plain-english
python 0-INBOX/check-vocab-consistency.py --file "3-TRANSFORMATIONS/Translations/en-ai/Chapter two (Claude AI).md" --track en-ai
```

Checks: (1) forbidden transliterations, (2) required renderings present, (3) inconsistent rendering pairs, (4) block ID coverage. Exit code 0 = clean.

### `0-INBOX/SKILL-translate-plain-english.md`
Skill definition for the en-plain-english workflow. Currently a draft in 0-INBOX — to register it, a human must move it to `4-SYSTEM/Skills/translate-plain-english/SKILL.md`. (LLM cannot write to 4-SYSTEM.)

### `BCA-Chapters-1-3-Plain-English.md` (project root)
Grade 8 translation of Ch1–3, 135 verses. Passed all vocabulary checks. Note: `^3-2` is absent from the Sanskrit edition — marked with a note in the file.

---

## Termbase — en-plain-english (locked renderings)

| Sanskrit concept | Required rendering |
|---|---|
| bodhicitta | the Mind of Enlightenment |
| bodhisattva / jina-putra | Hero of Enlightenment |
| sugata / tathāgata | the Blissful Ones |
| dharma | the Teaching / the Truth |
| saṃsāra | the cycle of life |
| nirvāṇa | final peace / liberation |
| dharmakāya | Truth Body |
| pāpa / duṣkṛta | harmful deeds / wrongdoing |
| puṇya / kuśala | goodness / helpful deeds |
| śūnyatā | Emptiness |

**Forbidden terms (en-plain-english):** bodhicitta, bodhisattva, samsara, nirvana, dharma, dharmakaya, sugata, tathagata, sunyata, karma, bodhi, merit, virtue, sin, vice, vow, "leisure and endowment"

---

## Rail structure — 2-RAILS/Verses/

Each file `{ch}-{v}.md` has:
```yaml
---
verse_id: 2-1
root_text: 1-SOURCES/Translations/bo-...md
root_block: ^2-1
language: bo
commentaries: [kunpal, ngulchu-thogmed, sabzang, prajnakaramati]
status: complete
---
```
Sections: `## Verse`, `## Commentary passages` (transclusion refs only), `## Synthesis (original language)` (actual Tibetan text — this is what the translation script uses), `## Disambiguated verse`.

**Rail coverage:**
- Ch1: 36 verse files (1-1.md → 1-36.md), status: complete
- Ch2: 65 verse files (2-1.md → 2-65.md), status: complete
- Ch3: 35 verse files (3-1.md → 3-35.md, ^3-2 absent), status: complete
- Ch4–10: not yet built

**Section files:** `2-RAILS/Sections/` has combined section summaries for Ch1 (11 files) and Ch2 (25 files). Ch3 sections not yet built.

---

## Pending tasks (priority order)

1. **Ch2 en-ai translation** — most urgent; rails are ready, translation not written.
   - Read `3-TRANSFORMATIONS/Translations/en-ai/requirements.md` + `termbase.md`
   - For each of the 65 verse rails in `2-RAILS/Verses/2-*.md`, generate a scholarly translation paragraph
   - Save to `3-TRANSFORMATIONS/Translations/en-ai/Chapter two (Claude AI).md`
   - Format: one prose paragraph per verse, block ID at end, same format as Ch1

2. **Ch3 section files** — `2-RAILS/Sections/` has nothing for Ch3 yet. Use `section-summary-raw` + `section-summary-combined` skills.

3. **Ch4–10 verse rails** — run `verse-context-batch` for Ch4–10 (scripts exist for Ch2 and Ch3 as reference: `0-INBOX/verse-context-batch-ch2.py`, `0-INBOX/verse-context-batch-ch3.py`).

4. **Register translate-plain-english skill** — human action required: move `0-INBOX/SKILL-translate-plain-english.md` to `4-SYSTEM/Skills/translate-plain-english/SKILL.md`.

5. **sk-en termbase expansion** — `2-RAILS/Bilingual-Glossaries/sk-en.md` only has 9 keywords. The proper Sanskrit→English chain needs `glossary-select` run against `sk-en.md` to produce a full termbase for Sanskrit-sourced workflows.

---

## Source file reference

| File | Purpose |
|---|---|
| `1-SOURCES/Text/sk-dev.md` | Sanskrit root text, all 10 chapters, block IDs ^1-1 to ^10-N |
| `1-SOURCES/Translations/bo-བློ་ལྡན་ཤེས་རབ།.md` | Tibetan root text (canonical translation source) |
| `2-RAILS/Bilingual-Glossaries/bo-en.md` | Consolidated Tibetan→English glossary, 50 keywords, 239 renderings |
| `2-RAILS/Bilingual-Glossaries/sk-bo.md` | Sanskrit→Tibetan glossary, 9 keywords, draft |
| `2-RAILS/Bilingual-Glossaries/sk-en.md` | Sanskrit→English glossary, 9 keywords, draft |
| `3-TRANSFORMATIONS/Translations/en-ai/requirements.md` | Scholarly track style contract |
| `3-TRANSFORMATIONS/Translations/en-ai/termbase.md` | Scholarly track locked renderings |
| `3-TRANSFORMATIONS/Translations/en-plain-english/requirements.md` | Grade 8 style contract |
| `3-TRANSFORMATIONS/Translations/en-plain-english/termbase.md` | Grade 8 locked renderings (Tibetan lemmas) |
| `4-SYSTEM/Skills/SKILLS-CATALOG.md` | Master list of all skills [exists] / [planned] |

---

## Chapter titles reference

| # | Sanskrit | Plain English |
|---|---|---|
| 1 | Bodhicittānuśaṃsa | The Benefits of the Mind of Enlightenment |
| 2 | Pāpadeśanā | Confessing Wrongdoing |
| 3 | Bodhicittaparigraha | Taking Up the Mind of Enlightenment |
| 4 | Bodhicittāpramāda | Carefulness |
| 5 | Saṃprajanyarakṣaṇa | Guarding Awareness |
| 6 | Kṣāntipāramitā | The Perfection of Patience |
| 7 | Vīryapāramitā | The Perfection of Effort |
| 8 | Dhyānapāramitā | The Perfection of Meditation |
| 9 | Prajñāpāramitā | The Perfection of Wisdom |
| 10 | Pariṇāmanā | Dedication |

---

## Block ID format

`^{chapter}-{verse}` — e.g. `^2-1`, `^6-33`. No zero-padding. Chapter headings use `^N-0`. Absent verse `^3-2` is noted but not present in the Sanskrit edition.

---

## Notes on the Sanskrit workflow

The en-plain-english track translates directly from Sanskrit (`sk-dev.md`), not Tibetan. The termbase has Tibetan source lemmas but the English renderings apply equally to the corresponding Sanskrit concepts. The 2-RAILS synthesis (Tibetan) is used as interpretive context only — the model bridges Sanskrit ↔ Tibetan ↔ English using its own training knowledge. This is a structural workaround because the 2-RAILS pipeline was built from Tibetan sources only. The proper fix would be expanding `sk-en.md` to a full termbase, but this is pending.
