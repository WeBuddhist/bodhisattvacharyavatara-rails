# commentary-fact-check — Chapter 3, BCAC20_NKW Commentary

**Scope:** Padmakara (2006) English translation, Chapter 3 "The Full Acceptance of Bodhichitta" (verses 3-1 to 3-33)
**Commentary:** `1-SOURCES/Commentaries/Transcluded/BCAC20_NKW_bo_segmented.md` — Khenpo Ngakwang Kunga Wangchuk (Dzongsar Shedra)
**Date:** August 11, 2026

Two `commentary-fact-check` runs, both against BCAC20_NKW:

1. **Clean audit** — the real, unmodified Padmakara translation, checked for actual translation issues.
2. **Detection benchmark** — the same translation with 20 deliberately injected errors, checked to see how many the skill catches.

Both translation files are wording-identical to the real, published Padmakara (2006) translation; only line-wrapping was changed (one verse per line) to match the skill's extraction script.

A note on this chapter's extraction: the commentary's chapter-3 buckets show a confirmed one-verse cascading shift (a root couplet lands at the tail of one bucket, its explanation at the head of the next) that persists through most of the chapter. Both runs resolved this by content-matching rather than trusting bucket labels, per the skill's own instructions.

---

## Table 1 — Clean audit (no error injection)

**File audited:** `padmakara-ch3-baseline-lines.md` (= real Padmakara wording, reformatted only)

**Result: 31/33 verses clean, 1 hard ERROR, 1 softening note.**

| Verse | Verdict | Tibetan (Wylie) | Commentary gloss | English | Issue |
|---|---|---|---|---|---|
| 3-8 | ⚠ ERROR (order) | sman / sman pa / nad g.yog | fixed order: **medicine → doctor → nurse** | "the doctor, nurse, the medicine itself" | The English reverses the root verse's own word order — a real, pre-existing issue, not injected |
| 3-9 | softening | mu ge'i bskal pa | the **famine**-eon specifically (one of three named degeneration-kalpas) | "the aeons marked by scarcity and want" | Softened from the specific named era to a general description |

No kāya/dharma/mind swaps, wrong entities, or wrong number/scope were found anywhere else in the chapter.

---

## Table 2 — Detection benchmark (20 injected errors)

**File audited:** `padmakara-ch3-test.md` (answer key: `answer_key_ch3.json`)

**Result: 16/20 injected errors caught as hard ERROR → Recall = 80.0%.**

