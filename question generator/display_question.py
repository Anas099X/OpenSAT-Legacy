import requests
import json

url = "https://getpantry.cloud/apiv1/pantry/018074c8-1891-4995-9fd6-2d8b5cf4eb17/basket/sat_question_test"

payload = ""
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("GET", url, headers=headers, data=payload)

data = json.loads(response.text)

print(f" {data['questions'][0]['question']['paragraph']} \n{data['questions'][0]['question']['query']}")
