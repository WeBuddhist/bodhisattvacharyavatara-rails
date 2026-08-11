---
title: Fact-Check Report — 2-RAILS/Verses vs bca-english-plain (English, plain audience)
ground_truth: 2-RAILS/Verses/<chapter>-<verse>-summary.md (Key Terms + AI-Overview synthesis sections)
translation: AI_translation/english/bca-english-plain.md
audience: plain
scope: chapters 1-4 (chapter 4 limited to verses 1-20, the only range with rail coverage)
extraction_script: AI_translation/skills/scripts/rails_fact_check_extract.py
status: draft
---

# Fact-Check Report: 2-RAILS/Verses × bca-english-plain (English)

Prepared by: Claude, at the user's request, adapting the vault's `commentary-fact-check`
methodology (`4-SYSTEM/Skills/commentary-fact-check/SKILL.md`) to a different ground
truth.

**Ground truth used:** `2-RAILS/Verses/<id>-summary.md` — specifically each verse's
གནད་ཚིག (Key Terms) table and བསྡུས་དོན (AI-Overview synthesis), which are themselves
draft syntheses of 6-8 Tibetan commentaries. **These rail files are all
`status: draft`** (0 files under `2-RAILS/Verses/` are `status: complete` as of this
run) — per `4-SYSTEM/CLAUDE.md` §7, a draft rail is not yet a domain-specialist-approved
source. Findings below should be read as "the translation disagrees with the current
draft synthesis," not as a final verdict on either file.

**Deviation from workspace convention, flagged for the record:** `AI_translation/skills/requirements.md`
§0 states this workspace "does not read `2-RAILS/`" and that commentary-grounded
fact-checking should use the vault's `commentary-fact-check` skill against raw
`1-SOURCES/Commentaries/`. This report deliberately uses `2-RAILS/Verses/` instead,
per explicit instruction. Coverage is therefore capped at chapters 1-4 (the only
chapters with rail summaries); a full-text fact-check would still need the raw-commentary
route or additional rails.

**Method:** term-by-term alignment against the rail's Key Terms glosses (the closest
rail equivalent to a commentary's own glosses), not a gist check. Stance: assume the
translation contains errors; a verse is not cleared until its key terms are checked.
Severity key:
- **ERROR** — the English names the wrong thing (wrong referent, wrong named entity,
  wrong number/scope, kāya/mind/dharma swap, wrong simile tenor) — flagged even if fluent.
