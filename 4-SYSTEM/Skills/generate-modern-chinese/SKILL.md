---
name: spyodjug-zh-plain-chinese
description: >
  為《入菩薩行論》zh-plain-chinese 翻譯軌道生成白話書面語中文翻譯，對照藏文原典與 Padmakara 英譯，依照 requirements.md 的所有規範翻譯並存入 Obsidian。當使用者說「幫我翻譯第N天」、「生成偈N.X到N.X的白話翻譯」、「更新 zh-plain-chinese 的 day 檔案」、「依照 Padmakara 翻譯某幾首偈頌」，或貼上 Padmakara 英文偈頌並要求中文白話版時，請立即觸發此技能。也適用於使用者要求修訂現有 zh-plain-chinese day 檔案、更新術語表、或對照藏文檢查現有翻譯的情況。
---

# zh-plain-chinese 白話翻譯技能

本技能負責《入菩薩行論》（Bodhisattvacharyāvatāra）zh-plain-chinese 翻譯軌道的生成與維護工作。

---

## 專案路徑

- **Vault 根目錄：** `C:\Users\yojen\Obsidian\bodhisattvacharyavatara-rails\`
- **翻譯規範：** `3-TRANSFORMATIONS/Translations/zh-plain-chinese/requirements.md`
- **讀者輪廓：** `3-TRANSFORMATIONS/Translations/zh-plain-chinese/audience profile.md`
- **術語表：** `3-TRANSFORMATIONS/Translations/zh-plain-chinese/termbase.md`
- **Day 檔案：** `3-TRANSFORMATIONS/Translations/zh-plain-chinese/days/`

**藏文原典：** `1-SOURCES/Translations/bo-བློ་ལྡན་ཤེས་རབ།.md`
**Padmakara 英譯：** `1-SOURCES/Translations/en-Padmakara_2006.md`
**賈曹傑注疏：** `1-SOURCES/Commentaries/zh-賈曹傑 入菩薩行論廣解.md`
**達賴喇嘛教授：** `1-SOURCES/Commentaries/zh-第十四世達賴喇嘛.md`

---

## 第一品各天偈頌對照

| 天數 | 偈頌 |
|------|------|
| Day-01 | 1.1–1.3 |
| Day-02 | 1.4–1.6 |
| Day-03 | 1.7–1.9 |
| Day-04 | 1.10–1.12 |
| Day-05 | 1.13–1.15 |
| Day-06 | 1.16–1.18 |
| Day-07 | 1.19–1.21 |
| Day-08 | 1.22–1.24 |
| Day-09 | 1.25–1.27 |
| Day-10 | 1.28–1.30 |
| Day-11 | 1.31–1.33 |
| Day-12 | 1.34–1.36 |

其他品的天數對應，查閱 Vault 中相應的 `zh-daily-summary/days/` 檔案確認。

---

## 工作流程

### 第一步：讀取規範文件

開始翻譯前，必須讀取：
1. `requirements.md` — 所有翻譯規範
2. `audience profile.md` — 目標讀者輪廓
3. `termbase.md` — 已確認的術語表

### 第二步：讀取原典

對照以下來源翻譯：
1. **藏文原典**（bo-བློ་ལྡན་ཤེས་རབ།.md）— 義理忠實度的最終依據
2. **Padmakara 英譯**（en-Padmakara_2006.md）— 文學節奏與行文參考
3. **賈曹傑注疏**（如遇術語或義理不確定時）

同時讀取相應天數的 `zh-daily-summary` day 檔案，確認偈頌範圍。

### 第三步：翻譯

依照 requirements.md 的所有規範。以下是核心原則摘要（詳細規則以 requirements.md 為準）：

**義理忠實（信）**
- 每個翻譯選擇必須可追溯至藏文原典或注疏，嚴禁添譯
- 遇到不確定的詞語，查閱注疏再翻譯，不得猜測
- 使用 termbase.md 中已確認的術語譯法

**語言品質（達）**
- 現代白話書面語，非口語，非文言
- 符合中文書面語的自然語序，加入必要的連接詞
- 避免名詞化結構，優先使用動詞謂語
- 描述**負面處境**（如輪迴束縛）保留「被」字句；描述**正面成就**改為主動直述
- 描述眾生欲求、動機時，使用主動性詞語（「希求」而非「希望」）
- 條件＋反問、因果＋結論等修辭結構，用逗號連接而非句號打斷

**術語規範**
- 佛陀各稱號（善逝、大能仁、如來等）統一譯為「佛」（單數）或「諸佛」（複數，依藏文語境）
- 保留「菩提心」「菩薩」，不替換為白話說法
- 經典名稱必須使用完整正式名稱附書名號（如《妙臂菩薩所問經》），不得用描述性說法替代

**文學品質（雅）**
- 文句流暢，可朗讀默誦而不感障礙
- 呈現寂天論師「優美、謙遜、淺顯易懂」的文風
- 在清晰易懂的前提下，讓文字帶有莊重而溫暖的品質

### 第四步：生成 Day 檔案

存為 `days/day-XX.md`，格式如下：

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

### 第五步：專有名詞核查

翻譯完成後，依照 requirements.md 第 4a 節，生成本次翻譯的專有名詞列表，確認：
- 人名與稱號是否使用正式名稱
- 經典名稱是否完整且附書名號
- 佛教術語是否與 termbase.md 一致

發現新術語或確認已有術語的正確用法時，更新 `termbase.md`。

---

## 常見問題

**Padmakara 與藏文有出入時：** 以藏文為義理依據。Padmakara 是參考，不是底本。若有添譯或義理偏差，依藏文修正。

**術語不確定時：** 先查 termbase.md，再查注疏，再決定。不確定時寧可保守，不猜測。

**修訂現有 day 檔案時：** 讀取現有內容，對照藏文原典重新檢查，依使用者指示修改，如有術語變更同步更新 termbase.md。

**是否需要更新對照表 docx：** 對照表是獨立任務，只在使用者明確要求時才更新。
