---
name: bca-practice-plan
description: Generate a complete single-day Bodhisattvacharyavatara (སྤྱོད་འཇུག) practice plan session document in the traditional 6-section format, in Tibetan. Use this skill whenever the user asks to create, generate, or produce a daily practice plan, practice session, or ཉམས་ལེན་ document for the Bodhisattvacharyavatara (also written Bodhicaryavatara, Spyod 'jug, BCA, or Guide to the Bodhisattva's Way of Life). Trigger on phrases like "create a practice plan for day X", "generate today's BCA session", "make a Spyod 'jug practice plan", "365-day plan", "ཉམས་ལེན་", "སྤྱོད་འཇུག་སློབ་སྦྱོང", "generate a practice document", or any request for a structured daily Bodhisattvacharyavatara study/practice session. Always use this skill even when the user just says something like "make me today's Spyod 'jug" or "can you do day 45 of the practice plan" — don't try to improvise a structure without this skill.
---

# 365-Day Bodhisattvacharyavatara Practice Plan Generator

This skill generates a single day's structured practice plan document for a 365-day practice of Śāntideva's *Bodhisattvacharyavatara* (སྤྱོད་འཇུག). Each day produces a complete 6-section markdown file in Tibetan, following the traditional format used by Tigerboy (tigerboy@webuddhist.com).

---

## What you're building

Each practice plan is a self-contained daily session that:
- Opens with fixed refuge and bodhicitta prayers
- Sets a contextual motivation for the day's topic
- Explores the specific BCA verses assigned to that day
- Provides commentary and practical application
- Closes with fixed dedication and aspiration prayers

The output is always saved as a Tibetan-language markdown file.

---

## [Source files](C:\Users\tiger\Obsidian\bodhisattvacharyavatara-rails\4-SYSTEM\Skills\365-day-practice-plan-generator\SKILL.md)

