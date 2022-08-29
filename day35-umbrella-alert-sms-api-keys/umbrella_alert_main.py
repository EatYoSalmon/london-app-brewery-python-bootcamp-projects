from email.message import Message
from operator import index
import requests
from sample_response import sample_response
import pandas as pd
import datetime as dt
import os
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient
import sys
from pathlib import Path


def fetch_json(url: str, params: dict) -> dict:
    """
    Fetch json object via an API REST call;
    Return a Python dictionary
    """
    response = requests.get(url=url, params=params)
    print(f"\n---STATUS: {response.status_code}---\n")
    response.raise_for_status()

    return response.json()


def categorized_hourly_report(cat: str, data: pd.DataFrame):

    cat_dict = {
        'rain': "\n### RAINING HOURS\n",
        'clear': "\n### GOOD TO GO\n",
        'atmos': "\n### ATMOSPHERIC\n",
    }

    if len(data) > 0:
        print(cat_dict[cat])
        print(data[['main', 'description']])

PARENT_DIR = str(Path(__file__).parent.resolve())
MESSAGE_PATH = f"{PARENT_DIR}/message_body.txt"

FROM_NUMBER = r'<twilio active phone numbe>r'
TO_NUMBER = r'<twilio verified phone number>'

weather_api_key = r'<openweathermap api key>'

weather_normal = r'https://api.openweathermap.org/data/2.5/weather'
weather_one_call = r'https://api.openweathermap.org/data/3.0/onecall'

lat, lng = 13.661094, 100.731803
city = 'Bangkok,Thailand'

weather_params = {

    'lat': lat,
    'lon': lng,
    'appid': weather_api_key,
    # 'q': city,
    'exclude': 'current,minutely,daily'
}

weather = sample_response    # Sample API Response cuz I ain't paying
# weather = fetch_json(weather_normal, weather_params)    # Normal Forecast
# weather = fetch_json(weather_one_call, weather_params)    # Detailed Forecast
# weather = fetch_json(weather_one_call, weather_params)    # Hourly Forecast

# print(weather)
will_rain = False

id_list = []
main_list = []
dscb_list = []

for delta in range(0, 12):
    wthr_id = weather['hourly'][delta]['weather'][0]['id']
    wthr_main = weather['hourly'][delta]['weather'][0]['main']
    wthr_dscb = weather['hourly'][delta]['weather'][0]['description']

    if wthr_id < 700:
        will_rain = True

    id_list.append(wthr_id)
    main_list.append(wthr_main)
    dscb_list.append(wthr_dscb)
    # wthr_dict[delta]['main'] = wthr_main
    # wthr_dict[delta]['description'] = wthr_dscb

wthr_dict = {
    'id': id_list,
    'main': main_list,
    'description': dscb_list,
}

df = pd.DataFrame.from_dict(wthr_dict)
df = df.reset_index()
df = df.rename(columns={'index': 'delta_hr'})
# print(df.head())

rain_df = df.loc[df['id'] < 700]
clear_df = df.loc[df['id'] >= 800]
atmos_df = df.loc[(df['id'] >= 700) & (df['id'] < 800)]

original_stdout = sys.stdout    # Save a reference to the original standard output

with open(MESSAGE_PATH, 'w') as file:
    sys.stdout = file    # Change the standard output to the file we created.

    if will_rain:
        print("\n\tLooks like it's going to rain.")
        print("\tPlease bring an umbrella with you today! ☂️\n")

        rain_dict = categorized_hourly_report('rain', rain_df)
        atmos_dict = categorized_hourly_report('atmos', atmos_df)

    else:
        print("\n\tLucky! The weather says the sky is clear.")
        print("\tIt seems you won't be needing an umbrella today. 🕺\n")

    # rain_dict = categorized_hourly_report('rain', rain_df)
    # clear_dict = categorized_hourly_report('clear', clear_df)
    # atmos_dict = categorized_hourly_report('atmos', atmos_df)

    sys.stdout = original_stdout # Reset the standard output to its original value

# --- TWILIO ---
# proxy_client = TwilioHttpClient()
# proxy_client.sesion.proxies = {'https': os.environ['https_proxy']}

twl_acc_sid = r'<twilio account id>'
twl_auth_token = r'<twilio authentication token>'

if will_rain:

    with open(MESSAGE_PATH, 'r') as file:
        message_body = file.read()

        # client = Client(twl_acc_sid, twl_auth_token, http_client=proxy_client)
        client = Client(twl_acc_sid, twl_auth_token)
        message = client.messages.create(
            body=message_body,
            from_=FROM_NUMBER,
            to=TO_NUMBER
        )
