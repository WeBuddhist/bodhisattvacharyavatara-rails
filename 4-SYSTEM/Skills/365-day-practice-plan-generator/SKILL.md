---
name: bca-practice-plan
description: Generate a complete single-day Bodhisattvacharyavatara (སྤྱོད་འཇུག) practice plan session document in the traditional 7-section format, in Tibetan. Use this skill whenever the user asks to create, generate, or produce a daily practice plan, practice session, or ཉམས་ལེན་ document for the Bodhisattvacharyavatara (also written Bodhicaryavatara, Spyod 'jug, BCA, or Guide to the Bodhisattva's Way of Life). Trigger on phrases like "create a practice plan for day X", "generate today's BCA session", "make a Spyod 'jug practice plan", "365-day plan", "ཉམས་ལེན་", "སྤྱོད་འཇུག་སློབ་སྦྱོང", "generate a practice document", or any request for a structured daily Bodhisattvacharyavatara study/practice session. Always use this skill even when the user just says something like "make me today's Spyod 'jug" or "can you do day 45 of the practice plan" — don't try to improvise a structure without this skill.
---

# 365-Day Bodhisattvacharyavatara Practice Plan Generator

This skill generates a single day's structured practice plan document for a 365-day practice of Śāntideva's *Bodhisattvacharyavatara* (སྤྱོད་འཇུག). Each day produces a complete 7-section markdown file in Tibetan, following the traditional format used by Tigerboy (tigerboy@webuddhist.com).

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

## Source files

| File | Purpose |
|------|---------|
| `C:\Users\tiger\Obsidian\bodhisattvacharyavatara-rails\0-INBOX\bo-root versions\bo-བློ་ལྡན་ཤེས་རབ།-དངུལ་ཆུ་ཐོགས་མེད་སྤྱོད་འཇུག་རྩ་བ།.md` | **Root text** — canonical Tibetan translation by Blo ldan shes rab. **Always read this file and extract verses directly from it.** Never quote root-text verses from memory or training data. Verses are identified by block references in the format `^chapter-verse` (e.g. `^4-43` for Chapter 4, verse 43). |
| `C:\Users\tiger\Obsidian\bodhisattvacharyavatara-rails\1-SOURCES\Commentaries\bo-དངུལ་ཆུ་ཐོགས་མེད།.md` | **Commentary** — Ngulchu Thokme's *Ocean of Good Explanations* in Tibetan. **Always read this file and extract commentary from it.** Never invent or improvise commentary. |

---

## Step 1 — Gather inputs

Ask the user (or infer from context) for:

1. **Day number** (1–365) — required
2. **Chapter** (ལེའུ་) and **verse range** (ཤླཽཀ་) — if not provided, look up from the schedule in `references/verse-schedule.md`
3. **Save location** — default to the user's Obsidian folder: `C:\Users\tiger\Obsidian\bodhisattvacharyavatara-rails\0-INBOX\Plans\`
4. **Language for commentary** — default is Tibetan (བོད་སྐད།); English commentary notes can be added if the user asks

If the user only gives a day number, consult the verse schedule to find the chapter and verses for that day.

Once you have the chapter and verse range, **read both source files** (root text and commentary) before writing any content. Extract the exact verse text and the relevant commentary passages before composing the document.

---

## Tibetan writing style — mandatory for all generated sections

All generated prose must follow these style rules without exception:

**Voice and person — differs by section**
- **Sections 2, 3.2, and 6** (Benefits, Commentary, Glossary): Use a **neutral, explanatory tone**. Write as a teacher explaining the teaching to a practitioner. You may address the reader as ཁྱེད་ (you) to maintain warmth, but never use ངས་ / ང་རང་ / བདག་གིས་ in these sections. The focus is the teaching itself, not the practitioner's personal voice.
- **Section 4 only** (Daily Life Application): Use the **first person singular** — ངས་, ང་རང་, བདག་གིས་. Never ང་ཚོས་ or ང་ཚོ་. This section voices the practitioner's own personal commitment to applying today's teaching.

**Sentence flow**
- Sentences must be **connected and flowing**, linked by conjunctive particles: དང་། བཅས་། ཏེ། ནས། ཞིང་། etc.
- Avoid short staccato clauses separated by།། — each paragraph should read like a single continuous thought, the way a lama would speak.
- End substantive paragraphs and closing sentences with full final particles: ཡིན་ནོ།། or འགྱུར་རོ།། or ལགས་སོ།།

