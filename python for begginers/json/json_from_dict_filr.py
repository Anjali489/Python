import json

# Create a dictionary object
person_dict = {'first': 'Anjali', 'last':'Sharma'}
# Add additional key pairs to dictionary as needed
person_dict['City']='Jaipur'

# Convert dictionary to JSON object
person_json = json.dumps(person_dict)

# Print JSON object
print(person_json)