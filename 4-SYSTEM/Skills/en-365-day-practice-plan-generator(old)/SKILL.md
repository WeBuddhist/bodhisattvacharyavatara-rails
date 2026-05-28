---
name: en-365-day-practice-plan-generator
description: Generate a complete single-day Bodhisattvacharyavatara (སྤྱོད་འཇུག) practice plan session document in the traditional 7-section format, in English, with combined commentary summaries. Saves to 3-TRANSFORMATIONS/Plans/spyod-jug-365/en/Days/.
---

---
# 365-Day Bodhisattvacharyavatara English Practice Plan Generator

This skill generates a single day's structured daily practice plan document in English for a 365-day study of Śāntideva's *Bodhisattvacharyavatara* (སྤྱོད་འཇུག). Each day produces a complete, self-contained 7-section markdown file in English, following the traditional format used in this vault.

---

## What you're building

Each practice plan is a self-contained daily session that:
- Opens with fixed refuge and bodhicitta prayers in both Tibetan and English.
- Sets a contextual motivation/benefit for the day's topic based on traditional commentaries.
- Explores the specific BCA verses assigned to that day, displaying both the Tibetan root text and its English translation.
- Provides a combined English commentary summary for each verse, synthesizing the explanations from Gyaltsab Darma Rinchen, Sazang Mati Panchen, and Ngulchu Thokme Zangpo.
- Offers practical daily life applications.
- Closes with fixed dedication and aspiration prayers in both Tibetan and English.
- Concludes with a Key Terms Glossary defining notable Tibetan terms in English.

The output is always saved as an English-language markdown file in `3-TRANSFORMATIONS/Plans/spyod-jug-365/en/Days/`.

---

## Source files

| File | Purpose |
|------|---------|
| `1-SOURCES/Translations/bo-བློ་ལྡན་ཤེས་རབ།.md` | **Root text** — canonical Tibetan translation by Blo ldan shes rab. **Always read this file and extract verses directly from it.** |
| `3-TRANSFORMATIONS/Translations/en-ai/Chapter one (Claude AI).md` | **English Verse Translation** — AI-generated English translation of the verses. (Or other verified English translations in `1-SOURCES/Translations/` like Wallace or Padmakara if requested). |
| `3-TRANSFORMATIONS/Translations/en-ai/Verses/<verse-id>.md` | **Verse-specific Commentary Summaries** — Pre-generated commentary explanations and summaries for Gyaltsab, Sazang, and Thokme in English. **Always prioritize reading these files first to extract commentary summaries.** |
| `3-TRANSFORMATIONS/Translations/en-ai/en-AI-generated-commentary-gyaltsab.md`<br>`3-TRANSFORMATIONS/Translations/en-ai/en-AI-generated-commentary-sazang.md`<br>`3-TRANSFORMATIONS/Translations/en-ai/en-AI-generated-commentary-thokme.md` | **Full English Commentaries** — Full AI-generated English translations of Gyaltsab, Sazang, and Thokme's commentaries. Use these if verse-specific summary files do not exist. |

---

## Step 1 — Gather inputs

Ask the user (or infer from context) for:

1. **Day number** (1–365) — required.
2. **Chapter** and **verse range** — if not provided, look up from the schedule in `4-SYSTEM/Skills/365-day-practice-plan-generator/references/verse-schedule.md`.
3. **Save location** — always defaults to: `3-TRANSFORMATIONS/Plans/spyod-jug-365/en/Days/`.

If the user only gives a day number, consult the verse schedule to find the chapter and verses for that day.

Once you have the chapter and verse range, **read the source files** before writing any content. Extract the exact Tibetan verse text, English verse translation, and the relevant commentary passages or summaries.

---

## Step 2 — Compose the 7-section document

Generate the complete document in English using the template below. The fixed sections are provided word-for-word; the variable sections must be generated freshly based on the specific chapter and verses.

### Document Frontmatter & Headers [MANDATORY]

The document frontmatter and header must appear at the very top of the file:

