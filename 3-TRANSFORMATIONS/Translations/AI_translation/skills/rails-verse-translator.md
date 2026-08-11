---
name: rails-verse-translator
description: Translate a long, verse- or segment-structured source text chapter by chapter, using a locked termbase for terminology consistency and an audience profile for register, while preserving the source's exact segment IDs and per-segment line structure. Use whenever a termbase and audience profile already exist and the next step is producing the actual translation — the final step after keyword-equivalence-mapper, word-sense-grouper, and termbase-builder. Not tied to any specific source or target language; works for any language pair as long as the source has segment IDs and a per-segment line/pada structure worth preserving.
---

# Rails Verse Translator

**Governed by [`requirements.md`](3-TRANSFORMATIONS/Translations/AI_translation/skills/requirements.md).** Read it before starting. Pacing, structural invariants, naming, file inventory, merge verification, and done criteria live there — do not restate or diverge from them here.

Produces a segment-aligned, termbase-consistent translation of a structured source text, one chapter at a time, with a review gate between units. This is the step that drives on the rails the termbase lays down.

## Translate fresh — never reuse a prior translation as a shortcut

Every segment must be translated from the source, actively consulting the locked termbase term by term. This holds even when a `zeroshot-translator` output already exists for the same text/audience/language — and even when the termbase was built from that file. Shared vocabulary is not the same as having applied the termbase. See `requirements.md` §2.

If the rails result closely resembles a prior zero-shot pass, that is fine — but only if arrived at by translating, not by copying the prior file and validating structure after the fact.

## Inputs needed before starting

- The source text, split into chapters with segment IDs intact — see `split-file-by-markers` if needed.
- The locked termbase (from `termbase-builder` or equivalent).
- The audience profile (same one used to build the termbase, when applicable).
- Any hard formatting constraints stated separately.

## Workflow

1. Read the full source unit first — note every segment ID and its line count; flag atypical counts.
2. Translate segment by segment from the source, using the locked termbase for terminology. Apply the audience profile's register across the whole unit (see `requirements.md` §1).
3. Follow the structural invariants and one-chapter-per-turn pacing in `requirements.md` §§3–4.
4. Verify the unit against those invariants; fix mismatches before presenting.
5. Present the finished unit and stop. Wait for explicit approval before the next chapter.
6. If a termbase entry genuinely does not fit a specific context, **flag it to the user** — do not quietly deviate.

## Merging into the final document

Once every unit is approved, deliver a **single merged file** (required for this path — unlike zero-shot):

1. Concatenate units in order (front matter/intro, chapters, colophon).
2. Add frontmatter per `requirements.md` §5 (`translation_approach` must state rails; paths must resolve).
3. Re-verify the whole merged document against the full source per `requirements.md` §7.
4. Save under the target-language folder with the rails naming form (no `-zeroshot`):
   ```
   <text-slug>-<target-language>-<audience-profile-slug>.md
   ```
   Example: `AI_translation/hindi/bca-hindi-plain.md`

## Notes

- Wrong line count on a draft segment: condense or expand while still conveying the source line's content — never pad with filler the source does not have.
- Content drifted onto the wrong segment ID: stop and re-derive the mapping from the source before writing further.
