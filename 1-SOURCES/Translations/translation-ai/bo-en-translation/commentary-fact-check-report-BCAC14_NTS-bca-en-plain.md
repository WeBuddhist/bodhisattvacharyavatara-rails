# BCA Translation — Commentary Fact-Check

- **Commentary (ground truth):** `1-SOURCES/Commentaries/Transcluded/BCAC14_NTS_bo_segmented.md` (Ngulchu Thokme, *Ocean of Good Explanations*)
- **Translation audited:** `1-SOURCES/Translations/translation-ai/bo-en-translation/bca-en-plain.md`

Method: strict term-by-term alignment against the commentary's own glosses
(kāya/entity/number/simile/agent/order sensitive), not a gist check. Preliminary
self-check, not a scholarly sign-off — a domain specialist reviews before this is
treated as final (an LLM never marks its own output complete).

## Progress

| Scope checked |
|---|
| Chapter 1, verses 1-1 to 1-5 |

### Chapter 1 — verses 1-1 to 1-5

| Verse | Verdict | Tibetan (Wylie) | Commentary gloss | English | Fix |
|---|---|---|---|---|---|
| 1-1 | ⚠ ERROR | ཆོས་ཀྱི་སྐུ་མངའ (chos kyi sku mnga') | possessing the **dharmakāya** — a buddha-body; commentary cites *Uttaratantra* on its two aspects | "To the **dharma** they embody" | render as **dharmakāya / truth-body**, not "dharma" (the teaching) |
| 1-1 | ⚠ ERROR | སྡོམ (sdom) | the bodhisattva's **vow / three ethical disciplines** (nyes spyod sdom pa, dge chos sdud, sems can don byed) | "how to enter this **way of life**" | "the bodhisattva's **vows / training**", not the generic "way of life" |
| 1-2 | ✓ | — | (sngon chad ma byung / sdeb sbyor / gzhan don / rang yid bsgom all align) | — | clean |
| 1-3 | ⚠ minor | དགེ་བ་བསྒོམ་ཕྱིར … དད་པའི་ཤུགས (dge ba bsgom phyir … dad pa'i shugs) | *purpose* = cultivating virtue; what increases = the **force of faith** (faith generally) | "strengthen my **faith / In virtue**" | faith isn't *in* virtue; "cultivating virtue, my faith grows" |
| 1-4 | ✓ | — | (dal 'byor / rnyed dka' / phan pa align; line-2 elaboration dropped, acceptable) | — | clean |
| 1-5 | ⚠ minor | རབ་སྣང་སྟོན་པ (rab snang ston pa) | lightning momentarily reveals **forms** (gzugs rab tu snang ba ston pa) | "Lights up **the sky**" | lightning reveals the **forms / landscape**, not "the sky" |

**Result: 2/5 clean, 2 errors (1-1 ×2), 2 softening/minor mismatches (1-3, 1-5).**

Note: verse 1-1's *chos kyi sku* → "dharma" error is exactly the kāya-vs-dharma
class the gist-level pass missed and the term-alignment method is designed to
catch.
