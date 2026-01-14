import vosk
import json
import pyaudio
from agent import run, off
import atexit
from dotenv import dotenv_values

atexit.register(off)
config = dotenv_values(".env")

model = vosk.Model(config["VOICE_CLIENT_VOSK_MODEL"])
recognizer = vosk.KaldiRecognizer(model, 16000)

if __name__ == "__main__":
    p = pyaudio.PyAudio()
    stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8000)
    stream.start_stream()

    while True:
        data = stream.read(4000)
        if recognizer.AcceptWaveform(data):
            result = json.loads(recognizer.Result())
            if 'text' in result:
                text = result['text']
                if config["VOICE_CLIENT_ACTIVATION"] in text:
                    command = text.split(config["VOICE_CLIENT_ACTIVATION"], 1)[1].strip()
                    run(command)
