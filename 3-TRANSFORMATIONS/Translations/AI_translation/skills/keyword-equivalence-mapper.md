---
name: keyword-equivalence-mapper
description: Given a pre-extracted, per-verse (or per-segment) list of keywords in a source language, and a translation of the same text into a target language, produce a combined file mapping each source keyword to its equivalent in the target language, verse by verse. Use whenever a keyword list already exists for one language, indexed by segment/verse ID, and needs to be matched against a translation in another language to build a bilingual keyword or termbase reference. Language-agnostic — works for any source/target language pair (Tibetan-Hindi, Pali-English, Sanskrit-Chinese, etc.), not tied to a specific language combination.
---

# Keyword Equivalence Mapper

Takes a keyword list already extracted per segment ID in one language, and a translation of the same text in another language, and produces a combined file where each source-language keyword is paired with its target-language equivalent for that specific verse.

## When to use this

This is the step between "we have keywords per verse in language A" and "we have a bilingual glossary usable for termbase-building or consistency-checking a translation." It assumes the keyword extraction already happened (a separate task) — this skill's job is purely to align those existing keywords against a second-language translation, verse by verse.

## Inputs needed

1. **Source keyword file** — one line per segment ID, listing the keywords already extracted for that segment. Typical format:
   ```
   [id] word1, word2, word3, ...
   ```
2. **Target-language translation** — a translation of the same text, with the same segment IDs. This can be a single file or already split into per-chapter files (see the `split-file-by-markers` skill if it still needs splitting) — either works, as long as each segment ID can be located in it.

## Workflow

1. **Confirm the segment ID convention matches** between the two inputs — the keyword file and the translation must reference the same IDs, or there's nothing to align. Spot-check a handful of IDs across both files before starting the full pass.

2. **Go segment by segment.** For each ID in the source keyword file:
   - Find that same segment in the target-language translation.
   - For each keyword listed for that segment, identify the word or phrase in the target-language verse that carries its meaning.
   - If the target-language translation doesn't have a direct equivalent for a given keyword (common with particles, honorifics, or words rendered implicitly rather than explicitly), mark it `(no direct equivalent)` rather than forcing a stretch match or leaving it blank. This is an honest, useful signal, not a failure — flag it plainly.

3. **This requires real per-verse comparison, not pattern-matching.** A keyword can be translated differently depending on the verse's context, and a target-language equivalent won't always be a single clean word (it may be a short phrase). Work verse by verse rather than trying to build a fixed word-to-word dictionary up front — the same source keyword may legitimately map to different target-language equivalents across different verses.

4. **Work through the text one chapter at a time, and never run chapters in parallel.** Even though this step is a mapping/lookup task rather than fresh translation, it still requires holding each verse's context in mind to pick the right equivalent — doing several chapters at once (whether by batching them together or dispatching them concurrently) degrades the quality of the matches and makes them harder to review, and also drives up token consumption per turn unnecessarily. Finish one chapter's mapping, append it to the output file, then move to the next.

5. **Output format** mirrors the source keyword file's structure, with each keyword expanded to a pair:
   ```
   [id] source_word1=target_equivalent1, source_word2=target_equivalent2, ...
   ```
   Keep the same segment order and the same keywords-per-segment as the input file — this step adds equivalents, it doesn't add or drop keywords.

6. **Save the result** with a descriptive filename indicating both languages involved (by name, e.g. `tibetan`/`hindi`, not a short tag) and the audience profile used for the translation being mapped (e.g. `keywords-by-reference-<source-language>-<target-language>-<audience-profile-slug>.md`), so it's clear at a glance which language pair *and* which audience-specific translation it was built from. This matters even though this step itself doesn't make audience-dependent choices — the target-language translation it's mapped against was produced for a specific audience, and a different audience profile's translation could plausibly attach different equivalents to the same source keywords. Include the audience slug so re-running this for a different audience profile doesn't silently overwrite or get confused with a prior one.

## Notes

- This skill doesn't touch the keyword extraction itself — if no per-segment keyword file exists yet for the source language, that's a prerequisite step, not part of this skill.
- Because the mapping is done verse by verse, the same source keyword can end up with different target-language equivalents in different segments — that's expected and correct, not an inconsistency to "fix." A later step (e.g. `glossary-sense-tagger` / `termbase-builder`, if this project has them) is where those variants get consolidated into a single chosen term per sense, if that's the eventual goal.
