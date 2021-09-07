
import smtplib
from dotenv import load_dotenv
import os

load_dotenv()

gmail_user = os.getenv("GMAIL_USER")
gmail_password = os.getenv("GMAIL_PASSWORD")

sent_from = gmail_user
to = [os.getenv("TO_EMAIL")]
subject = 'IKEA PRODUCT AVAILABLE'

def send_email(body: str):
    to_string = ", ".join(to)
    email_string = f"From: {sent_from}\nTo: {to_string}\nSubject: {subject}\n\n{body}"
    try:
        smtp_server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        smtp_server.ehlo()
        smtp_server.login(gmail_user, gmail_password)
        smtp_server.sendmail(sent_from, to, email_string)
        smtp_server.close()
        print ("Email sent successfully!")
    except Exception as ex:
        print ("Something went wrong….",ex)
