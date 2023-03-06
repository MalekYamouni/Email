import smtplib
from pwinput import pwinput #verschlüsselt mein Passwort im Terminal
from email.mime.text import MIMEText
from tkinter import *



def Send():
    text = "Hallo das ist eine Email aus Python. Ich wünsche dir Frohe Weihnachten ho ho ho!!!\
        Mfg.\
        Malek <3 !" #dieser Text wird versendet
        
    username = input("Email: ")
    passw = pwinput("Password: ")
    empfänger = input("Empfänger: ")

    mail = MIMEText(text)
    mail['Subject'] = "Abdelmalek"
    mail['From'] = username
    mail['To'] = empfänger

    #smtpserver GMX.net = mail.gmx.net
       
    sender = smtplib.SMTP("mail.gmx.net", 587) #587 ist der SMTP Postausgangs Port
    sender.ehlo()   
    sender.starttls() # TLS ist ein Verschlüsselungsprotokoll Transport Layer Security/ SSL Secure Socket Layer ist der Vorgänger
    sender.ehlo()

    

    sender.login(username, passw)
    sender.send_message(mail)

    sender.close() #lib schließen

Send()