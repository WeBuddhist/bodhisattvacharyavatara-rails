# BCA Translation — Commentary Fact-Check

- **Commentary (ground truth):** `1-SOURCES/Commentaries/Transcluded/BCAC20_NKW_bo_segmented.md` (Khenpo Ngakwang Kunga Wangchuk, Dzongsar Shedra)
- **Translation audited:** `padmakara-ch2-baseline-lines.md` (clean baseline — wording identical to the published Padmakara 2006 translation, reformatted to one line per verse; no injected errors)

Method: strict term-by-term alignment against the commentary's own glosses
(kāya/entity/number/simile/agent/order sensitive), not a gist check. Preliminary
self-check, not a scholarly sign-off — a domain specialist reviews before this is
treated as final (an LLM never marks its own output complete).

## Progress

| Scope checked |
|---|
| Chapter 1, verses I-1 and 1-1–1-36 (BCAC20_NKW, see companion ch1 report) |
| Chapter 2, verses 2-1–2-65 (BCAC20_NKW, clean baseline) |

## Chapter 2 — verses 2-1–2-65 (clean audit, real Padmakara wording only)

Every verse's commentary passage was extracted and read; for each anchor the
commentary explicitly glosses, names, counts, or illustrates (Three Jewels
sequence, kāya/sku references in the bathing-and-adornment section 2-10–2-19,
the eight great bodhisattvas named across 2-13/2-22/2-49–2-52, the numeric
scope words *kun/thams cad* throughout the offering and refuge sections, the
dream simile at 2-36, the cause→effect direction at 2-62, etc.) the real
Padmakara English was checked against it term-by-term. A dedicated second
pass then re-scanned specifically for kāya↔dharma↔mind swaps, wrong named
entities, and wrong numbers/scope — none were found beyond what is listed
below.

**Result: 63/65 verses clean with no notes at all, 1/65 carrying a soft
style/scope note, 1/65 carrying a hard ERROR (enumeration order).**

All of the following checked correct in the real translation and are *not*
flagged: the Three Jewels sequence (Buddha/Dharma/Sangha) at 2-1, 2-24, and
2-26; every kāya (*sku*) reference in the bathing/anointing/robing sequence
2-10–2-19 stayed "body/them," never "dharma" or "mind"; all eight named
bodhisattvas (Samantabhadra, Mañjughoṣa, Lokeshvara at 2-13; Mañjughoṣa again
at 2-22; Samantabhadra/Mañjughoṣa at 2-49; Avalokita at 2-50; Ākāshagarbha/
Kṣhitigarbha at 2-51; Vajrapāṇi at 2-52) matched their commentary names
exactly; every *kun/thams cad* ("all/every") scope word checked (2-27 "all
directions," 2-45/2-46 "the four directions," 2-47 "every fear," 2-56 "our
every ill," 2-14's "a thousand million worlds" for *stong gsum*) was rendered
with matching scope; the dream simile at 2-36 stayed a dream; the
cause→effect direction of "evil, only cause of sorrow" at 2-62 was not
reversed; and the vow/vs./natural-fault distinction at 2-63 ("transgressions
of the precepts" for *bcas pa'i sdig pa*) stayed precise.

| Verse | Verdict | Tibetan (Wylie) | Commentary gloss | English | Fix |
|---|---|---|---|---|---|
| 2-38 | ⚠ ERROR | གཏི་མུག་ཆགས་དང་ཞེ་སྡང་ (gti mug chags dang zhe sdang) | the root verse itself states the three poisons in the fixed order ignorance (gti mug) → attachment (chags) → aversion (zhe sdang) | "through hatred, lust, and ignorance" — aversion → attachment → ignorance, an exact mirror-reversal of the root order | reorder to "through ignorance, lust, and hatred" (or equivalent) to preserve the stated sequence |
| 2-24 | ◦ style/softening | ཞིང་རྡུལ་ཀུན་གྱི་གྲངས་སྙེད (zhing rdul kun gyi grangs snyed) | bodies equal in number to ALL the dust-motes of the boundlessly vast buddha-**fields** (*zhing khams rab 'byams*, plural world-systems) | "the grains of dust upon **the earth**" — narrows the cosmological scope (all buddha-fields) to just this one planet | not a renamed referent (still reads as "countless"), so kept as a style note rather than a hard error; could tighten to "the grains of dust in every realm" if a future revision wants to restore the full scope |

No other ERROR or MISMATCH rows were found. In particular, the verses that
also serve as this benchmark's fault-injection sites (2-1, 2-6, 2-8, 2-9,
2-13, 2-14, 2-25, 2-26, 2-28, 2-30, 2-36, 2-45, 2-47, 2-48, 2-50, 2-52, 2-56,
2-62, 2-63) and the five designated negative-control verses (2-3, 2-17,
2-33, 2-43, 2-60) were all confirmed clean here, in the *unmodified* baseline
— confirming those anchors are genuinely sound in the real translation before
any error was deliberately introduced for the separate test file.

**Result: 63/65 clean, 1 error, 1 softening note.**
