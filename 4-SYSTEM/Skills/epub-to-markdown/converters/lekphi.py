#!/usr/bin/env python3
"""
Converter: LEK-PHI Series (Khenpo Kunzang Palden / similar Tibetan commentaries)
Generated: 2026-05-10
Publisher: Unknown (publisher field absent from OPF metadata)

CSS class -> callout mapping for this epub family:
  Tibetan-Sabche                             (#005e7f blue)  -> > [!sabche]   Outline/structural labels (sa bcad)
  Tibetan-Sabche-After-Title-Chapter         (#005e7f blue)  -> > [!sabche]   Same role, follows chapter title
  Tibetan-External-Citations                 (#897335 gold)  -> > [!lung]     Prose citations from canonical texts
  Tibetan-Citations-in-Verse_*-First-Line    (#897335 gold)  -> verse start   Grouped into a single [!lung] block
  Tibetan-Citations-in-Verse_*-Middle-Lines  (#897335 gold)  -> verse middle  Grouped into a single [!lung] block
  Tibetan-Citations-in-Verse_*-Last-Line     (#897335 gold)  -> verse end     Grouped into a single [!lung] block
  Tibetan-Commentary                         (#343233 dark)  -> plain text    Main commentary body
  Tibetan-Commentary-Non-Indent              (#343233 dark)  -> plain text    Commentary without indent
  Tibetan-Regular-Indented                   (#343233 dark)  -> plain text    Indented body text
  Tibetan-Chapter                            (#343233 dark)  -> # heading     Major chapter/section title
  Tibetan-Sub-Chapter                        (#343233 dark)  -> ## heading    Sub-chapter title
  Tibetan-Chapters                           (#343233 dark)  -> plain text    Chapter label (minor)
  Credits-Page_*                                             -> skipped       Front matter / credits
  Front-*                                                    -> skipped       Front matter / title page

Verse citation grouping:
  Consecutive paragraphs with Tibetan-Citations-in-Verse_* classes are collected
  and emitted together as a single [!lung] callout block, preserving line breaks.

No mixed_class_patterns found in this epub — paragraph-level classification is sufficient.
"""

import argparse
import re
import ebooklib
from ebooklib import epub
from bs4 import BeautifulSoup
import yaml


# ---------------------------------------------------------------------------
# Class classification
# ---------------------------------------------------------------------------

SABCHE_CLASSES = {
    'Tibetan-Sabche',
    'Tibetan-Sabche-After-Title-Chapter',
}

VERSE_CITATION_CLASSES = {
    'Tibetan-Citations-in-Verse_Tibetan-Citations-First-Line',
    'Tibetan-Citations-in-Verse_Tibetan-Citations-Middle-Lines',
    'Tibetan-Citations-in-Verse_Tibetan-Citations-Last-Line',
}

PROSE_CITATION_CLASSES = {
    'Tibetan-External-Citations',
}

CHAPTER_CLASSES = {
    'Tibetan-Chapter',
}

SUBCHAPTER_CLASSES = {
    'Tibetan-Sub-Chapter',
}

SKIP_CLASSES = {
    'Credits-Page_Front-Page---Text-Author',
    'Credits-Page_Front-Title',
    'Front-Page---Text-Titles',
    'Front-Title',
    'Partners-Line',
}

FRONT_MATTER_DOCS = {'cover.xhtml', 'LEK-PHI-126.xhtml'}


def classify(p_element):
    """Return the semantic role for a <p> element based on its CSS classes."""
    classes = set(p_element.get('class', []))
    # Strip utility-only override classes
    classes.discard('_idGenParaOverride-1')

    if classes & SKIP_CLASSES:
        return 'skip'
    if classes & CHAPTER_CLASSES:
        return 'chapter'
    if classes & SUBCHAPTER_CLASSES:
        return 'subchapter'
    if classes & SABCHE_CLASSES:
        return 'sabche'
    if classes & PROSE_CITATION_CLASSES:
        return 'lung'
    if classes & VERSE_CITATION_CLASSES:
        if 'Tibetan-Citations-in-Verse_Tibetan-Citations-First-Line' in classes:
            return 'verse-first'
        if 'Tibetan-Citations-in-Verse_Tibetan-Citations-Last-Line' in classes:
            return 'verse-last'
        return 'verse-mid'
    return 'plain'


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
        'title_en': 'The Nectar of Manjushri\'s Speech: A Commentary on the Bodhisattvacaryavatara',
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
    return '## དཀར་ཆག / Table of Contents\n\n' + '\n'.join(lines) + '\n\n---\n\n'


# ---------------------------------------------------------------------------
# Callout formatting
# ---------------------------------------------------------------------------

def wrap_callout(callout_type, text):
    text = text.strip()
    lines = [l.rstrip() for l in text.split('\n')]
    body = '\n'.join('> ' + l for l in lines if l)
    return '> [!' + callout_type + ']\n' + body + '\n\n'


def get_text(element):
    return element.get_text().strip()


# ---------------------------------------------------------------------------
# Document processing with verse grouping
# ---------------------------------------------------------------------------

def process_body(body):
    """
    Walk all direct children (and their <p> descendants) of the body element,
    classify each paragraph, and emit Markdown. Consecutive verse-citation
    paragraphs are grouped into a single [!lung] callout block.
    """
    paragraphs = body.find_all(['p', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6'], recursive=True)
    md = ''
    i = 0
    while i < len(paragraphs):
        el = paragraphs[i]
        tag = el.name

        # Handle heading tags directly
        if tag in ('h1', 'h2', 'h3', 'h4', 'h5', 'h6'):
            level = int(tag[1])
            text = get_text(el)
            if text:
                md += '#' * level + ' ' + text + '\n\n'
            i += 1
            continue

        # Paragraph
        role = classify(el)
        text = get_text(el)

        if role == 'skip' or not text:
            i += 1
            continue

        if role == 'chapter':
            md += '# ' + text + '\n\n'

        elif role == 'subchapter':
            md += '## ' + text + '\n\n'

        elif role == 'sabche':
            md += wrap_callout('sabche', text)

        elif role == 'lung':
            md += wrap_callout('lung', text)

        elif role in ('verse-first', 'verse-mid', 'verse-last'):
            # Collect consecutive verse lines into one block
            verse_lines = [text]
            j = i + 1
            while j < len(paragraphs):
                next_role = classify(paragraphs[j])
                if next_role in ('verse-first', 'verse-mid', 'verse-last'):
                    next_text = get_text(paragraphs[j])
                    if next_text:
                        verse_lines.append(next_text)
                    j += 1
                else:
                    break
            combined = '\n'.join(verse_lines)
            md += wrap_callout('lung', combined)
            i = j
            continue

        else:  # plain
            md += text + '\n\n'

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
