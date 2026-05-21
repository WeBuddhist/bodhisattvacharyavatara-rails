---
name: format-chinese-commentary
description: Format and normalize Chinese Buddhist commentaries of the Bodhicharyavatara in the 1-SOURCES folder. Structures headings, maps traditional outlines (科判), applies block IDs, and implements a robust batch-processing protocol for long texts.
---

# Chinese Commentary Formatting Skill (中文註釋處理與格式化工具)

## Purpose (目的)

This skill defines the standard procedure for formatting, structuring, and normalizing Chinese commentaries of the *Bodhicharyavatara* (入菩薩行論) in the `1-SOURCES/Commentaries/` folder. It maps traditional Chinese outlines (科判) into the Markdown heading hierarchy, breaks down long prose into highly granular paragraphs, transcludes root verses, applies precise Obsidian block IDs, and implements a robust batch-processing protocol to handle long texts.

---

## Core Principles (核心原則)

1. **Strict Preservation (嚴格保留)**: Do not delete, summarize, or alter any commentary text. Maintain the original wording, including traditional outline labels (e.g., `甲一`, `乙二`, `丙三`).
2. **Paragraph Granularity (段落細粒度化)**: Break long prose sections into very short, discrete paragraphs (ideally 1–3 sentences, not exceeding 3-4 lines of Chinese text). This is crucial for precise block referencing.
3. **Traditional Outline (科判) Mapping**: Map hierarchical Chinese outline labels to the Markdown heading hierarchy up to Level 4 (`####`).
4. **Root Verse Transclusion (根境頌詞嵌入)**: Transclude the matching root verse from the root text file immediately before the commentary on that verse.
5. **Obsidian Block IDs (區塊識別碼)**: Apply sequential, unique block IDs at the end of every discrete text block, restarting the counter under each heading.
6. **Batch Processing (分批處理)**: Since commentaries are extremely long, process the text in sequential batches, maintaining a state block to ensure continuity.

---

## 1. Heading Structure & Outline Mapping (標題結構與科判對照)

Traditional Chinese commentaries organize their analysis using extensive hierarchical outlines (科判) prefixed with Heavenly Stems (甲、乙、丙、丁...), Earthly Branches (子、丑、寅、卯...), or Chinese numerals (一、二、三...). These must be mapped to the Markdown heading tree:

- **Level 1 (`#`)**: Main Book Title. Used only once at the very top of the file (below the frontmatter). No block ID.
- **Level 2 (`##`)**: Chapters (品). Format: `## N. [Chapter Title] ^N-0` (e.g., `## 1. 第一品 讚菩提心功德品 ^1-0`).
- **Level 3 (`###`)**: Major structural divisions (usually `甲` level). Format: `### N.M [Division Title] ^N-M-0` (e.g., `### 1.1 甲一、釋題 ^1-1-0`).
- **Level 4 (`####`)**: Sub-divisions (usually `乙` or `丙` level). Format: `#### N.M.P [Sub-division Title] ^N-M-P-0` (e.g., `#### 1.1.1 乙一、譯文皈敬 ^1-1-1-0`).
- **Granular Divisions**: For deeper levels (e.g., `丁`, `戊`, `己`, `子`, `丑` etc.), do NOT use headings deeper than `####` (Level 5 `#####` is restricted). Instead, format them as bold text inside standard paragraphs, followed by a block ID (e.g., `**丁一、所為義。** 由於稱揚殊勝皈境功德... ^1-1-5`).

### Format Rules:
- Leave exactly one blank line before and after every heading.
- ID format for headings always ends with `-0` (reserved for headings).
- Do NOT add block IDs to heading lines using the caret `^` at the end; instead, write them inline at the end of the heading text (e.g., `### 1.1 甲一、釋題 ^1-1-0`).

---

## 2. Paragraph & Verse Formatting (段落與頌詞格式)

- **Prose Granularity**: Long paragraphs must be split at logical break points (e.g., transitions in argument, new sub-arguments, or before/after citations). Keep paragraphs short (1–2 sentences, 3-4 lines maximum) to optimize them for referencing.
- **Root Verse Transclusion**: Whenever a root verse is introduced, insert a transclusion link pointing to the root text file.
  - Format: `![[1-SOURCES/Text/sk-dev.md#^1-1]]` (where `sk-dev.md` is the root text declared in the frontmatter, and `^1-1` is the matching verse ID).
- **Chinese Verse Translation**: If the commentary includes a Chinese translation of the root verse (usually 4-line stanzas), format it as an independent block with each verse-line on its own line:
  ```markdown
  為己一切生中備諮詢，  
  亦為利他與我同類機，  
  遵依正士智者之所許，  
  入菩薩行論釋今當作。 ^1-10
  ```
  Note: Use two spaces at the end of each line for line breaks within the block, and place the block ID at the end of the final line.

---

## 3. Obsidian Block IDs (区块識別碼規範)

- **Placement**: Add a unique block ID at the end of every discrete text block (paragraphs, verses, standalone list items).
- **ID Format**:
  - Chapter-level blocks: `^N-V` (where `N` is the Chapter number, and `V` is the sequential counter starting at 1).
  - Section-level blocks: `^N-S-V` (where `S` is the Section number).
  - To prevent complexity, **always prefer a flat 2-segment or 3-segment format** (e.g., `^1-1`, `^1-2` or `^1-1-1`, `^1-1-2`).
- **Sequence Restart**: The sequential counter (`V`) MUST restart at `1` under every new Level 2 (`##`) or Level 3 (`###`) heading.
- **No Carets on Headings**: Do NOT use block IDs with carets on heading lines. Headings use the inline `-0` format (e.g., `^1-1-0`).