**Register and tone**
- The target audience is **general Tibetan-speaking practitioners who are beginners** to the *Bodhisattvacharyavatara* — not scholars or academics. Write accordingly.
- All commentary content must be **extracted from the source commentary file** (`bo-དངུལ་ཆུ་ཐོགས་མེད།.md`) and the meaning preserved faithfully — but the **style and tone must be adapted** into clear, easy-to-read modern Tibetan that any practitioner can understand without difficulty. Think of it as rendering a traditional commentary into accessible language, the way a kind teacher would explain it to a new student.
- Avoid archaic or highly technical scholastic phrasing. Prefer shorter, clearer sentences over dense classical constructions — but do not sacrifice correct Tibetan grammar.
- When referring to Śāntideva, always use the honorific form: རྒྱལ་སྲས་ཆེན་པོ་ཞི་བ་ལྷ། — never just ཞི་བའི་ལྷ or the author's name alone.
- Address the practitioner directly in places (using ཁྱེད་ or the implied second person) to keep the personal practice feeling alive.

**What to avoid**
- ❌ Dzongkha grammatical patterns or vocabulary
- ❌ Cold, encyclopaedic or overly academic prose — even neutral-tone sections (2, 3.2, 6) should feel warm and accessible, like a kind teacher speaking to a student
- ❌ First person singular (ངས་ / ང་རང་ / བདག་གིས་) in Sections 2, 3.2, and 6
- ❌ ང་ཚོས་ / ང་ཚོ་ (collective "we") anywhere in the document
- ❌ Clipped clauses that don't flow into one another

**Model example** (Section 4 tone — personal application, first person singular):
> ཐོག་མར་ངས་དཀོན་མཆོག་གསུམ་ལ་གུས་པ་དང་སེམས་ཅན་ཐམས་ཅད་ལ་དམིགས་པའི་བྱང་ཆུབ་ཀྱི་སེམས་སྐྱེ་བའི་སྨོན་ལམ་འདེབས། དེ་རིང་ངས་སྤྱོད་འཇུག་གི་ལེའུ་དང་པོའི་ཤློཀ་དང་པོ་དང། གཉིས་པ། གསུམ་པ་བཅས་སློབ་སྦྱོང་དང་ཉམས་སུ་ལེན་རྒྱུ་ཡིན། རྒྱལ་སྲས་ཆེན་པོ་ཞི་བ་ལྷས་བྱང་ཆུབ་ཀྱི་སེམས་སྒོམ་པའི་ཕྱིར་གཞུང་འདི་བརྩམས་པར་གསུངས་པས། ང་རང་ཉིད་ཀྱིས་ཀྱང་རང་རྒྱུད་ཀྱི་ང་རྒྱལ་འཇོམས་པ་དང་གཞན་ཕན་གྱི་བསམ་པས་ཀུན་ནས་བསླངས་ཏེ་དེ་རིང་གི་སྤྱོད་འཇུག་སློབ་སྦྱོང་དང་ཉམས་ལེན་གྱི་ལས་ལ་འཇུག་པར་བྱ་རྒྱུ་ཡིན་ནོ།།

---

## Step 2 — Compose the 7-section document

Generate the complete document in Tibetan using the template below. The fixed sections are provided word-for-word; the variable sections must be generated freshly based on the specific chapter and verses.

### Document header [MANDATORY — always first]

The document header is **required in every output** and must appear **before Section 1**. Do not skip it, reorder it, or merge it into any other section.

```

---
# ཉིན་ [DAY_NUMBER_TIBETAN] - ཉིན་ ༣༦༥ ཡི་སྤྱོད་འཇུག་སློབ་སྦྱོང།

## སྤྱོད་འཇུག་ལེའུ་[CHAPTER_ORDINAL]། ཤླཽཀ་ [VERSE_START_TIBETAN] - [VERSE_END_TIBETAN]

---
```

> ⚠️ The blank line before the first `---` is required. Without it, Obsidian parses the header as YAML frontmatter and hides the title from view.

Convert day numbers, chapter numbers, and verse numbers to Tibetan numerals (see numeral table below).

---

