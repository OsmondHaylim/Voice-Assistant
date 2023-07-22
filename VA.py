import pyttsx3 as tts
import speech_recognition as sr
import webbrowser
import datetime
import os
import pywhatkit
import pyjokes
import wikipedia

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 0.8
        audio = r.listen(source) 
        
        try:
            q = r.recognize_google(audio, language="en")
            return q
        except sr.UnknownValueError:
            print("X")
            return "I am waiting"
        except sr.RequestError:
            print("Sorry, service is down")
            return "I am waiting"
        except:
            return 'I am waiting'
        
def speak(message):
    engine = tts.init()
    newVoiceRate = 155
    engine.setProperty('rate',newVoiceRate)
    print(f'{message}')
    engine.say(message)
    engine.runAndWait()

def query_day():
    day = datetime.date.today() #YYYY-MM-DD
    weekday = day.weekday() #Range 0-6 (Mon-Sun)
    mapping = {0:'Monday', 1:'Tuesday', 2:'Wednesday', 3:'Thursday', 4:'Friday', 5:'Saturday', 6:'Sunday'}
    try:
        speak(f'Today is {mapping[weekday]}')
    except:
        pass

def query_time():
    hour = datetime.datetime.now().hour
    minute = datetime.datetime.now().minute
    if hour == 0:
        speak(f'It is 12 {minute} A M')
    elif hour >= 12:
        speak(f'It is {hour-12} {minute} P M')
    else:
        speak(f'It is {hour} {minute} A M')

def hello(name = None):
    if name == None:
        speak('Hello. I am Mona. How may I help you?')
    else:
        speak(f'Hello {name}. I am Mona. How may I help you?')

def main():
    hello()
    start = True
    while(start):
        q = listen().lower()
        if q == 'hello':
            hello()
            continue
        elif 'what' and 'time' in q:
            query_time()
            continue
        elif 'what' in q and 'day' in q:
            query_day()
            continue
        elif 'start' in q and 'youtube' in q:
            speak('opening youtube. Just a second')
            webbrowser.open('https://www.youtube.com')
            continue
        elif 'start' in q and 'google' in q:
            speak('opening google. Just a second')
            webbrowser.open('https://www.google.com')
            continue
        elif 'wikipedia' in q:
            q = q.replace('wikipedia','')
            speak(f'checking wikipedia for {q}')
            result = wikipedia.summary(q, sentences=2)
            speak(result)
            continue
        elif 'search web' in q:
            q = q.replace('search web','')
            speak(f'searching {q} from web')
            pywhatkit.search(q)
            continue
        elif 'play' in q:
            q = q.replace('play','')
            speak(f'searching {q} from youtube')
            pywhatkit.playonyt(q)
            continue
        elif 'joke' in q:
            speak(pyjokes.get_joke())
            continue
        elif 'stop' in q or 'bye' in q:
            speak('Mona is offline')
            start = False

main()