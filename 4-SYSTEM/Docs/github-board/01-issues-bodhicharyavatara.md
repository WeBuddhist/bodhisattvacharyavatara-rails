# Issue drafts — Bodhicharyavatara (བྱང་ཆུབ་སེམས་དཔའི་སྤྱོད་པ་ལ་འཇུག་པ།)

Copy-paste ready. Parent issue first, then each sub-issue.

---

## PARENT ISSUE (the board card)

**Title:** `[TEXT] Bodhicharyavatara — བྱང་ཆུབ་སེམས་དཔའི་སྤྱོད་པ་ལ་འཇུག་པ།`
**Labels:** `text`
**Body:**

> Master tracking issue for the full processing pipeline of the Bodhicharyavatara (Śāntideva). This card moves across the board as stages complete; all work items are sub-issues below.
>
> **Vault:** `bodhisattvacharyavatara-rails`
> **Pipeline:** Sources → Rails → Transformations
>
> ### Stage overview
> - [ ] 1 · Sources: Root Text (S1–S2)
> - [ ] 1 · Sources: Translations & Commentaries (S3–S4)
> - [ ] 2 · Rails: Sections & Verses (R1–R3)
> - [ ] 2 · Rails: Claims & Wiki (R4–R7)
> - [ ] 3 · Transformations (T1–T4)

---

## S1 — Sanskrit root text: source + IDs

**Title:** `S1 [Bodhicharyavatara] Sanskrit root text: source high-quality edition + assign IDs`
**Labels:** `artifact`, `stage:sources`, `root-text`
**Body:**

> **Output:** `1-SOURCES/Text/`
>
> - [ ] Source a high-quality Sanskrit edition of the root text (note edition/provenance, e.g. Minayev, Vaidya, La Vallée Poussin)
> - [ ] Record source metadata (edition, editor, year, digital source)
> - [ ] Assign chapter/section IDs
> - [ ] Assign verse IDs
> - [ ] Validate ID scheme is consistent with project-wide conventions (`4-SYSTEM/Docs/`)

---

## S2 — Tibetan root text: editions → proofread edition → IDs → Sanskrit links

**Title:** `S2 [Bodhicharyavatara] Tibetan root text: multi-edition sourcing, proofread edition, IDs, verse-level Sanskrit alignment`
**Labels:** `artifact`, `stage:sources`, `root-text`
**Body:**

> **Output:** `1-SOURCES/Text/`
>
> - [ ] Source multiple Tibetan editions of the root text (Derge, Narthang, Peking, Cone, modern editions…)
> - [ ] Collate and produce one well-proofread, high-quality Tibetan edition
> - [ ] Proofreading pass reviewed (record who/what verified)
> - [ ] Assign chapter/section IDs
> - [ ] Assign verse IDs
> - [ ] Link Tibetan verses to Sanskrit verses at the verse level (handle verse-count mismatches explicitly)

---

## S3 — Human translations: source, IDs, verse links

**Title:** `S3 [Bodhicharyavatara] Existing human translations: source, assign IDs, link to root text`
**Labels:** `artifact`, `stage:sources`, `translations`
**Body:**

> **Output:** `1-SOURCES/Translations/`
>
> Per language/translation (add a checkbox per translation found):
> - [ ] Inventory existing human translations (English, Chinese, Hindi, French, …) with rights/licensing notes
> - [ ] Ingest each translation
> - [ ] Assign chapter/section IDs
> - [ ] Assign verse IDs
> - [ ] Link each translation to the root text at verse level

---

## S4 — Commentaries: gather, IDs, verse links

**Title:** `S4 [Bodhicharyavatara] Commentaries: gather all, assign IDs, link to root text at verse level`
**Labels:** `artifact`, `stage:sources`, `commentaries`
**Body:**

> **Output:** `1-SOURCES/Commentaries/`
>
> - [ ] Compile a complete inventory of existing commentaries (Indian + Tibetan; note author, century, lineage)
> - [ ] Ingest each commentary (one checkbox per commentary as inventory firms up)
> - [ ] Assign chapter/section IDs to each commentary
> - [ ] Link each commentary to the root text at verse level
> - [ ] Record coverage map: which verses each commentary actually comments on

---

## R1 — Sections: raw TOCs

**Title:** `R1 [Bodhicharyavatara] Sections/RAW: extract table of contents for every text`
**Labels:** `artifact`, `stage:rails`, `sections`
**Body:**

> **Output:** `2-RAILS/Sections/RAW/`
>
> - [ ] Extract TOC for the root text
> - [ ] Extract TOC for each commentary (sa bcad)
> - [ ] Normalize TOC format (one raw file per text)
> - [ ] Cross-check TOC nodes against assigned section IDs

---

## R2 — Sections: multilevel summaries

**Title:** `R2 [Bodhicharyavatara] Sections: one file per TOC level with section summaries`
**Labels:** `artifact`, `stage:rails`, `sections`
**Body:**

