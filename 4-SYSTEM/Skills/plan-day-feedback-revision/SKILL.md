---
name: plan-day-feedback-revision
description: Audit an existing Bodhisattva Challenge plan day file against the Day-1 tester feedback criteria and revise it in place to fix every content issue the testers raised, without breaking the 6-section format or the citation chain.
---

# plan-day-feedback-revision

This skill takes a day file that already exists in `3-TRANSFORMATIONS/Plans/the-bodhisattva-challenge/en/Days/` and improves it against the documented Day-1 user feedback. It runs in two phases: an **audit** that scores the file against seven feedback-derived criteria and records every finding, then a **revision** that rewrites the file in place to clear those findings. It exists because Day-1 testers reported that the plan content felt AI-generated, too abstract for the Tier 3 audience, poorly oriented, and untrustworthy — and a single read-through is not enough to catch and fix those problems consistently across 365 days. Correct output is a day file that still matches the `english-plan-generator` 6-section structure exactly, but reads as human-written, plainly relevant to a 5-minute-a-day practitioner, fully oriented, and traceable claim-by-claim to the source rails.

The feedback this skill operationalises is recorded in `webuddhist-knowledge/30_PRODUCTS/31_App/Research/Plan_Content_Feedback/Day_1/Day_1_Summary.md`. This skill addresses only the **content** themes from that summary. App and UX themes (audio playback, dark mode, streak tracking, plan-card images, in-app navigation to recitation) are out of scope — they are not fixable in a rails day file and must be routed to the product team instead.

---

## Inputs

| Input | Description | Path / format |
|---|---|---|
| **Target day file** | The day file to revise. Required. If a range is given (e.g. days 1–10), process one file at a time. | `3-TRANSFORMATIONS/Plans/the-bodhisattva-challenge/en/Days/[DAY].md` |
| **Generator contract** | The authoritative format and style rules for a day file. Read in full before revising — this skill never relaxes a rule it sets. | `4-SYSTEM/Skills/english-plan-generator/SKILL.md` |
| **Feedback summary** | The Day-1 findings these criteria are derived from. | `webuddhist-knowledge/30_PRODUCTS/31_App/Research/Plan_Content_Feedback/Day_1/Day_1_Summary.md` |
| **Audience profile** | The Tier 3 persona the content must serve (regular learner, 5–10 min/day, re-entry, no scholarly depth assumed). | `webuddhist-knowledge/40_DOCS/45_Reference/Personas.md` |
| **Liturgy asset** | The verbatim opening and closing liturgy that sections 2.2 and 2.5 must reproduce exactly. | `3-TRANSFORMATIONS/Plans/the-bodhisattva-challenge/en/assets/liturgy.md` |
| **Source rails (for re-grounding 2.4 / 2.6)** | The verse context the commentary note and practice challenge must trace to. Prefer the rail package; fall back to interim summaries. | `2-RAILS/Verses/<verse-id>.md` (preferred, `status: complete` only) → `3-TRANSFORMATIONS/Translations/en-ai/Verses/<verse-id>.md` (interim) |

If the target day file does not exist, stop and report it — this skill revises existing files only; it does not generate new days (use `english-plan-generator` for that). If neither a complete rail nor an interim summary exists for a verse, stop and flag the dependency — never invent commentary content to satisfy the credibility criterion.

## Output

Two files per day processed:

1. **The revised day file**, overwritten in place at
   `3-TRANSFORMATIONS/Plans/the-bodhisattva-challenge/en/Days/[DAY].md`.
   Same 6-section structure as the generator produces, plus a `revision` block added to its frontmatter.

2. **The audit record**, written to
   `3-TRANSFORMATIONS/Plans/the-bodhisattva-challenge/en/feedback-audit/[DAY].md`.
   One finding per criterion: PASS, or FAIL with the offending text and the fix applied. This is the paper trail; it is never cited from anywhere and is safe to delete.

---

## Output file format

### Revised day file frontmatter (add the `revision` block; keep existing keys)

```yaml
---
day: [DAY_NUMBER]
chapter: [CHAPTER_NUMBER]
verses: "[CHAPTER]-[START] to [CHAPTER]-[END]"
date: [unchanged]
status: draft
generation_note: "[unchanged]"
revision:
  skill: plan-day-feedback-revision
  date: [YYYY-MM-DD]
  feedback_source: "Day_1_Summary.md"
  criteria_failed_before: [C1, C4, C6]   # the criteria that were FAIL on audit
  out_of_scope_flags: ["audio asset requested for this day"]  # omit if none
---
```

