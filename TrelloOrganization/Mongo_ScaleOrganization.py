import pprint
from pymongo import MongoClient
client = MongoClient()

db = client['Trello']
coll = db['DOT-Indonesia']

import requests
import json
import sys
from trello import TrelloApi

key = '19e1e8779951830e0d86122f201454c6'
token = '6fec5904bd2db30d876191d45f68bbec0db6322e36ebaa2ad80c2bcd7948d5f9'
params_key_and_token = {'key':key, 'token':token}
base = 'https://api.trello.com/1/'

# update counter
counter = sys.argv[2]
coll.update({'_id': sys.argv[1]}, {"$set": {'counter': counter} })

# update board if every counter reach 10
if counter == 10:
    if sys.argv[1] is not None:
        board_id = sys.argv[1]
        
    board_url = base + 'boards/' + board_id
    params_key_and_token.update({'cards': 'all', 'customFields': 'true', 'card_customFieldItems': 'true',
                                 'labels': 'all', 'lists': 'all', 'actions': 'all'})
    response = requests.request("GET", board_url, params=params_key_and_token)
    board_array = response.json()

    board_array['_id'] = board_array.pop('id')
    board_save = coll.update({'_id': board_array['_id']}, {'$set': board_array}, upsert=True)

client.close()
