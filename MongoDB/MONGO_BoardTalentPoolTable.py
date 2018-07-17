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
html_table = html_table + "<th>Location</th>"

for lists in coll.find({'type': 'List'}):
    html_list = "<th>"+str(lists['name'])+"</th>"
    html_table = html_table + html_list


html_table = html_table + "<th>Total Level</th></tr>"
#tidak dapat ditotal secara vertikal dan horizontal karena ada potongan diantaranya (misalnya backend, junior, intermediate)
#total_vertical = 0
#total_horizontal = 0


level_list = []
for label in coll.find({'type': 'Label'}):
    if 'level' in label['name']:
        #level_str = label['name'].split()
        #print (level_str[0])
        #level.append(level_str[0])
        level_list.append(label['name'])

location_list = ['remote', 'onsite']

# Junior, Intermediate Level in 2 loops
for label in coll.find({'type': 'Label'}):
    # Differentiate by level (Junior / Intermediate / any level)
    for level in level_list:
        #html_table = html_table + "<tr><td>" + label['name'] + "</td><td>" + level +"</td>"
        for location in location_list:
            #html_table = html_table + "<td>" + location + "</td>"
            html_table = html_table + "<tr><td>" + label['name'] + "</td><td>" + level + "</td><td>" + location + "</td>"
            for lists in coll.find({'type': 'List'}):
                ans = coll.find({"$and": [{'type': 'Card'}, {'closed': False}, {'idList': lists['_id']}, {'labels.name': {"$all": [label['name'], level, location]} }]}).count()
                #total_vertical = total_vertical + ans
                
                if ans > 0:
                    html_card = "<td><b>"+str(ans)+"</b></td>"
                    html_table = html_table + html_card
                    #print (lists['name'], label['name'], 'junior level', ans)
                else:
                    html_card = "<td>"+str(ans)+"</td>"
                    html_table = html_table + html_card

            # total sum per job per junior level
            total_level = coll.find({"$and": [{'type': 'Card'}, {'closed': False}, {'labels.name': {"$all": [label['name'], level, location]} }]}).count()
            html_table = html_table + "<td><h3>" + str(total_level) + "</h3></td></tr>"

        # Add Job and Level (without Location)
        html_table = html_table + "<tr><td>" + label['name'] + "</td><td>" + level + "</td><td>" + 'NO LOCATION' + "</td>"
        for lists in coll.find({'type': 'List'}):
            ans = coll.find({"$and": [{'type': 'Card'}, {'closed': False}, {'idList': lists['_id']}, {'labels.name': {"$all": [label['name'], level]} }]}).count()
            #total_vertical = total_vertical + ans
            
            if ans > 0:
                html_card = "<td><b>"+str(ans)+"</b></td>"
                html_table = html_table + html_card
                #print (lists['name'], label['name'], 'junior level', ans)
            else:
                html_card = "<td>"+str(ans)+"</td>"
                html_table = html_table + html_card

        total_level = coll.find({"$and": [{'type': 'Card'}, {'closed': False}, {'labels.name': {"$all": [label['name'], level]} }]}).count()
        html_table = html_table + "<td><h3>" + str(total_level) + "</h3></td></tr>"


    # Add NO LEVEL
    for location in location_list:    
        html_table = html_table + "<tr><td>" + label['name'] + "</td><td>" + 'NO LEVEL' +"</td><td>" + location + "</td>"
        for lists in coll.find({'type': 'List'}):
            ans = coll.find({"$and": [{'type': 'Card'}, {'closed': False}, {'idList': lists['_id']}, {'labels.name': {"$eq": label['name'], "$eq":location, "$nin":level_list } }]}).count()

            if ans > 0:
                html_card = "<td><b>"+str(ans)+"</b></td>"
                html_table = html_table + html_card
                #print (lists['name'], label['name'], 'junior level', ans)
            else:
                html_card = "<td>"+str(ans)+"</td>"
                html_table = html_table + html_card

        total_level = coll.find({"$and": [{'type': 'Card'}, {'closed': False}, {'labels.name': {"$eq": label['name'], "$eq":location, "$nin":level_list } }]}).count()
        html_table = html_table + "<td><h3>" + str(total_level) + "</h3></td></tr>"

    # Add NO LEVEL, NO LOCATION
    html_table = html_table + "<tr><td>" + label['name'] + "</td><td>" + 'NO LEVEL' +"</td><td>" + 'NO LOCATION' + "</td>"
    for lists in coll.find({'type': 'List'}):
        ans = coll.find({"$and": [{'type': 'Card'}, {'closed': False}, {'idList': lists['_id']}, {'labels.name': {"$eq": label['name'], "$nin":level_list } }]}).count()

        if ans > 0:
            html_card = "<td><b>"+str(ans)+"</b></td>"
            html_table = html_table + html_card
            #print (lists['name'], label['name'], 'junior level', ans)
        else:
            html_card = "<td>"+str(ans)+"</td>"
            html_table = html_table + html_card

    total_level = coll.find({"$and": [{'type': 'Card'}, {'closed': False}, {'labels.name': {"$eq": label['name'], "$nin":level_list } }]}).count()
    html_table = html_table + "<td><h3>" + str(total_level) + "</h3></td></tr>"


    '''    
    # Intermediate Level
    html_table = html_table + "<tr><td>" + label['name'] + "</td><td>Intermediate</td>"
    for lists in coll.find({'type': 'List'}):
        ans = coll.find({"$and": [{'type': 'Card'}, {'closed': False}, {'idList': lists['_id']}, {'labels.name': {"$all": [label['name'], "intermediate level"]} }]}).count()
        #total_vertical = total_vertical + ans
        
        if ans > 0:
            html_card = "<td><b>"+str(ans)+"</b></td>"
            html_table = html_table + html_card
            #print (lists['name'], label['name'], 'intermediate level', ans)
        else:
            html_card = "<td>"+str(ans)+"</td>"
            html_table = html_table + html_card        

    # total sum per job per intermediate level        
    total_level = coll.find({"$and": [{'type': 'Card'}, {'closed': False}, {'labels.name': {"$all": [label['name'], "intermediate level"]} }]}).count()
    html_table = html_table + "<td><h3>" + str(total_level) + "</h3></td></tr>"
    '''
# total sum per list (BELUM berdasarkan Job & level
html_table = html_table + """<tr><td colspan="3">""" + 'Total List' + "</td>"
for lists in coll.find({'type': 'List'}):
    ans = coll.find({"$and": [{'type': 'Card'}, {'idList': lists['_id']}, {'closed': False} ]}).count()
    #total_horizontal = total_horizontal + ans
    html_table = html_table + "<td><h3>" + str(ans) + "</h3></td>"

#total_all = total_vertical + total_horizontal
#html_table = html_table + "<td><h2>" + str(total_all) + "</h2></td></tr>"
html_table = html_table+"</table></html>"
hs = open ("htmlTrelloTable.html", "w")
hs.write(html_table)
hs.close()




client.close()

# exclude: tech in asia, remote, onsite, Mahasiswa Warness
# split: junior level, intermediate level -> determine the level of the job