The body keeps the exact 6-section structure defined by `english-plan-generator` — same `#` title (notification text), same six `##` headings in order (`Opening`, `Renewing the Bodhisattva Vow`, `Today's Verses`, `From the Tradition`, `Aspiration`, `Today's Practice Challenge`). This skill does not add, remove, rename, or reorder sections. It only changes their contents to clear audit findings.

### Audit record format

```markdown
---
day: [DAY_NUMBER]
audited: [YYYY-MM-DD]
result: revised | clean
---

# Day [DAY] — feedback audit

| Criterion | Verdict | Finding | Fix applied |
|---|---|---|---|
| C1 AI-slop markers | FAIL | 7 em-dashes used as connectors; "profound" in 2.1 | Replaced with periods/commas; removed "profound" |
| C2 Tier 3 accessibility | PASS | — | — |
| C3 Orientation | FAIL | 2.1 jumps into content; no sense of what the section is doing | Rewrote 2.1 to orient first |
| C4 Liturgy present & prominent | PASS | — | — |
| C5 Translation quality | FLAG | verse 2-14 English reads awkwardly ("...") | Flagged for translation track; verse text NOT rewritten here |
| C6 Credibility & sourcing | FAIL | claim in 2.4 not traceable to any rail | Removed; replaced with a cited point from Sazang Mati Panchen |
| C7 Reading load | PASS | — | — |

## Out-of-scope (route to product team)
- [audio / UX items the tester raised that this skill cannot fix]
```

---

## Rules

1. **Structure is fixed.** Never add, remove, rename, or reorder the six sections, and never introduce a sub-header below `##`. If a finding seems to require a new section, it is out of scope — record it, do not restructure.
2. **The citation chain holds.** Every claim in `From the Tradition` (2.4) and `Today's Practice Challenge` (2.6) must trace to a specific passage in the source rails. If you cannot locate the source, delete the claim; never paper over a gap with invented or parametric content. This rule outranks the desire to make the day feel complete.
3. **Source-derived text is read-only here.** Tibetan verse (2.3), the verse English translation (2.3), and the liturgy (2.2 / 2.5) are reproduced from their source files. This skill does **not** rewrite them. If a verse translation reads badly (criterion C5), record a FLAG in the audit and leave the verse text untouched — fixing translations belongs to the translation track, not this skill.
4. **No new slop while removing old slop.** When rewriting prose, do not trade one machine-tell for another. Reducing em-dashes does not mean inserting "moreover" / "furthermore" / "it is important to note." Plain, short, human sentences only.
5. **Revisions stay within the word caps.** 2.1 ≤ 60 words; 2.4 ≤ 150 words; 2.6 one instruction. If clearing a finding would exceed a cap, cut elsewhere — never exceed the cap to add credibility or context.
6. **Do not raise `status` to `complete`.** This skill leaves `status: draft`. Only a domain specialist marks a day complete.
7. **One day per run.** When given a range, fully audit-and-revise one day file (and write its audit record) before moving to the next. Do not batch-edit.
8. **Out-of-scope feedback is recorded, never acted on.** Audio, video, dark mode, streaks, card images, and navigation are app concerns. Note them in the audit record's out-of-scope section and in the frontmatter `out_of_scope_flags`; make no content change in their name.
9. **Write only to the two output paths.** Never modify `1-SOURCES/`, `2-RAILS/`, the liturgy asset, the schedule, or any other day file than the target.

---

## Procedure

### Step 1 — Load context

a. Read the target day file in full.
b. Read `english-plan-generator/SKILL.md`, the Day-1 feedback summary, and the Tier 3 persona section of `Personas.md`.
c. Read the source rail(s) for this day's verses — `2-RAILS/Verses/<verse-id>.md` if `status: complete`, otherwise the interim `en-ai/Verses/<verse-id>.md`. These are the only legitimate sources for re-grounding 2.4 and 2.6.
d. Open the liturgy asset so 2.2 / 2.5 can be checked against it verbatim.

### Step 2 — Audit against the seven criteria

Score each criterion PASS / FAIL (or FLAG for C5). Record the offending text verbatim for every FAIL.

