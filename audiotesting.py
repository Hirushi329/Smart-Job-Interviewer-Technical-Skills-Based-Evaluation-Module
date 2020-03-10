import pydub
import speech_recognition as sr
import sounddevice as sd
from pydub import AudioSegment
import numpy as np
import os
from scipy.io.wavfile import write
from TextToSpeech.hiru import run

fs = 44100  # Sample rate
seconds = 5  # Duration of recording
print("Start recording the answer.....")
myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
sd.wait()  # Wait until recording is finished
write('output.wav', fs, myrecording)  # Save as WAV file in 16-bit format
sound = 'output.wav'
run(sound)