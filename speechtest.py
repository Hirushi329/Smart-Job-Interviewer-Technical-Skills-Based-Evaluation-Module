import speech_recognition as sr

sound = "OSR_us_000_0011_8k.wav"
recognizer = sr.Recognizer()

with sr.AudioFile(sound) as source:
    recognizer.adjust_for_ambient_noise(source)
    print("Converting audio file to text...")
    audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio)
        print("The converted text:" + text)

    except Exception as e:
        print(e)