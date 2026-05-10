# EPUB to Markdown Extraction Skill

This skill converts EPUB files to structured Markdown. It is **adaptive**: for each new epub it first inspects the epub's internal structure, then either reuses an existing publisher-specific converter or generates a new one tailored to that epub's conventions.

---

## Workflow Overview

```
epub file
   │
   ▼
Step 1: Inspect ──► profile JSON
   │
   ▼
Step 2: Check converters/ for matching publisher slug
   │
   ├─ Found ──► Step 4: Run existing converter
   │
   └─ Not found ──► Step 3: Generate new converter ──► Step 4: Run it
                                                           │
                                                           ▼
                                                    Step 5: Review output
```

---

## Step 1 — Inspect the EPUB

Run the inspector to extract a full structural profile of the epub:

```bash
python 4-SYSTEM/Skills/epub-to-markdown/epub_inspector.py path/to/source.epub
```

The inspector outputs JSON containing:
- `publisher` / `publisher_slug` — identifies which converter to use
- `title`, `title_en`, `author`, `language`, `date`, `source_id` — all available metadata
- `css_classes` — every CSS class found in stylesheets, with its colour value, element count, and sample text from the epub
- `heading_colors` — colour values assigned to h1–h6 in CSS
- `toc` — structured table of contents
- `spine_docs` — ordered list of content documents

Read the profile carefully. Pay attention to:

- **`css_classes`**: which classes carry colour values and what the samples suggest about their semantic role (root text, citation, TOC label, etc.)
- **`heading_colors`**: whether heading colours share values with class colours (usually means same semantic role)
- **`mixed_class_patterns`**: if this list is non-empty, the epub uses sub-paragraph colour coding. **However, `mixed_class_patterns` can be empty even when inline spans carry semantic classes** — the inspector only detects patterns where the span class name differs from the paragraph class name, and it may miss utility-suffixed classes like `Tibetan-Sabche _idGenCharOverride-1`. **Always run the span co-occurrence check below regardless of what `mixed_class_patterns` reports.**

**Mandatory inline-span check (run this after every inspection):**

```bash
python3 -c "
from bs4 import BeautifulSoup
from collections import Counter
import zipfile, os, sys

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
        print(f'p={pc} span={sc}: {n}')
" path/to/source.epub
```

Any `(p_class, span_class)` pair where they differ is a mixed-content paragraph requiring run-based processing. Common patterns and how to handle them:

  - `<p class=plain> contains <span class=sabche>` — inline outline label at the start of a commentary paragraph. Split into `[!sabche]` for the label + plain text for the rest.
  - `<p class=plain> contains <span class=lung>` — prose citation embedded mid-commentary. Split into plain + `[!lung]` + plain (or plain + `[!lung]` if citation is at the end).
  - `<p class=lung> contains <span class=plain>` — citation paragraph with a trailing connective phrase (`ཞེས་དང༌།`, `ཞེས་སོ།།`) reverting to plain. Emit the citation body as `[!lung]`, then the connective as plain text.
  - `<p class=plain> contains <span class=bold>` — outline label at the start of a commentary paragraph. Split into `[!toc]` for the label + plain text for the rest.

**If any mixed patterns are found**, the converter must use a run-based approach: walk each `<p>`'s children one by one, resolve each span's effective semantic class (span class takes priority over paragraph class, utility classes like `_idGenCharOverride-1` are stripped), group consecutive same-class content into runs, and emit each run as its own block. See `converters/lekphi.py` for a complete reference implementation of this pattern.

---

## Step 2 — Check for an Existing Converter

Look in `4-SYSTEM/Skills/epub-to-markdown/converters/` for a file named `<publisher_slug>.py` (where `publisher_slug` comes from the inspector output).

**If a matching converter exists:** skip to Step 4.

**If no converter exists:** proceed to Step 3.

---

## Step 3 — Generate a Custom Converter

Using the profile from Step 1, write a new Python script at:

```
4-SYSTEM/Skills/epub-to-markdown/converters/<publisher_slug>.py
```

The script must follow the same interface as `epub_to_markdown.py`:

```bash
python converters/<publisher_slug>.py path/to/source.epub path/to/output.md
```

