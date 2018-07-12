'''
MongoDB Python -> GET data from MongoDB database
print as HTML table tag
'''
import pprint
from itertools import islice
from pymongo import MongoClient
client = MongoClient()

db = client['Trello']
coll = db['Board-Coba']

# trello table -> hierarchy: list (apply, in review), job (android, backend), level (junior, intermediate)
trello_table = {}

# membuat tabel list (table bagian vertikal)
for lists in coll.find({'type': 'List'}):
    trello_table.update({lists['_id']:None})
#print (trello_table)
    
#for card in islice(coll.find({"$and": [{'type': 'Card'},{'labels': {"$ne": None}}]}) , 2):
#    pprint.pprint(card)

# print HTML table
html_table = """<html><table border="1"><tr><th>Job</th><th>Level</th>"""
#html_table = html_table + "<th>Job</th><th>Level</th>"

for lists in coll.find({'type': 'List'}):
    html_list = "<th>"+str(lists['name'])+"</th>"
    html_table = html_table + html_list
html_table = html_table + "<th>Total Level</th></tr>"
    
# Junior, Intermediate Level in 2 loops
for label in coll.find({'type': 'Label'}):
    # Junior Level
    if (label['name']=='junior level') or (label['name']=='intermediate level'):
            continue
    html_table = html_table + "<tr><td>" + label['name'] + "</td><td>Junior</td>"
    for lists in coll.find({'type': 'List'}):
        ans = coll.find({"$and": [{'type': 'Card'}, {'idList': lists['_id']}, {'labels.name': {"$all": [label['name'], "junior level"]} }]}).count()
        
        if ans > 0:
            html_card = "<td><b>"+str(ans)+"</b></td>"
            html_table = html_table + html_card
            print (lists['name'], label['name'], 'junior level', ans)
        else:
            html_card = "<td>"+str(ans)+"</td>"
            html_table = html_table + html_card

    #total_level = coll.find({"$and": [{'type': 'Card'}, {'labels.name': {"$all": [label['name'], "junior level"]} }]}).count()
    #html_table = "<td>" + str(total_level) + "</td></tr>"
    
    # Intermediate Level
    html_table = html_table + "<tr><td>" + label['name'] + "</td><td>Intermediate</td>"
    for lists in coll.find({'type': 'List'}):
        
        ans = coll.find({"$and": [{'type': 'Card'}, {'idList': lists['_id']}, {'labels.name': {"$all": [label['name'], "intermediate level"]} }]}).count()
        
        if ans > 0:
            html_card = "<td><b>"+str(ans)+"</b></td>"
            html_table = html_table + html_card
            print (lists['name'], label['name'], 'intermediate level', ans)
        else:
            html_card = "<td>"+str(ans)+"</td>"
            html_table = html_table + html_card
        
    html_table = html_table + "</tr>"
    #total_level = coll.find({"$and": [{'type': 'Card'}, {'labels.name': {"$all": [label['name'], "intermediate level"]} }]}).count()
    #html_table = "<td>" + str(total_level) + "</td></tr>"
    
html_table = html_table+"</table></html>"
hs = open ("htmlTrelloTable.html", "w")
hs.write(html_table)

#print (html_table)
hs.close()
