---
name: BCA-Daily-Practice-Plan-HHDL
description: Generate one or more Bodhisattvacharyavatara (སྤྱོད་འཇུག) daily practice plans for the Dalai Lama track ("HHDL"), entirely in Tibetan, in the 6-section emoji-headed format (🪷 setting intention, ☕️ intro, 📖 today's verses, 💡 extended info, 💧 aspirations, 📿 today's practice). Use whenever the user asks for a practice plan by day number with little or no elaboration — "day-1", "day 20 to day 35", "generate day 45", "make the plan for days 100-105", "HHDL plan for day X" — for this vault's Bodhisattva Challenge / Dalai Lama track. Section content is split between fixed liturgy (copied verbatim) and generated content produced by calling the gemini_generate tool, grounded strictly in the schedule, root text, and 2-RAILS/Verses commentary summaries. Always use this skill for such requests — do not improvise the structure or write the generated sections directly without it.
---

# BCA Daily Practice Plan — HHDL (Dalai Lama track)

Generates complete daily practice-plan documents for the Bodhisattva Challenge's
Dalai Lama track. Each day is a single Tibetan-only `.md` file built from six
sections — three fixed (copied verbatim), one mechanically extracted (root
verses), and two generated (via the `gemini_generate` tool, grounded in the
verse-context rails).

