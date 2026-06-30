#!/usr/bin/env python3
"""
enrich_en_bo_keyword_meaning.py
================================
Goes verse by verse through the TF-IDF keyword index.
For each verse, sends the English text, Tibetan text, and keyword list
to Gemini and gets back the Tibetan word/phrase for each keyword in context.

Usage:
    python 4-SYSTEM/scripts/english_keyword/enrich_en_bo_keyword_meaning.py
    python 4-SYSTEM/scripts/english_keyword/enrich_en_bo_keyword_meaning.py --limit 20
    python 4-SYSTEM/scripts/english_keyword/enrich_en_bo_keyword_meaning.py --resume
    python 4-SYSTEM/scripts/english_keyword/enrich_en_bo_keyword_meaning.py --workers 10
"""

import os, sys, json, re, time, argparse, pathlib, warnings, threading
from concurrent.futures import ThreadPoolExecutor, as_completed
warnings.filterwarnings("ignore", category=FutureWarning, module="google")


# ---------------------------------------------------------------------------
# .env loader
# ---------------------------------------------------------------------------

def _load_dotenv():
    candidates = [pathlib.Path.cwd()]
    for p in pathlib.Path.cwd().parents:
        if (p / "4-SYSTEM").is_dir():
            candidates.append(p)
            break
    candidates.append(pathlib.Path(__file__).parent)
    for base in candidates:
        env_file = base / ".env"
        if env_file.exists():
            with open(env_file, encoding="utf-8") as f:
                for line in f:
                    line = line.strip()
                    if not line or line.startswith("#") or "=" not in line:
                        continue
                    k, _, v = line.partition("=")
                    k = k.strip()
                    v = v.strip().strip('"').strip("'")
                    if k and k not in os.environ:
                        os.environ[k] = v
            return

_load_dotenv()

try:
    from google import genai
    from google.genai import types
except ImportError:
    print("Error: google-genai not installed.  Run: pip install google-genai")
    sys.exit(1)


# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------

HERE      = pathlib.Path(__file__).parent
REPO_ROOT = HERE.parent.parent.parent

_DEFAULT_TFIDF   = HERE / "output/en-David_Karma_Choephel_verse_keywords.json"
_DEFAULT_TIBETAN = REPO_ROOT / "1-SOURCES/Translations/bo-བློ་ལྡན་ཤེས་རབ།.md"
_DEFAULT_OUTDIR  = HERE / "output"
_DEFAULT_MODEL   = "gemini-flash-latest"

SYSTEM_PROMPT = (
    "You are an expert in Tibetan Buddhist texts and the Tibetan language.\n"
    "Given an English verse and its Tibetan translation, return the Tibetan word or phrase\n"
    "that best expresses each listed English keyword as used in that verse.\n"
    "Return ONLY valid JSON: {\"keyword\": \"Tibetan\"}\n"
    "Use Tibetan script only. No Wylie, no English, no explanation."
)

_VERSE_MARKER = re.compile(r"\^([\w][\w\-]*\d+)\s*$")

# Thread-local Gemini client (one client per thread)
_thread_local = threading.local()
_api_key_global = ""
_model_global = _DEFAULT_MODEL


# ---------------------------------------------------------------------------
# Loaders
# ---------------------------------------------------------------------------

def load_json(path):
    if not path.exists():
        print("Error: file not found: " + str(path))
        sys.exit(1)
    return json.loads(path.read_text(encoding="utf-8"))


def load_tibetan_verses(path):
    text = path.read_text(encoding="utf-8")
    if text.startswith("---"):
        end = text.find("\n---", 3)
        if end != -1:
            text = text[end + 4:]
    verses, buffer = {}, []
    for line in text.splitlines():
        line = line.strip()
        if not line or line.startswith("![["):
            continue
        m = _VERSE_MARKER.search(line)
        if m:
            vid  = m.group(1)
            last = re.sub(r"^#+\s*", "", line[: m.start()].strip()).strip()
            if last:
                buffer.append(last)
            if buffer:
                verses[vid] = " ".join(buffer)
            buffer = []
        else:
            cleaned = re.sub(r"^#+\s*", "", line).strip()
            if cleaned:
                buffer.append(cleaned)
    return verses


