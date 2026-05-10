#!/usr/bin/env python3
"""
Converter: LEK-PHI Series (Khenpo Kunzang Palden / similar Tibetan commentaries)
Generated: 2026-05-10
Updated:   2026-05-10 — run-based span processing to capture inline colour-coded spans

Publisher: Unknown (publisher field absent from OPF metadata)

CSS class -> callout mapping:
  Paragraph-level (paragraph own class determines role when no overriding span):
    Tibetan-Sabche / Tibetan-Sabche-After-Title-Chapter  (blue  #005e7f) -> [!sabche]
    Tibetan-External-Citations                           (gold  #897335) -> [!lung]
    Tibetan-Citations-in-Verse_*                         (gold  #897335) -> grouped [!lung]
    Tibetan-Commentary / Non-Indent / Regular-Indented   (dark  #343233) -> plain text
    Tibetan-Chapter                                      (dark  #343233) -> # heading
    Tibetan-Sub-Chapter                                  (dark  #343233) -> ## heading
    Credits-Page_* / Front-*                                             -> skipped

  Inline span override (span class takes precedence over paragraph class):
    Tibetan-Sabche            inside any paragraph -> emit as [!sabche] run
    Tibetan-External-Citations inside any paragraph -> emit as [!lung] run
    Tibetan-Commentary         inside any paragraph -> emit as plain-text run
    _idGenCharOverride-1       utility class -- always ignored

  Mixed-paragraph patterns observed in this epub:
    <p class="Tibetan-Regular-Indented">
        <span class="Tibetan-Sabche _idGenCharOverride-1">outline label</span>
        <span class="Tibetan-Commentary _idGenCharOverride-1">commentary body</span>
    </p>
    -> [!sabche] block + plain-text block

    <p class="Tibetan-Commentary-Non-Indent">
        <span class="Tibetan-Commentary">...las. </span>
        <span class="Tibetan-External-Citations">citation verse</span>
        <span class="Tibetan-Commentary">zhes...</span>
    </p>
    -> plain block + [!lung] block + plain block

Processing approach -- run-based (not paragraph-level):
  Each <p> is walked child-by-child. Consecutive spans/text-nodes sharing the
  same effective semantic class are merged into a run. Each run is emitted as
  its own block. This correctly handles all mixed-class paragraphs.
"""

import argparse
import re
import ebooklib
from ebooklib import epub
from bs4 import BeautifulSoup, NavigableString, Tag
import yaml


# ---------------------------------------------------------------------------
# Semantic class resolution
# ---------------------------------------------------------------------------

UTILITY_CLASSES = {'_idGenCharOverride-1', '_idGenParaOverride-1'}

SABCHE_CLASSES = {
    'Tibetan-Sabche',
    'Tibetan-Sabche-After-Title-Chapter',
}

VERSE_CITATION_CLASSES = {
    'Tibetan-Citations-in-Verse_Tibetan-Citations-First-Line',
    'Tibetan-Citations-in-Verse_Tibetan-Citations-Middle-Lines',
    'Tibetan-Citations-in-Verse_Tibetan-Citations-Last-Line',
}

PROSE_CITATION_CLASSES = {'Tibetan-External-Citations'}
CHAPTER_CLASSES = {'Tibetan-Chapter'}
SUBCHAPTER_CLASSES = {'Tibetan-Sub-Chapter'}

SKIP_CLASSES = {
    'Credits-Page_Front-Page---Text-Author',
    'Credits-Page_Front-Title',
    'Front-Page---Text-Titles',
    'Front-Title',
    'Partners-Line',
}

FRONT_MATTER_DOCS = {'cover.xhtml', 'LEK-PHI-126.xhtml'}


def semantic_classes(element):
    """Return meaningful CSS classes, stripping utility-only classes."""
    return {c for c in element.get('class', []) if c not in UTILITY_CLASSES}


