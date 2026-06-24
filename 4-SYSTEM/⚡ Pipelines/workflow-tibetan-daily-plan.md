# Daily Plan Creation Workflow — Tibetan

**365-Day Bodhisattvacharyavatara Practice Plan · བྱང་ཆུབ་སེམས་དཔའི་སྤྱོད་པ་ལ་འཇུག་པ།**
`Skill: bca-practice-plan` · Language: བོད་སྐད།

---

## ① Required Documents & Inputs

| Layer | File | Purpose |
|---|---|---|
| `1-SOURCES` · Root Text | `bo-བློ་ལྡན་ཤེས་རབ།-དངུལ་ཆུ་ཐོགས་མེད་སྤྱོད་འཇུག་རྩ་བ།.md` | Canonical Tibetan root text — extract verses exactly by `^chapter-verse` block ID. Never quote from memory. |
| `1-SOURCES` · Commentary | `bo-དངུལ་ཆུ་ཐོགས་མེད།.md` | Ngulchu Thokme's *Ocean of Good Explanations* — extract commentary passages directly. Never invent. |
| Skill Reference | `Skills/365-day.../references/verse-schedule.md` | Day-by-day verse assignments — consult when only a day number is given |

---

## ② Daily Planning Workflow

### Step 1 — Skill Check & Identify Day

> [!info] Workflow Governance · Schedule Lookup
> Open `SKILLS-CATALOG.md`, confirm `bca-practice-plan` is the matching skill. Determine day number (1–365). If no verse range is provided, look up chapter and verses from `references/verse-schedule.md`.

### Step 2 — Read Both Source Files

> [!info] Textual Research · Block-ID Navigation · Citation Integrity
> Read `bo-བློ་ལྡན་ཤེས་རབ།…རྩ་བ།.md` and extract verses exactly using `^chapter-verse` block references. Read `bo-དངུལ་ཆུ་ཐོགས་མེད།.md` and extract relevant commentary passages.
>
> **If a verse or its commentary cannot be located in the source files, state this explicitly — do not substitute your own words.**

### Step 3 — Compose the Document (Header + 5 Sections)

> [!info] Classical Tibetan Composition · Register Adaptation · Structural Formatting
> Generate document with mandatory header first, then five sections in order. Fixed sections reproduced verbatim; variable sections generated from source material.

#### Document Header (Mandatory — before Section 1)

```
---
# ཉིན་ [DAY_NUMBER_TIBETAN] - ཉིན་ ༣༦༥ ཡི་སྤྱོད་འཇུག་སློབ་སྦྱོང།

## སྤྱོད་འཇུག་ལེའུ་[CHAPTER_ORDINAL]། ཤློཀ་ [START] - [END]

---
```

> [!warning]
> The blank line before the first `---` is required. Without it, Obsidian parses the header as YAML frontmatter and hides the title.

#### Section Structure

| Section | Type | Rules |
|---|---|---|
| **§ 1 — སྐྱབས་འགྲོ་སེམས་བསྐྱེད།** | Fixed | Refuge + Bodhicitta vow. Two prayer stanzas, verbatim every day. |
| **§ 2 — ཕན་ཡོན།** | Generated | Exactly 3 bullet points. Each title **must end** `འི་ཕན་ཡོན།`. Specific to today's verses. Neutral teacher tone — no first person (ངས་/ང་རང་). |
| **§ 3 — དེ་རིང་གི་རྩ་ཚིག** | Generated | **3.1:** All verses first (exact text from source, in sequence). **3.2:** Commentary per verse — `ངོས་འཛིན།` then `འགྲེལ་བཤད།`. No interleaving. No `#### ༣.༡` / `#### ༣.༢` headings in output. |
| **§ 4 — ཉམས་སུ་ལེན་ཚུལ།** | Generated | Exactly 1 point. **First person singular** (ངས་ / བདག་གིས་). Concrete, real-life application of today's verses. Never collective ང་ཚོས་. |
| **§ 5 — བསྔོ་བ་དང་སྨོན་ལམ།** | Fixed | Dedication + Aspiration. Two prayer stanzas, verbatim every day. |

#### Section 3 Commentary Format (per verse)

