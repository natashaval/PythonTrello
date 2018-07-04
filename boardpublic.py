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
board_url = base + 'boards/' + board_id
response = requests.request("GET", board_url, params=params_key_and_token)
board_array = response.json()
#print (response.text)


# 2. List yang ada dalam board tertentu
#if board['name'] == 'Welcome Board':
list_url = base + 'boards/' + board_id + '/lists'
list_list = requests.get(list_url, params=params_key_and_token)
list_list_array = list_list.json()
print ('\tJumlah list dalam board :' + str(len(list_list_array)))

for lists in list_list_array:
        print ('\t - ' + lists['name'] + lists['id'])

# 3. Cards yang ada pada list tertentu
        card_url = base + 'lists/' + lists['id'] + '/cards'
        params_key_and_token.update({'fields': 'id,name,labels'})
        card_list = requests.get(card_url, params=params_key_and_token)
        card_list_array = card_list.json()
        print (card_list_array)
        print ('\t\tJumlah card dalam list : ' + str(len(card_list_array)))
        
        for cards in card_list_array:
            print ('\t\t -- ' + cards['name'])

filter_choice = input('Do you want to filter card by label? (Y/N) ')
if filter_choice == 'Y' or filter_choice == 'y':
    board_filter_label = board_array['labelNames']
    for key,val in board_filter_label.items():
        if val:
            print (key, "=>", val)

# Filter card by label
    filter_name = input("Which label do you want to filter? ")
    total_filter_name = 0
    card_url = base + 'boards/' + board_id + '/cards'
    if params_key_and_token['fields']:
        del params_key_and_token['fields']
    card_list = requests.get(card_url, params=params_key_and_token)
    card_list_array = card_list.json()
    
    for cards in card_list_array:
        if cards['labels'] and cards['labels'][0]['name'] == filter_name:
            print (cards['name'])
            total_filter_name += 1
    print (total_filter_name)
        
