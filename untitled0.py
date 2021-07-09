import pyttsx3 #For Speak
import datetime 
import speech_recognition as sr 

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def time_():
    Time=datetime.datetime.now().strftime("%H:%M:%S") #for 24 hour clock
    speak("the current time is")
    speak(Time)
    Time=datetime.datetime.now().strftime("%I:%M:%S") # for 12-hour clock
    speak(Time)
def date():
    year = (datetime.datetime.now().year)
    month = (datetime.datetime.now().month)
    date = (datetime.datetime.now().day)
    speak("the current date is")
    speak(date)
    speak(month)
    speak(year)
def wishme():
    speak("Welcome back Rohit!")
    time_()
    date()
    hour = datetime.datetime.now().hour
    if hour >=6 and hour<12:
        speak("Good Morning Sir")
    elif hour >=12 and hour<18:
        speak("Good Afternoon Sir!")
    elif hour >=18 and hour <24:
        speak("Good Evening Sir!")
    else:
        speak("Good Night Sir!")
    speak("Jarvis at your service. Please tell me how can I help you?")

def TakeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-US')
        print(query)
        
    except Exception as e:
        print(e)
        print("Say that again please...")
        return "None"
    return query

TakeCommand()