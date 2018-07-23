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

#print (len(sys.argv), str(sys.argv))

# update counter
counter = int(sys.argv[2])
coll.update({'_id': sys.argv[1]}, {"$set": {'counter': counter} }, upsert=True)

# update board if every counter reach 10 (counter in data type string as argv)
if counter >= 10:
    if sys.argv[1] is not None:
        board_id = sys.argv[1]
        
        board_url = base + 'boards/' + board_id
        board_stats = {'cards': 'all', 'customFields': 'true', 'card_customFieldItems': 'true',
                                     'labels': 'all', 'lists': 'all'}
        param_get_board = {}
        param_get_board.update(params_key_and_token.copy())
        param_get_board.update(board_stats.copy())
        print (param_get_board)
        response = requests.request("GET", board_url, params=param_get_board)
        board_array = response.json()

        # insert set to board array (get all newest)
        board_array['_id'] = board_array.pop('id')
        board_array['counter'] = '0'
        board_save = coll.update({'_id': board_array['_id']}, {'$set': board_array}, upsert=True)

        board_action_url = base + 'boards/' + board_id + '/actions'
        response = requests.request("GET", board_action_url, params=params_key_and_token)
        action_array = response.json()
        
        # hanya menambah action yang belum ada di array
        action_save = coll.update({'_id': board_id}, {'$addToSet': {'actions': {'$each': action_array} } })
        
        

client.close()
