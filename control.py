import pyautogui as gui
import time
from text_speech import *
import pyttsx3
import speech_recognition as sr
def zoom_meeting(mail_id,paswd):
    # gui.click(1755,20,duration=0.5)
    # # c=gui.locateCenterOnScreen('./res/zoom.png')
    # # if c:
    # #     gui.click(c,clicks=2,duration=0.5)
    # #     gui.hotkey('win','up')
    # # else:
    # #     for i in range(3):
    # gui.click(x=950, y=666,duration=0.2) 
    # gui.hotkey('win','m')
    # time.sleep(1)
    # gui.hotkey('ctrl','alt','1')
    # time.sleep(3.8)
    # gui.click(x=742, y=80,duration=0.5)
    # gui.hotkey('win','up')
    gui.click(x=742, y=61,duration=1)
    gui.click(x=754, y=437,duration=0.5)
    time.sleep(1.2)
    gui.typewrite(mail_id)
    time.sleep(0.5)
    gui.hotkey('tab')
    time.sleep(0.5)
    gui.hotkey('tab')
    time.sleep(0.7)
    #gui.hotkey('fn',"left")
    #gui.typewrite("12B_10_")
    gui.hotkey('tab')
    time.sleep(0.5)
    gui.hotkey('tab')
    gui.hotkey('space')
    time.sleep(0.5)
    gui.hotkey('tab')
    gui.hotkey('space')
    # gui.click(x=1018, y=736,duration=0.5)
    # gui.click(x=730, y=478,duration=1.5)
    time.sleep(1.6)
    gui.typewrite(paswd) 
    time.sleep(0.5)
    gui.hotkey('tab')
    time.sleep(0.5)
    #gui.click(x=961, y=741,duration=0.5)
    gui.hotkey('space')

def details(n):
    Id = {'man':"976 142 1394","Phy":"252 345 5438","Chem":"353 266 1350","Eng":"609 056 2835","Cs":"901 468 1675","Pe":"","Prashant sir":"7920653270","Shija":"706 882 3941","Meher aunty":"496 033 0314"}
    Pass = {'man':"hzlzm95","Phy":"sriP123","Chem":"A2020z","Eng":"a","Cs":"12mi34an","Pe":"","Shija":"667775","Prashant sir":"qwertypkr","Meher aunty":"Meher"}
    i,p = Id[n],Pass[n]
    return i,p
def zoom_join():
    c=0
    while c!=1:
        c+=1
        sentense = "what meeting would you like to join"
        say = TextToSpeech(sentense)
        say.run()
        resp = SpeechToText()
        text = resp.run()
        print(text)
        #n = input("which lesson next : ")
        i,p = details(text)
        # t = float(input("When is your sesson (in minitues): "))
        # for j in range(1,int(t+1)):
        #     time.sleep(60)
        #     print(j)
        zoom_meeting(i,p)
        # if c==4:
        #     if input("I suggest you to stop the prg for the device to cool down , do you wanna quit (y/n) : ")=='y':
        #         break
        #     c=0
        time.sleep(2)
        say = TextToSpeech("Happy meeting !")
        say.run()

            