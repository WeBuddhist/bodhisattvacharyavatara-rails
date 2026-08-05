# Glossary Coverage Across Three Keyword-Extraction Methods

**Question:** how many of the English terms in `glossary.md` are surfaced by YAKE, by TF-IDF, and by the combined (fused) method &mdash; exactly, and partially?

**Corpus:** 531 glossary terms (229 single-word, 302 multi-word) checked against three rankings over the same English text.

> This report replaces an earlier version of `CORRELATION_REPORT.md` whose numbers were invalid. That version reported TF-IDF at 0.2% coverage and zero terms shared between the three methods; both were parser artifacts. See *Corrections* at the end.

---

## 1. Headline results

| Method | Terms ranked | Exact | Partial | **Total found** | **Coverage** |
|---|---:|---:|---:|---:|---:|
| YAKE | 3,376 | 181 | 233 | **414** | **78.0%** |
| TF-IDF (pure unigram) | 7,632 | 197 | 288 | **485** | **91.3%** |
| TF-IDF (file as published) | 9,190 | 254 | 231 | **485** | **91.3%** |
| Fused / Combined | 7,978 | 238 | 247 | **485** | **91.3%** |

Read this table with the next one before drawing conclusions: most of the *partial* column is the loose reverse-containment tier, which is far weaker evidence than an exact match. On **exact matches alone**, coverage runs 34.1%&ndash;47.8%.

## 2. The same numbers split by match tier

| Method | Exact | Partial &mdash; forward | Partial &mdash; reverse | None |
|---|---:|---:|---:|---:|
| YAKE | 181 | 14 | 219 | 117 |
| TF-IDF (pure unigram) | 197 | 0 | 288 | 46 |
| TF-IDF (file as published) | 254 | 1 | 230 | 46 |
| Fused / Combined | 238 | 0 | 247 | 46 |

**Tier definitions**

| Tier | Rule | Example |
|---|---|---|
| **Exact** | the two normalized token sequences are identical | glossary `Bodhicitta` = ranked `bodhicitta` |
| **Partial &mdash; forward** | the glossary term appears as a whole-token run *inside a longer ranked term* | glossary `Amitayus` inside ranked `buddha protector amitayus` |
| **Partial &mdash; reverse** | a ranked term appears as a whole-token run *inside a longer glossary term* | ranked `space` for glossary `Absolute space` |
| **None** | neither direction matches | glossary `Chenrezi` |

Forward partial is the stricter, more useful reading: the glossary concept is genuinely present in the ranking, just carrying extra context. Reverse partial only tells you that one component word of a compound glossary entry showed up somewhere, which is much weaker &mdash; `space` is not evidence that the ranking captured *Absolute space*.

Why forward partial is near zero for two methods: TF-IDF proper ranks **single words only**, and a single word cannot contain a multi-word phrase. The fused list keeps only 310 multi-word phrases after NPMI gating, so it has almost no longer terms to absorb a glossary entry either. YAKE is the only method whose n-grams produce meaningful forward partials.

Worked forward-partial examples from YAKE:

- glossary **Amitayus** &rarr; ranked `buddha protector amitayus`
- glossary **Amoghasiddhi** &rarr; ranked `buddha amoghasiddhi`
- glossary **Aryadeva** &rarr; ranked `master aryadeva`
- glossary **Beginning** &rarr; ranked `prayer beginning`
- glossary **Clinging** &rarr; ranked `ego clinging`
- glossary **Drikung Kyobpa** &rarr; ranked `drikung kyobpa rinpoche`
- glossary **Equality** &rarr; ranked `great equality`
- glossary **Infinite Aspiration** &rarr; ranked `buddha infinite aspiration`

## 3. How terms were compared

Both sides pass through the same pipeline before comparison:

1. strip markdown bold, lowercase;
2. drop parentheticals &mdash; `Bliss (experience)` &rarr; `bliss`;
3. strip punctuation, hyphens become spaces;
4. light singularization &mdash; `teachings` &rarr; `teaching`;
5. compare as **token sequences**, never as raw substrings.

Step 5 matters. A raw substring test makes `bell` match `rebellion` and lets any single-letter parsing artifact match every term in the glossary; that is exactly how the previous report reached its numbers.

## 4. Overlap between the three methods

Comparing the three genuine methods (TF-IDF here is the pure unigram list &mdash; see &sect;6).

