from email.message import EmailMessage
import ssl
import smtplib

email_sender="aseaau21@gmail.com"
password=1234
email_password=password
email_receiver="webase91@gmail.com"
subject="Don't forget to subscribe"

body="""

when you watch a video,please hit subscribe

"""
#an EmailMessage object
em=EmailMessage()
em['From']=email_sender
em['To']=email_receiver
em['subject']=subject
em.set_content(body)

# Create an SSL context for secure communication
context=ssl.create_default_context()

# Connect to the SMTP server and send the email
with smtplib.SMTP_SSL('smtp.gmail.com',465,context=context) as smtp:
    smtp.login(email_sender,email_password)#login to the email
    smtp.send_email(email_sender,email_receiver,em.as_string())#send th email
