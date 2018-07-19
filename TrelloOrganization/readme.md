Requirement of Scaling Organization Trello Boards:
1. Webhook every board to the same file .php (create python to curl this webhook)
2. Input -> 1 Document per Board in collection + counter for each Action (update)
3. Shell exec python `file.py` *BoardID from webhook model *action counter
   * as arguments argv
4. In python, update counter per Document if any action happened. If action == 10, update board

Generate Webhook :
1. Open terminal
2. Run `python curl_createwebhook.py` to create curl command to add webhook
3. Open `curl_create_webhook.txt` after generating, copy all command in terminal
4. To delete webhook, run `python curl_deletewebhook.py` in terminal

## Webhook -> PHP -> Python -> MongoDB