**Language discipline — absolute.** Every word of prose content in the output
must be Tibetan. No English, no other language, anywhere in the six sections —
not in headings, not in generated prose, not in translations or glosses. The
only non-Tibetan-script tokens permitted are `^chapter-verse` block-ID anchors
(Arabic digits — required by the vault's citation convention) and the section
emojis themselves.

**Generated vs. fixed — the core discipline of this skill.** Sections 1 and 5
are reproduced character-for-character from this file, every time, for every
day — never paraphrased, reordered, or "improved." Sections 2, 4, and 6 are
composed by calling `mcp__gemini-mcp__gemini_generate`, not written directly
by the agent — the agent's job is to assemble the grounding material and
constraints into the prompt, call the tool, and then mechanically verify the
result (syllable counts, required opening phrases, citation integrity), never
to originate the Tibetan prose itself. Section 3 is mechanically extracted,
not generated at all.

---

## Source files

| File | Purpose |
|---|---|
| `3-TRANSFORMATIONS/Plans/Dalai Lama/Tibetan-schedule-corrected.md` | The day → verse schedule. Column 1 (`Y.Day`) is the day number; column 3 (`Verses`) is the chapter.verse range for that day, e.g. `2.35-2.37`. |
| `1-SOURCES/Translations/bo-བློ་ལྡན་ཤེས་རབ།.md` | Canonical Tibetan root text. **Always read this file and extract verses directly from it** by `^chapter-verse` block ID. Never quote a verse from memory. |
| `2-RAILS/Verses/<chapter>-<verse>-summary.md` | Per-verse commentary synthesis (Verse-Context-Summary format): མཆན་འགྲེལ, དོན་འགྲེལ (per-commentary explanations), ལུང (scriptural quotations), གཙོ་གནད (main teaching points), གནད་ཚིག (key terms), བསྡུས་དོན (AI-overview synthesis). This is the **only** source for Sections 4 and 6 — never supplement with outside knowledge. |
| `mcp__gemini-mcp__gemini_generate` | The tool that must actually produce the Tibetan prose for Sections 2, 4, and 6. Takes a `prompt` string (and an optional `model`). Call it with the assembled grounding + constraints; do not skip the call and write the prose yourself. |
| `references/tibetan-numerals-and-ordinals.md` (in this skill folder) | Cardinal/ordinal number formation, chapter-name table, and the day→chapter→folder map. |
| `scripts/count_syllables.py` (in this skill folder) | Approximate Tibetan syllable counter, used to enforce the hard syllable ceilings in Sections 4 and 6. |

---

## Output location and filename

```
3-TRANSFORMATIONS/Plans/Dalai Lama/Chapter-<C> D<s>-D<e>/Day-<N>-Ch<C>-V<start>-<end>.md
```

- Resolve the `Chapter-<C> D<s>-D<e>` folder from the chapter→folder map in
  `references/tibetan-numerals-and-ordinals.md` — do not guess it from the
  chapter number alone.
- `<N>` is the plain day number, no zero-padding. `<start>`/`<end>` are the
  plain verse numbers within the chapter (not cumulative), matching the
  `Verses` column of the schedule. Example: Day 36 → `2.54-2.56` →
  `Chapter-2 D15-D40/Day-36-Ch2-V54-56.md`.
- Filenames and the folder path use plain Arabic digits — this is a filesystem
  identifier, not plan content, so it is exempt from the Tibetan-only rule.

### ⚑ Overwrite guard

Files at this path may already exist (some days were produced by earlier
generators or hand-authored). Before writing:

1. If the target file does not exist, or exists but is empty/only a stub, write freely.
2. If it exists and already contains populated content in any of Sections 2/4/6 (i.e. more than the fixed skeleton), **stop and get explicit human confirmation** before overwriting. On approval, move the existing file to a sibling `Archive/` folder (e.g. `Chapter-2 D15-D40/Archive/Day-36-Ch2-V54-56.md`, adding a numeric suffix if that name is already taken) rather than deleting it.

---

## Phase 0 — Parse the day request

The user will typically give day numbers tersely: `day-1`, `day 20 to day 35`,
`days 45, 46, 50`. Expand whatever is given into an explicit list of day
numbers before starting Phase 1. Run Phases 1–3 once per day in the list;
batch the lookups (schedule, root text, summaries) where consecutive days
share a chapter to avoid re-reading the same file repeatedly.

---

## Phase 1 — Collect information (per day)

Do all four steps, and read every file involved, before writing anything.

### Step 1 — Decide the day(s)

Already done in Phase 0. Confirm each requested day number actually has a row
in `Tibetan-schedule-corrected.md` — if not, stop and report the gap rather
than guessing a verse range.

### Step 2 — Identify the verse numbers for the day

Look up the day's row in `Tibetan-schedule-corrected.md`; read the `Verses`
column (third column). Format is `<chapter>.<start>-<chapter>.<end>` (e.g.
`2.35-2.37`) or, for single-verse days, `<chapter>.<verse>`. Extract:
chapter number, start verse, end verse (equal to start if a single verse).

### Step 3 — Find the exact verse(s) for the day

Open `1-SOURCES/Translations/bo-བློ་ལྡན་ཤེས་རབ།.md` and locate each verse in
the range by its `^chapter-verse` block ID (e.g. `^2-35`, `^2-36`, `^2-37`).
Copy the verse text **exactly as written**, including the trailing `॥ ॥`-style
line-final punctuation and the block ID. Never paraphrase, never quote from
memory or training data. If a block ID is missing from the file, stop and
report it — do not substitute or invent the verse.

### Step 4 — Find information for the verse(s)

For each verse in the range, open
`2-RAILS/Verses/<chapter>-<verse>-summary.md` (e.g. `2-RAILS/Verses/2-35-summary.md`).
Read the whole file. Collect, per verse:

- **དོན་འགྲེལ།** (per-commentary explanations) — candidate stories/similes/detailed breakdowns for Section 4.
- **ལུང།** (scriptural quotations) — candidate citations for Section 4.
- **གཙོ་གནད།** (main teaching points) — candidate clarifying explanations for Section 4, and candidate benefit/connection material for Section 6.
- **གནད་ཚིག** (key terms) — background only; rarely quoted directly.
- **བསྡུས་དོན།** (AI-overview synthesis) — a fallback overview if the other layers are thin.

If a verse's summary file does not exist, note the gap explicitly (it limits
what Section 4 can draw on for that verse) — do not invent material to fill
it.

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
verses today's practice covers, and (b) makes the reader want to engage with
them. A doorway, not a summary.

**Build the citation phrase first**, before calling the generator. Using the
ordinal tables in `references/tibetan-numerals-and-ordinals.md`, convert the
chapter number and the start/end verse numbers to their Tibetan ordinal-word
forms, then compose:

- Multi-verse day: `ལེའུ་[chapter-ordinal]འི་ཚིགས་བཅད་[start-ordinal]་ནས་[end-ordinal]་བར་ཚིགས་བཅད་[count-cardinal]་གྱི་ཐོག་ལ་ཡིན།`
  — e.g. chapter 2, verses 35–37 → `ལེའུ་གཉིས་པའི་ཚིགས་བཅད་སོ་ལྔ་པ་ནས་སོ་བདུན་པ་བར་ཚིགས་བཅད་གསུམ་གྱི་ཐོག་ལ་ཡིན།`
- Single-verse day: `ལེའུ་[chapter-ordinal]འི་ཚིགས་བཅད་[verse-ordinal]་གྱི་ཐོག་ལ་ཡིན།`

