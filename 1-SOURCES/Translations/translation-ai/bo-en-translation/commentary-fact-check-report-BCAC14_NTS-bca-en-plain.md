# BCA Translation — Commentary Fact-Check

- **Commentary (ground truth):** `1-SOURCES/Commentaries/Transcluded/BCAC14_NTS_bo_segmented.md` (Ngulchu Thokme, *Ocean of Good Explanations*)
- **Translation audited:** `1-SOURCES/Translations/translation-ai/bo-en-translation/bca-en-plain.md`

Method: strict term-by-term alignment against the commentary's own glosses
(kāya/entity/number/simile/agent/order sensitive), not a gist check. Preliminary
self-check, not a scholarly sign-off — a domain specialist reviews before this is
treated as final (an LLM never marks its own output complete).

> **Status (2026-07-06): all errors and softening notes below have been applied to
> `bca-en-plain.md`.** Rows are retained as a record of what was changed. Chapter 1
> was subsequently reworded for non-native-reader readability (meaning unchanged),
> so the "English" quotes below reflect the pre-readability wording.

## Progress

| Scope checked |
|---|
| Chapter 1 — complete (verses 1-1 to 1-36) |

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

### Chapter 1 — verses 1-6 to 1-36

Errors (wrong referent) and notable softening notes. Verses not listed
(1-6 through 1-19 except 1-19 note, 1-22 to 1-29, 1-31, 1-32, 1-34, 1-35, 1-36)
aligned clean against the commentary.

| Verse | Verdict | Tibetan (Wylie) | Commentary gloss | English | Fix |
|---|---|---|---|---|---|
| 1-20 | ⚠ ERROR | དམན་མོས (dman mos) | beings inclined to the **lesser vehicle** (theg dman la mos pa), to be led into the Mahāyāna | "those / who aim **a little lower on the path**" | "those inclined to the **lesser vehicle**", not an effort level |
| 1-21 | ⚠ ERROR | སེམས་ཅན་རྣམས་ཀྱི་ཀླད་ནད (sems can rnams kyi klad nad) | the headache of **beings** (pl.); commentary narrows to **a few** beings (nyung zad rnams) | "just **one** being's headache" | "**a few beings'** headaches" — number error |
| 1-30 | ⚠ ERROR | དགེ་མཚུངས (dge mtshungs) | what **virtue / goodness** (dge ba) equals it? — one of three parallel Qs: virtue / friend / merit | "such boundless **kindness**" | **goodness/virtue**, not "kindness"; also restore order virtue→friend→merit |
| 1-6 | note | རྫོགས་པའི་བྱང་ཆུབ་སེམས (rdzogs pa'i…) | **perfect/complete** bodhichitta (endowed w/ wisdom & compassion) | "the power of bodhichitta" | "perfect/complete" dropped (softening) |
| 1-7 | note | བདེ་མཆོག (bde mchog) | supreme bliss = **unsurpassed enlightenment / buddhahood** | "the highest happiness" | softened to generic happiness |
| 1-19 | note | བག་མེད (bag med) | **heedless / careless** (incl. intoxicated) | "loses their focus" | weak rendering of heedlessness |
| 1-26 | note | དགའ་བའི་རྒྱུ … བསོད་ནམས (dga' ba'i rgyu … bsod nams) | **cause** of joy; **merit** of the precious mind | "the very **seed**" / "how **good** it is" | cause→seed, merit→"good" (softening) |
| 1-29 | note | (agent) | subject of "satisfies/cuts/dispels" is **bodhichitta** itself | "Imagine **one who** takes those beings…" | agent reframed as a person; resolved by 1-30 "friend" |
| 1-33 | note | བདེ་བར་གཤེགས་ཀྱི་བདེ་བ་བླ་ན་མེད | the **unsurpassed bliss of the sugatas** (buddhahood) | "the highest happiness that there is" | loses that it is buddha-bliss specifically |

**Result (1-6 to 1-36): 28/31 clean, 3 errors (1-20, 1-21, 1-30), 6 softening notes.**

## Chapter 1 summary

**Full chapter: 5 errors, 33/36 verses clean of hard errors.**

Errors to fix: **1-1** (×2: *chos kyi sku* → "dharma"; *sdom* → "way of life"),
**1-20** (*dman mos* → "aim a little lower"), **1-21** ("just one" → beings/a few),
**1-30** (*dge ba* → "kindness"). Remainder are optional softening refinements.
