# commentary-fact-check — Chapter 3, BCAC20_NKW Commentary

**Scope:** Padmakara (2006) English translation, Chapter 3 "The Full Acceptance of Bodhichitta" (verses 3-1 to 3-33)
**Commentary:** `1-SOURCES/Commentaries/Transcluded/BCAC20_NKW_bo_segmented.md` — Khenpo Ngakwang Kunga Wangchuk (Dzongsar Shedra)
**Date:** August 11, 2026

Two `commentary-fact-check` runs, both against BCAC20_NKW:

1. **Clean audit** — the real, unmodified Padmakara translation, checked for actual translation issues.
2. **Detection benchmark** — the same translation with 20 deliberately injected errors, checked to see how many the skill catches.

Both translation files are wording-identical to the real, published Padmakara (2006) translation; only line-wrapping was changed (one verse per line) to match the skill's extraction script.

A note on this chapter's extraction: the commentary's chapter-3 buckets show a confirmed one-verse cascading shift (a root couplet lands at the tail of one bucket, its explanation at the head of the next) that persists through most of the chapter. Both runs resolved this by content-matching rather than trusting bucket labels, per the skill's own instructions — noted here so the per-verse citations below make sense.

---

## Clean audit — no error injection

**File audited:** `padmakara-ch3-baseline-lines.md` (= real Padmakara wording, reformatted only)

**Result: 31/33 verses clean, 1 hard ERROR, 1 softening note.**

| Verse | Verdict | Tibetan (Wylie) | Commentary gloss | English | Issue |
|---|---|---|---|---|---|
| 3-8 | ⚠ ERROR (order) | sman / sman pa / nad g.yog | fixed order: **medicine → doctor → nurse** | "the doctor, nurse, the medicine itself" | The English reverses the root verse's own word order — a real, pre-existing issue, not injected |
| 3-9 | softening | mu ge'i bskal pa | the **famine**-eon specifically (one of three named degeneration-kalpas) | "the aeons marked by scarcity and want" | Softened from the specific named era to a general description |

No kāya/dharma/mind swaps, wrong entities, or wrong number/scope were found anywhere else in the chapter.

---

## Detection benchmark — 20 injected errors

**File audited:** `padmakara-ch3-test.md` (answer key: `answer_key_ch3.json`)

**Result: 16/20 injected errors caught as hard ERROR → Recall = 80.0%.** 1 further case was logged as a softening note only; 3 were missed with no flag at all.

### Recall by category

| Category | Caught (ERROR) / Total | Recall |
|---|---|---|
| kāya / dharma / mind swaps | 3 / 3 | 100% |
| Precise term softened to vague synonym | 2 / 3 | 66.7% |
| Wrong named entity | 1 / 1 | 100% |
| Wrong number / scope | 5 / 6 | 83.3% |
| Wrong grammatical agent / role | 3 / 3 | 100% |
| Wrong enumeration order | 0 / 2 | 0% |
| Wrong simile tenor | 2 / 2 | 100% |

(Chapter 3's root verses name no specific bodhisattvas or sūtras, so only one named-entity case could be designed this chapter — the vehicle-name swap at 3-23, Bodhisattva precepts → Śrāvaka precepts.)

### Cases missed entirely (no flag at all)

- **3-24** — "in those precepts...train myself" → "in those habits...train myself"
- **3-18** — enumeration reordered: "a boat, a raft, a bridge" → "a bridge, a raft, a boat"
- **3-19** — enumeration reordered: "an isle...a lamp" → "a lamp...an isle"

### Cases caught only as a softening note, not a hard ERROR

- **3-21** — "boundless multitudes" → "many multitudes" (still conveys vastness, so kept below ERROR severity)

### False positives / soft flags on negative controls

None of the 5 formal negative-control verses (3-1, 3-9, 3-15, 3-20, 3-33) received any flag at all — no hard ERROR and no softening note. This is the cleanest control result of the benchmark so far.

### A separate structural finding (unrelated to the injected errors)

The detection run flagged that the English text tagged `^3-33` matches the Tibetan "guest-wanderer" simile, but the chapter's actual closing benediction verse ("Today, before all the Protectors... may gods and asuras rejoice") has no corresponding English verse anywhere in the file. This may reflect a difference in verse-numbering convention between editions (chapter 3 is split into 32, 33, or 34 verses depending on the source) rather than an outright omission — flagged for specialist review, not counted as a term-level error.

---

## Comparison: before vs. after error injection

| Metric | Before injection (clean) | After injection |
|---|---|---|
| Verses checked | 33 | 33 |
| Hard ERROR rows | 1 (a real, pre-existing issue at 3-8) | 16 |
| Verses with a hard ERROR | 1 | 16 |
| Softening / style notes | 1 | 3 |
| Verses fully clean (no ERROR, no note) | 31 | 17 |

As in Chapter 2, the one real pre-existing issue found in the clean run (3-8's reversed medicine/doctor/nurse order) does not reappear at all in the injected run's findings — again suggesting some run-to-run inconsistency in what gets surfaced, independent of the text itself. Every hard ERROR in the "after" run traces back to one of the 20 deliberately injected changes.

---

## Comparison across chapters (same commentary, same methodology)

| Metric | Chapter 1 | Chapter 2 | Chapter 3 |
|---|---|---|---|
| Verses | 36 | 65 | 33 |
| Recall (hard ERROR only) | 85.0% (17/20) | 50.0% (10/20) | 80.0% (16/20) |
| Caught only as softening | 0 | 4 | 1 |
| Missed entirely | 3 | 6 | 3 |
| Hard false positives on controls | 0/5 | 0/5 | 0/5 |
| Soft flags on controls | 2/5 | 1/5 | 0/5 |

Chapter 3's recall (80%) lands close to Chapter 1's (85%) and well above Chapter 2's (50%) — enumeration order is the one consistently weak category here (0% in both Ch.1 and Ch.3's harder cases, though Ch.1 did catch its single enumeration case). This strengthens the earlier hypothesis that detection quality depends on chapter length and how explicitly the commentary spells out word-relationship details, not just on the general skill design.

---

## Conclusions

1. The clean audit surfaced one genuine, real issue in the published translation at 3-8 (medicine/doctor/nurse given in reversed order) — worth flagging to a reviewer, independent of the benchmark.
2. On the fault-injected file, recall was 80% (16/20) — strong across most categories (kāya/dharma/mind, named entity, agent/role, and simile tenor all 100%), with enumeration order again the clear weak point (0%).
3. Zero false positives of any kind — hard or soft — across all 5 negative controls, the cleanest precision result of the three chapters run so far.
4. A separate, real structural question was surfaced (a possible missing closing verse at the end of the chapter) — unrelated to the injected benchmark, worth a specialist's attention.

---

## Companion files

All in `0-INBOX/factcheck-benchmark/`:

- `commentary-fact-check-report-BCAC20_NKW-padmakara-ch3-CLEAN.md` — full clean-audit report
- `commentary-fact-check-report-BCAC20_NKW-padmakara-ch3-test.md` — full detection-benchmark report
- `answer_key_ch3.json` — the answer key and category design for the 20 injected errors
- `padmakara-ch3-baseline-lines.md` / `padmakara-ch3-test.md` — the clean and fault-injected Chapter 3 translation files
