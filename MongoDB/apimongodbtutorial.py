#http://api.mongodb.com/python/current/tutorial.html

# Steps:
# 1. Connect ke MongoClient (ada di localhost port 27017 by default)
# 2. Membuat database dengan cara client. [nama-database]
# 3. Membuat collections (tabel) dibawah db. [nama-collection]
# 4. Mengisi documents (record) pada collections dengan insert

import pprint
from pymongo import MongoClient
client = MongoClient()
db = client['test-database']
collection = db['test-collection']
# tidak muncul karena collection baru 'test-collection' akan dibuat ketika
# ada insert document

import datetime
post = {"author" : "Mike",
        "text" : "My first blog post!",
        "tags" : ["mongodb", "python", "pymongo"],
        "date" : datetime.datetime.utcnow()
        }

#make collection (make table)
posts = db['posts']

post_insert = posts.insert_one(post)
post_id = post_insert.inserted_id

'''
# A common task in web applications is to get an ObjectId from the request URL
# and find the matching document. It’s necessary in this case to convert
# the ObjectId from a string before passing it to find_one:

from bson.objectid import ObjectId

# The web framework gets post_id from the URL and passes it as a string
def get(post_id):
    # Convert from string to ObjectId:
    document = client.db.collection.find_one({'_id': ObjectId(post_id)})
'''


mylist = [
  { "name": "Amy", "address": "Apple st 652"},
  { "name": "Hannah", "address": "Mountain 21"},
  { "name": "Michael", "address": "Valley 345"},
  { "name": "Sandy", "address": "Ocean blvd 2"},
  { "name": "Betty", "address": "Green Grass 1"},
  { "name": "Richard", "address": "Sky st 331"},
  { "name": "Susan", "address": "One way 98"},
  { "name": "Vicky", "address": "Yellow Garden 2"},
  { "name": "Ben", "address": "Park Lane 38"},
  { "name": "William", "address": "Central st 954"},
  { "name": "Chuck", "address": "Main Road 989"},
  { "name": "Viola", "address": "Sideway 1633"}
]

mylist_insert = db.orang.insert_many(mylist)

# find -> select * (SQL) tapi menggunakan cursor, jadi harus menggunakan iterator
# untuk {} pertama dalam find = where (SQL)
# untuk {} kedua dalam find = select ..., dimana semuanya harus sama 1 atau sama 0
# kecuali untuk _id (bisa berbeda dari yang lain)
for orang in db.orang.find({}, {"_id": 0, "name": 1}):
    print (orang)

# for orang in db.orang.find({}, {"name": 1, "address": 0}): # akan menghasilkan error
# jika ingin select tertentu saja pakai yang "..." : 1

client.close()
