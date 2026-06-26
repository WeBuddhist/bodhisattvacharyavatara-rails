#!/usr/bin/env python3
"""
find_toc_contexts.py -- rewrite [[context]] in a TOC tree with accurate body contexts.

For each entry the script finds the section opening using a layered strategy:

  1. Existing [[ctx]] hint search  -- if the TOC already has a snippet, locate it
     in the source first; this is the strongest prior for correct position.
  2. Verbatim title search         -- find all occurrences of the section title.
  3. Fuzzy title search            -- syllable-window match when verbatim fails.

When multiple candidates survive the position constraint, Gemini is called with
FULL TOC context (existing ctx hint, parent title+ctx, resolved sibling ctxs)
AND text context (source passages around each candidate) so the AI can make a
well-informed pick -- not a preview/dkar-chag listing, but the actual body opening.

  0 occurrences  -> fuzzy fallback; keep existing context if nothing found
  1 occurrence   -> use it directly (no API call)
  2+ occurrences -> narrow by position; call Gemini with TOC+text context

Rewrites the toc-tree file in-place (backs up original as .bak).

Usage:
    python 4-SYSTEM/scripts/toc_tree_extractor/find_toc_contexts.py \\
        0-INBOX/toc-tree-BCAC20_TG_bo.md \\
        1-SOURCES/Commentaries/BCAC20_TG_bo.md
"""

import argparse
import os
import re
import sys
from pathlib import Path


# ---------------------------------------------------------------------------
# .env loader
# ---------------------------------------------------------------------------
def _load_dotenv():
    candidates = [Path.cwd()]
    for p in Path.cwd().parents:
        if (p / "4-SYSTEM").is_dir():
            candidates.append(p)
            break
    candidates.append(Path(__file__).parent)
    for base in candidates:
        env_file = base / ".env"
        if env_file.exists():
            with open(env_file, encoding="utf-8") as f:
                for line in f:
                    line = line.strip()
                    if not line or line.startswith("#") or "=" not in line:
                        continue
                    key, _, val = line.partition("=")
                    key = key.strip()
                    val = val.strip().strip('"').strip("'")
                    if key and key not in os.environ:
                        os.environ[key] = val
            return


_load_dotenv()

DEFAULT_MODEL = "gemini-flash-latest"
MAX_RETRIES = 5
RETRY_BACKOFF = 6
# Minimum score to count a match as confident enough to advance the sibling
# constraint. Verbatim hits score 1.0. Fuzzy hits below this threshold are used
# for the context string but do NOT update the position tracker, preventing a
# weak match from cascading and blocking later siblings.
CONSTRAINT_MIN_SCORE = 0.85

# ---------------------------------------------------------------------------
# Tibetan canonicalisation
# ---------------------------------------------------------------------------
_TSHEG = "་"   # tsheg
_SHAD_CHARS = "།༎༏༐༑༒༔"
_SHAD_OR_WS_RE = re.compile("[" + _SHAD_CHARS + r"\s]+")


def tib_canon(s):
    if not s:
        return ""
    s = _SHAD_OR_WS_RE.sub(_TSHEG, s)
    s = re.sub(re.escape(_TSHEG) + "+", _TSHEG, s)
    return s.strip(_TSHEG)


# ---------------------------------------------------------------------------
# TOC tree parser / writer
# ---------------------------------------------------------------------------
_TREE_RE = re.compile(
    r"^(?P<indent>\s*\*\s+(?P<dec>\d+(?:\.\d+)*)\.?\s+)"
    r"(?P<title>[^\[]+?)(?:\s*\[\[(?P<ctx>[^\]]*)\]\])?\s*$"
)


def parse_toc(path):
    entries = []
    for raw in path.read_text(encoding="utf-8").splitlines():
        m = _TREE_RE.match(raw)
        if not m:
            continue
        title = m.group("title").strip().rstrip("།").strip()
        entries.append({
            "dec":   m.group("dec"),
            "title": title,
            "ctx":   (m.group("ctx") or "").strip() or None,
            "raw":   raw,
        })
    return entries


