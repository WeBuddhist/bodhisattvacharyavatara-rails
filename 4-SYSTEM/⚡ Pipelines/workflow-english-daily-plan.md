# Daily Plan Creation Workflow — English

**The Bodhisattva Challenge · One Year Training in the Way of the Bodhisattva**
`Skill: english-plan-generator` · Language: English

---

## ① Required Documents & Inputs

| Layer | File | Purpose |
|---|---|---|
| `1-SOURCES` | `bo-བློ་ལྡན་ཤེས་རབ།.md` | Root Text (Tibetan) — extract verses exactly by block ID |
| `1-SOURCES` | Classical Commentaries | Gyaltsab, Sazang Mati Panchen, Ngulchu Thokme |
| `1-SOURCES` | `Translations/` + `References/` | Existing translations and reference material |
| `2-RAILS` | `Verses/<verse-id>.md` ★ `status: complete` | Verse context packages — preferred source for §2.4 + §2.6 |
| `2-RAILS` | `Sections/<node-id>.md` | Section context for transition days |
| `3-TRANSFORMATIONS` | `en-ai/en-AI-generated-root-loden-sherab.md` | AI English translation — locate verses by block ID |
| `3-TRANSFORMATIONS` | `en-ai/Verses/<verse-id>.md` | Interim commentary summaries (fallback only) |
| Plan Assets | `en/assets/schedule-corrected.md` | Verse schedule — maps day numbers to chapter + verse range |
| Plan Assets | `en/assets/liturgy.md` | Fixed liturgy — reproduced verbatim in §2.2 and §2.5 |
| Plan Contracts | `en/requirements.md` | Style contract — all rules binding |
| Plan Contracts | `en/termbase.md` | Vocabulary contract — one rendering per keyword |

---

## ② Daily Planning Workflow

### Step 1 — Skill Check

> [!info] Workflow Governance · Information Retrieval
> Open `4-SYSTEM/Skills/SKILLS-CATALOG.md`. Confirm `english-plan-generator` is the matching skill. Read its `SKILL.md` in full before proceeding — all rules there are binding.

### Step 2 — Identify Day & Verse Range

> [!info] Scheduling · Cross-reference Lookup
> Determine the day number (1–365). Look up chapter and verse range in `en/assets/schedule-corrected.md` if not provided.

### Step 3 — Rail Status Check ⬦ Decision Point

> [!warning] Source Validation · Risk Flagging
> **Are `2-RAILS/Verses/<verse-id>.md` packages marked `status: complete`?**
>
> - **Yes →** use preferred rail sources for §2.4 + §2.6
> - **No →** fall back to interim summaries in `en-ai/Verses/`; record `generation_note` in frontmatter
> - **Neither exists →** stop and flag the dependency — do not invent content

### Step 4 — Gather All Source Material

> [!info] Textual Research · Block-ID Navigation · Citation Tracing
> Read root text verses (Tibetan), AI-generated English translation (by block ID), verse context rails, section rails, fixed liturgy, `requirements.md`, and `termbase.md`. Read everything before writing.

### Step 5 — Compose the 6-Section Day File

> [!info] Content Generation · Register Adaptation · Structural Formatting
> Generate the complete day document. Fixed sections reproduced verbatim; variable sections generated fresh from source material.

| Section | Type | Rules |
|---|---|---|
| **§ 2.1 — Opening** | Variable | 2–4 sentences, ≤60 words. Orients reader within section/chapter structure. No summary, no teaching. |
| **§ 2.2 — Renewing the Bodhisattva Vow** | Fixed | Four immeasurables → refuge → vow. Verbatim from `liturgy.md`. No variation, no added headers. |
| **§ 2.3 — Today's Verses** | Sourced | Tibetan + English per verse, presented as a unit. Exact extraction only — no paraphrase. |
| **§ 2.4 — From the Tradition** | Variable | One concept/fact from commentaries not evident in verses. Prose only, ≤150 words. Named commentator. |
| **§ 2.5 — Aspiration** | Fixed | Aspiration + dedication. Verbatim from `liturgy.md`. Same rules as §2.2. |
| **§ 2.6 — Today's Practice Challenge** | Variable | One instruction, 2nd person present tense. Real situation. Traceable to §2.4 and named commentator. |

