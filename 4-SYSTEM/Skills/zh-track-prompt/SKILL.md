---
name: zh-track-prompt
description: >
  Build or revise the Chinese (Traditional) prompt of a Chinese translation track (zh-academic, zh-children,
  any zh-<descriptor>): a Chinese-only system prompt that the translation model receives, written section by
  section with the user as a bilingual draft (Chinese text, English mirror for maintainers who do not read
  Chinese, design notes, decision log) and assembled into the track's requirements.md. Covers task and role,
  how to use each reference field, register with a style sample, term rules and locked formulas, output format,
  wiring the prompt into the runner (--system), and an optional A/B test. Trigger on "make a Chinese prompt for
  the translation", "write the zh prompt", "translate the prompt into Chinese for Gemini", "improve the Chinese
  translation prompt", "children's Chinese prompt", "update requirements.md for zh-academic / zh-children",
  「中文翻譯提示詞」「幫我寫兒童版的提示詞」「改進翻譯的 prompt」.
profile: rails-vault
---

# zh-track-prompt

Produces the prompt a model translates with for one Chinese track: `3-TRANSFORMATIONS/Translations/zh-<descriptor>/requirements.md`, whose whole body (minus frontmatter) is the system instruction, plus the bilingual working draft it is built from. It exists because a prompt split between a short Chinese style sheet and English task lines, field notes and output rules buried in a runner leaves the model guessing how far to trust each source and lets formulas, terms and register drift. Correct output is a five-section Chinese prompt (一 task and role, 二 reference fields and their order of authority, 三 register with a normalised style sample, 四 term rules, 五 output format) in which every rule traces to a user decision or a measured failure, every fixed formula the user chose is also locked in the termbase so it is checked, and an English mirror lets a non-Chinese-reading operator maintain it.

---

## Inputs

1. **Track folder** `3-TRANSFORMATIONS/Translations/zh-<descriptor>/` with `requirements.md` (with frontmatter), `termbase.md`, `audience.md`. If the folder or `requirements.md` frontmatter is missing, stop: the track must be commissioned first (see `About Translations.md`).
2. **The translation runner** that sends the prompt (in the pilot vaults: `0-INBOX/kf-pilot/translate/gm_variant_translate.py`). Needed to read what the model actually receives: system instruction, task line, per-segment JSON fields, feedback strings. If the vault has no runner, the skill still builds the prompt (steps 1–6) and says that wiring and testing are not possible.
3. **The termbase files** the runner locks from (e.g. `0-INBOX/kf-pilot/termbase/vajracchedika-zh/termbase.json`, `overrides.json`) and the track's `termbase.md`.
4. **Registered commentary IDs and titles** from the vault annex §Commentaries (`4-SYSTEM/Guidelines/vault-annex.md`; `4-SYSTEM/Docs/vault-annex.md` in vaults that still use the older layout).
5. **A style sample from the user** (a short passage in the target register) and its source. Never choose a sample yourself; ask.
6. **The user's decisions** on authority order, fixed formulas, paradox or other set phrases, and sensitive term families. Ask for each; never assume.
7. **Optional:** the track's current output (`work/<stem>-zh.jsonl`) to measure problems, and the usage ledger (`usage-ledger.jsonl`, `4-SYSTEM/scripts/usage-ledger/prices.json`) for cost estimates.

## Output

| Path | What |
|---|---|
| `0-INBOX/zh-prompt/zh-<descriptor>-prompt-draft.md` | Working draft: decision log, findings, sample, sections 一–五 each with Chinese, `### English mirror`, `### Design notes` |
| `3-TRANSFORMATIONS/Translations/zh-<descriptor>/requirements.md` | Built prompt: frontmatter + title + Chinese sections only |
| `0-INBOX/zh-prompt/archive/zh-<descriptor>-requirements-v<N>.md` | Previous `requirements.md`, archived before the first build |
| termbase JSON, `overrides.json`, track `termbase.md` (and any mirror copy) | Only when the user decides to lock a formula or change a rendering |
| `0-INBOX/zh-prompt/ab-test/PLAN.md` | Optional A/B test plan (no paid call without approval) |

