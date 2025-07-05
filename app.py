import sys
from TTS.api import TTS
from pydub import AudioSegment
import tempfile
import os

# Initialize TTS (using a deep male voice model)
tts = TTS(model_name="tts_models/en/vctk/vits", progress_bar=False, gpu=False)

def synthesize(text, out_path):
    tts.tts_to_file(text=text, file_path=out_path, speaker="p317")  # p317 is a deep male voice

def play_audio(path):
    audio = AudioSegment.from_file(path)
    audio.export("/tmp/tts_output.mp3", format="mp3")
    os.system(f"afplay /tmp/tts_output.mp3")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python app.py 'Your text here'")
        sys.exit(1)
    text = sys.argv[1]
    with tempfile.NamedTemporaryFile(suffix='.wav', delete=False) as tmp:
        synthesize(text, tmp.name)
        play_audio(tmp.name)
        save_path = input("Save MP3 as (leave blank to skip): ")
        if save_path:
            if not save_path.lower().endswith('.mp3'):
                save_path += '.mp3'
            audio = AudioSegment.from_file(tmp.name)
            audio.export(save_path, format='mp3')
            print(f"Audio saved to {save_path}")
        os.unlink(tmp.name)
