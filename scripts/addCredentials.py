from scripts import Debug
from scripts import Encrypt
from scripts import Status

def startAddingCredentials():
    Debug.clear()
    Debug.error("Credentials Exist: False", 1)
    print("Add your email credentials down here.")
    print("If you wish to enter your password manually everytime you start the program, leave the field 'Password' empty. (Safer)\n")
    email = input("Email: ")
    password = input ("Password: ")

    emailFile = open(str(Status.InfoFolderLocation + "email.pymail"), "a")
    passwordFile = open(str(Status.InfoFolderLocation + "password.pymail"), "a")

    emailFile.write(email)
    passwordFile.write(str(Encrypt.encryptPassword(password)))

    emailFile.close()
    passwordFile.close()

    Debug.log("Credentials have been created!")

    Status.AddedCredentials = True
    Status.AddingCredentials = False
    Status.SettingUp = True