| File                                                                                                                                     | Purpose                                                                                                                                                                                                                                                                                                        |
| ---------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `C:\Users\tiger\Obsidian\bodhisattvacharyavatara-rails\1-SOURCES\Translations\bo-བློ་ལྡན་ཤེས་རབ།.md` | **Root text** — canonical Tibetan translation by Blo ldan shes rab. **Always read this file and extract verses directly from it.** Never quote root-text verses from memory or training data. Verses are identified by block references in the format `^chapter-verse` (e.g. `^4-43` for Chapter 4, verse 43). |
| `C:\Users\tiger\Obsidian\bodhisattvacharyavatara-rails\1-SOURCES\Commentaries\` (all `.md` files in this folder) | **Commentaries** — all available Tibetan and Chinese commentaries on the *Bodhisattvacharyavatara*. **Always read the relevant files and extract commentary from them.** Never invent or improvise commentary. Read as many commentaries as are relevant to the verse being covered. |

---

## Step 1 — Gather inputs

Ask the user (or infer from context) for:

1. **Day number** (1–365) — required
2. **Chapter** (ལེའུ་) and **verse range** (ཤློཀ་) — if not provided, read `C:\Users\tiger\Obsidian\bodhisattvacharyavatara-rails\3-TRANSFORMATIONS\Plans\the-bodhisattva-challenge\bo\schedule-corrected.md` and look up the day's assigned verse(s) there
3. **Language for commentary** — default is Tibetan (བོད་སྐད།); English commentary notes can be added if the user asks

If the user only gives a day number, read `3-TRANSFORMATIONS/Plans/the-bodhisattva-challenge/bo/schedule-corrected.md` to find the chapter and verse(s) assigned for that day.

Once you have the chapter and verse range, **read the root text and all relevant commentary files** before writing any content. Extract the exact verse text from `bo-བློ་ལྡན་ཤེས་རབ།.md` and the relevant commentary passages from all files in `1-SOURCES/Commentaries/` before composing the document.

---

## Tibetan writing style — mandatory for all generated sections

All generated prose must follow these style rules without exception.

---

### Voice and person — differs by section

- **Section 2** (Introduction): **Neutral, warm tone.** Write as a kind teacher opening the day. Address the reader as ཁྱེད་ to maintain closeness, but never use ངས་ / ང་རང་ / བདག་གིས་ here. Introduce the teaching; do not explain the verse.
- **Section 4** (Explanations): **Neutral, explanatory tone.** Write as a teacher bringing the teaching alive. Address the reader as ཁྱེད་. Never use ངས་ / ང་རང་ / བདག་གིས་ in this section.
- **Section 5** (Daily Life Application): **First person singular only** — ངས་, ང་རང་, བདག་གིས་. Never ང་ཚོས་ or ང་ཚོ་. This is the practitioner's own voice committing to today's practice.

---

### Sentence architecture — the single most important rule

**Each clause must do one thing.** Give it one time reference, one action, or one conclusion — then close it and open the next. Never pack two or more logical functions into a single subordinate clause.

**The test:** read each clause aloud. If a native speaker has to pause to re-parse the structure, the clause is too complex. Break it in two.

**Clause connection ladder — use in order of closeness:**

| Particle | Use when… |
|---|---|
| ཞིང་ / ལ་ | two actions happen together or in quick succession |
| ནས་ / ཏེ | the second clause follows from or results from the first |
| དང་། | listing items of equal weight |
| ། | complete stop before a new, independent thought |
| ཡིན་ནོ།། / འགྱུར་རོ།། | close a paragraph with a sense of settled conclusion |

**Never end a paragraph mid-thought.** The final sentence should feel like an arrival, not a trailing clause.

---

### Nominalization trap — avoid collapsing actions into abstract nouns

Tibetan makes it easy to stack genitive modifiers (X-བའི་ Y-བའི་ Z). This produces text that is grammatically valid but impossible to read naturally. Keep modifier chains to **one level deep**. If you need two levels, rewrite as two clauses.

❌ **Bad** — stacked nominalizations:
> ང་རང་གི་མི་རྟག་པའི་བསམ་པ་འདིས་ད་ལྟར་གྱི་གོ་སྐབས་ལ་རྩར་ཆོད་ཅིག་བྱ་རྒྱུ་ཡིན་ནོ།།

✓ **Good** — the action expressed as a verb, the connection made with ལས་ or ཞིང་:
> མི་རྟག་པར་དྲན་ཞིང་ད་ལྟར་གྱི་གོ་སྐབས་ལ་རྩར་ཆོད་ཅིག་བྱ་རྒྱུ་ཡིན་ནོ།།

❌ **Bad** — a temporal clause buried inside a relative clause:
> ཅིག་ཤེས་བཞིན་དུ་དེ་ལ་དུས་ཚོད་འཐོར་བར་འཇུག་བཞིན་ཡོད་པའི་སྐབས་དེར།

✓ **Good** — the time reference stated simply:
> དོན་མེད་པར་དུས་འདའ་རྒྱུར་གྱུར་བའི་སྐབས།

---

### Sentence rhythm

- **Open sentences name the situation clearly** — who, when, or what — before the verb.
- **Middle clauses carry the action** — connected by ཞིང་ or ཏེ.
- **Closing sentences land with a concrete commitment or conclusion** — sealed by ཡིན་ནོ།། or འགྱུར་རོ།།
- Vary sentence length. Two medium sentences followed by one short, decisive sentence reads better than three medium sentences in a row.
- Never open two consecutive sentences with the same grammatical construction.

---

### Register and tone

- The target audience is **general Tibetan-speaking practitioners who are beginners** to the *Bodhisattvacharyavatara* — not scholars or academics.
- Commentary must be **extracted from the source file** and its meaning preserved faithfully — but rendered into clear, warm, modern Tibetan that any practitioner can follow without difficulty. Think of a kind teacher explaining a classical text to a new student.
- Avoid archaic scholastic phrasing. Prefer concrete verbs over abstract constructions. Do not sacrifice correct Tibetan grammar.
- Always refer to Śāntideva as རྒྱལ་སྲས་ཆེན་པོ་ཞི་བ་ལྷ། — never the name alone or shortened forms.
- Address the practitioner directly (ཁྱེད་) wherever it keeps the personal practice feeling alive — but not so often it becomes a formula.

---

### What to avoid

- ❌ Dzongkha grammatical patterns or vocabulary
- ❌ Cold, encyclopaedic prose — every section should feel like a warm human voice, even the explanatory ones
- ❌ ངས་ / ང་རང་ / བདག་གིས་ in Sections 2 and 4
- ❌ ང་ཚོས་ / ང་ཚོ་ anywhere in the document
- ❌ Stacked relative clauses: X-བའི་ Y-བའི་ Z — rewrite as two clauses
- ❌ Long participial strings used as temporal clauses — name the time simply, then start the main clause
- ❌ Ending a paragraph on a subordinate particle (ཞིང་, ནས་, ལ་) — always close with a full final particle

---

### Vocabulary precision — common errors to avoid

| Wrong | Correct | Note |
|---|---|---|
| གཡོག་མི་བྱ་བར་ | གཡོ་མི་བྱ་བར་ | གཡོག་ = to serve (as a servant); གཡོ་ = deception/pretext/excuse |
| བློ་ལངས་ | བློ་སྐྱེས་ | བློ་ལངས་ is unusual; བློ་སྐྱེ་ is the correct verb for "a thought arises" |

---

### Model examples

**Section 2 — neutral introduction, warm, ≤ 60 words:**
> རྒྱལ་སྲས་ཆེན་པོ་ཞི་བ་ལྷའི་ལེའུ་བཞི་པའི་ཤློཀ་བཅུ་བཞི་ནས་བཅུ་དྲུག་བར་གྱི་ཤློཀ་གསུམ་དེ་རིང་ཉམས་སུ་ལེན་རྒྱུ་ཡིན་ཏེ། ད་ལྟར་ཁྱེད་ལ་ཡོད་པའི་མི་ལུས་ཀྱི་གོ་སྐབས་འདི་ཐོབ་ཤིན་ཏུ་དཀའ་ལ་ཐོབ་ཀྱང་མི་རྟག་པར་གསུངས་པས། ཁྱེད་ད་རེས་མི་ལུས་ཀྱི་གཏིང་རིན་ཐང་ལ་ཡིད་ཀྱིས་གཏད་ལ་འདི་དང་ཕྲད་ཅིག།

**Section 4 — explanation, neutral teacher voice:**
> ཤློཀ་འདིར་"དེང་ནས་"ཞེས་གསུངས་པ་ནི་དགེ་བའི་བློ་སྐྱེས་པའི་དུས་ད་ལྟ་འདི་ཉིད་ནས་ཞེས་པའི་དོན་ཡིན་ཏེ། ཐར་པ་གཞན་གྱིས་བསྟེར་ཐབས་མེད་ལ་རང་ཉིད་ཀྱིས་བརྩོན་མི་བྱས་ན་ལྟར་སྔར་མི་ཐར་བར་གསུངས་སོ།། སྔོན་ཆད་སངས་རྒྱས་དཔག་མེད་འདས་ཟིན་ཀྱང་བདག་མ་བཏུལ་བ་འདི་ཡིན་ཏེ། ད་དུང་རང་གིས་རང་སྣོད་མ་ཡིན་པར་བྱས་ན་ངན་འགྲོར་ལྟུང་གི་སངས་རྒྱས་དང་ཕྲད་པར་མི་འགྱུར་བར་གསུངས་སོ།།

**Section 5 — today's challenge, first person singular:**
> **ལག་གཉིས་ཐལ་མོ་སྦྱར་ནས་སྐྱབས་ཡུལ་རྣམས་ལ་གུས་ཕྱག་འཚལ།**
**འགྲེལ་བཤད།** ཞོགས་པ་མལ་ནས་ལངས་མ་ཐག་སངས་རྒྱས་དང་བྱང་ཆུབ་སེམས་དཔའ་རྣམས་མདུན་དུ་བསྒོམས་ནས་གུས་པས་ཕྱག་འཚལ་དགོས། དེ་ནས་དེ་རིང་ཉིན་གང་བོར་རང་གི་བྱ་སྤྱོད་ཐམས་ཅད་གཞན་ལ་ཕན་པའི་ལས་འབའ་ཞིག་སྒྲུབ་པའི་དམ་བཅའ་བརྟན་པོ་ཞིག་འཇོག་པར་བྱའོ། །

---

## Step 2 — Compose the practice session document

Generate the complete document in Tibetan using the template below. The fixed sections are provided word-for-word; the variable sections must be generated freshly based on the specific chapter and verses.

### Document header [MANDATORY — always first]

The document header is **required in every output** and must appear **before Section 1**. Do not skip it, reorder it, or merge it into any other section.

```

