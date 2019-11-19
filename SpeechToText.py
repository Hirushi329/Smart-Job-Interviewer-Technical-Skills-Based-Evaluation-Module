# Speech to text conversion

import speech_recognition as sr

recognizer = sr.Recognizer()
harvard = sr.AudioFile('harvard.wav')
with harvard as source:
    # print("Say something");
    audio = recognizer.record(source)
    recognizer.recognize_google(audio)
    # print("The allocated time is over. Thank you!")
    # try:
    #     print("TEXT: " + recognizer.recognize_google(audio))
    # except:
    #     pass;
