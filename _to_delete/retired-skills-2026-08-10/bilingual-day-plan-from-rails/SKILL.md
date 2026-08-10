---
name: bilingual-day-plan-from-rails
description: Generate grounded English and Hindi Bodhisattva Challenge day-plan files from the Tibetan day file and the 2-RAILS/Verses/ commentary summaries, for chapters where rails coverage exists. Use when asked to create, write, or fill in missing day plans (in English, Hindi, or both) for a given day number or verse range, where a bo/ Tibetan day file already exists. Not for chapters that lack 2-RAILS/Verses/ summaries — that case needs a different approach.
---

# Bilingual Day Plan From Rails

Produces one or more day-plan files (English and/or Hindi) for the Bodhisattva
Challenge, grounded in the `2-RAILS/Verses/<chapter>-<verse>-summary.md` files
rather than in the Tibetan day file alone. The Tibetan day file tells you the
day's chosen angle and practice; the rails are the actual source of what goes
on the page. Conflating the two is the most common failure mode in this
domain — see Step 3.

## When this applies

- A Tibetan day file exists at
  `3-TRANSFORMATIONS/Plans/the-bodhisattva-challenge/bo/Chapter-<C> D<start>-D<end>/Day-<N>-Ch<C>-V<start>-<end>.md`.
- A rails summary exists for every verse the day covers, at
  `2-RAILS/Verses/<C>-<V>-summary.md`.
- If rails are missing for one or more verses in range, stop and say so
  before writing anything — do not fall back to translating the Tibetan day
  file directly (that produces exactly the two failures the English
  requirements doc warns about: gaps filled by the writer's own reasoning,
  and attributions bundled onto whoever is named last).

## Step 0 — Scope and ask

Before touching any source file, confirm with the user (unless clearly
unattended):
- Which day(s) / verse range(s), exactly.
- Which language(s): English only, Hindi only, or both.
- Anything unusual about the range worth flagging up front — e.g. a verse
  source that doesn't cover this range yet, a chapter boundary, a known gap
  in either termbase. Check for these before asking, not after.

Do not silently expand scope beyond what was asked, and do not silently
narrow it either — if a blocker exists for part of the request, name the
blocker and ask how to proceed for that part while continuing with the rest.

## Step 1 — Gather every source before writing anything

Read, in this order:

1. `en/requirements.md` and `en/termbase.md` (if writing English)
2. `hi/requirements.md` and `hi/termbase.md` (if writing Hindi)
3. The Tibetan day file(s) for the day(s) in scope
4. `bo/schedule-corrected.md` — confirm the verse range assigned to each day
   number actually matches what you were asked to write
5. Two or three **recent, already-approved** day files in each target
   language, as a control on what "accepted practice" looks like right now
   — requirements.md documents intent, but actual practice can drift from it
   (e.g. a different verse-text source than the one named in the doc). When
   the two disagree, match practice and flag the conflict in
   `generation_note` rather than silently picking one.
6. The verse-text sources, which are fixed:
   - English: `AI_translation/english/bca-english-plain.md`
   - Hindi: `AI_translation/hindi/bca-hindi-plain.md`
   These are the current canonical sources. Confirm they actually cover
   every verse in range (search for the `^<C>-<V>` block ID for each verse
   before relying on the file) — do not assume coverage from a chapter-level
   glance.
7. `2-RAILS/Verses/<C>-<V>-summary.md` for every verse in range, in full —
   not skimmed. Each file has: per-commentator explanations, a `⚑`-marked
   divergences section, metaphors/stories, main teaching points, key terms,
   and a synthesis. All of it is candidate material; almost none of it goes
   on the page (see Step 3).

Do not start drafting until all of this has been read once. Writing from
partial context is what produces attribution errors later.

## Step 2 — Verify verse text before quoting it

- English: locate the exact verses by block ID (`^<C>-<V>`) in
  `AI_translation/english/bca-english-plain.md`.
- Hindi: locate the exact verses by block ID in
  `AI_translation/hindi/bca-hindi-plain.md`.
- If either canonical source does not yet cover a verse in range, stop and
  ask how to proceed (wait for the source to be extended, fall back to a
  different source, or leave a placeholder) — do not silently substitute a
  different register or source.
- Check the block IDs are contiguous and match the day's `verse:` frontmatter
  before writing a single word of commentary.
- Note for older days (roughly 15–31): those were written against different
  verse sources (`BCA-Full-Children-English.md` for English,
  `bca-hi-poetic.md` for Hindi), which is why their register may not exactly
  match new days written from the canonical sources above. Don't imitate
  that older sourcing choice going forward — flag the mismatch across the
  chapter if it's visible, but write new days from the current canonical
  sources.

## Step 3 — Draft the commentary section: one idea, full provenance

For each day:

1. Pick **one** added idea — something the commentary contributes that a
   careful reader of the bare verses would not reach. It must trace to a
   specific main teaching point or key term in the rails, with its citation.
2. Attribute it to whichever commentator is the *first-cited* source for
   that specific point in the rails — not to whoever else happens to be
   co-cited nearby, and not to whoever is more "recognizable." Check the key
   term / main-point citation order, don't assume.
3. Write the section using only content traceable to a citation. If a
   sentence sounds like a reasonable inference but isn't traceable, cut it
   — even if it reads well and even if the reference days contain similar
   uninferenced sentences.
