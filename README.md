# PythonTrello

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
# PythonTrello
