import sounddevice as sd
import speech_recognition as sr
import wavio as wavio
from scipy.io.wavfile import write
import numpy as np

fs = 4400  # Sample rate
seconds = 5  # Duration of recording
print("Start recording the answer.....")
# myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
x = np.int(seconds*fs)
myrecording = sd.rec(x, samplerate=fs, channels=2)
sd.wait()  # Wait until recording is finished
write('output.wav', fs, myrecording.astype(np.int8))  # Save as WAV file in 16-bit format
recognizer = sr.Recognizer()
sound = "output.wav"

with sr.AudioFile(sound) as source:
    recognizer.adjust_for_ambient_noise(source)
    print("Converting the answer to text...")
    audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio)
        print("The converted text:" + text)

    except Exception as e:
        print('error')