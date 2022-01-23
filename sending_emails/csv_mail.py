#!/usr/bin/env python3

import yagmail
import os
import pandas

sender = "qwertyasdf199@gmail.com"
yag = yagmail.SMTP(user=sender, password=os.getenv("APP_PASS"))

contacts = pandas.read_csv("files/contacts.csv")

for index, row in contacts.iterrows():
    reciever = row['email']
    name = row['name']

    subject = "Welcome {}".format(name)
    contents = "You're fired {}!".format(name)

    print("Sending email to {}...".format(name))
    yag.send(to=reciever, subject=subject, contents=contents)
    print("Email sent!")
