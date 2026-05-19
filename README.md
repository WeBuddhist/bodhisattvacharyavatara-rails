# bodhisattvacaryavatara-rails

བྱང་ཆུབ་སེམས་དཔའི་སྤྱོད་པ་ལ་འཇུག་པ། · *Bodhisattvacaryāvatāra* · Śāntideva

A collaborative [Obsidian](https://obsidian.md) vault that makes AI-powered work on the *Bodhisattvacaryāvatāra* reliable, traceable, and consistent at scale.

## Why

AI models are powerful but unreliable at scale. Hand a model a classical text and a stack of commentary and ask for a translation, an adaptation, a study guide, or a daily reading, and what comes back looks fluent but is hard to trust:

- **Hallucinations** — fabricated meanings that sound plausible.
- **Inconsistency** — the same technical term rendered three different ways across one document.
- **Style drift** — register shifts as the context window fills.
- **No traceability** — no way to verify whether any specific claim is grounded in the commentary tradition or invented on the spot.
- **Doesn't scale** — every new output rediscovers the same interpretive work from scratch.

These failures aren't because the model is weak. They happen because the model is being asked to be **two different specialists at once** — a source-language domain expert who understands every nuance the commentary tradition has worked out, *and* a target-language stylist who knows how to render that meaning for a specific audience. With no preparation and no division of labour, it tries to do both jobs at generation time, in the same prompt, from raw sources. The drift is structural.

## How

The fix is to separate the two specialists, then let them collaborate.

**`2-RAILS/` is the source-language specialist, made permanent.** A pre-built, citation-grounded knowledge base of the commentary tradition — every sense distinction, every compound analysis, every commentator's reading — compiled once, by an LLM under domain-specialist review, with every claim citing the human source that grounds it.

**Each track in `3-TRANSFORMATIONS/` is a target-language specialist for one audience.** A Translation track is a specialist in writing for a particular language and readership. An Adaptation track is a specialist in writing for a particular format (scholastic, liturgical, popular). A Plan track is a specialist in pacing a study arc along a calendar. Each one is bound by its own `requirements.md` (style contract) and `termbase.md` (vocabulary contract).

Two principles hold the collaboration together:

- **Descriptive rails, prescriptive transformations.** The source specialist *describes* what the tradition attests: every commentator, every translator, every attested rendering. Each target specialist *prescribes* what *their* output does for *their* audience.
- **One-way citation chain.** `1-SOURCES/ → 2-RAILS/ → 3-TRANSFORMATIONS/`. Target specialists cite the source specialist; they never reach past the rails into raw commentary.

This is what makes the methodology scale. The expensive interpretive work happens once, in `2-RAILS/`, and is amortised over every output ever produced from the vault. **Lay the rails once; run many transformations on them.**

For the full reasoning — the specialist-pair and Wikipedia analogies — see [`4-SYSTEM/Guidelines/why-rails.md`](4-SYSTEM/Guidelines/why-rails.md).

## What

The vault is a four-stage pipeline. Each stage has its own folder; each folder's `About <Folder>.md` is the authoritative source on what goes in it and how.

```
1-SOURCES/   →   2-RAILS/   →   3-TRANSFORMATIONS/
human            original-       per-output prescriptive
authoritative    language        rails plus the
material         descriptive     AI-generated output
                 context

                ▲
                │ all driven by
                │
              4-SYSTEM/   skills, templates, methodology
```

- **[`1-SOURCES/`](1-SOURCES/)** — root texts, commentaries, existing translations, audio, references. Read-only ground truth.
- **[`2-RAILS/`](2-RAILS/)** — original-language descriptive context at every level a transformation might need: section summaries, verse packages, per-term wiki articles, bilingual glossaries. Every claim cites `1-SOURCES/`.
- **[`3-TRANSFORMATIONS/`](3-TRANSFORMATIONS/)** — three categories of output (**Translations**, **Adaptations**, **Plans**). Each track is governed by `requirements.md` (style contract) + `termbase.md` (vocabulary contract); the AI-generated output files sit alongside, citing the rails.
- **[`4-SYSTEM/`](4-SYSTEM/)** — skills and workflows for every stage of the pipeline, plus cross-cutting methodology docs and templates.

Vault-specific conventions for the *Bodhisattvacaryāvatāra* (addressing scheme, registered commentary IDs, language tracks) live in [`4-SYSTEM/Guidelines/vault-annex.md`](4-SYSTEM/Guidelines/vault-annex.md).

## Getting started — pick your path

### If you are a human contributor

1. **This README** — Why · How · What (you are here).
2. [`4-SYSTEM/Guidelines/why-rails.md`](4-SYSTEM/Guidelines/why-rails.md) — the specialist-pair and Wikipedia analogies in full.
3. [`4-SYSTEM/Guidelines/0-VAULT-Structure.md`](4-SYSTEM/Guidelines/0-VAULT-Structure.md) — the architecture and the citation chain.
4. [`1-SOURCES/About Sources.md`](1-SOURCES/About%20Sources.md) — rules for collecting, formatting, and linking source material.
5. [`2-RAILS/About Rails.md`](2-RAILS/About%20Rails.md) — the schema for the descriptive rails.
6. [`3-TRANSFORMATIONS/About Transformations.md`](3-TRANSFORMATIONS/About%20Transformations.md) — how transformation tracks are set up and how outputs are produced.
7. [`4-SYSTEM/Guidelines/vault-annex.md`](4-SYSTEM/Guidelines/vault-annex.md) — the conventions specific to this vault.
8. [`4-SYSTEM/Skills/SKILLS-CATALOG.md`](4-SYSTEM/Skills/SKILLS-CATALOG.md) — every workflow skill, grouped by pipeline stage.

### If you are an AI agent

1. [`4-SYSTEM/CLAUDE.md`](4-SYSTEM/CLAUDE.md) — operational instructions: citation chain, write permissions, do-nots, standard operations. Read in full before touching any file.
2. The `About <Folder>.md` for the folder you're working in — [`1-SOURCES/About Sources.md`](1-SOURCES/About%20Sources.md), [`2-RAILS/About Rails.md`](2-RAILS/About%20Rails.md), or [`3-TRANSFORMATIONS/About Transformations.md`](3-TRANSFORMATIONS/About%20Transformations.md). Each is the canonical authority for that folder's rules.
3. [`4-SYSTEM/Guidelines/vault-annex.md`](4-SYSTEM/Guidelines/vault-annex.md) — vault-specific conventions: addressing scheme, registered commentary IDs, language tracks.
4. The relevant `4-SYSTEM/Skills/<skill>/SKILL.md` for the specific task.
