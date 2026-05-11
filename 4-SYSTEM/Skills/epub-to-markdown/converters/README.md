# Converter Pipeline — Institutional Memory

Each file in this directory is a publisher-specific EPUB→Markdown converter.
This README is the **single source of truth** for patterns, bugs, and decisions
made across all converters. Read it before writing a new one. Append to it
whenever you discover a new pattern, fix a bug, or make a design decision.

---

## Directory contents

| File | Publisher / scope | Status |
|---|---|---|
| `epub_to_markdown.py` | Generic fallback (template) | Stable |
| `vajra-vidya-library.py` | Vajra Vidya Library | Stable |
| `lekphi.py` | LEK-PHI series (Khenpo Kunzang Palden) | Stable |

Supporting scripts (in parent directory):

| File | Purpose |
|---|---|
| `epub_inspector.py` | Structural profile → JSON |
| `root_marker_to_bold.py` | Standalone post-processor: `༷` → `**bold**` |

---

## Universal inspection checklist

Run these steps on **every new epub** before writing a converter.

### 1. Run the inspector

```bash
python epub_inspector.py source.epub > profile.json
```

Check: `publisher_slug`, `css_classes`, `heading_colors`, `mixed_class_patterns`,
`spine_docs`, `toc`.

### 2. Run the span co-occurrence check (MANDATORY — do not skip)

The inspector's `mixed_class_patterns` field **can be empty even when mixed
inline spans exist** — it misses utility-suffixed classes like
`Tibetan-Sabche _idGenCharOverride-1`. Always run this independently:

```bash
python3 -c "
from bs4 import BeautifulSoup
from collections import Counter
import zipfile, sys

epub_path = sys.argv[1]
with zipfile.ZipFile(epub_path) as z:
    docs = [n for n in z.namelist() if n.endswith('.xhtml') or n.endswith('.html')]
    counts = Counter()
    for doc in docs:
        soup = BeautifulSoup(z.read(doc), 'html.parser')
        for p in soup.find_all('p'):
            pcls = tuple(c for c in p.get('class', []) if not c.startswith('_'))
            for span in p.find_all('span', recursive=False):
                scls = tuple(c for c in span.get('class', []) if not c.startswith('_'))
                if scls and scls != pcls:
                    counts[(pcls, scls)] += 1
    for (pc, sc), n in counts.most_common():
        print(f'p={pc}  span={sc}  n={n}')
" source.epub
```

Any row where `p_class != span_class` is a **mixed paragraph** requiring
run-based processing (see Algorithm section below).

### 3. Check for root-text syllable markers

```bash
python3 -c "
import zipfile, sys
MARKER = '༷'  # U+0F37 TIBETAN MARK NADA
with zipfile.ZipFile(sys.argv[1]) as z:
    total = sum(z.read(n).decode('utf-8', errors='ignore').count(MARKER)
                for n in z.namelist() if n.endswith('.xhtml'))
    print(f'Root marker count: {total}')
" source.epub
```

If count > 0, ensure `convert_root_markers()` is called in `emit_run()`.

---

## Algorithm reference

### A. Paragraph-level classification (simple case)

When **no mixed spans** are present, classify by the `<p>` element's own
CSS classes and call `get_text()`:

```
Tibetan-Sabche / Tibetan-Sabche-After-Title-Chapter  → [!sabche] callout
Tibetan-External-Citations                           → [!lung] callout
Tibetan-Citations-in-Verse_*                         → grouped [!lung] (see B)
Tibetan-Chapter                                      → # H1 heading
Tibetan-Sub-Chapter                                  → ## H2 heading
Tibetan-Commentary[-Non-Indent] / Regular-Indented   → plain text
Credits-Page_* / Front-*                             → skip
```

Utility-only classes (`_idGenCharOverride-1`, `_idGenParaOverride-1`) are
always stripped before classification and never carry semantic meaning.

### B. Verse citation grouping

Consecutive paragraphs whose class belongs to `Tibetan-Citations-in-Verse_*`
(First-Line, Middle-Lines, Last-Line) must be **collected into a single
`[!lung]` callout** — one callout per logical verse stanza, not one per line.

```python
if p_role == 'verse':
    verse_lines = []
    j = i
    while j < len(paragraphs) and resolve_role(...paragraphs[j]...) == 'verse':
        verse_lines.append(paragraphs[j].get_text().strip())
        j += 1
    md += wrap_callout('lung', '\n'.join(verse_lines))
    i = j
    continue
```

Emitting one callout per paragraph line is wrong — it fragments a single stanza
into separate blocks.

### C. Run-based processing (mixed paragraphs)

When the span co-occurrence check reveals mixed content, the converter **must**
walk each `<p>` child-by-child instead of calling `get_text()`:

```
For each child node of <p>:
  - NavigableString  → inherits paragraph's role
  - <br>             → append '\n' to current run
  - <span>           → resolve span's own classes first;
                       fall back to paragraph's role if span has no semantic class

Group consecutive children with the same effective role into a run.
Emit each run as its own block (callout or plain text).
```

The span role resolution strips utility classes (`_idGenCharOverride-1` etc.)
before checking against the semantic class sets.

