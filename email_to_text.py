#!/usr/bin/env python

# Import the following libs for sending the email
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
# Import json to read files 
import json
import random


#-------------------------------------FUNCTIONS GALORE--------------------------------------

def send_email(to_address="", from_address="", sender_password="", subject="", body=""):
    msg = MIMEMultipart()
    msg['From'] = from_address
    msg['To'] = to_address
    msg['Subject'] = subject
    message = body
    msg.attach(MIMEText(message))
    # Init server
    mailserver = smtplib.SMTP('smtp.gmail.com', 587)
    # Identify ourselves to smtp gmail client
    mailserver.ehlo()
    # Secure our email with tls encryption
    mailserver.starttls()
    # Re-identify ourselves as an encrypted connection
    mailserver.ehlo()
    mailserver.login(from_address, sender_password)

    mailserver.sendmail(from_address, to_address, msg.as_string())

    mailserver.quit()

# Consolidate all reusable code 
# Could be consolidated more actually 
def load_json_file(json_file_name):
    with open(json_file_name) as data_file:    
        data = json.load(data_file)
        return data


# make a dic file for list of common phone number endings
def carrier_ending():
    data = load_json_file('phone_carriers.json')
    return data['carriers']['metro']
    


# make a dic file for list of body statements
def body_comments():  
    data = load_json_file('body_comments.json')
    random_num = get_rand_num(0,5)
    return data['comments'][random_num]



# make a dic file for list of subject titles
def subjects():
    data = load_json_file('subject_list.json')
    random_num = get_rand_num(0,5)
    return data['headings'][random_num]



def get_rand_num(low_num, high_num):
    rand_num = random.randint(low_num, high_num)
    return rand_num



#-----------END FUNCTIONS


# -------------------------This works----------------------------


carrier = carrier_ending()

# Finally send the email
loop = 1
while loop > 0:
    try:
        to_address = 
        from_address = 
        password = 
        subject = subjects()
        body = body_comments()
        send_email(to_address, from_address, password, subject,
                   body)
        print '[+] sent message...'
        loop = loop - 1
    
    except smtplib.SMTPAuthenticationError:
        print "Could not verify email"
        break

#---------------End this works-----------------------------