# ---------------------------------------------------------------------------
# Gemini helpers
# ---------------------------------------------------------------------------

def get_client():
    """Return a thread-local Gemini client."""
    if not hasattr(_thread_local, "client"):
        _thread_local.client = genai.Client(api_key=_api_key_global)
    return _thread_local.client


def parse_json_response(text):
    text = re.sub(r"^```[a-z]*\n?", "", text.strip()).rstrip("`").strip()
    try:
        obj = json.loads(text)
        if isinstance(obj, dict):
            return obj
    except Exception:
        pass
    return {}


def call_gemini(prompt, system, retries=3):
    client = get_client()
    for attempt in range(1, retries + 1):
        try:
            resp = client.models.generate_content(
                model=_model_global,
                contents=prompt,
                config=types.GenerateContentConfig(
                    system_instruction=system,
                    temperature=0.1,
                    max_output_tokens=1024,
                ),
            )
            return (resp.text or "").strip()
        except Exception as e:
            msg = str(e)
            wait = 2 * attempt
            # Back off longer on rate limit errors
            if "429" in msg or "quota" in msg.lower() or "rate" in msg.lower():
                wait = 10 * attempt
            print("  [retry " + str(attempt) + "] " + msg[:80])
            time.sleep(wait)
    return ""


def get_tibetan_meanings(en_verse, bo_verse, keywords):
    """
    Step 1: batch call all keywords.
    Step 2: retry missing ones individually.
    Step 3: fallback plain translation.
    Returns {keyword: tibetan_text}.
    """
    kw_list = "\n".join("- " + kw for kw in keywords)
    prompt = (
        "English verse:\n" + en_verse + "\n\n"
        "Tibetan verse:\n" + bo_verse + "\n\n"
        "For each keyword below, give the Tibetan word or phrase as used in this verse.\n"
        "Keywords:\n" + kw_list + "\n\n"
        "Return JSON only: {\"keyword\": \"Tibetan meaning\", ...}"
    )
    result = parse_json_response(call_gemini(prompt, SYSTEM_PROMPT))

    missing = [kw for kw in keywords if not result.get(kw, "").strip()]
    for kw in missing:
        hint = "{\"" + kw + "\": \"Tibetan meaning\"}"
        single = (
            "English verse:\n" + en_verse + "\n\n"
            "Tibetan verse:\n" + bo_verse + "\n\n"
            "What is the Tibetan word or phrase for \"" + kw + "\" in this verse?\n"
            "Return JSON only: " + hint
        )
        parsed = parse_json_response(call_gemini(single, SYSTEM_PROMPT))
        if parsed.get(kw, "").strip():
            result[kw] = parsed[kw]
        else:
            fb_hint = "{\"" + kw + "\": \"Tibetan\"}"
            fb = (
                "Translate the English word \"" + kw + "\" into Tibetan script. "
                "Return JSON only: " + fb_hint
            )
            parsed2 = parse_json_response(call_gemini(fb, "Reply in Tibetan script only."))
            result[kw] = parsed2.get(kw, "").strip()

    return result


# ---------------------------------------------------------------------------
# Verse worker
# ---------------------------------------------------------------------------

def process_verse(args_tuple):
    """Process a single verse. Runs in a thread pool worker."""
    vid, v, bo_text, idx, total = args_tuple
    en_text = v["text"]
    kws     = v.get("keywords", [])
    if not kws:
        return vid, None

    kw_keys = [kw["key"] for kw in kws]

    if bo_text:
        bo_meanings = get_tibetan_meanings(en_text, bo_text, kw_keys)
    else:
        bo_meanings = {}

    kw_entries = []
    for kw in kws:
        kw_entries.append({
            "key":   kw["key"],
            "rank":  kw.get("rank",  0),
            "score": kw.get("score", 0),
            "count": kw.get("count", 1),
            "bo":    bo_meanings.get(kw["key"], ""),
        })

    filled  = sum(1 for kw in kw_entries if kw["bo"])
    missing = len(kw_entries) - filled
    status  = str(filled) + "/" + str(len(kw_entries)) + " filled"
    if missing:
        status += "  !" + str(missing) + " empty"
    if not bo_text:
        status = "(no Tibetan verse)"

    print("[" + str(idx) + "/" + str(total) + "] " + vid + "  " + status)
    return vid, {"text": en_text, "keywords": kw_entries}


