# save in MongoDB database
import pprint
from pymongo import MongoClient
client = MongoClient()
db = client['Trello']

# import from Trello API
import requests
import json
from trello import TrelloApi

#key = input ('Your Trello API key? ')
#token = input ('Your Trello token? ')
key = '19e1e8779951830e0d86122f201454c6'
token = '6fec5904bd2db30d876191d45f68bbec0db6322e36ebaa2ad80c2bcd7948d5f9' 
params_key_and_token = {'key':key, 'token':token}

base = 'https://api.trello.com/1/'
# JANGAN LUPA ganti jadi 'ptdotindonesia1'
organization_name = 'pythonuser'

def Merge(dict1, dict2):
    res = {**dict1, **dict2}
    return res

organization_url = base + 'organizations/' + organization_name + '/boards'

# Ambil Boards yang ada dibawah Organisasi PT DOT Indonesias
params_key_and_token.update({'fields': 'name,desc,dateLastActivity,memberships'})
organization_list = requests.request("GET", organization_url, params=params_key_and_token)
organization_list_array = organization_list.json()

print ('Jumlah Boards: ' + str(len(organization_list_array)))
if 'fields' in params_key_and_token:
    del params_key_and_token['fields']

# Tampilkan jumlah, nama board, tanggal aktivitas terakhir, deskripsi board
for board in organization_list_array:
    print (board['name'] + ' id: ' + board['id'])
    '''if 'dateLastActivity' in board:
        print ('Last Activity: ' + str(board['dateLastActivity']))
    print (board['desc'])'''

board_name = input('Nama board yang ingin ditampilkan isinya: ')
for board in organization_list_array:
    if (board['name'] == board_name):
        board_id = board['id']

board_url = base + 'boards/' + board_id + '/actions'
params_key_and_token.update({'fields': 'id,type,date,memberCreator,member'})
response = requests.request("GET", board_url, params=params_key_and_token)
board_array = response.json()
c_action = db[board_name]

#print (board_array)
action_iterator = 1
for action in board_array:
    print ('\n' + str(action_iterator) + '. ' + action['type'] + ' ' + action['date'])
    print (action['memberCreator']['username'] + ' ' + action['memberCreator']['fullName'])
    if 'member' in action:
        print ('another member: ' + action['member']['username'] + ' ' + action['member']['fullName'])
    action_iterator += 1
    #harus melakukan assign baru key id ke _id O(N) agar bisa unique value di MongoDB
    action['_id'] = action.pop('id')
    

# Masukkan action ke MongoDB collection dengan nama collection = board_name
'''
It is significantly faster to use find() + limit() because findOne() will always read + return the document if it exists. find() just returns a cursor (or not) and only reads the data if you iterate through the cursor.
-- https://stackoverflow.com/questions/8389811/how-to-query-mongodb-to-test-if-an-item-exists
-- https://blog.serverdensity.com/checking-if-a-document-exists-mongodb-slow-findone-vs-find/
Better to use "COVERED INDEX"
'''
action_insert = c_action.insert_many(board_array)


'''
filter_choice = input('Do you want to filter action/log based on name? (Y/N) ')
if filter_choice == 'Y' or filter_choice == 'y':
    filter_name = input('What is the username / FullName? ')
    for action in board_array:
        if (action['memberCreator']['username'] == filter_name) or (action['memberCreator']['fullName'] == filter_name):
            print ('\n' + action['type'] + ' ' + action['date'])
        if ('member' in action) and (action['member']['fullName'] == filter_name or action['member']['username'] == filter_name):
            print ('-- ' + action['type'] + ' ' + action['date'])
'''
