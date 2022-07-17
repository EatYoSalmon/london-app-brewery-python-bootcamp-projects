import requests
import datetime as dt


# 100 - Loading
# 200 - Success
# 300 - Redirection
# 400 - Client Error
# 500 - Server Error

response = requests.get(url='http://api.open-notify.org/iss-now.json')

# DON'T code the conditionals to raise exception yourself;
# Use .raise_for_status() method instead
# if response.status_code == 404:
#     raise Exception("That resource does not exist.")
# elif response.status_code == 401:
#     raise Exception("You are not authorized to access this data")

# This method throws an HTTP error if the response is not a success;
response.raise_for_status()

data = response.json()

position = list(data['iss_position'].values())
time = dt.datetime.fromtimestamp(data['timestamp']).astimezone()
print(position, time)

# MY_LAT, MY_LNG = 13.64646320967636, 100.68070241375268

# parameters = {
#     'lat': MY_LAT,
#     'lng': MY_LNG,
#     'formatted': 0
# }

# response = requests.get(
#     'https://api.sunrise-sunset.org/json', params=parameters)
# # response = requests.get('https://api.sunrise-sunset.org/json')
# response.raise_for_status()

# data = response.json()

# sunrise_hr = int(data['results']['sunrise'].split('T')[1].split(':')[0])
# sunset_hr = int(data['results']['sunset'].split('T')[1].split(':')[0])

# time_now = dt.datetime.now()

# print(sunrise_hr)
# print(sunset_hr)
# print(time_now)
