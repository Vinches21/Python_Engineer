import requests
import json

url = "https://petstore.swagger.io/v2/pet/findByStatus"

response = requests.get(url)

data = response.json()
print(data)

a = 5
b = 10
print(not a > 10)


