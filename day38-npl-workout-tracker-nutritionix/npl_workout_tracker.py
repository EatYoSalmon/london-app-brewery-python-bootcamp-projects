from wsgiref import headers
import requests
import os
from datetime import datetime


# Optional Constants
GENDER = 'female'
WEIGHT = 46
HEIGHT = 172
AGE = 23

# Required Constants
APP_ID = os.environ.get('NUTRINIXID')
API_KEY = os.environ.get('NUTRINIXAPI')
SHEETY_ENDPOINT = os.environ.get('SHEETYWORKOUTENDPOINT')
TOKEN = os.environ.get('SHEETYTOKEN')

if (APP_ID is None) or (API_KEY is None):
    raise Exception("Please use your own authorizations")

# Set up for posting user input to Nutritionix Natural Exercise API
exercise_input = input('Tell me about your workout today: ')

exercise_endpoint = r'https://trackapi.nutritionix.com/v2/natural/exercise'
headers = {
    'x-app-id': APP_ID,
    'x-app-key': API_KEY,
}
body = {
    'query': exercise_input,
    # 'gender': GENDER,
    # 'weight_kg': WEIGHT,
    # 'height_cm': HEIGHT,
    # 'age': AGE,
}

response = requests.post(url=exercise_endpoint, headers=headers, json=body)
response.raise_for_status()

# Preparing to add new rows to Spreadsheet via Sheety.co
exer_list = response.json()['exercises']

headers = {'Authorization': TOKEN}

for exer in exer_list:

    now = datetime.now()
    body = {
        'workout': {
            'date': now.strftime(r'%d/%m/%Y'),
            'time': now.strftime(r'%X'),
            'exercise': exer['name'].title(),
            'duration': exer['duration_min'],
            'calories': exer['nf_calories'],
        }
    }

    response = requests.post(url=SHEETY_ENDPOINT, headers=headers, json=body)
    response.raise_for_status()
    print(response.json())
