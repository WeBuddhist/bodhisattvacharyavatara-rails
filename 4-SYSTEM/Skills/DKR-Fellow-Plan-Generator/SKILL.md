---
name: dkr-fellow-plan
description: Generate a complete Day-63 practice plan for the DKR Fellow package of the Bodhisattvacharyavatara, in the 5-section format used by this program. Use when the user asks to create, generate, or fill in Day 63 of the DKR Fellow plan, or any request referencing "DKR Fellow", "DKR Fellow Day 63", or the file Day-63-Ch10-V45-58.md. Always use this skill — do not improvise the structure.
---

# DKR Fellow Practice Plan — Day 63 Generator

This skill generates the Day-63 practice plan for the 63-day DKR Fellow package of the *Bodhisattvacharyavatara* (སྤྱོད་འཇུག). The plan covers Chapter 10 (བསྔོ་བའི་ལེའུ་), Verses 45–58, using DKR's Tibetan commentary as the teaching source. Output is a single Tibetan-language markdown file.

---

## What you're building

A 5-section practice plan document that:

1. Opens with fixed refuge and bodhicitta prayers
2. Presents the root verses assigned for Day 63
3. Extracts DKR's teaching on the relevant themes from his Tibetan commentary
4. Closes with fixed dedication and aspiration prayers
5. Offers a concrete daily-life application drawn from the day's verses and DKR's teaching

---

## Source files

| File | Purpose |
|---|---|
| `C:\Users\tiger\Obsidian\bodhisattvacharyavatara-rails\1-SOURCES\Translations\bo-བློ་ལྡན་ཤེས་རབ།.md` | **Root text** — canonical Tibetan translation by Blo ldan shes rab. Read this file and extract verses ^10-45 through ^10-58 exactly. Never quote verses from memory. |
| `C:\Users\tiger\Obsidian\bodhisattvacharyavatara-rails\3-TRANSFORMATIONS\Plans\DKR-Fellow\schedule.md` | **Schedule** — confirms Day 63 = Chapter 10, Verses 45–58 (10.45–10.58). Read this to verify the assignment before extracting verses. |
| `C:\Users\tiger\Obsidian\bodhisattvacharyavatara-rails\3-TRANSFORMATIONS\Plans\DKR-Fellow\DKR-Teaching-Assignment-to-Days.md` | **DKR's teaching — pre-assigned by day.** The Day-63 section (heading `## Day-63-Ch10-V45-58`) contains DKR's teaching for this day at blocks **^9-39 through ^9-43**. Copy these blocks verbatim into Section 3 — do not generate or paraphrase. |

---

## Step 1 — Verify the assignment

1. Read `3-TRANSFORMATIONS/Plans/DKR-Fellow/schedule.md` and confirm Day 63 = 10.45–10.58.
2. Read `1-SOURCES/Translations/bo-བློ་ལྡན་ཤེས་རབ།.md` and locate verses ^10-45 through ^10-58. Extract their exact text.
3. Read `3-TRANSFORMATIONS/Plans/DKR-Fellow/DKR-Teaching-Assignment-to-Days.md`, section `## Day-63-Ch10-V45-58`, blocks ^9-39 through ^9-43. These are the pre-assigned DKR teaching paragraphs for Day 63 — copy them verbatim for Section 3.

Do not write any content until all three reads are complete.

---

## Tibetan writing style — mandatory for all generated sections

All generated prose follows these rules without exception.

### Voice and person — differs by section

- **Section 2 (root verses)**: No prose — only verse text. No explanatory writing.
- **Section 3 (DKR teaching)**: **Neutral, explanatory tone.** Write as a teacher bringing the teaching alive. Do **not** use first person (ངས་ / ང་རང་ / བདག་གིས་). You may address the reader as ཁྱེད་ to maintain warmth.
- **Section 5 (daily life application)**: **First person singular only** — ངས་, ང་རང་, བདག་གིས་. Never ང་ཚོས་ or ང་ཚོ་. This is the practitioner's own voice.

### Sentence architecture

**Each clause must do one thing.** Give it one time reference, one action, or one conclusion — then close it and open the next. Never pack two or more logical functions into a single subordinate clause.

**Clause connection ladder — use in order of closeness:**

