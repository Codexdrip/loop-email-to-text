#!/usr/bin/env python

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
    with open('phone_carriers.json') as data_file:    
        data = json.load(data_file)
        print '678987' + data['carriers']['metro']



# make a dic file for list of body statements
def body_comments():
   with open('body_comments.json') as data_file:    
        data = json.load(data_file)
        x = random.randint(0,5)
        print 'random is ' + str(x)
        print data['comments'][x]
        



#-----------END FUNCTIONS

body_comments()



''' -------------------------This works----------------------------
to_address = 
from_address = 
subject = 
body = 

# Prompt for sender email password
password = getpass.getpass(prompt='Password: ')

#password =  

# Finally send the email
loop = 3 #int(raw_input('Loop how many times? > '))
while loop > 0:
    try:
        send_email(to_address, from_address, password, subject,
                   body)
        loop = loop - 1
        print '[+] ' + str(loop) + ' loops to go...'
    except smtplib.SMTPAuthenticationError:
        print "Could not verify email"
        break

'''#---------------End this works-----------------------------



#---------------------------------------FUTURE IDEAS---------------------------
# make a dic file for different emails addresses and loop through all addresses


# make a dic file for list of subject titles



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
'''