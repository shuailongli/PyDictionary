from gtts import gTTS
import speech_recognition as sr
import time
import os

def listen(label="Event"):
    r = sr.Recognizer()
    while(1):
        with sr.Microphone() as source:
            #print(label+" listening")
            audio = r.listen(source)
            try:
                #print(" recognizing")
                mytext=r.recognize_google(audio)
                #print("you said " + mytext)
                return mytext
            except sr.UnknownValueError:
                #print(label+" could not understand audio")
                1
            except sr.RequestError as e:
                #print(label+" error; {0}".format(e))
                1


def speak(mytext):
    if mytext.strip():
        language = 'en'
        myobj = gTTS(text=mytext, lang=language, slow=False)
        myobj.save("temp/audio.mp3")
        os.system("afplay temp/audio.mp3")
        os.system("rm temp/audio.mp3")
