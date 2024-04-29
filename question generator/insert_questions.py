import requests
import json


def add_question(bucket_name,array_name,input_question):
    
 url = f"https://getpantry.cloud/apiv1/pantry/018074c8-1891-4995-9fd6-2d8b5cf4eb17/basket/sat_database"

 headers = {
  'Content-Type': 'application/json'
 }

 get_jsondata = requests.request("GET", url, headers=headers, data="")

 # Load the existing JSON string
 load_data = json.loads(get_jsondata.text)

 input_data = json.loads(input_question)

 # Append the new data to the "test" array
 load_data[array_name].append(input_data)

 # Convert the modified data back to a JSON string
 modified_json = json.dumps(load_data)  # Optional: adds indentation for readability

 write_modifed = requests.request("POST", url, headers=headers, data=modified_json)
 return write_modifed