def rewrite_toc(path, new_contexts, out_path=None):
    """Write updated toc-tree to out_path (defaults to path, i.e. in-place).
    Always backs up the original source at path + '.bak'."""
    if out_path is None:
        out_path = path
    raw_lines = path.read_text(encoding="utf-8").splitlines(keepends=True)
    out = []
    for raw in raw_lines:
        m = _TREE_RE.match(raw.rstrip("\n\r"))
        if m and m.group("dec") in new_contexts:
            dec    = m.group("dec")
            indent = m.group("indent")
            title  = m.group("title").strip().rstrip("།").strip()
            ctx    = new_contexts[dec]
            out.append(f"{indent}{title} [[{ctx}]]\n")
        else:
            out.append(raw)
    bak = path.with_suffix(path.suffix + ".bak")
    bak.write_text(path.read_text(encoding="utf-8"), encoding="utf-8")
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text("".join(out), encoding="utf-8")
    return bak


def find_vault_root(start):
    """Walk up from start until we find the dir containing 4-SYSTEM/."""
    for p in [start] + list(start.parents):
        if (p / "4-SYSTEM").is_dir():
            return p
    return start


# ---------------------------------------------------------------------------
# Source text index
# ---------------------------------------------------------------------------
def build_index(lines):
    parts, offsets = [], []
    pos = 0
    for i, line in enumerate(lines):
        c = tib_canon(line)
        offsets.append((i, pos))
        if c:
            parts.append(c)
            pos += len(c) + 1
    canon_text = _TSHEG.join(p for p in parts if p)
    return canon_text, offsets


def canon_pos_to_line(offsets, char_pos):
    best = 0
    for line_idx, canon_start in offsets:
        if canon_start <= char_pos:
            best = line_idx
        else:
            break
    return best


def line_to_canon_pos(offsets, line_idx):
    for li, cp in offsets:
        if li >= line_idx:
            return cp
    return offsets[-1][1] if offsets else 0


def find_all_verbatim(canon_text, query):
    """All verbatim char positions of query in canon_text."""
    results, start = [], 0
    while True:
        idx = canon_text.find(query, start)
        if idx == -1:
            break
        results.append(idx)
        start = idx + 1
    return results


def find_best_fuzzy(canon_text, query, min_match=0.6):
    """Best fuzzy (syllable window) match. Returns (char_pos, score) or (None, 0)."""
    q_sylls = [s for s in query.split(_TSHEG) if s]
    n = len(q_sylls)
    if not q_sylls:
        return None, 0.0
    best_pos, best_len = None, 0
    for window in range(n, max(1, int(n * min_match)) - 1, -1):
        if window <= best_len:
            break
        for ci in range(n - window + 1):
            needle = _TSHEG.join(q_sylls[ci:ci + window])
            ti = canon_text.find(needle)
            if ti != -1 and window > best_len:
                best_len, best_pos = window, ti
        if best_len > 0 and best_len >= n * min_match:
            break
    if best_pos is None or best_len / n < min_match:
        return None, (best_len / n if best_len else 0.0)
    return best_pos, best_len / n


def snippet_from_source(lines, line_idx, max_syllables=20):
    """Verbatim snippet from source line, trimmed to ~max_syllables syllables."""
    if line_idx >= len(lines):
        return ""
    text = lines[line_idx].strip().rstrip("།\n\r").strip()
    sylls = text.split(_TSHEG)
    if len(sylls) > max_syllables:
        text = _TSHEG.join(sylls[:max_syllables])
    return text.strip()


def passage_around(lines, line_idx, radius=2):
    """+-radius source lines around line_idx as a single string."""
    start = max(0, line_idx - radius)
    end   = min(len(lines), line_idx + radius + 1)
    return "".join(lines[start:end]).strip()


# ---------------------------------------------------------------------------
# Ctx-hint search  (existing [[ctx]] as location prior)
# ---------------------------------------------------------------------------
def find_ctx_hint_positions(canon_text, ctx_hint, offsets, min_match=0.7):
    """
    Search for an existing [[ctx]] snippet in the source text.
    Returns list of (line_idx, score). Score 1.0 = verbatim; <1.0 = fuzzy.
    """
    if not ctx_hint or ctx_hint in ("?", ""):
        return []
    query = tib_canon(ctx_hint)
    if not query:
        return []
    # verbatim
    positions = find_all_verbatim(canon_text, query)
    if positions:
        return [(canon_pos_to_line(offsets, cp), 1.0) for cp in positions]
    # fuzzy
    fpos, score = find_best_fuzzy(canon_text, query, min_match=min_match)
    if fpos is not None:
        return [(canon_pos_to_line(offsets, fpos), score)]
    return []


