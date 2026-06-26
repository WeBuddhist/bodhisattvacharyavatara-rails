#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Reflow Tibetan text by the shad (།).

Steps:
  1. Remove all existing line breaks (collapse whitespace to single spaces).
  2. Insert a line break after every shad group (one or more ། optionally
     separated by spaces, e.g. ། ། / །། / །། །། / ། ། ། །).
  3. Exception: never break after the opening header ༄༅། ། — it stays
     attached to the text that follows it.

A leading YAML frontmatter block (--- ... ---) is preserved untouched; only
the body below it is reflowed.

Usage:
    # single file
    python shad_linebreak.py input.txt [output.txt]
    cat input.txt | python shad_linebreak.py            # stdin -> stdout

    # whole folder, recursive -> overwrites each source file in place
    python shad_linebreak.py path/to/folder
    python shad_linebreak.py path/to/folder --ext .md .txt
"""
import argparse
import os
import re
import sys

# A shad group: one shad, then any number of (spaces + shad).
# Either preceded by a yig-mgo head mark (any run of ༄ ༅ ༆ ༇, e.g. ༄། །,
# ༄༅། །, ༄༅༅། །) -> kept, no break; or standalone -> break after.
PATTERN = re.compile(r'([༄-༇]+\s*།(?:\s*།)*)|(།(?:\s*།)*)')

# A leading YAML frontmatter block: --- on the first line, then content,
# then a closing --- (or ...) on its own line.
FRONTMATTER = re.compile(r'\A(---\r?\n.*?\r?\n(?:---|\.\.\.)[ \t]*\r?\n?)',
                         re.DOTALL)


def split_frontmatter(text: str):
    """Return (frontmatter, body). frontmatter is '' if none present."""
    m = FRONTMATTER.match(text)
    if m:
        return m.group(1), text[m.end():]
    return '', text


def reflow(text: str) -> str:
    # 1. remove all line breaks -> one continuous string (whitespace normalised)
    text = re.sub(r'\s+', ' ', text).strip()
    if not text:
        return ''

    # 2 + 3. insert breaks after shad groups, except the ༄༅ header
    def repl(m):
        if m.group(1) is not None:       # ༄༅། ། header -> keep, no break
            return m.group(1)
        return m.group(2) + '\n'         # ordinary shad group -> break after

    out = PATTERN.sub(repl, text)

    # tidy: drop spaces sitting around the inserted newlines, collapse blanks
    out = re.sub(r'[ \t]*\n[ \t]*', '\n', out)
    out = re.sub(r'\n{2,}', '\n', out).strip()
    return out + '\n'


def process_text(text: str) -> str:
    front, body = split_frontmatter(text)
    return front + reflow(body)


def process_folder(folder: str, exts) -> int:
    """Recurse folder and overwrite each matching file in place."""
    exts = tuple(e.lower() for e in exts)
    count = 0
    for dirpath, _dirs, files in os.walk(folder):
        for name in sorted(files):
            _root, ext = os.path.splitext(name)
            if ext.lower() not in exts:
                continue
            path = os.path.join(dirpath, name)
            with open(path, encoding='utf-8') as f:
                text = f.read()
            with open(path, 'w', encoding='utf-8') as f:
                f.write(process_text(text))
            print(os.path.relpath(path, folder))
            count += 1
    return count


def main():
    p = argparse.ArgumentParser(description='Reflow Tibetan text by the shad (།).')
    p.add_argument('input', nargs='?', help='input file or folder (stdin if omitted)')
    p.add_argument('output', nargs='?', help='output file (single-file mode only)')
    p.add_argument('--ext', nargs='+', default=['.md'],
                   help='folder mode: extensions to process (default: .md)')
    args = p.parse_args()

    # folder mode -> overwrite each matching file in place
    if args.input and os.path.isdir(args.input):
        n = process_folder(args.input, args.ext)
        print(f'\n{n} file(s) processed (overwritten in place).', file=sys.stderr)
        return

    # single-file / stdin mode
    if args.input:
        with open(args.input, encoding='utf-8') as f:
            text = f.read()
    else:
        text = sys.stdin.read()

    result = process_text(text)

    if args.output:
        with open(args.output, 'w', encoding='utf-8') as f:
            f.write(result)
    else:
        sys.stdout.write(result)


if __name__ == '__main__':
    main()
