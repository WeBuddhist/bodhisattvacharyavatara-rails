---
name: root-verse-context-creator
description: Use this skill for any task involving Tibetan Buddhist root texts that are combined with a nested outline (ས་བཅད།, sa-bcad). The skill generates a Tibetan contextual summary paragraph for each group of root verses by tracing the complete nested outline path — from the outermost container down to the specific section — and closing with གཞུང་ཚིག་ཡིན་ནོ།། in the style of Khenpo Kunpal's sa-bcad commentary. Trigger whenever the user says things like "summarize root text based on nested contents," "create verse context summaries," "generate sa-bcad path summaries," "do the next chapter," or shows a file that interleaves Tibetan nested outline headings with verse blocks. Also trigger for follow-up requests like "now do Chapter 2" or "continue the verse summaries." The task can scope to a single chapter or the whole text.
---

# Root Verse Context Creator

## What This Skill Produces

For every group of root-text verses that appears under a section heading in a sa-bcad+root-text (ས་བཅད་རྩ་སྦྱར།) file, produce a contextual summary paragraph in Tibetan that:

1. Quotes the verses exactly as they appear in the source file.
2. Appends a Tibetan prose paragraph that traces the full nested outline path — from the outermost relevant container all the way down to the specific leaf section — and closes with `གཞུང་ཚིག་ཡིན་ནོ།།`.

Save the output as a Markdown file in the `2-RAILS/Verses/` folder of the workspace, named `bo-[chapter]-ས་བཅད་གཞིར་བཟུང་རྩ་ཚིང་ངོས་འཛིན།.md`.

---

## Step 1 — Read and Parse the Source File

The source file is large; read it in chunks using `offset` and `limit`. Because the file interleaves outline headings with verse blocks, pay attention to:

- **Outline headings**: Lines starting with `-` and containing a `^TOC-…` anchor. The indentation level (number of tabs) encodes nesting depth.
- **Verse blocks**: Lines indented under an outline heading that contain Tibetan syllables but **no** `^TOC-…` anchor. Verse lines usually start with a tab and end with `། །` or `།`.
- **Chapter colophon** (`མཚན།` heading): Marks the end of a chapter's verse content.

Group the verses: every consecutive set of verse lines that falls under the same leaf-level outline heading is one verse group. Note the full ancestor chain of that heading — that chain is the outline path you will trace in the summary.

---

## Step 2 — Build the Outline Path in Tibetan

The summary paragraph must state the position of the verse group in the outline. Reconstruct this path in natural Tibetan prose by working **outward to inward**: start from the outermost relevant container (usually the chapter group), state how many sub-sections it contains, name them, pick the one that leads to the target, and repeat at each level until you reach the leaf section.

### Core Sentence Frame

```
ཞེས་པའི་[VERSE-COUNT-PHRASE]་འདི་[ནི/དག་ནི]་[PATH-CHAIN]་གཞུང་ཚིག་ཡིན་ནོ།།
```

- Use `འདི་ནི་` for a single-verse group.
- Use `འདི་དག་ནི་` for a multi-verse group.

### Path Chain Construction

Each level of the chain follows one of two patterns:

**A. Branching level** — when the parent contains multiple named sub-sections and you must say "from the N sub-sections, the Kth one is…":

```
[PARENT-NAME]-ལ་ [CHILD-1] དང་ [CHILD-2] གཉིས་ལས། [ORDINAL]-པ་ [CHILD-K]-…
```

When there are three named children:
```
[PARENT-NAME]-ལ་ [CHILD-1]། [CHILD-2]། [CHILD-3]-བཅས་གསུམ་ལས། [ORDINAL]-པ་ [CHILD-K]-…
```

When there are more children, list them with `།` separators and close with `-བཅས་[N]-ལས།`.

**B. Direct level** — when a container has exactly one named part that is the target:
```
[CONTAINER-NAME]-ཡི་ [PART-NAME]-བཤད་པ་ལ་…
```

