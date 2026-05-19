# Adaptations — per-track convention

This folder holds audience-targeted retellings of the source text — domain shifts rather than language shifts. An adaptation may target children, scholars, sermon audiences, meditation practitioners, or any other reader who needs the text reframed rather than simply translated.

See [`../About Transformations.md`](../About%20Transformations.md) for the top-level rules that govern all transformation categories.

---

## Track structure

```
Adaptations/
└── [track-id]/         # e.g. childrens-en, scholarly-summary-en
    ├── requirements.md # adaptation brief (audience, structure, what to keep/omit)
    ├── termbase.md     # (optional) locked renderings
    ├── audience.md     # audience profile
    └── <output>.md     # the generated files
```

## Starting a new adaptation track

1. Create the folder `Adaptations/[descriptor]-[lang]/`.
2. Author `requirements.md` covering: audience, structural shape of the output, what to keep / dissolve / footnote / omit, source-rail dependencies.
3. Scaffold `audience.md` from [`../../4-SYSTEM/Templates/audience.md`](../../4-SYSTEM/Templates/audience.md).
4. Add `termbase.md` only if the adaptation locks specific renderings; many adaptations work directly from the rails without one.
5. Confirm the relevant `2-RAILS/` packages are `status: complete` before generating.
