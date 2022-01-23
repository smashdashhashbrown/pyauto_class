#!/usr/bin/env python3

import yagmail
import os
import pandas

sender = "qwertyasdf199@gmail.com"
yag = yagmail.SMTP(user=sender, password=os.getenv("APP_PASS"))

contacts = pandas.read_csv("files/financials.csv")

for index, row in contacts.iterrows():
    reciever = row['email']
    name = row['name']
    amt = row['amount']
    path = row['receipt_path']

    subject = "Bill for {}".format(name)
    contents = ["You owe {}! Receipt attached.".format(amt), path]

    print("Sending email to {}...".format(name))
    yag.send(to=reciever, subject=subject, contents=contents)
    print("Email sent!")
