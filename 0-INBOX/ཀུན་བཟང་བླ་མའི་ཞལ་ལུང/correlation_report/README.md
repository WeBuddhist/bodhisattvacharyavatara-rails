# Correlation Report

This folder contains keyword extraction analysis and correlation reports.

## Files

| File | Description |
|------|-------------|
| `en-keywords-fused-pmi.md` | Combined/fused ranking of YAKE and TF-IDF method |
| `DETAILED_CORRELATION_REPORT.md` | Longer and more detailed report of the final result |
| `SHORTER_CORRELATION_REPORT_SUMMARY.md` | Shorter summary of the detailed report |

## Scripts

| Script | Description |
|--------|-------------|
| `analyze_correlation.py` | Measures how much of the hand-curated `glossary.md` (531 terms) each keyword method recovers. Classifies every glossary term as exact / inside-a-longer-keyword / partial / not-found against YAKE, TF-IDF, and the fused list, then writes the detailed report. |
| `fuse_keywords_pmi.py` | Contains the logic for how YAKE and TF-IDF methods are combined |

## Input Data

- `glossary.md` — hand-curated glossary (531 terms)
- `en-n-gram-keyword.json` — YAKE keyword extraction output
- `en-tfidf.md` — TF-IDF keyword extraction output