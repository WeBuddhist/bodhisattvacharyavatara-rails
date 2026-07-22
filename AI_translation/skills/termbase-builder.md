---
name: termbase-builder
description: Take a sense-tagged, word-indexed keyword file (word with one or more senses, each sense listing one or more candidate target-language terms) and an audience/style profile, and produce a locked termbase with exactly one chosen term per sense. Use whenever a sense-tagged glossary already exists and needs to be narrowed down to final terminology for a specific audience — the natural next step after word-sense-grouper, and the step right before using the result as a fixed reference for translation. Not tied to any specific source or target language; works for any language pair as long as the input follows the word: {sense: term_a / term_b; sense2: term_c} format.
---

# Termbase Builder

Selects exactly one canonical target-language term per sense from a sense-tagged, word-indexed keyword file, guided by an audience/style profile, producing a termbase meant to be used as a fixed terminology reference afterward.

## Why this needs an audience profile, not just "pick the best one"

The same sense can have multiple valid target-language terms that differ in register, familiarity, or formality — a general audience and a specialist audience often warrant genuinely different choices for the same underlying meaning. This step isn't about finding an objectively "best" term; it's about finding the term that fits who this text is for. That's why the audience profile is a required input, not an optional nicety.

## Inputs needed

1. **Sense-tagged word file** — the output of `word-sense-grouper` or equivalent, in the format:
   ```
   word: {sense_tag: term_a / term_b; sense_tag2: term_c}
   ```
2. **Audience/style profile** — a description of who the translation is for and what register/tone/goals it should hit (e.g. a Plain English Version with no background in the subject vs. specialists, formal vs. natural language, how much explanatory latitude is allowed). If this doesn't exist yet, it needs to before this step can proceed with any confidence — ask for one rather than guessing at the audience.

## Workflow

1. **Read the audience profile closely** before touching any terms. Note anything that bears directly on word choice: target register, how much unfamiliar terminology the audience can be expected to tolerate, whether clarity or precision is prioritized when they conflict, and any explicit style constraints.

2. **For senses with exactly one candidate term**, keep it as-is — there's no decision to make.

3. **For senses with multiple candidate terms**, choose the single term that best fits the audience profile. This is a real judgment call, not a mechanical pick (e.g. "shortest" or "first listed") — weigh which candidate a reader matching the profile would actually understand and find natural, and which register it fits. If the right choice depends on more context than the sense tag and candidate list provide, it's fine to note the uncertainty rather than silently guessing.

4. **Output format** — same word-indexed structure as the input, but with each sense collapsed to one term, no alternates:
   ```
   word: {sense_tag: chosen_term; sense_tag2: chosen_term2}
   ```

5. **Verify.** The set of words and the set of senses per word should be unchanged from the input — this step narrows candidates down to one, it doesn't add or remove words or senses. A mismatch means something got dropped or merged incorrectly, not an intentional simplification.

6. **Save the result with the audience profile in the filename** (e.g. `<source-language>-<target-language>-termbase-<audience-profile-slug>.md`, using full language names rather than short tags, and using the audience profile's slug as-is rather than padding it with extra words like "-english-version"), not just the language pair. This is the step where audience actually drives the output content, so it matters most here: running this again with a different audience profile against the same sense-tagged input produces a legitimately different termbase, and the filename needs to make that difference visible rather than risk one silently overwriting the other.

7. **Treat the result as locked once approved.** The entire point of a termbase is to stop re-litigating word choice during translation — once the user signs off on it, it should be used as a fixed reference downstream (e.g. by a rails-style verse translation pass), not revised casually mid-translation. If a term genuinely turns out to be wrong for some later context, that's worth surfacing to the user explicitly rather than quietly editing the termbase file.

## Notes

- This skill assumes the sense-tagging (grouping equivalents into distinct meanings) already happened. If the input file still mixes multiple senses under one umbrella or hasn't been deduplicated, that's a problem to fix upstream (see `word-sense-grouper`), not something to patch here.
- Because term selection depends entirely on the audience profile, the same sense-tagged input can legitimately produce different termbases for different audiences — that's expected, not a sign of inconsistency.
