import speech_recognition as sr
from time import ctime
import webbrowser
import time
import playsound
import os
import random
import datetime
from gtts import gTTS

r = sr.Recognizer()

def record_audio(ask= False):
    with sr.Microphone() as source:
        if(ask):
            jarvis_speak(ask)
            print("Listening...")
            audio = r.listen(source)
            voice_data = " "
            try:
                voice_data = r.recognize_google(audio)
            except sr.UnknownValueError:
                jarvis_speak("sorry , i didnt get that")
            except sr.RequestError:
                jarvis_speak("sorry , i cant do not that")
            return voice_data
        
def jarvis_speak(audio_string):
    tts = gTTS(text=audio_string ,lang = 'en',slow = False)
    r = random.randint(1,1000000)
    audio_file = 'audio-' +str() +'.mp3'
    tts.save(audio_file)
    playsound.playsound(audio_file)
    print(audio_string)
    os.remove(audio_file)
    
def respond(voice_data):
    if 'who are you' or 'describe yourself' in voice_data:
        jarvis_speak("i'm jarvis , i'm rohit's voice assistant")
    if 'what is your name' in voice_data:
        jarvis_speak("my name is jarvis")
    if 'what time is it' in voice_data:
        jarvis_speak(ctime())
    if 'search' in voice_data:
        search = record_audio('what do you want to search for')
        url = 'https://google.com/search?q='+ search
        webbrowser.get().open(url)
        jarvis_speak("Here what i found for"+ search)
    if "find location" in voice_data:
        location=record_audio("what is the location")
        url='https://google.com/maps/place/'+ location
        webbrowser.get().open(url)
        jarvis_speak("here is the location"+ location)
    if 'exit' in voice_data:
        jarvis_speak('thank you have a nice day')
        exit()
        
def greetme():
    currentH = int(datetime.datetime.now().hour)
    if currentH >= 10 and currentH < 3:
        jarvis_speak("hi sir, good morning, How can i help you ?")
    if currentH >= 3 and currentH < 15:
        jarvis_speak("hi sir, good afternoon, How can i help you ?")
    if currentH <=15 and currentH != 19:
        jarvis_speak("hi sir, good evening, How can i help you ?")
    if currentH >=19 and currentH != 10:
        jarvis_speak("hi sir, good night, How can i help you ?")
        
time.sleep(1)
greetme()
while 1:
    voice_data = record_audio()
    respond(voice_data)
    
            