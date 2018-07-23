'''
membuat 1 webhook
'''

import subprocess
import pprint

'''
curl_webhook = subprocess.getstatusoutput
('curl https://trello.com/1/tokens/6fec5904bd2db30d876191d45f68bbec0db6322e36ebaa2ad80c2bcd7948d5f9/webhooks/?key=19e1e8779951830e0d86122f201454c6 \
-H "Content-Type: application/json" \
-d '{
"callbackURL": "http://73d8b7fc.ngrok.io/trelloorg/webhook.php",
"idModel": "5a5c4f8f846918a84a3a4f85"}' ')

str_webhook = ''.join(str(curl_webhook))
data_webhook = str_webhook[str_webhook.find("{")+1:str_webhook.find("}")]

print (data_webhook)

hs = open("curlwebhook.txt", "w")
hs.write(data_webhook)
hs.close()
'''

key = '19e1e8779951830e0d86122f201454c6'
token = '6fec5904bd2db30d876191d45f68bbec0db6322e36ebaa2ad80c2bcd7948d5f9'
id_model = input('input ID model? ')
name = 'DESKRIPSI BOARD'
curl = 'curl https://trello.com/1/tokens/' + token + '/webhooks/?key=' + key #+ ' \\'
header = ' -H "Content-Type: application/json"' #+ ' \\'
data = ' -d \'{"callbackURL": "http://73d8b7fc.ngrok.io/trelloorg/webhook.php", '+ '"description":"' + name + '","idModel": "' + id_model + '"}\' '
curl = curl + header + data
print (curl)
