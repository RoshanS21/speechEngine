# speechEngine

## Quick Start

1. Install dependencies:
   ```sh
   pip install -r requirements.txt
   brew install ffmpeg  # for MP3 export
   ```

2. Run the app:
   ```sh
   python app.py
   ```

## Requirements
- Python 3.11 or newer (Apple Silicon recommended)
- See `requirements.txt` for all Python dependencies

## Special Notes
- PySimpleGUI must be installed from the private server:
  ```sh
  python -m pip install --upgrade --extra-index-url https://PySimpleGUI.net/install PySimpleGUI
  ```
- All other dependencies are installed via:
  ```sh
  pip install -r requirements.txt
  ```

## Notes
- The default voice is a deep male (VCTK p225). You can change the speaker in `app.py`.
- For best performance, use on Apple Silicon (M1/M2/M3/M4).