def resolve_role(cls_set):
    """
    Map a set of CSS classes to a semantic role string.
    Returns one of: 'sabche', 'lung', 'verse', 'plain', 'chapter', 'subchapter', 'skip', or None.
    None means no semantic opinion (inherit from context).
    """
    if not cls_set:
        return None
    if cls_set & SKIP_CLASSES:
        return 'skip'
    if cls_set & CHAPTER_CLASSES:
        return 'chapter'
    if cls_set & SUBCHAPTER_CLASSES:
        return 'subchapter'
    if cls_set & SABCHE_CLASSES:
        return 'sabche'
    if cls_set & PROSE_CITATION_CLASSES:
        return 'lung'
    if cls_set & VERSE_CITATION_CLASSES:
        return 'verse'
    return 'plain'


# ---------------------------------------------------------------------------
# Run extraction
# ---------------------------------------------------------------------------

def extract_runs(p_element):
    """
    Walk a <p> element's direct children and return a list of (role, text) pairs.
    Consecutive content with the same effective role is merged into one run.

    Role priority: span's own classes > paragraph's classes.
    Bare NavigableString nodes inherit the paragraph's role.
    """
    p_role = resolve_role(semantic_classes(p_element)) or 'plain'

    runs = []
    cur_role = None
    cur_parts = []

    def flush():
        if cur_parts:
            text = ''.join(cur_parts).strip()
            if text:
                runs.append((cur_role, text))

    for child in p_element.children:
        if isinstance(child, NavigableString):
            text = str(child)
            if not text.strip():
                continue
            role = p_role
            if role == cur_role:
                cur_parts.append(text)
            else:
                flush()
                cur_role = role
                cur_parts = [text]

        elif isinstance(child, Tag):
            if child.name == 'br':
                cur_parts.append('\n')
                continue

            span_role = resolve_role(semantic_classes(child))
            role = span_role if span_role is not None else p_role

            # Collect inner text (handling nested br tags)
            inner = []
            for sub in child.descendants:
                if isinstance(sub, NavigableString):
                    inner.append(str(sub))
                elif isinstance(sub, Tag) and sub.name == 'br':
                    inner.append('\n')
            text = ''.join(inner)
            if not text.strip():
                continue

            if role == cur_role:
                cur_parts.append(text)
            else:
                flush()
                cur_role = role
                cur_parts = [text]

    flush()
    return runs


# ---------------------------------------------------------------------------
# Callout formatting
# ---------------------------------------------------------------------------

def wrap_callout(callout_type, text):
    text = text.strip()
    lines = [l.rstrip() for l in text.split('\n')]
    body = '\n'.join('> ' + l for l in lines if l)
    return '> [!' + callout_type + ']\n' + body + '\n\n'


def emit_run(role, text):
    """Emit one run as the appropriate Markdown block."""
    text = text.strip()
    if not text:
        return ''
    if role == 'sabche':
        return wrap_callout('sabche', text)
    if role == 'lung':
        return wrap_callout('lung', text)
    return text + '\n\n'


# ---------------------------------------------------------------------------
# Metadata
# ---------------------------------------------------------------------------

def dc(book, key):
    raw = book.get_metadata('DC', key)
    return raw[0][0] if raw else None


def opf_meta(book):
    result = {}
    for val, attrs in book.metadata.get('http://www.idpf.org/2007/opf', {}).get('meta', []):
        name = attrs.get('name') or attrs.get('property')
        content = attrs.get('content') or val
        if name:
            result[name] = content
    return result


def extract_metadata(book):
    meta = opf_meta(book)
    source_id = None
    for val, attrs in book.get_metadata('DC', 'identifier') or []:
        if attrs.get('id') == 'BookId' or 'uuid' in str(val).lower():
            source_id = val
            break
    d = {
        'title': dc(book, 'title') or 'Unknown Title',
        'title_en': "The Nectar of Manjushri's Speech: A Commentary on the Bodhisattvacaryavatara",
        'author': dc(book, 'creator') or 'Unknown Author',
        'author_en': 'Khenpo Kunzang Palden (Khenpo Kunpal)',
        'language': 'bo',
        'date': dc(book, 'date'),
        'source_id': source_id,
        'source_description': 'Extracted from EPUB source (LEK-PHI-126)',
    }
    calibre_sort = meta.get('calibre:title_sort')
    if calibre_sort:
        d['calibre_title_sort'] = calibre_sort
    return {k: v for k, v in d.items() if v is not None}


