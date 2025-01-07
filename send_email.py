import os
import ssl,smtplib

def send_email(message):
    host="smtp.gmail.com"
    port=465

    username = "ayushman1744@gmail.com"
    password = os.getenv("PASSWORD")

    receiver="ayushman1744@gmail.com"
    context=ssl.create_default_context()

    with smtplib.SMTP_SSL(host,port,context=context) as server:
        server.login(username,password)
        server.sendmail(username,receiver,message)