Reference implementation: `lekphi.py → extract_runs()`.

#### Common mixed patterns and how to handle them

| `p` class | inline `span` class | Meaning | Emit |
|---|---|---|---|
| `Tibetan-Regular-Indented` | `Tibetan-Sabche` | Outline label opening commentary | `[!sabche]` then plain |
| `Tibetan-Commentary-Non-Indent` | `Tibetan-External-Citations` | Inline prose citation mid-commentary | plain + `[!lung]` + plain |
| `Tibetan-Sabche` | `Tibetan-Sabche` | Pure sabche (single class, no split needed) | `[!sabche]` |
| `Tibetan-Citations-in-Verse_*` | `Tibetan-External-Citations` | Verse content in span (normal) | plain span text |

### D. Root-text marker conversion (`༷` U+0F37)

`༷` (TIBETAN MARK NADA) annotates individual characters within a syllable
to mark that syllable as belonging to the root text being commented upon.
Consecutive marked syllables form a single bold span.

**Tokenise** at tsheg `་`, shad `།`, space, newline (boundary character stays
attached to the preceding token). **Classify** each token (contains `༷` or
not). **Group** consecutive same-class tokens. **Render**:
- Unmarked group → emit as-is, stripping any stray `༷`
- Marked group → ` **text** ` (leading space if preceding text doesn't end
  with space; always trailing space)

```
མེད་པའི་ཕྱིར་ན་འཐད༷་པ༷་བཞི་དང༷་བཅ༷ས་པ༷ར་བྱང་ཆུབ་སེམས་དཔའ་
→ མེད་པའི་ཕྱིར་ན་ **འཐད་པ་** བཞི་ **དང་བཅས་པར་** བྱང་ཆུབ་སེམས་དཔའ་
```

Call `convert_root_markers(text)` inside `emit_run()` so it applies to every
block type. The function is defined in both `lekphi.py` (inline) and
`../root_marker_to_bold.py` (standalone tool). Copy from there, do not
reimplement from scratch.

**Marker codepoint**: `༷` is **U+0F37** (TIBETAN MARK NADA), **not** U+0F17
(TIBETAN ASTROLOGICAL SIGN SGRA GCAN-CHAR RTAGS). Verify with:
```python
hex(ord('༷'))  # → '0xf37'
```

### E. TOC construction

Do **not** use `book.toc` as the sole source for the TOC. `book.toc` reflects
only the epub's NCX/nav structure, which can omit inline structural labels
(sa bcad labels that appear as span content inside commentary paragraphs).

**Correct approach**: collect every `[!sabche]` label emitted during body
processing in document order, then build the TOC from that list. This ensures
the TOC matches the body exactly.

```python
# In process_body(), when emitting a sabche run:
sabche_labels.append(convert_root_markers(text.strip()))

# After processing all spine documents:
toc_lines = ['- ' + label for label in all_sabche_labels]
toc_block = '## TOC heading\n\n' + '\n'.join(toc_lines) + '\n\n---\n\n'
```

---

## Publisher patterns

### LEK-PHI series — `lekphi.py`

**Source**: LEK-PHI-126, Khenpo Kunzang Palden, *The Nectar of Manjushri's
Speech* (EPUB, 2017, no publisher field in OPF metadata)

**CSS class inventory**:

| Class | Colour | Count (main doc) | Role |
|---|---|---|---|
| `Tibetan-Sabche` | #005e7f (blue) | 197 p + 215 inline spans | `[!sabche]` |
| `Tibetan-Sabche-After-Title-Chapter` | #005e7f (blue) | 1 | `[!sabche]` |
| `Tibetan-Commentary-Non-Indent` | #343233 (dark) | 200 | plain text |
| `Tibetan-Regular-Indented` | #343233 (dark) | 83 | plain text (may contain mixed spans) |
| `Tibetan-External-Citations` | #897335 (gold) | 23 inline spans | `[!lung]` |
| `Tibetan-Citations-in-Verse_*-First-Line` | #897335 (gold) | 4 | verse group → `[!lung]` |
| `Tibetan-Citations-in-Verse_*-Middle-Lines` | #897335 (gold) | 8 | verse group → `[!lung]` |
| `Tibetan-Citations-in-Verse_*-Last-Line` | #897335 (gold) | 4 | verse group → `[!lung]` |
| `Tibetan-Chapter` | #343233 (dark) | 1 | `#` H1 heading |
| `Tibetan-Sub-Chapter` | #343233 (dark) | 1 | `##` H2 heading |
| `Credits-Page_*` / `Front-*` | #343233 (dark) | — | skip |

**Spine**: `cover.xhtml` (skip), `LEK-PHI-126.xhtml` (skip — credits),
`LEK-PHI-126-1.xhtml` (chapter title), `LEK-PHI-126-2.xhtml` (full body)

**Mixed paragraph patterns found** (confirmed by span co-occurrence check):

