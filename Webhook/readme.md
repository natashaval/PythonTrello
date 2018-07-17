Tutorial Add Webhook:
1. Install Ngrok (if not sign up, only available for 8 hours)
(is it only available 1x ??)

2. Run XAMPP Apache to open port 80
3. go to C:\xampp\htdocs\ -> make new folder
4. Make new file with extension .php to be the callback URL in Trello token webhooks
5. Run Ngrok.exe and type in cmd `ngrok http 80`
6. Save http://___.ngrok.io and open web Interface in browser
7. Create [new webhook](https://developers.trello.com/reference/#webhooks-2), fill callback URL with `http://___.ngrok.io/newfolder/newfile.php`
8. Save the result (in need for saving the ID)
9. To [delete webhook](https://developers.trello.com/reference/#webhooksid-1), fill the Webhook ID

10. For every webhook happened, counter will be updated in `counter.txt`
11. Move folder `script` file `MONGO_BoardTalentPool.py` into newfolder
12. If counter == 49, run Python script to get Cards, customFields, card_customFieldsItems, Labels, Lists, and Actions into MongoDB.
