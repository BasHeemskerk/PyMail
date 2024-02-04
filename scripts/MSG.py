import smtplib, ssl, os, mimetypes
from pathlib import Path
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email import encoders
from email.mime.base import MIMEBase
from email.mime.application import MIMEApplication
from email.header import Header

from scripts import Debug
from scripts import Status
from scripts import Encrypt
#from scripts import Zipper
    
AttachmentFolderLocation = Status.AttachmentFolderLocation
InfoFolderLocation = Status.InfoFolderLocation


def setupMail():

    Debug.clear()
    Debug.log("Setting up email")
    Debug.log("Attachments folder files: " + str(os.listdir(AttachmentFolderLocation)))
    Debug.log("Info folder files: " + str(os.listdir(InfoFolderLocation)))
    Debug.log("Credentials Exist: True")

    email = open(str(InfoFolderLocation + "email.pymail"), "r")
    password = open(str(InfoFolderLocation + "password.pymail"), "r")

    Sender = email.read()
    Password = str(Encrypt.decryptPassword(str(password.read())))

    smtp_server = "smtp.gmail.com"
    port = 465

    print("From: " + Sender)
    Reciever = input("To: ")
    Subject = input("Subject: ")
    print("")
    Header = input ("Header: ")
    Middle = input ("Message: ")
    End = input ("Footer: ")
    print("")
    Attachments = input("Include attachments? (confirm/deny): ")
    if (Password == ""):
        print("")
        Password = input("Password: ")
    else:  
        print("")
        print("Password: *auto-filled via file*")

    if (Attachments == "deny" or Attachments == ""):
        send(smtp_server, port, Sender, Reciever, Subject, Header, Middle, End, Password)
    elif (Attachments == "confirm"):
        sendWithAddedAttachments(smtp_server, port, Sender, Reciever, Subject, Header, Middle, End, Password)

    #os.close(email)
    #os.close(password)

def send(smtp_server, port, sender, reciever, subject, header, middle, end, Password):
    if (Status.SentMail == False):
        finalMessage = "From: " + sender + "\nTo: " + reciever + "\nSubject: " + subject + "\n\nMessage: \n\n" + header + "\n\n" + middle + "\n\n" + end + "\n\nSent from PyMail;\nMade by Bas Heemskerk."
        Debug.log("MESSAGE: \n" + finalMessage)
        Debug.log("CREDENTIALS: \n" + sender + "\n" + str(Encrypt.encryptPassword(Password)))

        context = ssl.create_default_context()

        with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
            server.login(sender, Password)
            server.sendmail(sender, reciever, finalMessage)
                


        SentMail = True

def sendWithAddedAttachments(smtp_server, port, sender, reciever, subject, header, middle, end, Password):

    if (Status.SentMail == False):

        finalMessage = header + "\n\n" + middle + "\n\n" + end + "\n\nSent from PyMail;\nMade by Bas Heemskerk"

        finalMessageMime = MIMEMultipart()

        finalMessageMime["From"] = sender
        finalMessageMime["To"] = reciever
        finalMessageMime["Subject"] = subject

        part1 = (MIMEText(finalMessage, 'plain'))

        filename = Status.AttachmentFolderLocation + "attachment.zip"
        attachment = open(Status.AttachmentFolderLocation + "attachment.zip", "rb")

        part2 = MIMEBase('application', 'octet-stream')
        part2.set_payload((attachment).read())
        encoders.encode_base64(part2)
        part2.add_header('Content-Disposition', "attachment; filename= %s" % filename)

        finalMessageMime.attach(part1)
        finalMessageMime.attach(part2)

        context = ssl.create_default_context()


        with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
            #server.starttls()
            server.login(sender, Password)
            server.sendmail(sender, reciever, finalMessageMime.as_string())

