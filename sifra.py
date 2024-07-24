import speech_recognition as sr
import subprocess
import pywhatkit
import pyttsx3
import datetime
import webbrowser
import os

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
recognizer = sr.Recognizer()

def speak(text):
    engine.say(text)
    engine.runAndWait()
    return text

def listen():
    
    with sr.Microphone() as source:
        print("Please wait...")
        recognizer.adjust_for_ambient_noise(source, duration=0.2)
        print("Listening...")
        recordaudio = recognizer.listen(source)
    
    try:
        command = recognizer.recognize_google(recordaudio).lower()
        print("You said: " + command)
        
        
    except sr.UnknownValueError:
        text = speak("Sorry, I did not understand that.")
        print(f"Sifra said: {text}")
        return None
    return command

def respond(command):
    if 'play' in command:
        song = command.replace('play', '', 1).strip()
        text = speak(f"Playing {song} on YouTube...")
        pywhatkit.playonyt(song)
        print(f"Sifra said: {text}")
        return
        
    else:
        now =datetime.datetime.now()
        today = datetime.date.today()
        responses =[
            ["hello","Hello! How can I help you today?"],
            ["name","My name is SIFRA!"],
            ["morning","good morning, Have a nice day!"],
            ["afternoon","good afternoon"],
            ["night","good night"],
            ["time",f"The time is {now.strftime('%I:%M %p')}"],
            ["date",f"Today is {today.strftime('%B %d, %Y')}"],
            ["good bye","Goodbye!"]]
        
        for response in responses:
            if response[0] in command:
                text =speak(response[1])
                print(f"SIFRA said: {text}")
                
                if response[0] == "good bye":
                    exit()
                else:
                    return
                
        programs = [
            ["chrome", r'C:\Program Files\Google\Chrome\Application\chrome.exe'],
            ["sublime", r'C:\Program Files\Sublime Text 3\sublime_text.exe'],
            ["eclipse", r'C:\Users\hp\eclipse\java-2022-06\eclipse\eclipse.exe'],
            ["visual code studio", r'C:\Users\hp\AppData\Local\Programs\Microsoft VS Code\Code.exe'],
            ["pycharm", r"C:\Program Files\JetBrains\PyCharm 2023.2.3\bin\pycharm64.exe"],
            ["edge", r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"],
            ["xamp",r"C:\xamppX\xampp-control.exe"]
        ]
        
        for prog in programs:
            if f"open {prog[0]}" in command:
                text = speak(f"Opening {prog[0]}...")
                print(f"Sifra said: {text}")
                subprocess.Popen([prog[1]])
                return
        
        sites = [
            ["youtube", "https://www.youtube.com"], 
            ["wikipedia", "https://www.wikipedia.com"], 
            ["google", "https://www.google.com"]
            ]
        
        for site in sites:
            if f"open {site[0]}" in command:
                webbrowser.open(site[1])
                text = speak(f"Opening {site[0]}")
                print(f"Sifra said: {text}")
                return
            
        processes =[
            ["shutdown","shutdown /s /t 1"],
            ["restart", "shutdown /r /t 1"],
            ["sleep", "rundll32.exe powrprof.dll,SetSuspendState 0,1,0"]
        ]
        
        for process in processes:
            if process[0] in command:
                text = speak(f"{process[0]} the computer")
                print(f"SIFRA said {process[0]}")
                os.system(process[1])
                return
        
        text = speak("I'am not sure how to do that.")
        print(f"Sifra said: {text}")

def main():
    text = speak("Hiii, Myself SIFRA")
    print(f"Sifra said: {text}")
    text=speak("SIFRA Voice assistant activated. How can I assist you?")
    print(f"Sifra said: {text}")
    while True:
        command = listen()
        if command:
            respond(command)
        
if __name__ == "__main__":
    main()