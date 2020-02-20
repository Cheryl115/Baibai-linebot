#-*-coding:utf-8-*-
from flask import Flask, request, abort
from linebot import(
    LineBotApi, WebhookHandler
)
from linebot.exceptions import(
    InvalidSignatureError   
)
from linebot.models import(
    MessageEvent, TextMessage, TextSendMessage, ImageSendMessage    
)

app = Flask(__name__)

# Channel Access token
line_bot_api = LineBotApi('VP4eBVJ2kL9RMt+qUaZaENdVe6iWofCWFbP88v1saK7mm8JbYRw6b5fI6RzypwaXcXvkcEZ2UjARLiRljALZ/GZL0bt4dAaK/Y41RPtSnIJSgJBMIdNk4hyr7slx5eQbbmj2JLHluTyWq565bKpQugdB04t89/1O/w1cDnyilFU=')
# Channel Serect
handler = WebhookHandler('5b970bc4adae550146051e40223f24c8')

# 監聽來自/callback的Post Request

@app.route("/callback", methods=['Post'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request Body: " + body)

    #handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSinatureError:
        abort(400)
    return 'OK'

#處理訊息
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    print(event)
    text = event.message.text
    message = TextSendMessage(text)
    line_bot_api.reply_message(
        event.reply_token,
        message)

import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)




