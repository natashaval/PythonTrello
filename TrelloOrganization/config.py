# config to set up Trello (key, token); DB (host, DBname, collection); Webhook(URL)

Trello_config = {
    'api_key' : '19e1e8779951830e0d86122f201454c6',
    'token' : '6fec5904bd2db30d876191d45f68bbec0db6322e36ebaa2ad80c2bcd7948d5f9',
    'organization_name' : 'ptdotindonesia1'
}

Database_config = {
    'host' : 'mongodb://localhost:27017/',
    'database_name' : 'Trello',
    'collection_name' : 'DOT-Indonesia'
}

Webhook = {
    'hook_url' : 'http://bc267cb3.ngrok.io/trelloorg/webhook.php'
}
