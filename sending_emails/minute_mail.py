#!/usr/bin/env python3

import yagmail
import os
import time

sender = "qwertyasdf199@gmail.com"
reciever = "ezeejyce@10mail.org"

subject = "Minutely Time Update"

while True:
    curr_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    contents = "The local time is: {}".format(curr_time)
    print("Email contents: '{}'".format(contents))

    print("Sending email...")
    yag = yagmail.SMTP(user=sender, password=os.getenv("APP_PASS"))
    yag.send(to=reciever, subject=subject, contents=contents)
    print("Email sent!")
    time.sleep(60)
