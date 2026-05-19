# Translations — per-track convention

This folder holds language-by-language translation tracks. Each subfolder is one track: one target language, one audience, one register.

See [`../About Transformations.md`](../About%20Transformations.md) for the top-level rules that govern all transformation categories.

---

## Track structure

```
Translations/
└── [track-id]/         # e.g. en-contemporary, bn-scholarly
    ├── requirements.md # style contract (written in target language)
    ├── termbase.md     # vocabulary contract (one rendering per keyword)
    ├── audience.md     # audience profile
    ├── <output>.md     # the generated translation files
    └── qa-report.md    # MQM critique driving the next revision
```

## Starting a new translation track

1. Create the folder `Translations/[lang]-[descriptor]/`.
2. Author `requirements.md` covering: target audience and register, bilingual glossary reference path, preferred renderings for structurally significant terms, style constraints, cultural-adaptation rules, and source-rail dependencies.
3. Scaffold `audience.md` from [`../../4-SYSTEM/Templates/audience.md`](../../4-SYSTEM/Templates/audience.md).
4. Ensure `2-RAILS/Bilingual-Glossaries/[src]-[tgt].md` exists and is `status: complete`.
5. Run `glossary-select` to produce `termbase.md`.
6. Confirm the rails covering the first batch are `status: complete`.
7. Generate the first batch as `draft`; run QA; iterate until `complete`.

## Translation workflow (Phase 1 → 2 → 3)

**Phase 1 — Prescriptive rail preparation**
- Ensure `requirements.md` and `termbase.md` are complete.
- Confirm section and verse rails are `status: complete` for the batch.

**Phase 2 — Batched translation**
- Translate using the `translate-section` skill.
- Each generated file lists its source rails in `context_packages:` frontmatter.

**Phase 3 — MQM quality assurance**
- Run `translation-qa` to produce or extend `qa-report.md`.
- Iterate until no critical or major MQM errors remain.
- Domain specialist sets `status: complete`.
