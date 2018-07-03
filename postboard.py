import requests


key = '19e1e8779951830e0d86122f201454c6'
token = '6fec5904bd2db30d876191d45f68bbec0db6322e36ebaa2ad80c2bcd7948d5f9'
param_butuh= {'key':key, 'token':token}
base = 'https://api.trello.com/1/'

# POST add new board
"""
board_url = base + 'boards/'
name = input("Name for new board? ")
param_butuh.update({'name': name})
response = requests.request("POST", board_url, params=param_butuh)

print (response.text)
"""

#DELETE existing board
'''
board_name = input("Name a board wish to delete? ")
boards_url = base + 'members/me/boards'
board_list = requests.get(boards_url, params=param_butuh)
board_list_array = board_list.json()

for board in board_list_array:
    if board['name'] == board_name:
        board_id = board['id']

del_board = base + 'boards/' + board_id
response = requests.request("DELETE", del_board, params=param_butuh)
print (response.text)
'''

#POST add new list
"""
list_name = input("Name for new list? ")
board_name = input("Name of the board the list should be created on? ")

boards_url = base + 'members/me/boards'
board_list = requests.get(boards_url, params=param_butuh)
board_list_array = board_list.json()

for board in board_list_array:
    if board['name'] == board_name:
        board_id = board['id']

param_butuh.update({'name': list_name, 'idBoard':board_id})
list_url = base + 'lists'
response = requests.request("POST", list_url, params=param_butuh)
print (response.text)
"""

#POST add new card
boards_url = base + 'members/me/boards'
board_list = requests.get(boards_url, params=param_butuh)
board_list_array = board_list.json()

for board in board_list_array:
    print (board['name'])

board_name = input("Name of a board to add the card? ")
for board in board_list_array:
    board_id = board['id']

list_url = base + 'boards/' + board_id + '/lists'
list_list = requests.request("GET", list_url, params=param_butuh)
list_list_array = list_list.json()

for lists in list_list_array:
    print (lists['name'])

list_name = input("Name of the list to add the card on? ")
for lists in list_list_array:
    if lists['name'] == list_name:
        list_id = lists['id']

card_name = input("Name of the card you wished to add? ")
card_url = base + '/cards'
card_desc = input("Description to the card? ")
param_butuh.update({'name': card_name, 'desc': card_desc, 'idList':list_id})
response = requests.request("POST", card_url, params=param_butuh)
print(response.text)