Double-check this phrase by hand — ordinal formation is irregular and easy to
get wrong by guessing (see the worked examples in the reference file).

**Call `gemini_generate`.** Assemble a prompt that includes: the confirmed
citation phrase; the exact verse text from Step 3; a one-line paraphrase-free
summary of what the verse(s) are about drawn from the བསྡུས་དོན/གཙོ་གནད layers
collected in Phase 1 (for the generator's own grounding, not for the reader);
and these constraints, stated explicitly in the prompt:

- Output must be Tibetan only — no English, no transliteration, no markdown formatting, no preamble or explanation of what was generated.
- 1–2 sentences, brief, warm, inviting — a doorway, not a synopsis.
- Must state the citation phrase (verbatim or lightly integrated grammatically).
- Must not explain or paraphrase the verse's meaning — that belongs to Section 4, not here.

Take the tool's returned text as-is aside from mechanical cleanup (stripping
any stray markdown fencing or preamble the model added). If it contains any
non-Tibetan-script prose, regenerate with a stricter prompt rather than
translating or hand-fixing it.

```markdown
# ☕️ ངོ་སྤྲོད།

[generated 1–2 sentence intro, includes the citation phrase]
```

### Section 3 — 📖 དེ་རིང་གི་རྩ་ཚིག (Today's verses) — EXTRACTED, not generated

Paste the verse(s) retrieved in Step 3 verbatim, each verse block ending with
its `^chapter-verse` anchor, in order:

```markdown
# 📖 དེ་རིང་གི་རྩ་ཚིག

[verse 1 text] ^C-V1

[verse 2 text] ^C-V2
```

No commentary, no headers per verse, no editorializing — verses only, exactly
as they appear in the source file.

### Section 4 — 💡 གོ་རྟོགས། (Extended Info) — GENERATED

**Goal:** surface the single best piece of extended material the commentary
actually contains for these verses — a story (སྒྲུང), a simile (དཔེ), a
citation (ལུང), a detailed breakdown, or a clarifying explanation — presented
accessibly. This is not a verse-by-verse commentary walkthrough, and it is not
always present.

Before calling the generator, decide from the Phase 1 material collected
(དོན་འགྲེལ, ལུང, གཙོ་གནད) whether there actually is a standout piece of extended
material for this verse range. If the commentary offers nothing beyond
ordinary verse explanation, **the section is correctly left empty** — do not
manufacture something to fill it. If several good candidates exist, pick the
one that will support Section 6's practice the best rather than combining
all of them.

**Call `gemini_generate`** with a prompt that includes: the selected
commentary excerpt(s) verbatim, cited passages only (never invent); and these
constraints, stated explicitly:

- Output must be Tibetan only, no markdown, no preamble.
- Must open with **exactly** this phrase, filling in whichever bracketed option genuinely fits (story/point/anecdote/simile/citation/valuable-teaching — do not default to the same one every time):
  `ཚིགས་བཅད་འདི་དག་དང་འབྲེལ་བའི་འགྲེལ་བཤད་ཁག་ལས་ང་ཚོར་གོ་བདེ་ཞིང་བློ་སྐྱེད་ལྡན་པའི་འགྲེལ་བཤད་/གནད་དོན་/གཏམ་རྒྱུད་/དཔེ་/ལུང་/རིན་ཐང་ཅན་འདི་འདྲ་ཞིག་གསུངས་ཡོད།`
- Hard ceiling: **300 Tibetan syllables total.** This is a ceiling, not a target — instruct the generator not to pad toward it, and prefer a shorter, well-chosen answer.
- Base only on the supplied commentary excerpts. No outside knowledge, however plausible.

After generation, run `scripts/count_syllables.py` on the output. If it
exceeds 300, either regenerate with a tighter instruction or trim — trimming
must cut only redundant material, never information the source doesn't
support keeping anyway.

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
range — the one an ordinary person with no special training could actually
act on today — and build all three subsections around that one verse only.
If the day has only one verse, that is automatically the chosen verse.

**Call `gemini_generate`** with a prompt that includes: all of today's verses
(so the generator can choose among them) and the collected commentary
material for each (from Phase 1); the practice-category tag list; and these
constraints, stated explicitly:

