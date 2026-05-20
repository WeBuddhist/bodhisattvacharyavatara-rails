---
name: bca-practice-plan
description: >
  Generate a complete single-day Bodhisattvacharyavatara (སྤྱོད་འཇུག) practice plan session
  document in the traditional 7-section format, in Tibetan. Use this skill whenever the user
  asks to create, generate, or produce a daily practice plan, practice session, or ཉམས་ལེན་
  document for the Bodhisattvacharyavatara (also written Bodhicaryavatara, Spyod 'jug, BCA,
  or Guide to the Bodhisattva's Way of Life). Trigger on phrases like "create a practice plan
  for day X", "generate today's BCA session", "make a Spyod 'jug practice plan", "365-day plan",
  "ཉམས་ལེན་", "སྤྱོད་འཇུག་སློབ་སྦྱོང", "generate a practice document", or any request for a
  structured daily Bodhisattvacharyavatara study/practice session. Always use this skill even
  when the user just says something like "make me today's Spyod 'jug" or "can you do day 45
  of the practice plan" — don't try to improvise a structure without this skill.
---

# 365-Day Bodhisattvacharyavatara Practice Plan Generator

This skill generates a single day's structured practice plan document for a 365-day study of Śāntideva's *Bodhisattvacharyavatara* (སྤྱོད་འཇུག). Each day produces a complete 7-section markdown file in Tibetan, following the traditional format used by Tigerboy (tigerboy@webuddhist.com).

---

## What you're building

Each practice plan is a self-contained daily session that:
- Opens with fixed refuge and bodhicitta prayers
- Sets a contextual motivation for the day's topic
- Explores the specific BCA verses assigned to that day
- Provides commentary, practical application, and a glossary
- Closes with fixed dedication and aspiration prayers

The output is always saved as a Tibetan-language markdown file.

---

## Step 1 — Gather inputs

Ask the user (or infer from context) for:

1. **Day number** (1–365) — required
2. **Chapter** (ལེའུ་) and **verse range** (ཤླཽཀ་) — if not provided, look up from the schedule in `references/verse-schedule.md`
3. **Save location** — default to the user's Obsidian folder: `C:\Users\tiger\Obsidian\bodhisattvacharyavatara-rails\0-INBOX\Plans\`
4. **Language for commentary** — default is Tibetan (བོད་སྐད།); English commentary notes can be added if the user asks

If the user only gives a day number, consult the verse schedule to find the chapter and verses for that day.

---

## Step 2 — Compose the 7-section document

Generate the complete document in Tibetan using the template below. The fixed sections are provided word-for-word; the variable sections must be generated freshly based on the specific chapter and verses.

### Document header

```
---
# ཉིན་ [DAY_NUMBER_TIBETAN] - ཉིན་ ༣༦༥ ཡི་སྤྱོད་འཇུག་སློབ་སྦྱོང།

## སྤྱོད་འཇུག་ལེའུ་[CHAPTER_ORDINAL]། ཤླཽཀ་ [VERSE_START_TIBETAN] - [VERSE_END_TIBETAN]

---
```

Convert day numbers, chapter numbers, and verse numbers to Tibetan numerals (see numeral table below).

---

### Section 1 — སྐྱབས་འགྲོ་སེམས་བསྐྱེད། (Refuge & Bodhicitta) [FIXED]

Always include these two sub-sections verbatim:

```markdown
### ༡། སྐྱབས་འགྲོ་སེམས་བསྐྱེད།

#### **༡. སྐྱབས་འགྲོ།** (སྤྱོད་འཇུག་ལེའུ་ ༢ ཤླཽཀ་ ༢༦)

> བྱང་ཆུབ་སྙིང་པོར་མཆིས་ཀྱི་བར། །
> 
> སངས་རྒྱས་རྣམས་ལ་སྐྱབས་སུ་མཆི། །
> 
> ཆོས་དང་བྱང་ཆུབ་སེམས་དཔའི། །
> 
> ཚོགས་ལའང་དེ་བཞིན་སྐྱབས་སུ་མཆི། །

#### **༢. སེམས་བསྐྱེད།** (སྤྱོད་འཇུག་ལེའུ་ ༣ ཤླཽཀ་ ༢༢ - ༢༣)

> ཇི་ལྟར་སྔོན་གྱི་བདེ་གཤེགས་ཀྱིས། །
> 
> བྱང་ཆུབ་ཐུགས་ནི་བསྐྱེད་པ་དང་། །
> 
> བྱང་ཆུབ་སེམས་དཔའི་བསླབ་པ་ལ། །
> 
> དེ་དག་རིམ་བཞིན་གནས་པ་ལྟར། །

> དེ་བཞིན་འགྲོ་ལ་ཕན་དོན་དུ། །
> 
> བྱང་ཆུབ་སེམས་ནི་བསྐྱེད་བགྱི་ཞིང་། །
> 
> དེ་བཞིན་དུ་ནི་བསླབ་པ་ལའང་། །
> 
> རིམ་པ་བཞིན་དུ་བསླབ་པར་བགྱི། །
```

---

### Section 2 — ཀུན་སློང་བཅོས་པ། (Setting the Motivation) [GENERATED]

Write a short motivational framing paragraph in Tibetan (3–5 sentences) that:
- Grounds the practitioner in the Three Jewels and bodhicitta
- Introduces the theme of today's chapter/verses in accessible terms
- Frames the day's study as a chance to recognize and work with inner afflictions (ཉོན་མོངས་པ།)
- Uses the **same voice and register** as the example: direct, encouraging, slightly literary Tibetan prose

Do not use bullet points here — it should read as connected prose, like a brief oral teaching opening.

---

### Section 3 — ཕན་ཡོན། (Benefits of Today's Verses) [GENERATED]

Write exactly **3 benefit bullet points** in Tibetan. Each point should:
- Have a bold **title** (4–7 Tibetan words) that names the specific benefit
- Follow with 2–3 sentences of explanation
- Be tied specifically to the themes of today's verses (not generic bodhisattva benefits)

Pattern to follow:
```markdown
*   **[Benefit title in Tibetan]** [2–3 sentences of explanation]
```

The three benefits should form a natural progression: from psychological/emotional freedom → clarifying one's focus/target → developing resilience/courage. Adapt this arc to the specific chapter content.

---

### Section 4 — དེ་རིང་གི་སྤྱོད་འཇུག་རྩ་ཚིག་དངོས། (Today's Root Verses with Commentary) [GENERATED]

For each verse being studied today:

1. **Header**: `#### **[Tibetan numeral]. ཤླཽཀ་[ordinal]།** (ལེའུ་ [chapter] ཤླཽཀ་ [number])`
2. **Verse block**: The full Tibetan verse in a blockquote, with `། །` line endings
3. **Commentary** (`*   **འགྲེལ་བཤད།**`): 4–8 sentences of Tibetan-language commentary that:
   - Unpacks the verse's literal meaning
   - Explains the philosophical context (e.g., why "bearing a grudge against afflictions" differs from ordinary grudges)
   - Connects the verse to the daily practice of bodhicitta
   - Uses concrete imagery and analogy (the warrior metaphor, the example of a battlefield, etc.)

If a verse is very well-known (e.g., Ch. 4:43–44, Ch. 6:10, Ch. 8:120–125), draw on the traditional commentarial literature. For lesser-known verses, generate commentary that faithfully reflects the text's meaning and philosophical spirit.

---

### Section 5 — ཉིན་རེའི་འཚོ་བའི་ནང་ཉམས་སུ་ལེན་ཚུལ། (Daily Life Application) [GENERATED]

Write exactly **3 practical application points** in Tibetan. Each should:
- Have a numbered bold label (e.g., `**༡. [Short descriptive title]**`)
- Give a concrete instruction for how to bring the verse's teaching into today's ordinary life
- Be actionable and specific — tell the practitioner *what to do* when anger arises, when distraction occurs, etc.

Ground each point in the specific verses studied today — don't give generic mindfulness advice.

---

### Section 6 — བསྔོ་བ་དང་སྨོན་ལམ། (Dedication & Aspiration) [FIXED]

Always include these two sub-sections verbatim:

```markdown
### ༦། བསྔོ་བ་དང་སྨོན་ལམ།

####  **༡. བསྔོ་བ།** (སྤྱོད་འཇུག་ལེའུ་ ༡༠ ཤླཽཀ་ ༡)

> བདག་གིས་བྱང་ཆུབ་སྤྱོད་པ་ལ། །
> 
> འཇུག་པ་རྣམ་པར་བརྩམས་པ་ཡི། །
> 
> དགེ་བ་གང་དེས་འགྲོ་བ་ཀུན། །
> 
> བྱང་ཆུབ་སྤྱོད་ལ་འཇུག་པར་ཤོག །

####  **༢. སྨོན་ལམ།** (ཀླུ་སྒྲུབ་ཀྱི་གསུང་།)

> བྱང་ཆུབ་སེམས་མཆོག་རིན་པོ་ཆེ། །
> 
> མ་སྐྱེས་པ་རྣམས་སྐྱེ་གྱུར་ཅིག །
> 
> སྐྱེས་པ་ཉམས་པ་མེད་པ་དང་། །
> 
> གོང་ནས་གོང་དུ་འཕེལ་བར་ཤོག །
```

---

### Section 7 — གནད་ཚིག་ཁག་གི་འགྲེལ་བཤད། (Key Terms Glossary) [GENERATED]

Select 3–6 key Tibetan terms that appear in today's verses. For each:
- Bold the Tibetan term
- Provide an English translation in parentheses
- Write 2–4 sentences defining how the term is used in this specific verse/chapter context (not just a dictionary definition)

Pattern:
```markdown
**[Tibetan term]** ([English gloss]) [contextual definition]
```

Choose terms where the technical or contextual meaning differs meaningfully from the ordinary-language meaning — these are the teaching moments.

---

## Step 3 — Assemble and save the file

Combine all 7 sections into a single markdown file. Use this filename format:

```
Day-[padded 3-digit day]-Ch[chapter]-v[start]-[end].md
```

Example: `Day-001-Ch4-v43-44.md`

Save to: `C:\Users\tiger\Obsidian\bodhisattvacharyavatara-rails\0-INBOX\Plans\`

After saving, present the file with a `computer://` link and a one-sentence summary of the day's verses.

---

## Tibetan numeral reference

| Arabic | Tibetan |
|--------|---------|
| 0 | ༠ |
| 1 | ༡ |
| 2 | ༢ |
| 3 | ༣ |
| 4 | ༤ |
| 5 | ༥ |
| 6 | ༦ |
| 7 | ༧ |
| 8 | ༨ |
| 9 | ༩ |

Combine digits as normal: 45 = ༤༥, 134 = ༡༣༤, 365 = ༣༦༥.

For chapter names in the header, use the traditional Tibetan word form for the ordinal (e.g., ལེའུ་བཞི་པ། for Chapter 4), not the numeral form.

---

## Chapter name reference (ordinal form for headers)

| # | Tibetan ordinal | Chapter title |
|---|-----------------|---------------|
| 1 | དང་པོ། | བྱང་ཆུབ་ཀྱི་ཕན་ཡོན། |
| 2 | གཉིས་པ། | སྡིག་པ་བཤགས་པ། |
| 3 | གསུམ་པ། | བྱང་ཆུབ་སེམས་ཀྱི་བདག་ཉིད་ལེན་པ། |
| 4 | བཞི་པ། | བྱང་ཆུབ་སེམས་ལ་མི་བརྟེན་པ། |
| 5 | ལྔ་པ། | བག་ཡོད་པ། |
| 6 | དྲུག་པ། | བཟོད་པ། |
| 7 | བདུན་པ། | བརྩོན་འགྲུས། |
| 8 | བརྒྱད་པ། | བསམ་གཏན། |
| 9 | དགུ་པ། | ཤེས་རབ། |
| 10 | བཅུ་པ། | བསྔོ་བ། |

---

## Verse schedule reference

For full day-by-day verse assignments, read `references/verse-schedule.md` (bundled with this skill).

If the user doesn't specify verses and asks only for a day number, consult that file to find the correct chapter and verse range before generating the plan.

---

## Quality checklist before saving

- [ ] All 7 sections present with correct section numbering (༡། through ༧།)
- [ ] Section 1 and Section 6 match the fixed prayer texts **exactly** — do not paraphrase or alter
- [ ] Day number, chapter, and verse numbers are in Tibetan numerals in the header
- [ ] Exactly 3 benefit points in Section 3
- [ ] Each verse has its own commentary block in Section 4
- [ ] Exactly 3 daily application points in Section 5
- [ ] Glossary has 3–6 terms with contextual definitions (not generic dictionary entries)
- [ ] File saved with correct naming convention to the Plans folder
- [ ] Horizontal rules (---) separate all major sections
