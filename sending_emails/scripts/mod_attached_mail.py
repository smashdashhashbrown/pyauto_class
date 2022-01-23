#!/usr/bin/env python3

import yagmail
import os
import pandas


def main():
    sender = "qwertyasdf199@gmail.com"
    fname = "files/default-bill.txt"
    yag = yagmail.SMTP(user=sender, password=os.getenv("APP_PASS"))

    contacts = pandas.read_csv("files/financials2.csv")

    for index, row in contacts.iterrows():
        reciever = row['email']
        name = row['name']
        amt = row['amount']

        generate_bill(fname, "{} bill amount: {}".format(name, amt))

        subject = "Bill for {}".format(name)
        contents = ["You owe {}! Receipt attached.".format(amt), fname]

        print("Sending email to {}...".format(name))
        yag.send(to=reciever, subject=subject, contents=contents)
        print("Email sent!")


def generate_bill(fname, content):
    with open(fname, 'w') as file:
        file.write(content)


if __name__ == "__main__":
    main()
