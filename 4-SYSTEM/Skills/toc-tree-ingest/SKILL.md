---
name: toc-tree-ingest
description: >
  Ingest a pre-extracted TOC tree (toc-tree-*.md) into a commentary file in
  1-SOURCES/Commentaries/commentaries_with_toc/ by inserting markdown headings
  with block IDs. All nodes are placed in a single pass using document-order
  cursor disambiguation. The [[...]] context snippets locate positions in the
  commentary — they are never copied into the output.

  Trigger this skill when the user says things like:
  "ingest the TOC tree", "insert headings from the toc-tree file",
  "add section headings to the commentary", "ingest toc tree".
---

# toc-tree-ingest

Inserts section headings derived from a pre-extracted TOC tree into a Tibetan
commentary file. All nodes across all depths are processed in a **single pass**,
in strict document order (the order they appear in the toc-tree file).

---

## Anchor strategy

Each TOC node has a `[[...]]` context snippet — a verbatim quotation from the
commentary that appears immediately after that section's opening. The first 60
characters (trailing tshegs U+0F0B stripped) become the `context_anchor` used
to locate the heading's insertion point.

**Document-order cursor disambiguation:** nodes are processed in the same
sequence they appear in the toc-tree file. A cursor tracks the line of the
last successfully placed heading. When an anchor appears in multiple places
in the commentary (e.g. the same structural phrase repeated in every chapter),
the script picks the **first occurrence at or after the cursor**. This
automatically selects the correct occurrence without any manual disambiguation,
because the tree's document order mirrors the commentary's document order.

Nodes whose anchor appears zero times are flagged as **not-found** and must be
inserted manually (see Step 3).

---

## Architecture

```
toc-tree-*.md
      │
      ▼  Step 1 — parse (once per commentary)
  /tmp/toc-tree-*.json
      │
      ▼  Step 2 — ingest (single pass, all depths)
  scripts/toc_tree_ingest.py ingest
      │
      ▼
  1-SOURCES/Commentaries/commentaries_with_toc/<id>.toc.md
  (headings inserted in place; prose untouched)
```

Two script modes:
- **`parse`** — run once; produces the JSON tree cache.
- **`ingest`** — single run; inserts all nodes in document order using cursor disambiguation.

---

## Inputs

| Field | Description |
|---|---|
| `toc_file` | Path to the toc-tree-*.md file, e.g. `0-INBOX/temp/TOC-BCAC14_GDR_bo/toc-tree-BCAC14_GDR_bo.md` |
| `commentary_file` | Path to the commentary .toc.md to update, e.g. `1-SOURCES/Commentaries/commentaries_with_toc/BCAC14_GDR_bo.toc.md` |

The commentary .toc.md must already exist (copied from the source in `1-SOURCES/Commentaries/`).

---

## Output

The commentary file is updated **in place**. Section heading lines of the form:

```
{heading_hashes} {label} ^{block-id}
```

are inserted immediately before the anchor line for each node. No existing
prose is deleted, reordered, or retyped.

### Heading level by depth

| Depth | Markdown heading |
|---|---|
| 1 | `##` |
| 2 | `###` |
| 3 | `####` |
| 4 | `#####` |
| 5+ | `######` |

### Block ID formula

Decimal path segments joined with `-`, then `-0` appended.

| Decimal ID | Block ID |
|---|---|
| `1` | `^1-0` |
| `1.3` | `^1-3-0` |
| `1.3.2` | `^1-3-2-0` |
| `1.3.2.2.2.2.1.1.1` | `^1-3-2-2-2-2-1-1-1-0` |

No zero-padding. No segment cap — depth follows the tree exactly.

---

## Procedure

### Step 0 — Prepare the commentary file

Copy the source commentary to the `commentaries_with_toc/` folder if not
already present:

```bash
cp "1-SOURCES/Commentaries/BCAC14_GDR_bo.md" \
   "1-SOURCES/Commentaries/commentaries_with_toc/BCAC14_GDR_bo.toc.md"
```

### Step 1 — Parse the TOC tree (run once per commentary)

Write the JSON to `/tmp/` to avoid NTFS ghost-file issues:

```bash
python3 -u -c "
import json, re
from collections import Counter
from pathlib import Path

TOC_MD  = '0-INBOX/temp/TOC-BCAC14_GDR_bo/toc-tree-BCAC14_GDR_bo.md'
JSON_OUT = '/tmp/toc-tree-BCAC14_GDR_bo.json'
ANCHOR_LENGTH = 60
CONTEXT_MAX   = 200

def decimal_to_block_id(decimal_id):
    return '^' + '-'.join(decimal_id.rstrip('.').split('.')) + '-0'

def parse_line(line):
    s = line.lstrip()
    if not s.startswith('* '): return None
    parts = s[2:].strip().split(None, 1)
    if not parts: return None
    raw_id = parts[0].rstrip('.')
    if not re.fullmatch(r'[\d]+(?:\.[\d]+)*', raw_id): return None
    rest = parts[1].strip() if len(parts) > 1 else ''
    if '[[' in rest:
        label_part, ctx_part = rest.split('[[', 1)
        label   = label_part.strip()
        context = ctx_part.rstrip(']').rstrip(']').strip()
    else:
        label = rest.strip(); context = ''
    depth  = raw_id.count('.') + 1
    anchor = context[:ANCHOR_LENGTH].strip().rstrip('་')
    return {'decimal_id': raw_id, 'depth': depth, 'label': label,
            'block_id': decimal_to_block_id(raw_id),
            'context': context[:CONTEXT_MAX], 'context_anchor': anchor}

nodes = []
with open(TOC_MD, encoding='utf-8') as fh:
    for line in fh:
        n = parse_line(line)
        if n:
            n['doc_order'] = len(nodes)
            nodes.append(n)

max_depth = max(n['depth'] for n in nodes)
with open(JSON_OUT, 'w', encoding='utf-8') as fh:
    json.dump({'source': TOC_MD, 'total_nodes': len(nodes),
               'max_depth': max_depth, 'nodes': nodes},
              fh, ensure_ascii=False, indent=2)

print(f'Parsed {len(nodes)} nodes, max depth {max_depth}', flush=True)
c = Counter(n['depth'] for n in nodes)
for d in sorted(c): print(f'  depth {d:2d}: {c[d]}', flush=True)
"
```

