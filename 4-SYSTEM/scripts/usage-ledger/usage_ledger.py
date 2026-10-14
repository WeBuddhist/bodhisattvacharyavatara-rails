#!/usr/bin/env python3
"""One token/cost ledger for every model call in the KF translation pilot.

Each line of the ledger (JSONL) is one unit of model work:

  {ts, step, text, lang, variant, batch, segments, attempt,
   engine, model, calls, tokens:{input, output, thinking, cache_read, cache_write},
   seconds, source, note}

  engine  claude-agent | gemini-api | dharmamitra-api
  source  agent-transcript | api-response | backfill | estimate

Library use (from a pipeline script):
    from usage_ledger import log_call
    log_call(LEDGER, step="term-review", text="vajracchedika", engine="gemini-api", ...)

CLI:
  harvest-agent   read a Claude Code subagent transcript and log its exact usage
  backfill-gemini log past gm_translate.py runs from their work/*.jsonl ledgers,
                  one row per API call (their per-block usage is a copy of the
                  batch call's usage, so it is de-duplicated here)
  summary         totals by step, engine and model
"""
import argparse
import datetime as _dt
import json
import pathlib
import sys
from collections import defaultdict

DEFAULT_LEDGER = pathlib.Path(__file__).resolve().parents[3] / "0-INBOX/kf-pilot/usage-ledger.jsonl"
TOKEN_KEYS = ("input", "output", "thinking", "cache_read", "cache_write")
OUT_CHARS_PER_TOKEN = 3.0  # rough for mixed English / Tibetan / JSON; see agent_usage()


def now():
    return _dt.datetime.now().isoformat(timespec="seconds")


def log_call(ledger=DEFAULT_LEDGER, *, step, text, engine, model, tokens, lang=None, variant=None,
             batch=None, segments=None, attempt=1, calls=1, seconds=None, source="api-response",
             note=None, ts=None):
    rec = {"ts": ts or now(), "step": step, "text": text, "lang": lang, "variant": variant,
           "batch": batch, "segments": segments, "attempt": attempt, "engine": engine,
           "model": model, "calls": calls,
           "tokens": {k: int(tokens.get(k) or 0) for k in TOKEN_KEYS},
           "seconds": seconds, "source": source, "note": note}
    ledger = pathlib.Path(ledger)
    ledger.parent.mkdir(parents=True, exist_ok=True)
    with ledger.open("a", encoding="utf-8") as fh:
        fh.write(json.dumps(rec, ensure_ascii=False) + "\n")
    return rec


# ------------------------------------------------------------- claude agents


def agent_usage(transcript):
    """Sum the usage of one subagent transcript, one count per API message.

    Claude Code writes one record per content block, all carrying the same
    message id and usage, so records are de-duplicated by message id. The usage
    is the snapshot taken when the response STARTED: input and cache tokens are
    exact, output tokens are not, and thinking is stored redacted. Output is
    therefore estimated from the visible output (text + tool-call arguments) at
    OUT_CHARS_PER_TOKEN characters per token; thinking is not counted."""
    per_msg, first, last, models = {}, None, None, set()
    out_chars = defaultdict(int)
    for line in pathlib.Path(transcript).read_text(encoding="utf-8").splitlines():
        try:
            r = json.loads(line)
        except json.JSONDecodeError:  # a truncated line (transcript cut mid-write); skip it
            continue
        ts = r.get("timestamp")
        if ts:
            first = first or ts
            last = ts
        m = r.get("message") or {}
        if r.get("type") != "assistant" or not m.get("usage"):
            continue
        models.add(m.get("model"))
        for blk in m.get("content") or []:
            if blk.get("type") == "text":
                out_chars[m.get("id")] += len(blk.get("text", ""))
            elif blk.get("type") == "tool_use":
                out_chars[m.get("id")] += len(json.dumps(blk.get("input", {}), ensure_ascii=False))
        u = m["usage"]
        prev = per_msg.get(m.get("id"))
        if prev is None or (u.get("output_tokens") or 0) >= (prev.get("output_tokens") or 0):
            per_msg[m.get("id")] = u
    tok = defaultdict(int)
    for mid, u in per_msg.items():
        tok["input"] += u.get("input_tokens") or 0
        tok["output"] += max(u.get("output_tokens") or 0, round(out_chars[mid] / OUT_CHARS_PER_TOKEN))
        tok["cache_read"] += u.get("cache_read_input_tokens") or 0
        tok["cache_write"] += u.get("cache_creation_input_tokens") or 0
        tok["thinking"] += ((u.get("output_tokens_details") or {}).get("thinking_tokens") or 0)
    secs = None
    if first and last:
        f = _dt.datetime.fromisoformat(first.replace("Z", "+00:00"))
        l_ = _dt.datetime.fromisoformat(last.replace("Z", "+00:00"))
        secs = round((l_ - f).total_seconds(), 1)
    return dict(tok), len(per_msg), secs, sorted(m for m in models if m)


