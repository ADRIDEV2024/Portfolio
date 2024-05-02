import os 
import ssl
import smtplib
from email.message import EmailMessage

# Sending a get request to the hidden file where we have
# our password as an enviroment variable
email_password = os.environ.get("Email Password") 
email_sender = "adridev2024@gmail.com"
email_receiver = "receiverperson@gmail.com"


subject = " Read this email please! Really important content!"
body = "I need to say you something about last day, I am Adrian and I think..."


email = EmailMessage()
email["FROM"] = "adridev2024@gmail.com"
email["TO"] =  "receiverperson@gmail.com"
email["Subject"] = subject
email.set_content(body) # We define and save the email body using the Content Manager