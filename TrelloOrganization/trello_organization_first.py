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
import sys
import config
from trello import TrelloApi

key = config.Trello_config['api_key']
token = config.Trello_config['token']
params_key_and_token = {'key':key, 'token':token}
base = 'https://api.trello.com/1/'
org_name = config.Trello_config['organization_name']

org_url = base + 'organizations/' + org_name
params_key_and_token.update({'members': 'all','memberships': 'all'})
response = requests.request("GET", org_url, params=params_key_and_token)
org_array = response.json()

org_save = coll.update({'_id': org_array['id']}, {'$set': org_array}, upsert=True)
client.close()
