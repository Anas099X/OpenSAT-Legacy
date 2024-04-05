import json

# Define the data you want to insert
new_data = {"name": "My New Item", "value": 10}

jsonvalues = '''

{

"test":[

]

}

'''

# Load the existing JSON string
data = json.loads(jsonvalues)

# Append the new data to the "test" array
data["test"].append(new_data)

# Convert the modified data back to a JSON string
modified_json = json.dumps(data, indent=4)  # Optional: adds indentation for readability

print(modified_json)
