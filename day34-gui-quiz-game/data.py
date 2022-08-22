import requests


def fetch_json(url: str, params: dict) -> dict:
    """
    Fetch json object via an API REST call;
    Return a Python dictionary
    """
    response = requests.get(url=url, params=params)
    response.raise_for_status()

    return response.json()


# API Endpoints
opentrivia_api = r'https://opentdb.com/api.php'
params = {
    'amount': 10,
    'type': 'boolean'
}

data = fetch_json(url=opentrivia_api, params=params)
# print(f"Dtype of response.json(): {type(data)}\n")

question_data = data['results']
# print(f"Dtype: {type(question_data)}\n")
# print(question_data)
