import pyttsx3
import speech_recognition as sr
class TextToSpeech():
    def __init__(self,sentense):
        self.sentense = sentense
    def run(self):
        text_speech = pyttsx3.init()
        # answer = input("say smthin : ")
        text_speech.say(self.sentense)
        text_speech.runAndWait()

class SpeechToText():
    def run(self):
        recog = sr.Recognizer()
        with sr.Microphone() as source :
            recog.adjust_for_ambient_noise(source)
            print("Say something  : ")
            ask = TextToSpeech("Hi there how can i help you ?")
            audio = recog.listen(source)
            text = recog.recognize_google(audio)
            try:
                print("you have said : ", text)

            except Exeception as e :
                print("Please try again : ", str(e))
                l = TextToSpeech(sentense = "Hmmm couldn't get you, can you repeat that . ")
                l.run()
                a = SpeechToText()
                a.run()
        return text

class SpeechToText_actions():
    def run(self):
        recog = sr.Recognizer()
        with sr.Microphone() as source:
            audio = recog.listen(source)
            text = recog.recognize_google(audio)
            print(f"you have said : {text}")
            try:
                return texthi
            except Exception as e:
                l = TextToSpeech(sentense = "Hmmm couldn't get you, can you repeat that . ")
                l.run()
                a = SpeechToText_actions()
                a.run()
                
class Stealth_listening():
    def run (self):
        recog = sr.Recognizer()
        with sr.Microphone() as source:
            try:
                print("inn")
                audio = recog.listen(source)
                print("listening")
                text = recog.recognize_google(audio)
                print("prompt : ", text)
                return text
            except Exception as e:
                # a = Stealth_listening()
                # a.run()
                print(e)

# text = SpeechToText()
# a=text.run()
# print(a)