import sys
import os
import json
import requests

# Path where you want the project to sit
path = "/Users/{your_username}/Documents/"

def create():
    # Creates folder
    folderName = str(sys.argv[1])
    # In this directory
    os.makedirs(path + folderName)
    # Call GitHub Create Repo API
    github_create(folderName)

def github_create(folderName):
    # Get API Token from https://github.com/settings/tokens
    api_token = '{your_token}'
    url = 'https://api.github.com/user/repos'
    headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Basic {0}'.format(api_token)
            }
    data = {
            "name": folderName,
            "description": "This is my private project.",
            "homepage": "https://github.com",
            }
    # Convert Python object to JSON string            
    data_json = json.dumps(data)

    response = requests.post(url, data=data_json, headers=headers)
    print(response)
    
    # Uncomment below if you want to see the Response of the API
    # print(response.text)
    
    # Parse a JSON string
    json_response = json.loads(response.text)

    # Command to clone the repo
    print('git clone '+json_response['clone_url'])

    
if __name__ == "__main__":
    create()

