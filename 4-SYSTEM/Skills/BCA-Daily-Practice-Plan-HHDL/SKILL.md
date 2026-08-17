---
name: BCA-Daily-Practice-Plan-HHDL
description: Generate one or more Bodhisattvacharyavatara (སྤྱོད་འཇུག) daily practice plans for the Dalai Lama track ("HHDL"), entirely in Tibetan, in the 6-section emoji-headed format (🪷 setting intention, ☕️ intro, 📖 today's verses, 💡 extended info, 💧 aspirations, 📿 today's practice). Use whenever the user asks for a practice plan by day number with little or no elaboration — "day-1", "day 20 to day 35", "generate day 45", "make the plan for days 100-105", "HHDL plan for day X" — for this vault's Bodhisattva Challenge / Dalai Lama track. Section content is split between fixed liturgy (copied verbatim) and generated content produced by calling the gemini_generate tool, grounded strictly in the schedule, root text, and 2-RAILS/Verses commentary summaries. Always use this skill for such requests — do not improvise the structure or write the generated sections directly without it.
Author:
  - Tigerboy
---

# BCA Daily Practice Plan — HHDL (Dalai Lama track)

Generates complete daily practice-plan documents for the Bodhisattva Challenge's Dalai Lama track. Each day is a single Tibetan-only `.md` file built from six sections — three fixed (copied verbatim), one mechanically extracted (root verses), and two generated (via the `gemini_generate` tool, grounded in the verse-context rails).

