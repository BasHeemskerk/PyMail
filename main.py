import time
import os.path

from scripts import MSG
from scripts import Status
from scripts import Splash
from scripts import Debug
from scripts import addCredentials
from scripts import Settings

def __mainLoop__():
    if (Status.SplashScreen):
        Splash.showSplash()
    elif (Status.EditSettings):
        Settings.editSettings()
    elif (Status.AddedCredentials == False and Status.AddingCredentials == False):
        checkingForCredentials()
    elif (Status.AddedCredentials == False and Status.AddingCredentials == True):
        addCredentials.startAddingCredentials()
    elif(Status.SettingUp):
        MSG.setupMail()
    
    time.sleep(0.01)

    __mainLoop__()

def checkingForCredentials():
    if (os.path.exists(Status.InfoFolderLocation + "email.pymail") and os.path.exists(Status.InfoFolderLocation + "password.pymail")):
        Status.AddedCredentials = True
    else:
        Status.AddedCredentials = False
        Debug.log("Credentials Exist: False")
        Status.AddingCredentials = True 


__mainLoop__()