4. Preserve every `⚑` divergence for verses in range without adjudicating
   it: state the shared ground, and if the page must pick a reading (e.g.
   "at death" vs. a minority reading), say in `generation_note` that a
   choice was made and why, rather than presenting one reading as
   uncontested.
5. Note explicitly when a verse opens a new section relative to the
   previous day (e.g. a numbered sequence like "the four powers" moving
   from its first item to its second) — both on the page and by picking up
   any half of the practice instruction the previous day's draft may have
   dropped.
6. First-use rule for any named sequence with parts (like "the four
   powers"): if you name it as one-of-N, gloss what the other parts are per
   the termbase, or don't name it as one-of-N at all.

## Step 4 — `generation_note`: write it as an audit trail, not a summary

For every day file, the note must let a stranger re-derive your choices
without re-reading the rails. Include:

- Which rail passage grounds the added idea, with citation, and which
  commentator it is actually attributed to and why (see Step 3.2).
- Everything of substance left in the rails and not carried to the page —
  named specifically, with a reason (usually: length). If you claim
  something "has no story in the rails," verify that by checking for a
  `སྒྲུང་འགྲེལ།` / narrative section for that verse — don't assert it from
  memory.
- Every `⚑` divergence for verses in range, whether or not it made the page.
- Which practice-category label (if any) came from an actual parenthetical
  in the Tibetan day file's practice section, versus which is your inference
  — flag inferred labels for human confirmation rather than presenting them
  as sourced.
- Any conflict between what the requirements doc says to do and what
  reference days actually do (verse source, formatting quirks, etc.) —
  named plainly, not silently resolved either way.

Write the Hindi note in Hindi, re-derived from the day's own choices — do
not machine-translate the English note, since the two languages' notes will
diverge (e.g. Hindi has its own termbase gloss requirements the English note
doesn't need).

## Step 5 — Translate to Hindi from the English day file, not from Tibetan

- Source is the English day file already written for that day, plus the
  Hindi verse source and Hindi termbase.
- Nothing in the English gets added to or dropped from the Hindi — check
  every sentence has a counterpart, especially payoff/closing sentences,
  which are the easiest thing to lose in translation.
- Register: short sentences, everyday vocabulary per the Hindi termbase's
  explicit avoid-list, no word repeated more than once or twice in a
  section — vary it or use a pronoun.
- Watch for a poetic verse source that has folded a commentary gloss into
  the verse text itself (check the requirements doc for a flagged instance
  of this). If so, the commentary section should acknowledge that the
  reader already saw that gloss inside the verse quote, rather than
  re-presenting it as new information.
- Check pronouns resolve unambiguously — Hindi drops antecedents more
  easily than English; if it's not obvious who "he" or "it" refers to, name
  the referent.

## Step 6 — Adversarial self-audit before delivering

Do not deliver on the strength of your own read of the file you just wrote.
Run a second, independent pass — ideally a fresh agent with no memory of the
drafting — instructed explicitly to find contract violations, not to
summarize or approve. Give the auditor:

- The requirements + termbase files for each language
- Two or three reference days as the accepted-practice baseline
- The rails files, to check attribution and divergence-flattening
- Explicit instruction to check: heading wording/order, word counts per
  section, commentator-count limit, banned punctuation/diacritics/emojis,
  claim traceability, divergence flattening, termbase compliance, whether
  today's practice actually differs from the last two days, register
  quality (repetition, ambiguous pronouns, calqued phrasing), and frontmatter
  completeness.

Fix every finding that survives a check against the actual source files —
don't take the auditor's word for a claim about a source without verifying
it yourself if the stakes justify it (the auditor can also be wrong).

## Step 7 — Mechanical verification

Before delivering, script-check (don't eyeball):

- Word counts per section against the stated ranges
- Heading text and order match exactly, including numeral style (Hindi:
  Devanagari numerals in headings)
- Quoted verse text is byte-identical to the source, including trailing
  punctuation/spacing that produces line breaks
- Block IDs are contiguous and match frontmatter
- No em-dash / diacritic / emoji violations in body prose (verse quotes are
  exempt where the source itself uses them)

## Step 8 — Deliver

Send the files, and if the vault is on a connected device, write them back
to the correct `Days/Chapter-<C> D<start>-D<end>/` folder in each language.
Do not mark `status: complete` — that is a domain specialist's call, not the
generator's.

## Known failure modes seen in practice

- Using an older reference day's verse source (`BCA-Full-Children-English.md`,
  `bca-hi-poetic.md`) instead of the current canonical source
  (`bca-english-plain.md`, `bca-hindi-plain.md`), producing a page whose
  register doesn't match either the new standard or, if mixed within one
  day, itself.
- Attributing an added idea to a commentator who is merely co-cited, not
  the actual first/sole source — check citation order on the specific main
  point, every time.
- Presenting an inference as commentary because it "sounds like" something
  the rails would say — if you can't point to the sentence in the rails, cut
  it.
- Flattening a divergence inside a fused paraphrase (e.g. combining two
  distinct readings into a third reading nobody actually holds).
- Two consecutive days ending up with the same practice action because a
  distinguishing half of the Tibetan instruction (e.g. "for self and
  others") got dropped in the first day's draft.
- Naming a sequence-with-parts ("first of four...") without glossing the
  other parts, leaving a first-time reader with an unexplained count.
- A `generation_note` claim that is checkable and wrong (e.g. "no story in
  the rails" when a narrative section exists) — every checkable claim in the
  note should actually be checked, not asserted from a skim.
