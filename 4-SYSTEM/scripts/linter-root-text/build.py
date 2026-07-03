from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path

from constants import SCHEMA_FIELDS, LANG_TAG_MAP, LANG_TO_BCP47, LANGUAGE_VALUES
from lookup import lookup_person, search_bdrc_work, fetch_bdrc_work_titles
from validate import validate_text_input, resolve_language

OUTPUT_DIR = Path(__file__).parent / "output"

_WYLIE_RE = __import__('re').compile(r"'[a-zA-Z]")

def _wylie_to_unicode(text, lang_tag):
    if lang_tag != "bo":
        return text
    if not text or any("ༀ" <= c <= "࿿" for c in text):
        return text
    if not _WYLIE_RE.search(text):
        return text
    try:
        import pyewts as _pyewts
        converter = _pyewts.pyewts()
        converted = converter.toUnicode(text)
        if converted and converted.strip():
            return converted
    except ImportError:
        pass
    return text


def _convert_bo_entry(entry):
    """Convert bo-x-ewts or bo keys in a title/alt_title dict to Tibetan Unicode."""
    if not isinstance(entry, dict):
        return entry
    new_entry = {}
    for k, v in entry.items():
        if k in ("bo-x-ewts", "bo") and isinstance(v, str):
            new_entry["bo"] = _wylie_to_unicode(v, "bo")
        else:
            new_entry[k] = v
    return new_entry


def build_text_input(data):
    payload = {}
    vault_tag = data.get("lang_tag") or ""
    person_warnings = []

    # Pre-fetch BDRC work title info
    bdrc_work_info = None
    bdrc_work_id = data.get("bdrc_work_id") or data.get("bdrc")
    raw_title = data.get("title")
    if not bdrc_work_id and raw_title and isinstance(raw_title, str) and raw_title.strip():
        bdrc_work_id, work_warn = search_bdrc_work(raw_title.strip())
        if work_warn:
            person_warnings.append(work_warn)
    if bdrc_work_id:
        bdrc_work_info, ttl_warn = fetch_bdrc_work_titles(bdrc_work_id)
        if ttl_warn:
            person_warnings.append(ttl_warn)
        if bdrc_work_info:
            payload["_resolved_bdrc_work_id"] = bdrc_work_id
            doc_lang = LANG_TAG_MAP.get(vault_tag, vault_tag)
            for bcp47 in LANG_TO_BCP47.get(doc_lang, [doc_lang]):
                if bcp47 in bdrc_work_info["pref"]:
                    payload["_resolved_title"] = bdrc_work_info["pref"][bcp47]
                    break

    for field in SCHEMA_FIELDS:
        if field == "title":
            if bdrc_work_info and bdrc_work_info.get("pref"):
                title_obj = dict(bdrc_work_info["pref"])
            else:
                title_obj = {}
                raw = data.get("title")
                if isinstance(raw, str) and raw.strip():
                    lang_key = LANG_TAG_MAP.get(vault_tag, vault_tag) or "default"
                    title_obj[lang_key] = raw
                elif isinstance(raw, dict):
                    title_obj = dict(raw)
                en_title = data.get("title in English") or data.get("title_in_english")
                if en_title and isinstance(en_title, str) and en_title.strip():
                    title_obj["en"] = en_title
            # Convert bo-x-ewts or bo Wylie values to Unicode
            payload["title"] = _convert_bo_entry(title_obj) if title_obj else None


        elif field == "alt_titles":
            if bdrc_work_info and bdrc_work_info.get("alt"):
                raw_alts = bdrc_work_info["alt"]
            else:
                alt = data.get("alt_titles")
                if isinstance(alt, str) and alt.strip():
                    lang_key = LANG_TAG_MAP.get(vault_tag, vault_tag) or "default"
                    raw_alts = [{lang_key: alt}]
                else:
                    raw_alts = alt
            # Convert bo-x-ewts Wylie entries to Unicode and normalize key to "bo"
            if isinstance(raw_alts, list):
                payload["alt_titles"] = [_convert_bo_entry(e) for e in raw_alts]
            else:
                payload["alt_titles"] = raw_alts


        elif field == "language":
            raw_lang = data.get("language", "")
            if raw_lang:
                code, _ = resolve_language(raw_lang)
                payload["language"] = code or raw_lang
            else:
                payload["language"] = vault_tag if vault_tag in LANGUAGE_VALUES else None

        elif field == "contributions":
            import re as _re
            contribs = list(data.get("contributions") or [])

            def _split_names(raw):
                if not raw:
                    return []
                return [n.strip() for n in _re.split(r"[,;]", str(raw)) if n.strip()]

            author_raw = data.get("author in English") or data.get("author_in_english") or data.get("author")
            translator_raw = data.get("translator in English") or data.get("translator_in_english") or data.get("translator")

            named_roles = (
                [(n, "author") for n in _split_names(author_raw)] +
                [(n, "translator") for n in _split_names(translator_raw)]
            )

            _ID_TAG_RE = _re.compile(r'\[(?P<source>bdrc|op):(?P<id>[^\]]+)\]')

            for name, role in named_roles:
                if name.startswith("[FILL"):
                    continue

                id_match = _ID_TAG_RE.search(name)
                clean_name = _ID_TAG_RE.sub("", name).strip()

                entry = {"type": "person", "role": role}

                if id_match:
                    id_source = id_match.group("source")
                    id_value = id_match.group("id").strip()
                    if id_source == "bdrc":
                        entry["bdrc_id"] = id_value
                    else:
                        entry["id"] = id_value
                else:
                    person, warns = lookup_person(clean_name)
                    person_warnings.extend(warns)
                    resolved_author = None
                    if person and person.get("names"):
                        names = person["names"]
                        doc_lang = LANG_TAG_MAP.get(vault_tag, vault_tag)
                        resolved_author = names.get(doc_lang) or names.get("en") or next(iter(names.values()), None)
                    if person:
                        if person.get("bdrc_id"):
                            entry["bdrc_id"] = person["bdrc_id"]
                        elif person.get("id"):
                            entry["id"] = person["id"]
                    if resolved_author and "_resolved_author" not in payload:
                        payload["_resolved_author"] = resolved_author

                contribs.append(entry)

            payload["contributions"] = contribs if contribs else None

        elif field == "license":
            payload["license"] = data.get("license")

        elif field in data:
            payload[field] = data[field]

        else:
            payload[field] = None

    payload["_person_warnings"] = person_warnings
    return payload


