---
name: word-sense-grouper
description: Take a verse/segment-indexed keyword-equivalence file (source_word=target_equivalent pairs per segment ID) and regroup it by source word instead of by segment, clustering the target-language equivalents attested for each word into distinct senses. Use whenever a bilingual keyword file already exists indexed by segment ID and needs to be consolidated into a word-indexed, sense-tagged glossary — the natural next step after keyword-equivalence-mapper. Source and target languages are not fixed to any specific pair; sense tags are written in English regardless of which languages are involved, since they're just short glosses to distinguish meanings, not a mirror of the target language.
---

# Word Sense Grouper

Takes a segment-indexed bilingual keyword file (built by `keyword-equivalence-mapper` or equivalent) and regroups it by source-language word, clustering every target-language equivalent attested for that word into distinct senses.

## Why this step exists

A keyword-equivalence file indexed by segment ID is organized the wrong way for spotting translation consistency: the same source word can appear in dozens of segments, each listing its own local equivalent, with no way to see at a glance what the full range of translations for that word looks like. Regrouping by word surfaces that range directly, and separating it into senses distinguishes genuine polysemy (a word meaning different things in different contexts) from mere stylistic variation (different synonyms for the same meaning).

## Input

A segment-indexed file in the format:
```
[id] source_word1=target_equivalent1, source_word2=target_equivalent2, ...
```
(the output of `keyword-equivalence-mapper`, or anything with the same shape).

## Workflow

1. **Aggregate by source word.** For every distinct source-language word across the whole file, collect every target-language equivalent attested for it, from every segment it appears in.

2. **Cluster into senses.** Group the attested equivalents into distinct meanings. Two equivalents belong to the same sense if they're just synonym choices for the same underlying meaning in that language; they belong to different senses if the source word is genuinely being used to mean different things in different segments. If it's unclear which case you're looking at, err toward checking a couple of the actual segments rather than guessing from the target-language words alone — near-synonyms in the target language can still reflect one sense, and superficially similar target words can still reflect two.

3. **Tag each sense in English**, regardless of what the source and target languages are. The sense tag is a short, plain-English gloss of the meaning (e.g. `all/every`, `conventional truth`, `ablaze all over`) — its job is to let someone scanning the file tell the senses apart at a glance, not to serve as a translation itself.
   - **When the target language is itself English** (or otherwise shares wording with the gloss language), do not just copy the attested equivalent into the tag slot — `tag: value` pairs like `what use: what use` are a translation duplicated, not a gloss, and they defeat the entire purpose of tagging for a multi-sense word. Compose the tag as an actual short description of the meaning (what distinguishes this sense from the word's other senses — part of speech, register, literal vs. figurative, the concept it names), even when that description ends up close in wording to the equivalent itself for a plain, unambiguous, single-sense word. The bar is: would this tag, read on its own, tell someone which meaning is intended? A bare copy of the value never clears that bar for a multi-sense word. Even a word with only one attested sense still gets a tag, so the format stays uniform.

4. **Handle "no direct equivalent" entries carefully, then drop them from the output.** If the source keyword file marks some occurrences as having no equivalent, don't silently ignore them during clustering — check whether *every* occurrence of that word lacks an equivalent versus just some occurrences (in which case it likely belongs as its own sense, or should be folded into a related sense if it's really the same meaning rendered implicitly elsewhere). Once that check is done, the output file itself carries no `untranslated: (no direct equivalent)` senses:
   - If a word's *only* attested sense is "no direct equivalent," omit that word entirely from the output.
   - If a word has other real senses alongside "no direct equivalent" occurrences, drop the "no direct equivalent" clause and keep only the attested senses.
   - Never merge a real target-language equivalent with the literal string "untranslated" or "(no direct equivalent)" inside the same clause — a sense's value must be actual target-language text.

5. **Output format**, one line per source word:
   ```
   source_word: {sense_tag: target_equivalent_a / target_equivalent_b; sense_tag2: target_equivalent_c}
   ```
   - Multiple synonym equivalents for the same sense are separated by ` / `.
   - Multiple senses for the same word are separated by `; `.
   - Order senses roughly by frequency or first appearance — whichever makes the file easier to scan; consistency across entries matters more than the specific rule chosen.

6. **Verify.** Cross-check the set of distinct source words before and after this step against the segment-indexed input. Every source word that appeared anywhere in the input should have exactly one entry in the output; a mismatch usually means an aggregation slip rather than an intentional omission.

7. **Save the result** with a filename that includes the source/target languages (by name, e.g. `tibetan`/`hindi`, not a short tag) and the audience profile of the translation the input was built from (e.g. `<source-language>-word-<target-language>-senses-<audience-profile-slug>.md`). Even though sense-clustering itself doesn't make audience-dependent choices, the input file traces back to a specific audience's translation — carrying that through the filename keeps outputs for different audience profiles from being confused with or silently overwriting each other.

## Notes

- This skill doesn't decide anything about which equivalent is "correct" or "preferred" — it only clusters and labels what's attested. Picking a single canonical term per sense (e.g. for building a locked termbase) is a separate, later step.
- Because clustering senses is a judgment call, when a word's equivalents look ambiguous between one sense and two, it's fine to ask the user how granular they want it rather than guessing — over-splitting produces a bloated, hard-to-use glossary, and under-splitting hides a real distinction the source text is making.
