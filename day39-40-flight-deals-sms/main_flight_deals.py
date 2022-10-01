# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
# 1. Populate the sheet with cities' IATA codes (not airport codes)
# 2. Search cheapest flights from tomorrow to 6 months from now
# 3. If price is lower than specified in the sheet, send an SMS via Twiolio
#     -> departure city & airport code, destination city & airport code, price, date

import os
import requests
import datetime as dt
from pprint import pprint
from twilio.rest import Client

from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager


SHEETY_ENDPOINT = os.environ.get('SHEETYFLIGHTENDPOINT')
SHEETY_TOKEN = os.environ.get('SHEETYTOKEN')
FLIGHTSEARCH_API_KEY = os.environ.get('TEQUILAKIWIAPI')
ORIGIN_CITY_CODE = 'LON'

TWILIO_ID = os.environ.get('TWILIOACCSID')
TWILIO_TOKEN = os.environ.get('TWILIOAUTHTOKEN')
FROM_NUMBER = os.environ.get('FROMNUMBER')
TO_NUMBER = os.environ.get('TONUMBER')

tequila_endpoints = {
    'search': r'https://api.tequila.kiwi.com/v2/search',
    'locations': r'https://api.tequila.kiwi.com/locations/query'
}

searcher = FlightSearch(FLIGHTSEARCH_API_KEY, tequila_endpoints)

manager = DataManager(SHEETY_ENDPOINT, SHEETY_TOKEN)
manager = manager.update_sheet(searcher)

destinations = manager.fetch_iata_codes()

tomorrow = (dt.datetime.now() + dt.timedelta(days=1))
six_month = (dt.datetime.now() + dt.timedelta(days=6*30))

deals = [
    searcher.fetch_deal(ORIGIN_CITY_CODE, dest, tomorrow, six_month)
    for dest in destinations
]

for deal in deals:

    if deal is None:
        continue

    deal.print_data()

notifier = NotificationManager(TWILIO_ID, TWILIO_TOKEN, FROM_NUMBER, TO_NUMBER)
notifier.good_deals_sms(deals, manager.sheet)
