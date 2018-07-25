import pprint
from pymongo import MongoClient
import config
host = config.Database_config['host']
client = MongoClient(host=host)

db_name = config.Database_config['database_name']
coll_name = config.Database_config['collection_name']
db = client[db_name]
coll = db[coll_name]

query_member_doing = {}

boards_array = coll.find({})
for board in boards_array[40:41]:
    members_dict = {}
    for members in board['members']:
        members_dict.update({members['id']:members['fullName']})
    lists_dict = {}
    for lists in board['lists']:
        lists_dict.update({lists['id']:lists['name']})
    print(members_dict)

    
    print(board['name'], 'jumlah cards: ',len(board['cards']))
    '''
    board_cards = coll.aggregate([
        {"$match": {'name': board['name']}},
        {"$unwind": "$cards"},
        {"$project": {'cards':1}},
        #{"$group": {'_id': None, "count": {"$sum":1}}}
        {"$count": 'jumlah'}
        ])
    
    for ans in board_cards:
        #pprint.pprint(ans['cards']['name'])
        print(ans)
    '''
    
    for member_key, member_val in members_dict.items():
        for list_key, list_val in lists_dict.items():
            #print (member_key, member_val, list_key, list_val)
            ans = coll.aggregate([
                {"$match": {'name':board['name']}},
                {"$unwind": "$cards"},
                {"$match": {"$and": [{'cards.idList': list_key}, {'cards.idMembers': member_key}]}},
                {"$project": {'cards':1}},
                {"$count": 'jumlah'}
                ])
            #print(ans)
            for hasil in ans:
                if hasil['jumlah'] > 0:
                    print (member_val, list_val, hasil['jumlah'])
    
