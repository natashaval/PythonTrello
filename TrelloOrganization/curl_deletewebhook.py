import subprocess

key = '19e1e8779951830e0d86122f201454c6'
token = '6fec5904bd2db30d876191d45f68bbec0db6322e36ebaa2ad80c2bcd7948d5f9'

# retrieve webhooks created within token
curl = 'curl https://api.trello.com/1/tokens/'+ token + '/webhooks?key=' + key
#print (curl)

curl_token = subprocess.getstatusoutput(curl)
curl_token1 = ''.join(str(curl_token))

#print (curl_token1)
data = curl_token1[curl_token1.find("[")+1:curl_token1.find("]")]
#print (data)

# take webhook id from curl
webhook_id = []
data_split = data.split("},{")
for board in data_split:
    bid = board[board.find('id":"'):board.find('","')]
    bid = bid[5:]
    #print (bid)
    webhook_id.append(bid)

#print (webhook_id)

# delete webhook within token
for i in range(len(webhook_id)):
    curl = 'curl -X "DELETE" https://api.trello.com/1/tokens/'+ token + '/webhooks/'+ webhook_id[i] +'?key=' + key
    #print (curl)
    curl_delete = subprocess.getstatusoutput(curl)
