import speech_recognition as sr
import sounddevice as sd
import numpy as np
from scipy.io.wavfile import write

# sound = "OSR_us_000_0011_8k.wav"
def speech_to_text():
    fs = 44100  # Sample rate
    seconds = 15  # Duration of recording
    print("Start recording the answer.....")
    myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
    sd.wait()  # Wait until recording is finished
    write('output.wav', fs, myrecording.astype(np.int16))  # Save as WAV file in 16-bit format
    recognizer = sr.Recognizer()
    sound = "output.wav"

    with sr.AudioFile(sound) as source:
        recognizer.adjust_for_ambient_noise(source)
        print("Converting the answer to text...")
        audio = recognizer.listen(source)

        try:
            text = recognizer.recognize_google(audio)
            print("The converted text:" + text)
            return text

        except Exception as e:
            print(e)
            return e