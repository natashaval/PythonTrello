'''
Get Trello Organization - Board, Member, Action (addMembertoOrganization dsb)
'''

import pprint
from pymongo import MongoClient
client = MongoClient()

db = client['Trello']
coll = db['DOT-Org']

import requests
import json
import sys
from trello import TrelloApi

key = '19e1e8779951830e0d86122f201454c6'
token = '6fec5904bd2db30d876191d45f68bbec0db6322e36ebaa2ad80c2bcd7948d5f9'
params_key_and_token = {'key':key, 'token':token}
base = 'https://api.trello.com/1/'

org_name = 'ptdotindonesia1'
org_url = base + 'organizations/' + org_name

params_key_and_token.update({'boards':'all', 'members':'all'})
response = requests.request("GET", org_url, params=params_key_and_token)
org_array = response.json()

for boards in org_array['boards']:
    boards['_id'] = boards.pop('id')
    boards['type'] = 'Board'
    boards_save = coll.update({'_id': boards['_id']}, {'$set': boards}, upsert=True)

for members in org_array['members']:
    members['_id'] = members.pop('id')
    members['type'] = 'Member'
    members_save = coll.update({'_id': members['_id']}, {'$set': members}, upsert=True)

org_url = base + 'organizations/' + org_name + '/actions'
response = requests.request("GET", org_url, params=params_key_and_token)
org_array_action = response.json()

for actions in org_array_action:
    actions['_id'] = actions.pop('id')
    actions['actionType'] = actions.pop('type')
    actions['type']= 'Action'
    actions_save = coll.update({'_id': actions['_id']}, {'$setOnInsert': actions}, upsert=True)

client.close()


    
