import requests
import json
from trello import TrelloApi

key = input ('Your Trello API key? ')
token = input ('Your Trello token? ')
params_key_and_token = {'key':key, 'token':token}

base = 'https://api.trello.com/1/'
# JANGAN LUPA ganti jadi 'ptdotindonesia1'
organization_name = 'ptdotindonesia1'

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
    print (board['name'])
    if 'dateLastActivity' in board:
        print ('Last Activity: ' + str(board['dateLastActivity']))
    print (board['desc'])

board_name = input('Nama board yang ingin ditampilkan isinya: ')
for board in organization_list_array:
    if (board['name'] == board_name):
        board_id = board['id']


# 2. List yang ada dalam board tertentu
list_url = base + 'boards/' + board_id + '/lists'
list_list = requests.get(list_url, params=params_key_and_token)
list_list_array = list_list.json()
print ('\tJumlah list dalam board :' + str(len(list_list_array)))

for lists in list_list_array:
        print ('\t - ' + lists['name'])

lists_choice = input('\nTampilkan semua isi card dalam list? (y/n) ')

def funcShowCard(list_id_param, list_name_param):
    card_url = base + 'lists/' + list_id_param + '/cards'
    params_key_and_token.update({'fields': 'id,name,desc,pos'})
    card_list = requests.get(card_url, params=params_key_and_token)
    card_list_array = card_list.json()
#    total_persentaselist = 0
    print ('\t - ' + list_name_param)
    print ('\t\tJumlah card dalam list : ' + str(len(card_list_array)))
    
    for cards in card_list_array:
        print ('\t\t -- ' + cards['name'])

# 4. Checklist items yang ada di card tertentu
        check_url = base + 'cards/' + cards['id'] + '/checklists'
        if "fields" in params_key_and_token:
            params_key_and_token.pop("fields")
        check_list = requests.get(check_url, params=params_key_and_token)
        check_list_array= check_list.json()

        if len(check_list_array) > 0:
            print ('\t\t\tJumlah checklist setiap card : ' + str(len(check_list_array)))
#        total_persentasecard = 0

        for checklist in check_list_array:
            belum = 0
            selesai = 0
            print ('\t\t\t --- Checklist: ' + checklist['name'])
            for centang in checklist['checkItems']:
                print ('\t\t\t\t' + centang['name'] + '->' + centang['state'])
                if centang['state'] == 'complete':
                    selesai += 1
                else:
                    belum += 1
            print ('\t\t\tSelesai: ' + str(selesai) + ' Belum: ' + str(belum))
            if (selesai > 0) or (belum > 0):
                persentaseselesai = selesai / (selesai+belum) * 100
#                total_persentasecard += persentaseselesai
                print ('\t\t\t===Persentase selesai: ' + str(persentaseselesai) + '%')

#        if len(check_list_array) > 0:
#            persentasecard = total_persentasecard / len(check_list_array)
#            print ('\t\t=====Persentase selesai setiap card: ' + repr(persentasecard))
#            total_persentaselist += persentasecard

#    if len(card_list_array) > 0: 
#        persentaselist = total_persentaselist / len(card_list_array)
#        print ('\t\t=====Persentase selesai setiap list: ' + repr(persentaselist))
        

# 3. Cards yang ada pada list tertentu
if (lists_choice == 'y') or (lists_choice == 'Y'):
    for lists in list_list_array:
        funcShowCard(lists['id'], lists['name'])

else:
    lists_name = input ('\nNama dari LIST yang ingin menampilkan isi cardnya? ')
    for lists in list_list_array:
        if (lists_name == lists['name']):
            lists_id = lists['id']
    funcShowCard(lists_id, lists_name)