| Verse | Verdict | Tibetan (Wylie) | Commentary gloss | English | Fix |
|---|---|---|---|---|---|
| 3-2 | ⚠ ERROR | བྱང་ཆུབ (byang chub) | the cause of attaining śrāvaka/pratyekabuddha **enlightenment/liberation** | "cause of gaining a better rebirth" | byang chub = enlightenment, not rebirth |
| 3-3 | ⚠ ERROR | བྱང་ཆུབ (byang chub, three kāyas) | enlightenment endowed with the **three kāyas**, wisdom, qualities | "wisdom-mind of the protectors" | drops the kāya dimension; enlightenment ≠ "mind" |
| 3-4 | ⚠ ERROR | སེམས་ཅན་ཐམས་ཅད (sems can thams cad) | **ALL** beings (doubly emphasized) | "seeks to place some beings in the state of bliss" | thams cad = all, not some |
| 3-6 | ⚠ ERROR | བསྐལ་པ་གྲངས་མེད (bskal pa grangs med) | **countless**, many eons | "stay among us for a hundred ages" | grangs med = countless, not a specific number |
| 3-7 | ⚠ ERROR | སེམས་ཅན་ཐམས་ཅད (sems can thams cad) | **ALL** beings' suffering | "may all the pain of many a living being" | thams cad = all, not many |
| 3-10 | ⚠ ERROR | མི་ཟད་གཏེར (mi zad gter) | **inexhaustible** treasure | "a treasure sometimes plentiful" | mi zad = inexhaustible, not intermittent — near-inversion |
| 3-13 | ⚠ ERROR | ལུས (lus) | **body**, given for others' use | "This mind I have now resigned..." | lus = body, not mind (body/mind swap) |
| 3-16 | ⚠ ERROR | དེ་དག་གི་དོན་ཀུན (de dag gi don kun) | **their** (the other beings') aims fulfilled | "cause whereby my good and wishes are fulfilled" | wrong agent — beneficiary is the other being, not "me" |
| 3-17 | ⚠ ERROR | ཐམས་ཅད་བྱང་ཆུབ་སྐལ་ལྡན་གྱུར | may **they** (wrongdoers) attain enlightenment | "may I attain the fortune of enlightenment!" | wrong agent/subject |
| 3-22 | ⚠ ERROR | ནམ་མཁའི་མཐས་གཏུགས་པའི | beings pervading the **entirety of space**, unbounded | "as far as the eye can see" | cosmic/unbounded scope reduced to a finite visual horizon |
| 3-23 | ⚠ ERROR | བྱང་ཆུབ་སེམས་དཔའི་བསླབ་པ | the **bodhisattva's** training | "in the precepts of the Śrāvakas" | bodhisattva ≠ śrāvaka; wrong vehicle |
| 3-28 | ⚠ ERROR | ཕྱག་དར་ཕུང་པོ | a heap of **filth/rubbish** | "a precious gem inside a heap of gold" | inverts the simile (worthless-vs-precious contrast destroyed) |
| 3-29 | ⚠ ERROR | འཇོམས་བྱེད་པའི | nectar that **destroys/conquers** the Lord of Death | "that is slain by the Lord of Death" | agent/action reversed — nectar defeats Death, not vice versa |
| 3-30 | ⚠ ERROR | རབ་ཞི / ཐམས་ཅད | completely pacifies **all** 84,000 afflictions | "perfectly allays most maladies" | thams cad = all, not most |
| 3-31 | ⚠ ERROR | སེམས་ཀྱི་ཟླ་བ | moon rising from the **mind** (triple-confirmed) | "the rising moon of the enlightened body" | mind→body(kāya) swap |
| 3-32 | ⚠ ERROR | དམ་ཆོས་འོ་མ | milk of the holy **Dharma** (Buddha's teachings) | "churned from the milk of the wish-granting cow" | replaces Dharma with an unrelated cow-image |

### Softening notes (not hard errors)

- **3-11** — "dus gsum" (three times) rendered as "gained and to be gained"; "all beings" compressed without "all"
- **3-21** — "countless and immeasurable" softened to "many multitudes" — still conveys vastness, borderline

**Result: 17/33 clean, 16 errors, 3 softening notes, plus 1 structural finding (see below) flagged for specialist review.**

### Cases missed entirely (no flag at all)

- **3-24** — "in those precepts...train myself" → "in those habits...train myself"
- **3-18** — enumeration reordered: "a boat, a raft, a bridge" → "a bridge, a raft, a boat"
- **3-19** — enumeration reordered: "an isle...a lamp" → "a lamp...an isle"

### A separate structural finding (unrelated to the injected errors)

The detection run flagged that the English text tagged `^3-33` matches the Tibetan "guest-wanderer" simile, but the chapter's actual closing benediction verse ("Today, before all the Protectors... may gods and asuras rejoice") has no corresponding English verse anywhere in the file. This may reflect a difference in verse-numbering convention between editions rather than an outright omission — flagged for specialist review, not counted as a term-level error.

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

(Chapter 3's root verses name no specific bodhisattvas or sūtras, so only one named-entity case could be designed this chapter — the vehicle-name swap at 3-23.)

### False positives / soft flags on negative controls

None of the 5 formal negative-control verses (3-1, 3-9, 3-15, 3-20, 3-33) received any flag at all — no hard ERROR and no softening note. The cleanest control result of the benchmark so far.

---

## Comparison: before vs. after error injection

| Metric | Before injection (clean) | After injection |
|---|---|---|
| Verses checked | 33 | 33 |
| Hard ERROR rows | 1 (a real, pre-existing issue at 3-8) | 16 |
| Verses with a hard ERROR | 1 | 16 |
| Softening / style notes | 1 | 3 |
| Verses fully clean (no ERROR, no note) | 31 | 17 |

As in Chapter 2, the one real pre-existing issue found in the clean run (3-8's reversed medicine/doctor/nurse order) does not reappear at all in the injected run's findings — again suggesting some run-to-run inconsistency in what gets surfaced, independent of the text itself.

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

Chapter 3's recall (80%) lands close to Chapter 1's (85%) and well above Chapter 2's (50%) — enumeration order is the one consistently weak category here.

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
