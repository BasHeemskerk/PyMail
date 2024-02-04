from scripts import Status
from scripts import Debug
import time
import keyboard

def editSettings():

    Debug.clear()
    Debug.log("Editing Settings.")

    print("On this screen you can configure various PyMail settings.")
    print("\n\nDo you want to log PyMail? (y/n)")
    print("\n\nCurrently: " + str(Status.mustLog))
    if (keyboard.is_pressed('y')):
        Status.mustLog = True
    elif (keyboard.is_pressed('n')):
        Status.mustLog = False
    

