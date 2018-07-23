# https://developers.trello.com/reference/#tokenstokenwebhooks-2

import requests
import json
import config

key = config.Trello_config['api_key']
token = config.Trello_config['token']
callbackurl = config.Webhook['hook_url']
params_key_and_token = {'key':key, 'token':token}
base = 'https://api.trello.com/1/'

org_name = config.Trello_config['organization_name']
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
    