def cmd_harvest(a):
    path = pathlib.Path(a.session_dir) / "subagents" / f"agent-{a.agent_id}.jsonl"
    tokens, calls, secs, models = agent_usage(path)
    rec = log_call(a.ledger, step=a.step, text=a.text, lang=a.lang, variant=a.variant, batch=a.batch,
                   segments=a.segments, attempt=a.attempt, engine="claude-agent",
                   model=",".join(models), tokens=tokens, calls=calls, seconds=secs,
                   source="agent-transcript+output-estimate", note=a.note or f"agent {a.agent_id}")
    print(json.dumps(rec, ensure_ascii=False))


# ------------------------------------------------------------- gemini backfill


def cmd_backfill(a):
    n = 0
    for f in a.files:
        seen = set()
        for line in pathlib.Path(f).read_text(encoding="utf-8").splitlines():
            r = json.loads(line)
            u = r.get("usage")
            if not u:
                continue
            key = (tuple(r.get("batch_block_ids") or [r.get("block_id")]), json.dumps(u, sort_keys=True))
            if key in seen:
                continue
            seen.add(key)
            log_call(a.ledger, ts=r.get("ts"), step=a.step, text=a.text, lang=r.get("target_language"),
                     variant=a.variant, batch=pathlib.Path(f).stem, segments=len(key[0]),
                     engine="gemini-api", model=r.get("model_version") or r.get("model"),
                     tokens={"input": u.get("prompt_tokens"), "output": u.get("output_tokens"),
                             "thinking": u.get("thinking_tokens")},
                     seconds=r.get("elapsed_s"), source="backfill", note=f"from {pathlib.Path(f).name}")
            n += 1
    print(f"backfilled {n} calls")


# ------------------------------------------------------------- summary


PRICES = pathlib.Path(__file__).resolve().parent / "prices.json"


def row_cost(r, prices):
    """USD for one ledger row at the list prices in prices.json (None if the model is not priced)."""
    p = prices["models"].get((r.get("model") or "").split(",")[0])
    if p is None:
        return None
    return sum(r["tokens"].get(k, 0) * p[k] for k in TOKEN_KEYS) / 1_000_000


def cmd_summary(a):
    rows = [json.loads(l) for l in pathlib.Path(a.ledger).read_text(encoding="utf-8").splitlines() if l.strip()]
    if a.text:
        rows = [r for r in rows if r["text"] == a.text]
    agg = defaultdict(lambda: defaultdict(int))
    for r in rows:
        k = (r["step"], r["engine"], r["model"])
        agg[k]["calls"] += r.get("calls") or 0
        agg[k]["seconds"] += r.get("seconds") or 0
        for t in TOKEN_KEYS:
            agg[k][t] += r["tokens"].get(t, 0)
    prices = json.loads(PRICES.read_text(encoding="utf-8"))
    cost = defaultdict(float)
    for r in rows:
        c = row_cost(r, prices)
        cost[(r["step"], r["engine"], r["model"])] += c or 0
    hdr = ["step", "engine", "model", "calls", *TOKEN_KEYS, "seconds", "USD"]
    print("| " + " | ".join(hdr) + " |\n|" + "---|" * len(hdr))
    for (step, eng, model), v in sorted(agg.items()):
        print(f"| {step} | {eng} | {model} | {v['calls']} | " +
              " | ".join(f"{v[t]:,}" for t in TOKEN_KEYS) + f" | {v['seconds']:.0f} | {cost[(step, eng, model)]:.2f} |")
    print(f"\nTotal USD at list prices ({prices['as_of']}): {sum(cost.values()):.2f}")


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--ledger", default=str(DEFAULT_LEDGER))
    sub = p.add_subparsers(dest="cmd", required=True)

    h = sub.add_parser("harvest-agent")
    h.add_argument("--session-dir", required=True, help="~/.claude/projects/<project>/<session-id>")
    h.add_argument("--agent-id", required=True)
    for k in ("step", "text"):
        h.add_argument(f"--{k}", required=True)
    for k in ("lang", "variant", "batch", "note"):
        h.add_argument(f"--{k}")
    h.add_argument("--segments", type=int)
    h.add_argument("--attempt", type=int, default=1)
    h.set_defaults(func=cmd_harvest)

    b = sub.add_parser("backfill-gemini")
    b.add_argument("files", nargs="+")
    b.add_argument("--step", required=True)
    b.add_argument("--text", required=True)
    b.add_argument("--variant")
    b.set_defaults(func=cmd_backfill)

    s = sub.add_parser("summary")
    s.add_argument("--text")
    s.set_defaults(func=cmd_summary)

    a = p.parse_args()
    a.func(a)


if __name__ == "__main__":
    sys.exit(main())
