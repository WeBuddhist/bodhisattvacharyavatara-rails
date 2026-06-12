---
name: english-plan-evaluator
description: Evaluate, review, or QA a single-day Bodhisattvacharyavatara practice plan session document against the english-plan-generator rules. Use whenever asked to check, grade, review, QA, or score a day file in 3-TRANSFORMATIONS/Plans/the-bodhisattva-challenge/en/Days/ — or to confirm a day is ready to mark complete. Produces a scorecard with pass/fail per criterion, the offending text quoted, and a suggested fix.
---

# English Practice Plan Evaluator — The Bodhisattva Challenge

This skill grades one already-written day file for the Bodhisattva Challenge English stream. It does not rewrite the day; it reports what passes, what fails, and exactly where, so a reviewer can decide and a domain specialist can sign off.

It is the QA companion to `english-plan-generator`. Every criterion below mirrors a rule in that skill. When the generator skill changes, update this one to match.

---

## When to use

- The user asks to check, review, evaluate, grade, QA, or score a day file.
- A day is being considered for promotion from `status: draft` to `status: complete`.
- After generating a day, as a self-check before saving.

---

## Inputs

1. **The day file** to evaluate (e.g. `3-TRANSFORMATIONS/Plans/the-bodhisattva-challenge/en/Days/14.md`).
2. **The source rails** the day was built from, for the grounding checks:
   - `3-TRANSFORMATIONS/Translations/en-ai/Verses/<verse-id>.md` (interim) or `2-RAILS/Verses/<verse-id>.md` (preferred).
   - `3-TRANSFORMATIONS/Plans/the-bodhisattva-challenge/en/assets/liturgy.md` (fixed liturgy).
   - `1-SOURCES/Translations/bo-བློ་ལྡན་ཤེས་རབ།.md` and `3-TRANSFORMATIONS/Translations/en-ai/en-AI-generated-root-loden-sherab.md` (verse text).
   - `3-TRANSFORMATIONS/Plans/the-bodhisattva-challenge/en/assets/schedule.md` (expected chapter and verse range).

Read the day file and every relevant source before scoring. Do not score grounding from memory.

---

## How to evaluate

Work through the four groups below. For each check, assign one of: **PASS**, **FAIL**, or **N/A**. Give every FAIL a severity and the evidence.

**Severities**
- **Critical** — breaks trust or fidelity: a claim not traceable to the rails; verse or liturgy text altered; content not from the sources. A day with any critical issue cannot be marked complete.
- **Major** — a clear rule violation that a reader would notice: wrong section, an explanation instead of an added idea, forceful practice, em-dashes, paraphrased term, missing "to whom".
- **Minor** — polish: slightly long, a mild filler word, light formatting overuse.

For every FAIL, quote the exact offending text and give a one-line suggested fix.

---

## Group 1 — Structure and fidelity (mostly critical)

