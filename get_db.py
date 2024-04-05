import requests
import json

url = "https://getpantry.cloud/apiv1/pantry/018074c8-1891-4995-9fd6-2d8b5cf4eb17/basket/newBasket26"

payload = ""
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("GET", url("1"), headers=headers, data=payload)

print(response.text)
