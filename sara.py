import wikipedia
import pyttsx3
import datetime
import speech_recognition as sr
from googletrans import Translator
import cv2


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
        speak("Good Morning.")

    elif hour>=12 and hour<18:
        speak("Good Afternoon.")
         
    else:
        speak("Good Evening.")

    speak("I am sara. please tell me how may I help you")

def translate_speech(src, target_language):
    r = sr.Recognizer()
    translator = Translator()
    
    with sr.Microphone() as source:
        speak("Speak something...")
        audio = r.listen(source)
        
    try:
        text = r.recognize_google(audio, language=src)
        speak(text)
        
        translation = translator.translate(text, src=src, dest=target_language)
        translated_text = translation.text
        
        print("your translation is:")
        speak(translated_text)
        
    except sr.UnknownValueError:
        speak("Unable to recognize speech.")
    except sr.RequestError as e:
        speak("Error:", e)

# Example usage
src = "en"  # English can be altered to any languages 
target_language = "kn"  # spanish can be altered to any languages 


def takeCommand():
    #it takes microphone inut from user and gives string op

    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 0.9 #noise control
        audio =r.listen(source)
    
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in') # type: ignore
        print(f"User said:{query}\n")

    except Exception as e:
       # print(e)
        print("say that again, I did not get you")
        return ":"
    return query

if __name__ =="__main__":
    wishMe()
    permit = input(speak("shall I capture a picture for the medical record purpose? press 'y' for yes and 'n' for no"))
    if permit == 'y':
            cap = cv2.VideoCapture(0)

            if not cap.isOpened():
              print("Error: Could not open webcam, permission denied or module aint present")
              exit()

            ret, frame = cap.read()

            cv2.imshow('Captured Image', frame)
            cv2.waitKey(2000)
            cv2.destroyAllWindows()  
            # Save the captured image to a file
            cv2.imwrite('D:\\My codes and programs\\IIT hackathon\\database\\captured_image.jpg', frame)
        # Release the VideoCapture and close the OpenCV window
            cap.release()
            cv2.destroyAllWindows()
        
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

        elif 'information' in query:
             usr = input(speak("please state your name:"))
             speak("Hello".format(usr))
             dob = input(speak("plese state your date of birth:"))
             gender = input("plese state your gender:")


        elif 'translate for me' in query:
            translate_speech(src, target_language)
        
        elif 'go to sleep' in query:
            quit()