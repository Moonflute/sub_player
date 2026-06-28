# Whisper / Torch setup notes

This project does not need `torch` for the deployed web app.

`torch` is only needed when regenerating listening data from MP3 files with
`transcribe_jlpt_audio.py`.

## Current transcription setup

- Transcription script: `transcribe_jlpt_audio.py`
- Whisper package used: `openai-whisper`
- Model used for the existing listening DB: `small`
- Local model file: `.whisper_models/small.pt`
- Previous PyTorch install: `torch 2.5.1+cu121`
- CUDA runtime: `12.1`
- GPU mode: used automatically when `torch.cuda.is_available()` is true
- Translation during transcription: Google batch translation via the existing pipeline

The project policy for JLPT listening transcription is:

- Start with `small`.
- Use `medium` only if transcript quality is clearly not good enough.
- Do not use larger Whisper models for this project.

## Commands used

Typical full run:

```powershell
python transcribe_jlpt_audio.py --model small --only-prefix mocktest_d_
```

Single-track retry:

```powershell
python transcribe_jlpt_audio.py --model small --only-id mocktest_d_01_015
```

After transcription, rebuild the static site:

```powershell
python build_webapp.py --skip-show-db
```

## Reinstalling later

For GPU transcription, install Whisper and a CUDA PyTorch build again.

```powershell
python -m pip install openai-whisper
python -m pip install torch --index-url https://download.pytorch.org/whl/cu121
```

Then verify:

```powershell
python -c "import torch; print(torch.__version__); print(torch.cuda.is_available()); print(torch.version.cuda)"
```

If GPU transcription is not needed, install a CPU-only PyTorch build instead,
but expect Whisper transcription to be much slower.