- **SOFTENING** — a precise term generalized to a vaguer one; may be acceptable at
  the `plain` audience register (which permits "technical terms rendered into ordinary
  words," per `AI_translation/audience_profile/plain.md`) but is logged so a human can
  decide.
- **NOTE** — editorial observation, no action implied.

---

## Progress

| Scope checked | Verses | Errors | Softening | Notes |
|---|---|---|---|---|
| Chapter 1 (1-1 to 1-36) | 36 | 2 | 3 | 1 |
| Chapter 2 (2-1 to 2-65) | 65 | 0 | 2 | 2 |
| Chapter 3 (3-1 to 3-33) | 33 | 0 | 0 | 1 |
| Chapter 4 (4-1 to 4-20, partial — only range with rail coverage) | 20 | 0 | 0 | 1 |

**Totals so far: 154 verses checked, 2 ERROR, 5 SOFTENING, 5 NOTE.**

---

## Chapter 1 — Explaining the Benefits of the Mind of Awakening

### ERROR — verse 1-20
**English:** "...in response to a reasonable request from the bodhisattva **Samantabhadra**."
**Rail key term (`ལག་བཟངས་ཀྱིས་ཞུས་པ`):** "the sūtra requested by Bodhisattva **Bhadrapāla**" (བྱང་ཆུབ་སེམས་དཔའ་ལག་བཟངས་ཀྱིས་ཞུས་པའི་མདོ་སྡེ།).
**Issue:** Wrong named entity. `ལག་བཟངས` (lag bzangs, "Good Hand") = **Bhadrapāla**, the bodhisattva who requested the sūtra Śāntideva cites here (the headache-relief simile in 1-21/1-22 comes from this same sūtra). `ཀུན་ཏུ་བཟང་པོ` (kun tu bzang po) is the Tibetan for **Samantabhadra**, a different, unrelated bodhisattva. This is a straight name swap, not a stylistic choice — confirmed independently against the Bhadrapālaśreṣṭhipariprcchā-sūtra citation that published translations (Padmakara, Wallace) also identify at this verse.
**Fix:** "...from the bodhisattva Bhadrapāla."

### ERROR — verse 1-5
**English:** "...does worldly merit and **wisdom** arise."
**Rail key term (`བསོད་ནམས་ཀྱི་བློ་གྲོས`):** "the mental clarity/intention to accomplish virtue; the aspiration for that purpose" (དགེ་བ་སྒྲུབ་འདོད་ཀྱི་བློ་གྲོས་ཀྱི་སྣང་བ། དོན་གཉེར་གྱི་འདུན་པ།) — a single mental state (an inclination toward merit), not the doctrinal pair "merit and wisdom" (བསོད་ནམས་དང་ཡེ་ཤེས་, the two accumulations).
**Issue:** `bsod nams kyi blo gros` names one thing — a fleeting virtuous turn of mind in worldly people — and the verse's point is that even *that* is rare. Splitting it into "merit and wisdom" imports the two-accumulations doctrine, which isn't what this term denotes here. Corroborated by Wallace's published rendering ("a meritorious state of mind [puṇyadhī] rarely arises") and Padmakara's ("a wish for merit... arises").
**Fix:** something like "...does a virtuous state of mind rarely arise" (dropping "wisdom," which isn't in the term).

### SOFTENING — verse 1-1
**English:** "...their spiritual children, / who **embody the truth**, and all worthy ones."
**Rail key term (`ཆོས་ཀྱི་སྐུ`):** dharmakāya — "the dharmadhātu utterly free of stain" (the realization aspect) / "the profound and vast scriptural corpus" (the teaching aspect) (རྟོགས་བྱ་ཆོས་སྐུ་ = ཆོས་ཀྱི་དབྱིངས་ཤིན་ཏུ་དྲི་མེད་པ། བསྟན་བྱ་ཆོས་སྐུ་ = ཟབ་རྒྱས་ལུང་གི་ཆོས་ཕུང་།).
**Issue:** This is the exact error class the vault's own `commentary-fact-check` skill names as its canonical example — *chos kyi sku* (dharmakāya, a buddha-**body**) softened to an abstraction ("the dharma" / here "the truth"). Two problems compound: (1) "the truth" drops the kāya/body sense entirely; (2) English clause order — "the buddhas, their spiritual children, / who embody the truth, and all worthy ones" — lets "who embody the truth" read as modifying "their spiritual children" (the nearest noun) rather than "the buddhas" (the correct referent; only sugatas possess the dharmakāya in this verse, not their bodhisattva offspring).
**Fix:** re-attach the clause unambiguously to the buddhas, e.g. "I bow to the buddhas who possess the dharma-body, together with their spiritual children, and to all worthy ones," and consider keeping "body" in some form even at plain register (e.g. "who embody the Dharma" is closer than "the truth," though still soft).

### SOFTENING — verse 1-13
**English:** "Even if one has committed **extremely unbearable misdeeds**..."
**Rail key term (`མཚམས་མེད` / ānantarya):** the five specific heinous crimes — patricide, matricide, killing an arhat, wounding a buddha, causing schism in the saṅgha.
**Issue:** The verse's force is that bodhicitta can save someone even from *this specific worst-case category* (the five ānantarya), not misdeeds in general. "Extremely unbearable misdeeds" is a defensible plain-register paraphrase but loses that it's a named, enumerated class rather than a superlative description — worth a human call on whether "plain" register should keep some marker (e.g. "even the five most terrible crimes") given how central this category is to the verse's rhetorical force.

### SOFTENING — verse 1-32
**English:** "...giving **merely a moment's food**, or satisfying them for half a day with disdain."
**Rail key term (`ནར་མའི་ཟས་སྦྱོར`):** food given **regularly, without interruption** — commentaries specify yearly or monthly, in small installments each time (ཟས་རྒྱུན་མ་ཆད་པའི་སྦྱོར་བ། ... ལོ་རེ་ཟླ་རེའི་སྦྱོར་བ ... རྒྱུན་མི་འཆད་ཀྱང་ཐུང་ཐུང་ཞིག).
**Issue:** genuine doubt, flagging rather than asserting — "merely a moment's food" reads as a **one-off** act, but the rail's commentary gloss describes a **sustained, repeated** small offering (small each time, but ongoing). If the gloss is right, the translation inverts a "small but regular" habit into a single brief instance, which changes what kind of generosity is being (mildly) praised before the next verse's continuous bodhisattva generosity. Given this is one of the more collapsed/telegraphic key-term entries in the rail file, I'd want a second opinion before calling it an ERROR — see open question below.

### NOTE — verse 1-4 (pattern, not a single-verse issue)
**English:** "This opportunity is very hard to find."
**Rail key term (`དལ་འབྱོར`):** the precious human rebirth — 8 leisures + 10 endowments, 18 qualities by name.
This collapses a named 18-fold doctrinal category to generic "opportunity." Acceptable under the `plain` audience profile ("technical terms rendered into ordinary words"), but since `dal 'byor` is a recurring BCA term, flagging here so the same choice can be checked for consistency in later chapters rather than re-litigated verse by verse.

**Result: 34/36 clean on the term-by-term pass, 2 errors, 3 softening notes, 1 pattern note.**

---

## Chapter 2 — Confession of Misdeeds

Named-entity check (this chapter names eight great bodhisattvas across 2-13, 2-22, 2-49–2-52):
Samantabhadra (2-13, 2-49), Mañjuśrī (2-13, 2-22, 2-49), Avalokiteśvara (2-13, 2-50),
Ākāśagarbha (2-51), Kṣitigarbha (2-51), Vajrapāṇi (2-52) all check out correctly against
their rail terms — no name swaps found in this chapter, unlike 1-20.

### SOFTENING — verse 2-1
**English:** "...the buddhas, the sacred Dharma, / the **pure jewels**, and the spiritual children..."
**Rail key term (`དཀོན་མཆོག་དྲི་མ་མེད་`):** "free of the two obscurations" — this is the
technical term for the **[Noble] Saṅgha**, the third of the Three Jewels, here named
separately from the bodhisattva "spiritual children" that follow it.
**Issue:** "the pure jewels" (plural, generic) doesn't signal to an English reader that
this is naming the Saṅgha specifically — it reads as a class of gemstones rather than
the third Jewel. The four-part addressee structure (Buddha / Dharma / Saṅgha / bodhisattva
offspring) is preserved in count but the third item's identity is obscured.
**Fix:** "the stainless Saṅgha" or "the pure Sangha jewel" would keep the Three-Jewels
structure legible.

### NOTE — verse 2-14 (terminology, flagging for consistency check)
**English:** "...whose sweet scent / fills the **triple world**..."
**Rail key term (`སྟོང་གསུམ་`):** the **trichiliocosm** — a specific cosmological unit
(a "three-thousandfold great chiliocosm"), explicitly distinguished in the rail's own
gloss from the more familiar "three realms" (khams gsum: desire/form/formless).
**Issue:** "the triple world" is the conventional English rendering of *khams gsum*
(the three realms), a different term. Using it for *stong gsum* risks the reader
assuming the more familiar concept. This may be a defensible plain-register choice
(both are "the whole of existence" in effect) but flagging since the two Tibetan terms
are commentarially distinguished and a scholarly-register pass should not conflate them.

### NOTE — verse 2-8 (not rail-anchored, flagging as an open question)
**English:** "May the **Supreme Bodhisattvas** completely accept me."
The rail's key terms for this verse only glossed "རྒྱལ་" (buddhas, in the preceding
line "To the buddhas and their spiritual children..."); no term covers the addressee of
the second line directly, so this isn't a rail-confirmed error. In the standard verse
structure the request to "accept me" is usually addressed to the same pair just named
(buddhas *and* bodhisattvas together, e.g. "skyes bu mchog" / "supreme beings"), not to
bodhisattvas alone. Narrowing "Supreme Beings" to "Supreme Bodhisattvas" would quietly
drop the buddhas as addressee of the request. Flagging for a second opinion since I
can't anchor it to a rail gloss the way the other findings are anchored.

### NOTE — verses 2-30/2-31, rail divergence not surfaced in the translation
**Rail key term (`གཞན་དག` ⚑):** flagged divergence — commentators split between reading
this as **"other teachers/preceptors"** (kunpal, gyaltsab, ngulchu-thogmed, sabzang,
minyak-kunzang-sonam, khenpo-kunga) and **"other suffering beings"** — the sick,
protector-less, hungry and thirsty, an object of compassion (khenpo-zhengah,
tenzin-gyatso). English resolves silently to "other teachers," which is a legitimate
translation choice (a flowing verse translation has to pick one reading), but per
`4-SYSTEM/CLAUDE.md` §8 ("divergences — never flatten") this is exactly the kind of
split a domain specialist should confirm is the intended reading rather than a default.

**Result: 65/65 clean on named entities (the chapter's highest-risk error class); 2 softening notes, 2 open questions not rail-anchored.**

---

## Chapter 3 — Full Acceptance of the Mind of Awakening

This chapter is mostly aspiration/wish verses (becoming a boat, medicine, wish-fulfilling
jewel, etc. for beings) with few named entities and few doctrinal-category terms to
misname — the error classes that produced findings in chapters 1-2 are largely absent
here. The multi-item similes (3-17: boat/ship/bridge scaled to small/medium/large water;
3-19: jewel/vase/mantra/medicine/tree/cow, six items) all check out in the correct
order against their rail terms — no swapped or dropped items.

### NOTE — verse 3-2
**English:** "...I also rejoice in the awakening of the protectors / and **the bodhisattvas on the paths**."
**Rail key term (`རྒྱལ་སྲས་ས`):** "the resultant stage" — specifically the bodhisattva
**grounds/bhūmis** (a distinct technical category from *lam*, "path," in the
five-paths/ten-grounds framework).
**Issue:** minor terminological blur — "on the paths" reads naturally in English but
conflates two named categories (path and ground) that the tradition keeps separate.
Likely harmless at `plain` register; flagging only because it's a recurring technical
pair (path vs. ground) worth keeping distinct if a `scholars`-register pass is ever
built from this same base text.

**Result: 33/33 clean — no named-entity or doctrinal-category errors found; 1 minor terminology note.**

---

## Chapter 4 — Heedfulness (verses 1-20 only — the only range with rail coverage; 4-21 to 4-48 have no `2-RAILS/Verses/` file yet)

The famous similes in this partial range (4-20's blind turtle and the yoke-hole in the
ocean) check out precisely against the rail's gloss — single hole, vast ocean, turtle
surfacing once a century, three converging improbabilities. One item considered and
ruled out below.

### Considered, not flagged — verse 4-7
**English:** "Even if **a person** abandons the Mind of Awakening..."
**Rail key term (`མི་གང`):** identifies the referent as **Ārya Śāriputra** specifically
(a canonical story: bodhicitta generated toward ten thousand buddhas in a past life,
then relinquished).
I checked whether dropping the name to generic "a person" is an entity error, but this
looks like commentarial identification of an unnamed root-verse reference rather than
something the verse itself names — published translations (Padmakara, Wallace) also
render this generically without naming Śāriputra in the verse proper, reserving the
identification for a footnote. Not flagging as an error; noting the check was made.

### NOTE — verse 4-5 (partial coverage of a two-tier warning)
**English:** "...merely thinks of giving... but does not give it, that person will become a hungry ghost."
**Rail key term (`དམ་བཅས་པ`):** distinguishes two tiers — merely *thinking* of giving and not
following through → rebirth as a hungry ghost (what the English covers); actually
**vowing** to give and not following through → rebirth in **hell**, a worse outcome.
The English only carries the first tier. This second tier reads as the term's own
bridge to verse 4-4's broader argument (breaking the vast bodhicitta vow) rather than
content verse 4-5 itself must state — flagging as a note rather than an error, since
I'm not fully certain the second tier belongs in 4-5's line versus being commentarial
scaffolding between 4-4 and 4-5.

**Result: 20/20 clean — no errors found in the covered range.**

---

## Summary — 154 verses, chapters 1-4 (the full rail-covered range)

| Severity | Count | Verses |
|---|---|---|
| ERROR | 2 | 1-20 (wrong bodhisattva name), 1-5 (merit/wisdom conflation) |
| SOFTENING | 5 | 1-1, 1-13, 1-32, 2-1, 2-14 |
| NOTE (open question, human input wanted) | 5 | 1-32 (same verse, doubt about severity), 2-8, 2-30/2-31, 3-2, 4-5 |

### Open questions for you

1. **1-20 and 1-5** are the two I'd act on without hesitation — confirmed against
   published translations, not just the rail.
2. **1-32** ("giving merely a moment's food") — I flagged this as SOFTENING but I'm
   genuinely unsure whether the rail's "small but regular" reading should override the
   translation's "one-off" framing, or whether the rail's telegraphic gloss is the
   less reliable side here. Would like your read before this goes further.
3. **2-8** ("May the Supreme Bodhisattvas completely accept me") — possible scope
   narrowing (buddhas dropped as addressee), but I couldn't anchor it to a rail
   citation the way the other findings are anchored, so treat this as lower-confidence.
4. Everything marked SOFTENING is plausibly fine at the `plain` audience register per
   `audience_profile/plain.md`'s license to render technical terms in ordinary words —
   I logged them for consistency-tracking across future chapters, not as claims that
   they're wrong.

### Coverage gap

Chapters 5-10 (and 4-21 to 4-48) have no `2-RAILS/Verses/` summaries yet, so this method
can't reach them without either building more rails or falling back to the vault's
`commentary-fact-check` skill against raw `1-SOURCES/Commentaries/`.

---

## Fixes applied — 2026-08-07

All three flagged items were resolved and edited directly into `bca-english-plain.md`:

| Verse | Before | After |
|---|---|---|
| 1-5 | "does worldly merit and wisdom arise" | "does a virtuous state of mind arise" |
| 1-20 | "from the bodhisattva Samantabhadra" | "from the bodhisattva Bhadrapāla" |
| 1-32 | "giving merely a moment's food" | "giving it only briefly each time, though regularly" |

Verified: re-ran `rails_fact_check_extract.py --chapters 1` and confirmed all three
verses still parse as 4-line blocks with intact segment IDs (`^1-5`, `^1-20`, `^1-32`).
Ran `AI_translation/skills/scripts/lint_translation.py` on the full file — zero errors
before line 705 (i.e. zero errors anywhere in chapters 1-3, the region touched by these
edits). Pre-existing lint errors from line 705 onward (chapter 4 onward) are a separate,
unrelated structural issue — see note below — not introduced by this pass.

## Open questions resolved — 2026-08-07

| Verse | Question | Decision | Fix |
|---|---|---|---|
| 2-8 | Does "Supreme Bodhisattvas" wrongly narrow the addressee, dropping buddhas? | Broaden the addressee | "May the Supreme Bodhisattvas completely accept me." → "May the Supreme Beings completely accept me." |
| 2-30/2-31 | `གཞན་དག` — "other teachers/preceptors" or "other suffering beings"? | Other suffering beings | "my parents, or other teachers," → "my parents, or other suffering beings," |

Verified: re-ran `rails_fact_check_extract.py --chapters 2` — 65/65 verses still pair
correctly, 2-8/2-30/2-31 parse with intact segment IDs and the new wording. No new lint
errors introduced (chapter 2 remains clean).

All 5 open questions from the Summary section above are now closed: 1-32 (resolved
earlier as SOFTENING, fix applied), 2-8 and 2-30/2-31 (resolved above), and the
remaining SOFTENING items (1-1, 1-13, 2-1, 2-14) are logged as acceptable at `plain`
register per the audience profile, not treated as errors requiring a fix.

### Separate issue found, not fixed here: block-ID placement is inconsistent from chapter 4 onward

`bca-english-plain.md` places each verse's `^chapter-verse` marker at the **end** of the
verse block in chapters 1-3, but at the **start** of the block from chapter 4 onward
(e.g. `^4-1` sits on the first line of that verse, not the last). This is what the
extraction script had to work around (see `ID_LINE_RE` handling in
`rails_fact_check_extract.py`), and it's also why `lint_translation.py` reports every
chapter-4-onward verse as an "empty verse block" — the linter assumes the id-at-end
convention throughout. This is a structural/formatting bug in the translation file
itself, unrelated to the fact-check findings above; flagging it here since it will
affect any tool built against this file's segment IDs. Worth a dedicated pass before
step 6 (vocab standardization) touches these chapters.

---
