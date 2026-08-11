# commentary-fact-check — Chapter 4, BCAC20_NKW Commentary

**Scope:** Padmakara (2006) English translation, Chapter 4 "Carefulness / Conscientiousness" (verses 4-1 to 4-48)
**Commentary:** `1-SOURCES/Commentaries/Transcluded/BCAC20_NKW_bo_segmented.md` — Khenpo Ngakwang Kunga Wangchuk (Dzongsar Shedra)
**Date:** August 11, 2026

Two `commentary-fact-check` runs, both against BCAC20_NKW:

1. **Clean audit** — the real, unmodified Padmakara translation, checked for actual translation issues.
2. **Detection benchmark** — the same translation with 20 deliberately injected errors, checked to see how many the skill catches.

Both translation files are wording-identical to the real, published Padmakara (2006) translation; only line-wrapping was changed (one verse per line) to match the skill's extraction script. One isolated commentary extraction artifact was found (empty bucket at "4-26," resolved by content-matching per the skill's own instructions) — noted, not a translation defect.

---

## Table 1 — Clean audit (no error injection)

**File audited:** `padmakara-ch4-baseline-lines.md` (= real Padmakara wording, reformatted only)

**Result: 45/48 verses clean with no notes, 3/48 carrying a soft style note, 0 hard ERRORs.**