| Particle | Use when… |
|---|---|
| ཞིང་ / ལ་ | two actions happen together or in quick succession |
| ནས་ / ཏེ | the second clause follows from or results from the first |
| དང་། | listing items of equal weight |
| ། | complete stop before a new, independent thought |
| ཡིན་ནོ།། / འགྱུར་རོ།། | close a paragraph with a sense of settled conclusion |

**Never end a paragraph mid-thought.** The final sentence should feel like an arrival, not a trailing clause.

### Nominalization trap

Keep modifier chains to **one level deep**. Rewrite deeper stacks as two clauses.

❌ Bad: ང་རང་གི་མི་རྟག་པའི་བསམ་པ་འདིས་ད་ལྟར་གྱི་གོ་སྐབས་ལ་རྩར་ཆོད་ཅིག་བྱ་རྒྱུ་ཡིན་ནོ།།
✓ Good: མི་རྟག་པར་དྲན་ཞིང་ད་ལྟར་གྱི་གོ་སྐབས་ལ་དམ་འཛིན་བྱ་རྒྱུ་ཡིན་ནོ།།

### Register and tone

- Target audience: **Tibetan-speaking practitioners familiar with the BCA** who are joining the DKR Fellow program.
- All DKR teaching content must be **extracted from BCAC21_DKR_bo.md** and rendered faithfully in clear, accessible modern Tibetan. Never invent or supplement from training data.
- Always refer to Śāntideva as རྒྱལ་སྲས་ཆེན་པོ་ཞི་བ་ལྷ།
- Always refer to DKR as རྫོང་སར་མཁྱེན་བརྩེ་རིན་པོ་ཆེ། on first mention; མཁྱེན་བརྩེ་རིན་པོ་ཆེ། thereafter.

### What to avoid

- ❌ Dzongkha grammatical patterns or vocabulary
- ❌ ངས་ / ང་རང་ / བདག་གིས་ in Section 3
- ❌ ང་ཚོས་ / ང་ཚོ་ anywhere in the document
- ❌ Stacked relative clauses: X-བའི་ Y-བའི་ Z — rewrite as two clauses
- ❌ Ending a paragraph on a subordinate particle (ཞིང་, ནས་, ལ་) — always close with a full final particle
- ❌ **བགྱི་** as a first-person verb — this is Dzongkha-style honorific, wrong for a practitioner's own voice. Use བྱ་ / བྱེད་ / བྱ་རྒྱུ་ / བྱ་བ་ཡིན་ instead.
- ❌ **གནད་དུ་ཕབ་** paired with **བསམ་གཏན་** — unnatural collocation. Use ཡིད་གཏད་དེ / སེམས་བཞག་སྟེ / དྲན་པ་གཏད་དེ.
- ❌ **ཕྱི་ལོར་ + ཐོབ་ངེས་མིན་** — fabricated compound not found in the tradition. To express "hard to obtain again later" follow the verse: ཕྱིར་ཐོབ་དཀའ་བས / ཕྱིས་འབྱོར་དཀའ་བས.

---

## Step 2 — Compose the document

Generate the complete document using the template below.

### Document header [MANDATORY — always first]

```
 
---
# ཉིན་ ༦༣ - མཁྱེན་བརྩེའི་སློབ་འབངས་སྤྱོད་འཇུག་སློབ་སྦྱོང། ཉིན་ ༦༣ །

## སྤྱོད་འཇུག་ལེའུ་བཅུ་པ། ཤློཀ་ ༤༥ - ༥༨

---
```

> ⚠️ The blank line before the first `---` is required. Without it, Obsidian parses the header as YAML frontmatter.

---

### Section 1 — སྐྱབས་འགྲོ་སེམས་བསྐྱེད། (Refuge & Bodhicitta) [FIXED]

Always include verbatim:

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

### Section 2 — དེ་རིང་གི་རྩ་ཚིག (Today's Root Verses) [GENERATED]

Open with the heading `### ༢། དེ་རིང་གི་རྩ་ཚིག`.

**No prose in this section — root verses only.**