- **Sections present and ordered**: Opening, Renewing the Bodhisattva Vow, Today's Verses, From the Tradition, Aspiration and Dedication, Today's Practice. Headings at `##`, none deeper.
- **Practice heading** is "Today's Practice", not "Today's Practice Challenge".
- **Liturgy verbatim**: sections 2.2 and 2.5 match `liturgy.md` exactly — no added, dropped, or reworded lines.
- **Verse text from source**: Tibetan matches `bo-བློ་ལྡན་ཤེས་རབ།.md`; English matches `en-AI-generated-root-loden-sherab.md`. No paraphrase or substitution. (A chapter colophon with no source English may be rendered plainly if clearly marked as the chapter's closing line.)
- **Verse range matches the schedule** for that day number.
- **Frontmatter present**: `day`, `chapter`, `verses`, `status`, and `generation_note` if interim sources were used.

## Group 2 — Grounding (critical)

- **Every claim in From the Tradition traces to a specific rail passage.** Locate it. If a claim (a story, a number, an attribution) cannot be found in the cited rail or its sources, it is critical. (Example check: a story like King Maitribala must appear in the commentary source, not just sound plausible.)
- **Every instruction in Today's Practice traces to the idea in From the Tradition**, which traces to the rails.
- **Commentator named** when a specific attribution is made (Gyaltsab Darma Rinchen, Sazang Mati Panchen, or Ngulchu Thokme Zangpo), with a one-clause identification on first use.
- **From the Tradition adds, not explains**: the point is something a careful reader of the verses alone would not reach. If it only restates the verse, that is a major failure.

## Group 3 — Voice and style (major / minor)

- **No machine-tells**: no em-dashes in body prose (the title separator is allowed), no emojis.
- **Terms used, not paraphrased or defined**: common terms (bodhisattva, bodhicitta, samsara, merit, refuge, karma) appear by name, not swapped for loose stand-ins ("a truly good person") and not glossed.
- **Plain grammar around terms**: "those who carry bodhicitta", not "those in whom bodhicitta has arisen".
- **Describes what the verses do, not what the reader feels**: no "you feel a quiet respect"; no shaky human-nature claims ("there are two ways we react").
- **Consequences name who they fall on**: harm, benefit, merit each say to whom; no floating consequence.
- **No rhetorical question-and-answer** in From the Tradition; importance is shown by comparison or result, not labelled "great"/"profound".
- **Mechanisms explained in concrete steps**, not one compressed abstract sentence.
- **Readable for a non-native speaker**: common words, short sentences, no idioms or figurative phrases that fail if read literally, plain verbs over strained noun phrases.
- **Today's Practice is a gentle invitation**: no "Your task today", no stacked commands, soft/conditional framing, lets the reader off the hook, no meta closing label, offers a doable action rather than asking the reader to watch a presumed negative feeling.
- **Formatting is light**: bold only on a few key phrases (claim, name, the line worth remembering), never whole sentences or every paragraph.
- **No forbidden elements**: benefits list, end glossary, Tibetan labels as headers, bullet "application" blocks, "Today I will…" device, parenthetical keyword tags, "profound benefits", "great teacher Shantideva", collective-attribution opener, sub-headers below `##`, horizontal rules between sections.

## Group 4 — Limits (minor unless far off)

- Notification (title) ≤ 12 words; no rhetorical question; specific to the day.
- Push-notification hook ≤ 12 words.
- Opening intro: 2–4 sentences, ≤ 60 words.
- From the Tradition: prose only, roughly 90–120 words, max 150.
- Today's Practice: one instruction, tight (one or two lines), second person, present tense.
- No diacritics in English prose.

---

## Output format

Produce a scorecard, then a verdict.

```
# Evaluation — Day [N] ([file])

Verdict: READY TO COMPLETE | NEEDS FIXES (n critical, n major, n minor)

## Critical
- [check] — "quoted offending text" → suggested fix

## Major
- [check] — "quoted offending text" → suggested fix

## Minor
- [check] — "quoted offending text" → suggested fix

## Passed
- short list of the notable checks that passed (structure, grounding, etc.)

## Rating
[N]/10 — [label]. One sentence justifying the score.
```

The rating is always the last thing in the report.

Rules for the report:
- Quote the exact text for every failure. Never describe a problem without showing it.
- Give each failure a concrete one-line fix, not a vague note.
- Be specific about location (which section).
- Do not rewrite the whole day. Suggest the fix; let the author apply it.

---

## Verdict rule

- **READY TO COMPLETE** only if there are zero critical and zero major issues. Minor issues may remain at the reviewer's discretion.
- Any critical issue → **NEEDS FIXES**, and the day must not be promoted to `status: complete`.
- The evaluator never sets `status: complete` itself. A domain specialist makes that call after the critical and major issues are cleared.

---

## Rating scale

End every evaluation with one overall rating out of 10. The rating summarises quality, but fidelity is non-negotiable, so the severities cap it:

- **9–10 — Excellent, ready.** Zero critical, zero major. 10 = nothing to fix; 9 = one trivial minor. Could be published as written.
- **7–8 — Good, ready with optional polish.** Zero critical, zero major, a few minors.
- **5–6 — Needs fixes.** Zero critical, one or two major. Not ready; clear the majors and re-evaluate.
- **3–4 — Weak.** Zero critical, three or more major, or style problems throughout. Substantial rework.
- **1–2 — Reject.** Any critical issue at all (a claim not traceable to the rails, altered verse or liturgy text, content not from the sources). Must not be used or marked complete, however good the rest is.

Capping rules:
- Any critical issue forces the score into **1–2**, regardless of other strengths.
- Any major issue caps the score at **6**.
- A score of **7 or above** corresponds to "READY TO COMPLETE"; **6 or below** corresponds to "NEEDS FIXES".
- The rating is a reviewer aid, not permission to publish. Only a domain specialist sets `status: complete`.

---

## Notes

- This skill reads and reports only. It does not edit the day file.
- If the day was built from interim `en-ai` sources rather than `complete` `2-RAILS` packages, note it in the report: grounding was checked against interim material and still needs specialist confirmation.
- Keep this skill in sync with `english-plan-generator`. Every checklist item and slop indicator there should have a matching check here.
