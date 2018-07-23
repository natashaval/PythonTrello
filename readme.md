Requirement of Scaling Organization Trello Boards:
1. Webhook every board to the same file .php (create python to curl this webhook)
2. Input -> 1 Document per Board in collection + counter for each Action (update)
3. Shell exec python `file.py` *BoardID from webhook model *action counter
   * as arguments argv
4. In python, update counter per Document if any action happened. If action == 10, update board

# Generate Webhook :
1. Open terminal
2. Run `python curl_createwebhook.py` to create curl command to add webhook
3. Open `curl_create_webhook.txt` after generating, copy all command in terminal
4. To delete webhook, run `python curl_deletewebhook.py` in terminal

# Move Board to MongoDB:
1. Run Apache to open port 80
2. Run ngrok to get URL
3. Run MongoDB as readme.md in [the front](github.com/natashaval/PythonTrello#5-juli-2018)
4. Open terminal and run `python trello_board_first.py` to insert organization boards for the first time in 
MongoDB
5. Copy `webhook.php, config.py, Mongo_GetCounter.py, Mongo_ScaleOrganization.py` into C:/xampp/htdocs/[new folder]
6. Run -Generate Webhook- and fill callbackURL as http://___.ngrok.io/[new folder]/webhook.php

# Update Board using Cron (when counter < 10) every 10 minutes
1. Open terminal
2. Run `python Mongo_CronBoard.py` to update every ___ [time] when counter is < 10



## Webhook -> PHP -> Python -> MongoDB