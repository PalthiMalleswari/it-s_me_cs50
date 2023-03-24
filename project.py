#! python 3
# Name : Palthi Malleswari
# College : IIIT Nuzvid
# Couse : CS50's Introduction to python programming
# Country : India
# Mail merging using python
# Sending Emails to multiple users automatically
# This is a mail regarding our Organization's (E-CRUSH) called MindFest event promotions


import validators
import csv
import yagmail
from tabulate import tabulate
import sys

sender_mail=''
app_pass=''


# Sender Details
def sender_details(sender,pas):
    global sender_mail,app_pass

    #name=input('Enter your Name:')
    sender_mail=sender
    app_pass=pas
    if validate_mail(sender_mail):
        # set up connections
        #print(f"Hii {name} 🙃")
        return 1

    else:
        return 0

# to validate mails
def validate_mail(mail):
    if validators.email(mail):
        return True
    else:
        return False

#working with the csv file to get list of mailID's to send
def getting_receivers():

    sender_mail=input('Enter Sender Email Address: ')
    app_pass='zufyjdcrowrbbsws'

    # Checking Sender Details
    if sender_details(sender_mail,app_pass):
        print('verified')
    else:
        print('Sorry..😕\nCheck your Email😓')
        sys.exit('Invalid Requirements')

    # Reading data from csv file using DictReader

    file=open('simple.csv','r')
    read=csv.DictReader(file)

    receivers=[]

    for row in read:
        mail=row['Email']
        id=row['ID']
        if validate_mail(mail):
            user_mail=mail
            user_message=messages(id)
            print('Sending Mail to '+id+' ......')
            send_Email(user_mail,user_message)      # sends mail to each user in the csv file
            receivers.append([user_mail])


        else:

            sys.exit(mail+' is not a valid email')

    print(tabulate(receivers,headers=['Receivers List'],tablefmt='grid'))
    file.close()


def messages(id):

    # Body of the mail

    body=f"""
            Hello, {id} 🤗 !\n\n
            Our E-Crush is back with an interesting 😀 event
            to be conducted on 8th March,
            on the occasion of women's day 👩🏻 and holy 🎨.
            every event brings a change to be better .🤩
            come with your team to set the stage on fire 🥳.
            Let's blast this HOLI and WOMENS day together ..😇
            Make it a way to raise your knowledge higher 🌟.
            Register now and burn out all your fear 🔥
            <a href="https://forms.gle/L1AyvjzFUboEeJpZ8">Register Here </a>
        """
    return body

def send_Email(receiver,body):
    global sender_mail,app_pass
    filename="mind_fest.jpg"

    try:

            yag = yagmail.SMTP(sender_mail,app_pass)
            yag.send(
                to=receiver,
                subject="Mind Fest Event by E-Crush🤩",
                contents=body,
                attachments=filename,
                )
            return f"Sent Successfully"

    except :
         raise AttributeError('Authentication Error')


def main():
    print('\n\n!!........Sending Multiple Emails 📧.........!!')
    print()

    getting_receivers()
    print('.............................Thank You🥰................................ ')

if __name__ == "__main__":
    main()