```
#### **N. ཤློཀ་[ordinal]།** (ལེའུ་ C ཤློཀ་ N)     ← verse header
> [exact verse text]                               ← block-quote, exact from source

#### **N. ཤློཀ་[ordinal]།** འགྲེལ་བཤད།             ← commentary header
- **ངོས་འཛིན།**: [one sentence ending …སྟོན་པའི་རྩ་ཚིག་ཡིན་ནོ། །]
- **འགྲེལ་བཤད།**: ཤློཀ་འདིའི་དོན་ནི་ … ཞེས་པའོ། །
```

> [!warning] Tone Rules
> - **§2 and §3.2:** Neutral, explanatory, teacher voice. No first person (ངས་ / ང་རང་ / བདག་གིས་). May address reader as ཁྱེད་.
> - **§4 only:** First person singular (ངས་ / བདག་གིས་). Never ང་ཚོས་ / ང་ཚོ་ anywhere.
> - Sentences connected by conjunctive particles: དང་། བཅས་། ཏེ། ནས། ཞིང་།
> - End substantive paragraphs with: ཡིན་ནོ།། or འགྱུར་རོ།། or ལགས་སོ།།
> - No Dzongkha grammatical patterns. No staccato clauses.
> - Śāntideva always: རྒྱལ་སྲས་ཆེན་པོ་ཞི་བ་ལྷ། — never just ཞི་བའི་ལྷ།

### Step 4 — Quality Checklist

> [!note] Quality Assurance · Grammar Review · Source Verification
> - [ ] Document header present, with day/chapter/verse in Tibetan numerals, positioned before §1
> - [ ] All 5 sections present with correct numbering (༡། through ༥།)
> - [ ] §1 and §5 match fixed prayer texts exactly — not paraphrased
> - [ ] Exactly 3 benefit bullets in §2 — each title ends `འི་ཕན་ཡོན།`
> - [ ] §3: no `#### ༣.༡ རྩ་ཚིག` / `#### ༣.༢ འགྲེལ་བཤད།` headings in output
> - [ ] §3 verse headers use real chapter verse numbers matching assigned range
> - [ ] §3.1 verses copied exactly from source file (not from memory)
> - [ ] §3.2 `འགྲེལ་བཤད།` extracted from `bo-དངུལ་ཆུ་ཐོགས་མེད།.md`; starts `ཤློཀ་འདིའི་དོན་ནི་`, ends `ཞེས་པའོ། །`
> - [ ] §4 uses first person singular — never collective ང་ཚོས་
> - [ ] §2 and §3.2 use neutral tone — no first person
> - [ ] Tibetan grammar correct: case endings, verb forms, particles throughout
> - [ ] Sentences flow with connective particles — no clipped clauses
> - [ ] Filename: `Day-[N]-Ch[C]-V[start]-[end].md` — no zero-padding, uppercase V

### Step 5 — Checklist Pass? ⬦ Decision Point

> [!warning] Problem-Solving · Iterative Revision
> - **Yes →** save file
> - **No →** revise failing section(s) and repeat checklist
> - **Verse/commentary not found in source →** stop and state explicitly — do not substitute

### ✓ Save Output File

> [!success] File Management · Metadata Governance
> Save to: `3-TRANSFORMATIONS/Plans/the-bodhisattva-challenge/bo/days/`
> Filename format: `Day-[N]-Ch[C]-V[start]-[end].md`
> Example: `Day-1-Ch1-V1-3.md`

---

## ③ Skills & Competencies by Stage

| Stage | Skills Required |
|---|---|
| Skill check & setup | Workflow governance, schedule lookup |
| Source gathering | Textual research, block-ID navigation, citation integrity |
| Composition — fixed sections | Liturgical precision, verbatim reproduction |
| Composition — benefits §2 | Verse-specific analysis, pedagogical framing, neutral register |
| Composition — verses §3.1 | Source extraction, Tibetan numerals, header formatting |
| Composition — commentary §3.2 | Commentary summarisation, modern Tibetan rendering, structural formulas |
| Composition — application §4 | Personal practice framing, first-person register, real-life application |
| Quality checklist | Quality assurance, Tibetan grammar review, source verification |
| Revision loop | Problem-solving, iterative revision |

---

## Key Constraints

> [!warning] Non-negotiable rules
> - **Two source files only:** root text + Ngulchu Thokme commentary — no other sources
> - **No parametric knowledge:** verse text and commentary must come from the files
> - **No fabrication:** if content cannot be found in source files, state this and stop
> - **Tone split is strict:** first person in §4 only; neutral in §2 and §3.2; no collective anywhere
> - **Citation chain:** `1-SOURCES → content` — rails are not required for the Tibetan stream