### Step 6 — Authenticity Test

> [!note] Critical Evaluation · Verse Specificity Check
> Each variable section must be verse-specific — not interchangeable with another day.
> - §2.4 must add something not derivable from reading the verse alone
> - §2.6 must name a real, recognisable situation
> - Swapping today's note with yesterday's should be immediately obvious

### Step 7 — Quality Checklist

> [!note] Quality Assurance · Format Compliance · Forbidden-Element Audit
> Verify all of the following before saving:
> - [ ] Frontmatter: `day`, `chapter`, `verses`, `status`, `generation_note` (if interim sources used)
> - [ ] Day title: notification text, ≤12 words, no rhetorical question, no affirmation
> - [ ] §2.2 and §2.5: liturgy verbatim, block-quote format, no added headers
> - [ ] §2.3: Tibetan exact from `bo-བློ་ལྡན་ཤེས་རབ།.md`; English from `en-AI-generated…`
> - [ ] §2.4: prose only, ≤150 words, one concept/fact, grounded in rails, named commentator
> - [ ] §2.6: one instruction, 2nd person, real situation, traceable to §2.4
> - [ ] No forbidden elements (benefits list, glossary, Tibetan section labels, bullet application blocks, "Today I will…", parenthetical tags, "profound benefits", "great teacher Shantideva", collective attribution opener)
> - [ ] No diacritics in English prose
> - [ ] No sub-headers below `##` level
> - [ ] No horizontal rules between sections

### Step 8 — Checklist Pass? ⬦ Decision Point

> [!warning] Problem-Solving · Iterative Revision
> - **Yes →** save file as `status: draft`
> - **No →** revise failing section(s) and repeat authenticity test from Step 6

### Step 9 — Save Output (status: draft)

> [!success] File Management · Metadata Governance
> Save to: `3-TRANSFORMATIONS/Plans/the-bodhisattva-challenge/en/Days/[DAY_NUMBER].md`
> Filename: `[DAY_NUMBER].md` — no zero-padding (e.g. `1.md`, `45.md`)

### Step 10 — Domain Specialist Review

> [!note] Stakeholder Review · Source Verification · Theological Accuracy
> A human expert reviews the draft against the source rails. Every claim in §2.4 and §2.6 must be traceable to a specific passage in the commentaries. **The LLM never sets its own status to `complete`.**

### ✓ Published — status: complete

> [!success] Publication Readiness · Multi-channel Communication
> Domain specialist sets `status: complete`. File is ready for publication. Push notification text is pulled directly from the day title.

---

## ③ Skills & Competencies by Stage

| Stage | Skills Required |
|---|---|
| Skill check & setup | Workflow governance, information retrieval |
| Source gathering | Textual research, block-ID navigation, citation tracing |
| Rail validation | Source validation, risk flagging |
| Composition | Content generation, register adaptation, structural formatting |
| Authenticity test | Critical evaluation, verse specificity check |
| Quality checklist | Quality assurance, format compliance, forbidden-element audit |
| Revision loop | Problem-solving, iterative revision |
| File saving | File management, metadata governance |
| Specialist review | Stakeholder coordination, source verification, theological accuracy |

---

## Key Constraints

> [!warning] Non-negotiable rules
> - **Citation chain:** `1-SOURCES → 2-RAILS → 3-TRANSFORMATIONS` — never skip a link
> - **Rail status:** only `status: complete` rails used for §2.4 + §2.6
> - **No parametric knowledge:** every claim must trace to a source file
> - **LLM never self-certifies:** domain specialist sets `complete`
> - **Forbidden elements list:** see SKILL.md §"What is not permitted"
