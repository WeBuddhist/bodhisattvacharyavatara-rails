import argparse
import os
import re
import ebooklib
from ebooklib import epub
from bs4 import BeautifulSoup
import yaml

"""
EPUB to Markdown Extractor
--------------------------
This script extracts content from EPUB files into a clean Markdown format,
preserving as much structural information as possible (headings, lists, links, etc.)
without applying specific methodology-based formatting (like block IDs).

Requirements:
- ebooklib
- beautifulsoup4
- PyYAML
"""

def clean_text(text):
    # Remove redundant whitespace while preserving basic line breaks if needed
    # However, for general extraction, we'll collapse multiple spaces.
    text = re.sub(r'[ \t]+', ' ', text).strip()
    return text

def extract_metadata(book):
    # Extract Dublin Core metadata
    raw_metadata = book.get_metadata('DC', 'title')
    title = raw_metadata[0][0] if raw_metadata else "Unknown Title"
    
    raw_metadata = book.get_metadata('DC', 'creator')
    author = raw_metadata[0][0] if raw_metadata else "Unknown Author"
    
    raw_metadata = book.get_metadata('DC', 'date')
    date = raw_metadata[0][0] if raw_metadata else "Unknown Date"
    
    raw_metadata = book.get_metadata('DC', 'language')
    language = raw_metadata[0][0] if raw_metadata else "en"
    
    metadata = {
        'title': title,
        'author': author,
        'date': date,
        'language': language,
        'source_description': 'Extracted from EPUB source'
    }
    return metadata

def process_element(element):
    """Converts a BeautifulSoup element to Markdown."""
    tag = element.name
    
    if tag in ['h1', 'h2', 'h3', 'h4', 'h5', 'h6']:
        level = int(tag[1])
        return f"{'#' * level} {element.get_text().strip()}\n\n"
    
    elif tag == 'p':
        # Handle bold/italic inside paragraphs
        for s in element.find_all(['strong', 'b']):
            s.replace_with(f"**{s.get_text()}**")
        for i in element.find_all(['em', 'i']):
            i.replace_with(f"*{i.get_text()}*")
        for a in element.find_all('a', href=True):
            a.replace_with(f"[{a.get_text()}]({a['href']})")
            
        text = element.get_text().strip()
        if text:
            return f"{text}\n\n"
    
    elif tag == 'ul':
        md = ""
        for li in element.find_all('li', recursive=False):
            md += f"- {li.get_text().strip()}\n"
        return md + "\n"
    
    elif tag == 'ol':
        md = ""
        for i, li in enumerate(element.find_all('li', recursive=False), 1):
            md += f"{i}. {li.get_text().strip()}\n"
        return md + "\n"
    
    elif tag == 'blockquote':
        return f"> {element.get_text().strip()}\n\n"
    
    return ""

def convert_epub_to_markdown(epub_path, output_path):
    try:
        book = epub.read_epub(epub_path)
    except Exception as e:
        print(f"Error reading EPUB: {e}")
        return

    metadata = extract_metadata(book)
    
    markdown_content = "---\n"
    markdown_content += yaml.dump(metadata, allow_unicode=True, sort_keys=False)
    markdown_content += "---\n\n"
    
    # Process items in the book spine order
    for item_id, linear in book.spine:
        item = book.get_item_with_id(item_id)
        if item.get_type() == ebooklib.ITEM_DOCUMENT:
            soup = BeautifulSoup(item.get_content(), 'html.parser')
            
            # Remove scripts and styles
            for script in soup(["script", "style"]):
                script.decompose()

            # The body content
            body = soup.find('body')
            if not body:
                continue
                
            # Iterate through direct children of the body to preserve order
            for child in body.find_all(recursive=False):
                markdown_content += process_element(child)

    # Save output
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(markdown_content)
    print(f"Successfully extracted content to {output_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Extract content from EPUB to Markdown")
    parser.add_argument("epub_path", help="Path to the source EPUB file")
    parser.add_argument("output_path", help="Path to the output Markdown file")
    args = parser.parse_args()
    
    convert_epub_to_markdown(args.epub_path, args.output_path)