# ---------------------------------------------------------------------------
# Gemini disambiguation
# ---------------------------------------------------------------------------
def get_client():
    try:
        from google import genai
    except ImportError:
        sys.exit("Error: google-genai not installed. Run: pip install google-genai")
    api_key = os.environ.get("GEMINI_API_KEY") or os.environ.get("GOOGLE_API_KEY")
    if not api_key:
        sys.exit("Error: GEMINI_API_KEY not set.")
    return genai.Client(api_key=api_key)


def gemini_pick(client, model, dec, title, parent_info, candidates,
                existing_ctx=None, sibling_info=None):
    """
    Ask Gemini which candidate is the actual section OPENING (not a preview).

    Uses full TOC context (existing [[ctx]] hint, parent title+ctx, sibling ctxs)
    plus source text context (passages around each candidate) to decide.

    candidates    : list of (line_idx, passage_text)
    existing_ctx  : the [[ctx]] snippet already in the TOC for this entry, or None
    sibling_info  : list of "dec: title [[ctx]]" strings for preceding siblings
    Returns 0-based index into candidates, or None on failure.
    """
    import time
    from google.genai import types

    cand_lines = "\n".join(
        f"{i+1}. (line {c[0]+1})\n{c[1]}"
        for i, c in enumerate(candidates)
    )

    toc_context_parts = []
    if parent_info:
        toc_context_parts.append(f"Parent section: {parent_info}")
    if sibling_info:
        toc_context_parts.append(
            "Preceding siblings (already located):\n" +
            "\n".join(f"  {s}" for s in sibling_info[-3:])
        )
    if existing_ctx and existing_ctx != "?":
        toc_context_parts.append(
            f"Existing context hint in TOC: [{existing_ctx}]\n"
            "(This snippet was previously recorded as the opening of this section.\n"
            " Strongly prefer the candidate whose passage contains or matches this hint.)"
        )

    toc_context_block = (
        "\nTOC STRUCTURAL CONTEXT:\n" + "\n".join(toc_context_parts)
        if toc_context_parts else ""
    )

    prompt = (
        "You are locating sections in a Tibetan Buddhist commentary.\n\n"
        f"Section: {dec}  title: {title}"
        f"{toc_context_block}\n\n"
        f"The section title appears at {len(candidates)} locations in the source text.\n"
        "Which location is where this section ACTUALLY OPENS -- where the commentary\n"
        "begins treating this topic -- NOT where it is merely listed in a preview,\n"
        "dkar-chag, or enumeration of upcoming topics?\n\n"
        "RULES for identifying a section OPENING vs. a PREVIEW:\n"
        "  OPENING:  the surrounding text is commentary prose specifically on this\n"
        "            topic; the title appears as a heading or the first phrase of\n"
        "            the body treatment.\n"
        "  PREVIEW / ENUMERATION: the surrounding text lists several upcoming\n"
        "            section names in sequence (parallel ordinal phrases back-to-back,\n"
        "            dkar-chag, or a numbered list of forthcoming topics).\n"
        "  POSITION: the opening must come AFTER the parent section's opening and\n"
        "            after any preceding sibling sections shown above.\n"
        "  HINT:     if an existing context hint is given, strongly prefer the\n"
        "            candidate whose passage contains or matches that hint.\n\n"
        f"Candidates:\n{cand_lines}\n\n"
        "Reply with ONLY the candidate number (1, 2, 3, ...). Nothing else."
    )

    config = types.GenerateContentConfig(
        temperature=0.0,
        thinking_config=types.ThinkingConfig(thinking_budget=0),
    )
    last_err = None
    for attempt in range(1, MAX_RETRIES + 1):
        try:
            resp = client.models.generate_content(
                model=model, contents=prompt, config=config)
            text = (resp.text or "").strip()
            m = re.search(r"\d+", text)
            if m:
                idx = int(m.group()) - 1
                if 0 <= idx < len(candidates):
                    return idx
            return 0
        except Exception as e:
            last_err = e
            if attempt < MAX_RETRIES:
                wait = RETRY_BACKOFF * (2 ** (attempt - 1))
                print(f"      ! Gemini error (attempt {attempt}): {e}; retrying in {wait}s",
                      file=sys.stderr)
                import time as _t
                _t.sleep(wait)
    print(f"      ! Gemini failed after retries: {last_err}", file=sys.stderr)
    return None


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
def main():
    ap = argparse.ArgumentParser(
        description="Rewrite [[context]] in a TOC tree with accurate body occurrences.")
    ap.add_argument("toc_file",    help="toc-tree-<id>.md")
    ap.add_argument("source_file", help="Commentary .md")
    ap.add_argument("--model",     default=DEFAULT_MODEL,
                    help=f"Gemini model (default: {DEFAULT_MODEL})")
    ap.add_argument("--min-match", type=float, default=0.6,
                    help="Min syllable fraction for fuzzy match (default: 0.6)")
    ap.add_argument("--short-title-syllables", type=int, default=2,
                    help="Titles with <= this many syllables skip title search (default: 2)")
    ap.add_argument("--no-ai", action="store_true",
                    help="Never call Gemini; use positional heuristic only")
    ap.add_argument("--dry-run", action="store_true",
                    help="Print proposed contexts without writing the file")
    args = ap.parse_args()

    toc_path = Path(args.toc_file).expanduser().resolve()
    src_path = Path(args.source_file).expanduser().resolve()
    for p in (toc_path, src_path):
        if not p.exists():
            sys.exit(f"Error: not found: {p}")

    entries = parse_toc(toc_path)
    if not entries:
        sys.exit("No TOC entries found.")

    lines = src_path.read_text(encoding="utf-8").splitlines(keepends=True)
    canon_text, offsets = build_index(lines)

    print(f"TOC:    {toc_path}  ({len(entries)} entries)")
    print(f"Source: {src_path}  ({len(lines)} lines)")
    print()

    client = None  # lazy-init

    dec_line      = {}   # dec -> located line (for parent/sibling constraint chaining)
    depth_last_line = {} # depth -> last CONFIDENT located line (sibling constraint)
    dec_ctx       = {}   # dec -> resolved context string (passed to AI as sibling info)
    dec_title     = {e["dec"]: e["title"] for e in entries}
    new_contexts  = {}   # dec -> new context string to write

    def parent_dec(dec):
        parts = dec.split(".")
        return ".".join(parts[:-1]) if len(parts) > 1 else None

    def parent_line_for(dec):
        pdec = parent_dec(dec)
        while pdec:
            pl = dec_line.get(pdec)
            if pl is not None:
                return pl
            pdec = parent_dec(pdec)
        return None

    def sibling_info_for(dec, depth):
        """Return resolved siblings at same depth, formatted for AI context."""
        prefix = ".".join(dec.split(".")[:-1])
        siblings = []
        for d, ctx_str in dec_ctx.items():
            d_depth  = len(d.split("."))
            d_prefix = ".".join(d.split(".")[:-1])
            if d_depth == depth and d_prefix == prefix and d != dec:
                t = dec_title.get(d, "")
                siblings.append(f"{d}: {t} [[{ctx_str}]]")
        return siblings

    def parent_info_str(dec):
        pdec = parent_dec(dec)
        if not pdec:
            return ""
        pl   = dec_line.get(pdec)
        pt   = dec_title.get(pdec, "")
        pctx = dec_ctx.get(pdec, "")
        line_tag = f" line {pl+1}" if pl is not None else ""
        return f"{pdec}: {pt} [[{pctx}]]{line_tag}"

    for entry in entries:
        dec   = entry["dec"]
        title = entry["title"]
        ctx   = entry["ctx"]   # existing [[ctx]] from TOC (may be None or "?")
        depth = len(dec.split("."))

        parent_line = parent_line_for(dec)
        min_canon = line_to_canon_pos(
            offsets, (parent_line + 1) if parent_line is not None else 0)
        prev_sib = depth_last_line.get(depth)
        if prev_sib is not None:
            sib_cp = line_to_canon_pos(offsets, prev_sib + 1)
            if sib_cp > min_canon:
                min_canon = sib_cp

        query   = tib_canon(title)
        n_sylls = len([s for s in query.split(_TSHEG) if s])

        located_line = None
        match_score  = 0.0
        method = ""

        # ================================================================
        # STEP 1: Locate existing [[ctx]] hint in source.
        # This is the strongest position prior -- if the TOC already has
        # a snippet that can be found in the body, use it directly.
        # ================================================================
        if ctx and ctx not in ("?", ""):
            hint_hits = find_ctx_hint_positions(canon_text, ctx, offsets)
            after_hint = [(li, sc) for li, sc in hint_hits
                          if line_to_canon_pos(offsets, li) >= min_canon]
            if after_hint:
                after_hint.sort(key=lambda x: line_to_canon_pos(offsets, x[0]))
                hint_line, hint_score = after_hint[0]
                if hint_score >= CONSTRAINT_MIN_SCORE:
                    located_line = hint_line
                    match_score  = hint_score
                    method = ("ctx-hint(verbatim)"
                              if hint_score == 1.0
                              else f"ctx-hint(fuzzy {hint_score:.0%})")

        # ================================================================
        # STEP 2: Verbatim title search, if ctx-hint didn't resolve.
        # ================================================================
        if located_line is None:
            if n_sylls <= args.short_title_syllables:
                all_positions = []
            else:
                all_positions = find_all_verbatim(canon_text, query)

            if all_positions:
                match_score = 1.0
                after = [cp for cp in all_positions if cp >= min_canon]

                if len(after) == 0:
                    # All occurrences before constraint -- use last (furthest in doc).
                    chosen_cp = all_positions[-1]
                    method = "last(pre-parent)"

                elif len(after) == 1:
                    chosen_cp = after[0]
                    method = "unique-after-constraint"

                else:
                    # Multiple candidates -- call AI with full TOC + text context.
                    if len(after) <= 5 and not args.no_ai:
                        if client is None:
                            client = get_client()
                        candidates = [
                            (canon_pos_to_line(offsets, cp),
                             passage_around(lines, canon_pos_to_line(offsets, cp)))
                            for cp in after
                        ]
                        p_info   = parent_info_str(dec)
                        sib_info = sibling_info_for(dec, depth)
                        print(f"  [{dec}] {len(after)} candidates -> Gemini (TOC+text ctx) ...",
                              flush=True)
                        pick = gemini_pick(
                            client, args.model, dec, title,
                            p_info, candidates,
                            existing_ctx=ctx,
                            sibling_info=sib_info,
                        )
                        chosen_cp = after[pick if pick is not None else 0]
                        method = f"ai-pick({(pick or 0)+1}/{len(after)})"
                    else:
                        chosen_cp = after[0]
                        method = "first-after-constraint"

                located_line = canon_pos_to_line(offsets, chosen_cp)

            else:
                # ============================================================
                # STEP 3: Fuzzy title search.
                # ============================================================
                segment = canon_text[min_canon:]
                fpos, score = find_best_fuzzy(segment, query, min_match=args.min_match)
                if fpos is not None and n_sylls > args.short_title_syllables:
                    located_line = canon_pos_to_line(offsets, min_canon + fpos)
                    match_score  = score
                    method = f"fuzzy({score:.0%})"
                else:
                    # No match at all -- keep existing context
                    if ctx and ctx != "?":
                        new_contexts[dec] = ctx
                        dec_ctx[dec] = ctx
                        print(f"  [{dec}] NO MATCH -- kept existing ctx  {title[:40]}")
                    else:
                        new_contexts[dec] = "?"
                        dec_ctx[dec] = "?"
                        print(f"  [{dec}] NO MATCH -- [[?]]  {title[:40]}")
                    continue

        # ---- Extract verbatim snippet from source ----
        snippet = snippet_from_source(lines, located_line)
        if not snippet:
            snippet = ctx or "?"

        new_contexts[dec] = snippet
        dec_ctx[dec] = snippet

        # Only advance position tracker for confident matches.
        # Weak fuzzy hits must not cascade and block later siblings.
        if match_score >= CONSTRAINT_MIN_SCORE:
            dec_line[dec] = located_line
            depth_last_line[depth] = located_line
            conf_tag = ""
        else:
            conf_tag = " (low-conf: pos not advanced)"

        print(f"  [{dec}] line {located_line+1:4}  [{method}]{conf_tag}"
              f"  ctx: {snippet[:50]}", flush=True)

    print()

    if args.dry_run:
        print("Dry run -- no file written.")
        return

    # Derive output path: 0-INBOX/temp/TOC-<id>/toc-tree-<id>.md
    commentary_id = re.sub(r"^toc-tree-", "", toc_path.stem)
    vault_root = find_vault_root(toc_path)
    out_path = vault_root / "0-INBOX" / "temp" / f"TOC-{commentary_id}" / toc_path.name

    bak = rewrite_toc(toc_path, new_contexts, out_path=out_path)
    print(f"Written -> {out_path}")
    print(f"Backup  -> {bak}")


if __name__ == "__main__":
    main()
