from __future__ import annotations
import json
import urllib.parse
import urllib.request

from constants import (
    _call_api, PERSONS_API, BDRC_SEARCH, BDRC_LABEL_LANGS,
    BDRC_TTL_LANG_MAP, LANG_TO_BCP47, LANG_TAG_MAP,
)


def search_bdrc(name):
    """Search BDRC Elasticsearch for a person by name. Returns (result, warn)."""
    index_line = json.dumps({"index": "bdrc_prod"})
    query_line = json.dumps({
        "from": 0, "size": 5,
        "query": {
            "function_score": {
                "script_score": {"script": {"id": "bdrc-score"}},
                "query": {"bool": {"filter": [], "must": [{
                    "multi_match": {
                        "type": "phrase",
                        "query": name.strip(),
                        "fields": [
                            "prefLabel_bo_x_ewts^1", "prefLabel_en^1",
                            "prefLabel_iast^1", "prefLabel_hani^1",
                            "altLabel_bo_x_ewts^0.6", "altLabel_en^0.6",
                            "altLabel_iast^0.6",
                        ]
                    }
                }]}}
            }
        }
    })
    payload = (index_line + "\n" + query_line + "\n").encode("utf-8")
    try:
        req = urllib.request.Request(
            BDRC_SEARCH, data=payload, method="POST",
            headers={"Content-Type": "application/json"},
        )
        with urllib.request.urlopen(req, timeout=10) as resp:
            raw = resp.read()
    except Exception as exc:
        return None, f"BDRC search failed for {name!r}: {exc}"
    if not raw:
        return None, f"BDRC search returned empty body for {name!r}"
    try:
        envelope = json.loads(raw.decode("utf-8"))
    except Exception as exc:
        return None, f"BDRC search bad JSON for {name!r}: {raw[:200]!r}"
    hits_list = envelope.get("responses", [envelope])[0].get("hits", {}).get("hits", [])
    persons = [h for h in hits_list if "Person" in h.get("_source", {}).get("type", [])]
    if not persons:
        return None, f"no Person found in BDRC for {name!r}"
    hit = persons[0]
    bdrc_id = hit.get("_id")
    names = {}
    for key, lang in BDRC_LABEL_LANGS.items():
        vals = hit["_source"].get(key)
        if vals:
            names[lang] = vals[0]
    warn = f"multiple BDRC persons matched {name!r} -- using first ({bdrc_id})" if len(persons) > 1 else None
    return {"bdrc_id": bdrc_id, "names": names}, warn


def fetch_bdrc_ttl_names(bdrc_id):
    """Fetch TTL for a BDRC person and return names dict keyed by our lang codes."""
    try:
        from rdflib import Graph, URIRef
        from rdflib.namespace import SKOS
    except ImportError:
        return None, "rdflib not installed -- run: pip install rdflib"
    url = f"https://ldspdi.bdrc.io/resource/{bdrc_id}.ttl"
    try:
        req = urllib.request.Request(url, headers={"Accept": "text/turtle"})
        with urllib.request.urlopen(req, timeout=15) as resp:
            ttl_data = resp.read().decode("utf-8")
    except Exception as exc:
        return None, f"TTL fetch failed for {bdrc_id}: {exc}"
    g = Graph()
    try:
        g.parse(data=ttl_data, format="turtle")
    except Exception as exc:
        return None, f"TTL parse failed for {bdrc_id}: {exc}"
    subject = URIRef(f"http://purl.bdrc.io/resource/{bdrc_id}")
    names = {}
    for label in g.objects(subject, SKOS.prefLabel):
        lang = str(label.language or "")
        code = BDRC_TTL_LANG_MAP.get(lang)
        if code and str(label).strip():
            names[code] = str(label).strip()
    return names or None, None


def lookup_person(name):
    """Find a person by name. Returns (person_dict, warnings_list).

    Step 1: persons API by name.
    Step 2: BDRC Elasticsearch → get bdrc_id → fetch TTL.
    """
    warnings = []
    if not name or len(name.strip()) < 2:
        return None, [f"author name too short to look up: {name!r}"]

    params = urllib.parse.urlencode({"name": name.strip(), "limit": 5, "offset": 0})
    data = _call_api(f"{PERSONS_API}?{params}")
    if data:
        items = data.get("items") or []
        if items:
            p = items[0]
            if len(items) > 1:
                warnings.append(f"multiple persons matched {name!r}: {[x['id'] for x in items]} -- using first")
            return {
                "id": p.get("id"),
                "bdrc_id": p.get("bdrc") or p.get("id"),
                "names": p.get("name"),
            }, warnings

    bdrc_person, warn = search_bdrc(name)
    if warn:
        warnings.append(warn)
    if not bdrc_person:
        return None, warnings

    bdrc_id = bdrc_person["bdrc_id"]
    names, ttl_warn = fetch_bdrc_ttl_names(bdrc_id)
    if ttl_warn:
        warnings.append(ttl_warn)
    if not names:
        names = bdrc_person["names"]

    warnings.append(f"person not in persons API -- found via BDRC ({bdrc_id})")
    return {"id": None, "bdrc_id": bdrc_id, "names": names}, warnings