1. Read `3-TRANSFORMATIONS/Plans/DKR-Fellow/schedule.md` to confirm Day 63 = verses 10.45–10.58.
2. Read `1-SOURCES/Translations/bo-བློ་ལྡན་ཤེས་རབ།.md` and extract verses ^10-45 through ^10-58 exactly.
3. For each verse, output:
   - **Header**: `#### **[verse number in Tibetan numerals]. ཤློཀ་[ordinal word]།** (ལེའུ་ ༡༠ ཤློཀ་ [verse number in Tibetan numerals])`
     - The ordinal word is the verse number spelled out (e.g. ༤༥ → བཞི་བཅུ་རྩ་ལྔ་པ, ༥༨ → ལྔ་བཅུ་རྩ་བརྒྱད་པ).
     - Bold contains only the numeral, ordinal word, and ། — the parenthetical reference is **outside** the bold.
   - **Verse block**: Full Tibetan verse in a blockquote, with །། line endings, copied **exactly** from the source file using the ^10-N block reference.

> ⚠️ Critical: verse text must be copied exactly from the source file. If a verse cannot be located, state this explicitly — do not substitute.

---

### Section 3 — གསུང་ཆོས། (DKR's Teaching) [VERBATIM FROM DKR-TEACHING-ASSIGNMENT-TO-DAYS]

Open with the heading `### ༣། གསུང་ཆོས།`.

Immediately after that heading, add the day's teaching title as a `####` subheading, taken verbatim from the `###` sub-heading found inside that day's section in `DKR-Teaching-Assignment-to-Days.md`. For Day 63 this is:

```
#### དངོས་པོའི་གནས་ཚུལ་རྟོགས་པའི་མཐའ་སྡོམ།
```

**Do not generate or paraphrase.** Copy the pre-assigned DKR teaching paragraphs verbatim from `3-TRANSFORMATIONS/Plans/DKR-Fellow/DKR-Teaching-Assignment-to-Days.md`.

#### Source pipeline for Section 3

Read the `## Day-63-Ch10-V45-58` section of `DKR-Teaching-Assignment-to-Days.md`. The `###` sub-heading immediately following the day header is the teaching title — include it as `####` in the plan. Then copy blocks **^9-39 through ^9-43** exactly as they appear, preserving paragraph breaks.

After the final block, add a single citation line:

```
**མཆན།**: [[3-TRANSFORMATIONS/Plans/DKR-Fellow/DKR-Teaching-Assignment-to-Days.md#^9-39|DKR-Teaching-Assignment-to-Days ^9-39–^9-43]]
```

> ⚠️ Critical: copy the blocks exactly — do not rephrase, summarise, or supplement with any other material.

---

### Section 4 — བསྔོ་བ་དང་སྨོན་ལམ། (Dedication & Aspiration) [FIXED]

Always include verbatim:

```markdown
### ༤། བསྔོ་བ་དང་སྨོན་ལམ།

#### **༡. བསྔོ་བ།**

> བདག་གིས་བྱང་ཆུབ་སྤྱོད་པ་ལ། །
> 
> འཇུག་པ་རྣམ་པར་བརྩམས་པ་ཡི། །
> 
> དགེ་བ་གང་དེས་འགྲོ་བ་ཀུན། །
> 
> བྱང་ཆུབ་སྤྱོད་ལ་འཇུག་པར་ཤོག །

#### **༢. སྨོན་ལམ།**

> བྱང་ཆུབ་སེམས་མཆོག་རིན་པོ་ཆེ། །
> 
> མ་སྐྱེས་པ་རྣམས་སྐྱེ་གྱུར་ཅིག །
> 
> སྐྱེས་པ་ཉམས་པ་མེད་པ་དང་། །
> 
> གོང་ནས་གོང་དུ་འཕེལ་བར་ཤོག །
```

---

### Section 5 — ཉམས་སུ་ལེན་ཚུལ། (Daily Life Application) [GENERATED]

Open with the heading `### ༥། ཉམས་སུ་ལེན་ཚུལ།`.

Write **exactly 1 practical application** drawn directly from the day's root text verses **and** from DKR's teaching in Section 3. The practice must be grounded in what the verses actually say and what Khyentse Rinpoche specifically teaches for this day — not generic advice.

#### Output format

Use the following trilingual structure:

```
**ལག་ལེན།**
**Tibetan:** [practice]
**English:** [practice]
**Hindi:** [practice]

**འགྲེལ་བཤད།**
**Tibetan:** (category) [explanation]
**English:** (category) [explanation]
**Hindi:** (category) [explanation]
```

#### Rules for ལག་ལེན (Practice)

Every practice must satisfy ALL THREE:

**1. Actionable today** — doable in ordinary daily life right now, not a vague aspiration or retreat activity.

