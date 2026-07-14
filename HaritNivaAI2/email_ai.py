import smtplib
from email.mime.text import MIMEText

SENDER_EMAIL = "yourgmail@gmail.com"
SENDER_PASSWORD = "YOUR_16_DIGIT_APP_PASSWORD"


def send_email(receiver, task, date):

    subject = "HaritNiva AI - Task Reminder"

    body = f"""
Hello Farmer,

This is a reminder from HaritNiva AI.

Task: {task}
Date: {date}

Best wishes,
HaritNiva AI
"""

    message = MIMEText(body)

    message["Subject"] = subject
    message["From"] = SENDER_EMAIL
    message["To"] = receiver

    with smtplib.SMTP("smtp.gmail.com",587) as server:
        server.starttls()
        server.login(SENDER_EMAIL,SENDER_PASSWORD)
        server.send_message(message)