---
# ཉིན་ [DAY_NUMBER_TIBETAN] - ཉིན་ ༣༦༥ ཡི་སྤྱོད་འཇུག་སློབ་སྦྱོང།

## སྤྱོད་འཇུག་ལེའུ་[CHAPTER_ORDINAL]། ཤློཀ་ [VERSE_START_TIBETAN] - [VERSE_END_TIBETAN]

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

### Section 2 — ངོ་སྤྲོད། (Introduction) [GENERATED]

> **Tone: first person and very engaging.** Write in the practitioner's own voice — ངས་, ང་རང་, བདག་གིས་. This is not a teacher introducing the day; it is the practitioner themselves opening their practice, speaking directly about the verse and why it matters right now.

Write exactly **2–4 sentences, ≤ 60 words** in Tibetan. This is not an explanation of the verse(s) — it is an introduction of the day with the verse(s). It should:
- Speak in first person: the practitioner introduces the day and its verse(s) in their own voice
- Be very engaging — draw a direct, living connection between the verse and the practitioner's own life
- Invite a felt sense of why this teaching matters today, so they are motivated to sit with it

---

### Section 3 — དེ་རིང་གི་རྩ་ཚིག (Today's Root Verses) [GENERATED]

Open the section with the literal heading `### ༣། དེ་རིང་གི་རྩ་ཚིག`. Include only root verses here — no commentary. Commentary appears in Section 4.

