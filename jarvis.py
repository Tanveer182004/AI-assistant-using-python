import os
import webbrowser
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import smtplib


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")
    
    else:
        speak("Good Evening!")
    
    speak("I am Jarvis Sir ! Please tell me how may I help you ?")

def takeCommand():
    #It takes microphone input from user and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold  = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio,language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)
        print("Say that again again please...")
        return "None"
    return query
def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com, 587')
    server.ehlo()
    server.starttls()
    server.login('engineeringwallah83@gmail.com', 'Tanveerengineer')
    server.sendmail('engineeringwallah83@gmail.com',to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
    # while True:
    if 1:
        query = takeCommand().lower()

        #Logic for executing tasks based on query
        if 'wikipedia'in query:
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query,sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        elif 'open youtube'in query:
            webbrowser.open("youtube.com")

        elif 'open google'in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow'in query:
            webbrowser.open("stackoverflow.com")

        elif 'play music'in query:
            music_dir = 'C:\\Users\\vanita\\Desktop\\music\\my music'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'open code'in query:
            codePath = "C:\\Users\\vanita\\AppData\\Local\\Programs\\Common\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'email to tanveer' in query:
            try:
                speak("What should I say ?")
                content = takeCommand()
                to = "engineeringwallah83@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent !")
            except Exception as e:
                #print(e)
                speak("not sent !")
        
        elif 'open winword' in query:
            codePath = "C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE"
            os.startfile(codePath)

        elif 'open Turbo C'in query:
            codePath = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Turbo C++\\Turbo C++ 3.2"
            os.startfile(codePath)