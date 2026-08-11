# commentary-fact-check — Chapter 2, BCAC20_NKW Commentary

**Scope:** Padmakara (2006) English translation, Chapter 2 "Confession" (verses 2-1 to 2-65)
**Commentary:** `1-SOURCES/Commentaries/Transcluded/BCAC20_NKW_bo_segmented.md` — Khenpo Ngakwang Kunga Wangchuk (Dzongsar Shedra)
**Date:** August 11, 2026

Two `commentary-fact-check` runs, both against BCAC20_NKW:

1. **Clean audit** — the real, unmodified Padmakara translation, checked for actual translation issues.
2. **Detection benchmark** — the same translation with 20 deliberately injected errors, checked to see how many the skill catches.

Both translation files are wording-identical to the real, published Padmakara (2006) translation; only line-wrapping was changed (one verse per line) to match the skill's extraction script.

---

## Clean audit — no error injection

**File audited:** `padmakara-ch2-baseline-lines.md` (= real Padmakara wording, reformatted only)

**Result: 63/65 verses clean, 1 hard ERROR, 1 softening note.**

This surfaced a genuine finding in the real, published translation:

| Verse | Verdict | Tibetan (Wylie) | Commentary gloss | English | Issue |
|---|---|---|---|---|---|
| 2-38 | ⚠ ERROR | gti mug / chags / zhe sdang | the three poisons in the fixed order **ignorance → attachment → aversion** | "through **hatred, lust, and ignorance**" | The English reverses the commentary's order — a real, pre-existing mistranslation, not an injected one |
| 2-24 | softening | zhing rdul kun (dust of **all** buddha-fields) | cosmological, countless scope | "grains of dust upon **the earth**" | Narrows scope but doesn't rename the referent |

---

## Detection benchmark — 20 injected errors

**File audited:** `padmakara-ch2-test.md` (answer key: `answer_key_ch2.json`)

**Result: 10/20 injected errors caught as hard ERROR → Recall = 50.0%.** A further 4 were logged as softening notes only (flagged, but not at ERROR severity); 6 were missed with no flag at all.

### Recall by category

| Category | Caught (ERROR) / Total | Recall | Notes |
|---|---|---|---|
| kāya / dharma / mind swaps | 2 / 3 | 66.7% | 2-1, 2-14 caught; 2-48 downgraded to softening |
| Precise term softened to vague synonym | 0 / 3 | 0% | 2-9 downgraded to softening; 2-30, 2-63 missed entirely |
| Wrong named entity | 3 / 3 | 100% | 2-13, 2-50, 2-52 all caught — the skill also flagged the 2-50/2-52 pair as a coherent "one-step name shift" pattern |
| Wrong number / scope | 3 / 4 | 75% | 2-8, 2-24, 2-56 caught; 2-47 missed entirely |
| Wrong grammatical agent / role | 1 / 3 | 33.3% | 2-28 caught; 2-62 downgraded to softening; 2-6 missed entirely |
| Wrong enumeration order | 0 / 2 | 0% | 2-25 downgraded to softening; 2-26 missed entirely |
| Other wrong referent (body part) | 1 / 1 | 100% | 2-45 caught |
| Wrong simile tenor | 0 / 1 | 0% | 2-36 missed entirely |

### Cases missed entirely (no flag at all)

- **2-30** — "my defilements" → "my weaknesses"
- **2-63** — "transgressions of the precepts" → "minor slips of conduct"
- **2-47** — "every fear" → "certain fears"
- **2-6** — "accept these gifts of mine" → "bestow these gifts on me" (agent reversal)
- **2-26** — refuge enumeration reordered
- **2-36** — dream simile replaced with a candle simile

### Cases caught only as a softening note, not a hard ERROR

- **2-48** — "the Dharma they realized" → "the wisdom they hold" (kāya/dharma-class swap, but logged as a defensible gloss)
- **2-9** — "evils of my past" → "mistakes of my past"
- **2-62** — agent/cause-effect reversal, noted as "reads as reversing cause/effect" but not escalated to ERROR
- **2-25** — enumeration order swap, correctly identified as an order issue but kept at softening severity

### False positives / soft flags on negative controls

None of the 5 formal negative-control verses (2-3, 2-17, 2-33, 2-43, 2-60) received a hard ERROR verdict. One control (**2-60**) did receive a softening note ("teacher's precepts" narrowing a broader gloss) — a defensible style read on real, unmodified wording, not a confirmed defect.

---

## Comparison: before vs. after error injection

Same translation, same commentary (BCAC20_NKW), same 65 verses — the only difference between the two runs is whether the 20 errors are present.

| Metric | Before injection (clean) | After injection |
|---|---|---|
| Verses checked | 65 | 65 |
| Hard ERROR rows | 1 (a real, pre-existing issue at 2-38) | 10 |
| Verses with a hard ERROR | 1 | 10 |
| Softening / style notes | 1 | 9 |
| Verses fully clean (no ERROR, no note) | 63 | 46 |

Notably, **verse 2-38's real error (three-poisons reordering) was demoted from a hard ERROR in the clean run to a softening note in the injected run**, even though the wording at that verse didn't change between the two files — a sign of some run-to-run inconsistency in severity judgment, not just a function of what's actually on the page. Every other hard ERROR in the "after" run does trace back to one of the 20 deliberately injected changes.

---

## Comparison to Chapter 1's results (same commentary, same methodology)

| Metric | Chapter 1 | Chapter 2 |
|---|---|---|
| Verses | 36 | 65 |
| Recall (hard ERROR only) | 85.0% (17/20) | 50.0% (10/20) |
| Caught only as softening | 0 | 4 |
| Missed entirely | 3 | 6 |
| Hard false positives on controls | 0/5 | 0/5 |
| Soft flags on controls | 2/5 | 1/5 |

Recall dropped sharply on Chapter 2 relative to Chapter 1 under the same commentary. The weakest categories this chapter — precise-term softening (0%), enumeration order (0%), and agent/role (33%) — are largely the same categories that were weak in Chapter 1, but this chapter also lost ground on cases that should have been straightforward (e.g. 2-47's clear "every"→"certain" scope change went unflagged, where equivalent cases in Chapter 1 were caught). This is consistent with the earlier finding that word-relationship and modifier-level errors are this skill's structural blind spot — and suggests that blind spot gets worse, not better, as chapters get longer and the commentary's own explicitness per verse thins out.

---

## Conclusions

1. The clean audit surfaced one genuine, real error in the published Padmakara translation at 2-38 (the three poisons given in reversed order) — independent of the benchmark, a legitimate finding worth flagging to a translation reviewer.
2. On the fault-injected file, recall fell to 50% (10/20), notably lower than Chapter 1's 85%. Named-entity and body-part-referent detection remained strong (100% each), but precise-term softening, enumeration order, and simile tenor all scored 0% as hard ERRORs this chapter.
3. Zero hard false positives on any of the 5 formal controls, though 1 received a softening note.
4. A real error (2-38) was scored ERROR in one run and softening in another with no change to the underlying text — worth noting as measurement noise when comparing recall figures across chapters too literally.

---

## Companion files

All in `0-INBOX/factcheck-benchmark/`:

- `commentary-fact-check-report-BCAC20_NKW-padmakara-ch2-CLEAN.md` — full clean-audit report
- `commentary-fact-check-report-BCAC20_NKW-padmakara-ch2-test.md` — full detection-benchmark report
- `answer_key_ch2.json` — the answer key and category design for the 20 injected errors
- `padmakara-ch2-baseline-lines.md` / `padmakara-ch2-test.md` — the clean and fault-injected Chapter 2 translation files
