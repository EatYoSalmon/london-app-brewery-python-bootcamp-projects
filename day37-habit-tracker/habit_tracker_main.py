import requests
import os
from datetime import datetime


USERNAME = os.environ.get('PIXELAUSERNAME')
API_KEY = os.environ.get('PIXELAAPI')

pixela_endpoint = r'https://pixe.la/v1/users'

# --- Create a new Pixela user account ---
# user_params = {
#     'token': API_KEY,
#     'username': USERNAME,
#     'agreeTermsOfService': 'yes',
#     'notMinor': 'yes',
# }

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

# --- Define a new graph ---
GRAPH_ID = 'graph01'
GRAPH_NAME = 'Reading Tracker'

graph_endpoint = f'{pixela_endpoint}/{USERNAME}/graphs'

headers = {'X-USER-TOKEN': API_KEY}

# graph_config = {
#     'id': GRAPH_ID,
#     'name': GRAPH_NAME,
#     'unit': 'min',
#     'type': 'int',
#     'color': 'shibafu',
#     'timezone': 'Asia/Bangkok',
# }

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

# --- Posting a new pixel ---
target_graph_endpoint = f'{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}'

dt_now = datetime.now()
today = dt_now.strftime(r'%Y%m%d')

pixel_params = {
    'date': today,
    'quantity': input("How long did you spend reading today?"),
}

response = requests.post(url=target_graph_endpoint, json=pixel_params, headers=headers)

# --- Updating a pixel (create if non-existent) ---
# target_pixel_endpoint = f'{target_graph_endpoint}/{today}'
# response = requests.put(url=target_pixel_endpoint, json=pixel_params, headers=headers)

# --- Deleting a pixel ---
# response = requests.delete(url=target_pixel_endpoint, headers=headers)

print(response.text)
print(f"View result at: {target_graph_endpoint}")