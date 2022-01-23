#!/usr/bin/env python3

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib
import os


def main():
    sender = 'bippitboopitygimmesomedoopity@outlook.com'
    password = os.getenv("OUTLOOK_PASS")

    # Source: https://dropmail.me/en/
    reciever = 'eavvzlbd@10mail.org'

    content = MIMEMultipart()
    content['From'] = sender
    content['To'] = reciever
    content["Subject"] = "This is another subject"

    body = "<h1>Body header!</h1>" \
           "<h3>Sub-header exampple...</h3>" \
           "Yatta yatta yatta"

    mimetxt = MIMEText(body, 'html')

    content.attach(mimetxt)

    server = smtplib.SMTP('smtp.office365.com', 587)
    server.starttls() # Starts TLS encryption
    print("Logging in...")
    server.login(sender, password)
    print("Sending mail...")
    server.sendmail(sender, reciever, content.as_string())
    print("Mail sent!")
    server.quit()


if __name__ == "__main__":
    main()