---

## 4. Batch Processing Protocol (分批處理協議)

Since Chinese commentaries are extremely long, they must be processed in sequential batches (chunks) of approximately **100–150 lines of text** (or ~3000–5000 characters). 

To maintain structural consistency across runs, the agent must adhere to the following protocol:

### Step 1: Identify and Split
1. Read the raw text file and identify natural boundaries (e.g., end of chapters, end of major `甲` sections).
2. Split the file into sequential batches. Save the raw batches in `0-INBOX/temp/` if needed.

### Step 2: Read State
Before processing a new batch, read the **State Block** from the end of the previous processed file or the current session context. The State Block tracks:
- `current_chapter` (Chapter number, e.g., `1`)
- `current_section` (Section number, e.g., `1.1`)
- `current_subsection` (Subsection number, e.g., `1.1.1` or `none`)
- `block_counter` (Sequential block counter, e.g., `45`)

### Step 3: Format the Batch
Process the batch applying all formatting, outline mapping, and block ID rules. Ensure that:
- If a new heading is encountered, reset the `block_counter` to `1` (or appropriate sub-counter).
- Increment the `block_counter` for every formatted paragraph/verse.

### Step 4: Write and Append
Append the formatted text to the target file in `1-SOURCES/Commentaries/`.

### Step 5: Write State Block
At the very end of the processed batch, write the updated State Block as an HTML comment so the next run can read it:
```markdown
<!-- BATCH_STATE
current_chapter: 1
current_section: 1.2
current_subsection: 1.2.1
block_counter: 18
-->
```

---

## 5. Examples (示範)

### Raw Chinese Commentary Input:
```text
入菩薩行論廣解卷一
極尊正士諸具大悲心者足下恭敬頂禮。
誰之智慧盡除諸罪，相好功德熾然四身，輪超法界際，大悲流露六十支分韻音，無垢光明普照無邊諸眾生，任運成辦，恒常無間，善能破除無邊眾生愚癡諸黑暗，於諸能仁自在上師大士聖妙吉祥足前，我今恭敬禮。
為己一切生中備諮詢，亦為利他與我同類機，遵依正士智者之所許，入菩薩行論釋今當作。自見取執絹網所繫縛，謂言欲證小乘菩提果，不須證入甚深真如性，願捨諸顛倒說而諦聽。
其所造《入菩薩行論》分四：甲一、釋題；甲二、皈敬；甲三、正義；甲四、結義。今初：
梵語有四種，此是桑支達語也。此論題名「菩提」，藏語降曲；「薩埵」，藏語「生巴」；「雜雅」，藏语「覺巴」；阿瓦打[冒-目+阿]藏語「[覺/勿]巴。」
```

### Formatted Output:
```markdown
---
title: 入菩薩行論廣解
author: 賈曹傑 (Gyaltsab Je)
translator: 隆蓮法師 (Longlian)
language: Chinese
file_type: commentary
lang_tag: zh
verse_id_format: verse
registered_id: gyaltsab-je
root_text: 1-SOURCES/Text/sk-dev.md
covers_verses: 1-1–10-58
source_description: "隆蓮法師譯《入菩薩行論廣解》。"
---

# 入菩薩行論廣解

## 0. Introduction ^0-0

入菩薩行論廣解  
寂天菩薩造頌　傑操大師註解　隆蓮法師譯 ^0-1

極尊正士諸具大悲心者足下恭敬頂禮。 ^0-2

誰之智慧盡除諸罪，相好功德熾然四身，輪超法界際，大悲流露六十支分韻音，無垢光明普照無邊諸眾生，任運成辦，恒常無間，善能破除無邊眾生愚癡諸黑暗，於諸能仁自在上師大士聖妙吉祥足前，我今恭敬禮。 ^0-3

為己一切生中備諮詢，  
亦為利他與我同類機，  
遵依正士智者之所許，  
入菩薩行論釋今當作。 ^0-4

自見取執絹網所繫縛，謂言欲證小乘菩提果，不須證入甚深真如性，願捨諸顛倒說而諦聽。 ^0-5

### 0.1 總綱科判 ^0-1-0

其所造《入菩薩行論》分四：甲一、釋題；甲二、皈敬；甲三、正義；甲四、結義。今初： ^0-1-1

#### 0.1.1 甲一、釋題 ^0-1-1-0

梵語有四種，此是桑支達語也。此論題名「菩提」，藏語降曲；「薩埵」，藏語「生巴」；「雜雅」，藏語「覺巴」；阿瓦打[冒-目+阿]藏語「[覺/勿]巴。」 ^0-1-1-1

<!-- BATCH_STATE
current_chapter: 0
current_section: 0.1
current_subsection: 0.1.1
block_counter: 1
-->
```

---

## 6. Quality Checklist (品質檢查表)

- [ ] Frontmatter block exists at the very top with all required fields.
- [ ] Headings are formatted strictly as `## N. Title ^N-0` (or `### N.M Title ^N-M-0`).
- [ ] No carets `^` are placed at the end of heading lines.
- [ ] All prose sections are broken into short paragraphs (max 3-4 lines).
- [ ] Root verse transclusions are inserted correctly as `![[1-SOURCES/Text/sk-dev.md#^N-V]]`.
- [ ] Block IDs are sequential, unique, and restart at 1 under each heading.
- [ ] State Block is appended at the end of the batch.
- [ ] No text, commentary, or outline labels were omitted or summarized.
