import requests
import json


def add_question(bucket_name,array_name,input_question):
    
 url = f"INPUT JSON DATABASE HERE"

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


