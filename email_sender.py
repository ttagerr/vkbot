import os
from smtplib import SMTP
from email.mime.text import MIMEText
from dotenv import load_dotenv

load_dotenv()

def send_email(to_email, subject, body):
    smtp_server = 'smtp.gmail.com' #смтп для гугл
    smtp_port = 587 #порт для гугл
    smtp_user = os.getenv('SMTP_USER')
    smtp_password = os.getenv('SMTP_PASSWORD')

    msg = MIMEText(body, 'html', 'utf-8')
    msg['Subject'] = subject
    msg['From'] = smtp_user
    msg['To'] = to_email

    with SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(smtp_user, smtp_password)
        server.send_message(msg)
