import speech_recognition as sr
from googletrans import Translator

r = sr.Recognizer()
with sr.Microphone() as source:
    print("Say something!")
    audio = r.listen(source)
try:
    print("You said: " + r.recognize_google(audio))
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
    print(
    "Could not request results from Google Speech Recognition service; {0}".format(
        e))

translator = Translator()
translations = translator.translate([r.recognize_google(audio)], dest='ko')
for translation in translations:
    print(translation.text)
