import requests
import json
import pprint
from trello import TrelloApi
from pymongo import MongoClient

client = MongoClient()
db = client['Trello']
coll = db['TrelloPython']

key = '19e1e8779951830e0d86122f201454c6'
token = '6fec5904bd2db30d876191d45f68bbec0db6322e36ebaa2ad80c2bcd7948d5f9'
params_key_and_token = {'key':key, 'token':token}

trello = TrelloApi(key, token=token)

print ('Open your board in browser. Next, add `.json` at the end of the link')
print ('Search for board id by `id`')

board_id = input("Insert board id here: ")

# https://pythonhosted.org/trello/trello.html
board_json = trello.boards.get(board_id)
list_json = trello.boards.get_list(board_id)
card_json = trello.boards.get_card(board_id)
action_json = trello.boards.get_action(board_id)
checklist_json = trello.boards.get_checklist(board_id)
member_json = trello.boards.get_member(board_id)

# 1. Board
for board in board_json:
    board['_id'] = board.pop('id')
    board['type'] = 'Board'
    board_save = coll.update({'_id': board['_id']}, {'$set': board}, upsert=True)
    
# 2. List
for lists in list_json:
    print ('\t - ' + lists['name'] + lists['id'])
    # Simpan lists dalam MongoDB
    lists['_id'] = lists.pop('id')
    lists['type'] = 'List'
    # tidak pakai setOnInsert karena data dapat berubah, jadi hanya menggunakan set
    lists_save = coll.update({'_id': lists['_id']}, {'$set': lists}, upsert=True)

# 3. Card
for cards in card_json:
    cards['_id'] = cards.pop('id')
    cards['type'] = 'Card'
    cards_save = coll.update({'_id': cards['_id']}, {'$set': cards}, upsert=True)            