```
p=('Tibetan-Regular-Indented',) span=('Tibetan-Sabche',)              n=14
p=('Tibetan-Regular-Indented',) span=('Tibetan-Commentary',)          n=90
p=('Tibetan-Commentary-Non-Indent',) span=('Tibetan-Commentary',)     n=204
p=('Tibetan-Regular-Indented',) span=('Tibetan-External-Citations',)  n=4
p=('Tibetan-Commentary-Non-Indent',) span=('Tibetan-External-Citations',) n=3
```

**Output stats (verified)**:
- TOC entries: 211 (198 epub TOC + 13 inline sabche labels missed by book.toc)
- `[!sabche]` callouts: 211
- `[!lung]` callouts: 11 (4 verse groups + 7 inline prose citations)
- Root marker bold spans: 11,545
- Remaining `༷` in output: 0

---

## Bug log

> Append every bug found and fixed. Include: symptom, root cause, fix.

---

### BUG-001 — Inspector reported `mixed_class_patterns: []` but mixed spans existed

**Symptom**: First converter draft used paragraph-level `get_text()`.
Output had 198 sabche callouts instead of 211. Inline labels like
`གཉིས་པ་སློབ་དཔོན་དགྲ་བཅོམ་པས་` were silently merged into plain text.

**Root cause**: `epub_inspector.py` detects mixed patterns by comparing raw
class name strings. Spans with utility suffix classes
(`Tibetan-Sabche _idGenCharOverride-1`) don't match the paragraph's class
string exactly, so the inspector reports no mixed patterns even though
13 paragraphs contain inline sabche spans and 7 contain inline citation spans.

**Fix**: Always run the span co-occurrence check (see Universal checklist §2).
Switch to run-based processing (`extract_runs()`) for any epub where the
check returns rows.

---

### BUG-002 — TOC missing 13 entries (inline sabche labels)

**Symptom**: `book.toc` had 198 entries; 13 structural labels that appear
as inline spans inside `Tibetan-Regular-Indented` paragraphs were absent.

**Root cause**: `book.toc` is built from the epub's NCX/nav, which only
anchors to top-level paragraph IDs. Inline span content is invisible to it.

**Fix**: Build the TOC by collecting every sabche label emitted during body
processing in document order (see Algorithm §E). `book.toc` is still useful
for href→anchor mapping if Obsidian block links are needed later.

---

### BUG-003 — Root marker codepoint confusion (U+0F17 vs U+0F37)

**Symptom**: First attempt at marker detection used `MARKER = '༗'`
(TIBETAN ASTROLOGICAL SIGN SGRA GCAN-CHAR RTAGS). Marker count was 0.

**Root cause**: The actual marker character in this epub is `༷` **U+0F37**
(TIBETAN MARK NADA). U+0F17 is a visually similar but different character.

**Fix**: Always verify the actual codepoint before hardcoding:
```python
for ch in sample_text:
    if 0x0F00 <= ord(ch) <= 0x0FFF and ch not in known_tibetan_chars:
        print(hex(ord(ch)), repr(ch))
```

---

### BUG-004 — Verse citations emitted as one callout per line

**Symptom**: Each of the 16 verse citation paragraphs (4 First-Line + 8
Middle + 4 Last-Line) was emitted as a separate `[!lung]` block, producing
16 single-line callouts instead of 4 complete verse stanzas.

**Root cause**: Initial `process_body()` iterated paragraphs one at a time
without lookahead, emitting a callout for each `Tibetan-Citations-in-Verse_*`
paragraph individually.

**Fix**: On encountering the first verse paragraph, consume all consecutive
verse paragraphs in a while loop and emit a single joined callout (see
Algorithm §B).

---

## Design decisions

> Append rationale for non-obvious choices.

---

### DD-001 — Run-based processing vs. paragraph-level get_text()

`get_text()` on a mixed paragraph loses all span-level semantic information.
Run-based processing has more code but is the only correct approach when
any `(p_class, span_class)` co-occurrence row exists. The cost is worth it
even for epubs where most paragraphs are homogeneous.

### DD-002 — Callout type `sabche` (not `toc`)

Tibetan *sa bcad* (ས་བཅད་) labels are structural outline markers — the
equivalent of section headings in prose form. They are not literally a
"table of contents" entry, so `[!sabche]` is semantically clearer than
`[!toc]`. Obsidian renders unknown callout types gracefully.

### DD-003 — TOC from body scan, not book.toc

See BUG-002. `book.toc` is still read and can be used for href→anchor
mapping (e.g. Obsidian block links), but must not be the sole source for
the document TOC.

### DD-004 — Trailing space after bold `**` groups

Markdown parsers (including Obsidian) require whitespace around `**...**`
to treat it as bold when adjacent to Tibetan script, which has no natural
word-boundary characters. The trailing space is added unconditionally;
the leading space is added only when the preceding text does not already
end with a space, to avoid double spaces.

### DD-005 — `convert_root_markers()` called in `emit_run()`, not post-hoc

Applying the conversion inside `emit_run()` means it runs on the raw
extracted text before callout wrapping, so it correctly handles multi-line
verse content split across `\n` within a single run. A line-by-line
post-processor on the final MD file also works (see `root_marker_to_bold.py`)
but is less reliable for multiline callout content.
