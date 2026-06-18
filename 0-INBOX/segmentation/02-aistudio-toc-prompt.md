# Prompt — generate a proper table of contents

Use this in the **user turn** in Google AI Studio, with `01-aistudio-system-instruction.md` already loaded as the system instruction. Fill the three fields and paste the commentary where shown.

---

## Prompt to paste

```
TASK: Extract the complete ས་བཅད་ (topical outline) from the Tibetan commentary below and produce a proper, fully nested table of contents.

METADATA
- title-bo: <<<Tibetan title of the work, e.g. སྤྱོད་འཇུག་ས་བཅད།>>>
- commentary-id: <<<short id, e.g. bo-kunpal>>>

WHAT TO PRODUCE
1. The table of contents as an ASCII TREE (ལྟེ་བའི་དཀར་ཆག), using the tree format in your system instruction:
   - the title-bo as the root line (no connector), the whole tree inside a ```text fenced code block
   - box-drawing connectors `├──` / `└──` with `│` / spaces for ancestors — depth shown by indentation, NO heading levels, no depth limit
   - a hierarchical `^TOC-…` id on every node, and that node's source block id in square brackets at the end of the line, e.g. `[^0-9]`
2. Below the code block, under a `## Notes` heading, list any nodes you marked `⚑` and why.

REQUIREMENTS
- Read the ENTIRE commentary before writing anything.
- VERBATIM-SUBSTRING RULE (most important): every heading must be a literal copy-paste from the commentary text below. Before writing any node, confirm its exact string appears in the source. If you can't find it there, DO NOT write it — it's hallucinated. Do not normalise headings to the textbook/standard name of the topic, and do not add a number word the source didn't print. Use this commentary's actual wording, even if you "know" the standard form.
- Include EVERY announced section — top-level divisions and every nested subdivision (ལ་གཉིས། / ལ་གསུམ་སྟེ། / དང་པོ་ / གཉིས་པ་ …). Do not stop at the first chapter. But achieve completeness only by reading more of the source — NEVER by inventing nodes to look thorough.
- COVERAGE CHECK: scan the source for its count phrases (ལ་N་ལས/སྟེ, རྣམ་པ་N) and ordinal runs (དང་པོ་/གཉིས་པ་…). If my text has dozens of these but your tree has far fewer nodes, you skipped spans — go back and extract them. A sparse tree of real strings beats a full-looking tree of invented ones.
- Number children sequentially within each parent (no gaps, no reuse). A child's id prefix must match its parent's id.
- Draw the tree with correct connectors: `└──` only for the last child of each parent, `├──` otherwise; carry `│` down every ancestor that still has siblings below it.
- ARITY CHECK: when a parent declares a count (གཉིས་/གསུམ་/བཞི་/ལྔ་/དྲུག་/བདུན་/བརྒྱད་ … or `ལ་N་སྟེ།`), FIRST confirm that cardinal is literally printed in my source next to that heading. If it is NOT — i.e. you added it from your knowledge of the standard framework (10 chapters, 7 limbs, 3 trainings, 3 wisdoms, 4 mindfulnesses) — strip the number, restore the bare verbatim heading, and re-segment from the source's real ordinals. If the count IS source-printed, the direct children must equal it: re-nest grandchildren or re-read for a missed item. Only a genuinely source-printed count that still mismatches gets a `⚑` + Note.
- NO RATIONALISING NOTES: never write a note like "the text doesn't enforce the seven framework" / "doesn't explicitly name the three" / "doesn't declare a count of four." Such a sentence is proof YOU supplied the number — delete the number from the heading instead of footnoting it. Notes are only for real source-internal discrepancies and true ambiguities.
- ORDINALS OUTRANK THE VERSE: segment children by the commentary's own ordinal sub-headings (དང་པོ་/གཉིས་པ་/ལྔ་པ་…), NOT by the word-count of a root-verse enumeration. A branch may be a compound slot pairing two terms (e.g. `མཆོད་བསྟོད་` = offering+praise as ONE branch with two sub-items; `བསྐུལ་ཞིང་གསོལ་བ་གདབ་པ་` = ONE branch). When the verse lists more terms than the declared count, nest the paired terms one level down rather than listing them as siblings.
- Extract only what the text actually announces. Do not invent sections.
- Output the fenced tree (and the Notes section) only — no preamble, no explanation, no English glosses unless I ask.

After the TOC, run your self-check silently and fix any violations before returning the final answer.

COMMENTARY:
<<<paste the full commentary text here, keeping the ^block-id at the end of each line>>>
```

---

## Optional add-ons

**Want the flat outline too?** Add this line under `WHAT TO PRODUCE`:

```
0. First output the FLAT outline (ས་བཅད་རྐྱང་པ།): each node as `- <text> ^TOC-…`, one tab per depth level, one blank line before a parent's first child. Then the ASCII tree.
```

**Want an English gloss alongside each heading (for review only)?** Add:

```
- After each Tibetan heading, on the SAME line, add a parenthetical English gloss in (round brackets). Keep the Tibetan exactly as-is; the gloss is supplementary and must not replace it.
```

**Long commentary getting truncated?** Process it in chapter-sized chunks: paste one chapter per turn, and start the prompt with `Continue the same outline tree. The last id you assigned was ^TOC-… ; resume numbering from there.` so the `^TOC-…` numbering stays continuous across turns.

---

## Worked micro-example (for calibration)

If the commentary contains:

```
བཤད་བྱའི་ཡན་ལག་བཤད་པ་དང་། བཤད་བྱ་དངོས་བཤད་པ་གཉིས་ལས། ^0-9
དང་པོ་བཤད་བྱའི་ཡན་ལག་བཤད་པ་ལ་གསུམ་སྟེ། སློབ་དཔོན་གྱིས་ཆོས་ཇི་ལྟར་འཆད་ཚུལ། ^0-9
སློབ་མས་ཇི་ལྟར་ཉན་ཚུལ། དཔོན་སློབ་གཉིས་ཀས་འཆད་ཉན་ཇི་ལྟར་བགྱི་བའི་ཚུལ་ལོ། ^0-10
```

…the expected tree fragment is:

```text
སྤྱོད་འཇུག་ས་བཅད།
├── བཤད་བྱའི་ཡན་ལག་བཤད་པ། ^TOC-1 [^0-9]
│   ├── སློབ་དཔོན་གྱིས་ཆོས་ཇི་ལྟར་འཆད་ཚུལ། ^TOC-1-1 [^0-9]
│   ├── སློབ་མས་ཇི་ལྟར་ཉན་ཚུལ། ^TOC-1-2 [^0-10]
│   └── དཔོན་སློབ་གཉིས་ཀས་འཆད་ཉན་ཇི་ལྟར་བགྱི་བའི་ཚུལ། ^TOC-1-3 [^0-10]
└── བཤད་བྱ་དངོས་བཤད་པ། ^TOC-2 [^0-9]
```

Note how `གཉིས་ལས།` ("of the two") created the two top-level nodes `^TOC-1` and `^TOC-2`, and `ལ་གསུམ་སྟེ།` ("has three") created the three children of `^TOC-1`. `^TOC-2` is the last top-level node, so it uses `└──`; the `│` column under `^TOC-1` stops once its last child `^TOC-1-3` is drawn.