### Section 1 — སྐྱབས་འགྲོ་སེམས་བསྐྱེད། (Refuge & Bodhicitta) [FIXED]

Always include these two sub-sections verbatim:

```markdown
### ༡། སྐྱབས་འགྲོ་སེམས་བསྐྱེད།

#### **༡. སྐྱབས་འགྲོ།**

> བྱང་ཆུབ་སྙིང་པོར་མཆིས་ཀྱི་བར། །
> 
> སངས་རྒྱས་རྣམས་ལ་སྐྱབས་སུ་མཆི། །
> 
> ཆོས་དང་བྱང་ཆུབ་སེམས་དཔའ་ཡི། །
> 
> ཚོགས་ལའང་དེ་བཞིན་སྐྱབས་སུ་མཆི། །

#### **༢. སེམས་བསྐྱེད།**

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

### Section 2 — ཕན་ཡོན། (Benefits of Today's Verses) [GENERATED]

> **Tone: neutral and explanatory.** Write as a teacher presenting the benefits to the practitioner. Do not use first person (ངས་ / ང་རང་). You may address the reader as ཁྱེད་ to maintain warmth.

Write exactly **3 benefit bullet points** in Tibetan. Each point should:
- Have a bold **title** (4–7 Tibetan words) that names the specific benefit
- Follow with 2–3 sentences of clear, accessible explanation
- Be tied specifically to the themes of today's verses (not generic bodhisattva benefits)

Pattern to follow:
```markdown
*   **[Benefit title in Tibetan]** [2–3 sentences of explanation]
```

The three benefits should form a natural progression: from psychological/emotional freedom → clarifying one's focus/target → developing resilience/courage. Adapt this arc to the specific chapter content.

---

### Section 3 — དེ་རིང་གི་རྩ་ཚིག (Today's Root Verses with Commentary) [GENERATED]

This section is divided into two distinct subsections: all root verses first, then all commentaries. Do not interleave them.

#### Subsection 3.1 — རྩ་ཚིག (Root Verses)

List every verse assigned to today in sequence. For each verse:

1. **Header**: `#### **[Tibetan numeral]. ཤླཽཀ་[ordinal]།** (ལེའུ་ [chapter ordinal] ཤླཽཀ་ [verse number])`
2. **Verse block**: The full Tibetan verse in a blockquote, with `། །` line endings — copied **exactly** from `bo-བློ་ལྡན་ཤེས་རབ།.md` using the `^chapter-verse` block references (e.g. `^1-1`, `^4-43`). **Do not quote verses from memory or training data.**

No commentary, explanation, or editorial text belongs in this subsection — verses only.

#### Subsection 3.2 — འགྲེལ་བཤད། (Commentary)

> **Tone: neutral and explanatory.** Write as a teacher clarifying the meaning for the practitioner. Do not use first person (ངས་ / ང་རང་). You may address the reader as ཁྱེད་ to maintain warmth.

For each verse, provide one commentary block in the same order as the verses above:

1. **Header**: `#### **[Tibetan numeral]. ཤླཽཀ་[ordinal]།་འགྲེལ་བཤད།**`
2. **Commentary label**: `*   **འགྲེལ་བཤད།**`
3. **Commentary text**: 4–8 sentences of Tibetan prose **extracted and summarised from `bo-དངུལ་ཆུ་ཐོགས་མེད།.md`**. Locate the relevant passage for the verse in that file, then rewrite it in clear, easy-to-read modern Tibetan that a beginner practitioner can understand and apply directly. **Do not invent, improvise, or add material not found in that commentary file.**

> ⚠️ **Critical rule for Section 3**: Both verse text and commentary must come from the source files. If you cannot locate a verse or its commentary in the files, state this explicitly — do not substitute your own words.

---

### Section 4 — ཉམས་སུ་ལེན་ཚུལ། (Daily Life Application) [GENERATED]

> **Tone: personal, first person singular.** This section is the practitioner's own voice — a personal commitment to apply today's teaching. Use ངས་, ང་རང་, བདག་གིས་. Never ང་ཚོས་ or ང་ཚོ་.

Write exactly **3 practical application points** in Tibetan. Each should:
- Have a numbered bold label (e.g., `**༡. [Short descriptive title]**`)
- Be written in first person — the practitioner speaking about what *they* will do
- Give a concrete, actionable instruction for bringing the verse's teaching into today's ordinary life
- Be specific to the verses studied today — not generic mindfulness advice