| Reached by | Exact match only | Any tier |
|---|---:|---:|
| All three methods | 124 | 414 |
| At least one method | 254 | 485 |
| No method | 277 | 46 |

| Unique contribution | Exact match only | Any tier |
|---|---:|---:|
| Only YAKE finds it | 16 | 0 |
| Only TF-IDF finds it | 0 | 0 |
| Only Fused finds it | 0 | 0 |

The 16 terms **only YAKE** matches exactly are all multi-word phrases that a unigram ranking structurally cannot represent:

> `Bodhisattva Abbot`, `Feast offering`, `Gyalse Rinpoche`, `Joyous Realm`, `Khampa Lungpa`, `Lingje Repa`, `Melong Dorje`, `Omniscient Dharma-King`, `Precious word empowerment`, `Secret empowerment`, `Shang Rinpoche`, `Tangtong Gyalpo`, `Vajra recitation`, `Vajra song`, `Water torma`, `Wisdom empowerment`

TF-IDF and the fused list contribute nothing that the other two miss. Their vocabularies are supersets built from the same unigram pool, so they add depth, not new concepts.

## 5. Where glossary terms land in each ranking

Coverage says whether a term appears anywhere in a list of several thousand. This says whether a method puts glossary terms *near the top*, which is what matters if the ranking is used to propose glossary candidates.

Each cell: glossary terms found in the top-k, and what share of that top-k they represent.

| Method | top 100 | top 250 | top 500 | top 1,000 | top 2,000 |
|---|---:|---:|---:|---:|---:|
| YAKE | 18 (18.0%) | 44 (17.6%) | 75 (15.0%) | 109 (10.9%) | 154 (7.7%) |
| TF-IDF (pure unigram) | 17 (17.0%) | 37 (14.8%) | 54 (10.8%) | 86 (8.6%) | 120 (6.0%) |
| Fused / Combined | 17 (17.0%) | 47 (18.8%) | 75 (15.0%) | 111 (11.1%) | 164 (8.2%) |

The three are close at the very top. Past the first few hundred terms the fused ranking keeps the highest concentration of glossary terms, which is the behaviour the RRF fusion was designed to produce &mdash; it is a better *ranking*, even though its raw coverage is similar to TF-IDF's.

## 6. A caveat about `en-tfidf.md`

The "Full Ranked Table" in `en-tfidf.md` holds **9,190** rows, but only **7,632** are TF-IDF results. The remaining **1,558** rows are multi-word **YAKE phrases appended to the same table** (the file marks them with `-` in the Count, TF-IDF, IDF and Band columns).

So the file is a merged artifact, not a TF-IDF ranking. Treating it as one credits TF-IDF with YAKE's phrase extraction &mdash; worth 57 extra exact matches. Both readings are reported above; the pure unigram list is the one used in the method comparison.

Similarly, `en-keywords-fused-pmi.md` contains a second table under `## Gated out` listing phrases the NPMI gate **rejected**. Those are not results and are excluded.

## 7. Cross-check against the files' own annotations

Both markdown files already carry a `Glossary` column marking rows as `✓` (exact), `~` (partial) or `—` (none), produced independently of this analysis.

| File | Its own `✓` count | Exact matches computed here | Difference |
|---|---:|---:|---:|
| `en-tfidf.md` | 229 | 254 | +25 |
| `en-keywords-fused-pmi.md` | 215 | 238 | +23 |

The counts agree closely and this analysis finds slightly more, because normalization here also folds plurals and parentheticals. The agreement is a useful independent confirmation that the exact-match layer is sound.

## 8. Transliteration is hiding real matches

21 glossary terms score as "not found" purely because the glossary and the source text romanise Sanskrit differently &mdash; the glossary writes `sh`, the text writes `s`:

| Glossary spelling | Spelling in the rankings |
|---|---|
| Akanishtha | `akanistha` |
| Atisha | `atisa` |
| Avalokiteshvara | `avalokitesvara` |
| Darshaka | `darsaka` |
| Kashyapa | `kasyapa` |
| Mahakashyapa | `mahakasyapa` |
| Manjushri | `manjusri` |
| Manjushrimitra | `manjusrimitra` |
| Pratimoksha | `pratimoksa` |
| Purnakashyapa | `purnakasyapa` |
| Rakshasa | `raksasa` |
| Rishi | `risi` |
| Shakyamuni | `sakyamuni` |
| Shantideva | `santideva` |
| Shariputra | `sariputra` |
| Shastra | `sastra` |
| Shravaka | `sravakas` |
| Shrona | `srona` |
| Vaishakha | `vaisakha` |
| Vaishravana | `vaisravana` |
| Vikramashila | `vikramasila` |

