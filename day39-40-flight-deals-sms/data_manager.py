from email.quoprimime import header_decode
import os
import requests
from flight_search import FlightSearch

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self, sheet_endpoint, token) -> None:

        self.endpoint = sheet_endpoint
        self.auth = {'Authorization': token}

        self.sheet = self.fetch_sheet()


    def fetch_sheet(self) -> dict:

        response = requests.get(url=self.endpoint, headers=self.auth)
        response.raise_for_status()

        sheet = response.json()['prices']

        return sheet


    def update_sheet(self, searcher: FlightSearch):

        for record in self.sheet:

            if record['iataCode'] != '' and record['city'] != '':
                continue

            elif record['iataCode'] == '' and record['city'] == '':
                print("\n!!---ERROR---!!: Lookup table is invalid,")
                print("!!---ERROR---!!: please recheck your Google Sheet\n")
                return

            elif record['iataCode'] == '':
                city = searcher.fetch_location(record['city'])
                record['iataCode'] = city['code']

            elif record['city'] == '':
                city = searcher.fetch_location(record['iataCode'])
                record['city'] = city['name']

            update_record = {'price': record}
            endpoint = f"{self.endpoint}/{record['id']}"

            response = requests.put(url=endpoint, headers=self.auth, json=update_record)
            response.raise_for_status()

        return self


    def fetch_iata_codes(self) -> list:
        
        codes = [record['iataCode'] for record in self.sheet]
        return codes