# ---------------------------------------------------------------------------
# Natural sort
# ---------------------------------------------------------------------------

def verse_key(vid):
    parts = re.split(r"[-]", vid)
    try:
        return [int(p) for p in parts]
    except ValueError:
        return [0]


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def parse_args():
    p = argparse.ArgumentParser(description="Enrich verse keywords with Tibetan meanings via Gemini.")
    p.add_argument("--tfidf",   default=None)
    p.add_argument("--tibetan", default=None)
    p.add_argument("--outdir",  default=None)
    p.add_argument("--model",   default=_DEFAULT_MODEL)
    p.add_argument("--limit",   default=None, type=int)
    p.add_argument("--resume",  action="store_true")
    p.add_argument("--workers", default=5, type=int, help="Parallel Gemini workers (default 5)")
    p.add_argument("--save-every", default=20, type=int, help="Save after every N completed verses")
    return p.parse_args()


def main():
    global _api_key_global, _model_global

    args = parse_args()

    _api_key_global = os.environ.get("GEMINI_API_KEY", "")
    if not _api_key_global:
        print("Error: GEMINI_API_KEY not set.")
        sys.exit(1)
    _model_global = args.model

    tfidf_path   = pathlib.Path(args.tfidf).resolve()   if args.tfidf   else _DEFAULT_TFIDF
    tibetan_path = pathlib.Path(args.tibetan).resolve() if args.tibetan else _DEFAULT_TIBETAN
    outdir       = pathlib.Path(args.outdir).resolve()  if args.outdir  else _DEFAULT_OUTDIR
    outdir.mkdir(parents=True, exist_ok=True)

    stem     = tfidf_path.stem.replace("_verse_keywords", "")
    out_path = outdir / (stem + "_en_bo_keyword_meaning_enriched.json")

    print("Loading verse keywords -> " + tfidf_path.name)
    tfidf_data = load_json(tfidf_path)

    print("Loading Tibetan        -> " + tibetan_path.name)
    tibetan = load_tibetan_verses(tibetan_path)
    print("  " + str(len(tibetan)) + " Tibetan verses loaded")

    result = {}
    if args.resume and out_path.exists():
        result = load_json(out_path)
        print("Resuming: " + str(len(result)) + " verses already done")

    verse_ids = sorted(tfidf_data.keys(), key=verse_key)
    if args.limit:
        verse_ids = verse_ids[: args.limit]

    todo = [vid for vid in verse_ids if vid not in result] if args.resume else verse_ids
    total = len(todo)
    print("Verses to process: " + str(total) + "  workers=" + str(args.workers) + "\n")

    save_lock = threading.Lock()
    completed = [0]

    def save_result():
        out_path.write_text(
            json.dumps(
                dict(sorted(result.items(), key=lambda kv: verse_key(kv[0]))),
                ensure_ascii=False,
                indent=2,
            ),
            encoding="utf-8",
        )

    tasks = [
        (vid, tfidf_data[vid], tibetan.get(vid, ""), idx, total)
        for idx, vid in enumerate(todo, 1)
    ]

    with ThreadPoolExecutor(max_workers=args.workers) as pool:
        futures = {pool.submit(process_verse, t): t[0] for t in tasks}
        for future in as_completed(futures):
            vid, entry = future.result()
            if entry is None:
                continue
            with save_lock:
                result[vid] = entry
                completed[0] += 1
                if completed[0] % args.save_every == 0:
                    save_result()

    save_result()
    print("\nDone. Written -> " + str(out_path) + "  (" + str(len(result)) + " verses)")


if __name__ == "__main__":
    main()
