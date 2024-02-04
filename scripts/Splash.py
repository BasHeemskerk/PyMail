import time
import os
import keyboard

from scripts import Status
from scripts import Debug

def showSplash():
    Debug.writeSessionTime()
    Debug.clear()
    Debug.log("At splash screen.")

    print("\nWelcome to PyMail!")
    print("Version: " + Status.version)
    print("\nMade by Bas Heemskerk")

    #print("\n\nPress 'S' to open PyMail Settings.")

    #if (keyboard.is_pressed('s')):
        #Debug.log("Open settings")
        #Status.EditSettings = True

    time.sleep(5)

    if Status.EditSettings == False:
        Status.SplashScreen = False
        Status.SettingUp = True