import pprint
from pymongo import MongoClient
client = MongoClient()

db = client['Trello']
coll = db['DOT-Indonesia']

import sys
board_id = sys.argv[1]

board_counter = coll.find_one({'_id': board_id}, {'counter': 1})
print (board_counter['counter'])
