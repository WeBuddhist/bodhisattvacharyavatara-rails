#!/usr/bin/env python3
"""
Converter: NTZ Commentary (སྤྱོད་འཇུག་གི་འགྲེལ་པ་ལེགས་བཤད་རྒྱ་མཚོ)
Generated: 2026-06-30

Publisher: Unknown (InDesign-generated epub, no publisher in OPF)

CSS class -> wiki markup mapping:
  CharOverride-1  (no colour, font-only)           -> plain text (commentary body)
  CharOverride-2  (red    #ff0000)                  -> [[root|text]]  (root text)
  CharOverride-3  (blue   #0070c0)                  -> [[toc|text]]   (sa bcad / structural)
  CharOverride-4  (green  #00b050)                  -> [[toc|text]]   (sa bcad variant)
  CharOverride-5  (blue   #0070c0)                  -> [[toc|text]]   (same as 3)
  CharOverride-6  (gold   #ffc000)                  -> [[quote|text]] (scriptural citation)
  CharOverride-7  (subscript, font-size:0.848em)    -> plain text (footnote markers)
  CharOverride-8  (red    #ff0000)                  -> [[root|text]]  (same as 2)
  Chapter         (black)                           -> # heading
  Normal          (black)                           -> paragraph container
  Normal ParaOverride-2                             -> paragraph container (indented)

TOC:
  Built from every [[toc|…]] block emitted during body processing, in
  document order. The epub's nav TOC is chapter-level only.
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

UTILITY_CLASSES = {'_idGenCharOverride-1', '_idGenParaOverride-1',
                   'ParaOverride-1', 'ParaOverride-2'}

ROOT_CLASSES = {'CharOverride-2', 'CharOverride-8'}
TOC_CLASSES = {'CharOverride-3', 'CharOverride-4', 'CharOverride-5'}
QUOTE_CLASSES = {'CharOverride-6'}
CHAPTER_CLASSES = {'Chapter'}
PLAIN_CLASSES = {'CharOverride-1', 'CharOverride-7', 'Normal'}

SKIP_DOCS = {'cover.xhtml'}


def semantic_classes(element):
    """Return meaningful CSS classes, stripping utility-only classes."""
    return {c for c in element.get('class', []) if c not in UTILITY_CLASSES}


def resolve_role(cls_set):
    """
    Map a set of CSS classes to a semantic role string.
    Returns: 'toc', 'root', 'lung', 'chapter', 'plain', or None.
    """
    if not cls_set:
        return None
    if cls_set & CHAPTER_CLASSES:
        return 'chapter'
    if cls_set & ROOT_CLASSES:
        return 'root'
    if cls_set & TOC_CLASSES:
        return 'toc'
    if cls_set & QUOTE_CLASSES:
        return 'lung'
    if cls_set & PLAIN_CLASSES:
        return 'plain'
    # Default: Normal paragraph with no overrides
    return 'plain'


# ---------------------------------------------------------------------------
# Run extraction (run-based span processing)
# ---------------------------------------------------------------------------

def extract_runs(p_element):
    """
    Walk a <p> element's direct children and return a list of (role, text) pairs.
    Consecutive content with the same effective role is merged into one run.
    Role priority: span's own classes > paragraph's classes.
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
# Callout / block formatting
# ---------------------------------------------------------------------------

def wrap_callout(callout_type, text):
    text = text.strip()
    return '[[' + callout_type + '|' + text + ']]\n\n'


def emit_run(role, text):
    """Emit one run as the appropriate Markdown block."""
    text = text.strip()
    if not text:
        return ''
    if role == 'toc':
        return wrap_callout('toc', text)
    if role == 'root':
        return wrap_callout('root', text)
    if role == 'lung':
        return wrap_callout('quote', text)
    return text + '\n\n'


# ---------------------------------------------------------------------------
# Metadata
# ---------------------------------------------------------------------------

def dc(book, key):
    raw = book.get_metadata('DC', key)
    return raw[0][0] if raw else None


def extract_metadata(book):
    source_id = None
    for val, attrs in book.get_metadata('DC', 'identifier') or []:
        if 'uuid' in str(val).lower() or 'urn' in str(val).lower():
            source_id = val
            break

    return {
        'title': dc(book, 'title') or 'Unknown Title',
        'title_en': 'The Ocean of Excellent Explanation: A Commentary on the Bodhisattvacaryavatara',
        'author': 'དངུལ་ཆུ་ཐོགས་མེད་བཟང་པོ',
        'author_en': 'Ngulchu Thogme Zangpo',
        'language': 'bo',
        'date': dc(book, 'date'),
        'source_id': source_id,
        'source_description': 'Extracted from EPUB (NTZ_com.epub)',
    }


# ---------------------------------------------------------------------------
# Document processing
# ---------------------------------------------------------------------------

def process_body(body):
    """
    Walk all elements in the body, emit Markdown via run-based extraction.
    Returns (md_text, toc_labels).
    """
    paragraphs = body.find_all(['p', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6'])
    md = ''
    toc_labels = []
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

        if p_role == 'chapter':
            text = el.get_text().strip()
            if text:
                md += '## ' + text + '\n\n'
            i += 1
            continue

        # General paragraph: run-based extraction
        runs = extract_runs(el)
        for idx, (role, text) in enumerate(runs):
            if role == 'toc':
                toc_labels.append(text.strip())
            block = emit_run(role, text)
            # If more runs follow, strip trailing newlines so next run
            # continues on same line (e.g. [[toc|…]]plain text)
            if idx < len(runs) - 1:
                block = block.rstrip('\n')
            md += block

        i += 1

    return md, toc_labels


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
    frontmatter = '---\n' + yaml.dump(metadata, allow_unicode=True, sort_keys=False) + '---\n\n'

    body_md = ''
    all_toc_labels = []

    for item_id, linear in book.spine:
        item = book.get_item_with_id(item_id)
        if not item or item.get_type() != ebooklib.ITEM_DOCUMENT:
            continue

        fname = item.get_name().split('/')[-1]
        if fname in SKIP_DOCS:
            continue

        soup = BeautifulSoup(item.get_content(), 'html.parser')
        for t in soup(['script', 'style']):
            t.decompose()
        body_el = soup.find('body')
        if not body_el:
            continue

        doc_md, doc_labels = process_body(body_el)
        body_md += doc_md
        all_toc_labels.extend(doc_labels)

    # Build TOC from toc labels found in the body
    toc_lines = ['- ' + label for label in all_toc_labels]
    toc_block = '## དཀར་ཆག / Table of Contents\n\n' + '\n'.join(toc_lines) + '\n\n---\n\n'

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(frontmatter + toc_block + body_md)
    print('Successfully extracted to ' + output_path)
    print(f'TOC entries: {len(all_toc_labels)}')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='EPUB to Markdown - NTZ Commentary')
    parser.add_argument('epub_path', help='Path to the source EPUB file')
    parser.add_argument('output_path', help='Path to the output Markdown file')
    args = parser.parse_args()
    convert_epub_to_markdown(args.epub_path, args.output_path)