# ---------------------------------------------------------------------------
# TOC
# ---------------------------------------------------------------------------

def build_toc_md(toc, depth=0):
    lines = []
    for entry in toc:
        if isinstance(entry, epub.Link):
            lines.append('  ' * depth + '- ' + (entry.title or ''))
        elif isinstance(entry, tuple):
            section, children = entry
            title = section.title if hasattr(section, 'title') else ''
            if title:
                lines.append('  ' * depth + '- **' + title + '**')
            lines.extend(build_toc_md(children, depth + 1))
    return lines


def toc_block(book):
    lines = build_toc_md(book.toc)
    if not lines:
        return ''
    return '## dkar chag / Table of Contents\n\n' + '\n'.join(lines) + '\n\n---\n\n'


# ---------------------------------------------------------------------------
# Document processing
# ---------------------------------------------------------------------------

def process_body(body):
    """
    Walk all p elements in the body, emit Markdown via run-based extraction.
    Consecutive verse-citation paragraphs are grouped into a single lung block.
    """
    paragraphs = body.find_all(['p', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6'])
    md = ''
    i = 0
    while i < len(paragraphs):
        el = paragraphs[i]

        # Native heading tags
        if el.name in ('h1', 'h2', 'h3', 'h4', 'h5', 'h6'):
            level = int(el.name[1])
            text = el.get_text().strip()
            if text:
                md += '#' * level + ' ' + text + '\n\n'
            i += 1
            continue

        p_role = resolve_role(semantic_classes(el))

        if p_role == 'skip':
            i += 1
            continue

        if p_role == 'chapter':
            text = el.get_text().strip()
            if text:
                md += '# ' + text + '\n\n'
            i += 1
            continue

        if p_role == 'subchapter':
            text = el.get_text().strip()
            if text:
                md += '## ' + text + '\n\n'
            i += 1
            continue

        # Verse citation: collect consecutive verse paragraphs into one lung block
        if p_role == 'verse':
            verse_lines = []
            j = i
            while j < len(paragraphs):
                if resolve_role(semantic_classes(paragraphs[j])) == 'verse':
                    t = paragraphs[j].get_text().strip()
                    if t:
                        verse_lines.append(t)
                    j += 1
                else:
                    break
            if verse_lines:
                md += wrap_callout('lung', '\n'.join(verse_lines))
            i = j
            continue

        # General paragraph (sabche / lung / plain): run-based extraction
        runs = extract_runs(el)
        for role, text in runs:
            md += emit_run(role, text)

        i += 1

    return md


# ---------------------------------------------------------------------------
# Main conversion
# ---------------------------------------------------------------------------

def convert_epub_to_markdown(epub_path, output_path):
    try:
        book = epub.read_epub(epub_path)
    except Exception as e:
        print('Error reading EPUB: ' + str(e))
        return

    metadata = extract_metadata(book)
    md = '---\n' + yaml.dump(metadata, allow_unicode=True, sort_keys=False) + '---\n\n'
    md += toc_block(book)

    for item_id, linear in book.spine:
        item = book.get_item_with_id(item_id)
        if not item or item.get_type() != ebooklib.ITEM_DOCUMENT:
            continue

        fname = item.get_name().split('/')[-1]
        if fname in FRONT_MATTER_DOCS:
            continue

        soup = BeautifulSoup(item.get_content(), 'html.parser')
        for t in soup(['script', 'style']):
            t.decompose()
        body = soup.find('body')
        if not body:
            continue

        md += process_body(body)

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(md)
    print('Successfully extracted to ' + output_path)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='EPUB to Markdown - LEK-PHI Series')
    parser.add_argument('epub_path', help='Path to the source EPUB file')
    parser.add_argument('output_path', help='Path to the output Markdown file')
    args = parser.parse_args()
    convert_epub_to_markdown(args.epub_path, args.output_path)
