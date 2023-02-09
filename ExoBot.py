#Import library for telegram bot
import requests
from pprint import pprint

TOKEN = '5455890832:AAGh9-yUlkri7iXD5V4AOlWDdRN-pAiOBLY'

#Send message 
def send_message(text:str, chat_id:int):
    url = f'https://api.telegram.org/bot{TOKEN}/sendMessage'
    answer = requests.post(url, data={'chat_id': chat_id, 'text': text})
    return answer.json()
#Get updates
def get_updates():
    url = f'https://api.telegram.org/bot{TOKEN}/getUpdates'
    answer = requests.get(url)
    data = answer.json()
    # Get result form data
    result = data['result']
    return result

def get_last_update(updates):
    # Get last update

    # Get message text
    text = updates['message'].get('text')
    # Get chat id
    chat_id = updates['message']['chat']['id']
    # Get update id
    update_id = updates['update_id']
    return text, chat_id,update_id


# Last update id
# Send message through loop
s = 0
while True:
    result = get_updates() 
    text,chat_id,update_id = get_last_update(result[-1])
    if s < update_id:
        send_message(text, chat_id)
        s = update_id