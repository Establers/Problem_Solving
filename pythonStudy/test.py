import speech_recognition as sr
# print(sr.__version__)
r = sr.Recognizer()
mic = sr.Microphone()

with mic as source :
    audio = r.listen(source)

r.recognize_google(audio)



