# Recognizing Sachad (ས་བཅད) and splitting into two levels

This is background reading for Phase 1 of `toc-generator`. It is guidance for
judgment, not a rule engine — Tibetan commentaries vary too much in surface
wording for regex to reliably separate genuine structural markers from
look-alikes (verse quotations, incidental lists, citations). Read for
*meaning*: is this passage naming and dividing the text's own topics, or is
it just prose that happens to contain a number?

## What a Sachad looks like

A ས་བཅད (*sa bcad*, "ground-cut") is a short structural phrase, usually set
apart from the surrounding prose, that does one of two jobs:

**Announces a division** — states that the current topic splits into N named
parts, e.g.:

> དང་པོ་ལ་གཉིས་ཏེ། མཚན་དོན་དང་། འགྱུར་ཕྱག་གོ།
> ("The first has two parts: the meaning of the title, and the translators'
> homage.")

**Opens a division** — a short label marking "now treating part N", e.g.:

> གཉིས་པ་འགྱུར་ཕྱག་ནི།
> ("Second, the translators' homage:")

Common surface signals (any one is a hint, none is proof by itself — always
confirm by reading what the sentence is actually doing):

- Ordinal labels: དང་པོ། / གཉིས་པ། / གསུམ་པ། / བཞི་པ། ... — including as a
  single line on its own, or fused with a name (`གཉིས་པ་འགྱུར་ཕྱག་ནི།`)
- Division words closing a list: `ལ་གཉིས།`, `ལ་གསུམ་སྟེ།`, `ལ་བཞི།`,
  `དབྱེ་ན།`
- A closing count after a list just given: `ཞེས་རྣམ་པ་གསུམ་མོ།`,
  `གནས་བརྒྱད་དོ།`
- `ནི།` immediately after an ordinal or a short topic name, opening its body

**Not a Sachad — do not tag:**

- Verse quotations or citations that merely contain a number
- Ordinary prose that happens to list several things in passing
- Chapter label lines that are simple headers, not structural divisions of a
  larger argument (judgment call — if in doubt, treat a genuine chapter
  boundary as a depth-1 main topic; it usually is one)
- Editorial verse-locator markers like `1.1`, `8.17`

If you are not sure whether a passage divides the text's own topics versus
just describing something in the world, treat it as *not* a Sachad. Recall
matters less here than in exhaustive outline-extraction work — this skill
only needs the two levels a reader would actually use to navigate, not a
complete inventory of every nested division in the text.

## Splitting into exactly two levels

Real Sachad nesting is often 4, 6, or more levels deep in a fully-extracted
sa-bcad tree. `toc-generator` deliberately does **not** reproduce that full
depth — it picks two navigational tiers:

- **Depth 1 (main topic, `##`)** — the outermost divisions a reader would
  jump between: chapters, major parts, or (within a chapter) the highest-level
  divisions the author's own outline announces. As a rule of thumb, a
  commentary of normal length should end up with somewhere on the order of
  5–30 depth-1 entries for the whole file — enough to be a useful map, not so
  many it stops being one.
- **Depth 2 (sub-topic, `###`)** — the immediate children of a depth-1 topic:
  the parts *that* topic's own Sachad names when it enumerates. Every
  depth-2 entry has exactly one depth-1 ancestor.
- **Anything deeper** — grandchildren of a depth-1 topic, i.e. divisions
  three or more Sachad-levels down — gets **no heading of its own**. It stays
  as ordinary prose under its nearest depth-2 ancestor. Do not invent a third
  markdown level to hold it.

Where exactly the depth-1/depth-2 boundary falls is a judgment call when the
literal nesting is uneven across the document (some chapters divide deeply,
others barely at all). Prefer the split that keeps depth-1 entries
comparable in scope to each other (e.g. all chapter-level, or all
major-part-level) even if that means some depth-1 topics have no depth-2
children at all, and others have several.

## Worked example

Source (abbreviated):

```
དང་པོ་ལ་གཉིས་ཏེ། མཚན་དོན་དང་། འགྱུར་ཕྱག་གོ།
དང་པོ་མཚན་དོན་ནི། [prose ...]
གཉིས་པ་འགྱུར་ཕྱག་ལ་གསུམ་སྟེ། ལོ་ཙཱ་བའི་མཚན་དང་། ཕྱག་འཚལ་བའི་ཡུལ་དང་། དགོས་པའོ།
དང་པོ་ནི། [prose ...]
གཉིས་པ་ནི། [prose ...]
གསུམ་པ་ནི། [prose ...]
```

Classification:

- `མཚན་དོན།` and `འགྱུར་ཕྱག།` are depth-1 main topics (children of the
  document's top-level division).
- `ལོ་ཙཱ་བའི་མཚན།`, `ཕྱག་འཚལ་བའི་ཡུལ།`, `དགོས་པ།` are depth-2 sub-topics —
  they are the three children `འགྱུར་ཕྱག་ལ་གསུམ་སྟེ།` names, so they nest
  under the `འགྱུར་ཕྱག།` main-topic heading.
- The bare `དང་པོ་ནི།` / `གཉིས་པ་ནི།` / `གསུམ་པ་ནི།` lines are body-openers
  for those three sub-topics — not separate outline entries.
- If any of those three sub-topics themselves divided further (a depth-3
  Sachad), that deeper division is left as plain prose under its depth-2
  heading — no depth-4 markdown heading is created.

## Language note

This skill's examples are Tibetan because that is the common case in this
vault, but the same two-tier judgment applies to a commentary in any
language that uses analogous structural-announcement conventions (numbered
divisions, "first / second / third" section openers, and so on) — Sanskrit,
Chinese, English, etc. The recognition step is always "is this sentence
naming and dividing the text's own topics", regardless of language.
