import webbrowser
import wikipedia
import pyttsx3
import os
import datetime
import speech_recognition as sr
from googletrans import Translator


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning Sir!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon, Sir.")
         
    else:
        speak("Good Evening, Sir.")

    speak("I am sara. please tell me how may I help you")

def translate_speech(source_language, target_language):
    r = sr.Recognizer()
    translator = Translator()
    
    with sr.Microphone() as source:
        speak("Speak something...")
        audio = r.listen(source)
        
    try:
        text = r.recognize_google(audio, language=source_language)
        speak(text)
        
        translation = translator.translate(text, src=source_language, dest=target_language)
        translated_text = translation.text
        
        print("your translation is:")
        speak(translated_text)
        
    except sr.UnknownValueError:
        speak("Unable to recognize speech.")
    except sr.RequestError as e:
        speak("Error:", e)

# Example usage
source_language = "en"  # English //can be altered to any languages 
target_language = "ka"  # spanish //can be altered to any languages 


def takeCommand():
    #it takes microphone input from user and gives string op

    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 0.9 #noise control
        audio =r.listen(source)
    
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said:{query}\n")

    except Exception as e:
       # print(e)
        print("say that again, I did not get you")
        return "None"
    return query

if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()
    #logic for task execution

        if 'wikipedia' in query:
            speak("looking into Wikipedia...")
            query = query.replace("Wikipedia","")
            results = wikipedia.summary(query,sentences=2) #try wiki
            speak("Wikipedia says...")
            print(results)
            speak(results)

        #website section 
        if 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'open maharaja institute website' in query:
            webbrowser.open('https://www.mit.edu/')
        elif 'open stack overflow' in query:
            webbrowser.open("stackoverflow.com")
        elif 'play some music' in query:
            webbrowser.open('spotify.com')
        elif 'show me way in map' in query:
            webbrowser.open('maps.google.com/maps')
        elif 'open canva' in query:
            webbrowser.open('https://www.canva.com/design/DAFmkzRelpM/mv4e-NrphvzKeXnnD9IgOA/edit')
        elif 'download songs' in query:
            webbrowser.open('https://www.pagalworld.com.se/find/Hindi/1.html')
        elif 'my college website' in query:
            webbrowser.open('https://vidyavikasengineering.com/')
        elif 'my mails' in query:
            webbrowser.open('https://mail.google.com/mail/u/0/')
        elif 'news' in query:
            webbrowser.open('https://www.google.com/search?q=latest+news&rlz=1C1RXQR_enIN1015IN1015&oq=latest+news&gs_lcrp=EgZjaHJvbWUyBggAEEUYOTINCAEQABiDARixAxiABDIMCAIQABgUGIcCGIAEMgYIAxAAGAMyEAgEEAAYgwEYsQMYyQMYgAQyCggFEAAYkgMYigUyCggGEAAYkgMYigUyDQgHEAAYgwEYsQMYgAQyBggIEAAYAzINCAkQABiDARixAxiABNIBDjEyNDA4Njk3NmowajE1qAIAsAIA&sourceid=chrome&ie=UTF-8')
        elif 'buy things' in query:
            webbrowser.open('https://www.amazon.in/')
        elif 'hotels nearby' in query:
            webbrowser.open('https://www.google.com/maps/search/hotels+in+mysore/@12.3201616,76.6225026,14z/data=!3m1!4b1?entry=ttu')
        elif 'famous places' in query:
            webbrowser.open('https://www.google.com/maps/search/hotels+in+mysore/@12.3201616,76.6225026,14z/data=!3m1!4b1?entry=ttu')
        
        #directory section
        elif 'play music' in query:
            music_dir = 'D:\\music'   
            songs = os.listdir(music_dir)   
            print(songs)
            os.startfile(os.path.join(music_dir,songs[0]))

        elif 'translate for me' in query:
            translate_speech(source_language, target_language)
        
        elif 'go to sleep' in query:
            quit()


            