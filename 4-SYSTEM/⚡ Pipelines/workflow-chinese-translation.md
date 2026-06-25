# Daily Plan Creation Workflow — Chinese

**《入菩薩行論》zh-plain-chinese · Padmakara 白話中文翻譯軌道**
`Skill: spyodjug-zh-plain-chinese` · Language: 現代白話書面語

> [!note]
> This is a **translation track**, not a practice plan format. The output is verse translations with a brief connecting note — no liturgy, no practice instructions.

---

## ① Required Documents & Inputs

| Layer | File | Purpose |
|---|---|---|
| `1-SOURCES` · 根本文 | `bo-བློ་ལྡན་ཤེས་རབ།.md` | 藏文原典 — 義理忠實度的最終依據 |
| `1-SOURCES` · 英譯 | `en-Padmakara_2006.md` | Padmakara 英譯 — 文學節奏與行文參考（非底本） |
| `1-SOURCES` · 注疏 | `zh-賈曹傑 入菩薩行論廣解.md` | 賈曹傑注疏 — 術語與義理不確定時查閱 |
| `1-SOURCES` · 注疏 | `zh-第十四世達賴喇嘛.md` | 達賴喇嘛教授 |
| Track Contract | `zh-plain-chinese/requirements.md` | 翻譯規範 — **所有規則以此文件為準** |
| Track Contract | `zh-plain-chinese/audience profile.md` | 目標讀者輪廓 |
| Track Contract | `zh-plain-chinese/termbase.md` | 術語表 — 已確認的術語譯法 |

---

## ② Daily Planning Workflow

### 第一步 — 讀取規範文件

> [!info] Contract Review · Terminology Governance
> Read `requirements.md`, `audience profile.md`, and `termbase.md` in full **before generating any content**. All translation rules are binding from `requirements.md` — this workflow is a summary only.

### 第二步 — 讀取原典 & 確認偈頌範圍

> [!info] Multi-source Research · Block-ID Navigation · Cross-language Reading
> Read the three sources in order of authority:
> 1. **藏文原典** (`bo-བློ་ལྡན་ཤེས་རབ།.md`) — truth anchor for meaning
> 2. **Padmakara 英譯** (`en-Padmakara_2006.md`) — literary rhythm and phrasing reference
> 3. **賈曹傑注疏** — consult when a term or meaning is uncertain
>
> Confirm verse range from the day's schedule (e.g. Day-01 = 1.1–1.3).

### 術語確認 ⬦ Decision Point

> [!warning] Terminology Resolution · Source Consultation
> **Is the term in `termbase.md`?**
> - **Yes →** use the confirmed rendering
> - **No →** check `termbase.md` first → then commentary → then decide. Never guess. When in doubt, choose the conservative rendering.
> - **New term confirmed →** update `termbase.md` before saving the day file

### 第三步 — 翻譯：三美原則 (信・達・雅)

> [!info] Translation · Literary Adaptation · Buddhist Textual Fidelity
> Apply all three principles simultaneously for every verse.

| Principle | 原則 | Core Rules |
|---|---|---|
| **信 — Fidelity** | 義理忠實 | Every choice traceable to Tibetan or commentary. No additions. Padmakara is reference, not source. |
| **達 — Clarity** | 現代白話書面語 | Modern written Chinese — not colloquial, not Classical. Natural word order + connectives. Verbs over nouns. |
| **雅 — Elegance** | 莊重而溫暖 | Readable aloud. Warm, solemn, not academic. Shantideva's style: beautiful, humble, accessible. |

#### 語言規範 (Language Rules)

| Rule | Detail |
|---|---|
| 負面處境 | Use 被字句 (passive) — e.g. 輪迴束縛 |
| 正面成就 | Use active voice |
| 眾生欲求/動機 | Use active agency words: 「希求」not 「希望」|
| 條件＋反問 | Connect with comma, not full stop |
| 佛陀稱號 | 善逝/大能仁/如來 → 「佛」(singular) or 「諸佛」(plural) |
| 菩提心/菩薩 | Keep as-is — do not replace with vernacular |
| 經典名稱 | Full formal title + 《書名號》always — never a descriptive substitute |

> [!warning] Padmakara Conflict Rule
> **Tibetan always wins.** If Padmakara adds content or shifts meaning relative to the Tibetan, correct according to the Tibetan. Padmakara is rhythm reference only.

### 第四步 — 生成 Day 檔案

> [!info] Document Structure · Thematic Synthesis
> Assemble translated verses into the day file structure:

```markdown
# 第X天 — Padmakara 白話中文

**第N品：[品名]　偈 N.X–N.X**

---

[第一首偈頌的白話翻譯]

[第二首偈頌的白話翻譯]

[第三首偈頌的白話翻譯]

---

*[簡短注解，說明各偈主題與彼此連結]*
```

### 第五步 — 專有名詞核查 & Termbase Update

> [!note] Terminology Audit · Quality Assurance · Termbase Maintenance
> Generate a proper-noun checklist for this day's translation. Verify:
> - [ ] 人名與稱號使用正式名稱
> - [ ] 經典名稱完整且附《書名號》
> - [ ] 佛教術語與 `termbase.md` 一致
> - [ ] 佛陀稱號統一（善逝/大能仁/如來 → 「佛」或「諸佛」）
>
> **If any new term is confirmed, update `termbase.md` before saving the day file.**

### 核查通過？ ⬦ Decision Point

> [!warning] Consistency Check · Iterative Revision
> - **Yes →** save day file (and `termbase.md` if updated)
> - **No →** correct inconsistencies against termbase, re-check. The day file and termbase must be consistent before saving.

### ✓ Save Output (Day File + Termbase if Updated)

> [!success] File Management · Version Governance
> - Day file: `3-TRANSFORMATIONS/Translations/zh-plain-chinese/days/day-XX.md`
> - If termbase updated: save `termbase.md` simultaneously
> - **Do not update the parallel docx comparison table** unless the user explicitly requests it

---

## ③ Skills & Competencies by Stage

| Stage | Skills Required |
|---|---|
| Contract review | Terminology governance, requirement analysis |
| Source gathering | Multi-source research, block-ID navigation, cross-language reading |
| Terminology resolution | Term lookup, source consultation, conservative decision-making |
| Translation — 信 | Textual fidelity, commentary consultation, zero-addition discipline |
| Translation — 達 | Modern Chinese register, syntax restructuring, voice/aspect rules |
| Translation — 雅 | Literary sensitivity, tonal calibration, readability testing |
| Document assembly | Structural formatting, thematic synthesis, note writing |
| Terminology audit | Proper-noun verification, termbase consistency, QA |
| Termbase maintenance | Terminology governance, version control |

---

## Key Constraints

> [!warning] Non-negotiable rules
> - **藏文優先：** Tibetan is always the meaning authority — Padmakara is rhythm reference only
> - **No additions:** every translation choice must trace to Tibetan or commentary
> - **No guessing:** uncertain terms → consult commentary → decide conservatively
> - **Termbase consistency:** new terms must be added to `termbase.md` before saving the day file
> - **Docx table:** update only when explicitly requested by user
> - **No parametric knowledge:** if unsure about a term or meaning, check the source files

---

## Source Authority Hierarchy

```
藏文原典 (bo-བློ་ལྡན་ཤེས་རབ།.md)       ← 義理忠實度最終依據
        ↓
Padmakara 英譯 (en-Padmakara_2006.md)  ← 節奏與文學參考
        ↓
賈曹傑注疏 / 達賴喇嘛教授               ← 術語與義理疑問時查閱
        ↓
termbase.md                            ← 已確認術語，直接採用
```