```yaml
---
day: [DAY_NUMBER]
chapter: [CHAPTER_NUMBER]
verses: "[CHAPTER_NUMBER]-[VERSE_START] to [CHAPTER_NUMBER]-[VERSE_END]"
status: draft
---

# Day [DAY_NUMBER] — Bodhisattvacharyavatara Practice Plan

## Chapter [CHAPTER_NUMBER]: [CHAPTER_TITLE_ENGLISH] — Verses [CHAPTER_NUMBER]-[VERSE_START] to [CHAPTER_NUMBER]-[VERSE_END]

---
```

---

### Section 1 — Refuge & Bodhicitta (སྐྱབས་འགྲོ་སེམས་བསྐྱེད།) [FIXED]

Always include this section verbatim:

```markdown
### 1. Refuge & Bodhicitta (སྐྱབས་འགྲོ་སེམས་བསྐྱེད།)

#### **1. Refuge (སྐྱབས་འགྲོ།)**
> བྱང་ཆུབ་སྙིང་པོར་མཆིས་ཀྱི་བར། །
> སངས་རྒྱས་རྣམས་ལ་སྐྱབས་སུ་མཆི། །
> ཆོས་དང་བྱང་ཆུབ་སེམས་དཔའ་ཡི། །
> ཚོགས་ལའང་དེ་བཞིན་སྐྱབས་སུ་མཆི། །
> 
> *Until I reach the heart of awakening,*
> *I take refuge in the Buddhas.*
> *Likewise, I take refuge in the Dharma*
> *And in the assembly of Bodhisattvas.*

```

---

### Section 2 — Benefit (ཕན་ཡོན།) [GENERATED]

Write exactly **3 benefit bullet points** in English. Open the section with this exact sentence:
`Based on the traditional commentaries of Gyaltsab Darma Rinchen, Sazang Mati Panchen, and Ngulchu Thokme Zangpo, practicing and reflecting on today's verses yields the following profound benefits:`

Each point should:
- Have a bold **title** (with an explanatory tag in parentheses, e.g., **Title (Tag):**)
- Follow with 2–3 sentences of explanation(not exceed 50 words )
- Be tied specifically to the themes of today's verses (not generic benefits)

Pattern to follow:
```markdown
### 2. Benefit (ཕན་ཡོན།)

Based on the traditional commentaries of Gyaltsab Darma Rinchen, Sazang Mati Panchen, and Ngulchu Thokme Zangpo, practicing and reflecting on today's verses yields the following profound benefits:

*   **[Benefit Title] ([Theme]):** [2–3 sentences of explanation]
*   **[Benefit Title] ([Theme]):** [2–3 sentences of explanation]
*   **[Benefit Title] ([Theme]):** [2–3 sentences of explanation]
```

---

### Section 3 — Today's Root Verses & Commentaries (དེ་རིང་གི་སྤྱོད་འཇུག་རྩ་ཚིག་དངོས།) [GENERATED]

For each verse in the assigned range, output the root verse in Tibetan and English, followed by a synthesized, combined commentary summary.

Format:
```markdown
### 3. Today's Root Verses & Commentaries (དེ་རིང་གི་སྤྱོད་འཇུག་རྩ་ཚིག་དངོས།)

#### **Verse [CHAPTER_NUMBER]-[VERSE_NUMBER]**
> [Tibetan Root Verse from bo-བློ་ལྡན་ཤེས་རབ།.md]
> 
> *[English Verse Translation]*

##### **Combined Commentary Summary for Verse [CHAPTER_NUMBER]-[VERSE_NUMBER]**
[Provide a synthesized, cohesive, and well-structured English summary of the explanations from Gyaltsab Darma Rinchen, Sazang Mati Panchen, and Ngulchu Thokme Zangpo. Instead of separate bullet points, write a unified narrative of 1-2 lines that hightling the key points and concepts.]
```

> ⚠️ **Critical rule for Section 3**: Both verse text and commentary explanations must come from the source files. If you cannot locate a verse or its commentary in the files, state this explicitly — do not invent or substitute your own words.

---

### Section 4 — Daily Life Application (ཉིན་རེའི་འཚོ་བའི་ནང་ཉམས་སུ་ལེན་ཚུལ།) [GENERATED]

Write exactly **3 practical application points** in English. Each should:
- Have a numbered bold label (e.g., `*   **1. [Short descriptive title]:**`)
- Give a concrete, actionable instruction for how to bring the verse's teaching into today's ordinary life.
- Ground each point in the specific verses studied today — avoid generic mindfulness advice.

