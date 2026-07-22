---
name: rails-verse-translator
description: Translate a long, verse- or segment-structured source text chapter by chapter, using a locked termbase for terminology consistency and an audience profile for register, while preserving the source's exact segment IDs and per-segment line structure. Use whenever a termbase and audience profile already exist and the next step is producing the actual translation — the final step after keyword-equivalence-mapper, word-sense-grouper, and termbase-builder. Not tied to any specific source or target language; works for any language pair as long as the source has segment IDs and a per-segment line/pada structure worth preserving.
---

# Rails Verse Translator

Produces a segment-aligned, termbase-consistent translation of a structured source text, one chapter (or other natural unit) at a time, with a review gate between units.

## Why "rails," and why one unit at a time

A locked termbase only pays off if the translation actually uses it consistently — this skill is the step that drives on the rails the termbase lays down, rather than re-deciding word choice verse by verse. Working one unit at a time and stopping for review isn't just caution for its own sake: catching a systemic issue (wrong register, a term that doesn't actually fit in context, a structural misunderstanding) after the first chapter costs one chapter's rework. Catching it after the eighth costs eight. If the user hasn't stated this constraint explicitly, propose it anyway for any text of meaningful length.

**Translate one chapter per turn, never in parallel.** Each chapter is its own turn: translate it, verify it, present it, then wait for the user's explicit approval before starting the next. Don't dispatch multiple chapters at once (e.g. via parallel subagents) even if it would be faster — the whole point of this pacing is that a problem caught in chapter 1 can be fixed before it repeats through chapters 2 onward. Translating chapters in parallel defeats that entirely, since by the time a systemic issue is noticed, every chapter already has it.

This also matters for token consumption: a long source text translated in full within a single turn (or fanned out across many parallel subagent turns at once) burns through a large amount of context/tokens in one shot, with no natural checkpoint to stop at if something needs correcting. Pacing it one chapter per turn keeps each turn's token cost bounded and avoids paying for rework across material that hasn't been reviewed yet.

## Translate fresh — never reuse a prior translation as a shortcut

Every segment in this step must be translated from the source text itself, actively consulting the locked termbase term by term as you go. This holds even when a `zeroshot-translator` output (or any other prior translation) already exists for the same text/audience/language combination, and even when that prior output happens to share vocabulary with the termbase — which it often will, since the termbase is frequently built *from* that same prior translation's word choices. Shared vocabulary is not the same thing as having gone through the rails process: copying or lightly adapting a prior translation and then verifying only structural properties (segment IDs, line counts) checks that the shape is right without checking that the translation was actually produced by applying the termbase. If a rails translation ends up closely resembling a prior zeroshot pass, that's a fine and expected outcome of both being good translations of the same source — but it must be arrived at by translating, not by starting from the prior file and validating it after the fact.

## Inputs needed before starting

- The source text, split into chapters (or whatever natural unit makes sense) with segment IDs intact — see `split-file-by-markers` if it still needs splitting.
- The locked termbase (from `termbase-builder` or equivalent).
- The audience/style profile (register, goals, priority order — often the same one used to build the termbase).
- Any hard formatting constraints stated separately (e.g. punctuation conventions, things to avoid).

## The core rule: match the source's line structure, not just its meaning

Each segment in the source has a specific internal line count (e.g. a four-line verse, a two-line couplet). The translation of that segment should mirror that line count, with each target-language line corresponding to its source line's content — not collapsed into flowing prose and not mechanically word-wrapped to hit a number. This requires actually working out what each individual source line says and rendering that specific content on the corresponding target line. Segments with an atypical line count for their chapter (occasional 2-line or 5-line blocks mixed into a mostly-4-line chapter) should be matched to their own actual count, not forced to the chapter's typical pattern.

## Workflow

1. **Read the full source unit first**, noting every segment ID and its exact line count, and flagging any segment whose line count differs from the majority — these need deliberate attention rather than getting mishandled on autopilot.

2. **Translate segment by segment**, using the locked termbase for terminology. Don't introduce new sub-headers, blank structural lines, or reordering — preserve the source's structure exactly aside from the language itself. **Separate consecutive segments with a single blank line (one line-break gap), even if the source uses two or more.** The source's segment IDs and per-segment line counts are what must be preserved exactly; the number of blank lines between blocks is a formatting choice, not part of the segment structure, and should be normalized to one throughout the translation output.

3. **Preserve each segment ID exactly**, attached in the same position as in the source (typically the end of the last line of its segment).

4. **Apply the audience profile's register and any stated style constraints** consistently across the whole unit, not just the first few segments.

5. **Verify before presenting.** Check the translated unit's segment IDs and per-segment line counts against the source unit — same IDs present, same line count per ID, no drift. Also check that segments are separated by exactly one blank line throughout, not the source's spacing. Fix any mismatch before showing it to the user rather than after.

6. **Present the finished, verified unit and stop.** A few sample segments plus confirmation it passed verification is usually enough. Don't start the next unit until the user explicitly approves — even if the pattern seems obvious, a systemic problem is far cheaper to catch after one unit than after several.

## Merging into the final document

Once every unit is translated and approved, the deliverable is a single merged file, not a folder of loose chapter files:

1. **Concatenate the units in order** (front matter/intro, then each chapter, then any colophon/back matter), into one file.
2. **Add a frontmatter block** describing the translation: source file, termbase used, audience, translation approach, segment ID coverage, and any other metadata worth recording for future reference (this is what makes the file self-documenting later, without having to reconstruct how it was produced).
3. **Re-verify the whole merged document against the original source** — same segment IDs present, same line count per segment, checked across the entire text this time rather than per-chapter. This catches anything that could have gone wrong specifically at the seams between units (a dropped blank line, a duplicated or skipped segment at a chapter boundary) that per-chapter verification wouldn't necessarily reveal.
4. Only treat the merge as done once this whole-document check passes cleanly — a per-chapter pass that was clean on its own doesn't guarantee the merged result is.

## Naming the output

Save the merged file in a subfolder for the target language, named using the full language name (e.g. `hindi`, not a short tag like `hi`):
```
<text-slug>-<target-language>-<audience-profile-slug>.md
```
Example: `AI_translation/hindi/bca-hindi-plain.md`

No `-zeroshot` marker here — its absence is what distinguishes a rails (termbase-guided) translation from a `zeroshot-translator` output of the same text/audience/language combination.

## Notes

- If an early draft segment ends up with the wrong line count, condense or expand it — don't leave it mismatched, and don't pad with filler content the source doesn't have. The fix should still convey everything the source line conveys, just fit to the correct number of lines.
- If you notice content has drifted onto the wrong segment ID (e.g. a run of segments shifted by one), stop and re-derive the mapping from the source before writing anything further — this is an easy mistake on long, visually similar sequences and a hard one to catch after the fact.
- The termbase built for this pipeline is meant to be treated as locked during this step — if a term genuinely doesn't fit some specific context, that's worth flagging to the user rather than quietly deviating from it.
