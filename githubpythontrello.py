#https://github.com/bmccormack/trello-python-demo/blob/master/demo.py
#https://stackoverflow.com/questions/26552278/trello-api-getting-boards-lists-cards-information
#https://developers.trello.com/docs/api-introduction

import requests
import json
from trello import TrelloApi

key = '19e1e8779951830e0d86122f201454c6'
if not key:
    from settings import trello_key
    key = trello_key

token = '6fec5904bd2db30d876191d45f68bbec0db6322e36ebaa2ad80c2bcd7948d5f9'
#print (key)

base = 'https://api.trello.com/1/'
#bisa lewat bash juga dengan awalan 'curl', atau python

boards_url = base + 'members/me/boards'

params_key_and_token = {'key':key, 'token':token}
#untuk parameter setelah tanda '?' untuk bagian GET
#jika tidak ada muncul unauthorized permission

arguments = {'fields': 'name', 'lists': 'open'}
#ini untuk apaa??

#response = requests.get(boards_url, params=params_key_and_token, data=arguments)
response = requests.get(boards_url, params=params_key_and_token)

response_array_of_dict = response.json()

#print (response_array_of_dict)

# 1. Boards dari Trello
for board in response_array_of_dict:
    print (board['name'] + '\t id: '  +board['id'])
    if board['name'] == 'Welcome Board':
        #print (board['shortLink'])
        #cards_url = base + 'cards'
        #id_list = board['lists'][0]['id']
        welcomeBoard_url = board['shortLink']

# == Masuk ke list dari WelcomeBoard        
list_url = base + 'boards/' + welcomeBoard_url + '/lists'
wboard_list = requests.get(list_url, params=params_key_and_token, data=arguments)
wboard_list_array = wboard_list.json()
#print (wboard_list_array)

# 2. Lists yang ada dalam board tertentu (list dari Welcome Board)
for lists in wboard_list_array:
    print (lists['name'] + '\t id:' + lists['id'])
# 3. Cards yang ada pada list tertentu
    card_url = base + 'lists/' + lists['id'] + '/cards'
    params_key_and_token.update({'fields': 'id,name,desc,pos'})
    card_list = requests.get(card_url, params=params_key_and_token)
    card_list_array = card_list.json()
    #print (card_list_array)
    for cards in card_list_array:
        print ('-- ' + cards['name'] + '/t id: ' + cards['id'])

#4. Checklist items yang ada di card tertentu
        check_url = base + 'cards/' + cards['id'] + '/checklists'
        #params_key_and_token.pop("fields")
        check_list = requests.get(check_url, params=params_key_and_token)
        #check_list_array = check_list.json()
        check_list_array= check_list.json()

        for checklist in check_list_array:
                    belum = 0
                    selesai = 0
                    print ('\t\t\t --- Checklist: ' + checklist['name'])
                    for centang in checklist['checkItems']:
                        print ('\t\t\t' + centang['name'] + '->' + centang['state'])
                        if centang['state'] == 'complete':
                            selesai += 1
                        else:
                            belum += 1
                    print ('\t\t\tSelesai: ' + str(selesai) + ' Belum: ' + str(belum))
                    if (selesai > 0) or (belum > 0):
                        persentaseselesai = selesai / (selesai+belum) * 100
                        print ('\t\t\tPersentase selesai: ' + str(persentaseselesai) + '%')
                   
