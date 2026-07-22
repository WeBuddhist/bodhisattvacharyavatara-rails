---
name: zeroshot-translator
description: Produce a direct, zero-shot translation of a source text into a target language, guided by an audience profile — no termbase involved at all (no keyword extraction, sense-tagging, or terminology-locking). Use whenever the user asks for a quick or exploratory translation into a specific language using an existing audience profile, as a faster alternative to the full rails pipeline (keyword-equivalence-mapper -> word-sense-grouper -> termbase-builder -> rails-verse-translator). The target language is given by the user in their prompt, not fixed in this skill.
---

# Zero-Shot Translator

Translates a source text directly into a target language named by the user, applying an existing audience profile for register and style. There is no termbase in this path at all — no keyword extraction, no sense-tagging, no locked terminology. This is the fast path — useful for a first draft, a quick comparison, or when full terminology-locking isn't warranted for the task at hand.

## When to use this instead of the rails pipeline

Reach for this when the user wants a translation now and hasn't asked for (or doesn't need) locked, consistent terminology across a long text — e.g. a single chapter, a draft to react to, or a translation where term consistency matters less than speed. If the user is building toward a long, terminology-critical translation, mention that the rails pipeline (`keyword-equivalence-mapper` -> `word-sense-grouper` -> `termbase-builder` -> `rails-verse-translator`) exists as the more rigorous alternative, but don't force it on a request that's just asking for a zero-shot pass.

## Inputs needed

1. **Source text** (or its split chapters — see `split-file-by-markers` if splitting first is useful for a long text).
2. **Target language** — stated by the user in their prompt. This skill doesn't assume or default to any particular language; confirm it if the prompt is ambiguous.
3. **Audience profile** — an existing profile describing the intended readership, register, and translation goals (e.g. `audience_profile/plain.md`). If none exists yet, that needs to be created first rather than guessed at.

## Workflow

1. Read the audience profile closely — tone, register, how much explanatory latitude is allowed, priority order between understanding/accuracy/readability/consistency, etc.
2. Translate the source into the target language, applying the audience profile's guidance directly. Since there's no termbase, use your own best judgment for terminology, staying consistent within the piece even without an external reference locking word choices in advance.
3. **Translate verse by verse, pada-aligned to the source — this is required, not optional, even without a termbase.** Each segment's translation must mirror its source's exact line count, with each target-language line corresponding to its source line's content, not collapsed into flowing prose or mechanically word-wrapped. Preserve every segment ID exactly, in the same position as the source (typically the end of the last line of its segment). Skipping the termbase step doesn't mean skipping structural fidelity — the two are independent; this one always applies whenever the source has a segment/pada structure.
4. If the source is long, it's still reasonable to work through it in natural chunks (e.g. chapter by chapter) with the user rather than producing the entire thing in one uninterrupted pass — apply the same one-unit-per-turn reasoning as `rails-verse-translator` if the text is large enough that a systemic issue would be expensive to discover late.
5. **Translate chapters one at a time, in sequence, never in parallel.** Finish and present one chapter, then wait for the user's go-ahead before starting the next — don't dispatch multiple chapters at once (e.g. via parallel subagents) even though there's no termbase step gating things here. The same reasoning as `rails-verse-translator` applies: a register or structural problem caught after one chapter is cheap to fix; the same problem discovered after several chapters have already been produced in parallel is not, and it also avoids burning a large amount of tokens translating material that hasn't been reviewed yet.

## Where the output goes

1. **Create a subfolder for the target language** if one doesn't already exist, named after the language (e.g. `hindi`, `english`, `chinese`) rather than its short tag.
2. **The required output is the per-chapter split**, in a subfolder named:
   ```
   <text-slug>-<target-language>-<audience-profile-slug>-zeroshot_split_chapters/
   ```
   Example: `AI_translation/hindi/bca-hindi-plain-zeroshot_split_chapters/`

   - `<text-slug>` is a short identifier for the source text (e.g. `bca` for Bodhicaryāvatāra in this project) — infer it from existing filenames/conventions in the project if there is one, or ask if it's genuinely unclear.
   - `<target-language>` is the full language name (e.g. `hindi`, `english`, `chinese`), not a short tag — matching the language subfolder's own name.
   - `<audience-profile-slug>` matches the audience profile's own name (e.g. `plain`).
   - The `-zeroshot` marker distinguishes it from a termbase-guided (rails) translation of the same text/audience/language combination.

   This is the natural output shape since the translation happens chapter by chapter to begin with — no separate merge step is needed to produce it.

3. **A merged single file (same name without `_split_chapters`) is optional**, not a required output of this skill — only produce one if the user actually asks for it.

## Notes

- Because there's no locked termbase, re-running a zero-shot translation (or translating the same text for a different audience profile) can legitimately produce different word choices each time — that's expected, not an inconsistency to chase down.
- If the user later wants to upgrade this into a rails-guided translation, this zero-shot file is a reasonable candidate to build the keyword extraction and glossary from — its terminology choices, even if not locked, reflect real translation decisions worth capturing rather than starting from nothing.
