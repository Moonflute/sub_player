from __future__ import annotations

import json
import re
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent
SOURCE_DIR = BASE_DIR / "_jlpt source" / "jlptN3_mocktest_separate"
REFINED_DIR = BASE_DIR / "_jlpt source refined"
LISTENING_INDEX = REFINED_DIR / "listening" / "n3_listening_review_index.json"
SUMMARY_PATH = REFINED_DIR / "summary.json"


def section_sort_key(path: Path) -> tuple[int, str]:
    match = re.match(r"(\d+)", path.name)
    return (int(match.group(1)) if match else 999, path.name)


def file_sort_key(path: Path) -> tuple[int, int, str]:
    match = re.search(r"문제(?P<problem>\d+)[^\d]+(?P<number>\d+)번", path.stem)
    if not match:
        return (999, 999, path.name)
    return (int(match.group("problem")), int(match.group("number")), path.name)


def display_title(path: Path) -> str:
    value = path.stem
    value = re.sub(r"^해커스N3", "해커스 N3 ", value)
    value = re.sub(r"실전모의고사(\d+)회", r"실전모의고사 \1회", value)
    value = re.sub(r"문제(\d+)_", r"문제\1_", value)
    return value


def build_mock_sections() -> list[dict]:
    if not SOURCE_DIR.exists():
        raise SystemExit(f"Mocktest source folder is missing: {SOURCE_DIR}")

    sections: list[dict] = []
    for section_index, section_dir in enumerate(sorted((p for p in SOURCE_DIR.iterdir() if p.is_dir()), key=section_sort_key), start=1):
        order_match = re.match(r"(?P<order>\d+)", section_dir.name)
        mock_order = int(order_match.group("order")) if order_match else section_index
        tracks = []
        for track_index, audio_path in enumerate(sorted(section_dir.glob("*.mp3"), key=file_sort_key), start=1):
            track_id = f"mocktest_{mock_order:02d}_{track_index:03d}"
            rel_path = audio_path.relative_to(BASE_DIR)
            tracks.append(
                {
                    "id": track_id,
                    "mode": "listening",
                    "level": "N3",
                    "section_order": 100 + mock_order,
                    "section_title": f"해커스 N3 실전모의고사 {mock_order}회",
                    "title": display_title(audio_path),
                    "source_audio": str(rel_path).replace("\\", "/"),
                    "file_size": audio_path.stat().st_size,
                    "transcript_status": "pending",
                    "transcript_file": "",
                    "segments": [],
                }
            )
        sections.append(
            {
                "order": 100 + mock_order,
                "title": f"해커스 N3 실전모의고사 {mock_order}회",
                "track_count": len(tracks),
                "tracks": tracks,
            }
        )
    return sections


def main() -> int:
    if not LISTENING_INDEX.exists():
        raise SystemExit("Listening index is missing. Build the base listening DB first.")

    payload = json.loads(LISTENING_INDEX.read_text(encoding="utf-8"))
    existing_sections = [
        section
        for section in payload.get("sections", [])
        if not str(section.get("title", "")).startswith("해커스 N3 실전모의고사 ")
    ]
    mock_sections = build_mock_sections()
    payload["sections"] = existing_sections + mock_sections
    payload["track_count"] = sum(len(section.get("tracks", [])) for section in payload["sections"])
    payload["mocktest_source"] = str(SOURCE_DIR.relative_to(BASE_DIR)).replace("\\", "/")

    LISTENING_INDEX.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")

    summary = json.loads(SUMMARY_PATH.read_text(encoding="utf-8")) if SUMMARY_PATH.exists() else {}
    summary["listening_track_count"] = payload["track_count"]
    summary["mocktest_listening_track_count"] = sum(len(section.get("tracks", [])) for section in mock_sections)
    SUMMARY_PATH.write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8")

    print(
        json.dumps(
            {
                "sections_added": len(mock_sections),
                "tracks_added": summary["mocktest_listening_track_count"],
                "total_tracks": payload["track_count"],
            },
            ensure_ascii=False,
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
