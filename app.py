import os, sys
from flask import Flask, request
import requests
from pymessenger import Bot

app = Flask(__name__)

PAGE_ACCESS_TOKEN = ""
WEBHOOK_VERIFY_TOKEN = ""

bot = Bot(PAGE_ACCESS_TOKEN)

@app.route('/', methods=['GET'])
def verify():
    try:
        log(request)
        #send a request to check if the user exist
        token = {'token': request.args.get("hub.verify_token")}
        response = requests.get("https://arcane-scrubland-52062.herokuapp.com/", params=token)
        key = response.json()
        global PAGE_ACCESS_TOKEN
        global WEBHOOK_VERIFY_TOKEN
        PAGE_ACCESS_TOKEN = key['access_key']
        WEBHOOK_VERIFY_TOKEN = key['verify_key']
        log(PAGE_ACCESS_TOKEN)
        log(WEBHOOK_VERIFY_TOKEN)
    except Exception as e:
        pass
    
    # Webhook verification
    if request.args.get("hub.mode") == "subscribe" and request.args.get("hub.challenge"):
        if not request.args.get("hub.verify_token") == WEBHOOK_VERIFY_TOKEN:
            return "Verification token mismatch", 403
        return request.args["hub.challenge"], 200
    return "verified", 200

@app.route('/', methods=['POST'])
def webhook():
    data = request.get_json()
    log("THE DATA")
    log(data['object'])

    # if data['object']  == 'page':
    #     for entry in data['entry']:
    #         for messaging_event in entry['messaging']:

    #             #IDs
    #             sender_id = messaging_event['sender']['id']
    #             recipient_id = messaging_event['recipient']['id']
    #             if messaging_event.get('message'):
    #                 if 'text' in messaging_event['message']:
    #                     messaging_text = messaging_event['message']['text']
    #                 else:
    #                     messaging_text = 'no text'
                    
    #                 # Echo
    #                 response = messaging_text
                    
    #                 bot.send_text_message(sender_id, response)

    return "ok", 200

def log(message):
    print(message)
    sys.stdout.flush()



if __name__ == "__main__":
    app.run(debug = True, port = 80)
