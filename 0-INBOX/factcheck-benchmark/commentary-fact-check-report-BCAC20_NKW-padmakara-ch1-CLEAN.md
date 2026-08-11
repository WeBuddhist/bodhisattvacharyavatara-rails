# BCA Translation — Commentary Fact-Check

- **Commentary (ground truth):** `1-SOURCES/Commentaries/Transcluded/BCAC20_NKW_bo_segmented.md` (Khenpo Ngakwang Kunga Wangchuk, BCAC20_NKW)
- **Translation audited:** `padmakara-ch1-baseline-lines.md` (Padmakara Translation Group, 2006 — reformatted one-verse-per-line)

Method: strict term-by-term alignment against the commentary's own glosses
(kāya/entity/number/simile/agent/order sensitive), not a gist check. Preliminary
self-check, not a scholarly sign-off — a domain specialist reviews before this is
treated as final (an LLM never marks its own output complete).

## Progress

| Scope checked |
|---|
| Chapter 1, verses 1-1 to 1-36 (full chapter) |

### Chapter 1 — verses 1–36

**Method note:** Extraction was clean — 36/36 verse buckets on both the commentary side (via `extract_commentary.py`, auto-detected link_base `bo-བློ་ལྡན་ཤེས་རབ།`, 0 empty buckets) and the translation side (via `extract_translation.py`). No cascading-shift artifacts observed. A full term-by-term alignment table was built for every verse against the commentary's own glosses before any verdict was assigned. A dedicated second pass then re-checked every occurrence of *sku* (kāya), every named entity, and every number/scope term across the chapter.

No hard ERROR rows were found — every anchored term the commentary explicitly glosses, names, counts, or illustrates is rendered as the correct referent in the English (all three kāya/body occurrences stay "body," not "dharma" or "mind"; Subāhu and Sudhana are correctly distinguished as two different people; the plantain-tree simile is exact; the vow/discipline gloss for *sdom pa* is exact). Four soft MISMATCH/softening notes were logged for the editor's attention — none renames the referent to something wrong, so none rises to ERROR:

| Verse | Verdict | Tibetan (Wylie) | Commentary gloss | English | Note |
|---|---|---|---|---|---|
| 1-9 | ⚠ softening | བདེ་གཤེགས་རྣམས་ཀྱི་སྲས (bde gshegs **rnams** kyi sras) | "sras" = heirs/children of the **Sugatas** (plural — Buddhas collectively) | "the children of **the Blissful One**" (singular) | Number: plural "Sugatas" collapsed to a singular generic epithet. Common English convention, not a wrong referent — flagged for completeness per the number/scope check. |
| 1-14 | ⚠ softening | བྱམས་མགོན (byams mgon) | Commentary explicitly names the speaker: **Maitreya** ("rje btsun byams pa mgon po," "endowed with wisdom"), addressing Sudhana (nor bzang) | "the **Wise and Loving Lord**" (no proper name given) | Named entity: the commentary explicitly names Maitreya as the speaker of this attribution (a check the skill flags by name). English keeps only the descriptive epithet ("Loving Lord" = a literal gloss of *byams mgon*) and omits "Maitreya." Sudhana, the addressee, is correctly named. Not a wrong name — just an un-named epithet — so logged as softening, not ERROR. |
| 1-21 | ⚠ softening | ཕན་འདོགས་བསམ་པ (phan 'dogs bsam pa) | "a thought/intention of wishing to help or benefit" (not a giving/donation term) | "with **kindly generosity**" | Precise term → near-synonym: the commentary's phrase is about a benevolent *intention*, not the specific virtue of generosity/giving (sbyin pa, dāna). "Generosity" imports a more specific technical sense not in the Tibetan. Mild softening, not a doctrinal-category error. |
| 1-36 | ⚠ softening | སྐྱེས་པ་དེ་ཡི་སྐུ་ལ་ཕྱག་འཚལ (...de yi **sku** la phyag 'tshal) | Commentary specifies the object of the prostration is literally the person's **body** (down to the soles of the feet) | "to **them** I bow" | Kāya-adjacent: *sku* (body) generalized to "them" (the person) rather than rendered explicitly as "body." Not a swap to a wrong category (not "mind," not "dharma") — a mild generalization, logged per the kāya-sensitivity check. |

All other anchored terms across all 36 verses — including the three-jewels breakdown in 1-1 (bde gshegs = Buddha jewel; chos kyi sku = Dharma jewel, kept as "dharmakāya," not reduced to "the dharma"; sras bcas = Sangha jewel); the alchemy/gold simile (1-10, rgyal ba'i sku → "the body of a Buddha," correctly kept as kāya); the plantain-tree simile (1-12, chu shing → "the plantain tree," exact); the two named sūtra-recipients Subāhu (1-20, lag bzangs) and Sudhana (1-14, nor bzang), correctly differentiated; Brahmā and the ṛiṣhis (1-23); the two-fold aspiring/engaged bodhicitta division and its ordering (1-15–1-17); and all number/scope markers checked (countless beings, hundreds, all without exception, etc.) — matched cleanly.

**Result: 32/36 clean with no notes, 4/36 carrying a softening note, 0 errors.**
