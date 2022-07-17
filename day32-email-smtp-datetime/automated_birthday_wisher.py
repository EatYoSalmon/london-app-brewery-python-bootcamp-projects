from re import TEMPLATE
import smtplib
import datetime as dt
import pandas as pd
import os
from pathlib import Path
from random import choice

PARENT_DIR = Path(__file__).parent.resolve()
TEMPLATE_DIR = PARENT_DIR.joinpath('/letter_templates')
DATA = PARENT_DIR.joinpath('birthdays.csv')

SENDER_EMAIL = 'sender_address@somemail.com'
SMTP_KEY = 'smpt.somemail.com'
PASSWORD = '$ome-∑ick-Passw0rd'

df = pd.read_csv(DATA)
templates = [filename for filename in os.listdir(TEMPLATE_DIR)]

now = dt.datetime.now()
today = (now.month, now.day)

birthday_dict = {(row['month'], row['day']): row for (i, row) in df.iterrows()}

if today in birthday_dict:

    person = birthday_dict[today]
    name = person['name']
    email = person['email']

    template = templates.choice
    with open(TEMPLATE_DIR.joinpath(template), 'r') as file:
        template_text = file.read()

    subject = f"Happy Birthday {name}!"
    body = template_text.replace('[NAME]', name)

    message = f"Subject:{subject}\n\n{body}"

    with smtplib.SMPT(SMTP_KEY) as connection:

        connection.starttls()
        connection.login(user=SENDER_EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=SENDER_EMAIL,
            to_addrs=email,
            msg=message,
        )