| Verse | Tibetan (Wylie) | Commentary gloss | English | Note |
|---|---|---|---|---|
| 4-6 | བླ་ན་མེད་པའི་བདེ་བ (bla na med pa'i bde ba) | happiness of unsurpassed/supreme awakening | "the highest bliss" | intensity slightly softened |
| 4-12 | གུས་པས (gus pas) | acting with respect/reverence | "attentively" | precise term (reverence) softened to a different quality |
| 4-17 | སྡིག་པ་འབའ་ཞིག་དགེ་བ་མེད (sdig pa 'ba' zhig dge ba med) | ONLY misdeeds, NO virtue at all (absolute) | "My evils will be many, virtues none" | slight loosening of the absolute ("only/none") |

No hard referent errors were found anywhere in the real, unmodified chapter — no kāya/dharma/mind swaps, no wrong entities, no wrong number/scope, no wrong simile tenor, no agent reversals.

---

## Table 2 — Detection benchmark (20 injected errors)

**File audited:** `padmakara-ch4-test.md` (answer key: `answer_key_ch4.json`)

**Result: 15/20 injected errors caught as hard ERROR → Recall = 75.0%.**

| Verse | Verdict | Tibetan (Wylie) | Commentary gloss | English | Fix |
|---|---|---|---|---|---|
| 4-3 | ⚠ ERROR | དེ་ཡི་སྲས (de yi sras) | the Buddha's bodhisattva heirs, named explicitly (Mañjughoṣa, Maitreya, Avalokiteśvara) | "their śrāvakas" | *sras* = bodhisattva heirs, not śrāvakas |
| 4-4 | ⚠ ERROR | སེམས་ཅན་དེ་དག་ཀུན (sems can de dag kun) | ALL those beings deceived | "many beings will have been betrayed" | *kun* = all, not "many" |
| 4-7 | ⚠ ERROR | ཐམས་ཅད་མཁྱེན་པ་ཁོ་ནས (thams cad mkhyen pa kho nas) | known only by the omniscient Buddha, explicitly excluding others | "only understood by the Bodhisattvas" | should be the Buddha, not the Bodhisattvas |
| 4-13 | ⚠ ERROR | སངས་རྒྱས་གྲངས་མེད (sangs rgyas grangs med) | countless/innumerable Buddhas | "A few Buddhas have already lived and passed away" | *grangs med* = countless, direct reversal |
| 4-16 | ⚠ ERROR | ལུས་ནི་ཐང་གཅིག་བརྙན་པོ (lus ni thang gcig brnan po) | this **body** is like something borrowed | "My mind is like something briefly lent" | *lus* = body, not mind |
| 4-17 | ⚠ ERROR | སྡིག་པ་འབའ་ཞིག་དགེ་བ་མེད (sdig pa 'ba' zhig dge ba med) | only evil, no virtue at all (absolute) | "My evils will be many, virtues few" | absolute "none" softened to relative "few" |
| 4-19 | ⚠ ERROR | བསྐལ་པ་བྱེ་བ་བརྒྱར (bskal pa bye ba brgyar) | a hundred **times ten-million** aeons | "for a hundred ages" | drops the ten-million multiplier |
| 4-20 | ⚠ ERROR | མི་ཉིད (mi nyid) | human birth/humanness specifically | "this state of bliss is difficult to find" | drops the precise referent (human rebirth) |
| 4-25 | ⚠ ERROR | སེམས་གདུང་འགྱུར་བ (sems gdung 'gyur ba) | one's own **mind** will be tormented (contrasted with body burned by fire) | "My body...will also be tormented" | *sems* = mind, not body |
| 4-29 | ⚠ ERROR | དགའ་མགུར་བདག་ལ་གནོད་བྱེད་པ (dga' mgur bdag la gnod byed pa) | the afflictions harm **me** | "at their pleasure I injure them" | agent/patient reversed |
| 4-30 | ⚠ ERROR | ཐམས་ཅད་བདག་ལ་དགྲར་ལངས (thams cad bdag la dgrar langs) | ALL the gods/demigods rise against me | "a few of the gods and demigods...came against me" | *thams cad* = all, not "a few" |
| 4-31 | ⚠ ERROR | དེར་བདག་སྐད་ཅིག་གཅིག་ལ་འདོར (der bdag skad cig gcig la 'dor) | the afflictions cast **me** into the fire | "I fling it in an instant headlong down" | agent/patient reversed |
| 4-33 | ⚠ ERROR | ཉོན་མོངས་རྣམས་ནི་བསྟེན་བྱས་ན (nyon mongs rnams ni bsten byas na) | **I** serve/indulge the afflictions | "should my dark defiled emotions serve me" | agent reversed |
| 4-46 | ⚠ ERROR | བདག་ཡིད་ལས་བསལ (bdag yid las bsal) | removed from **my mind** | "when driven from my body" | *yid* = mind, not body |
| 4-47 | ⚠ ERROR | འདི་ནི་སྒྱུ་འདྲ ('di ni sgyu 'dra) | **the afflictions** are like a magician's illusion | "My body is a simple mirage" | wrong simile tenor — belongs to the afflictions, not the body |

### Softening / style notes (not hard errors)

| Verse | Note |
|---|---|
| 4-6 | "unsurpassed bliss" softened to "great happiness"; "all" wandering beings drops the quantifier |
| 4-8 | agent/patient framing shifted (incidental, not one of the 20 injected verses) |
| 4-9 | "welfare of beings" framing softened — this verse was one of the injected sites (item: "Halts the merit"→"Halts the progress"), but the note addresses different wording, so the injected phrase itself was not identified |
| 4-11 | first ground (Pramuditā) generalized to plural "grounds" — this is one of the 5 formal negative controls |
| 4-12 | "reverence" softened to "attentively" |
| 4-14 | "illness" merged into "pains" — this verse was an injected enumeration-order site, but the note addresses different wording, so the injected reordering itself was not identified |
| 4-26 | two notes on dropped scope/reflexivity (incidental, not an injected or control verse) |
| 4-40 | enumeration order reversed (fishermen/butchers/farmers) — this correctly identifies the injected error, but at softening severity rather than hard ERROR |

**Result: 33/48 clean, 15 errors, 10 softening notes.**

---

## Scoring against the answer key

| Category | Caught (ERROR) / Total | Recall | Notes |
|---|---|---|---|
| kāya / dharma / mind swaps | 3 / 3 | 100% | 4-16, 4-25, 4-46 all caught |
| Precise term softened to vague synonym | 0 / 3 | 0% | 4-6 caught only as softening; 4-9 flagged for an unrelated reason; 4-18 missed entirely |
| Wrong named entity | 2 / 2 | 100% | 4-3, 4-7 both caught |
| Wrong number / scope | 5 / 5 | 100% | 4-4, 4-13, 4-17, 4-19, 4-30 all caught |
| Wrong grammatical agent / role | 3 / 3 | 100% | 4-29, 4-31, 4-33 all caught |
| Wrong enumeration order | 0 / 2 | 0% | 4-40 caught only as softening; 4-14 flagged for an unrelated reason |
| Wrong simile tenor | 2 / 2 | 100% | 4-20, 4-47 both caught |

**Overall recall: 15/20 = 75.0%.**

### False positives / soft flags on negative controls

None of the 5 formal negative-control verses (4-2, 4-11, 4-24, 4-36, 4-45) received a hard ERROR verdict. One control (**4-11**) received a softening note (Pramuditā generalized to plural "grounds") — a defensible style read on real, unmodified wording.

---

## Comparison: before vs. after error injection

| Metric | Before injection (clean) | After injection |
|---|---|---|
| Verses checked | 48 | 48 |
| Hard ERROR rows | 0 | 15 |
| Softening / style notes | 3 | 10 |
| Verses fully clean (no ERROR, no note) | 45 | 33 |

Every hard ERROR in the "after" run traces back to one of the 20 deliberately injected changes. As with prior chapters, several softening notes land on verses that had a real injected error present but describe a different, unrelated wording issue on that same line rather than the injected change itself (4-9, 4-14) — meaning those two injections were effectively invisible to the skill even though the verse got some attention.

---

## Comparison across all chapters run so far (same commentary, same methodology)

| Metric | Ch.1 (36v) | Ch.2 (65v) | Ch.3 (33v) | Ch.4 (48v) |
|---|---|---|---|---|
| Recall (hard ERROR only) | 85.0% | 50.0% | 80.0% | 75.0% |
| Caught only as softening | 0 | 4 | 1 | 2 |
| Missed entirely | 3 | 6 | 3 | 1 |
| Hard false positives on controls | 0/5 | 0/5 | 0/5 | 0/5 |
| Soft flags on controls | 2/5 | 1/5 | 0/5 | 1/5 |

Two patterns are now consistent across all four chapters: **enumeration order** and **precise-term softening** are the weakest categories every time (0% in at least half the chapters each), while **named entity**, **number/scope**, and **kāya/dharma/mind** detection stay strong (mostly 100%) throughout. Zero hard false positives have occurred on any negative control across all four chapters and 90 total control-verse checks.

---

## Conclusions

1. On the real, unmodified translation, Chapter 4 passes almost entirely clean — 0 hard errors, only 3 minor style notes.
2. On the fault-injected file, recall was 75% (15/20) — perfect on kāya/dharma/mind, named entity, number/scope, agent/role, and simile tenor (100% each), but 0% on precise-term softening and enumeration order, continuing the pattern from earlier chapters.
3. Zero hard false positives on any of the 5 negative controls.
4. A recurring failure mode across chapters: when an injected error sits on a verse that also has an unrelated real softening issue, the skill sometimes flags the verse for the pre-existing issue while missing the injected one — worth noting since it means a "flagged" verse doesn't guarantee the actual planted error was the one caught.

---

## Companion files

All in `0-INBOX/factcheck-benchmark/`:

- `commentary-fact-check-report-BCAC20_NKW-padmakara-ch4-CLEAN.md` — full clean-audit report
- `commentary-fact-check-report-BCAC20_NKW-padmakara-ch4-test.md` — full detection-benchmark report
- `answer_key_ch4.json` — the answer key and category design for the 20 injected errors
- `padmakara-ch4-baseline-lines.md` / `padmakara-ch4-test.md` — the clean and fault-injected Chapter 4 translation files
