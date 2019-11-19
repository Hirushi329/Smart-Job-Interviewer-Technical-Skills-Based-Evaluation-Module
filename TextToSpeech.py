from gtts import gTTS
import os

mytext = 'What is a null pointer exception in java, and how to fix it'
language = 'en'
myobj = gTTS(text=mytext, lang=language, slow=False)
myobj.save("Question.mp3")
os.system("Question.mp3")