import requests
from datetime import datetime
import smtplib
import time

MY_LAT, MY_LNG = 13.64646320967636, 100.68070241375268
PROX = 3

SENDER_EMAIL = 'sender_address@somemail.com'
SMTP_KEY = 'smpt.somemail.com'
PASSWORD = '$ome-∑ick-Passw0rd'


def is_iss_overhead(lat, lng, prox):
    """Check whether ISS is orbiting in proximity range of your coordinate."""

    response = requests.get(url='http://api.open-notify.org/iss-now.json')
    response.raise_for_status()

    data = response.json()

    iss_lat = float(data['iss_position']['latitude'])
    iss_lng = float(data['iss_position']['longitude'])

    is_lat_prox = ((lat - prox) <= iss_lat <= (lat + prox))
    is_lng_prox = ((lng - prox) <= iss_lng <= (lng + prox))

    if is_lat_prox and is_lng_prox:

        return True


def is_night():

    parameters = {
        'lat': MY_LAT,
        'lng': MY_LNG,
        'formatted': 0
    }

    response = requests.get(
        'https://api.sunrise-sunset.org/json',
        params=parameters
    )
    response.raise_for_status()

    data = response.json()

    sunrise = int(data['results']['sunrise'].split('T')[1].split(':')[0])
    sunset = int(data['results']['sunset'].split('T')[1].split(':')[0])
    now = datetime.now().hour

    if now >= sunset or now <= sunrise:
        return True


# Send Email
while True:

    time.sleep(60)
    if is_iss_overhead(MY_LAT, MY_LNG, PROX) and is_night():

        print("ISS is overhead!")

        subject = "Look up 👆🏻"
        body = "The ISS is above you in the!"

        message = f"Subject:{subject}\n\n{body}"

        with smtplib.SMPT(SMTP_KEY) as connection:

            connection.starttls()
            connection.login(user=SENDER_EMAIL, password=PASSWORD)
            connection.sendmail(
                from_addr=SENDER_EMAIL,
                to_addrs=SENDER_EMAIL,
                msg=message,
            )