---

## Output file format

`requirements.md`:

```markdown
---
track: zh-<descriptor>
text: <經名>（藏文本 <root-id>）
target_language: zh（繁體）
register: <register>
status: draft
termbase: termbase.md
prompt_version: v<N>（<YYYY-MM-DD>）
prompt_use: 本檔去掉 frontmatter 後，即是 Gemini 的完整系統指示（<runner> --system）
prompt_source: 0-INBOX/zh-prompt/zh-<descriptor>-prompt-draft.md（含英文對照與設計說明；修改請改草稿，再執行 4-SYSTEM/Skills/zh-track-prompt/scripts/assemble.py）
previous_version: 0-INBOX/zh-prompt/archive/zh-<descriptor>-requirements-v<N-1>.md
---

# 翻譯要求 —— <經名>，中文<版本>

## 一、任務與角色
…
## 二、參考資料說明
…
## 三、語域與文體
…
## 四、術語規則
…
## 五、輸出格式
…
```

The draft follows `templates/draft-skeleton.md` exactly: sections separated by a line `---`, each section `## 一、…` to `## 五、…`, the Chinese text first, then `### English mirror`, then `### Design notes (section N)`.

---

## Rules

1. **Only the Chinese is sent.** The English mirror and design notes never reach the model; `scripts/assemble.py` refuses to build if they would.
2. **Edit the draft, never `requirements.md`.** Change the Chinese first, then its English mirror, then run `assemble.py`.
3. **Every rule has a reason in the design notes**: a user decision (dated, with the user's own words when they gave a reason) or a measured failure (counts and segment IDs).
4. **No decision on the user's behalf.** Authority order, formulas, sample, sensitive terms and every termbase change are asked, shown with options, and recorded in the decision log before they are written.
5. **JSON keys and field names stay as the runner sends them** (`tibetan`, `academic_translation`, `blocks`, `id`, `translation` …). Explain them in Chinese; never rename them.
6. **The style sample is the user's**, its source is recorded in the prompt, its punctuation is normalised to the track's rules (「」, ：, 麼 …), and the prompt states what to learn and what not to imitate. Tell the user when the vault repo is public; never commit a scanned page or image of a sample to a public repo.
7. **A fixed formula the user chooses is locked in the termbase**, not only stated in the prompt, so the compliance check enforces it. A formula ending in ！ or ？ must be checked with its punctuation.
8. **Other tracks stay unchanged.** After any change to the runner or the termbase, compare the locked terms of every track and language before and after; anything outside the intended Chinese track that changed is a bug.
9. **Archive before replacing.** The previous `requirements.md` is copied to `0-INBOX/zh-prompt/archive/` before the first build.
10. **No paid model call without approval.** Simulate requests by intercepting the API call; give a cost estimate from the usage ledger and wait for a yes before any real run.
11. **Write to `3-TRANSFORMATIONS/` only when the user asked for it**; `0-INBOX/` for drafts; never `1-SOURCES/`.
12. **A derived track** (e.g. children's, written from the academic track) takes its meaning from the source track; where the user decides that sensitive wording (paradox frames, doctrinal term families) must match the source track, the prompt says so explicitly so the "plain words" rules do not pull it away.

---

## Procedure

1. **Read what the model receives today.**
   a. In the runner, find the system instruction, the task line, the per-segment payload fields, the output rules and the feedback strings; note the language of each.
   b. Read the track's `requirements.md`, `termbase.md`, `audience.md`, and the termbase style sheet if there is one.
   c. If output exists, measure: variants of recurring formulas, vocatives, sentence/clause length, locked-term misses (run the runner's compliance check without calling the API), and any rendering that the termbase itself forces into an error (nested locks, two spellings).
   d. Tell the user what is Chinese and what is English today, and the findings, before drafting.
2. **Create the draft** at `0-INBOX/zh-prompt/zh-<descriptor>-prompt-draft.md` from `templates/draft-skeleton.md`; fill the decision log and findings.
3. **Draft section by section with the user**, one section per turn: write the Chinese, the English mirror and the design notes; show the Chinese to the user; apply changes; record each decision. Order: 一 (task, role, readers, the only source text, commentaries by registered ID), 二 (each payload field: content, use, trust; the order of authority; revision feedback), 三 (the user's sample, normalised; what to learn; what not to imitate; fixed wordings), 四 (term rules, fixed formulas mapped part by part to the Tibetan with an example, rules aimed at measured failures), 五 (JSON, ids, no notes, no line breaks, quotation marks, headings, script and punctuation).
4. **Lock the formulas the user chose.** For each: add an entry to the termbase JSON (`"formula": true`, its own occurrence list found by a pattern on the Tibetan, rendering per register), a row to the track `termbase.md` (and any mirror copy), and a record in `overrides.json`. Check every track's locks before and after (rule 8). Report how many current segments do not comply.
5. **Fix termbase-caused errors** the findings revealed, only after showing the user each affected segment with a proposed wording and getting a yes.
6. **Build the prompt.**
   a. Copy the current `requirements.md` to `0-INBOX/zh-prompt/archive/zh-<descriptor>-requirements-v<N>.md`.
   b. Add the `prompt_version`, `prompt_use`, `prompt_source`, `previous_version` fields to its frontmatter.
   c. Run `python3 4-SYSTEM/Skills/zh-track-prompt/scripts/assemble.py 0-INBOX/zh-prompt/zh-<descriptor>-prompt-draft.md 3-TRANSFORMATIONS/Translations/zh-<descriptor>` (`--title` if the file has no `# ` line).
7. **Wire it into the runner** if it has a `--system <file>` option (frontmatter stripped, no English output rules, Chinese task line). If it does not, add one that leaves every other track's request unchanged, and check that with rule 8. Then simulate one request per variant by intercepting the API call: confirm the system text starts with the title, has no frontmatter and no English rules, and that the user message carries the Chinese task line and the expected fields and locks.
8. **Optional A/B test.** Write `0-INBOX/zh-prompt/ab-test/PLAN.md`: old vs new prompt on the same segments (a spread sample plus segments targeting each new rule), identical inputs, first pass only; automatic metrics (locks, formulas, register markers, leaks from the sample), the fact-check for accuracy, a blind pairwise judge for preference; a decision rule; calls and cost from the ledger. Do not run it without approval.
9. **Operator guide.** If someone else runs the pipeline, write `0-INBOX/zh-prompt/RUN-FULL.md`: pull, A/B gate, archive the old output and fact-check runs, translate with `--system`, fact-check, fix (`scripts/make_feedback.py` builds the `--feedback` file from a merged run), keep-best rule, close, push; derived tracks after their source track. Costs per step.
10. **Commit** with a message listing what changed; push only when the user says so.

---

## Completion check

- [ ] Draft at `0-INBOX/zh-prompt/zh-<descriptor>-prompt-draft.md` has sections 一–五, each with Chinese, `### English mirror` and `### Design notes`, plus a dated decision log
- [ ] Every rule in the prompt has a design note naming a user decision or a measured failure
- [ ] The style sample's source is in the prompt; its punctuation follows the track's rules; no sample image is committed to a public repo
- [ ] Every fixed formula the user chose is locked in the termbase JSON, the track `termbase.md` and `overrides.json`, and checked with its punctuation
- [ ] Locked terms of every other track and language are identical before and after
- [ ] The previous `requirements.md` is archived; the new one was built by `assemble.py` and contains no English mirror or design notes
- [ ] A simulated request (no API call) shows the Chinese system prompt, the Chinese task line, the expected fields and locks
- [ ] No paid model call was made without the user's approval; any test or run plan states calls and cost
- [ ] Changes are committed; pushed only if the user asked
