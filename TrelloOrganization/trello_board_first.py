import pprint
from pymongo import MongoClient
client = MongoClient()

db = client['Trello']
coll = db['DOT-Indonesia']

import requests
import json
from trello import TrelloApi

key = input('Input your Trello key API? ')
token = input('Input your token? ')
org_name = input('Input your organization name? ')
params_key_and_token = {'key':key, 'token':token}

base = 'https://api.trello.com/1/'
org_url = base + 'organizations/' + org_name + '/boards'
fields = {'fields': 'id,name'}
param_org = {}
param_org.update(params_key_and_token.copy())
param_org.update(fields.copy())
response = requests.request("GET", org_url, params=param_org)
org_array = response.json()

for board in org_array:
    board_url = base + 'boards/' + board['id']
    params_key_and_token.update({'cards': 'all', 'customFields': 'true', 'card_customFieldItems': 'true',
                             'labels': 'all', 'lists': 'all', 'actions': 'all'})
    response = requests.request("GET", board_url, params=params_key_and_token)
    board_array = response.json()
    board_array['counter'] = 0
    board_save = coll.update({'_id': board['id']}, {'$set': board_array}, upsert=True)
    print ('Board', board['name'], 'saved successfully')
    

client.close()
