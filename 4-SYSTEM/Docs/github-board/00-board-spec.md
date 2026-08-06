# Text Processing Pipeline — GitHub Project Board Spec

## Concept

One GitHub Project (v2) for the whole pipeline. **Each text is one card** (a parent issue) that moves left-to-right across stage columns as work progresses. All artifact-level work lives in **sub-issues** attached to the text's parent issue, so the board stays readable at a glance while detail is one click away.

```
[Backlog] → [1·Sources: Root Text] → [1·Sources: Translations & Commentaries]
→ [2·Rails: Sections & Verses] → [2·Rails: Claims & Wiki]
→ [3·Transformations] → [Done]
```

## Board layout

- **View 1 — Pipeline (Board layout)**: grouped by `Status`. Cards = text parent issues only (filter: `label:text`). This is the main view.
- **View 2 — Work detail (Table layout)**: all sub-issues, grouped by parent, filterable by `Stage` and `Artifact` labels.
- **View 3 — My work (Board by Assignee)**: optional, for collaborators.

## Status column definitions (when does a card move?)

| Column | Card enters when… | Card leaves when… |
|---|---|---|
| **Backlog** | Text is selected for processing | Sourcing work starts |
| **1 · Sources: Root Text** | Work starts on Sanskrit + Tibetan root text | Proofread Tibetan edition exists with chapter/section + verse IDs, linked verse-level to Sanskrit |
| **1 · Sources: Translations & Commentaries** | Root text edition is stable | All translations + commentaries gathered, ID'd, and linked to root text at verse level |
| **2 · Rails: Sections & Verses** | Sources are linked | TOCs extracted, section summaries done, 1 file per root verse compiled from commentaries |
| **2 · Rails: Claims & Wiki** | Verse files usable | Claim files consolidated, keyword lists built, wiki articles polished |
| **3 · Transformations** | Rails context complete | Planned transformations (translations, plans, videos, e-learning) shipped |
| **Done** | All planned transformations shipped | — |

> Stages overlap in practice (e.g. commentary sourcing while rails work starts). The card sits in the **earliest incomplete stage**; sub-issue states show the real parallel picture.

## Custom fields

| Field | Type | Values / purpose |
|---|---|---|
| `Status` | (built-in) | The 7 columns above |
| `Priority` | Single select | P0 / P1 / P2 |
| `Target` | Date | Target completion for current stage |
| `Languages` | Text | e.g. `sa, bo, en, zh, hi, mr` — coverage of translations |

## Labels

**Type:** `text` (parent card), `artifact` (sub-issue)
**Stage:** `stage:sources`, `stage:rails`, `stage:transformations`
**Artifact:** `root-text`, `translations`, `commentaries`, `sections`, `verses`, `claims`, `local-wiki`, `plans`, `translation-out`, `video`, `elearning`
**Other:** `blocked`, `needs-review`, `tooling` (for pipeline/script work not tied to one text)

## Issue hierarchy

```
#N  [TEXT] Byang chub sems dpa'i spyod pa la 'jug pa (Bodhicharyavatara)   ← card on board
 ├─ sub-issue  S1  Sanskrit root text: source + IDs
 ├─ sub-issue  S2  Tibetan root text: editions, proofread edition, IDs, Sanskrit links
 ├─ sub-issue  S3  Human translations: source, IDs, verse links
 ├─ sub-issue  S4  Commentaries: gather, IDs, verse links
 ├─ sub-issue  R1  Sections: raw TOCs
 ├─ sub-issue  R2  Sections: multilevel summaries
 ├─ sub-issue  R3  Verses: per-verse commentary compilations
 ├─ sub-issue  R4  Claims: raw per-commentary extraction
 ├─ sub-issue  R5  Claims: consolidated per-claim files
 ├─ sub-issue  R6  Local-Wiki: keyword lists (raw)
 ├─ sub-issue  R7  Local-Wiki: articles
 ├─ sub-issue  T1  Transformations: plans
 ├─ sub-issue  T2  Transformations: translations
 ├─ sub-issue  T3  Transformations: short videos
 └─ sub-issue  T4  Transformations: e-learning course
```

GitHub shows sub-issue completion as a progress bar on the parent card — the board therefore shows each text's overall % complete for free.

## Mapping to the vault

| Sub-issue | Vault location |
|---|---|
| S1–S2 | `1-SOURCES/Text/` |
| S3 | `1-SOURCES/Translations/` |
| S4 | `1-SOURCES/Commentaries/` |
| R1–R2 | `2-RAILS/Sections/` (`RAW/` + per-level files) |
| R3 | `2-RAILS/Verses/` |
| R4–R5 | `2-RAILS/Claims/` (`RAW/` + per-claim files) |
| R6–R7 | `2-RAILS/Local-Wiki/` (`RAW/` + articles) |
| T1–T4 | `3-TRANSFORMATIONS/` |

## Workflow automations (Project settings → Workflows)

- Item added → `Status: Backlog`
- Parent issue closed → `Status: Done`
- (Manual) Move card when a stage's sub-issues all close — GitHub can't automate cross-column moves on sub-issue state yet, so this is a weekly triage action.