**Ordinals in Tibetan:**

| Position | Tibetan |
|----------|---------|
| 1st | དང་པོ་ |
| 2nd | གཉིས་པ་ |
| 3rd | གསུམ་པ་ |
| 4th | བཞི་པ་ |
| 5th | ལྔ་པ་ |
| 6th | དྲུག་པ་ |
| 7th | བདུན་པ་ |

**Count words for sub-sections:**

| Count | Tibetan |
|-------|---------|
| 2 | གཉིས་ལས། |
| 3 | གསུམ་ལས། |
| 4 | བཞི་ལས། |
| 5 | ལྔ་ལས། |
| 6 | དྲུག་ལས། |

### Closing the Path

The final clause names the leaf section and ends:

- `[LEAF-SECTION]-སྟོན་པའི་གཞུང་ཚིག་ཡིན་ནོ།།`  — when the section "shows/demonstrates" something.
- `[LEAF-SECTION]-བཤད་པའི་གཞུང་ཚིག་ཡིན་ནོ།།`  — when the section "explains" something.
- `[LEAF-SECTION]-བསྒྲུབ་པའི་གཞུང་ཚིག་ཡིན་ནོ།།`  — when the section "establishes" something through scripture or reasoning.
- `[LEAF-SECTION]-བསྟན་པའི་གཞུང་ཚིག་ཡིན་ནོ།།`  — when the section "teaches/presents" through an example.
- For a cross-reference section (ཞལ་འཕང་བ།): `འདིར་མ་བཤད་པ་གཞུང་གཞན་དུ་ཞལ་འཕང་བའི་གཞུང་ཚིག་ཡིན་ནོ།།`

Choose the closing verb that matches the sa-bcad label of the leaf section.

---

## Step 3 — Count the Verses Correctly

| Lines in group | Phrase to use |
|---------------|---------------|
| 2 (half-verse) | `ཚིགས་སུ་བཅད་པ་འདི་ནི་` |
| 4 (1 full verse / shloka) | `ཤློཀ་གཅིག་པོ་འདི་ནི་` |
| 8 (2 shlokas) | `ཤློཀ་གཉིས་པོ་འདི་དག་ནི་` |
| 12 (3 shlokas) | `ཤློཀ་གསུམ་པོ་འདི་དག་ནི་` |
| 16 (4 shlokas) | `ཤློཀ་བཞི་པོ་འདི་དག་ནི་` |
| 20 (5 shlokas) | `ཤློཀ་ལྔ་པོ་འདི་དག་ནི་` |
| 28 (7 shlokas) | `ཤློཀ་བདུན་པོ་འདི་དག་ནི་` |

For edge cases (e.g., a verse that runs 6 lines because it contains one 4-line shloka plus a 2-line fragment), treat the 4-line block as one shloka and the 2-line block as a separate group if they appear under different headings. If they appear under the same heading, count the combined line count and use the nearest shloka count plus note the fragment.

---

## Step 4 — Assemble the Output

Produce a Markdown file using this repeating unit for each verse group:

```markdown
## [SECTION-NUMBER-IN-TIBETAN]། [LEAF-SECTION-HEADING]

[VERSE LINE 1]
[VERSE LINE 2]
[VERSE LINE 3]
[VERSE LINE 4]

[…additional verse stanzas if present…]

ཞེས་པའི་[VERSE-COUNT-PHRASE]་འདི་[ནི/དག་ནི]་[FULL PATH CHAIN]་གཞུང་ཚིག་ཡིན་ནོ།།

---
```

Number the sections consecutively in Tibetan numerals (༡། ༢། ༣། …).

Title the file:
```
bo-[chapter-name-in-Tibetan]-ས་བཅད་ལྟར་གཞུང་ཚིག་མདོར་བསྡུས།.md
```

Add a closing colophon at the very end:
```
*[Text name]་ལས། [Chapter title]་ཞེས་བྱ་བ་སྟེ་ལེའུ་[ordinal]་གཞུང་ཚིག་ས་བཅད་ལྟར་མདོར་བསྡུས་སོ།། །།*
```

