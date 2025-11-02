import json

# Create a dictionary object
person_dict = {'first': 'Anjali', 'last':'Sharma'}
# Add additional key pairs to dictionary as needed
person_dict['City']='Mumbai'

# Create a list object of programming languages 
languages_list = ['C','Python','JavaScript']

# Add list object to dictionary for the languages key
person_dict['languages']= languages_list

# Convert dictionary to JSON object
person_json = json.dumps(person_dict)

# Print JSON object
print(person_json)