**Language discipline — absolute.** Every word of prose content in the output must be Tibetan. No English, no other language, anywhere in the six sections — not in headings, not in generated prose, not in translations or glosses. The only non-Tibetan-script tokens permitted are `^chapter-verse` block-ID anchors (Arabic digits — required by the vault's citation convention) and the section emojis themselves.

**Generated vs. fixed — the core discipline of this skill.** Sections 1 and 5 are reproduced character-for-character from this file, every time, for every day — never paraphrased, reordered, or "improved." Sections 2, 4, and 6 are composed by calling `mcp__gemini-mcp__gemini_generate`, not written directly by the agent — the agent's job is to assemble the grounding material and constraints into the prompt, call the tool, and then mechanically verify the result (syllable counts, required opening phrases, citation integrity), never to originate the Tibetan prose itself. Section 3 is mechanically extracted, not generated at all.

**Reading level — plain, 8th-grade Tibetan, for every generated section.** Sections 2, 4, and 6 must read at an easy, 8th-grade Tibetan level that any ordinary person can follow on first reading — short clear sentences, everyday vocabulary, no archaic scholastic or classical-commentarial phrasing, no dense unglossed philosophical compounds. Bake this instruction explicitly into every `gemini_generate` prompt (see the per-section constraint lists below); do not rely on the model defaulting to it. This rule governs register only — it does not license paraphrasing, omitting, or softening the underlying content, and it never applies to Sections 1, 3, or 5, which are liturgy and root verses reproduced exactly as attested regardless of how classical their language is.

**Grammar discipline — ending particles (རྫོགས་ཚིག/མཐའ་རྟགས), absolute, for every generated sentence.** When a sentence-final verb closes with one of the ten suffix letters ག ང ད ན བ མ ར ལ ས, the matching ending particle must be used — the initial consonant of the particle must equal the suffix letter:

| Suffix | Particle | Example |
|---|---|---|
| ག | གོ | བྱེད་གོ། |
| ང | ངོ | གཏོང་ངོ་། |
| ད | དོ | བགྱིད་དོ། |
| ན | ནོ | བྱིན་ནོ། |
| བ | བོ | འགྲུབ་བོ། |
| མ | མོ | བསམ་མོ། |
| ར | རོ | བགྱིར་རོ། |
| ལ | ལོ | བསྐྱལ་ལོ། |
| ས | སོ | བགྱིས་སོ། |

A stem ending in the vowel-suffix འ takes འོ་ with contraction (e.g. དཀའོ།, མངའོ།). A stem with no suffix consonant at all takes འོ་ appended directly (e.g. སྡེའོ།, པོའོ།, མའོ།). **Whenever a sentence closes with one of these ending particles, it must be followed by a double shad (།།), never a single shad (།)** — e.g. གཏོང་ངོ་།། not གཏོང་ངོ། and never a mismatched form like གཏོང་དོ། (ང suffix wrongly paired with the དོ particle, which belongs to a ད suffix). This rule applies to Sections 2, 4, and 6 — check every generated sentence that ends in a རྫོགས་ཚིག particle against the suffix-letter table above before accepting the output; a mismatched particle or a missing second shad is a mechanical error, not a content judgment call, so correct it directly (same category as the Section-6 category-tag bracket fix) rather than leaving it or regenerating from scratch. This rule does not apply to the auxiliary/copula verbs ཡིན་, མིན་, ཡོད་, མེད་, which conventionally close a sentence bare with a single shad and take no རྫོགས་ཚིག particle. It never applies to Sections 1, 3, or 5 (fixed liturgy and root verses), which are reproduced exactly as attested regardless of their own grammar.

---

## Source files

| File | Purpose |
|---|---|
| `3-TRANSFORMATIONS/Plans/Dalai Lama/Tibetan-schedule-corrected.md` | The day → verse schedule. Column 1 (`Y.Day`) is the day number; column 3 (`Verses`) is the chapter.verse range for that day, e.g. `2.35-2.37`. |
| `1-SOURCES/Translations/bo-བློ་ལྡན་ཤེས་རབ།.md` | Canonical Tibetan root text. **Always read this file and extract verses directly from it** by `^chapter-verse` block ID. Never quote a verse from memory. |
| `2-RAILS/Verses/<chapter>-<verse>-summary.md` | Per-verse commentary synthesis (BCA-Verse-Context-Summary format): མཆན་འགྲེལ, དོན་འགྲེལ (per-commentary explanations), ལུང (scriptural quotations), གཙོ་གནད (main teaching points), གནད་ཚིག (key terms), བསྡུས་དོན (AI-overview synthesis). This is the **only** source for Sections 4 and 6 — never supplement with outside knowledge. |
| `mcp__gemini-mcp__gemini_generate` | The tool that must actually produce the Tibetan prose for Sections 2, 4, and 6. Takes a `prompt` string (and an optional `model`). Call it with the assembled grounding + constraints; do not skip the call and write the prose yourself. |
| `references/tibetan-numerals-and-ordinals.md` (in this skill folder) | Cardinal/ordinal number formation, chapter-name table, and the day→chapter→folder map. |
| `scripts/count_syllables.py` (in this skill folder) | Approximate Tibetan syllable counter, used to enforce the hard syllable ceilings in Sections 4 and 6. |

---

## Output location and filename — overwrite the existing file, never create a new one

All 365 day files already exist on disk, one per day, under
`3-TRANSFORMATIONS/Plans/Dalai Lama/Chapter-<C> D<s>-D<e>/`. This skill's job
is to **locate the correct existing file for the requested day and overwrite
it in place** — it never creates a new file and never needs to invent a
filename.

```
3-TRANSFORMATIONS/Plans/Dalai Lama/Chapter-<C> D<s>-D<e>/Day-<N>-Ch<C>-V<start>-<end>.md
```

Example: Day 41 → `Chapter-3 D41-D54/Day-41-Ch3-V1-2.md`.

### Locate the file (do this before generating anything)

1. Resolve the `Chapter-<C> D<s>-D<e>` folder from the chapter→folder map in `references/tibetan-numerals-and-ordinals.md`, using the chapter number found in Phase 1 Step 2 — do not guess it from the chapter number alone.
2. Inside that folder, find the file matching `Day-<N>-Ch*-V*.md` (`<N>` = the requested day number, no zero-padding). There is exactly one such file per day across the whole plan.
3. **Consistency check:** confirm the `Ch<C>-V<start>-<end>` portion of the filename you found matches the chapter and verse range you computed from `Tibetan-schedule-corrected.md` in Phase 1 Step 2. The filename encodes this redundantly, so a mismatch means either the schedule lookup or the file search went wrong — **stop and report it**, do not overwrite a file whose filename disagrees with the schedule.
4. If no file matching `Day-<N>-*.md` exists in the resolved folder at all, that is an error state (every day 1–365 should already have one) — stop and report it rather than creating a new file.

### Overwriting

Once the file is located and the consistency check passes, **overwrite it
directly** with the freshly assembled six-section plan (Phase 3) — no
archiving step and no confirmation prompt. These files are the generation
targets, not curated content to be preserved; that is precisely what this
skill exists to fill in. Filenames and folder paths use plain Arabic
digits — this is a filesystem identifier, not plan content, so it is exempt
from the Tibetan-only rule.

---

## Phase 0 — Parse the day request

The user will typically give day numbers tersely: `day-1`, `day 20 to day 35`, `days 45, 46, 50`. Expand whatever is given into an explicit list of day numbers before starting Phase 1. Run Phases 1–3 once per day in the list; batch the lookups (schedule, root text, summaries) where consecutive days share a chapter to avoid re-reading the same file repeatedly.

---

## Phase 1 — Collect information (per day)

Do all four steps, and read every file involved, before writing anything.

### Step 1 — Decide the day(s)

Already done in Phase 0. Confirm each requested day number actually has a row in `Tibetan-schedule-corrected.md` — if not, stop and report the gap rather than guessing a verse range.

### Step 2 — Identify the verse numbers for the day

Look up the day's row in `Tibetan-schedule-corrected.md`; read the `Verses` column (third column). Format is `<chapter>.<start>-<chapter>.<end>` (e.g. `2.35-2.37`) or, for single-verse days, `<chapter>.<verse>`. Extract: chapter number, start verse, end verse (equal to start if a single verse).

### Step 3 — Find the exact verse(s) for the day

Open `1-SOURCES/Translations/bo-བློ་ལྡན་ཤེས་རབ།.md` and locate each verse in the range by its `^chapter-verse` block ID (e.g. `^2-35`, `^2-36`, `^2-37`).
Copy the verse text **exactly as written**, including the trailing `॥ ॥`-style line-final punctuation and the block ID. Never paraphrase, never quote from memory or training data. If a block ID is missing from the file, stop and report it — do not substitute or invent the verse.

### Step 4 — Find information for the verse(s)

For each verse in the range, open `2-RAILS/Verses/<chapter>-<verse>-summary.md` (e.g. `2-RAILS/Verses/2-35-summary.md`).
Read the whole file. Collect, per verse:

- **དོན་འགྲེལ།** (per-commentary explanations) — candidate stories/similes/detailed breakdowns for Section 4.
- **ལུང།** (scriptural quotations) — candidate citations for Section 4.
- **གཙོ་གནད།** (main teaching points) — candidate clarifying explanations for Section 4, and candidate benefit/connection material for Section 6.
- **གནད་ཚིག** (key terms) — background only; rarely quoted directly.
- **བསྡུས་དོན།** (AI-overview synthesis) — a fallback overview if the other layers are thin.

If a verse's summary file does not exist, note the gap explicitly (it limits
what Section 4 can draw on for that verse) — do not invent material to fill it.

