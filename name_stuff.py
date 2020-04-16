import requests

url = 'https://random-word-api.herokuapp.com//word?number=2'
response = requests.get(url)
response_json = response.json()

print(*response_json, sep='_')
