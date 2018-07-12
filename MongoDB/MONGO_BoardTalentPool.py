'''
Python Trello to get: Boards with array of actions, cards, labels, lists

API are useful:
1. Data is changing quickly. It doesn't make sense to regenerate dataset and download every minute.
2. A small piece of a much larger set of data.
3. Repeated computation involved.
'''

import pprint
from pymongo import MongoClient
client = MongoClient()

db = client['Trello']
coll = db['Board-Coba']

import requests
import json
import sys
from trello import TrelloApi

key = '19e1e8779951830e0d86122f201454c6'
token = '6fec5904bd2db30d876191d45f68bbec0db6322e36ebaa2ad80c2bcd7948d5f9'
params_key_and_token = {'key':key, 'token':token}
base = 'https://api.trello.com/1/'

print ('Open your board in browser. Next, add `.json` at the end of the link')
print ('Search for board id by `id`')

board_id = input("Insert board id here: ")
board_url = base + 'boards/' + board_id

params_key_and_token.update({'cards': 'all', 'labels': 'all', 'lists': 'all', 'actions': 'all'})
response = requests.request("GET", board_url, params=params_key_and_token)
board_array = response.json()

list_dict = {}
# set karena list dan card dapat berubah-ubah
for lists in board_array['lists']:
    lists['_id'] = lists.pop('id')
    lists['type'] = 'List'
    list_dict.update({lists['_id']:lists['name']})
    lists_save = coll.update({'_id': lists['_id']}, {'$set': lists}, upsert=True)

for cards in board_array['cards']:
    cards['_id'] = cards.pop('id')
    cards['type'] = 'Card'
    cards_save = coll.update({'_id': cards['_id']}, {'$set': cards}, upsert=True)            

# setOnInsert karena tidak akan berubah untuk action log,
# jika belum berubah maka akan diinsert, jika sudah ada dibiarkan
for actions in board_array['actions']:
    actions['_id'] = actions.pop('id')
    actions['type']= 'Action'
    actions_save = coll.update({'_id': actions['_id']}, {'$setOnInsert': actions}, upsert=True)
    
for labels in board_array['labels']:
    labels['_id'] = labels.pop('id')
    labels['type'] = 'Label'
    labels_save = coll.update({'_id': labels['_id']}, {'$set': labels}, upsert=True)            

