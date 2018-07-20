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

trello_boards = coll.find({})
for board in trello_boards[:5]:
    counter = int(board['counter'])
    board_id = board['id']
    # force run to pull board when counter is less than 10
    if counter < 10:
        board_url = base + 'boards/' + board_id
        board_stats = {'cards': 'all', 'customFields': 'true', 'card_customFieldItems': 'true',
                                     'labels': 'all', 'lists': 'all'}
        param_get_board = {}
        param_get_board.update(params_key_and_token.copy())
        param_get_board.update(board_stats.copy())
        print (param_get_board)
        response = requests.request("GET", board_url, params=param_get_board)
        board_array = response.json()

        board_array['_id'] = board_array.pop('id')
        board_array['counter'] = '0'
        board_save = coll.update({'_id': board_array['_id']}, {'$set': board_array}, upsert=True)

        board_action_url = base + 'boards/' + board_id + '/actions'
        response = requests.request("GET", board_action_url, params=params_key_and_token)
        action_array = response.json()
        
        # hanya menambah action yang belum ada di array
        action_save = coll.update({'_id': board_id}, {'$addToSet': {'actions': {'$each': action_array} } })
        
client.close()
