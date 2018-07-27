import pprint
from pymongo import MongoClient
import config
host = config.Database_config['host']
client = MongoClient(host=host)

db_name = config.Database_config['database_name']
coll_name = config.Database_config['collection_name']
db = client[db_name]
coll = db[coll_name]

import sys
board_id = sys.argv[1]

board_counter = coll.find_one({'_id': board_id}, {'counter': 1})
print (board_counter['counter'])
