# lovely text
This sends an email to phone number 'x' amount of times.

As of 4/30/17 this incomplete.

Update: The program works now as of 5/31/17
Update: The tweaked branch works now as of 6/5/17, This branch is now named lovely text.


With this script you'll be able to send a sweet email to a phone number from the command line. If you put the script as a cronjob then you can send sweet text everyday if you please. Fill up the external files (subject_list.json & body_comments.json) with nice messages and the script will randomly choose a subject title and message from those files and send them as a text message or email. There is also a file with common email-to-text phone carrier endings (phone_carriers.json) so those endings can be applied to the phone number. Imagine your mother or significant other receiving a sweet text every morning, that would light up their day!

Some ideas:
  - YOu can send emails as text messages and loop the sending process to send numerous messages at one time.
  - Put this as a chron job to send daily emails or text messages.

Here is a simple example how to use the script
EX:
# -------------------------This works----------------------------


carrier = carrier_ending('att') # Add the phone number carrier ending here, check the file (phone_carriers.json) for mappings 

# Finally send the email
loop = 2 # sends two random messages
while loop > 0:
    try:
        to_address = "1234567890" + carrier # put a phone number here or email
        from_address = "fakeemailex@gmail.com" # this is your email
        password = "fakepassword" # password to your email
        subject = subjects() # get a random subject from (subject_list.json)
        body = body_comments() # get a random subject from (body_comments.json)
        send_email(to_address, from_address, password, subject,
                   body)
        print '[+] sent message...'
        loop = loop - 1
    
    except smtplib.SMTPAuthenticationError:
        print "Could not verify email"
        break

#---------------End this works-----------------------------

Simple!!! Enjoy...
  
  
