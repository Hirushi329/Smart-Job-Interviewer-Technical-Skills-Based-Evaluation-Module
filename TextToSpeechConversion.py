from gtts import gTTS
import os
import time
from TextToSpeech import SpeechToText

def text_to_speech_conversion(question):
    language = 'en'
    myobj = gTTS(text=question, lang=language, slow=False)
    myobj.save("Question.mp3")
    os.system("Question.mp3")
    time.sleep(10)
    # answer = SpeechToText.speech_to_text_conversion()
    # return answer