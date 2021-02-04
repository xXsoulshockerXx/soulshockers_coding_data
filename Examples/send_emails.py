"""
Sending Emails with Python

In this example, you can sent basic email using built in libraries.
"""

import imaplib # default IMAP library
import smtplib, ssl # Library for SMTP SSL Connections
from email.message import EmailMessage

msg = EmailMessage() # this tells the program that this is a multi-part variable and will treat it as defined in our imaplib library.
msg.set_content('Email sending example using Python. It\'s Simple Text Message')

fromEmail = 'sender@example.com' # sending account information
fromPassword = 'insert your password' # account password
toEmail = 'receiver@example.com' # Replace with any valid email address

msg['Subject'] = 'Simple Test Message'
msg['From'] = fromEmail
msg['To'] = toEmail

s = smtplib.SMTP('smtp.example.com', 587) # Insert your smtp server information here. This is using STARTTLS (587), to use SSL (465), change the ports. If using smtp.gmail.com, and have two-factor authentication turned on, you may need to turn on less secure apps and also generate an app password to use for the connection.

s.starttls() # comment this out if not using STARTTLS connection (which is port 587)

s.login(fromEmail, fromPassword)
s.send_message(msg)
s.quit()

print(f'Email has been sent to: {toEmail}.')
print()