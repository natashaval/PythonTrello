import pprint
from pymongo import MongoClient
client = MongoClient()

db = client['Trello']
coll = db['TalentPool']

import plotly.plotly as py
import plotly.graph_objs as go

list_array = []
for lists in coll.find({'type': 'List'}):
    list_array.append(lists['name'])

ans_array = []
data = []
for label in coll.find({'type': 'Label'}):
    for lists in coll.find({'type': 'List'}):
        ans = coll.find({"$and": [{'type': 'Card'}, {'closed': False}, {'idList': lists['_id']}, {'labels.name': label['name'] }]}).count()
        ans_array.append(ans)

    trace = go.Bar(
        x = list_array,
        y = ans_array,
        name = label['name']
    )

    ans_array = []
    data.append(trace)
        
layout = go.Layout(barmode = 'stack')
fig = go.Figure(data=data, layout=layout)
py.plot(fig, filename='stacked-bar')

client.close()
