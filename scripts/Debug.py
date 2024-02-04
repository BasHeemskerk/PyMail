import os
import time
import datetime

from scripts import Status
from scripts import Encrypt

def log(message):
    if (Status.mustDebug):
        print("---DEBUG.LOG---")
        print(message)
        print("---------------")

    if (Status.mustLog):
        writelogfile(message, 0)

        #time.sleep(3)

def error(message, ID):
    print("---ERROR.LOG---")
    print(message + ", code: " + str(ID))
    print("---------------")

    if (Status.mustLog):
        writelogfile(message, ID)

    time.sleep(3)

def writeSessionTime():
    debugFile = open(str(Status.InfoFolderLocation + "log.txt"), "a")
    debugFile.write("\n---Session: " + str(datetime.datetime.now()) + "---")

def writelogfile(message, ID):
    debugFile = open(str(Status.InfoFolderLocation + "log.txt"), "a")
    if (ID == 0):
        debugFile.write("\n")
        debugFile.write("DEBUG.LOG: ")
        debugFile.write(message)
    else:
        debugFile.write("\n")
        debugFile.write("ERROR.LOG: ")
        debugFile.write(message + ", code: " + str(ID))


def clear():
    os.system('cls')
