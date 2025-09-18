import requests

parameter = {
    "amount": 10,
    "type": "boolean",
}

response = requests.get(url="https://opentdb.com/api.php", params=parameter)
response.raise_for_status()
data_file = response.json()

question_data = data_file["results"]