---

## Reference: Worked Example (Chapter 1)

The session that produced the Chapter 1 output demonstrates every grammar pattern this skill requires. Study these examples carefully:

### Single verse (4 lines) — ལུས་རྟེན་བཤད་པ།

> ཞེས་པའི་ཤློཀ་གཅིག་པོ་འདི་ནི་བྱང་ཆུབ་ཀྱི་སེམས་རིན་པོ་ཆེ་མ་སྐྱེས་པ་བསྐྱེད་པར་བྱེད་པའི་ལེའུ་གསུམ་ལས། དང་པོ་བྲོད་པ་བསྐྱེད་པ་ཕན་ཡོན་གྱི་ལེའུ་ཡི་གཞུང་བཤད་པ་ལ་བྱང་ཆུབ་སེམས་ཀྱི་རྟེན་བཤད་པ་དང་བརྟེན་པ་སེམས་བསྐྱེད་ཀྱི་ཕན་ཡོན་བཤད་པ་བཅས་ས་བཅད་གཉིས་ལས། དང་པོ་བྱང་ཆུབ་སེམས་ཀྱི་རྟེན་བཤད་པ་ལ་ལུས་རྟེན་བཤད་པ་དང་སེམས་རྟེན་བཤད་པ་གཉིས་ལས། དང་པོ་ལུས་རྟེན་བཤད་པའི་གཞུང་ཚིག་ཡིན་ནོ།།

**Path decoded:**
- Outermost container → ལེའུ་གསུམ་ (3 chapters) → དང་པོ་ (1st chapter)
- Within 1st chapter's text → 2 outline sections (རྟེན། and ཕན་ཡོན།) → དང་པོ་ (1st: རྟེན།)
- Within རྟེན། → 2 parts (ལུས་རྟེན། and སེམས་རྟེན།) → དང་པོ་ (1st: ལུས་རྟེན།)
- Closes: ལུས་རྟེན་བཤད་པའི་གཞུང་ཚིག་ཡིན་ནོ།།

### Three verses (12 lines) — དགེ་བ་གཞན་ལས་ཁྱད་འཕགས་ཕན་ཡོན། (the example given by user)

> ཞེས་པའི་ཤློཀ་གསུམ་པོ་འདི་དག་ནི་བྱང་ཆུབ་ཀྱི་སེམས་རིན་པོ་ཆེ་མ་སྐྱེས་པ་བསྐྱེད་པར་བྱེད་པའི་ལེའུ་གསུམ་ལས། དང་པོ་བྲོད་པ་བསྐྱེད་པ་ཕན་ཡོན་གྱི་ལེའུ་ཡི་གཞུང་བཤད་པ་ལ་བྱང་ཆུབ་སེམས་ཀྱི་རྟེན་དང་བརྟེན་པ་སེམས་བསྐྱེད་ཀྱི་ཕན་ཡོན་བཤད་པ་བཅས་ས་བཅད་གཉིས་ལས། གཉིས་པ་བརྟེན་པ་སེམས་བསྐྱེད་ཀྱི་ཕན་ཡོན་བཤད་པ་ལ་སེམས་བསྐྱེད་སྤྱིའི་ཕན་ཡོན་བཤད་པ་དང་སྨོན་འཇུག་སོ་སོའི་ཕན་ཡོན་བཤད་པ་གཉིས་ལས། དང་པོ་སེམས་བསྐྱེད་སྤྱིའི་ཕན་ཡོན་བཤད་པ་ལ་དགེ་བ་གཞན་ལས་ཁྱད་པར་དུ་འཕགས་པའི་ཕན་ཡོན། མིང་དོན་གནས་འགྱུར་བའི་ཕན་ཡོན། ཕན་ཡོན་དཔེའི་སྒོ་ནས་བསྟན་པ་བཅས་གསུམ་ལས། དང་པོ་དགེ་བ་གཞན་ལས་ཁྱད་པར་དུ་འཕགས་པའི་ཕན་ཡོན་སྟོན་པའི་གཞུང་ཚིག་ཡིན་ནོ།།

