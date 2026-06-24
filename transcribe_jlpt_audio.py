from __future__ import annotations

import argparse
import json
import os
import shutil
import time
from pathlib import Path

import main as engine
from build_webapp import build_translation_map, clean_translation, serialize_grammar, serialize_vocab

BASE_DIR = Path(__file__).resolve().parent
REFINED_DIR = BASE_DIR / "_jlpt source refined"
LISTENING_INDEX = REFINED_DIR / "listening" / "n3_listening_review_index.json"
TRANSCRIPT_DIR = REFINED_DIR / "listening" / "transcripts"
WHISPER_MODEL_DIR = BASE_DIR / ".whisper_models"


def load_whisper():
    try:
        import imageio_ffmpeg

        ffmpeg_path = Path(imageio_ffmpeg.get_ffmpeg_exe())
        WHISPER_MODEL_DIR.mkdir(parents=True, exist_ok=True)
        ffmpeg_alias = WHISPER_MODEL_DIR / "ffmpeg.exe"
        if not ffmpeg_alias.exists():
            shutil.copy2(ffmpeg_path, ffmpeg_alias)
        os.environ["PATH"] = f"{ffmpeg_alias.parent}{os.pathsep}{ffmpeg_path.parent}{os.pathsep}{os.environ.get('PATH', '')}"
    except Exception:
        pass

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


def analyze_segments(segments: list[dict], translate: bool) -> list[dict]:
    sentences = [segment["text"] for segment in segments if segment.get("text")]
    translation_map = build_translation_map(sentences, translate) if translate else {sentence: "" for sentence in sentences}

    engine.ensure_reference_database(BASE_DIR)
    vocab_index, grammar_entries, hackers_reference = engine.load_reference_data_from_database(BASE_DIR)

    from janome.tokenizer import Tokenizer

    tokenizer = Tokenizer()
    enriched: list[dict] = []
    for segment in segments:
        text = segment.get("text", "")
        analysis = engine.analyze_sentence(
            text,
            translation_map,
            tokenizer,
            vocab_index,
            grammar_entries,
            hackers_reference,
        )
        enriched.append(
            {
                **segment,
                "translation": clean_translation(translation_map.get(text, "")),
                "vocab_matches": [serialize_vocab(item) for item in analysis.vocab_matches] if analysis else [],
                "grammar_matches": [serialize_grammar(item) for item in analysis.grammar_matches] if analysis else [],
            }
        )
    return enriched


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


def merge_track_transcript(track: dict, transcript: dict) -> None:
    transcript_file = f"listening/transcripts/{track['id']}.json"
    track["transcript_status"] = "complete"
    track["transcript_file"] = transcript_file
    track["transcript_model"] = transcript.get("model", "")
    track["language"] = transcript.get("language", "ja")
    track["text"] = transcript.get("text", "")
    track["segments"] = transcript.get("segments", [])


def has_segment_translations(track: dict) -> bool:
    segments = track.get("segments", [])
    return bool(segments) and all(segment.get("translation") for segment in segments)


def write_index(index_payload: dict) -> None:
    tmp_path = LISTENING_INDEX.with_suffix(".json.tmp")
    content = json.dumps(index_payload, ensure_ascii=False, indent=2)
    tmp_path.write_text(content, encoding="utf-8")
    for attempt in range(1, 6):
        try:
            tmp_path.replace(LISTENING_INDEX)
            return
        except PermissionError:
            if attempt == 5:
                LISTENING_INDEX.write_text(content, encoding="utf-8")
                try:
                    tmp_path.unlink(missing_ok=True)
                except OSError:
                    pass
                return
            time.sleep(0.4 * attempt)


def count_complete_tracks(index_payload: dict) -> int:
    return sum(
        1
        for section in index_payload.get("sections", [])
        for track in section.get("tracks", [])
        if track.get("transcript_status") == "complete" and track.get("segments")
    )


def count_complete_selected_tracks(tracks: list[dict]) -> int:
    return sum(1 for track in tracks if track.get("transcript_status") == "complete" and track.get("segments"))


def main() -> int:
    parser = argparse.ArgumentParser(description="Transcribe refined JLPT listening audio with Whisper.")
    parser.add_argument("--model", default="small", choices=["small", "medium"])
    parser.add_argument("--language", default="ja")
    parser.add_argument("--limit", type=int, default=None)
    parser.add_argument("--only-id", default="")
    parser.add_argument("--only-prefix", default="")
    parser.add_argument("--no-translate", action="store_true")
    parser.add_argument("--overwrite", action="store_true")
    args = parser.parse_args()

    if not LISTENING_INDEX.exists():
        raise SystemExit("Listening index is missing. Run refine_jlpt_sources.py first.")

    whisper = load_whisper()
    WHISPER_MODEL_DIR.mkdir(parents=True, exist_ok=True)
    model = whisper.load_model(args.model, download_root=str(WHISPER_MODEL_DIR))
    TRANSCRIPT_DIR.mkdir(parents=True, exist_ok=True)

    index_payload = json.loads(LISTENING_INDEX.read_text(encoding="utf-8"))
    tracks = list(iter_tracks(index_payload, args.limit))
    if args.only_id:
        tracks = [track for track in tracks if track["id"] == args.only_id]
    if args.only_prefix:
        tracks = [track for track in tracks if str(track.get("id", "")).startswith(args.only_prefix)]

    total_tracks = len(tracks)
    for order, track in enumerate(tracks, start=1):
        out_path = TRANSCRIPT_DIR / f"{track['id']}.json"
        if (
            out_path.exists()
            and track.get("transcript_status") == "complete"
            and has_segment_translations(track)
            and not args.overwrite
        ):
            completed = count_complete_selected_tracks(tracks)
            remaining = max(0, total_tracks - completed)
            percent = completed / total_tracks * 100 if total_tracks else 100
            print(f"[skip] {order}/{total_tracks} {track['id']} already complete | done={completed} remaining={remaining} {percent:.1f}%")
            continue

        if out_path.exists() and not args.overwrite:
            transcript = json.loads(out_path.read_text(encoding="utf-8"))
            print(f"[cached] {order}/{total_tracks} {track['id']} <- {out_path}")
        else:
            print(f"[start] {order}/{total_tracks} {track['id']}")
            transcript = transcribe_track(model, track, args.language)
            print(f"[transcribed] {order}/{total_tracks} {track['id']} segments={len(transcript.get('segments', []))}")

        transcript["model"] = args.model
        transcript["segments"] = analyze_segments(transcript.get("segments", []), translate=not args.no_translate)
        out_path.write_text(json.dumps(transcript, ensure_ascii=False, indent=2), encoding="utf-8")
        merge_track_transcript(track, transcript)
        write_index(index_payload)
        completed = count_complete_selected_tracks(tracks)
        remaining = max(0, total_tracks - completed)
        percent = completed / total_tracks * 100 if total_tracks else 100
        print(f"[merged] {order}/{total_tracks} {track['id']} -> {out_path}")
        print(f"[progress] done={completed}/{total_tracks} remaining={remaining} {percent:.1f}%")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
