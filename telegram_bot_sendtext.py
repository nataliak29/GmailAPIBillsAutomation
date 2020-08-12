import requests
import json
import os

def telegram_bot_sendtext(bot_message):
    cred_file =os.path.dirname(__file__)+"/credentials/info.json"
    f = open(cred_file ,)  
    data = json.load(f)
    bot_token = data['bot_token']
    bot_chatID = data['bot_chatID']
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message

    response = requests.get(send_text)

    return response.json()
    