These are the *same terms*, so the exact-match figures in &sect;1 are conservative by roughly 21 terms. Normalising transliteration on ingest would be the single highest-value fix to the extraction pipeline.

## 9. Terms no method finds

46 glossary terms are absent from all three rankings under any tier (277 under exact match alone).

**Spelling variants (21)** &mdash; present in the text, missed by string matching (see &sect;8):

> `Akanishtha`, `Atisha`, `Avalokiteshvara`, `Darshaka`, `Kashyapa`, `Mahakashyapa`, `Manjushri`, `Manjushrimitra`, `Pratimoksha`, `Purnakashyapa`, `Rakshasa`, `Rishi`, `Shakyamuni`, `Shantideva`, `Shariputra`, `Shastra`, `Shravaka`, `Shrona`, `Vaishakha`, `Vaishravana`, `Vikramashila`

**Not matched by any spelling rule (25)** &mdash; mostly proper nouns that fall below the minimum-count thresholds, or that belong to material the glossary covers but this text does not:

> `Akshobhya`, `Chamaradvipa`, `Chenrezi`, `Dharmata`, `Dipamkara`, `Egolessness`, `Garuda`, `Gelugpa`, `Gyelgong`, `Kapala`, `Krishnacharya`, `Kshatriya`, `Nalanda`, `Sakyapa`, `Samvarasara`, `Sarvanivaranavishkambhin`, `Shankara`, `Shantarakshita`, `Shavaripa`, `Shravakayana`, `Shri Singha`, `Smritijnana`, `Sunakshatra`, `Vipashyin`, `Yaksha`

A few of these are not truly absent, just unreachable by the folding rules used here. `Shri Singha` appears as `sri simha` (a different nasal, *ngh* vs *mh*), and `Shantarakshita` survives only as the truncated token `santarak`. Terms such as `Chenrezi`, `Garuda`, `Nalanda` and `Yaksha` have no near-form anywhere in the three rankings and are genuinely missing from the extracted vocabulary.

## 10. What this means

**The three methods are far more alike than different.** They draw on one shared unigram vocabulary: 124 glossary terms are matched exactly by all three (414 once partial tiers count), and neither TF-IDF nor the fused list finds a single term the others miss. Any claim that one method dramatically outperforms another on this data is an artifact.

**YAKE's value is phrases, not volume.** It ranks the fewest terms (3,376 vs 7,632) and has the lowest raw coverage, but it is the only method contributing unique exact matches (16), all multi-word. For a glossary that is 57% multi-word entries, that capability is not optional.

**The fused method does its job.** Its coverage matches TF-IDF while its ranking places more glossary terms in the top few hundred than either input alone. Fusion improved the ordering, which is what RRF optimises &mdash; it was never going to expand the vocabulary.

**Exact-match coverage is the honest headline: about 47.8% of the glossary, rising to 91.3% only if loose single-word overlap is counted.** The gap between those figures is the real state of things, and the two biggest recoverable losses are transliteration variance (21 terms) and multi-word entries that only n-gram extraction can reach.

## Corrections to the previous report

The prior `CORRELATION_REPORT.md` was generated by a script version with three defects, all fixed in `analyze_correlation.py`:

| Defect | Effect |
|---|---|
| A lazy regex `(.+?)` followed only by optional groups captured **one character** per numbered-list row | Injected single letters (`a`, `s`, `h`, &hellip;) into the term sets |
| Partial matching used bare substring tests in both directions | Every single letter matched every glossary term, so "partial" was ~100% noise |
| The separator row `\| ----- \|` was parsed as a glossary entry | Term count inflated to 532; the true count is 531 |

Corrected headline figures: TF-IDF matches 197 glossary terms exactly (37.1%) and reaches 91.3% once partial tiers count &mdash; not 0.2%. And 124 terms are matched exactly by all three methods (414 under any tier), not 0.

---

Generated by `analyze_correlation.py` from `glossary.md`, `en-n-gram-keyword.json`, `en-tfidf.md` and `en-keywords-fused-pmi.md`. Full matched-term lists: `correlation_analysis_results.txt`.
