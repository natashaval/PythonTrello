import pprint
from pymongo import MongoClient
import config
host = config.Database_config['host']
client = MongoClient(host=host)

db_name = config.Database_config['database_name']
coll_name = config.Database_config['collection_name']
db = client[db_name]
coll = db[coll_name]

members = {}
org_array = coll.find_one({'name': 'ptdotindonesia1'})

for member in org_array['members']:
    members.update({member['id']:member['fullName']})

pprint.pprint(members)

