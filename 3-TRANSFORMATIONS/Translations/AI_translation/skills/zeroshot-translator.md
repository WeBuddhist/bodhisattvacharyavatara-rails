---
name: zeroshot-translator
description: Produce a direct, zero-shot translation of a source text into a target language, guided by an audience profile — no termbase involved at all (no keyword extraction, sense-tagging, or terminology-locking). Use whenever the user asks for a quick or exploratory translation into a specific language using an existing audience profile, as a faster alternative to the full rails pipeline (keyword-equivalence-mapper -> word-sense-grouper -> termbase-builder -> rails-verse-translator). The target language is given by the user in their prompt, not fixed in this skill.
---

# Zero-Shot Translator

**Governed by [`requirements.md`](3-TRANSFORMATIONS/Translations/AI_translation/skills/requirements.md).** Read it before starting. Pacing, structural invariants, naming, and done criteria live there — do not restate or diverge from them here.

Translates a source text directly into a target language named by the user, applying an existing audience profile for register and style. There is no termbase in this path — no keyword extraction, no sense-tagging, no locked terminology. This is the fast path for a first draft, a quick comparison, or when full terminology-locking isn't warranted.

## When to use this instead of the rails pipeline

Use when the user wants a translation now and hasn't asked for locked terminology across a long text — e.g. a single chapter, a draft to react to, or speed over consistency. If the user is building toward a terminology-critical translation, mention that the rails pipeline exists (`keyword-equivalence-mapper` → `word-sense-grouper` → `termbase-builder` → `rails-verse-translator`), but don't force it on a plain zero-shot request.

## Inputs needed

1. **Source text** (or its split chapters — see `split-file-by-markers` if splitting first is useful).
2. **Target language** — stated by the user. Confirm if ambiguous; this skill does not default to any language.
3. **Audience profile** — an existing file under `audience_profile/` (e.g. `audience_profile/plain.md`). Create one first if none exists; do not guess register.

## Workflow

1. Read the audience profile closely — it is the register source of truth (see `requirements.md` §1).
2. Translate into the target language from the source, applying that profile. With no termbase, use your own judgment for terminology and stay consistent within the piece.
3. Follow the structural invariants and one-chapter-per-turn pacing in `requirements.md` §§3–4. Skipping the termbase does not relax structure.
4. Verify the unit against those invariants, present it, and wait for explicit approval before the next chapter.

## Where the output goes

1. Create a subfolder for the target language if needed, named with the **full language name** (`hindi`, `english` — see `requirements.md` §6).
2. **Required output** is the per-chapter split folder:
   ```
   <text-slug>-<target-language>-<audience-profile-slug>-zeroshot_split_chapters/
   ```
   Example: `AI_translation/hindi/bca-hindi-plain-zeroshot_split_chapters/`

   The `-zeroshot` marker distinguishes this from a rails translation of the same text/audience/language.

3. A merged single file (same name without `_split_chapters`) is **optional** — only produce one if the user asks.

## Notes

- Re-running can produce different word choices — expected, not drift to chase (see `requirements.md` §2).
- This zero-shot output is a reasonable base for later keyword mapping and a rails pass.