Pattern:
```markdown
### 4. Daily Life Application (ཉིན་རེའི་འཚོ་བའི་ནང་ཉམས་སུ་ལེན་ཚུལ།)

*   **1. [Descriptive Title]:** [Concrete daily life instruction]
*   **2. [Descriptive Title]:** [Concrete daily life instruction]
*   **3. [Descriptive Title]:** [Concrete daily life instruction]
```

---

### Section 5 — Dedication & Aspiration (བསྔོ་བ་དང་སྨོན་ལམ།) [FIXED]

Always include this section verbatim:

```markdown
### 5. Dedication & Aspiration (བསྔོ་བ་དང་སྨོན་ལམ།)

#### **1. Dedication (བསྔོ་བ།)**
> བདག་གིས་བྱང་ཆུབ་སྤྱོད་པ་ལ། །
> འཇུག་པ་རྣམ་པར་བརྩམས་པ་ཡི། །
> དགེ་བ་གང་དེས་འགྲོ་བ་ཀུན། །
> བྱང་ཆུབ་སྤྱོད་ལ་འཇུག་པར་ཤོག །
> 
> *By the virtue accumulated*
> *Through composing this entry into the Bodhisattva conduct,*
> *May all wandering beings without exception*
> *Engage in the Bodhisattva conduct.*

#### **2. Aspiration (སྨོན་ལམ།)**
> བྱང་ཆུབ་སེམས་མཆོག་རིན་པོ་ཆེ། །
> མ་སྐྱེས་པ་རྣམས་སྐྱེ་གྱུར་ཅིག །
> སྐྱེས་པ་ཉམས་པ་མེད་པ་དང་། །
> གོང་ནས་གོང་དུ་འཕེལ་བར་ཤོག །
> 
> *May the precious and supreme mind of awakening,*
> *Where it has not arisen, arise;*
> *Where it has arisen, may it not decline,*
> *But increase further and further.*
```

---

### Section 6 — Key Terms Glossary (གནད་ཚིག་ཁག་གི་འགྲེལ་བཤད།) [GENERATED]

Select 3–6 key Tibetan terms that appear in today's verses. For each:
- Bold the Tibetan term
- Provide an English translation in parentheses
- Write 2–4 sentences defining how the term is used in this specific verse/chapter context (drawing on the commentaries).

Pattern:
```markdown
### 6. Key Terms Glossary (གནད་ཚིག་ཁག་གི་འགྲེལ་བཤད།)

*   **[Tibetan term] ([English gloss]):** [Contextual definition]
```

---

## Step 3 — Save the file

Save the file to `3-TRANSFORMATIONS/Plans/spyod-jug-365/en/Days/[DAY_NUMBER].md`.

- Filename format: `[DAY_NUMBER].md` (e.g. `1.md`, `2.md`, `45.md` — no zero-padding).
- Target directory: `3-TRANSFORMATIONS/Plans/spyod-jug-365/en/Days/`

After saving, present the saved path to the user along with a brief, one-sentence summary of the day's verses.

---

## Quality checklist before saving

- [ ] Frontmatter and headers present with correct day, chapter, and verse range.
- [ ] Section titles match exactly (numbered 1 to 6).
- [ ] Section 1 and Section 5 match the fixed Tibetan and English prayer texts **exactly**.
- [ ] Benefit section has exactly 3 bullet points with bold titles and parenthetical themes.
- [ ] Root verses copied exactly from `1-SOURCES/Translations/bo-བློ་ལྡན་ཤེས་རབ།.md`.
- [ ] English verse translations extracted from `3-TRANSFORMATIONS/Translations/en-ai/Chapter one (Claude AI).md` (or other verified translation).
- [ ] Combined commentary summary under each verse is accurate, well-structured, and synthesizes the perspectives of Gyaltsab, Sazang, and Thokme.
- [ ] Daily life application has exactly 3 numbered, actionable points.
- [ ] Glossary has 3–6 terms with contextual, commentary-based definitions.
- [ ] Saved exactly to `3-TRANSFORMATIONS/Plans/spyod-jug-365/en/Days/[DAY_NUMBER].md`.