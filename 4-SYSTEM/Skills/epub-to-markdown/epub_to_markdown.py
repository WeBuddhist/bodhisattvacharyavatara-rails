import argparse
import re
import ebooklib
from ebooklib import epub
from bs4 import BeautifulSoup
import yaml

"""
EPUB to Markdown Extractor
--------------------------
Extracts EPUB content into clean Markdown, preserving semantic block types
as wiki markup links based on CSS class colour coding:

  .root  (orange-red #BB5500) -> [[root|text]]  -- root text verses
  .lung  (dark gold  #7D6608) -> [[quote|text]] -- scriptural citations
  .bold  (blue       #003377) -> [[toc|text]]   -- TOC enumeration items

Requirements: ebooklib, beautifulsoup4, PyYAML
"""


def extract_metadata(book):
    def get(key):
        raw = book.get_metadata('DC', key)
        return raw[0][0] if raw else None

    return {
        'title': get('title') or 'Unknown Title',
        'author': get('creator') or 'Unknown Author',
        'date': get('date') or 'Unknown Date',
        'language': get('language') or 'en',
        'source_description': 'Extracted from EPUB source',
    }


def get_color_class(element):
    """Return semantic class name if element carries a colour-coded CSS class."""
    classes = element.get('class', [])
    if 'root' in classes:
        return 'root'
    if 'lung' in classes:
        return 'lung'
    if 'bold' in classes:
        return 'bold'
    return None


def inline_formats(element):
    """Apply bold/italic/link inline formatting and return plain text."""
    for s in element.find_all(['strong', 'b']):
        s.replace_with('**' + s.get_text() + '**')
    for i in element.find_all(['em', 'i']):
        i.replace_with('*' + i.get_text() + '*')
    for a in element.find_all('a', href=True):
        a.replace_with('[' + a.get_text() + '](' + a['href'] + ')')
    return element.get_text().strip()


def wrap_callout(callout_type, text):
    """Wrap text in wiki markup link format."""
    return '[[' + callout_type + '|' + text + ']]\n\n'


def process_element(element):
    """Convert a BeautifulSoup element to Markdown."""
    tag = element.name

    if tag in ['h1', 'h2', 'h3', 'h4', 'h5', 'h6']:
        level = int(tag[1])
        return '#' * level + ' ' + element.get_text().strip() + '\n\n'

    elif tag == 'p':
        color_class = get_color_class(element)
        text = inline_formats(element)
        if not text:
            return ''
        if color_class == 'root':
            return wrap_callout('root', text)
        elif color_class == 'lung':
            return wrap_callout('quote', text)
        elif color_class == 'bold':
            return wrap_callout('toc', text)
        else:
            return text + '\n\n'

    elif tag == 'ul':
        md = ''
        for li in element.find_all('li', recursive=False):
            md += '- ' + li.get_text().strip() + '\n'
        return md + '\n'

    elif tag == 'ol':
        md = ''
        for i, li in enumerate(element.find_all('li', recursive=False), 1):
            md += str(i) + '. ' + li.get_text().strip() + '\n'
        return md + '\n'

    elif tag == 'blockquote':
        lines = element.get_text().strip().split('\n')
        body = '\n'.join('> ' + line for line in lines)
        return body + '\n\n'

    return ''


def convert_epub_to_markdown(epub_path, output_path):
    try:
        book = epub.read_epub(epub_path)
    except Exception as e:
        print('Error reading EPUB: ' + str(e))
        return

    metadata = extract_metadata(book)
    md = '---\n' + yaml.dump(metadata, allow_unicode=True, sort_keys=False) + '---\n\n'

    for item_id, linear in book.spine:
        item = book.get_item_with_id(item_id)
        if item.get_type() == ebooklib.ITEM_DOCUMENT:
            soup = BeautifulSoup(item.get_content(), 'html.parser')
            for tag in soup(['script', 'style']):
                tag.decompose()
            body = soup.find('body')
            if not body:
                continue
            for child in body.find_all(recursive=False):
                md += process_element(child)

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(md)
    print('Successfully extracted content to ' + output_path)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Extract EPUB content to Markdown')
    parser.add_argument('epub_path', help='Path to the source EPUB file')
    parser.add_argument('output_path', help='Path to the output Markdown file')
    args = parser.parse_args()
    convert_epub_to_markdown(args.epub_path, args.output_path)
