# commentary-fact-check — Chapter 1, BCAC20_NKW Commentary

**Scope:** Padmakara (2006) English translation, Chapter 1 (verses 1-1 to 1-36)
**Commentary:** `1-SOURCES/Commentaries/Transcluded/BCAC20_NKW_bo_segmented.md` — Khenpo Ngakwang Kunga Wangchuk (Dzongsar Shedra)
**Date:** August 10, 2026

Two `commentary-fact-check` runs, both against BCAC20_NKW:

1. **Clean audit** — the real, unmodified Padmakara translation, checked for actual translation issues.
2. **Detection benchmark** — the same translation with 20 deliberately injected errors, checked to see how many the skill catches.

Both translation files are wording-identical to the real, published Padmakara (2006) translation; only line-wrapping was changed (one verse per line) to match the skill's extraction script.

---

## Clean audit — no error injection

**File audited:** `padmakara-ch1-baseline-lines.md` (= real Padmakara wording, reformatted only)

**Result: 32/36 verses clean with no notes at all, 4/36 carrying a soft style note, 0 hard ERRORs.**

Every kāya/body occurrence stayed "body" and was never collapsed into "dharma" or "mind"; the two named sūtra-recipients (Subāhu at 1-20, Sudhana at 1-14) were correctly kept distinct; the plantain-tree and alchemy similes were exact; and the vow/discipline gloss for *sdom pa* at 1-1 was exact. In other words: on this chapter, against this commentary, the real Padmakara translation has no referent-level errors of the kind this skill is built to catch.

Four minor style notes were logged (none renames a referent, so none is a hard error):

| Verse | Tibetan (Wylie) | Commentary gloss | English | Note |
|---|---|---|---|---|
| 1-9 | བདེ་གཤེགས་རྣམས་ཀྱི་སྲས (*rnams* = plural) | heirs of the **Sugatas** (plural) | "children of **the Blissful One**" (singular) | Plural collapsed to a singular generic epithet — common English convention |
| 1-14 | བྱམས་མགོན (byams mgon) | explicitly names the speaker as **Maitreya** | "the **Wise and Loving Lord**" (no proper name) | Descriptive epithet used instead of the name; Sudhana (the addressee) is still correctly named |
| 1-21 | ཕན་འདོགས་བསམ་པ (phan 'dogs bsam pa) | a benevolent *intention* to help (not a giving/dāna term) | "with **kindly generosity**" | Imports a more specific "generosity" sense not present in the Tibetan |
| 1-36 | སྐུ་ལ་ཕྱག་འཚལ (...sku la phyag 'tshal) | object of prostration is literally the **body** | "to **them** I bow" | *sku* generalized to "them" rather than named explicitly |

---

## Detection benchmark — 20 injected errors

**File audited:** `padmakara-ch1-test.md` (same fault-injected file used throughout this benchmark; answer key: `answer_key.json`)

**Result: 17/20 injected errors caught → Recall = 85.0%**

### Recall by category

| Category | Caught / Total | Recall |
|---|---|---|
| kāya / dharma / mind swaps | 2 / 2 | 100% |
| Precise term softened to vague synonym | 2 / 3 | 66.7% |
| Wrong named entity | 3 / 3 | 100% |
| Wrong number / scope | 4 / 5 | 80% |
| Wrong simile tenor | 3 / 3 | 100% |
| Wrong grammatical agent / role | 1 / 2 | 50% |
| Wrong enumeration order | 1 / 1 | 100% |
| Other wrong referent (body part) | 1 / 1 | 100% |

### Cases missed

- **1-9** ("in that instant" → "within moments") — the verse got flagged, but for a different, real, pre-existing issue (Sugatas plural → "the Blissful One" singular), so the actual injected phrase was never addressed.
- **1-29** (agent reversal, "those whom bliss fills") — not flagged at all.
- **1-20** ("lesser paths" for *theg pa dman pa*) — logged as a softening note, not a hard ERROR.

### False positives / soft flags on negative controls

None of the 5 formal negative-control verses (1-2, 1-4, 1-17, 1-27, 1-35) — nor any of the 13 other untouched verses — received a hard ERROR verdict. Two controls (1-4, 1-27) did receive softening notes; both are defensible style observations on the real, unmodified wording (the clean audit above did not flag either), not confirmed defects.

---

## Comparison: before vs. after error injection

Same translation, same commentary (BCAC20_NKW), same 36 verses — the only difference between the two runs is whether the 20 errors are present.

| Metric | Before injection (clean) | After injection |
|---|---|---|
| Verses checked | 36 | 36 |
| Hard ERROR rows | 0 | 17 |
| Verses with a hard ERROR | 0 | 15 |
| Softening / style notes | 4 | 4 |
| Verses fully clean (no ERROR, no note) | 32 | 19 |

Every hard ERROR in the "after" run traces back to one of the 20 deliberately injected changes — the skill did not invent new hard errors on text it hadn't seen altered. The 4 softening notes appear in both runs, but not on the same verses: the clean run's softening notes fall on 1-9, 1-14, 1-21, and 1-36 (all genuine, pre-existing characteristics of the real translation); the injected run's softening notes fall on 1-1, 1-4, 1-20, and 1-27 instead — two of which (1-4, 1-27) are verses that were never modified, meaning the skill raised a mild style observation on clean text it hadn't flagged when run on its own. No hard ERROR false positives occurred in either run.

In short: the skill stayed silent on the real, unmodified translation (bar four minor style notes) and produced 17 hard ERROR findings once 20 errors were deliberately introduced — a clear signal that it is doing real detection work, not flagging indiscriminately, though its softening-note behavior shifted somewhat between the two runs.

---

## Conclusions

1. On the real, unmodified translation, Chapter 1 passes clean against BCAC20_NKW — no hard referent errors found, only 4 minor, defensible style notes.
2. On the fault-injected file, BCAC20_NKW as ground truth catches 85% of injected errors (17/20), strongest on referent-level categories (kāya/dharma/mind, named entity, simile tenor — all 100%), weakest on precise-term softening (66.7%) and agent/role reversal (50%).
3. Zero hard false positives across all 18 untouched verses.

---

## Companion files

All in `0-INBOX/factcheck-benchmark/`:

- `commentary-fact-check-report-BCAC20_NKW-padmakara-ch1-CLEAN.md` — full clean-audit report
- `commentary-fact-check-report-BCAC20_NKW-padmakara-ch1-test.md` — full detection-benchmark report
- `answer_key.json` / `scored_results.csv` — the answer key and scored data for the 20 injected errors
- `padmakara-ch1-baseline-lines.md` / `padmakara-ch1-test.md` — the clean and fault-injected translation files used in both runs
- `en-Padmakara_2006-TEST-ch1-errors.md` — the same 20 errors applied directly to a full duplicate of the real, multi-chapter source file (original stanza formatting preserved)
