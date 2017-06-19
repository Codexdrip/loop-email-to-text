#!/usr/bin/env python
# program name: Lovely text
# purpose: Sends a nice text message to an email or phone number
# date: 4/5/17 1:22am
# author: star_shelz

# Import argparse for reading command line args
import argparse
# Import getparse for reading passwords invisibly
import getpass
# Import the following libs for sending the email
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
# Import json to read files 
import json
import pprint
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



# make a dic file for different emails addresses and loop through all addresses
def phone_numbers():
    data = load_json_file('phone_nums.json')
    carrier = carrier_ending()
    for key in data:   #same thing as using x.keys()
        print data[key] + '@metropcs.com'


# Consolidate all reusable code 
# Could be consolidated more actually 
def load_json_file(json_file_name):
    with open(json_file_name) as data_file:    
        data = json.load(data_file)
        return data



def get_rand_num(low_num, high_num):
    rand_num = random.randint(low_num, high_num)
    return rand_num



#-----------END FUNCTIONS


# -------------------------This works----------------------------


# Prompt for sender email password
#password = getpass.getpass(prompt='Password: ')

carrier = carrier_ending()

# Finally send the email
loop = 3 #int(raw_input('Loop how many times? > '))
while loop > 0:
    try:
        to_address = 
        from_address = 
        subject = subjects()
        body = body_comments()
        password = 
        send_email(to_address, from_address, password, subject,
                   body)
        loop = loop - 1
        print '[+] ' + str(loop) + ' loops to go...'
    
    except smtplib.SMTPAuthenticationError:
        print "Could not verify email"
        break

#---------------End this works-----------------------------



#---------------------------------------FUTURE IDEAS---------------------------



#------------------------------TAKE OUTS--------------------------------------------------
'''
#Took out this section 
# Make add_argument calls here to keep code clean
def add_args():
    parser.add_argument('-f',
                        '--from-address',
                        help='the sender\'s email address',
                        required=True)
    parser.add_argument('-t',
                        '--to-address',
                        help='the recipient\'s email address',
                        required=True)
    parser.add_argument('-s',
                        '--subject',
                        help='the email subject',
                        required=False)
    parser.add_argument('-b', '--body', help='the email body', required=False)

# Initialize parser
parser = argparse.ArgumentParser(description='email from the terminal')
# Adds all arguments to parser
add_args()
# Parses command line args
args = parser.parse_args()


with open('phone_carriers.json') as data_file:    
        data = json.load(data_file)

  with open('subject_list.json') as data_file:    
        data = json.load(data_file)
        x = random.randint(0,5)
'''
