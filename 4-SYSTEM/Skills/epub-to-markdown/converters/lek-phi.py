#!/usr/bin/env python3
"""
Converter: LEK-PHI series (no publisher metadata)
Generated: 2026-05-10
Author: མཁན་པོ་ཀུན་དཔལ། (Khenpo Kunzang Palden)
Series ID pattern: LEK-PHI-NNN

CSS class -> callout mapping:
  Tibetan-Sabche (#005e7f, teal/blue)          -> > [!toc]   Structural outline labels (sa-bcad)
  Tibetan-Sabche-After-Title-Chapter (#005e7f) -> > [!toc]   Same, post-chapter title
  Tibetan-External-Citations (#897335, gold)   -> > [!lung]  Scriptural citations
  Tibetan-Citations-in-Verse_* (#897335, gold) -> > [!lung]  Verse citation lines (merged)
  Tibetan-Commentary (#343233, near-black)     -> plain text  Main commentary
  Tibetan-Commentary-Non-Indent (#343233)      -> plain text  Unindented commentary
  Tibetan-Regular-Indented (#343233)           -> plain text  Indented commentary
  Tibetan-Chapter (#343233)                    -> ## heading  Chapter heading
  Tibetan-Sub-Chapter (#343233)                -> ## heading  Sub-chapter heading

Note: Consecutive paragraphs belonging to the same callout type are merged into a single
callout block. This is especially relevant for verse citations split into
First-Line / Middle-Lines / Last-Line class variants.
"""

import argparse
import re
import ebooklib
from ebooklib import epub
from bs4 import BeautifulSoup
import yaml


# ---------------------------------------------------------------------------
# Class -> callout type
# ---------------------------------------------------------------------------

LUNG_CLASSES = {
    'Tibetan-External-Citations',
    'Tibetan-Citations-in-Verse_Tibetan-Citations-First-Line',
    'Tibetan-Citations-in-Verse_Tibetan-Citations-Middle-Lines',
    'Tibetan-Citations-in-Verse_Tibetan-Citations-Last-Line',
}

TOC_CLASSES = {
    'Tibetan-Sabche',
    'Tibetan-Sabche-After-Title-Chapter',
}

HEADING_CLASSES = {
    'Tibetan-Chapter',
    'Tibetan-Sub-Chapter',
    'Tibetan-Chapters',
}

FRONT_MATTER_DOCS = {'cover.xhtml', 'LEK-PHI-126.xhtml'}


def get_callout_type(element):
    classes = set(element.get('class', []))
    if classes & LUNG_CLASSES:
        return 'lung'
    if classes & TOC_CLASSES:
        return 'toc'
    if classes & HEADING_CLASSES:
        return 'heading'
    return None


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
        if 'BookId' in str(attrs.get('id', '')):
            source_id = val
            break
    if not source_id:
        ids = book.get_metadata('DC', 'identifier')
        if ids:
            source_id = ids[0][0]
    d = {
        'title': dc(book, 'title') or 'Unknown Title',
        'author': dc(book, 'creator') or 'Unknown Author',
        'language': dc(book, 'language') or 'bo',
        'date': dc(book, 'date'),
        'source_description': 'Extracted from EPUB (LEK-PHI series)',
    }
    title_en = meta.get('calibre:title_sort')
    if title_en and title_en != d['title']:
        d['title_en'] = title_en
    if source_id:
        d['source_id'] = source_id
    return d


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
    return '## དཀར་ཆག / Table of Contents\n\n' + '\n'.join(lines) + '\n\n---\n\n'


def build_chapter_map(book):
    chapter_map = {}
    def walk(toc):
        for entry in toc:
            if isinstance(entry, epub.Link):
                fname = entry.href.split('#')[0].split('/')[-1]
                if fname not in chapter_map:
                    chapter_map[fname] = entry.title or ''
            elif isinstance(entry, tuple):
                section, children = entry
                if hasattr(section, 'href') and section.href:
                    fname = section.href.split('#')[0].split('/')[-1]
                    if fname not in chapter_map:
                        chapter_map[fname] = section.title or ''
                walk(children)
    walk(book.toc)
    return chapter_map


