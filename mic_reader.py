import os 
import time
import playsound
import speech_recognition as sr 
from gtts import gTTS
import webbrowser


def speak(text):
    tts = gTTS(text = text, lang="en")
    filename = "voice1.mp3"
    tts.save(filename)
    playsound.playsound(filename)

def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.record(source, duration=4)
        said = ""
        try:
            said = r.recognize_google(audio)
            print(said)
        except Exception as e:
            print("Exception: " + str(e))
    return said

#speak("hello world")
text = get_audio()



if "hello" and "open silicon valley" in text.lower():
    print("hello, oppening silicon valley in microsoft edge")
    speak("hello, openning silicon valley in microsoft edge")
    webbrowser.open("https://english-films.co/serialy-na-angliyskom/9638-silikonovaya-dolina-sezon-1-silicon-valley-season-1-2014-hd-720-ru-eng.html", new = 1)