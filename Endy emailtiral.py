from email.message import EmailMessage
import ssl
import smtplib

email_sender = "acheampong6040@gmail.com"
email_password = "udmx wuib yatx zhij"

email_recipient = "acheampong6041@gmail.com",
                   

subject = "YouTube Learn"
body = "how are you doing"

em = EmailMessage()
em['From']=email_sender
em['To']=email_recipient
em['Subject']=subject
em.set_content(body)

context = ssl.create_default_context()
with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
   smtp.login(email_sender, email_password)
   smtp.sendmail(email_sender, email_recipient, em.as_string())