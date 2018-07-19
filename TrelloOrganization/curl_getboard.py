'''
membuat list dari boards yang ada dalam organisasi
'''

import subprocess
import pprint

# lakukan curl get board
org_board = subprocess.getstatusoutput('curl --request GET --url "https://api.trello.com/1/organizations/ptdotindonesia1/boards?filter=all&fields=id%2Cname&key=19e1e8779951830e0d86122f201454c6&token=6fec5904bd2db30d876191d45f68bbec0db6322e36ebaa2ad80c2bcd7948d5f9"')

# simpan tuple sebagai string
org_board1 = ''.join(str(org_board))
'''
# ambil ID dan name dari board sebagai output, jika ingin hapus webhook

pprint.pprint(sambel1)

for i in range(0, len(sambel1)):
    mystring = sambel1[sambel1.find("{")+1:sambel1.find("}")]
    print (mystring)
'''
# save list of board in txt for delete webhook id
hs = open("webhookid.txt", "w")

arg1 = org_board[1]
# ambil data board
data = arg1[arg1.find("[")+1:]
# split data board berdasarkan namanya
data_split = data.split("},{")
#print (data_split)
for i in range(0, len(data_split)):
    print(data_split[i])
    hs.write(data_split[i])
    hs.write('\n')


hs.close()
