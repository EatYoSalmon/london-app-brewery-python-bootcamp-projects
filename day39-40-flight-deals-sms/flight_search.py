import os
import string
import requests
from pprint import pprint
from flight_data import FlightData


class FlightSearch:
    #This class is responsible for talking to the Flight Search API.

    def __init__(
        self, key: string,
        endpoints={
            'search': r'https://api.tequila.kiwi.com/v2/search',
            'locations': r'https://api.tequila.kiwi.com/locations/query'
        }) -> None:
        
        self.endpoints = endpoints
        self.api_key = key


    def fetch_location(self, query: string) -> dict:

        headers = {'apikey': self.api_key}
        params = {
            'term': query,
            'location_types': 'city',
            # 'limit': 1,
        }

        response = requests.get(
            url=self.endpoints['locations'],
            headers=headers,
            params=params
        )
        response.raise_for_status()

        return response.json()['locations'][0]


    def fetch_deal(self, dept_code, dest_code, from_date, to_date) -> FlightData:

        headers = {'apikey': self.api_key}
        params = {
            'fly_from': dept_code,
            'fly_to': dest_code,
            'date_from': from_date.strftime(r'%d/%m/%Y'),
            'date_to': to_date.strftime(r'%d/%m/%Y'),
            'nights_in_dst_from': 7,
            'nights_in_dst_to': 28,
            'flight_type': 'round',
            'max_stopovers': 0,
            'one_for_city': 1,
            'curr': 'GBP',
        }

        response = requests.get(
            url=self.endpoints['search'],
            headers=headers,
            params=params
        )
        response.raise_for_status()

        try:
            data = response.json()['data'][0]
        except IndexError:
            print(f"--- No flight found for {dest_code} ---")
            return None
        
        flight_data = FlightData(
            price=data['price'],
            dept_city_name=data['route'][0]['cityFrom'],
            dept_city_code=data['route'][0]['cityCodeFrom'],
            dept_airport=data["route"][0]["flyFrom"],
            dest_city_name=data["route"][0]["cityTo"],
            dest_city_code=data['route'][0]['cityCodeTo'],
            dest_airport=data["route"][0]["flyTo"],
            travel_date=data["route"][0]["local_departure"].split("T")[0],
            return_date=data["route"][1]["local_departure"].split("T")[0]
        )

        return flight_data