---

## Phase 2 — Generate contents

### Section 1 — 🪷 སྐྱབས་འགྲོ་སེམས་བསྐྱེད། (Setting intention) — FIXED, verbatim every time

```markdown
# 🪷 སྐྱབས་འགྲོ་སེམས་བསྐྱེད།

## ཚད་མེད་བཞི།
སེམས་ཅན་ཐམས་ཅད་བདེ་བ་དང་བདེ་བའི་རྒྱུ་དང་ལྡན་པར་གྱུར་ཅིག
སེམས་ཅན་ཐམས་ཅད་སྡུག་བསྔལ་དང་སྡུག་བསྔལ་གྱི་རྒྱུ་དང་བྲལ་བར་གྱུར་ཅིག
སེམས་ཅན་ཐམས་ཅད་སྡུག་བསྔལ་མེད་པའི་བདེ་བ་དང་མི་འབྲལ་བར་གྱུར་ཅིག
སེམས་ཅན་ཐམས་ཅད་ཉེ་རིང་ཆགས་སྡང་གཉིས་དང་བྲལ་བའི་བཏང་སྙོམ་ལ་གནས་པར་གྱུར་ཅིག

## སྐྱབས་འགྲོ།
བྱང་ཆུབ་སྙིང་པོར་མཆིས་ཀྱི་བར། །
སངས་རྒྱས་རྣམས་ལ་སྐྱབས་སུ་མཆི། །
ཆོས་དང་བྱང་ཆུབ་སེམས་དཔའ་ཡི། །
ཚོགས་ལའང་དེ་བཞིན་སྐྱབས་སུ་མཆི། །

## སེམས་བསྐྱེད།
ཇི་ལྟར་སྔོན་གྱི་བདེ་གཤེགས་ཀྱིས། །
བྱང་ཆུབ་ཐུགས་ནི་བསྐྱེད་པ་དང་། །
བྱང་ཆུབ་སེམས་དཔའི་བསླབ་པ་ལ། །
དེ་དག་རིམ་བཞིན་གནས་པ་ལྟར། །

དེ་བཞིན་འགྲོ་ལ་ཕན་དོན་དུ། །
བྱང་ཆུབ་སེམས་ནི་བསྐྱེད་བགྱི་ཞིང་། །
དེ་བཞིན་དུ་ནི་བསླབ་པ་ལའང་། །
རིམ་པ་བཞིན་དུ་བསླབ་པར་བགྱི། །
```

