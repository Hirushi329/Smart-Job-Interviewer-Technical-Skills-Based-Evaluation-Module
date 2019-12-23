# Speech to text conversion

import speech_recognition as sr


def speech_to_text_conversion():
    recognizer = sr.Recognizer()
    harvard = sr.AudioFile('harvard.wav')
    with harvard as source:
        audio = recognizer.record(source)
        text = recognizer.recognize_google(audio)
        return text
    # print("The allocated time is over. Thank you!")
    # try:
    #     print("TEXT: " + recognizer.recognize_google(audio))
    # except:
    #     pass;