**Path decoded:**
- 3 chapters → 1st chapter's text → 2 sections → 2nd (benefits) → 2 sub-sections (སྤྱི། and སོ་སོ།) → 1st (སྤྱི།) → 3 sub-sub-sections → 1st (དགེ་འཕགས།)
- Closes: དགེ་བ་གཞན་ལས་ཁྱད་པར་དུ་འཕགས་པའི་ཕན་ཡོན་སྟོན་པའི་གཞུང་ཚིག་ཡིན་ནོ།།

### Six example sub-sections — list all six when descending into them

When the parent has 6 named children (as in ཕན་ཡོན་དཔེའི་སྒོ་ནས་བསྟན་པ།), name all six each time, then pick the target ordinal:

> …གསུམ་པ་ཕན་ཡོན་དཔེའི་སྒོ་ནས་བསྟན་པ་ལ་གསེར་འགྱུར་གྱི་དཔེས་སངས་རྒྱས་ཐོབ་པར་བསྟན་པ། རིན་པོ་ཆེའི་དཔེས་དོན་ཆེ་བར་བསྟན་པ། འབྲས་བུ་ཅན་གྱི་ལྗོན་ཤིང་གི་དཔེས་དགེ་རྩ་མི་ཟད་ཅིང་གོང་དུ་འཕེལ་བར་བསྟན་པ། སྐྱེལ་མ་དཔའ་བོའི་དཔེས་ངེས་པའི་སྡིག་པ་ཟིལ་གྱིས་གནོན་པར་བསྟན་པ། དུས་མཐའི་མེའི་དཔེས་མ་ངེས་པའི་སྡིག་པ་དྲུང་ནས་འབྱིན་པར་བསྟན་པ། འདིར་མ་བཤད་པ་གཞུང་གཞན་དུ་ཞལ་འཕང་བ་བཅས་དྲུག་ལས། [ORDINAL]-པ་ [TARGET-NAME]-གཞུང་ཚིག་ཡིན་ནོ།།

### Five verses — ལྔ་པོ་

> ཞེས་པའི་ཤློཀ་ལྔ་པོ་འདི་དག་ནི་…

### Seven verses — བདུན་པོ་

> ཞེས་པའི་ཤློཀ་བདུན་པོ་འདི་དག་ནི་…

### Half-verse (2 lines) — ཚིགས་སུ་བཅད་པ་

> ཞེས་པའི་ཚིགས་སུ་བཅད་པ་འདི་ནི་…

---

## Key Principles

**Trace every ancestor.** Every node in the hierarchy from the outermost container to the leaf must appear in the summary paragraph. Do not skip levels.

**Name all siblings when branching.** Whenever you state "from N sub-sections," list every sibling by name before naming the target. This is what gives the reader a complete picture of the outline branch.

**Use the sa-bcad heading names verbatim.** Do not paraphrase outline headings; quote them exactly as they appear in the source file. The names carry precise doctrinal meaning.

**Match the closing verb to the sa-bcad label.** Choose སྟོན་པ།, བཤད་པ།, བསྒྲུབ་པ།, or བསྟན་པ། based on the actual heading used in the source. If the heading contains དཔེ་ it usually closes with བསྟན་པ།; if it contains རིགས་པ། it closes with བསྒྲུབ་པ།.

**Copy verses exactly.** Do not alter spacing, punctuation, or the `། །` line-ending markers.

**Chapter scope.** If the user specifies a chapter (e.g., "Chapter 1 only"), process only the verse groups between that chapter's first outline heading and its closing `མཚན།` colophon.

---

## Output Location

Save the final Markdown file to:
```
[workspace-root]/2-RAILS/Verses/
```

Present the file to the user with a `computer://` link when done.