Copy this block character-for-character. Do not alter punctuation, line
breaks, or wording.

### Section 2 — ☕️ ངོ་སྤྲོད། (Practice Intro) — GENERATED

**Goal:** a short, warm, inviting line or two that (a) names exactly which
verses today's practice covers, and (b) makes the reader want to engage with them. A doorway, not a summary.

**Build the citation phrase first**, before calling the generator. Using the
ordinal tables in `references/tibetan-numerals-and-ordinals.md`, convert the chapter number and the start/end verse numbers to their Tibetan ordinal-word forms, then compose:

- Multi-verse day: `ལེའུ་[chapter-ordinal]འི་ཚིགས་བཅད་[start-ordinal]་ནས་[end-ordinal]་བར་ཚིགས་བཅད་[count-cardinal]་གྱི་ཐོག་ལ་ཡིན།`
  — e.g. chapter 2, verses 35–37 → `ལེའུ་གཉིས་པའི་ཚིགས་བཅད་སོ་ལྔ་པ་ནས་སོ་བདུན་པ་བར་ཚིགས་བཅད་གསུམ་གྱི་ཐོག་ལ་ཡིན།`
- Single-verse day: `ལེའུ་[chapter-ordinal]འི་ཚིགས་བཅད་[verse-ordinal]་གྱི་ཐོག་ལ་ཡིན།`

Double-check this phrase by hand — ordinal formation is irregular and easy to get wrong by guessing (see the worked examples in the reference file).

