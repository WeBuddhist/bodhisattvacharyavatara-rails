# Pipelines — how skills and scripts chain into end-to-end flows

This folder documents the **multi-step processes** of the vault: the flows where several skills and/or scripts run in sequence to take material from one state to another (e.g. raw commentary → ingested source → extracted TOC → section summaries).

It is the *wiring diagram* that sits alongside the *parts list*:

- [`../Skills/SKILLS-CATALOG.md`](../Skills/SKILLS-CATALOG.md) describes each **skill** on its own — purpose, inputs, outputs.
- [`../Scripts/`](../Scripts/) holds the runnable **scripts**.
- This folder describes how those pieces **connect** into a working process.

For the rules and philosophy behind the vault, and for one-off human chores (git, sync, setup), see [`../docs/`](../docs/). Pipelines are neither rules nor one-off chores — they are repeatable, cross-cutting processes.

---

## What each pipeline has

Every pipeline is documented by **two files that share the same base name**:

- **`<flow>.excalidraw.md`** — an Excalidraw diagram: the flow as a visual chart (boxes for stages, arrows for order). Open it in Obsidian's Excalidraw view to edit.
- **`<flow>.md`** — the detail doc: prose covering goal, inputs, stages, outputs, and notes. It embeds the diagram at the top with `![[<flow>.excalidraw.md]]`.

A pipeline doc should answer:

- **Goal** — what the flow produces and when you'd run it.
- **Inputs** — what you need before starting (files, API keys, prerequisite stages).
- **Stages** — each step in order: the skill or script that runs it, what it consumes, what it produces, and where outputs land.
- **Outputs** — the final artefacts and their locations.
- **Notes** — gotchas, resumability, when to skip stages, what comes next.

Keep each stage traceable to a real skill (`../Skills/<name>/SKILL.md`) or script (`../Scripts/<name>`) so the doc stays a true map of what exists.

---

## Flows

| Pipeline | Goal | Key skills / scripts |
|---|---|---|
| [`toc-extraction.md`](toc-extraction.md) · [diagram](toc-extraction.excalidraw.md) | Reconstruct a commentary's ས་བཅད (sa bcad) table of contents | `toc-candidate-extraction`, `add-toc`, `tag-inline-toc`, `Scripts/toc_tree_extractor` |

_Add a row here whenever you add a flow (link both the `.md` and the `.excalidraw.md`)._

---

## Conventions

- Two files per flow sharing one base name: `<flow>.md` (detail) and `<flow>.excalidraw.md` (diagram); lowercase, hyphenated names.
- The detail doc embeds its diagram at the top with `![[<flow>.excalidraw.md]]`.
- Reference skills and scripts by their real paths so links resolve in Obsidian.
- Pipeline docs are descriptive maps, not rules — when a flow's *rules* change, the change belongs in the relevant `SKILL.md` or Guideline, and this doc is updated to match.
