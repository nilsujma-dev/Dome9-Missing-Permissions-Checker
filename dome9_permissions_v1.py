import requests
import pandas as pd
from requests.auth import HTTPBasicAuth
import json
import sys
import os

# Check the hyperscaler argument
if len(sys.argv) < 2:
    print("Please provide a platform as an argument ('aws', 'azure', 'gcp')")
    sys.exit()

platform = sys.argv[1]

if platform.lower() not in ['aws', 'azure', 'gcp']:
    print("Invalid platform. Please provide 'aws', 'azure', or 'gcp'")
    sys.exit()

# Define Dome9 API Key and Secret
username = os.getenv('DOME9_USERNAME')
password = os.getenv('DOME9_PASSWORD')

if username is None or password is None:
    print("Please set the DOME9_USERNAME and DOME9_PASSWORD environment variables.")
    sys.exit()

# URL of the API, depending on the Platform
base_url = 'https://api.dome9.com/v2'
permissions_url = ''
account_url = ''

if platform == 'aws':
    permissions_url = f'{base_url}/cloudaccounts/MissingPermissions'
    account_url = f'{base_url}/CloudAccounts'
elif platform == 'azure':
    permissions_url = f'{base_url}/AzureCloudAccount/MissingPermissions'
    account_url = f'{base_url}/AzureCloudAccount'
elif platform == 'gcp':
    permissions_url = f'{base_url}/GoogleCloudAccount/MissingPermissions'
    account_url = f'{base_url}/GoogleCloudAccount'

# Make the API call
response = requests.get(permissions_url, headers={'accept': 'application/json'}, auth=HTTPBasicAuth(username, password))

# Check if the request was successful
if response.status_code == 200:
    # Load the response content as JSON
    data = response.json()

    # Find the max number of actions for any ID
    max_actions = max(len(item['actions']) for item in data)

    # Create a list of column names
    columns = ['id', 'name'] + [f'action{i+1}' for i in range(max_actions)]

    # Create a DataFrame to store the final output
    main_df = pd.DataFrame(columns=columns)

    # Convert the JSON data to a DataFrame
    data_list = []
    for item in data:
        row_dict = {'id': item['id']}
        # Make a new API call to get the "Name" for each ID
        name_response = requests.get(f'{account_url}/{item["id"]}', headers={'accept': 'application/json'}, auth=HTTPBasicAuth(username, password))
        if name_response.status_code == 200:
            name_data = name_response.json()
            row_dict['name'] = name_data['name']
        for i, action in enumerate(item['actions']):
            row_dict[f'action{i+1}'] = str(action)
        data_list.append(pd.DataFrame(row_dict, index=[0]))

    # Concatenate all dataframes
    main_df = pd.concat(data_list, ignore_index=True)

    # Rename columns: replace 'action' with 'issue'
    main_df.columns = [col.replace('action', 'issue') if 'action' in col else col for col in main_df.columns]

    # Write the DataFrame to an Excel file
    main_df.to_excel(f'output_{platform}.xlsx')

else:
    print('Failed to get data:', response.status_code)