- **C1 — AI-slop markers** *(feedback theme 1: "felt like generated by AI").* FAIL if any of: em-dashes used as sentence connectors (count them; replace with periods or commas); any emoji in body text; manufactured-enthusiasm words ("profound", "powerful", "beautiful", "deeply", "truly", "journey"); the forbidden phrases listed in the generator's "What is not permitted"; or visibly awkward, over-hedged phrasing.
- **C2 — Tier 3 accessibility** *(themes 4 & "too advanced for Tier 3").* FAIL if the content assumes scholarly background, stacks abstract Buddhist concepts without a concrete handle, uses an un-glossed less-common term, or if 2.6 does not name a real, ordinary situation a 5-minute-a-day practitioner would actually meet. The bar: a re-entry learner who is not a scholar can read it once and act on it.
- **C3 — Orientation** *(theme 2: "no onboarding or context").* FAIL if 2.1 (Opening) drops the reader into content without first situating today's verses inside the function of their section and chapter. On **Day 1 specifically**, the Opening must also briefly establish what this plan is and how a day works, since the reader has no prior context. Orient before teaching.
- **C4 — Liturgy present & prominent** *(theme 6: "recitation/liturgy buried or missing").* FAIL if 2.2 or 2.5 is missing, condensed, paraphrased, or deviates from the liturgy asset. Both must reproduce the asset verbatim in block-quote form, in the correct order.
- **C5 — Translation quality** *(theme 5).* FLAG (do not FAIL-and-rewrite) if a verse's English in 2.3 reads "off" or unclear. Record the verse ID and the phrasing. Leave the verse text unchanged — see Rule 3.
- **C6 — Credibility & sourcing** *(themes 7 & 1: trust).* FAIL if any claim in 2.4 or 2.6 cannot be traced to the source rail, if 2.4 makes a specific attribution without naming the commentator (Gyaltsab Darma Rinchen, Sazang Mati Panchen, or Ngulchu Thokme Zangpo), or if 2.4 reads as generic synthesis that could apply to any verse.
- **C7 — Reading load** *(theme 3: "too long", "like reading a PDF").* FAIL if 2.1 exceeds 60 words, 2.4 exceeds 150 words, 2.6 is more than one instruction, or any prose section pads a single point across multiple sentences. Tighten to the caps; cut what a busy reader would skip.

### Step 3 — Revise to clear every FAIL

Working section by section, rewrite only what is needed to turn each FAIL into a PASS, honouring all Rules:

a. **C1:** Replace em-dash connectors with periods or commas; delete emojis and enthusiasm words; remove any forbidden construction; smooth awkward sentences into short plain ones.
b. **C3:** Rewrite 2.1 so it orients first (section/chapter function; Day-1 plan-context if applicable), within 60 words, without summarising or teaching the verses.
c. **C2:** Make 2.4 land one concrete idea in plain language with any less-common term glossed in one clause; make 2.6 name a specific ordinary situation and point toward doing less harm, doing more good, or knowing one's mind better.
d. **C6:** For any unsourced claim, locate a real point in the rail and rewrite to it, naming the commentator where a specific attribution is made; if no source exists, cut the claim. Ensure 2.6 traces to what 2.4 actually says.
e. **C4:** Restore 2.2 / 2.5 verbatim from the liturgy asset if they drifted.
f. **C7:** Trim to the word caps; keep one point per section.
g. Re-check the `#` notification title: specific to the day, ≤ 12 words, no rhetorical question, no affirmation, no manufactured hype.
h. Leave all source-derived text (2.2, 2.3, 2.5) unchanged except to restore 2.2 / 2.5 from the asset.

### Step 4 — Update frontmatter and write both files

a. Add the `revision` block to the day file frontmatter (Step "Output file format"), listing the criteria that were FAIL before revision and any out-of-scope flags. Keep `status: draft`.
b. Overwrite the day file at `…/en/Days/[DAY].md`.
c. Write the audit record to `…/en/feedback-audit/[DAY].md` (create the `feedback-audit/` folder if absent), with one row per criterion and an out-of-scope section.

### Step 5 — Self-verify

Re-read the revised day file against Step 2. If any criterion would now FAIL, fix it before reporting done. Confirm the structure is byte-for-structure identical to the generator's six sections and that no source-derived text was altered.

---

## Completion check

- [ ] Target day file existed and was read in full; generator contract, feedback summary, persona, source rail(s), and liturgy asset all loaded.
- [ ] All seven criteria scored, with offending text recorded verbatim for every FAIL.
- [ ] Every FAIL cleared in the revision; C5 translation issues FLAGGED only, with verse text left unchanged.
- [ ] Six sections intact, in order, no sub-headers below `##`; source-derived text (2.2/2.3/2.5) unchanged except verbatim liturgy restoration.
- [ ] 2.1 ≤ 60 words, 2.4 ≤ 150 words, 2.6 a single instruction; notification title ≤ 12 words and specific.
- [ ] Every 2.4 / 2.6 claim traceable to the source rail; commentators named where attributed; no invented content.
- [ ] `revision` block added to frontmatter; `status` left as `draft`.
- [ ] Audit record written to `…/en/feedback-audit/[DAY].md` with one row per criterion and an out-of-scope section.
- [ ] Out-of-scope (audio/UX) feedback recorded, not acted on.
- [ ] Self-verify pass completed with no remaining FAIL.
