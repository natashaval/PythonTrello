# https://developers.trello.com/reference/#tokenstokenwebhooks-2

import requests
import json

#key = '19e1e8779951830e0d86122f201454c6'
#token = '6fec5904bd2db30d876191d45f68bbec0db6322e36ebaa2ad80c2bcd7948d5f9'
key = input ('Input your Trello API key: ')
token = input ('Input your token to associate with these webhooks: ')
callbackurl = input('Input URL as the endpoint for webhooks: ')
params_key_and_token = {'key':key, 'token':token}
base = 'https://api.trello.com/1/'

org_name = 'ptdotindonesia1'
base = base + 'organizations/' + org_name + '/boards'

hs = open("curl_create_webhook.txt", "w")

params_key_and_token.update({'fields': 'id,name'})
response = requests.request("GET", base, params=params_key_and_token)
org_board = response.json()

curl = 'curl https://trello.com/1/tokens/' + token + '/webhooks/?key=' + key
header = ' -H "Content-Type: application/json"'
for board in org_board:
    #print(board['id'], board['name'])
    data = ' -d \'{"callbackURL":"'+ callbackurl + '","description":"' + board['name'] + '","idModel":"' + board['id'] + '","active":true}\' '
    hasil = curl + header + data
    hs.write(hasil)
    hs.write('\n\n')

hs.close()
    
