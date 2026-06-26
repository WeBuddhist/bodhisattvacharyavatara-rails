---
name: practice-verse-alignment
description: For a Bodhisattvacharyavatara day-plan file, identify which of the day's verse(s) the "Today's Practice" section is grounded in, and flag any practice that does not trace to a verse (via "From the Tradition"). Use whenever asked "which verse aligns with the practice", "what verse does today's practice come from", or to check that a day's practice is anchored to its verses before sign-off. Reads and reports only; never edits the day file.
---

# Practice ↔ Verse Alignment — The Bodhisattva Challenge

This skill answers a single, narrow question for one day file: **which verse (or verses) does the "Today's Practice" actually draw on, and does that chain hold?**

It is a focused companion to `english-plan-evaluator`. The evaluator grades the whole day; this skill traces one link — Practice → From the Tradition → verse — and names the verse. Keep the tracing rule below in sync with the generator skills (`english-plan-generator`, `english-plan-from-tibetan`), which build the practice from the one added idea in "From the Tradition", which in turn is grounded in a specific verse.

---

## When to use

- The user asks which verse a day's "Today's Practice" aligns with, comes from, or is based on.
- A reviewer wants to confirm the practice is anchored to one of the day's verses (not floating, not drawn from a verse outside the day's range).
- As a quick self-check after writing a day, before the fuller `english-plan-evaluator` pass.

Do **not** use it to rewrite the day or to grade voice/style — that is the evaluator's job.

---

## Inputs

1. **The day file** (e.g. `3-TRANSFORMATIONS/Plans/the-bodhisattva-challenge/en/Days/Chapter-1 D1-D14/1.md`). Read it in full.
2. **The day's verses**, as listed in the file's `verses:` frontmatter and reproduced in "Today's Verses". The English verse text is what the alignment is judged against; pull the canonical text from the source if the file's copy is in doubt:
   - English: `3-TRANSFORMATIONS/Translations/en-ai/en-AI-generated-root-loden-sherab.md`, or `1-SOURCES/Translations/en-David_Karma_Choephel.md` (Chapter 2+), by block ID.
   - Tibetan: `1-SOURCES/Translations/bo-བློ་ལྡན་ཤེས་རབ།.md`, by block ID.
3. **The day's "From the Tradition" section** — the hinge. The practice is built from the one added idea here, and that idea is grounded in one verse. Trace through it.

Judge alignment from the text in front of you, not from memory of the verse.

---

## How to trace (the rule)

The grounding chain the generators follow is:

```
Today's Practice  ←  the one added idea in From the Tradition  ←  a specific verse in the day's range
```

So work backwards in two steps:

1. **Read "Today's Practice".** Name the concrete action it asks for and the single idea behind it (e.g. "trust that your actions have real effects").
2. **Find that idea in "From the Tradition".** It is almost always the explicit hinge of that paragraph. Note the term or move it turns on (e.g. *faith*, *the lord of death does not wait*, *the imprint that remains*).
3. **Match the idea to a verse.** Read each verse in the day's range and find the one whose content the idea is unpacking — the verse that contains the word, image, or claim the practice leans on. That is the aligned verse.

Tie-breakers:

- If the idea sits in **one** verse's wording (e.g. "the strength of my faith" → the faith verse), that verse is the alignment, even when other verses share the day.
- If the practice genuinely draws on **two** verses (a distinction that needs both), name both and say what each contributes.
- If "From the Tradition" rests on a verse **outside** the day's stated range, flag it (see Flags) — the practice is mis-anchored.
- If the practice cannot be traced to any of the day's verses at all, flag it as **unanchored**.

The Opening and the title often lean on *different* verses than the practice; that is expected and not a problem. Only the practice is being traced here.

---

## Output format

Keep it short. Lead with the answer.

```
# Practice alignment — Day [N] ([file])

Aligned verse: [C-V]  ("[the short phrase or word the practice leans on]")

Chain:
- Practice asks: [one line — the action + the idea behind it]
- From the Tradition turns on: [the term / move]
- That idea is in verse [C-V]: "[the exact verse phrase it unpacks]"

[If relevant] Other verses today ([range]) shape the Opening/title, not the practice.

Flags: [none] | [mis-anchored: practice leans on [C-V], outside today's range] | [unanchored: no verse in [range] supports the practice]
```

Rules for the report:
- **Name the verse first.** Everything else supports that answer.
- **Quote the verse phrase** the practice leans on — do not just assert the link.
- Write in plain language; no skill jargon.
- Report only. Do not edit the day or rewrite the practice. If you find a mis-anchor or an unanchored practice, say so and stop — fixing it is a separate, generator/evaluator task.

---

## Worked example (Day 1, verses 1-1 to 1-3)

- **Practice asks:** just before a sharp word or a small lie, test whether you really trust that what you do has effects — the idea is *trust that actions have results* (the first kind of faith).
- **From the Tradition turns on:** *faith* — Sazang Mati Panchen's three kinds, the first being trust that actions have real results.
- **That idea is in verse 1-3:** "the strength of my faith to cultivate virtue will temporarily increase" (Tibetan: དགེ་བ་བསྒོམ་ཕྱིར་བདག་གི་དད་པའི་ཤུགས།).
- **Aligned verse: 1-3.** Verses 1-1 (homage) and 1-2 (wrote it only to train his own mind) shape the Opening and title, not the practice.
- **Flags:** none.

---

## Notes

- This skill reads and reports only.
- It judges alignment, not quality. For a full structure/grounding/voice review, run `english-plan-evaluator`.
- Days built from interim `en-ai` sources (or, for Chapter 2+, from a translated Tibetan plan with no English rails) still trace the same way; note in the report that grounding was checked against interim material.