> ⚠️ Do **not** output subsection headings. The per-verse headers described below are the only headings inside this section.

Read `C:\Users\tiger\Obsidian\bodhisattvacharyavatara-rails\3-TRANSFORMATIONS\Plans\the-bodhisattva-challenge\bo\schedule-corrected.md` to confirm the verse(s) assigned for the day. Then look up the exact text of each verse in `C:\Users\tiger\Obsidian\bodhisattvacharyavatara-rails\1-SOURCES\Translations\bo-བློ་ལྡན་ཤེས་རབ།.md` using the `^chapter-verse` block reference. List them in sequence:

1. **Header**: `#### **[verse number in Tibetan numerals]. ཤློཀ་[ordinal word]།** (ལེའུ་ [chapter in Tibetan numerals] ཤློཀ་ [verse number in Tibetan numerals])`
   - Bold contains only the numeral, the ordinal-word verse name, and the ། — the parenthetical reference stays **outside** the bold.
   - The ordinal word is the verse number spelled out (e.g. ༡༢ → བཅུ་གཉིས་པ, ༢༠ → ཉི་ཤུ་པ, ༣༠ → སུམ་ཅུ་པ).
   - The verse number is the verse's **real number within the chapter** and must match the day's assigned verse range (the filename `V[start]-[end]`). Never use a document-local or cumulative count.
   - Example: `#### **༡༢. ཤློཀ་བཅུ་གཉིས་པ།** (ལེའུ་ ༡ ཤློཀ་ ༡༢)`
1. **Verse block**: The full Tibetan verse in a blockquote, with `། །` line endings — copied **exactly** from `bo-བློ་ལྡན་ཤེས་རབ།-དངུལ་ཆུ་ཐོགས་མེད་སྤྱོད་འཇུག་རྩ་བ།.md` using the `^chapter-verse` block reference for that verse. **Use the exact text from the file. Never quote verses from memory or training data.**

No commentary, explanation, or editorial text belongs in this section — verses only.

> ⚠️ **Critical rule for Section 3**: Verse text must be copied exactly from `bo-བློ་ལྡན་ཤེས་རབ།.md` using the `^chapter-verse` block reference. If you cannot locate a verse in the file, state this explicitly — do not substitute your own words.

---

### Section 4 — འགྲེལ་བཤད། (Explanations) [GENERATED]

Open the section with the literal heading `### ༤། འགྲེལ་བཤད།`.

> **Tone: neutral and engaging.** Write as a teacher bringing the teaching alive for the practitioner. Do not use first person (ངས་ / ང་རང་). You may address the reader as ཁྱེད་ to maintain warmth.

#### How to find the commentary — the pipeline

