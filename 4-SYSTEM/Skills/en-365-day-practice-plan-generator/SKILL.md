---
name: en-365-day-practice-plan-generator
description: Generate a complete single-day Bodhisattvacharyavatara (སྤྱོད་འཇུག) practice plan session document in the traditional 7-section format, in English, with combined commentary summaries. Saves to 3-TRANSFORMATIONS/Plans/spyod-jug-365/en/Days/.
---

# 365-Day Bodhisattvacharyavatara English Practice Plan Generator

This skill generates a single day's structured daily practice plan document in English for a 365-day study of Śāntideva's _Bodhisattvacharyavatara_ (སྤྱོད་འཇུག). Each day produces a complete, self-contained 7-section markdown file in English, following the traditional format used in this vault.

## What you're building

Each practice plan is a self-contained daily session that:

- Opens with fixed refuge and bodhicitta prayers in English.
- Sets a contextual motivation/benefit for the day's topic based on traditional commentaries.
- Explores the specific BCA verses assigned to that day, displaying both the Tibetan root text and its English translation.
- Provides a combined English commentary summary for each verse, synthesizing the explanations from Gyaltsab Darma Rinchen, Sazang Mati Panchen, and Ngulchu Thokme Zangpo.
- Offers practical daily life applications.
- Closes with fixed dedication and aspiration prayers in English.
- Concludes with a Key Terms Glossary defining notable terms in English.
    

The output is always saved as an English-language markdown file in `3-TRANSFORMATIONS/Plans/spyod-jug-365/en/Days/`.

## Source files

|                                                                                                                                                                                                                                                                         |                                                                                                                                                                                                                             |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **File**                                                                                                                                                                                                                                                                | **Purpose**                                                                                                                                                                                                                 |
| `1-SOURCES/Translations/bo-བློ་ལྡན་ཤེས་རབ།.md`                                                                                                                                                                                                                          | **Root text** — canonical Tibetan translation by Blo ldan shes rab. **Always read this file and extract verses directly from it.**                                                                                          |
| `3-TRANSFORMATIONS/Translations/en-ai/en-AI-generated-root-loden-sherab.md`                                                                                                                                                                                             | **English Verse Translation** — AI-generated English translation of the verses. (Or other verified English translations in `1-SOURCES/Translations/` like Wallace or Padmakara if requested).                               |
| `3-TRANSFORMATIONS/Translations/en-ai/Verses/<verse-id>.md`                                                                                                                                                                                                             | **Verse-specific Commentary Summaries** — Pre-generated commentary explanations and summaries for Gyaltsab, Sazang, and Thokme in English. **Always prioritize reading these files first to extract commentary summaries.** |
| `3-TRANSFORMATIONS/Translations/en-ai/en-AI-generated-commentary-gyaltsab.md`<br><br>  <br><br>`3-TRANSFORMATIONS/Translations/en-ai/en-AI-generated-commentary-sazang.md`<br><br>  <br><br>`3-TRANSFORMATIONS/Translations/en-ai/en-AI-generated-commentary-thokme.md` | **Full English Commentaries** — Full AI-generated English translations of Gyaltsab, Sazang, and Thokme's commentaries. Use these if verse-specific summary files do not exist.                                              |

## Step 1 — Gather inputs

Ask the user (or infer from context) for:

1. **Day number** (1–365) — required.
    
2. **Chapter** and **verse range** — if not provided, look up from the schedule in `4-SYSTEM/Skills/365-day-practice-plan-generator/references/verse-schedule.md`.
    
3. **Save location** — always defaults to: `3-TRANSFORMATIONS/Plans/spyod-jug-365/en/Days/`.
    

If the user only gives a day number, consult the verse schedule to find the chapter and verses for that day.

Once you have the chapter and verse range, **read the source files** before writing any content. Extract the exact Tibetan verse text, English verse translation, and the relevant commentary passages or summaries.

## Step 2 — Compose the 7-section document

Generate the complete document in English using the template below. The fixed sections are provided word-for-word; the variable sections must be generated freshly based on the specific chapter and verses.

### Document Frontmatter & Headers [MANDATORY]

The document frontmatter and header must appear at the very top of the file:

```
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

### Section 1 — Refuge (སྐྱབས་འགྲོ།) [FIXED]

Always include this section verbatim:

```
### 1. Refuge 

#### **1. Refuge (སྐྱབས་འགྲོ།)**

