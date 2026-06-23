from __future__ import annotations

import argparse
import json
import shutil
import subprocess
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent
REFINED_DIR = BASE_DIR / "_jlpt source refined"
LISTENING_INDEX = REFINED_DIR / "listening" / "n3_listening_review_index.json"
OUTPUT_AUDIO_DIR = REFINED_DIR / "listening" / "audio"


def resolve_ffmpeg() -> str:
    ffmpeg = shutil.which("ffmpeg")
    if ffmpeg:
        return ffmpeg
    try:
        import imageio_ffmpeg
    except ImportError as exc:
        raise SystemExit(
            "ffmpeg was not found. Install imageio-ffmpeg or put ffmpeg.exe on PATH, then rerun."
        ) from exc
    return imageio_ffmpeg.get_ffmpeg_exe()


def iter_tracks(index_payload: dict):
    for section in index_payload.get("sections", []):
        for track in section.get("tracks", []):
            yield track


def compress_track(ffmpeg: str, track: dict, bitrate: str, sample_rate: int, overwrite: bool) -> dict:
    source_path = BASE_DIR / track["source_audio"]
    output_path = OUTPUT_AUDIO_DIR / f"{track['id']}.mp3"
    output_path.parent.mkdir(parents=True, exist_ok=True)

    if overwrite or not output_path.exists():
        cmd = [
            ffmpeg,
            "-y" if overwrite else "-n",
            "-i",
            str(source_path),
            "-vn",
            "-ac",
            "1",
            "-ar",
            str(sample_rate),
            "-b:a",
            bitrate,
            str(output_path),
        ]
        subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    updated = dict(track)
    updated["compressed_audio"] = str(output_path.relative_to(REFINED_DIR)).replace("\\", "/")
    updated["site_audio"] = f"data/jlpt/{updated['compressed_audio']}"
    updated["compressed_bitrate"] = bitrate
    updated["compressed_sample_rate"] = sample_rate
    updated["compressed_file_size"] = output_path.stat().st_size
    return updated


def main() -> int:
    parser = argparse.ArgumentParser(description="Compress JLPT listening MP3 files for GitHub Pages.")
    parser.add_argument("--bitrate", default="48k")
    parser.add_argument("--sample-rate", type=int, default=22050)
    parser.add_argument("--limit", type=int, default=None)
    parser.add_argument("--overwrite", action="store_true")
    args = parser.parse_args()

    if not LISTENING_INDEX.exists():
        raise SystemExit("Listening index is missing. Run refine_jlpt_sources.py first.")

    ffmpeg = resolve_ffmpeg()
    payload = json.loads(LISTENING_INDEX.read_text(encoding="utf-8"))
    processed = 0
    total_size = 0

    for section in payload.get("sections", []):
        new_tracks = []
        for track in section.get("tracks", []):
            if args.limit is not None and processed >= args.limit:
                new_tracks.append(track)
                continue
            updated = compress_track(ffmpeg, track, args.bitrate, args.sample_rate, args.overwrite)
            processed += 1
            total_size += updated["compressed_file_size"]
            print(f"[audio] {processed:03d} {track['id']} {updated['compressed_file_size'] / 1024 / 1024:.2f}MB")
            new_tracks.append(updated)
        section["tracks"] = new_tracks

    payload["compressed_audio_bitrate"] = args.bitrate
    payload["compressed_audio_sample_rate"] = args.sample_rate
    payload["compressed_audio_total_size"] = sum(
        int(track.get("compressed_file_size", 0))
        for track in iter_tracks(payload)
    )
    LISTENING_INDEX.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")

    summary_path = REFINED_DIR / "summary.json"
    if summary_path.exists():
        summary = json.loads(summary_path.read_text(encoding="utf-8"))
    else:
        summary = {}
    summary["compressed_audio_bitrate"] = args.bitrate
    summary["compressed_audio_track_count"] = sum(1 for track in iter_tracks(payload) if track.get("compressed_audio"))
    summary["compressed_audio_total_size"] = payload["compressed_audio_total_size"]
    summary_path.write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8")

    print(
        json.dumps(
            {
                "processed": processed,
                "total_compressed_mb": round(payload["compressed_audio_total_size"] / 1024 / 1024, 2),
            },
            ensure_ascii=False,
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
