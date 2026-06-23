from __future__ import annotations

import argparse
import json
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent
REFINED_DIR = BASE_DIR / "_jlpt source refined"
LISTENING_INDEX = REFINED_DIR / "listening" / "n3_listening_review_index.json"
TRANSCRIPT_DIR = REFINED_DIR / "listening" / "transcripts"


def load_whisper():
    try:
        import whisper
    except ImportError as exc:
        raise SystemExit(
            "Whisper is not installed. Install openai-whisper first, then rerun this script. "
            "Use --model small first; use --model medium only if the transcript quality is not enough."
        ) from exc
    return whisper


def iter_tracks(index_payload: dict, limit: int | None):
    count = 0
    for section in index_payload.get("sections", []):
        for track in section.get("tracks", []):
            yield track
            count += 1
            if limit is not None and count >= limit:
                return


def transcribe_track(model, track: dict, language: str) -> dict:
    audio_path = BASE_DIR / track["source_audio"]
    result = model.transcribe(str(audio_path), language=language, verbose=False)
    segments = [
        {
            "index": index,
            "start_seconds": float(segment.get("start", 0.0)),
            "end_seconds": float(segment.get("end", 0.0)),
            "text": str(segment.get("text", "")).strip(),
        }
        for index, segment in enumerate(result.get("segments", []), start=1)
        if str(segment.get("text", "")).strip()
    ]
    return {
        "id": track["id"],
        "mode": "listening",
        "level": track.get("level", "N3"),
        "title": track["title"],
        "section_title": track.get("section_title", ""),
        "source_audio": track["source_audio"],
        "model": getattr(model, "name", ""),
        "language": language,
        "text": str(result.get("text", "")).strip(),
        "segments": segments,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Transcribe refined JLPT listening audio with Whisper.")
    parser.add_argument("--model", default="small", choices=["small", "medium"])
    parser.add_argument("--language", default="ja")
    parser.add_argument("--limit", type=int, default=None)
    parser.add_argument("--only-id", default="")
    args = parser.parse_args()

    if not LISTENING_INDEX.exists():
        raise SystemExit("Listening index is missing. Run refine_jlpt_sources.py first.")

    whisper = load_whisper()
    model = whisper.load_model(args.model)
    TRANSCRIPT_DIR.mkdir(parents=True, exist_ok=True)

    index_payload = json.loads(LISTENING_INDEX.read_text(encoding="utf-8"))
    tracks = list(iter_tracks(index_payload, args.limit))
    if args.only_id:
        tracks = [track for track in tracks if track["id"] == args.only_id]

    for track in tracks:
        transcript = transcribe_track(model, track, args.language)
        out_path = TRANSCRIPT_DIR / f"{track['id']}.json"
        out_path.write_text(json.dumps(transcript, ensure_ascii=False, indent=2), encoding="utf-8")
        print(f"[transcribed] {track['id']} -> {out_path}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
