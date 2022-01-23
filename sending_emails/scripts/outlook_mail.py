#!/usr/bin/env python3

import smtplib
import os


def main():
    sender = 'bippitboopitygimmesomedoopity@outlook.com'
    password = os.getenv("OUTLOOK_PASS")

    # Source: https://dropmail.me/en/
    reciever = 'eavvzlbd@10mail.org'

    # String must be formatted as such for subject and content
    # to be processed properly in email

    content = """\
Subject: This is a subject

This is the body of the email.
Hello!
"""              

    server = smtplib.SMTP('smtp.office365.com', 587)
    server.starttls() # Starts TLS encryption
    server.login(sender, password)
    print("Sending mail...")
    server.sendmail(sender, reciever, content)
    print("Mail sent!")
    server.quit()


if __name__ == "__main__":
    main()