- Output must be Tibetan only, no markdown beyond the three required `####` subheadings, no preamble.
- Choose exactly one verse from the day's range to build the practice around; name which one internally is fine, but the visible output is just the three subsections below.
- **དང་པོ་ཉམས་ལེན་དངོས** — one concrete action that fits ordinary modern life *today* — not a retreat activity, not a vague aspiration ("contemplate compassion"), a specific doable thing ("when I feel afraid today, I will..."). **Absolute hard limit: 30 Tibetan syllables** — do not exceed this even slightly.
- **གཉིས་པ་དེའི་འགྲེལ་བཤད** — explain the practice's benefit and how it connects to the chosen verse. Must open with exactly one bracketed category tag chosen from this list (pick whichever genuinely fits — do not default to the same one every time): `[སྡིག་པ་མི་བྱ་བ།, དགེ་བ་བྱ་བ།, རང་སེམས་འདུལ་བ།, སྦྱིན་པའི་ཉམས་ལེན།, ཚུལ་ཁྲིམས་ཀྱི་ཉམས་ལེན།, བཟོད་པའི་ཉམས་ལེན།, བརྩོན་འགྲུས་ཀྱི་ཉམས་ལེན།, བསམ་གཏན་གྱི་ཉམས་ལེན།, ཤེས་རབ་ཀྱི་ཉམས་ལེན།]`
- **གསུམ་པ་ཚིགས་བཅད་དངོས** — is not generated prose at all; it is the exact root verse the practice is drawn from, unaltered, unparaphrased, no commentary added, with its `^chapter-verse` anchor intact. Insert this from Step 3's already-verified verse text — do not let the generator retype the verse (risk of drift from the source).

> ⚠️ **Mechanical fix the generator reliably needs.** The category tag must be
> wrapped exactly as `_(tag)_` — underscore-parenthesis, i.e. an italicized
> parenthetical — matching the worked example below. Models frequently
> substitute plain square brackets (`[དགེ་བ་བྱ་བ།]`) instead. Check the raw
> tool output for this every time and correct it before inserting — this is
> mechanical cleanup, not content authorship, so fixing it does not violate
> the "don't hand-author" rule.

Format:

```markdown
# 📿 དེ་རིང་གི་ཉམས་ལེན།

#### དང་པོ་ཉམས་ལེན་དངོས།:
[<=30-syllable concrete action]

#### གཉིས་པ་དེའི་འགྲེལ་བཤད།:
_([category tag])_ [explanation of benefit, tied to the chosen verse]

#### གསུམ་པ་ཚིགས་བཅད་དངོས།:
[verse text, verbatim from Step 3] ^C-V
```

Worked example (chapter 2, verse 50):

```markdown
#### དང་པོ་ཉམས་ལེན་དངོས།:
ངས་དེ་རིང་སྡུག་བསྔལ་དང་འཇིགས་སྣང་འབྱུང་སྐབས་འཕགས་པ་སྤྱན་རས་གཟིགས་ལ་སྙིང་ཐག་པ་ནས་གསོལ་བ་འདེབས་རྒྱུ་ཡིན།

#### གཉིས་པ་དེའི་འགྲེལ་བཤད།:
_(དགེ་བ་བྱ་བ།)_ འཁོར་བའི་སྡུག་བསྔལ་དང་འཇིགས་སྣང་སྣ་ཚོགས་ཀྱིས་མནར་བའི་སྐབས་སུ། རང་དོན་གྱི་འཁྲིས་མེད་པར་གཞན་དོན་ཁོ་ན་མཛད་པའི་སྤྱན་རས་གཟིགས་མགོན་ལ་སྙིང་ཁུང་རུས་པའི་གཏིང་ནས་སྐྱབས་སུ་བཙལ་ན་སེམས་ཀྱི་འཇིགས་པ་ཞི་ཞིང་སྡིག་པ་དག་པར་འགྱུར་བས་སོ། །

#### གསུམ་པ་ཚིགས་བཅད་དངོས།:
ཐུགས་རྗེས་སྤྱོད་པ་མ་འཁྲུལ་བ། །
སྤྱན་རས་གཟིགས་མགོན་དེ་ལ་ཡང་། །
ཉམ་ཐག་ང་རོས་འོ་དོད་འབོད། །
སྡིག་ལྡན་བདག་ལ་བསྐྱབ་ཏུ་གསོལ། ། ^2-50
```

After generation, run `scripts/count_syllables.py` on just the first
subsection's content — regenerate (not trim by hand) if it exceeds 30
syllables, since hand-trimming risks producing an incomplete instruction.

---

## Phase 3 — Assemble and save

