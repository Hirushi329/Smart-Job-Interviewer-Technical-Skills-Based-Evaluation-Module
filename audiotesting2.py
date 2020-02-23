import numpy as np
from scipy.io.wavfile import write
import sounddevice as sd

fs = 44100  # Sample rate
seconds = 5  # Duration of recording
myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
sd.wait()  # Wait until recording is finished
write('output.wav', fs, myrecording.astype(np.int16))  # Save as WAV file in 16-bit format