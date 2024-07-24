import speech_recognition as sr
import subprocess
import pywhatkit
import pyttsx3
import datetime
import webbrowser
import threading

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
    if 'hello' in command:
        text = speak("Hello! How can I help you today?")
        print(f"Sifra said: {text}")
    
    elif 'name' in command:
        text = speak("My name is SIFRA !!!")
        print(f"Sifra said: {text}")
    
    elif 'time' in command:
        now = datetime.datetime.now()
        text = speak(f"The time is {now.strftime('%I:%M %p')}")
        print(f"Sifra said: {text}")
        
    elif 'date' in command:
        today = datetime.date.today()
        text = speak(f"Today is {today.strftime('%B %d, %Y')}")
        print(f"Sifra said: {text}")
        
    elif 'chrome' in command:
        text = speak("Opening Chrome...")
        print(f"Sifra said: {text}")
        program = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
        subprocess.Popen([program])
    
    elif 'sublime' in command:
        text = speak("Opening sublime text editor...")
        print(f"Sifra said: {text}")
        program = r'C:\Program Files\Sublime Text 3\sublime_text.exe'
        subprocess.Popen([program])
        
    elif 'play' in command:
        song = command.replace('play', '', 1).strip()
        text = speak(f"Playing {song} on YouTube...")
        pywhatkit.playonyt(song)
        print(f"Sifra said: {text}")
      
    elif 'morning' in command:
        text = speak("good morning, Have a nice day!") 
        print(f"Sifra said: {text}") 
      
    elif 'afternoon' in command:
        text = speak("Good afternoon")
        print(f"Sifra said {text}")
        
    elif 'night' in command:
        text = speak("Good Night, sweat dreams ")
        print(f"Sifra said: {text}")
        
    elif "youtube" in command:
        webbrowser.open("http://www.youtube.com")
        text = speak(f"opening youtube")
        print(f"SIFRA said: {text}")
        
    elif "google" in command:
        webbrowser.open("http://www.google.com")
        text = speak(f"opening google")
        print(f"SIFRA said: {text}")
    
    elif "wikipedia" in command:
        webbrowser.open("www.wikipedia.com")
        text = speak("opening wikipedia")
        print(f"SIFRA said: {text}")
    
    elif 'good bye' in command:
        text = speak("Goodbye!")
        print(f"Sifra said: {text}")
        exit()
        
    else:
        
        text = speak("I'am not sure how to do that.")
        print(f"Sifra said: {text}")

def main():
    text = speak("SIFRA IS CREATED BY ASHISH MAHAMUNI")
    print(f"Sifra said: {text}")
    text=speak("Voice assistant activated. How can I assist you?")
    print(f"Sifra said: {text}")
    while True:
        command = listen()
        if command:
            respond(command)
        
if __name__ == "__main__":
    main()
