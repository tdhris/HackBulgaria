from email.mime.text import MIMEText
from email.header import Header
import smtplib


def send_email(user_email, unique_hash_code, subject):
    smtp_host = "smtp.gmail.com"
    login, passw = 'ttestov64', 'Blah$$1234'

    message = MIMEText(unique_hash_code, 'plain', 'utf-8')
    message['From'] = login
    message['To'] = user_email
    message['Subject'] = Header(subject, 'utf-8')

    host = smtplib.SMTP(smtp_host, 587, timeout=10)
    try:
        host.starttls()
        host.login(login, passw)
        host.sendmail(message['From'], message['To'], message.as_string())
    finally:
        host.quit()
