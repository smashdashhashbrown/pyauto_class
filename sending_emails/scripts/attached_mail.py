#!/usr/bin/env python3

import yagmail
import os

sender = "qwertyasdf199@gmail.com"
# From https://dropmail.me/en/
# Variable to change
reciever = "ezeejyce@10mail.org"

subject = "This file has an attachment"
contents = ["See attached file", "files/text.txt"]

print("Sending email...")
yag = yagmail.SMTP(user=sender, password=os.getenv("APP_PASS"))
yag.send(to=reciever, subject=subject, contents=contents)
print("Email sent!")