| ✗ Not actionable | ✓ Actionable |
|---|---|
| "དེ་རིང་སྙིང་རྗེ་སྒོམ་ཞིང་དུས་ཚོད་ཆུད་ཟོས་སུ་མི་གཏོང་རྒྱུ་ཡིན།" | "དེ་རིང་ངས་མི་དབུལ་པོ་ཞིག་ལ་ཉིན་གུང་ཁ་ལག་ཅིག་སྤྲད་རྒྱུ་ཡིན།" |

**2. Brief** — under 20 Tibetan syllables (equivalent brevity in English ≤ 20 words, Hindi ≤ 20 words).

**3. Connected to one of nine categories** — label the *explanation* (not the practice) with the matching category in parentheses:

- སྡིག་པ་མི་བྱ་བ། — avoiding evil
- དགེ་བ་བྱ་བ། — doing good
- རང་སེམས་འདུལ་བ། — taming the mind
- སྦྱིན་པའི་ཉམས་ལེན། — generosity
- ཚུལ་ཁྲིམས་ཀྱི་ཉམས་ལེན། — ethics
- བཟོད་པའི་ཉམས་ལེན། — patience
- བརྩོན་འགྲུས་ཀྱི་ཉམས་ལེན། — diligence
- བསམ་གཏན་གྱི་ཉམས་ལེན། — meditation
- ཤེས་རབ་ཀྱི་ཉམས་ལེན། — wisdom

#### Rules for འགྲེལ་བཤད (Explanation)

- Under 40 Tibetan syllables (equivalent brevity in English and Hindi)
- Explain **how** today's specific practice enacts **this day's** verse teaching and DKR's teaching
- Reference what the verses actually say and what Khyentse Rinpoche specifically teaches — not generic spiritual statements
- Open with the relevant category in parentheses
- The explanation is a bridge: verse teaching + DKR teaching → today's action

#### Tibetan voice for this section

- **First person singular only** — ངས་, ང་རང་, བདག་གིས་. Never ང་ཚོས་ or ང་ཚོ་.
- Concrete and authentic — verse teaching cited directly, daily commitment stated plainly.
- Tibetan practice text sealed with a full final particle (ཡིན་ནོ།། or འགྱུར་རོ།།).

**Example (illustrative only — do not reuse):**

```markdown
**ལག་ལེན།**
**Tibetan:** དེ་རིང་ངས་སྡུག་བསྔལ་མྱོང་བའི་གང་ཟག་གཅིག་ལ་ཕན་པའི་ལས་གཅིག་བྱ་རྒྱུ་ཡིན།
**English:** I will do one act today that directly benefits someone who is suffering.
**Hindi:** आज मैं किसी दुखी व्यक्ति की एक मदद करूंगा।

**འགྲེལ་བཤད།**
**Tibetan:** (སྦྱིན་པའི་ཉམས་ལེན།) རྒྱལ་སྲས་ཆེན་པོ་ཞི་བ་ལྷས་གསུངས་པ་ལྟར་འགྲོ་བ་ཐམས་ཅད་བདེ་བར་གྱུར་ཅིག་ཅེས་སྨོན་ལམ་འདེབས་པ་ལས་ལྷག་སྟེ། རྫོང་སར་མཁྱེན་བརྩེ་རིན་པོ་ཆེའི་གསུང་ལྟར་བདེ་སྨོན་དེ་ལས་ཀར་བསྒྲུབ་དགོས།
**English:** (Generosity) Beyond aspirations for all beings to be happy as Śāntideva teaches, Khyentse Rinpoche emphasizes enacting those aspirations through concrete acts.
**Hindi:** (दान का अभ्यास) शांतिदेव की शिक्षा से आगे जाकर ख्येंत्से रिनपोछे सिखाते हैं कि यह कामना कर्म में परिणित होनी चाहिए।
```

---

## Step 3 — Assemble and write to the target file

Combine all sections into the complete document and write it to:

```
C:\Users\tiger\Obsidian\bodhisattvacharyavatara-rails\3-TRANSFORMATIONS\Plans\DKR-Fellow\Day-63-Ch10-V45-58.md
```

After writing, present the file and confirm it was written successfully.

---

## Tibetan numeral reference