Skip this step if `/tmp/toc-tree-BCAC14_GDR_bo.json` already exists and
the toc-tree file has not changed.

### Step 2 — Ingest all nodes in one pass

```bash
python3 -u -c "
import json, sys
from pathlib import Path

JSON_PATH   = '/tmp/toc-tree-BCAC14_GDR_bo.json'
COMMENTARY  = '1-SOURCES/Commentaries/commentaries_with_toc/BCAC14_GDR_bo.toc.md'

with open(JSON_PATH, encoding='utf-8') as fh:
    tree_data = json.load(fh)

all_nodes = sorted(tree_data['nodes'], key=lambda n: n['doc_order'])

def heading_line(node):
    levels = {1:'##',2:'###',3:'####',4:'#####'}
    h = levels.get(node['depth'], '######')
    return f\"{h} {node['label']} {node['block_id']}\"

text  = Path(COMMENTARY).read_text(encoding='utf-8')
lines = text.splitlines(keepends=True)

inserted = 0; skipped = 0
not_found = []; disamb = []
cursor = 0

for node in all_nodes:
    anchor   = node.get('context_anchor','').strip()
    block_id = node['block_id']
    h_line   = heading_line(node)

    if not anchor:
        not_found.append((node['decimal_id'], node['label'], 'empty anchor [[?]]'))
        continue

    matches = [i for i,ln in enumerate(lines) if anchor in ln]

    if len(matches) == 0:
        not_found.append((node['decimal_id'], node['label'],
                          f'anchor not found: {anchor[:60]!r}'))
        continue

    if len(matches) == 1:
        target = matches[0]
    else:
        after = [m for m in matches if m >= cursor]
        if not after:
            not_found.append((node['decimal_id'], node['label'],
                              f'{len(matches)} matches, none after cursor {cursor}'))
            continue
        target = after[0]
        disamb.append((node['decimal_id'], len(matches), target))

    already = any(block_id in lines[target-k]
                  for k in (1,2,3) if target-k >= 0)
    if already:
        cursor = max(cursor, target)
        skipped += 1
    else:
        lines.insert(target, '\n')
        lines.insert(target, h_line + '\n')
        cursor = target + 2
        inserted += 1

Path(COMMENTARY).write_text(''.join(lines), encoding='utf-8')

print(f'Inserted: {inserted}  Skipped: {skipped}  Not-found: {len(not_found)}  Disambiguated: {len(disamb)}', flush=True)
if disamb:
    print('\nDisambiguated (cursor-based):', flush=True)
    for did, cnt, ln in disamb: print(f'  [{did}] {cnt} matches → line {ln}', flush=True)
if not_found:
    print('\nNOT FOUND (insert manually):', flush=True)
    for did, lbl, reason in not_found:
        print(f'  [{did}] {lbl[:70]}', flush=True)
        print(f'       {reason}', flush=True)
    sys.exit(2)
"
```

### Step 3 — Resolve not-found nodes manually

Not-found nodes fall into two categories:

**`[[?]]` entries** — the toc-tree has no context snippet for this node
(the original OCR produced `[[?]]`). Locate the section in the commentary
by reading the surrounding prose and understanding the structure, then insert
the heading line manually at the correct position.

**Anchor mismatch** — the context snippet exists but contains a character
that differs from the commentary (OCR variant: e.g. `ས` vs `སྟ`, Thai
character intrusion, etc.). Read the commentary around the expected location
and insert the heading manually.

**Manual insertion format:**
```
###### Label text ^block-id

```
(blank line after; inserted immediately before the section's opening prose)

After all manual insertions, re-run Step 2 — the already-present check will
skip the manually inserted headings and confirm zero not-found.

---

## Rules

1. **No context content in the output.** Only the label and block ID are
   written to the commentary file. The `[[...]]` text is never inserted.
2. **No prose is altered.** Existing commentary lines are never deleted,
   reordered, or retyped.
3. **Block IDs follow the tree.** No segment cap. Use the full decimal path.
4. **Single pass, document order.** All depths are ingested in one run.
   The cursor ensures correct placement of repeated structural phrases.
5. **Idempotent.** The already-present check (looks for block_id in 1–3
   lines before the anchor) makes re-runs safe.
6. **Write to `/tmp/`** for JSON cache (avoids NTFS ghost-file issues).

---

## Completion checklist

- [ ] Commentary .toc.md copied from source
- [ ] JSON cache produced at `/tmp/toc-tree-<id>.json`
- [ ] `ingest` run: summary shows 0 not-found (or all not-found resolved manually)
- [ ] Final file line count = source line count + (2 × headings inserted)