> *Until I reach the heart of awakening,*
> *I take refuge in the Buddhas.*
> *Likewise, I take refuge in the Dharma*
> *And in the assembly of Bodhisattvas.*

> *བྱང་ཆུབ་སྙིང་པོར་མཆིས་ཀྱི་བར། །*
> *སངས་རྒྱས་རྣམས་ལ་སྐྱབས་སུ་མཆི། །*
> *ཆོས་དང་བྱང་ཆུབ་སེམས་དཔའ་ཡི། །*
> *ཚོགས་ལའང་དེ་བཞིན་སྐྱབས་སུ་མཆི། །*
```

### Section 2 — Benefit (ཕན་ཡོན།) [GENERATED]

Write 1 benefit in plain English (Grade 8–10 reading level). Open the section with this exact sentence:

`Based on the traditional commentaries of Gyaltsab Darma Rinchen, Sazang Mati Panchen, and Ngulchu Thokme Zangpo, practicing and reflecting on today's verses yields the following profound benefits:`

Each point should:

- Have a bold **title** (with an explanatory tag in parentheses, e.g., **Title (Tag):**)
- Follow with 4–5 sentences of explanation (not exceeding 50 words).
- Use active voice, short sentences (15–20 words), and common English words (no jargon).
- Be tied specifically to the themes of today's verses (not generic benefits).
- Avoid Sanskrit/Tibetan transliterations (e.g., use "Enlightenment" instead of "Bodhi", "Hero of Enlightenment" instead of "Bodhisattva").
    

Pattern to follow:

```
### 2. Benefit (ཕན་ཡོན།)

Based on the traditional commentaries of Gyaltsab Darma Rinchen, Sazang Mati Panchen, and Ngulchu Thokme Zangpo, practicing and reflecting on today's verses yields the following profound benefit:

*   **[Benefit Title] ([Theme]):** [3–4 sentences of explanation]
*   **[Benefit Title] ([Theme]):** [3–4 sentences of explanation]
*   **[Benefit Title] ([Theme]):** [3–4 sentences of explanation]
```

### Section 3 — Today's Root Verses & Commentaries (དེ་རིང་གི་སྤྱོད་འཇུག་རྩ་ཚིག་དངོས།) [GENERATED]

For each verse in the assigned range, output the root verse in Tibetan and English, followed by a synthesized, combined commentary summary.

Format:

```
### 3. Today's Root Verses & Commentaries (དེ་རིང་གི་སྤྱོད་འཇུག་རྩ་ཚིག་དངོས།)

#### **Verse [CHAPTER_NUMBER]-[VERSE_NUMBER]**
> [Tibetan Root Verse from bo-བློ་ལྡན་ཤེས་རབ།.md]
> 
> *[English Verse Translation]*

##### **Combined Commentary Summary for Verse [CHAPTER_NUMBER]-[VERSE_NUMBER]**
[Provide a synthesized, cohesive, and well-structured English summary of the explanations from Gyaltsab Darma Rinchen, Sazang Mati Panchen, and Ngulchu Thokme Zangpo. 
**Crucial Style Constraints:** 
- Write in plain English suited for a Grade 8–10 reading level.
- Limit sentence length to 15–20 words and use active voice.
- Do NOT use transliterated Sanskrit or Tibetan terms (e.g., use "Enlightenment" instead of "Bodhi"). 
- Adapt any obscure traditional metaphors into functional modern equivalents.
- Instead of separate bullet points, write a unified narrative of 2-3 short sentences highlighting the key points and concepts.]
```

> ⚠️ **Critical rule for Section 3**: Both verse text and commentary explanations must come from the source files. If you cannot locate a verse or its commentary in the files, state this explicitly — do not invent or substitute your own words.

### Section 4 — Daily Life Application (ཉིན་རེའི་འཚོ་བའི་ནང་ཉམས་སུ་ལེན་ཚུལ།) [GENERATED]

Write  3 practical application points in plain, accessible English (Grade 8–10 level). Each should:

- Have a numbered bold label (e.g., `* 1. [Short descriptive title]:`)
- Give a concrete, actionable instruction for how to bring the verse's teaching into today's ordinary life.
- Ground each point in the specific verses studied today — avoid generic mindfulness advice.
- Use direct, clear language with active voice and strict sentence lengths of 15–20 words.
    

Pattern:

