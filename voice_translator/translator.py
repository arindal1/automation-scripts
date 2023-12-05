import speech_recognition as sr
from langdetect import detect
from google_trans_new import google_translator
import pyttsx3

r = sr.Recognizer()
translator = google_translator()


def SpeakText(command):
    # Initialize the engine
    engine = pyttsx3.init()
    engine.say(command)
    engine.runAndWait()


def trans(x, d):
    s = detect(x)
    result = translator.translate(x, lang_src=s, lang_tgt=d)
    return result


print("Start speaking.....(To terminate the program say 'Exit' or 'Quit')")
while True:
    try:
        with sr.Microphone() as source2:
            r.adjust_for_ambient_noise(source2, duration=0.2)
            audio2 = r.listen(source2)
            MyText = r.recognize_google(audio2).lower()

            if MyText in ['exit', 'quit']:
                break

            print("Did you say " + MyText)
            target_language = input("Enter the language you need the text to be translated into:").lower()
            translated_text = trans(MyText, target_language)
            print(translated_text)

            # Speak the translated text
            SpeakText(translated_text)

    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))
    except sr.UnknownValueError:
        print("Unknown error occurred")