The commentary files in `C:\Users\tiger\Obsidian\bodhisattvacharyavatara-rails\1-SOURCES\Commentaries\` have root verses transcluded directly into them. To find what each commentary says about a verse:

1. Open each commentary file.
2. Locate the transclusion of the day's verse (e.g. `![[1-SOURCES/Text/...#^chapter-verse]]`).
3. **All text from that transclusion up to the next root verse transclusion is the commentary on that verse.** This block is your source material.

Read every commentary file and collect this pipeline material for each assigned verse before writing anything.

#### What to include

For each verse, write an explanation block under the verse header:

`#### **[verse number in Tibetan numerals]. ཤློཀ་[ordinal word]།** འགྲེལ་བཤད།`

Based on what the pipeline material actually contains, include one or more of the following content types. Do not force all three — use only those for which genuine material exists.

---

**Type 1 — ཁ་སྐོང་། (Extra information)**

Use when the verse mentions or elaborates on an important topic or term (e.g. དལ་འབྱོར་, བྱང་ཆུབ་སེམས་, etc.) and the commentaries contain rich material on it. Expand on the topic using that material — write in engaging, accessible Tibetan that deepens the practitioner's understanding.

```markdown
**ཁ་སྐོང་།** [Topic]: [Engaging expansion drawn from the commentary — 3–6 sentences.]

**མཆན།**: [[1-SOURCES/Commentaries/filename#^blockid|Display name ^blockid]]
```

---

**Type 2 — གཏམ་རྒྱུད། (Story)**

Use when you find an interesting story in the pipeline material related to the verse. Adapt it: render the classical language into clear modern Tibetan, and shape it into a short, inspiring narrative that helps practitioners understand and stay engaged with the BCA.

```markdown
**གཏམ་རྒྱུད།**: [Story in clear modern Tibetan — short and inspiring, ≤ 8 sentences.]

**མཆན།**: [[1-SOURCES/Commentaries/filename#^blockid|Display name ^blockid]]
```

---

**Type 3 — གནད་ཚིག (Keyword)**

Use when the verse contains an important or difficult term that a beginner practitioner might not understand. Explain it in plain Tibetan, briefly and clearly.

```markdown
**གནད་ཚིག** [Term]: [Plain-language explanation — 2–3 sentences.]

**མཆན།**: [[1-SOURCES/Commentaries/filename#^blockid|Display name ^blockid]]
```

---

#### Rules

- **Authenticity is absolute.** Every piece of content — extra information, story, keyword definition — must come directly from the pipeline material found in the commentary files. Never invent, assume, or add from general knowledge or training data.
- **Be selective.** For a given verse you might include only a ཁ་སྐོང་། and a གནད་ཚིག — or only a གཏམ་རྒྱུད། — or all three. Follow the commentary material, not a formula.
- Each content block must end with a `**མཆན།**` line citing the specific block ID(s) used, formatted as clickable Obsidian wikilinks: `[[1-SOURCES/Commentaries/filename#^blockid|Display name ^blockid]]`.

> ⚠️ **Critical rule for Section 4**: All content must be extracted from `1-SOURCES/Commentaries/` via the pipeline. If you cannot locate commentary for a verse in the files, state this explicitly — do not invent or improvise.

---

### Section 5 — ཉམས་སུ་ལེན་ཚུལ། (Today's Challenge) [GENERATED]

> **Tone: personal, first person singular.** This section is the practitioner's own voice — a personal commitment to apply today's teaching. Use ངས་, ང་རང་, བདག་གིས་. Never ང་ཚོས་ or ང་ཚོ་.

Write exactly **1 today's challenge** in Tibetan. It should:
- Have a bold label (e.g., `**༡. [Short descriptive title]**`)
- Be written in first person — the practitioner speaking about what *they* will do
- Be **very simple and actionable** — something any ordinary person can actually do today in their daily life, not advanced practice
- Be concrete and specific — not generic mindfulness advice
- Speak to common human situations: family, work, irritation, kindness, honesty, patience, generosity
- **If the day has more than one verse**, choose the single verse whose theme translates most naturally into a practical everyday challenge, and paste that verse (in Tibetan, as a blockquote) immediately after the bold label and before the challenge text

Real example (Day 15 — Chapter 2, Verses 1–3):
```markdown
**༡. རང་བྱུང་གི་མཛེས་པ་མཆོད་པར་འབུལ།**

> [Tibetan verse blockquote here — the chosen verse only]

དེ་རིང་ངས་ལམ་བགྲོད་པའི་སྐབས་སམ་ཕྱི་རོལ་ཏུ་འགྲོ་བའི་ཚེ། མེ་ཏོག་སྙིང་རྗེ་མོ་དང་། ཆུ་མིག་དྭངས་མ། རི་བོ་དང་ནགས་ཚལ་ཉམས་དགའ་བ་སོགས་བདག་པོས་མ་བཟུང་བའི་རང་བྱུང་གི་མཛེས་པ་གང་མཐོང་བ་དེ་དག་ཐམས་ཅད་སེམས་ཀྱི་ངང་ནས་དཀོན་མཆོག་ལ་མཆོད་པར་འབུལ་རྒྱུ་ཡིན། ངས་དེ་ལྟར་གོམས་པར་བྱས་ཏེ་རང་གི་སེམས་རྒྱུད་དགེ་བའི་ཕྱོགས་ལ་སྤྲོ་བ་བསྐྱེད་ཅིང་། རྒྱལ་སྲས་ཆེན་པོ་ཞི་བ་ལྷའི་ལེགས་བཤད་བཞིན་དུ་འཛིན་ཆགས་མེད་པའི་བློ་རྒྱུན་སྐྱོང་བར་བྱའོ། །
```

---

### Section 6 — བསྔོ་བ་དང་སྨོན་ལམ། (Dedication & Aspiration) [FIXED]

Always include these two sub-sections verbatim:

```markdown
### ༦། བསྔོ་བ་དང་སྨོན་ལམ།

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

### Section 7 — Image Generation Prompt [GENERATED]

This section produces a single English-language prompt for an external AI image generator. **Do not generate an image** — write only the prompt. The prompt will be used by Tigerboy to produce a classical Indian painting that illustrates the day's practice, and the day's verse and challenge will be overlaid as text before sharing on social media.

#### What to draw from

Before writing the prompt, synthesise the following from what was already generated:

- **The verse(s)** (Section 3) — the core theme, imagery, and metaphors Śāntideva uses
- **The explanations** (Section 4) — any vivid scenes, stories, or key concepts that emerged
- **The daily challenge** (Section 5) — the concrete human situation the practitioner is asked to work with

The prompt must tell a single coherent visual story that connects verse, explanation, and challenge — not three separate scenes.

#### Style parameters — always include

- Classical Indian Buddhist manuscript painting (Pāla dynasty style)
- Rich jewel tones: deep lapis lazuli blue, vermillion, gold leaf accents, forest green
- Flat perspective, elegant line work, decorative borders typical of illuminated manuscripts
- Figures in traditional Indian iconographic postures; landscape stylised and ornamental
- Warm devotional atmosphere — serene, luminous, inspiring

#### Composition guidance

The verse text and challenge text will be overlaid on the finished image for social media sharing. Design the prompt so:

- The **main narrative scene occupies the centre** of the image
- Decorative borders or sky/landscape at the **top and bottom** give natural space for text overlays
- The scene is **not overcrowded** — one or two clear focal figures or moments, not a busy panorama
- Target aspect ratio: **4:5 portrait** (ideal for Instagram)

#### How to write the prompt

1. Open with a concise scene description — who or what is depicted, what is happening, what emotion it conveys
2. Add the setting and natural elements drawn from the verse's own imagery (e.g. a wish-fulfilling tree, a lotus lake, a solitary figure on a mountain path)
3. Specify the painting style and technical parameters
4. Close with mood and lighting: "warm golden light", "serene and devotional", "glowing from within"

Write the prompt as a single flowing paragraph of 80–140 words. Do not use bullet points inside the prompt itself. Do not include instructions or meta-commentary in the prompt — only the image description.

#### Format in the document

Output the prompt under this heading:

```markdown
### ༧། Image Generation Prompt

[Prompt text here — English, single paragraph, 80–140 words.]
```

#### Example prompt (illustrative only — do not reuse)

```
A solitary bodhisattva sits beneath a vast wish-fulfilling tree whose golden branches stretch across a lapis-blue sky, its roots glowing beneath the earth. Before him, a wandering figure pauses on a dusty path, hands folded, eyes lifted in sudden recognition. The scene is rendered in Pāla dynasty manuscript painting style: rich jewel tones of vermillion, forest green, and deep blue with gold leaf accents, elegant flat perspective, fine calligraphic linework, and ornamental floral borders framing the composition top and bottom. The mood is serene and luminous — warm golden afternoon light, a sense of boundless quiet, the first moment of turning toward virtue. 4:5 portrait orientation.
```

---


## Step 3 — Assemble and write to the correct file

Combine all sections into the complete document. Then:

1. **Construct the target filename** from the day's inputs:
   ```
   Day-[day]-Ch[chapter]-V[start]-[end].md
   ```
   - Day number: no zero-padding (1, not 001)
   - Verse letter: uppercase **V**
   - Example: `Day-1-Ch4-V43-44.md`

2. **Find the matching file** inside `C:\Users\tiger\Obsidian\bodhisattvacharyavatara-rails\3-TRANSFORMATIONS\Plans\the-bodhisattva-challenge\bo\`. The 365 target files are distributed across chapter subfolders (e.g. `Chapter-1 D1-D14\`, `Chapter-4 D34-D55\`). Search all subfolders for the filename constructed in step 1 — the name will match exactly.

3. **Write the generated content into that file** — replacing whatever placeholder content is there.

After writing, present the file and confirm which file was written to with its subfolder path.

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

For full day-by-day verse assignments, read `C:\Users\tiger\Obsidian\bodhisattvacharyavatara-rails\3-TRANSFORMATIONS\Plans\the-bodhisattva-challenge\bo\schedule-corrected.md`.

If the user doesn't specify verses and asks only for a day number, read that file first to find the correct chapter and verse range before generating the plan.

---

## Quality checklist before saving

- [ ] Document header present, with correct day number, chapter ordinal, and verse range in Tibetan numerals — positioned **before Section 1**
- [ ] All 7 sections present with correct section numbering (༡། through ༧།)
- [ ] Section 1 and Section 6 match the fixed prayer texts **exactly** — do not paraphrase or alter
- [ ] Day number, chapter, and verse numbers are in Tibetan numerals in the header
- [ ] Section 2 introduction is 2–4 sentences, ≤ 60 words — introduces the day with the verse(s), not an explanation of the verse
- [ ] Section 3 — no subsection headings in the output
- [ ] Section 3 — verse headers follow `#### **N. ཤློཀ་[ordinal]།** (ལེའུ་ C ཤློཀ་ N)` — parenthetical **outside** the bold
- [ ] Section 4 — explanation headers follow `#### **N. ཤློཀ་[ordinal]།** འགྲེལ་བཤད།` — འགྲེལ་བཤད། **outside** the bold; verse numbers match those in Section 3
- [ ] Section 3 — verse numbers in all headers are the real chapter verse numbers and match the day's assigned range (filename `V[start]-[end]`)
- [ ] Section 3 — verses found in `1-SOURCES/Translations/bo-བློ་ལྡན་ཤེས་རབ།.md` and copied exactly — not quoted from memory or training data
- [ ] Section 4 — each explanation block contains one or more of: **ཁ་སྐོང་།** (extra information), **གཏམ་རྒྱུད།** (story), **གནད་ཚིག** (keyword); only types for which genuine pipeline material exists are included — never all three by default
- [ ] Section 4 — all content sourced from `1-SOURCES/Commentaries/` via the pipeline (commentary text between the verse transclusion and the next verse transclusion); each block ends with a **མཆན།** citation line
- [ ] Exactly 1 today's challenge in Section 5 — very simple and actionable for ordinary people in daily life
- [ ] If the day has multiple verses, Section 5 uses the single best verse for the challenge, with that verse quoted as a blockquote between the bold label and the challenge text
- [ ] Tibetan spelling and grammar reviewed — check case endings (e.g. ལ་དོན། སུ་དོན། གི་དོན།), verb forms, and particles for correctness throughout all generated sections
- [ ] Section 5 uses first person singular (ངས་ / ང་རང་) — never collective ང་ཚོས་
- [ ] Section 2 uses first person singular (ངས་ / ང་རང་) — practitioner's own voice opening the day
- [ ] Section 4 uses neutral tone — no first person (ངས་ / ང་རང་ / བདག་གིས་) in Section 4
- [ ] Sentences flow smoothly with connective particles — no clipped Dzongkha-style clauses
- [ ] Classical Tibetan literary register maintained; Śāntideva referred to as རྒྱལ་སྲས་ཆེན་པོ་ཞི་བ་ལྷ།
- [ ] Section 7 — image generation prompt is English, single paragraph, 80–140 words; based on the day's verse(s), explanations, and challenge; specifies Pāla dynasty style, jewel tones, 4:5 portrait; no meta-commentary inside the prompt
- [ ] Filename follows the format `Day-[day]-Ch[chapter]-V[start]-[end].md` — no zero-padding, uppercase V
- [ ] Horizontal rules (---) separate all major sections
