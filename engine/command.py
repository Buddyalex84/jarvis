import pyttsx3
import speech_recognition as sr
import eel
def speak(text):
    engine = pyttsx3.init('sapi5')
    voices=engine.getProperty('voices')
    engine.setProperty('voice',voices[1].id)
    engine.setProperty('rate',175)
    print(voices)
    engine.say(text)
    engine.runAndWait()
@eel.expose
def takecommand():
    r=sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening....")
        eel.DisplayMessage("listening...")
        r.pause_threshold=1
        r.adjust_for_ambient_noise(source)
        audio=r.listen(source,10,6)
    try:
        print("recognizing")
        eel.DisplayMessage("recognizing...")
        query=r.recognize_google(audio,language='en-in')
        print(f"user said:{query}\n")
        eel.DisplayMessage(query)

        speak(query)
    except Exception as e:
        print(e)
        print("say that again please")
        return "none"
    return query

