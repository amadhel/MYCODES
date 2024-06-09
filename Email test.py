#we need to import our emailmessage from the email.message module
#the ssl which is the server for the gmail
#the smtp from the smatp library
from email.message import EmailMessage
import ssl
import smtplib

#now that we have import the modules lets create the message space
#which consists of the body and subject or subject  and body
#i forgot to bring the email and the password plus the reciever own too sorry.
sender_email="acheampong6040@gmail.com"
email_password = "qucc lcad sjdm bbrd"
reciever_email="gevaciv449@javnoi.com"

#Lets continue
Subject="TEST EMAIL"
Body="""
Please ignore this email as its just a test running to check on 
how to send email to clients using python server and how to make 
sure its been send.
"""
#this is the body and the subject
#Lets create the server code:
em=EmailMessage()
em['From']=sender_email
em['To']=reciever_email
em['Subject']=Subject
em.set_content(Body)
context=ssl.create_default_context()
#now this is the email server code for the reciever and the sender
#lets get to the main server code
with smtplib.SMTP_SSL("smtp.gmail.com",465,context=context)as smtp:
    smtp.login(sender_email,email_password)
    smtp.sendmail(sender_email,reciever_email,em.as_string())

#LETS RUN AND SEE FROM OUR TEMP EMAIL IF ITS WORKING

#thank you sooo much and see yiu some other time
