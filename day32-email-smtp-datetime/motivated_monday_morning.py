import smtplib
import datetime as dt
from pathlib import Path
from random import choice
import re


# --- Simple Mail Transfer Protocol ---

# SMTP Provider Token:
# - Gmail: smtp.gmail.com
# - Hotmail: smtp.live.com
# - Yahoo: smtp.mail.yahoo.com

# SENDER_EMAIL = 'sender_address@somemail.com'
# PASSWORD = '$ome-∑ick-Passw0rd'
# RECIPIENT_LIST = [
#     'that-dude@somemail.com',
#     'some-chick@somemail.com',
#     'this-cute-guy@somemail.com',
# ]

# with smtplib.SMTP('smtp.notarealprovider.somemail.com') as connection:
#     connection.starttls()
#     connection.login(user=SENDER_EMAIL, password=PASSWORD)
#     connection.sendmail(
#         from_addr=SENDER_EMAIL,
#         to_addrs=RECIPIENT_LIST,
#         msg="Subject:Waddup Waddup Waddup!\n\n \
#         How y'all been doing? Happy Birthday Y'all!",
#     )


# --- DATETIME ---

# now = dt.datetime.now()
# this_year = now.year
# this_month = now.month
# day_of_week = now.weekday()

# print(day_of_week)

# dob = dt.datetime(year=1999, month=1, day=4, hour=5, minute=35)
# print(dob)


# --- EXERCISE 1 - MOTIVATED MONDAY MORNING ---

# Send Motivational Quotes to List of Recipient Every Monday:
#     - only works if the sender account's security level is lowered to
#       allow SMTP access from Python IDLE application;

PARENT_DIR = Path(__file__).parent.resolve()

QUOTE_DATA = str(PARENT_DIR) + '/' + 'quotes.txt'
SUBJECT_PATTERN = r'\w+(\s?\w*|\s\w\.\s\w+)$'

SENDER_EMAIL = 'sender_address@somemail.com'
SMTP_KEY = 'smtp.somemail.com'
PASSWORD = '$ome-∑ick-Passw0rd'
RECIPIENT_LIST = [
    'that-dude@somemail.com',
    'some-chick@somemail.com',
    'this-cute-guy@somemail.com',
]

today = dt.datetime.now().weekday()
this_hour = dt.datetime.now().hour()
monday = 0
six_am = 6

if today == monday and this_hour == six_am:

    with open(QUOTE_DATA, 'r') as file:
        quotes = file.readlines()

    pattern = re.compile(SUBJECT_PATTERN)
    rand_quote = choice(quotes)

    subject_title = pattern.match(rand_quote).group(0)
    subject_template = f"Motivated Monday Morning - A wise word \
        from {subject_title}"

    message = f"Subject:{subject_template}\n\n{rand_quote}"

    with smtplib.SMTP(SMTP_KEY) as connection:

        connection.starttls()
        connection.login(user=SENDER_EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=SENDER_EMAIL,
            to_addrs=RECIPIENT_LIST,
            msg=message,
        )

    pass
