from text_speech import *
import pyautogui as gui
import time
import random 
import pyttsx3
text_speech = pyttsx3.init()
class show_zoom():
    def run (self):
        gui.click(1755,20,duration=0.5)
        gui.click(x=950, y=666,duration=0.2) 
        gui.hotkey('win','m')
        time.sleep(1)
        gui.hotkey('ctrl','alt','1')
        gui.click(x=735, y=461,duration=0.2)
        sentense = random.choice(["There you have it , have a nice meeting !"])
        text_speech.say(sentense)
        text_speech.runAndWait()
        text_speech.say("Is there anything else i can help you with?")
        text_speech.runAndWait()
class google_it():
    def run(self):
        gui.click(1755,20,duration=0.5)
        gui.click(x=950, y=666,duration=0.2) 
        gui.hotkey('win','m')
        time.sleep(1)
        gui.hotkey('ctrl','alt','2')
        sentense = random.choice(["what would you like me to search","Okay lets google it, what say you ","Sure let surf it , whats your question ?"])
        say = TextToSpeech(sentense)
        say.run()
        resp = SpeechToText()
        text = resp.run()
        gui.typewrite(text)
        gui.hotkey('enter')
        sentense = random.choice(["Here's something I found","okay lets look it up"])
        text_speech.say(sentense)
        text_speech.runAndWait()