def write_output(path, doc_info, items):
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    stem = path.stem
    timestamp = datetime.now(timezone.utc).isoformat()
    built = build_text_input(doc_info)
    person_warnings = built.pop("_person_warnings", [])
    resolved_author = built.pop("_resolved_author", None)
    resolved_title = built.pop("_resolved_title", None)
    resolved_bdrc_work_id = built.pop("_resolved_bdrc_work_id", None)

    if not built.get("alt_titles"):
        items.append(("ERROR", "alt_titles: required (not found in source or BDRC)"))

    errors = [m for l, m in items if l == "ERROR"]
    infos = [m for l, m in items if l == "INFO"]

    if not errors:
        out_path = OUTPUT_DIR / f"{stem}.lint.json"
        result = {
            "status": "ok",
            "source": str(path.resolve()),
            "validated_at": timestamp,
            "notes": infos,
            "warnings": person_warnings,
            "text_input": built,
        }
    else:
        out_path = OUTPUT_DIR / f"{stem}.lint.errors.json"
        result = {
            "status": "error",
            "source": str(path.resolve()),
            "validated_at": timestamp,
            "error_count": len(errors),
            "errors": errors,
            "notes": infos,
            "warnings": person_warnings,
            "resolved": built,
        }

    out_path.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    return out_path, person_warnings, resolved_author, resolved_title, resolved_bdrc_work_id


def write_edition_output(path, doc_info, items):
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    stem = path.stem
    timestamp = datetime.now(timezone.utc).isoformat()

    built = build_text_input(doc_info)
    person_warnings = built.pop("_person_warnings", [])
    resolved_author = built.pop("_resolved_author", None)
    resolved_title = built.pop("_resolved_title", None)
    resolved_bdrc_work_id = built.pop("_resolved_bdrc_work_id", None)

    errors = [m for l, m in items if l == "ERROR"]
    infos  = [m for l, m in items if l == "INFO"]
    warns  = [m for l, m in items if l == "WARN"]

    if not errors:
        out_path = OUTPUT_DIR / f"{stem}.lint.json"
        result = {
            "status": "ok",
            "source": str(path.resolve()),
            "validated_at": timestamp,
            "notes": infos,
            "warnings": warns + person_warnings,
            "text_input": built,
        }
    else:
        out_path = OUTPUT_DIR / f"{stem}.lint.errors.json"
        result = {
            "status": "error",
            "source": str(path.resolve()),
            "validated_at": timestamp,
            "error_count": len(errors),
            "errors": errors,
            "notes": infos,
            "warnings": warns + person_warnings,
            "resolved": built,
        }
    out_path.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    return out_path, person_warnings, resolved_author, resolved_title, resolved_bdrc_work_id
