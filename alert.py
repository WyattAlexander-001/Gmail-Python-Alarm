import imaplib
import email
from playsound import playsound
import time
import os
print(os.getcwd())


def check_mail(username, password):
    mail = imaplib.IMAP4_SSL("imap.gmail.com")  # use IMAP4 protocol with SSL 
    mail.login(username, password) 
    mail.select("inbox") 

    # Search the inbox for all emails from .edu addresses
    result, data = mail.uid('search', None, '(FROM "@.edu")') 
    return len(data[0].split())  # return the number of .edu emails

def play_alarm():
    # replace alarm.mp3 with the path to your alarm sound file
    
    # Direct Path example:
    # playsound('H:\Projects\scripts\slowAlarm.mp3')
    playsound('sounds\slowAlarm.mp3')
def main():
    username = "SomeEmail@gmail.com"  # replace with your email
    password = "zznazxiiibryifxx"  # replace with your password

    # keep track of the number of emails at the start
    initial_count = check_mail(username, password)

    while True:
        try:
            current_count = check_mail(username, password)

            if current_count > initial_count:  
                play_alarm()
                initial_count = current_count

            time.sleep(60)  # wait for 60 seconds before checking again

        except Exception as e:
            print(f"An error occurred: {e}")
            time.sleep(60)

if __name__ == "__main__":
    main()