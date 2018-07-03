#https://github.com/bmccormack/trello-python-demo/blob/master/demo.py
#https://stackoverflow.com/questions/26552278/trello-api-getting-boards-lists-cards-information
#https://developers.trello.com/docs/api-introduction

# Waktu untuk run Web Developement Gemastik dan Welcome Board : 36s

import requests
import json
from trello import TrelloApi

key = '19e1e8779951830e0d86122f201454c6'
token = '6fec5904bd2db30d876191d45f68bbec0db6322e36ebaa2ad80c2bcd7948d5f9'
params_key_and_token = {'key':key, 'token':token}

base = 'https://api.trello.com/1/'
boards_url = base + 'members/me/boards'

board_list = requests.get(boards_url, params=params_key_and_token)
board_list_array = board_list.json()

# 1. Boards dari Trello
print ('Jumlah board:' + str(len(board_list_array)))
for board in board_list_array:
    print (board['name'])

# 2. List yang ada dalam board tertentu
    #if board['name'] == 'Welcome Board':
    list_url = base + 'boards/' + board['id'] + '/lists'
    list_list = requests.get(list_url, params=params_key_and_token)
    list_list_array = list_list.json()
    print ('\tJumlah list dalam board :' + str(len(list_list_array)))

    for lists in list_list_array:
            print ('\t - ' + lists['name'])

# 3. Cards yang ada pada list tertentu
            card_url = base + 'lists/' + lists['id'] + '/cards'
            params_key_and_token.update({'fields': 'id,name,desc,pos'})
            card_list = requests.get(card_url, params=params_key_and_token)
            card_list_array = card_list.json()
            print ('\t\tJumlah card dalam list : ' + str(len(card_list_array)))
            
            for cards in card_list_array:
                print ('\t\t -- ' + cards['name'])

#. 4. Checklist items yang ada di card tertentu
                check_url = base + 'cards/' + cards['id'] + '/checklists'
                if "fields" in params_key_and_token:
                    params_key_and_token.pop("fields")
                check_list = requests.get(check_url, params=params_key_and_token)
                check_list_array= check_list.json()

                if len(check_list_array) > 0:
                    print ('\t\t\tJumlah checklist setiap card : ' + str(len(check_list_array)))

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
                                



