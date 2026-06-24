from __future__ import annotations

import argparse
import json
import os
import re
import sys
import time
import urllib.error
import urllib.request
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


BASE_DIR = Path(__file__).resolve().parent
REFINED_DIR = BASE_DIR / "_jlpt source refined"
CACHE_PATH = REFINED_DIR / "gemini_translation_polish_cache.json"
READING_FILES = [
    REFINED_DIR / "reading" / "n3_custom_reading.json",
    REFINED_DIR / "reading" / "n3_official_workbook_reading.json",
]
LISTENING_FILE = REFINED_DIR / "listening" / "n3_listening_review_index.json"

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")


def load_dotenv(path: Path) -> None:
    if not path.exists():
        return
    for raw_line in path.read_text(encoding="utf-8-sig").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        name, value = line.split("=", 1)
        name = name.strip()
        value = value.strip().strip('"').strip("'")
        if name and name not in os.environ:
            os.environ[name] = value


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")


def load_cache() -> dict[str, Any]:
    if not CACHE_PATH.exists():
        return {}
    try:
        return json.loads(CACHE_PATH.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return {}


def save_cache(cache: dict[str, Any]) -> None:
    CACHE_PATH.parent.mkdir(parents=True, exist_ok=True)
    CACHE_PATH.write_text(json.dumps(cache, ensure_ascii=False, indent=2), encoding="utf-8")


def compact_spaces(text: str) -> str:
    return re.sub(r"\s+", " ", str(text or "")).strip()


def extract_json(text: str) -> Any:
    value = text.strip()
    if value.startswith("```"):
        value = re.sub(r"^```(?:json)?\s*", "", value)
        value = re.sub(r"\s*```$", "", value)
    try:
        return json.loads(value)
    except json.JSONDecodeError:
        start = value.find("{")
        end = value.rfind("}")
        if start != -1 and end != -1 and start < end:
            return json.loads(value[start : end + 1])
        raise


def gemini_request(prompt: str, model: str, api_key: str, retries: int, sleep_seconds: float) -> dict[str, Any]:
    url = f"https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent?key={api_key}"
    body = {
        "contents": [{"role": "user", "parts": [{"text": prompt}]}],
        "generationConfig": {
            "temperature": 0.2,
            "topP": 0.8,
            "responseMimeType": "application/json",
        },
    }
    encoded = json.dumps(body, ensure_ascii=False).encode("utf-8")

    last_error: Exception | None = None
    for attempt in range(1, retries + 1):
        request = urllib.request.Request(
            url,
            data=encoded,
            headers={"Content-Type": "application/json; charset=utf-8"},
            method="POST",
        )
        try:
            with urllib.request.urlopen(request, timeout=90) as response:
                payload = json.loads(response.read().decode("utf-8"))
            text = "".join(
                part.get("text", "")
                for candidate in payload.get("candidates", [])
                for part in candidate.get("content", {}).get("parts", [])
            )
            parsed = extract_json(text)
            if not isinstance(parsed, dict):
                raise ValueError("Gemini response root is not an object")
            return parsed
        except urllib.error.HTTPError as exc:
            last_error = exc
            retry_after = exc.headers.get("Retry-After")
            detail = exc.read().decode("utf-8", errors="ignore")
            retry_delay_match = re.search(r'"retryDelay"\s*:\s*"(\d+)s"', detail)
            wait = float(retry_after) if retry_after and retry_after.isdigit() else sleep_seconds * attempt
            if retry_delay_match:
                wait = max(wait, float(retry_delay_match.group(1)))
            if exc.code == 429:
                wait = max(wait, 12.0 * attempt)
            print(f"  [warn] Gemini HTTP {exc.code}; retry {attempt}/{retries} after {wait:.1f}s")
            time.sleep(wait)
        except Exception as exc:
            last_error = exc
            print(f"  [warn] Gemini parse/request failed: {exc.__class__.__name__}; retry {attempt}/{retries}")
            time.sleep(sleep_seconds * attempt)

    raise RuntimeError(f"Gemini request failed after {retries} retries: {last_error}")


def build_prompt(kind: str, title: str, section_title: str, entries: list[dict[str, str]]) -> str:
    source_blob = json.dumps(entries, ensure_ascii=False, indent=2)
    return f"""
당신은 JLPT N3 학습 콘텐츠의 일본어-한국어 번역을 다듬는 편집자입니다.

작업 종류: {kind}
섹션: {section_title}
문항/자료 제목: {title}

아래 JSON 배열에는 문장별 일본어 원문 ja와 기존 한국어 번역 ko가 있습니다.
전체 맥락을 먼저 읽고, 한국어 번역만 자연스럽게 다듬어 주세요.

규칙:
- id는 반드시 그대로 유지합니다.
- 입력 항목 수와 출력 항목 수를 반드시 동일하게 유지합니다.
- ja는 바꾸지 말고 의미 판단용으로만 참고합니다.
- 한국어 번역은 원문보다 의미를 추가하거나 삭제하지 않습니다.
- 앞뒤 맥락에 맞게 존댓말/반말, 설명문/대화문 어투를 통일합니다.
- JLPT 문제 지시문과 선택지는 시험지 한국어처럼 간결하게 씁니다.
- Whisper 전사 때문에 원문이 어색해도, 임의로 큰 내용을 새로 만들지 말고 자연스러운 범위에서만 보정합니다.
- 출력은 JSON 객체 하나만 반환합니다.

출력 형식:
{{
  "items": [
    {{"id": "입력 id", "ko": "다듬은 한국어 번역"}}
  ]
}}

입력:
{source_blob}
""".strip()


def polish_entries(
    *,
    kind: str,
    group_id: str,
    title: str,
    section_title: str,
    entries: list[dict[str, str]],
    model: str,
    api_key: str,
    cache: dict[str, Any],
    retries: int,
    sleep_seconds: float,
    dry_run: bool,
) -> dict[str, str]:
    entries = [entry for entry in entries if compact_spaces(entry.get("ja"))]
    if not entries:
        return {}

    cache_key = f"{kind}:{group_id}:{model}"
    cached = cache.get(cache_key)
    if isinstance(cached, dict) and cached.get("input") == entries and isinstance(cached.get("output"), dict):
        return {str(k): str(v) for k, v in cached["output"].items()}

    prompt = build_prompt(kind, title, section_title, entries)
    if dry_run:
        return {entry["id"]: entry.get("ko", "") for entry in entries}

    response = gemini_request(prompt, model, api_key, retries, sleep_seconds)
    output_items = response.get("items", [])
    if not isinstance(output_items, list):
        raise ValueError(f"{group_id}: Gemini response has no items list")

    expected_ids = [entry["id"] for entry in entries]
    output = {compact_spaces(item.get("id")): compact_spaces(item.get("ko")) for item in output_items if isinstance(item, dict)}
    if set(output) != set(expected_ids):
        missing = sorted(set(expected_ids) - set(output))
        extra = sorted(set(output) - set(expected_ids))
        raise ValueError(f"{group_id}: id mismatch, missing={missing[:5]}, extra={extra[:5]}")

    original_by_id = {entry["id"]: compact_spaces(entry.get("ko", "")) for entry in entries}
    ordered_output = {item_id: output[item_id] or original_by_id.get(item_id, "") for item_id in expected_ids}
    if any(not ordered_output[item_id] for item_id in expected_ids):
        raise ValueError(f"{group_id}: empty polished translation returned")
    cache[cache_key] = {
        "input": entries,
        "output": ordered_output,
        "updated_at": datetime.now(timezone.utc).isoformat(),
    }
    save_cache(cache)
    return ordered_output


def apply_item_translations(items: list[dict[str, Any]], translations: dict[str, str]) -> int:
    changed = 0
    for item in items:
        item_id = str(item.get("index", ""))
        polished = translations.get(item_id)
        if polished and item.get("translation") != polished:
            item["translation"] = polished
            changed += 1
    return changed


def count_reading_groups(path: Path) -> int:
    payload = load_json(path)
    return sum(len(section.get("passages", [])) for section in payload.get("sections", []))


def count_listening_groups(path: Path) -> int:
    payload = load_json(path)
    return sum(len(section.get("tracks", [])) for section in payload.get("sections", []))


def polish_reading_file(
    path: Path,
    model: str,
    api_key: str,
    cache: dict[str, Any],
    retries: int,
    sleep_seconds: float,
    limit: int | None,
    dry_run: bool,
    progress_offset: int = 0,
    progress_total: int | None = None,
    only_id: str | None = None,
) -> int:
    payload = load_json(path)
    groups_done = 0
    changed = 0
    skipped = 0
    top_items = payload.get("items", [])
    top_by_index = {str(item.get("index")): item for item in top_items}
    local_total = count_reading_groups(path)
    effective_total = progress_total or local_total

    for section in payload.get("sections", []):
        for passage in section.get("passages", []):
            if only_id and passage.get("id") != only_id:
                continue
            if limit is not None and groups_done >= limit:
                break
            passage_items = passage.get("items", [])
            entries = [
                {
                    "id": str(item.get("index")),
                    "ja": compact_spaces(item.get("text")),
                    "ko": compact_spaces(item.get("translation")),
                }
                for item in passage_items
            ]
            group_id = f"{payload.get('id')}:{passage.get('id')}"
            progress_index = progress_offset + groups_done + 1
            cache_key = f"reading:{group_id}:{model}"
            cache_label = "cache" if cache_key in cache else "api"
            print(
                f"[{progress_index}/{effective_total}] [reading:{cache_label}] "
                f"{payload.get('title')} / {section.get('title')} / {passage.get('title')} ({len(entries)} items)",
                flush=True,
            )
            try:
                translations = polish_entries(
                    kind="reading",
                    group_id=group_id,
                    title=str(passage.get("title", "")),
                    section_title=str(section.get("title", "")),
                    entries=entries,
                    model=model,
                    api_key=api_key,
                    cache=cache,
                    retries=retries,
                    sleep_seconds=sleep_seconds,
                    dry_run=dry_run,
                )
            except Exception as exc:
                print(f"  [skip] {group_id}: {exc}")
                groups_done += 1
                skipped += 1
                continue
            group_changed = apply_item_translations(passage_items, translations)
            changed += group_changed
            for item_id, polished in translations.items():
                if item_id in top_by_index:
                    top_by_index[item_id]["translation"] = polished
            passage["translation"] = "\n".join(item.get("translation", "") for item in passage_items if item.get("translation"))
            groups_done += 1
            print(
                f"  [ok] changed={group_changed}, total_changed={changed}, skipped={skipped}",
                flush=True,
            )
            time.sleep(sleep_seconds)
        if limit is not None and groups_done >= limit:
            break

    payload["translation_polish"] = {
        "provider": "gemini",
        "model": model,
        "updated_at": datetime.now(timezone.utc).isoformat(),
    }
    if not dry_run:
        write_json(path, payload)
    print(f"[reading:done] {payload.get('title')} groups={groups_done}, changed={changed}, skipped={skipped}", flush=True)
    return changed


def polish_listening_file(
    path: Path,
    model: str,
    api_key: str,
    cache: dict[str, Any],
    retries: int,
    sleep_seconds: float,
    limit: int | None,
    dry_run: bool,
    progress_offset: int = 0,
    progress_total: int | None = None,
    only_id: str | None = None,
) -> int:
    payload = load_json(path)
    groups_done = 0
    changed = 0
    skipped = 0
    local_total = count_listening_groups(path)
    effective_total = progress_total or local_total

    for section in payload.get("sections", []):
        for track in section.get("tracks", []):
            if only_id and track.get("id") != only_id:
                continue
            if limit is not None and groups_done >= limit:
                break
            segments = track.get("segments", [])
            entries = [
                {
                    "id": str(segment.get("index")),
                    "ja": compact_spaces(segment.get("text")),
                    "ko": compact_spaces(segment.get("translation")),
                }
                for segment in segments
            ]
            group_id = str(track.get("id"))
            progress_index = progress_offset + groups_done + 1
            cache_key = f"listening:{group_id}:{model}"
            cache_label = "cache" if cache_key in cache else "api"
            print(
                f"[{progress_index}/{effective_total}] [listening:{cache_label}] "
                f"{section.get('title')} / {track.get('title')} ({len(entries)} segments)",
                flush=True,
            )
            try:
                translations = polish_entries(
                    kind="listening",
                    group_id=group_id,
                    title=str(track.get("title", "")),
                    section_title=str(section.get("title", "")),
                    entries=entries,
                    model=model,
                    api_key=api_key,
                    cache=cache,
                    retries=retries,
                    sleep_seconds=sleep_seconds,
                    dry_run=dry_run,
                )
            except Exception as exc:
                print(f"  [skip] {group_id}: {exc}")
                groups_done += 1
                skipped += 1
                continue
            group_changed = apply_item_translations(segments, translations)
            changed += group_changed
            groups_done += 1
            print(
                f"  [ok] changed={group_changed}, total_changed={changed}, skipped={skipped}",
                flush=True,
            )
            time.sleep(sleep_seconds)
        if limit is not None and groups_done >= limit:
            break

    payload["translation_polish"] = {
        "provider": "gemini",
        "model": model,
        "updated_at": datetime.now(timezone.utc).isoformat(),
    }
    if not dry_run:
        write_json(path, payload)
    print(f"[listening:done] groups={groups_done}, changed={changed}, skipped={skipped}", flush=True)
    return changed


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Polish JLPT Korean translations with Gemini using passage/problem context.")
    parser.add_argument("--reading", action="store_true", help="Polish reading DBs.")
    parser.add_argument("--listening", action="store_true", help="Polish listening DB.")
    parser.add_argument("--limit", type=int, help="Limit processed groups for smoke tests.")
    parser.add_argument("--only-id", help="Process only one passage id or listening track id.")
    parser.add_argument("--dry-run", action="store_true", help="Validate grouping without calling Gemini or writing files.")
    parser.add_argument("--model", default=os.getenv("GEMINI_MODEL", "gemini-3.1-flash-lite-preview"))
    parser.add_argument("--retries", type=int, default=4)
    parser.add_argument("--sleep", type=float, default=0.8)
    return parser.parse_args()


def main() -> int:
    load_dotenv(BASE_DIR / ".env")
    args = parse_args()
    api_key = os.getenv("GEMINI_API_KEY", "").strip()
    if not api_key and not args.dry_run:
        raise SystemExit("GEMINI_API_KEY is missing. Put it in .env or environment variables.")

    do_reading = args.reading or not args.listening
    do_listening = args.listening or not args.reading
    cache = load_cache()
    total_changed = 0
    total_groups = 0
    if do_reading:
        total_groups += sum(count_reading_groups(path) for path in READING_FILES if path.exists())
    if do_listening and LISTENING_FILE.exists():
        total_groups += count_listening_groups(LISTENING_FILE)

    print(
        json.dumps(
            {
                "model": args.model,
                "dry_run": args.dry_run,
                "target_groups": total_groups,
                "cache_groups": len(cache),
            },
            ensure_ascii=False,
        ),
        flush=True,
    )
    progress_offset = 0

    if do_reading:
        for path in READING_FILES:
            if path.exists():
                total_changed += polish_reading_file(
                    path,
                    args.model,
                    api_key,
                    cache,
                    args.retries,
                    args.sleep,
                    args.limit,
                    args.dry_run,
                    progress_offset=progress_offset,
                    progress_total=total_groups,
                    only_id=args.only_id,
                )
                progress_offset += count_reading_groups(path)
    if do_listening and LISTENING_FILE.exists():
        total_changed += polish_listening_file(
            LISTENING_FILE,
            args.model,
            api_key,
            cache,
            args.retries,
            args.sleep,
            args.limit,
            args.dry_run,
            progress_offset=progress_offset,
            progress_total=total_groups,
            only_id=args.only_id,
        )

    print(json.dumps({"changed_translations": total_changed, "model": args.model, "dry_run": args.dry_run}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