| Arabic | Tibetan |
|---|---|
| 1 | ༡ |
| 2 | ༢ |
| 3 | ༣ |
| 4 | ༤ |
| 5 | ༥ |
| 6 | ༦ |
| 7 | ༧ |
| 8 | ༨ |
| 9 | ༩ |
| 10 | ༡༠ |
| 45 | ༤༥ |
| 58 | ༥༨ |
| 63 | ༦༣ |

Ordinal word forms for Chapter 10 verses (45–58):

| Verse | Tibetan ordinal |
|---|---|
| 45 | བཞི་བཅུ་རྩ་ལྔ་པ། |
| 46 | བཞི་བཅུ་རྩ་དྲུག་པ། |
| 47 | བཞི་བཅུ་རྩ་བདུན་པ། |
| 48 | བཞི་བཅུ་རྩ་བརྒྱད་པ། |
| 49 | བཞི་བཅུ་རྩ་དགུ་པ། |
| 50 | ལྔ་བཅུ་པ། |
| 51 | ལྔ་བཅུ་རྩ་གཅིག་པ། |
| 52 | ལྔ་བཅུ་རྩ་གཉིས་པ། |
| 53 | ལྔ་བཅུ་རྩ་གསུམ་པ། |
| 54 | ལྔ་བཅུ་རྩ་བཞི་པ། |
| 55 | ལྔ་བཅུ་རྩ་ལྔ་པ། |
| 56 | ལྔ་བཅུ་རྩ་དྲུག་པ། |
| 57 | ལྔ་བཅུ་རྩ་བདུན་པ། |
| 58 | ལྔ་བཅུ་རྩ་བརྒྱད་པ། |

---

## Quality checklist before saving

- [ ] Document header present, with day number ༦༣, chapter ལེའུ་བཅུ་པ།, and verse range ༤༥–༥༨ in Tibetan numerals — positioned **before Section 1**
- [ ] All 5 sections present with correct numbering (༡། through ༥།)
- [ ] Section 1 and Section 4 match the fixed prayer texts **exactly** — do not paraphrase or alter
- [ ] Section 2 — verses ^10-45 through ^10-58 found in source file and copied exactly; each verse has a header following `#### **N. ཤློཀ་[ordinal]།** (ལེའུ་ ༡༠ ཤློཀ་ N)` — parenthetical outside the bold
- [ ] Section 2 — no prose, no commentary — root verses only
- [ ] Section 3 — teaching title included as `####` subheading immediately after `### ༣། གསུང་ཆོས།`, taken from the `###` sub-heading in that day's DKR-Teaching-Assignment-to-Days section
- [ ] Section 3 — blocks ^9-39 through ^9-43 copied verbatim from `DKR-Teaching-Assignment-to-Days.md` (Day-63 section); ends with a **མཆན།** citation line referencing `DKR-Teaching-Assignment-to-Days ^9-39–^9-43`
- [ ] Section 3 — no generated, paraphrased, or supplemented content; text matches source exactly
- [ ] Section 5 — exactly 1 practice in trilingual format (ལག་ལེན། + འགྲེལ་བཤད།, each in Tibetan / English / Hindi)
- [ ] Section 5 — ལག་ལེན: under 20 syllables/words per language; actionable today; category label on འགྲེལ་བཤད only
- [ ] Section 5 — འགྲེལ་བཤད: under 40 syllables per language; references specific verse content **and** DKR's teaching; opens with category in parentheses
- [ ] Section 5 — Tibetan practice text: first person singular (ངས་ / ང་རང་); sealed with final particle (ཡིན་ནོ།། or འགྱུར་རོ།།)
- [ ] Section 5 — draws from both the day's root text verses **and** Khyentse Rinpoche's teaching (Section 3)
- [ ] Tibetan spelling and grammar reviewed — check case endings, verb forms, and particles
- [ ] No ང་ཚོས་ / ང་ཚོ་ anywhere in the document
- [ ] No Dzongkha-style phrasing
- [ ] Classical Tibetan literary register maintained; Śāntideva = རྒྱལ་སྲས་ཆེན་པོ་ཞི་བ་ལྷ།; DKR = རྫོང་སར་མཁྱེན་བརྩེ་རིན་པོ་ཆེ།
- [ ] Output written to `3-TRANSFORMATIONS/Plans/DKR-Fellow/Day-63-Ch10-V45-58.md`
- [ ] File presented to user after writing
