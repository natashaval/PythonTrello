# Action pada Board (Activity)
# For example: Move Card, Add Card

import requests
import json
from trello import TrelloApi

key = '19e1e8779951830e0d86122f201454c6'
token = '6fec5904bd2db30d876191d45f68bbec0db6322e36ebaa2ad80c2bcd7948d5f9'
params_key_and_token = {'key':key, 'token':token}

base = 'https://api.trello.com/1/'

print ('Open your board in browser. Next, add `.json` at the end of the link')
print ('Search for board id by `id`')

board_id = input("Insert board id here: ")
board_url = base + 'boards/' + board_id + '/actions'
params_key_and_token.update({'fields': 'id,type,date,memberCreator,member'})
response = requests.request("GET", board_url, params=params_key_and_token)
board_array = response.json()

#print (board_array)
for action in board_array:
    print ('\n' + action['type'] + ' ' + action['date'])
    print (action['memberCreator']['username'] + ' ' + action['memberCreator']['fullName'])
    if 'member' in action:
        print ('another member: ' + action['member']['username'] + ' ' + action['member']['fullName'])
        
filter_choice = input('Do you want to filter action/log based on name? (Y/N) ')
if filter_choice == 'Y' or filter_choice == 'y':
    filter_name = input('What is the username / FullName? ')
    for action in board_array:
        if (action['memberCreator']['username'] == filter_name) or (action['memberCreator']['fullName'] == filter_name):
            print ('\n' + action['type'] + ' ' + action['date'])
        if ('member' in action) and (action['member']['fullName'] == filter_name or action['member']['username'] == filter_name):
            print ('-- ' + action['type'] + ' ' + action['date'])