### What to customise in the generated script

**3.1 Metadata frontmatter**
Include every meaningful field the inspector found. Common additions beyond the generic script:
- `publisher` (always add if present)
- `title_en` (if `calibre:title_sort` contains an English title)
- `source_id` (the epub UUID/URN — useful for stable referencing)
- Any other OPF meta fields with obvious meaning

**3.2 CSS class → callout mapping**
For each CSS class with a non-black colour and meaningful element count:
1. Look at the colour value and sample texts together
2. Assign a descriptive `callout_type` string that names the semantic role (e.g. `root`, `lung`, `toc`, `verse`, `citation`, `commentary`, `note`, `heading-enum`)
3. Implement this in `get_color_class()` and route through `wrap_callout()`

Use this colour interpretation heuristic as a starting point:
- **Red / orange tones** → root text, verse, primary source
- **Gold / olive / amber tones** → scriptural citation, lung, canonical quote
- **Blue tones** (on paragraphs, not headings) → structural enumeration, TOC item
- **Green tones** → commentary note, gloss
- **Black (#000000)** → ordinary body text, no callout needed

If a class appears fewer than 5 times or its samples look like purely structural/decorative content (logos, credits), skip it.

**3.3 TOC injection**
If the epub has a meaningful TOC (more than just a cover + one section), inject a Markdown TOC block at the top of the output, after the frontmatter:

```markdown
## Table of Contents
- Chapter title → [[#anchor]]
  - Sub-entry
```

Use the `toc` array from the inspector to build this. Derive anchors from the `href` filename (e.g. `Chapter0001.xhtml` → `chapter-1`).

**3.4 Chapter separators**
If the spine has clearly named chapter documents (e.g. `Chapter0001.xhtml`, `Chapter0002.xhtml`), insert a horizontal rule (`---`) and an H2 chapter heading between spine documents, using the TOC title for that document if available.

**3.5 Additional metadata**
If `title_en` is present and differs from `title`, include it in the frontmatter as `title_en`.

### Script template

Base the generated script on `epub_to_markdown.py` — copy its structure and extend it. Do not start from scratch. Key functions to modify:
- `extract_metadata()` — add publisher, title_en, source_id, etc.
- `get_color_class()` — map this epub's specific classes
- `convert_epub_to_markdown()` — add TOC injection and chapter separators if applicable

Write a docstring at the top of the generated script explaining:
- Publisher name
- Date generated
- What each callout type means for this publisher

---

## Step 4 — Run the Converter

```bash
python 4-SYSTEM/Skills/epub-to-markdown/converters/<publisher_slug>.py \
  path/to/source.epub \
  path/to/output.md
```

The output file should be placed in `0-INBOX/md-texts/`.

---

## Step 5 — Post-Extraction Review

### 5.1 Metadata
Verify the YAML frontmatter is accurate and complete. Check that `title`, `author`, `publisher`, and `language` are correct.

### 5.2 Callout blocks
Spot-check that coloured blocks were correctly identified:
- Sample several `> [!root]`, `> [!lung]` etc. blocks and confirm they match the expected content type
- If callout blocks are absent but should be present, re-inspect the CSS (open the `.epub` as a zip and look at the stylesheet directly)

### 5.3 Structure
- Confirm chapter headings appear at the right places
- Check that the TOC (if injected) links resolve within the document
- Look for encoding artefacts, especially in Tibetan or other non-Latin scripts

---

## Reference Files

| File | Purpose |
|---|---|
| `epub_inspector.py` | Analyses any epub and outputs a JSON profile |
| `epub_to_markdown.py` | Generic fallback converter (also serves as the template) |
| `converters/<publisher_slug>.py` | Publisher-specific converters (generated and cached) |

---

## Limitations

- **Images**: Only text is extracted; image files are not copied.
- **Complex tables**: May be flattened or stripped; manual reconstruction may be needed.
- **CSS layouts**: Multi-column or sidebar layouts are linearised.
- **Inline colour spans**: Fully supported via run-based processing when the mandatory span co-occurrence check (Step 1) detects mixed patterns. Converters that pre-date this check (using paragraph-level `get_text()` only) will miss inline spans and must be regenerated.