---

### Section 5 — བསྔོ་བ་དང་སྨོན་ལམ། (Dedication & Aspiration) [FIXED]

Always include these two sub-sections verbatim:

```markdown
### ༥། བསྔོ་བ་དང་སྨོན་ལམ།

####  **༡. བསྔོ་བ།**

> བདག་གིས་བྱང་ཆུབ་སྤྱོད་པ་ལ། །
> 
> འཇུག་པ་རྣམ་པར་བརྩམས་པ་ཡི། །
> 
> དགེ་བ་གང་དེས་འགྲོ་བ་ཀུན། །
> 
> བྱང་ཆུབ་སྤྱོད་ལ་འཇུག་པར་ཤོག །

####  **༢. སྨོན་ལམ།**

> བྱང་ཆུབ་སེམས་མཆོག་རིན་པོ་ཆེ། །
> 
> མ་སྐྱེས་པ་རྣམས་སྐྱེ་གྱུར་ཅིག །
> 
> སྐྱེས་པ་ཉམས་པ་མེད་པ་དང་། །
> 
> གོང་ནས་གོང་དུ་འཕེལ་བར་ཤོག །
```

---

### Section 6 — གནད་ཚིག་ཁག་གི་འགྲེལ་བཤད། (Key Terms Glossary) [GENERATED]

> **Tone: neutral and explanatory.** Write clear, accessible definitions as a teacher would. Do not use first person (ངས་ / ང་རང་). You may address the reader as ཁྱེད་ where natural.

Select 3–6 key Tibetan terms that appear in today's verses. For each:
- Bold the Tibetan term
- Provide an English translation in parentheses
- Write 2–4 sentences in clear, easy-to-read modern Tibetan defining how the term is used in this specific verse/chapter context (not just a dictionary definition)

Pattern:
```markdown
**[Tibetan term]** ([English gloss]) [contextual definition]
```

Choose terms where the technical or contextual meaning differs meaningfully from the ordinary-language meaning — these are the teaching moments.

---

## Step 3 — Assemble and save the file

Combine all 7 sections into a single markdown file. Use this filename format:

```
Day-[day]-Ch[chapter]-V[start]-[end].md
```

- Day number: no zero-padding (1, not 001)
- Verse letter: uppercase **V**

Example: `Day-1-Ch4-V43-44.md`

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

- [ ] Document header present, with correct day number, chapter ordinal, and verse range in Tibetan numerals — positioned **before Section 1**
- [ ] All 6 sections present with correct section numbering (༡། through ༦།)
- [ ] Section 1 and Section 6 match the fixed prayer texts **exactly** — do not paraphrase or alter
- [ ] Day number, chapter, and verse numbers are in Tibetan numerals in the header
- [ ] Exactly 3 benefit points in Section 2
- [ ] Section 3.1 — all verses copied directly from `bo-བློ་ལྡན་ཤེས་རབ།.md` — not quoted from memory
- [ ] Section 3.2 — all commentary blocks extracted and summarised from `bo-དངུལ་ཆུ་ཐོགས་མེད།.md` — not invented
- [ ] Exactly 3 daily application points in Section 4
- [ ] Glossary has 3–6 terms with contextual definitions (not generic dictionary entries)
- [ ] Tibetan spelling and grammar reviewed — check case endings (e.g. ལ་དོན། སུ་དོན། གི་དོན།), verb forms, and particles for correctness throughout all generated sections
- [ ] Section 4 uses first person singular (ངས་ / ང་རང་) — never collective ང་ཚོས་
- [ ] Sections 2, 3.2, and 6 use neutral tone — no first person (ངས་ / ང་རང་ / བདག་གིས་) in these sections
- [ ] Sentences flow smoothly with connective particles — no clipped Dzongkha-style clauses
- [ ] Classical Tibetan literary register maintained; Śāntideva referred to as རྒྱལ་སྲས་ཆེན་པོ་ཞི་བ་ལྷ།
- [ ] Filename follows the format `Day-[day]-Ch[chapter]-V[start]-[end].md` — no zero-padding, uppercase V
- [ ] Horizontal rules (---) separate all major sections
