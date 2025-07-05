import PySimpleGUI as sg
from TTS.api import TTS
from pydub import AudioSegment
from pydub.playback import play
import tempfile
import os

# Initialize TTS (using a deep male voice model)
tts = TTS(model_name="tts_models/en/vctk/vits", progress_bar=False, gpu=False)

layout = [
    [sg.Text('Enter text to synthesize:')],
    [sg.Multiline(size=(60, 10), key='-TEXT-')],
    [sg.Button('Synthesize & Play'), sg.Button('Save as MP3'), sg.Exit()]
]

window = sg.Window('Text-to-Speech (TTS) - Deep Male Voice', layout)

def synthesize(text, out_path):
    tts.tts_to_file(text=text, file_path=out_path, speaker="p225")  # p225 is a deep male voice

def play_audio(path):
    audio = AudioSegment.from_file(path)
    play(audio)

while True:
    event, values = window.read()
    if event in (sg.WIN_CLOSED, 'Exit'):
        break
    if event == 'Synthesize & Play':
        text = values['-TEXT-'].strip()
        if text:
            with tempfile.NamedTemporaryFile(suffix='.wav', delete=False) as tmp:
                synthesize(text, tmp.name)
                play_audio(tmp.name)
                os.unlink(tmp.name)
    if event == 'Save as MP3':
        text = values['-TEXT-'].strip()
        if text:
            save_path = sg.popup_get_file('Save MP3', save_as=True, file_types=(('MP3 Files', '*.mp3'),))
            if save_path:
                with tempfile.NamedTemporaryFile(suffix='.wav', delete=False) as tmp:
                    synthesize(text, tmp.name)
                    audio = AudioSegment.from_file(tmp.name)
                    audio.export(save_path, format='mp3')
                    os.unlink(tmp.name)
                sg.popup('Saved!', f'Audio saved to {save_path}')

window.close()
