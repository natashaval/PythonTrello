import pprint
from pymongo import MongoClient
import config
host = config.Database_config['host']
client = MongoClient(host=host)

db_name = config.Database_config['database_name']
coll_name = config.Database_config['collection_name']
db = client[db_name]
coll = db[coll_name]

import requests
import json
from trello import TrelloApi

key = config.Trello_config['api_key']
token = config.Trello_config['token']
org_name = config.Trello_config['organization_name']
params_key_and_token = {'key':key, 'token':token}

base = 'https://api.trello.com/1/'
org_url = base + 'organizations/' + org_name + '/boards'
fields = {'fields': 'id,name'}
param_org = {}
param_org.update(params_key_and_token.copy())
param_org.update(fields.copy())
response = requests.request("GET", org_url, params=param_org)
org_array = response.json()

params_key_and_token.update({'fields':'all','cards': 'all', 'customFields': 'true', 'card_customFieldItems': 'true',
                             'labels': 'all', 'lists': 'all', 'actions': 'all', 'members': 'all',
                             'checklists': 'all', 'memberships': 'all', 'pluginData': 'true', 'boardPlugins':'true'})

for board in org_array:
    board_url = base + 'boards/' + board['id']
    response = requests.request("GET", board_url, params=params_key_and_token)
    board_array = response.json()
    board_array['counter'] = 0
    board_save = coll.update({'_id': board['id']}, {'$set': board_array}, upsert=True)
    print ('Board', board['name'], 'saved successfully')
    

board_id = '5a5c4f8f846918a84a3a4f85' #for DOT Talent Pool
board_url = base + 'boards/' + board_id

response = requests.request("GET", board_url, params=params_key_and_token)
board_array = response.json()
<<<<<<< Updated upstream:trello_board_first.py
=======
board_array['counter'] = 0
>>>>>>> Stashed changes:TrelloOrganization/trello_board_first.py
board_save = coll.update({'_id': board_id}, {'$set': board_array}, upsert=True)
print ('Board', board_array['name'], 'saved successfully')

client.close()
