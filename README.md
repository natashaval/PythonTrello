# PythonTrello

### 4 Juli 2018
##### Ambil Board, Lists, Cards, Checklists

1. Get Trello API key. You can retrieve your API key by logging into [Trello App 
Key](https://trello.com/app-key/).
2. Generate a Token. Copy: 
https://trello.com/1/authorize?expiration=never&scope=read,write,account&response_type=token&name=Server%20Token&key=` 
[[ YOUR TRELLO API KEY ]]
`
3. Masuk ke folder 2018-7-4_DOT_Trello, file python: untuk membuka board dalam organisasi PT DOT Indonesia 
(ptdotindonesia1), membuka list dalam board, membuka cards dalam lists, membuka checklist dari card, dan 
menghitung persentase setiap checklist

4. Run file `GET_organization_boards.py` pada [Python3] (www.python.org/downloads/).
- Pada file, masukkan Trello API key dan Token
- Pilih nama board yang tersedia
- Akan muncul list yang ada dalam board
- Tentukan apakah akan menampilkan seluruh cards dalam list atau hanya memilih salah satu list
- Jika ya, akan menampilkan seluruh cards, jika tidak akan menampilkan salah satu cards dalam nama list yang 
telah dimasukkan
- Akan muncul cards beserta checklist yang ada dan persentase setiap checklistnya 

==========
boardaction.py -> menunjukkan aktivitas log pada salah satu board dan melakukan filter yang telah dilakukan oleh 
member
boardpublic.py -> menunjukkan hasil boards, lists, cards serta dapat melakukan filter berdasarkan label

### 5 Juli 2018
##### Mengambil Action Log dan menyimpannya dalam MongoDB database)

Maksimal Action yang diambil dari TrelloAPI 50 Actions (?)

Tutorial install:
1. Install MongoDB from https://www.mongodb.com/download-center#community
2. If on Windows, follow tutorial 
https://docs.mongodb.com/manual/tutorial/install-mongodb-on-windows/
3. Start MongoDB database
"C:\Program Files\MongoDB\Server\4.0\bin\mongod.exe" --dbpath="[[ path to database 
directory ]]"
C:\Program Files\... -> default MongoDB path
3. Connect to MongoDB
"C:\Program Files\MongoDB\Server\4.0\bin\mongo.exe"

File ada di folder `MongoDB` file `MONGO_TrelloAction.py`

1. Masukkan nama database
2. Masukkan Trello key dan API
3. Pilih salah satu board untuk diambil activity log nya
4. Data akan tersimpan di collection dengan nama yang sama dengan nama board

* Bugs, jika terdapat nama board yang mengandung ' ' akan error untuk menghapusnya

Cara cek, masuk di python console / Python Shell (sebelumnya sudah menjalankan script 
diatas):
1. Cek database = `client.database_names()`
2. Drop database = `client.drop_database ( [[Nama Database]] )
3. Cek collection = `db.collection_names()`
4. Drop collection = `db.drop_collection( [[Nama Collection]] )`
5. Count document in collection = `db.[[Nama Collection]].count()`
6. List isi document = `for x in db.[[Nama Collection]].find(): pprint.pprint (x)`

# PythonTrello
