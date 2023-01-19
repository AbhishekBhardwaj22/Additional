#DAIS-Do As I Say

import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

print(voices)

engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour < 12:
        speak("Good Morning")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon")
    
    else:
        speak("Good Evening")
    speak("I am DAIS")

def takecommand():
    """This function will take voice input from User"""
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio , language = 'en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print("Say that again please..")
        return "None"
    return query

def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login("dais322Agmail.com","#helloworld@322")
    server.sendmail("abhishekbh327@gmail.com",to,content)
    server.close()

if __name__ == "__main__":
    wishme()
    while True:
        query = takecommand().lower()

        if 'wikipedia' in query:
            speak('Searching wikipedia..')
            query = query.replace('wikipedia','')
            results = wikipedia.summary(query,sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open('youtube.com')

        elif 'google' in query:
            webbrowser.open('google.com')

        elif 'play music' in query:
            music= "A:\D\Abhishek Bhardwaj\Phone Cloud\songs"
            songs = os.listdir(music)
            print(songs)
            os.startfile(os.path.join(music,songs[0]))

        elif "current time" in query:
            strtime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Current,Time is {strtime}") 

        elif 'send email' in query:
        #For this you require a dictionary with name and emails as key and value pairs
            try:
                speak("What should I Say?")
                content = takecommand()
                to = "abhishekbh326@gmail.com"
                sendEmail(to,content)

            except Exception as e:
                print(e)
                speak("Sorry I can't send your mail at this moment")

# Future Scope: Combining ML and many functions with DAIS