```
### 4. Daily Life Application (ཉིན་རེའི་འཚོ་བའི་ནང་ཉམས་སུ་ལེན་ཚུལ།)

*   **. [Descriptive Title]:** [Concrete daily life instruction]
*   **. [Descriptive Title]:** [Concrete daily life instruction]
*   **. [Descriptive Title]:** [Concrete daily life instruction]

```

### Section 5 — Dedication & Aspiration (བསྔོ་བ་དང་སྨོན་ལམ།) [FIXED]

Always include this section verbatim:

```
### 5. Dedication & Aspiration (བསྔོ་བ་དང་སྨོན་ལམ།)

#### **1. Dedication (བསྔོ་བ།)**

> *By the virtue accumulated*
> *Through composing this entry into the Bodhisattva conduct,*
> *May all wandering beings without exception*
> *Engage in the Bodhisattva conduct.*

> བདག་གིས་བྱང་ཆུབ་སྤྱོད་པ་ལ། །
> 
> འཇུག་པ་རྣམ་པར་བརྩམས་པ་ཡི། །
> 
> དགེ་བ་གང་དེས་འགྲོ་བ་ཀུན། །
> 
> བྱང་ཆུབ་སྤྱོད་ལ་འཇུག་པར་ཤོག །

#### **2. Aspiration (སྨོན་ལམ།)**

> *May the precious and supreme mind of awakening,*
> *Where it has not arisen, arise;*
> *Where it has arisen, may it not decline,*
> *But increase further and further.*

> བྱང་ཆུབ་སེམས་མཆོག་རིན་པོ་ཆེ། །
> 
> མ་སྐྱེས་པ་རྣམས་སྐྱེ་གྱུར་ཅིག །
> 
> སྐྱེས་པ་ཉམས་པ་མེད་པ་དང་། །
> 
> གོང་ནས་གོང་དུ་འཕེལ་བར་ཤོག །
```

### Section 6 — Key Terms Glossary (གནད་ཚིག་ཁག་གི་འགྲེལ་བཤད།) [GENERATED]

Select 3–6 key Tibetan terms that appear in today's verses. For each:

- Bold the Tibetan term.
    
- Provide its closest plain-English equivalent in parentheses (do not use Sanskrit transliterations like Bodhisattva; use "Hero of Enlightenment" or refer to the `termbase.md`).
    
- Write 2–4 short sentences (15–20 words each) defining how the term is used in this specific verse/chapter context.
    
- Ensure the definition uses common English words, avoids nested clauses, and contains no additional technical jargon.
    

Pattern:

```
### 6. Key Terms Glossary (གནད་ཚིག་ཁག་གི་འགྲེལ་བཤད།)

*   **[English term] ([Tibetan equivalent]):** [Contextual definition in plain English]
```

## Step 3 — Save the file

Save the file to `3-TRANSFORMATIONS/Plans/spyod-jug-365/en/Days/[DAY_NUMBER].md`.

- Filename format: `[DAY_NUMBER].md` (e.g. `1.md`, `2.md`, `45.md` — no zero-padding).
    
- Target directory: `3-TRANSFORMATIONS/Plans/spyod-jug-365/en/Days/`
    

After saving, present the saved path to the user along with a brief, one-sentence summary of the day's verses.

## Quality checklist before saving

- [ ] Frontmatter and headers present with correct day, chapter, and verse range.
    
- [ ] Section titles match exactly (numbered 1 to 6).
    
- [ ] Section 1 and Section 5 match the fixed Tibetan and English prayer texts **exactly**.
    
- [ ] Benefit section has exactly 3 bullet points written in plain English, avoiding jargon and transliteration.
    
- [ ] Root verses copied exactly from `1-SOURCES/Translations/bo-བློ་ལྡན་ཤེས་རབ།.md`.
    
- [ ] English verse translations extracted from `3-TRANSFORMATIONS/Translations/en-ai/Chapter one (Claude AI).md` (or other verified translation).
    
- [ ] Combined commentary summary is in plain English (Grade 8-10), strictly 15-20 words per sentence, active voice, and adapts complex metaphors.
    
- [ ] Daily life application has exactly 3 numbered, actionable points in clear, everyday language.
    
- [ ] Glossary has 3–6 terms translated to closest English equivalents (no transliteration) with jargon-free definitions.
    
- [ ] Saved exactly to `3-TRANSFORMATIONS/Plans/spyod-jug-365/en/Days/[DAY_NUMBER].md`.