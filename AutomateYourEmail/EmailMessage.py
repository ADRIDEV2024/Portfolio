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


# Apply SSL security protocol to protect the email and send it to the server in a secure way 
context = ssl.create_default_context()

with smtplib.SMTP_SSL("smtpgmail.com", 6000, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, email.as_string())

if __name__ == "__main__":
    EmailMessage()
