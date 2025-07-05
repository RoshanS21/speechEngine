# speechEngine

## Quick Start

1. Install dependencies:
   ```sh
   pip install -r requirements.txt
   brew install ffmpeg espeak  # for MP3 export and TTS phonemizer
   ```

2. Run the app:
   ```sh
   python app.py "Your text here"
   ```

## Requirements
- Python 3.11 or newer (Apple Silicon recommended)
- See `requirements.txt` for all Python dependencies
- Homebrew (for installing `ffmpeg` and `espeak`)

## Notes
- The default voice is a deep male (VCTK p225). You can change the speaker in `app.py`.
- For best performance, use on Apple Silicon (M1/M2/M3/M4).
- Audio will play automatically and you will be prompted to save as MP3 if desired.

---

### Troubleshooting
- If you see errors about missing `ffmpeg` or `espeak`, make sure you have installed them with Homebrew.
- No GUI is required or supported; this is a CLI-only app.