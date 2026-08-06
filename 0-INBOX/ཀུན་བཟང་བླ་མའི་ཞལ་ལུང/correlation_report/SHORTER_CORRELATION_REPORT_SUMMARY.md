# Glossary Coverage: YAKE vs TF-IDF vs Combined

## Why we are extracting keywords

We use automatic keyword extraction on our English translations of Tibetan Buddhist texts for three main reasons:

- **Terminology standardisation** &mdash; a source term should be rendered consistently across translations, not as several different English words.
- **Wikipedia articles** &mdash; each significant term warrants its own article, which first requires knowing which terms are significant.
- **E-learning courses** &mdash; course material is structured around key concepts, and the keyword list identifies them.

The glossary serves as the benchmark. It is curated by hand, so the share of it each method recovers indicates how far that method can be trusted on terms the glossary does **not** yet cover.

We took the **531 English terms** in `glossary.md` (229 single words, 302 phrases) and measured how many of them each method found.

---

## 1. The answer

| Method | Keywords it produced | Found exactly | Found inside a longer keyword | Only part of it found | **Total found** | **Coverage** |
|---|---:|---:|---:|---:|---:|---:|
| YAKE | 3,376 | 181 | 14 | 219 | **414** | **78.0%** |
| TF-IDF | 7,632 | 197 | 0 | 288 | **485** | **91.3%** |
| Combined | 7,978 | 238 | 0 | 247 | **485** | **91.3%** |

**Read the last column with care.** Those 78&ndash;91% figures lean heavily on the weakest kind of match &mdash; "only part of it found", where a single word like `absolute` is counted as covering the glossary entry *Absolute space*. That is not really finding the term.

If you drop that column and count only the two real kinds of match, coverage is **36.7% for YAKE**, **37.1% for TF-IDF**, **44.8% for Combined**. Those are the honest numbers.

## 2. What counts as a match

| Result | What it means | Example |
|---|---|---|
| **Found exactly** | the keyword is the glossary term | glossary *Bodhicitta* &rarr; keyword `bodhicitta` |
| **Inside a longer keyword** | the whole glossary term sits inside a bigger keyword | glossary *Amitayus* &rarr; keyword `buddha protector amitayus` |
| **Only part of it found** | just one word of a multi-word glossary term turned up | glossary *Absolute space* &rarr; keyword `absolute` |
| **Not found** | nothing matched | glossary *Chenrezi* |

The first two are real hits. The third is weak evidence and is kept in its own column so it never gets mistaken for the others.

This also explains the zeros in the "inside a longer keyword" column above. **TF-IDF ranks single words only**, and a single word cannot contain a two-word glossary phrase. Combined keeps just 310 phrases out of 7,978, so it has almost nothing longer to match against either. YAKE is the only method producing phrases in quantity.

## 3. The three methods mostly agree

| | Exact matches only | Counting every kind of match |
|---|---:|---:|
| Found by all three methods | 124 | 414 |
| Found by at least one | 254 | 485 |
| Found by none | 277 | 46 |

They are not really competing methods &mdash; they draw on the same vocabulary. **TF-IDF and Combined find nothing that the others miss.** Only YAKE contributes anything unique: 16 terms, every one of them a phrase:

> *Bodhisattva Abbot*, *Feast offering*, *Gyalse Rinpoche*, *Joyous Realm*, *Khampa Lungpa*, *Lingje Repa*, *Melong Dorje*, *Omniscient Dharma-King*, *Precious word empowerment*, *Secret empowerment*, *Shang Rinpoche*, *Tangtong Gyalpo*, *Vajra recitation*, *Vajra song*, *Water torma*, *Wisdom empowerment*

That is the practical case for keeping YAKE: **56.9% of the glossary is multi-word**, and a single-word method can never reach those entries.

## 4. Which method puts glossary terms near the top?

Coverage only asks whether a term appears somewhere in a list of thousands. This asks something more useful: if you read the top of each list, how many glossary terms do you get?

| Method | in the top 100 | in the top 500 | in the top 2,000 |
|---|---:|---:|---:|
| YAKE | 18 | 75 | 154 |
| TF-IDF | 17 | 54 | 120 |
| Combined | 17 | 75 | 164 |

All three are similar in the first 100. Deeper down, **Combined stays richest in glossary terms** &mdash; which is exactly what merging the two rankings was supposed to achieve. It did not find *more* terms than TF-IDF, but it orders them better.

## 5. What was missed, and why

46 glossary terms were not found by any method. They split into two very different groups.

**21 are just spelling differences.** The glossary and the source text romanise Sanskrit names differently &mdash; the glossary writes `sh` where the text writes `s`. These terms *are* in the text; the matching simply could not see them:

| Glossary spells it | The text spells it |
|---|---|
| Akanishtha | `akanistha` |
| Atisha | `atisa` |
| Avalokiteshvara | `avalokitesvara` |
| Darshaka | `darsaka` |
| Kashyapa | `kasyapa` |
| Mahakashyapa | `mahakasyapa` |
| &hellip;and 15 more | |

**Fixing this is the single most valuable change to the pipeline** &mdash; it recovers 21 terms for one normalisation rule.

**25 are genuinely absent** from the extracted keywords, such as *Chenrezi*, *Garuda*, *Nalanda* and *Yaksha*. These are mostly rare proper nouns that fall below the minimum-frequency cutoffs, or belong to material the glossary covers but this text does not. (Two near-misses: *Shri Singha* is present as `sri simha`, and *Shantarakshita* only as the cut-off token `santarak`.)

## 6. Bottom line

- **The three methods are far more alike than different.** 124 glossary terms are found exactly by all three, and two of the three add nothing unique.
- **Keep YAKE for phrases.** It produces the fewest keywords and the lowest coverage, but it is the only method that can reach the 57% of the glossary that is multi-word.
- **Combined is the best-ordered list.** Same coverage as TF-IDF, but more glossary terms near the top &mdash; use it if you want a ranked shortlist.
- **Put all three together and they match 47.8% of the glossary exactly &mdash; not 91%.** The difference is weak part-word matches, plus 21 terms lost to spelling alone.

---

*Note: `en-tfidf.md` contains 9,190 rows, but only the 7,632 with an actual TF-IDF score are used here as "TF-IDF" &mdash; the other 1,558 are YAKE phrases stored in the same table.*

*Full detail: `DETAILED_CORRELATION_REPORT.md`. Every matched term, one per line: `correlation_analysis_results.txt`.*
