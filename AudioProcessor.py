from gtts import gTTS
import time
import os

def speak(mytext):
    if mytext.strip():
        language = 'en'
        myobj = gTTS(text=mytext, lang=language, slow=False)
        myobj.save("temp/audio.mp3")
        os.system("afplay temp/audio.mp3")
        os.system("rm temp/audio.mp3")