1. Concatenate the six sections in order (1 → 2 → 3 → 4 → 5 → 6), separated by
   a blank line, each starting with its own `# [emoji] [name]` H1 heading
   exactly as shown above. Section 4 may be entirely absent (heading and all)
   only if genuinely no standout material was found — state this explicitly
   when reporting back, don't silently drop it without noting why.
2. Optionally prepend a document title line for navigation (not one of the six
   required sections, so it does not need to follow their heading scheme):
   `# ཉིན་ [day, Tibetan numeral] — སྤྱོད་འཇུག་ལེའུ་[chapter-ordinal]། ཚིགས་བཅད་[start]–[end]`
3. Resolve the output path (see "Output location and filename" above) and
   apply the overwrite guard.
4. Write the file.
5. Repeat for every day in the request.

---

## Phase 4 — Verification checklist

Run this for every day produced, before considering it done:

- [ ] File saved at `Chapter-<C> D<s>-D<e>/Day-<N>-Ch<C>-V<start>-<end>.md`, folder resolved from the chapter→folder map, not guessed.
- [ ] Overwrite guard honored — no populated existing file silently replaced.
- [ ] All six section headings present in order, each `# [emoji] [Tibetan name]` exactly as specified (🪷 ☕️ 📖 💡 💧 📿), except Section 4 may be legitimately absent.
- [ ] Section 1 and Section 5 are byte-identical to the fixed blocks in this file — no paraphrase, no reordering, no punctuation drift.
- [ ] Section 2 is 1–2 sentences, states the citation phrase, does not explain verse meaning, and was produced by `gemini_generate` (not authored directly).
- [ ] Section 2's citation phrase double-checked by hand against the ordinal reference table — chapter and verse ordinals correct.
- [ ] Section 3 contains only the day's verses, copied verbatim from `bo-བློ་ལྡན་ཤེས་རབ།.md` with intact `^chapter-verse` anchors, no commentary mixed in.
- [ ] Section 4, if present: opens with exactly the required fixed phrase (correct bracketed option chosen), is grounded only in this verse range's `2-RAILS/Verses/*-summary.md` content, is a single best point rather than several stitched together, and measures <=300 syllables via `scripts/count_syllables.py`.
- [ ] Section 4, if absent: the absence is because the commentary genuinely had nothing extra — noted in the report, not silently skipped.
- [ ] Section 6 is built around exactly one verse from the day's range; if the day has multiple verses, confirm the most actionable one was chosen.
- [ ] Section 6 subsection 1 (དང་པོ་ཉམས་ལེན་དངོས) measures <=30 syllables via the script — verified, not eyeballed.
- [ ] Section 6 subsection 2 (གཉིས་པ་དེའི་འགྲེལ་བཤད) opens with exactly one category tag from the fixed list, wrapped as `_(tag)_` (not `[tag]` or bare) — the tag genuinely fits and was not defaulted.
- [ ] Section 6 subsection 3 (གསུམ་པ་ཚིགས་བཅད་དངོས) is the exact verse text from Section 3/Step 3, not a re-typed or paraphrased version, with its anchor intact.
- [ ] Every word of prose content is Tibetan — no English or other language anywhere except `^chapter-verse` anchors and filenames/paths, which are exempt.
- [ ] No content in Sections 2, 4, or 6 was hand-authored by the agent bypassing `gemini_generate` — mechanical cleanup of the tool's output (stripping stray markdown/preamble) is fine; composing the prose is not.

---

## Known failure modes

- Writing Section 2/4/6 prose directly instead of calling `gemini_generate` — defeats the point of this skill's generation discipline.
- Guessing an ordinal instead of composing it from the decade-prefix table — 35th and 45th look similar but use different prefixes (སོ་ vs ཞེ་).
- Padding Section 4 to reach the 300-syllable ceiling, or padding Section 6's first subsection toward 30 — both ceilings are meant to force concision, not to be hit exactly.
- Filling Section 4 with invented or general-knowledge material when the commentary summary is thin — leave it empty instead.
- Letting the generator retype the root verse in Section 6's third subsection instead of pasting the already-verified text from Section 3 — introduces silent drift from the source.
- Choosing the same practice-category tag or the same Section-4 opening variant every day — both lists exist precisely so the choice varies with what the commentary actually supports.
- Silently overwriting an existing populated day file instead of applying the overwrite guard.
- Mixing Arabic and Tibetan numerals inside plan prose (Arabic is fine only in anchors and file paths).