**Call `gemini_generate`.** Assemble a prompt that includes: the confirmed
citation phrase; the exact verse text from Step 3; a one-line paraphrase-free summary of what the verse(s) are about drawn from the བསྡུས་དོན/གཙོ་གནད layers collected in Phase 1 (for the generator's own grounding, not for the reader); and these constraints, stated explicitly in the prompt:

- Output must be Tibetan only — no English, no transliteration, no markdown formatting, no preamble or explanation of what was generated.
- Plain, easy 8th-grade Tibetan — short sentences, everyday vocabulary, no archaic or scholastic phrasing. A common person should understand it on first reading.
- 1–2 sentences, brief, warm, inviting — a doorway, not a synopsis.
- Must state the citation phrase (verbatim or lightly integrated grammatically).
- Must not explain or paraphrase the verse's meaning — that belongs to Section 4, not here.
- Every sentence-final verb closing with a རྫོགས་ཚིག ending particle must use the particle matching its suffix letter (see the Grammar discipline note above), closed with a double shad (།།) — not a single shad, and not a mismatched particle like གཏོང་དོ་ (should be གཏོང་ངོ་།།).
- **No generic formulaic closing.** Do not end with a hollow devotional exhortation that could be pasted onto any day — e.g. "with a joyful mind and great faith, please engage in today's practice" (`སེམས་པ་སྤྲོ་པོ་དང་དད་པ་ཆེན་པོའི་ངང་ནས་... འཇུག་པར་ཞུ།`) names no reason, no image, nothing specific to today, and fails the actual goal of this section. The line beyond the citation phrase must contain something concrete and specific to *these* verses — a vivid image, a genuine question, a felt stake — so the reader senses in one line why today's particular verses are worth pausing for. Feed the prompt a one-line description of what's actually distinctive or evocative in today's verses (not just their topic) so the generator has something specific to work from.

Take the tool's returned text as-is aside from mechanical cleanup (stripping any stray markdown fencing or preamble the model added). If it contains any non-Tibetan-script prose, regenerate with a stricter prompt rather than translating or hand-fixing it. If it lapses into a generic closing formula despite the instruction, regenerate with the failing line quoted back to the model as an explicit example of what not to repeat.

```markdown
# ☕️ ངོ་སྤྲོད།

[generated 1–2 sentence intro, includes the citation phrase]
```

### Section 3 — 📖 དེ་རིང་གི་རྩ་ཚིག (Today's verses) — EXTRACTED, not generated

Paste the verse(s) retrieved in Step 3 verbatim, each verse block ending with its `^chapter-verse` anchor, in order:

```markdown
# 📖 དེ་རིང་གི་རྩ་ཚིག

[verse 1 text] ^C-V1

[verse 2 text] ^C-V2
```

No commentary, no headers per verse, no editorializing — verses only, exactly as they appear in the source file.

### Section 4 — 💡 གོ་རྟོགས། (Extended Info) — GENERATED

**Goal:** surface the single best piece of extended material the commentary actually contains for these verses — a story (སྒྲུང), a simile (དཔེ), a citation (ལུང), a detailed breakdown, or a clarifying explanation — presented accessibly. This is not a verse-by-verse commentary walkthrough, and it is not always present.

Before calling the generator, decide from the Phase 1 material collected (དོན་འགྲེལ, ལུང, གཙོ་གནད) whether there actually is a standout piece of extended material for this verse range. If the commentary offers nothing beyond ordinary verse explanation, **the section is correctly left empty** — do not manufacture something to fill it. If several good candidates exist, pick the one that will support Section 6's practice the best rather than combining all of them.

**Call `gemini_generate`** with a prompt that includes: the selected commentary excerpt(s) verbatim, cited passages only (never invent); and these constraints, stated explicitly:

- Output must be Tibetan only, no markdown, no preamble.
- Plain, easy 8th-grade Tibetan — short sentences, everyday vocabulary, no archaic or scholastic phrasing. Render the classical commentary's point in accessible modern Tibetan; do not carry over its dense technical register.
- Must open with **exactly** this phrase, filling in whichever bracketed option genuinely fits (story/point/anecdote/simile/citation/valuable-teaching — do not default to the same one every time):
  `ཚིགས་བཅད་འདི་དག་དང་འབྲེལ་བའི་འགྲེལ་བཤད་ཁག་ལས་ང་ཚོར་གོ་བདེ་ཞིང་བློ་སྐྱེད་ལྡན་པའི་འགྲེལ་བཤད་/གནད་དོན་/གཏམ་རྒྱུད་/དཔེ་/ལུང་/རིན་ཐང་ཅན་འདི་འདྲ་ཞིག་གསུངས་ཡོད།`
- Every sentence-final verb in your own framing prose (not inside a verbatim quotation) closing with a རྫོགས་ཚིག ending particle must use the particle matching its suffix letter, closed with a double shad (།།) — see the Grammar discipline note above.
- Hard ceiling: **300 Tibetan syllables total.** This is a ceiling, not a target — instruct the generator not to pad toward it, and prefer a shorter, well-chosen answer.
- Base only on the supplied commentary excerpts. No outside knowledge, however plausible.

After generation, run `scripts/count_syllables.py` on the output. If it
exceeds 300, either regenerate with a tighter instruction or trim — trimming must cut only redundant material, never information the source doesn't support keeping anyway.

> Note: the plain-8th-grade-Tibetan rule governs the *surrounding gloss*, not
> a verbatim scriptural quotation (ལུང) itself — if the chosen material is a
> direct citation, quote it exactly as sourced even if its register is
> classical, and put the plain-language rule to work in the sentence(s) that
> introduce or explain it.

```markdown
# 💡 གོ་རྟོགས།

[generated extended-info paragraph, opening with the required phrase — or nothing at all if the commentary has no standout material]
```

### Section 5 — 💧 བསྔོ་བ་དང་སྨོན་ལམ། (Aspirations) — FIXED, verbatim every time

```markdown
# 💧 བསྔོ་བ་དང་སྨོན་ལམ།

## བསྔོ་བ།
བདག་གིས་བྱང་ཆུབ་སྤྱོད་པ་ལ། །
འཇུག་པ་རྣམ་པར་བརྩམས་པ་ཡི། །
དགེ་བ་གང་དེས་འགྲོ་བ་ཀུན། །
བྱང་ཆུབ་སྤྱོད་ལ་འཇུག་པར་ཤོག །

## སྨོན་ལམ།
བྱང་ཆུབ་སེམས་མཆོག་རིན་པོ་ཆེ། །
མ་སྐྱེས་པ་རྣམས་སྐྱེ་གྱུར་ཅིག །
སྐྱེས་པ་ཉམས་པ་མེད་པ་དང་། །
གོང་ནས་གོང་དུ་འཕེལ་བར་ཤོག །
```

Copy this block character-for-character, same as Section 1.

### Section 6 — 📿 དེ་རིང་གི་ཉམས་ལེན། (Today's Practice) — GENERATED

**Goal:** pick the single most concretely actionable verse from today's
range — the one an ordinary person with no special training could actually act on today — and build all three subsections around that one verse only. If the day has only one verse, that is automatically the chosen verse.

**Call `gemini_generate`** with a prompt that includes: all of today's verses (so the generator can choose among them) and the collected commentary material for each (from Phase 1); the practice-category tag list; and these constraints, stated explicitly:

- Output must be Tibetan only, no markdown beyond the three required `##` subheadings, no preamble.
- Plain, easy 8th-grade Tibetan in subsections 1 and 2 — short sentences, everyday vocabulary, no archaic or scholastic phrasing. This is the most concrete, action-facing section, so plainness matters most here.
- Choose exactly one verse from the day's range to build the practice around; name which one internally is fine, but the visible output is just the three subsections below.
- **ཉམས་ལེན་དངོས** — a first-person **commitment** to take one concrete action *today*, directly based on or related to the chosen verse — not a generic mindfulness statement that could apply to any day, and not a retreat activity or vague aspiration ("contemplate compassion"). Phrase it as a commitment (e.g. `ངས་དེ་རིང་... བྱ་རྒྱུ་ཡིན།` — "today I will..."), and the action itself must trace back to what the chosen verse actually says — if the connection to the verse isn't clear, the action is wrong, not just under-explained. **Absolute hard limit: 30 Tibetan syllables** — do not exceed this even slightly.
- **དེའི་འགྲེལ་བཤད** — explain the practice's benefit and how it connects to the chosen verse. Must open with exactly one bracketed category tag chosen from this list (pick whichever genuinely fits — do not default to the same one every time): `[སྡིག་པ་མི་བྱ་བ།, དགེ་བ་བྱ་བ།, རང་སེམས་འདུལ་བ།, སྦྱིན་པའི་ཉམས་ལེན།, ཚུལ་ཁྲིམས་ཀྱི་ཉམས་ལེན།, བཟོད་པའི་ཉམས་ལེན།, བརྩོན་འགྲུས་ཀྱི་ཉམས་ལེན།, བསམ་གཏན་གྱི་ཉམས་ལེན།, ཤེས་རབ་ཀྱི་ཉམས་ལེན།]`
- **ཚིགས་བཅད་དངོས** — is not generated prose at all; it is the exact root verse the practice is drawn from, unaltered, unparaphrased, no commentary added, with its `^chapter-verse` anchor intact. Insert this from Step 3's already-verified verse text — do not let the generator retype the verse (risk of drift from the source).
- Every sentence-final verb in ཉམས་ལེན་དངོས and དེའི་འགྲེལ་བཤད (never in ཚིགས་བཅད་དངོས, which is verbatim scripture) closing with a རྫོགས་ཚིག ending particle must use the particle matching its suffix letter, closed with a double shad (།།) — see the Grammar discipline note above.

> ⚠️ **Mechanical fix the generator reliably needs.** 
> The category tag must be wrapped exactly as `_(tag)_` — underscore-parenthesis, i.e. an italicized parenthetical — matching the worked example below. 
> Models frequently substitute plain square brackets (`[དགེ་བ་བྱ་བ།]`) instead. 
> Check the raw tool output for this every time and correct it before inserting — this is mechanical cleanup, not content authorship, so fixing it does not violate the "don't hand-author" rule.

> ⚠️ **Another mechanical fix the generator reliably needs: ending-particle mismatches.** 
> Models frequently attach the wrong རྫོགས་ཚིག particle to a verb — e.g. writing `གཏོང་དོ།` when the verb suffix ང requires `ངོ`, giving `གཏོང་ངོ་།།` — or forget the required double shad after the particle. 
> Check every sentence-final verb in ཉམས་ལེན་དངོས and དེའི་འགྲེལ་བཤད against the suffix table in the Grammar discipline note and correct it before inserting; this is mechanical cleanup, not content authorship.

Format:

```markdown
# 📿 དེ་རིང་གི་ཉམས་ལེན།

## ཉམས་ལེན་དངོས།:
[<=30-syllable first-person commitment, action drawn directly from the chosen verse]

## དེའི་འགྲེལ་བཤད།:
_([category tag])_ [explanation of benefit, tied to the chosen verse]

## ཚིགས་བཅད་དངོས།:
[verse text, verbatim from Step 3] ^C-V
```

Worked example (chapter 2, verse 50):

```markdown
## ཉམས་ལེན་དངོས།:
ངས་དེ་རིང་སྡུག་བསྔལ་དང་འཇིགས་སྣང་འབྱུང་སྐབས་འཕགས་པ་སྤྱན་རས་གཟིགས་ལ་སྙིང་ཐག་པ་ནས་གསོལ་བ་འདེབས་རྒྱུ་ཡིན།

## དེའི་འགྲེལ་བཤད།:
_(དགེ་བ་བྱ་བ།)_ འཁོར་བའི་སྡུག་བསྔལ་དང་འཇིགས་སྣང་སྣ་ཚོགས་ཀྱིས་མནར་བའི་སྐབས་སུ། རང་དོན་གྱི་འཁྲིས་མེད་པར་གཞན་དོན་ཁོ་ན་མཛད་པའི་སྤྱན་རས་གཟིགས་མགོན་ལ་སྙིང་ཁུང་རུས་པའི་གཏིང་ནས་སྐྱབས་སུ་བཙལ་ན་སེམས་ཀྱི་འཇིགས་པ་ཞི་ཞིང་སྡིག་པ་དག་པར་འགྱུར་བས་སོ། །

## ཚིགས་བཅད་དངོས།:
ཐུགས་རྗེས་སྤྱོད་པ་མ་འཁྲུལ་བ། །
སྤྱན་རས་གཟིགས་མགོན་དེ་ལ་ཡང་། །
ཉམ་ཐག་ང་རོས་འོ་དོད་འབོད། །
སྡིག་ལྡན་བདག་ལ་བསྐྱབ་ཏུ་གསོལ། ། ^2-50
```

Note the example's action ("today I will pray sincerely to Avalokiteśvara when fear and suffering arise") is a direct enactment of the chosen verse's own content — the request "སྐྱབས་ཏུ་གསོལ" ("I pray you protect me") — not a loosely related generic practice. Every generated ཉམས་ལེན་དངོས must have this same tightness of fit.

After generation, run `scripts/count_syllables.py` on just the ཉམས་ལེན་དངོས
subsection's content — regenerate (not trim by hand) if it exceeds 30
syllables, since hand-trimming risks producing an incomplete instruction.

---

## Phase 3 — Assemble and save

1. Concatenate the six sections in order (1 → 2 → 3 → 4 → 5 → 6), separated by a blank line, each starting with its own `# [emoji] [name]` H1 heading exactly as shown above. Section 4 may be entirely absent (heading and all) only if genuinely no standout material was found — state this explicitly when reporting back, don't silently drop it without noting why.
2. Optionally prepend a document title line for navigation (not one of the six required sections, so it does not need to follow their heading scheme):
   `# ཉིན་ [day, Tibetan numeral] — སྤྱོད་འཇུག་ལེའུ་[chapter-ordinal]། ཚིགས་བཅད་[start]–[end]`
3. Locate the existing day file and run the consistency check (see "Output location and filename" above).
4. Overwrite that file with the assembled content.
5. Repeat for every day in the request.

---

## Phase 4 — Verification checklist

Run this for every day produced, before considering it done:

- [ ] The existing file at `Chapter-<C> D<s>-D<e>/Day-<N>-Ch<C>-V<start>-<end>.md` was located and overwritten — no new file created.
- [ ] Consistency check passed: the `Ch<C>-V<start>-<end>` in the filename matches the chapter/verse range computed from `Tibetan-schedule-corrected.md`.
- [ ] All six section headings present in order, each `# [emoji] [Tibetan name]` exactly as specified (🪷 ☕️ 📖 💡 💧 📿), except Section 4 may be legitimately absent.
- [ ] Section 1 and Section 5 are byte-identical to the fixed blocks in this file — no paraphrase, no reordering, no punctuation drift.
- [ ] Section 2 is 1–2 sentences, states the citation phrase, does not explain verse meaning, and was produced by `gemini_generate` (not authored directly).
- [ ] Section 2's non-citation sentence is specific to today's actual verses (a concrete image, question, or stake) — not a generic devotional closing that could be pasted onto any day.
- [ ] Section 2's citation phrase double-checked by hand against the ordinal reference table — chapter and verse ordinals correct.
- [ ] Section 3 contains only the day's verses, copied verbatim from `bo-བློ་ལྡན་ཤེས་རབ།.md` with intact `^chapter-verse` anchors, no commentary mixed in.
- [ ] Section 4, if present: opens with exactly the required fixed phrase (correct bracketed option chosen), is grounded only in this verse range's `2-RAILS/Verses/*-summary.md` content, is a single best point rather than several stitched together, and measures <=300 syllables via `scripts/count_syllables.py`.
- [ ] Section 4, if absent: the absence is because the commentary genuinely had nothing extra — noted in the report, not silently skipped.
- [ ] Section 6 is built around exactly one verse from the day's range; if the day has multiple verses, confirm the most actionable one was chosen.
- [ ] Section 6's three subheadings are `## ཉམས་ལེན་དངོས།`, `## དེའི་འགྲེལ་བཤད།`, `## ཚིགས་བཅད་དངོས།` — two hashtags, exact wording, no ordinal prefixes (དང་པོ/གཉིས་པ/གསུམ་པ).
- [ ] Section 6 subsection ཉམས་ལེན་དངོས is phrased as a first-person commitment ("today I will...") and the action traces directly back to the chosen verse's own content, not a generic practice loosely inspired by it; measures <=30 syllables via the script — verified, not eyeballed.
- [ ] Section 6 subsection དེའི་འགྲེལ་བཤད opens with exactly one category tag from the fixed list, wrapped as `_(tag)_` (not `[tag]` or bare) — the tag genuinely fits and was not defaulted.
- [ ] Section 6 subsection ཚིགས་བཅད་དངོས is the exact verse text from Section 3/Step 3, not a re-typed or paraphrased version, with its anchor intact.
- [ ] Every word of prose content is Tibetan — no English or other language anywhere except `^chapter-verse` anchors and filenames/paths, which are exempt.
- [ ] Sections 2, 4, and 6 read at a plain, easy 8th-grade Tibetan level — short sentences, everyday vocabulary, no archaic/scholastic phrasing carried over from the classical commentary (verbatim scriptural quotations in Section 4 are exempt from simplification; their surrounding gloss is not).
- [ ] No content in Sections 2, 4, or 6 was hand-authored by the agent bypassing `gemini_generate` — mechanical cleanup of the tool's output (stripping stray markdown/preamble) is fine; composing the prose is not.
- [ ] Every sentence-final verb in Sections 2, 4 (framing prose only, not quotations), and 6 (ཉམས་ལེན་དངོས/དེའི་འགྲེལ་བཤད only, not ཚིགས་བཅད་དངོས) that closes with a རྫོགས་ཚིག ending particle uses the particle matching its suffix letter — checked against the Grammar discipline table, not eyeballed — and is followed by a double shad (།།), never a single shad.

---

## Known failure modes

- Writing Section 2/4/6 prose directly instead of calling `gemini_generate` — defeats the point of this skill's generation discipline.
- Section 2 closing on a generic devotional formula ("with joyful mind and great faith, please practice") instead of something specific to that day's verses — reads as filler and defeats the "make the reader want to engage with these particular verses" goal.
- Guessing an ordinal instead of composing it from the decade-prefix table — 35th and 45th look similar but use different prefixes (སོ་ vs ཞེ་).
- Padding Section 4 to reach the 300-syllable ceiling, or padding Section 6's ཉམས་ལེན་དངོས subsection toward 30 — both ceilings are meant to force concision, not to be hit exactly.
- Writing Section 6's ཉམས་ལེན་དངོས as a generic, verse-agnostic practice ("be kind today", "notice your breath") instead of a commitment that traces directly back to what the chosen verse itself says.
- Filling Section 4 with invented or general-knowledge material when the commentary summary is thin — leave it empty instead.
- Letting the generator retype the root verse in Section 6's third subsection instead of pasting the already-verified text from Section 3 — introduces silent drift from the source.
- Choosing the same practice-category tag or the same Section-4 opening variant every day — both lists exist precisely so the choice varies with what the commentary actually supports.
- Creating a new file instead of finding and overwriting the day's existing file — all 365 already exist; this skill never invents a filename.
- Overwriting a file without running the filename-vs-schedule consistency check first, risking a mismatch between the file's own `Ch<C>-V<start>-<end>` and the actual computed verse range.
- Mixing Arabic and Tibetan numerals inside plan prose (Arabic is fine only in anchors and file paths).
- Letting generated prose drift into classical/scholastic register because the source commentary excerpts fed into the prompt were themselves dense and technical — the plain-8th-grade-Tibetan instruction must be stated explicitly in every generation prompt, not assumed.
- Attaching a mismatched ending particle (རྫོགས་ཚིག) to a sentence-final verb — e.g. `གཏོང་དོ།` for a verb ending in ང (should be `གཏོང་ངོ་།།`) — or dropping the required second shad after the particle. Check every generated sentence's ending against the suffix-letter table in the Grammar discipline note; this is a mechanical error the generator makes reliably and must be caught before saving.
