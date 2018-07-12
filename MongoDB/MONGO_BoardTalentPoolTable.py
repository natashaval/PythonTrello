'''
MongoDB Python -> GET data from MongoDB database
'''
import pprint
from itertools import islice
from pymongo import MongoClient
client = MongoClient()

db = client['Trello']
coll = db['Board-Coba']

# trello table -> hierarchy: list (apply, in review), job (android, backend), level (junior, intermediate)
trello_table = {}

# membuat tabel list (table bagian vertikal)
for lists in coll.find({'type': 'List'}):
    trello_table.update({lists['_id']:None})
#print (trello_table)
    
#for card in islice(coll.find({"$and": [{'type': 'Card'},{'labels': {"$ne": None}}]}) , 2):
#    pprint.pprint(card)
    
for label in coll.find({'type': 'Label'}):
    if (label['name']=='junior level') or (label['name']=='intermediate level'):
        print('INI JUNIOR / INTERMEDIATE SKIP')
        continue
        #trello_table[label['idList']].update
        #ans = coll.find({"$and": [{'type': 'Card'}, {'labels': label}]}).count()
    ans = coll.find({"$and": [{'type': 'Card'}, {'labels.name': {"$all": [label['name'], "junior level"]} }]}).count()
    print (label['name'], 'junior level', ans)
    ans = coll.find({"$and": [{'type': 'Card'}, {'labels.name': {"$all": [label['name'], "intermediate level"]} }]}).count()
    print (label['name'], 'intermediate level', ans)
    

# search job and list (junior / intermediate)