# ---------------------------------------------------------------------------
# Block rendering with consecutive-merge
# ---------------------------------------------------------------------------

def wrap_callout(callout_type, lines_list):
    """Render a list of text lines as a single callout block."""
    body_lines = []
    for text in lines_list:
        text = re.sub(r'\n{2,}', '\n', text.strip())
        for line in text.split('\n'):
            line = line.strip()
            if line:
                body_lines.append('> ' + line)
    if not body_lines:
        return ''
    return '> [!' + callout_type + ']\n' + '\n'.join(body_lines) + '\n\n'


def flush_pending(pending_type, pending_texts):
    if not pending_type or not pending_texts:
        return ''
    return wrap_callout(pending_type, pending_texts)


def process_body(body):
    """
    Walk all top-level elements in a body, merging consecutive same-type callout
    paragraphs into a single block (important for verse citations split across elements).
    """
    md = ''
    pending_type = None
    pending_texts = []

    for element in body.find_all(recursive=False):
        tag = element.name

        # Headings
        if tag in ['h1', 'h2', 'h3', 'h4', 'h5', 'h6']:
            md += flush_pending(pending_type, pending_texts)
            pending_type, pending_texts = None, []
            level = int(tag[1])
            md += '#' * level + ' ' + element.get_text().strip() + '\n\n'
            continue

        if tag == 'p':
            callout = get_callout_type(element)
            text = element.get_text().strip()
            if not text:
                continue

            # Heading-class paragraphs
            if callout == 'heading':
                md += flush_pending(pending_type, pending_texts)
                pending_type, pending_texts = None, []
                md += '## ' + text + '\n\n'
                continue

            # Callout paragraph
            if callout in ('lung', 'toc'):
                if callout == pending_type:
                    # Merge with ongoing block
                    pending_texts.append(text)
                else:
                    md += flush_pending(pending_type, pending_texts)
                    pending_type = callout
                    pending_texts = [text]
                continue

            # Plain paragraph
            md += flush_pending(pending_type, pending_texts)
            pending_type, pending_texts = None, []
            md += text + '\n\n'
            continue

        if tag == 'ul':
            md += flush_pending(pending_type, pending_texts)
            pending_type, pending_texts = None, []
            for li in element.find_all('li', recursive=False):
                md += '- ' + li.get_text().strip() + '\n'
            md += '\n'
            continue

        if tag == 'ol':
            md += flush_pending(pending_type, pending_texts)
            pending_type, pending_texts = None, []
            for i, li in enumerate(element.find_all('li', recursive=False), 1):
                md += str(i) + '. ' + li.get_text().strip() + '\n'
            md += '\n'
            continue

        if tag == 'blockquote':
            md += flush_pending(pending_type, pending_texts)
            pending_type, pending_texts = None, []
            lines = element.get_text().strip().split('\n')
            md += '\n'.join('> ' + l for l in lines) + '\n\n'
            continue

    md += flush_pending(pending_type, pending_texts)
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

    chapter_map = build_chapter_map(book)

    for item_id, linear in book.spine:
        item = book.get_item_with_id(item_id)
        if not item or item.get_type() != ebooklib.ITEM_DOCUMENT:
            continue

        fname = item.get_name().split('/')[-1]
        if fname in FRONT_MATTER_DOCS:
            continue

        ch_title = chapter_map.get(fname, '')
        md += '\n---\n\n'
        if ch_title:
            md += '## ' + ch_title + '\n\n'

        soup = BeautifulSoup(item.get_content(), 'html.parser')
        for t in soup(['script', 'style']):
            t.decompose()
        body = soup.find('body')
        if not body:
            continue

        # Content may be wrapped in a single div — unwrap if so
        direct = list(body.find_all(recursive=False))
        container = direct[0] if len(direct) == 1 and direct[0].name == 'div' else body
        md += process_body(container)

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(md)
    print('Successfully extracted content to ' + output_path)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='EPUB to Markdown - LEK-PHI series')
    parser.add_argument('epub_path', help='Path to the source EPUB file')
    parser.add_argument('output_path', help='Path to the output Markdown file')
    args = parser.parse_args()
    convert_epub_to_markdown(args.epub_path, args.output_path)