> **Output:** `2-RAILS/Sections/`
>
> - [ ] Define file-per-level structure from the raw TOCs
> - [ ] Generate summary for each section at every level (multilevel summaries)
> - [ ] Review summaries for accuracy against the source sections
> - [ ] Link section files to verse ranges

---

## R3 — Verses: per-verse commentary compilations

**Title:** `R3 [Bodhicharyavatara] Verses: one file per root verse compiled from all commentaries`
**Labels:** `artifact`, `stage:rails`, `verses`
**Body:**

> **Output:** `2-RAILS/Verses/` — one file per root verse containing:
>
> - [ ] All explanations from commentaries
> - [ ] Key concepts / teaching points
> - [ ] Stories / narratives
> - [ ] Metaphors & examples
> - [ ] Quotations
> - [ ] Key terms
> - [ ] AI overview (Google-style)
>
> Tasks:
> - [ ] Define per-verse file template
> - [ ] Run extraction across all commentaries
> - [ ] Spot-check N verses per chapter for extraction quality

---

## R4 — Claims: raw per-commentary extraction

**Title:** `R4 [Bodhicharyavatara] Claims/RAW: one file per commentary with all relevant claims/facts`
**Labels:** `artifact`, `stage:rails`, `claims`
**Body:**

> **Output:** `2-RAILS/Claims/RAW/`
>
> - [ ] Define claim extraction criteria (claims are **not limited** to claims/facts about this text alone)
> - [ ] One raw claims file per commentary
> - [ ] Each claim carries a citation back to its commentary location (chapter/section/verse ID)

---

## R5 — Claims: consolidated per-claim files

**Title:** `R5 [Bodhicharyavatara] Claims: one file per claim/question with answers from all commentaries`
**Labels:** `artifact`, `stage:rails`, `claims`
**Body:**

> **Output:** `2-RAILS/Claims/`
>
> - [ ] Cluster/dedupe raw claims into canonical claims/questions
> - [ ] One file per claim/question, aggregating answers from every commentary that addresses it
> - [ ] Preserve per-commentary citations
> - [ ] Flag contradictions between commentaries explicitly

---

## R6 — Local-Wiki: keyword lists (raw)

**Title:** `R6 [Bodhicharyavatara] Local-Wiki/RAW: TF-IDF + YAKE keyword lists, combined en + bo keyword lists`
**Labels:** `artifact`, `stage:rails`, `local-wiki`
**Body:**

> **Output:** `2-RAILS/Local-Wiki/RAW/`
>
> - [ ] TF-IDF English keyword list
> - [ ] YAKE English n-gram list
> - [ ] `keywords.md` — combined English list (merge + curate the two above)
> - [ ] `keywords.md` — Tibetan list
> - [ ] Manual curation pass: drop noise, merge variants, map en ↔ bo keyword pairs

---

## R7 — Local-Wiki: articles

**Title:** `R7 [Bodhicharyavatara] Local-Wiki: one article per keyword (claims → TOC → draft → polished Tibetan)`
**Labels:** `artifact`, `stage:rails`, `local-wiki`
**Body:**

> **Output:** `2-RAILS/Local-Wiki/` — one article per keyword, built in 4 passes:
>
> - [ ] **Pass 1:** List of claims + citations from commentaries for the keyword
> - [ ] **Pass 2:** Article TOC — organize the claim list into categories
> - [ ] **Pass 3:** Draft article stitched from citations (Claude skills)
> - [ ] **Pass 4:** Polished article in plain Tibetan, authored by Gemini, with sources as links
> - [ ] QA sample: review N articles end-to-end for citation fidelity

---

## T1 — Transformations: plans

**Title:** `T1 [Bodhicharyavatara] Transformations: plans`
**Labels:** `artifact`, `stage:transformations`, `plans`
**Body:**

> **Output:** `3-TRANSFORMATIONS/Plans/`
>
> - [ ] Define plan deliverables (scope TBD)
> - [ ] Produce plans from rails context

---

## T2 — Transformations: translations

**Title:** `T2 [Bodhicharyavatara] Transformations: translations`
**Labels:** `artifact`, `stage:transformations`, `translation-out`
**Body:**

> **Output:** `3-TRANSFORMATIONS/Translations/`
>
> - [ ] Define target languages and translation workflow (scope TBD)
> - [ ] Produce translations grounded in rails context (verses, claims, wiki)

---

## T3 — Transformations: short videos

**Title:** `T3 [Bodhicharyavatara] Transformations: short videos`
**Labels:** `artifact`, `stage:transformations`, `video`
**Body:**

> - [ ] Define video format, audience, and cadence (scope TBD)
> - [ ] Script generation from rails context (verses, stories, metaphors)
> - [ ] Production workflow

---

## T4 — Transformations: e-learning course

**Title:** `T4 [Bodhicharyavatara] Transformations: e-learning course`
**Labels:** `artifact`, `stage:transformations`, `elearning`
**Body:**

> - [ ] Define course structure, platform, and audience (scope TBD)
> - [ ] Build course units from section summaries + verse files
> - [ ] Assessments / interactive elements
