import speech_recognition as sr # pip install speechrecognition
import pyttsx3 # pip install pyttsx3
import datetime # in- built no need to install
import wikipedia # pip install wikipedia
import webbrowser # in-built
import os # in- built
import pyjokes # pip install pyjokes
'''note ----> pyaudio may not work in python latest versions(3.9 & 3.10). 
if you face any problem installing pyaudio you need to downgrade your python version to 3.6 or 3.7'''
import pyaudio # pip install pyaudio 
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id) # voices[1].id will enable the Female Voice

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour <=12:
        speak("Good Morning")
    elif hour >= 12 and hour <18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("I am Jarvis sir, Please tell me  how may I help You")
def takeCommand(): # defining the command function here
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio,language = "en-in")
        print(f"User Said: {query}\n")
    except Exception as e:
        # print(e)
        print("Say that again...")
        return "None"
    return query
if _name_ == "_main_":
    wishMe()
    # while True:
    if 1:
        query = takeCommand().lower()
        if 'wikipedia' in query:
            speak ('searching wikipedia...')
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query,sentences=2)
            speak("according to wikipedia")
            print(results)
            speak(results) 
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")
        elif'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"sir, the time is {strTime}")
            print(strTime)
        
        elif'open code' in query:
            codePath = "C:\\Users\\DELL\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath) 
        elif 'joke' in query:
            jokes = pyjokes.get_joke()
            speak(f"Here you go: {jokes}")

            print(jokes)