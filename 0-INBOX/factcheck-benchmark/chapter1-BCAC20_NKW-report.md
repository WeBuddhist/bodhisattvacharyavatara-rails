# commentary-fact-check — Chapter 1, BCAC20_NKW Commentary

**Scope:** Padmakara (2006) English translation, Chapter 1 (verses 1-1 to 1-36)
**Commentary:** `1-SOURCES/Commentaries/Transcluded/BCAC20_NKW_bo_segmented.md` — Khenpo Ngakwang Kunga Wangchuk (Dzongsar Shedra)
**Date:** August 10, 2026

Two `commentary-fact-check` runs, both against BCAC20_NKW:

1. **Clean audit** — the real, unmodified Padmakara translation, checked for actual translation issues.
2. **Detection benchmark** — the same translation with 20 deliberately injected errors, checked to see how many the skill catches.

Both translation files are wording-identical to the real, published Padmakara (2006) translation; only line-wrapping was changed (one verse per line) to match the skill's extraction script.

---

## Table 1 — Clean audit (no error injection)

**File audited:** `padmakara-ch1-baseline-lines.md` (= real Padmakara wording, reformatted only)

**Result: 32/36 verses clean with no notes at all, 4/36 carrying a soft style note, 0 hard ERRORs.**

| Verse | Tibetan (Wylie) | Commentary gloss | English | Note |
|---|---|---|---|---|
| 1-9 | བདེ་གཤེགས་རྣམས་ཀྱི་སྲས (*rnams* = plural) | heirs of the **Sugatas** (plural) | "children of **the Blissful One**" (singular) | Plural collapsed to a singular generic epithet — common English convention |
| 1-14 | བྱམས་མགོན (byams mgon) | explicitly names the speaker as **Maitreya** | "the **Wise and Loving Lord**" (no proper name) | Descriptive epithet used instead of the name; Sudhana (the addressee) is still correctly named |
| 1-21 | ཕན་འདོགས་བསམ་པ (phan 'dogs bsam pa) | a benevolent *intention* to help (not a giving/dāna term) | "with **kindly generosity**" | Imports a more specific "generosity" sense not present in the Tibetan |
| 1-36 | སྐུ་ལ་ཕྱག་འཚལ (...sku la phyag 'tshal) | object of prostration is literally the **body** | "to **them** I bow" | *sku* generalized to "them" rather than named explicitly |

Every kāya/body occurrence stayed "body" and was never collapsed into "dharma" or "mind"; the two named sūtra-recipients (Subāhu at 1-20, Sudhana at 1-14) were correctly kept distinct; the plantain-tree and alchemy similes were exact; and the vow/discipline gloss for *sdom pa* at 1-1 was exact. No hard referent errors found anywhere in the real, unmodified chapter.

---

## Table 2 — Detection benchmark (20 injected errors)

**File audited:** `padmakara-ch1-test.md` (answer key: `answer_key.json`)

**Result: 17/20 injected errors caught as hard ERROR → Recall = 85.0%.**

| Verse | Verdict | Tibetan (Wylie) | Commentary gloss | English | Fix |
|---|---|---|---|---|---|
| 1-1 | ⚠ ERROR | ཆོས་ཀྱི་སྐུ (chos kyi sku) | dharmakāya, a buddha-body attribute of the Sugata | "the dharma they embody" | should be "the dharma-body," not "the dharma" as a separate object of homage |
| 1-1 | ⚠ ERROR | སྡོམ (sdom) | vow/discipline of the Bodhisattva heirs | "the practice of the Bodhisattva way of life" | *sdom* = vow/discipline, not "way of life" |
| 1-5 | ⚠ ERROR | དངོས་པོར་གྱུར་པ་རྣམས་སྣང་བར་སྟོན་པ (lightning reveals objects/forms) | lightning reveals **forms**, not the sky itself | "the whole sky is illuminated" | wrong simile tenor — lightning reveals forms, not the sky |
| 1-6 | ⚠ ERROR | དགེ་བ་ཉམ་ཆུང (dge ba nyam chung) | virtue/goodness is weak | "Kindness, thus, is weak" | *dge ba* = virtue/goodness, not "kindness" |
| 1-7 | ⚠ ERROR | ཐུབ་དབང་བཅོམ་ལྡན་འདས་རྣམས (thub dbang, plural) | the mighty Sages / Lords of Sages (plural Buddha epithet) | "the mighty King" | should be plural "Sages," not singular "King" |
| 1-10 | ⚠ ERROR | མི་གཙང་བའི་ལུས (mi gtsang ba'i lus) | this impure physical **body** | "it takes our confused perceptions" | *lus* = body, not "perceptions" |
| 1-11 | ⚠ ERROR | འགྲོ་བའི་དེད་དཔོན་གཅིག་པུ (gcig pu = sole/alone) | the **sole** guide of beings (the Buddha alone) | "the boundless wisdom of the many guides" | *gcig pu* = sole/alone, not "many guides" |
| 1-14 | ⚠ ERROR | བྱམས་མགོན...ནོར་བཟང་ལ་བཤད (Maitreya explained to Sudhana) | Maitreya is the **explainer**, Sudhana (nor bzang) the **recipient** | "the Wise and Loving Lord explained to Maitreya" | Sudhana dropped; Maitreya wrongly made the recipient instead of the explainer |
| 1-19 | ⚠ ERROR | ནམ་མཁའ་དང་མཉམ་པར (nam mkha') | equal to **space/sky** | "equal to the depths of the ocean" | *nam mkha'* = space, not "ocean" |
| 1-20 | ⚠ ERROR | ལག་བཟངས་ཀྱིས་ཞུས་པ (lag bzangs = Subāhu) | sūtra requested by **Subāhu** | "the sūtra Sāriputra requested" | wrong named entity: Subāhu, not Śāriputra |
| 1-20 | ⚠ ERROR | ཐེག་པ་དམན་པ (theg pa dman pa) | the **lesser vehicle** (Hīnayāna) | "those inclined to simpler paths" | should name "lesser vehicle," not vague "simpler paths" |
| 1-21 | ⚠ ERROR | ཀླད་པའི་ནད (klad pa'i nad) | **headache** (deliberately trivial ailment) | "the aching hearts of other beings" | should be "headache," not an emotional-suffering referent |
| 1-22 | ⚠ ERROR | སེམས་ཅན་རེ་རེ (re re = each and every) | suffering of **each of countless** beings | "the endless pain of a few living beings" | scope reversal: countless, not "a few" |
| 1-23 | ⚠ ERROR | ཚངས་པ (tshangs pa) | **Brahmā**, lord of the Sahā world | "even Indra harbor such benevolence" | Brahmā dropped; Indra wrongly used as the climactic figure |
| 1-25 | ⚠ ERROR | སེམས་ཀྱི་རིན་ཆེན་ཁྱད་པར་ཅན (precious jewel of mind) | precious jewel of **mind** (bodhicitta) | "this noble, jewellike form of buddha-body" | mind→kāya swap; should stay "mind" |
| 1-28 | ⚠ ERROR | སྡུག་བསྔལ་ཉིད་ལ་མངོན་པར་རྒྱུག (beings run toward suffering) | beings are the **agent** running toward suffering | "misery itself pursues them" | agent reversed — beings run toward misery, not the other way |
| 1-33 | ⚠ ERROR | སེམས་ཅན་གྲངས་མེད་པ་མཐའ་ཡས (countless, boundless beings) | bodhisattvas give to **countless, boundless** beings | "bestow on a handful of followers" | scope reversal: countless, not "a handful" |
| 1-30 | ⚠ ERROR (order) | དགེ / བཤེས / བསོད་ནམས (virtue / friend / merit) | fixed enumeration order: virtue → friend → merit | "friend...virtue...merit" | enumeration order swapped |

### Cases missed

- **1-9** ("in that instant" → "within moments") — the verse got flagged, but for a different, real, pre-existing issue (Sugatas plural → "the Blissful One" singular), so the actual injected phrase was never addressed.
- **1-29** (agent reversal, "those whom bliss fills") — not flagged at all.

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
