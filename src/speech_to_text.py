# speech_to_text.py
import speech_recognition as sr

def record_and_convert():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Talk")
        audio_text = r.listen(source, 10 , 4)
        print("Time over, thanks")

    try:
        return r.recognize_google(audio_text)
    except:
        print("Did not understand, please try again.")
        return ""

if __name__ == '__main__':
    record_and_convert()
