import datetime
import random
import smtplib

import pandas

my_mail = ""
password = ""

birthdays = pandas.read_csv("birthdays.csv")
birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in birthdays.iterrows()}

now = datetime.datetime.now()
today = (now.month, now.day)

if today in birthdays_dict:
    birthday_person = birthdays_dict[today]
    file1 = open(f"letter_templates/letter_{random.randint(1, 3)}.txt")
    letter_choosen = file1.read()
    letter_to_send = letter_choosen.replace("[NAME]", birthday_person["name"])

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_mail, password=password)
        connection.sendmail(from_addr=my_mail, to_addrs=birthday_person["email"], msg=f"Subject: Happy birthday\n\n"
                                                                                      f"{letter_to_send}")
