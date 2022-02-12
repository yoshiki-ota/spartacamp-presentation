from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

import urllib.request
import os
import json
import scrape as sc

app = Flask(__name__)

# 環境変数取得
YOUR_CHANNEL_ACCESS_TOKEN = os.environ[
    "6kCwaWhEnjwjOp8wH86Cj01erEkmqVCQKDLjRUfJWUb5+CVVT7NJUz5BGglJSpetag7V" \
    "/EEFoSvPBTDmzYVX36TLxnZP6nutwaCN8PzUufbXHUe81doK24q06WrrPrBN/rXWFPmW7u/AJWBAFlmPFAdB04t89/1O/w1cDnyilFU="]
YOUR_CHANNEL_SECRET = os.environ["f1786025ab6db06b213b8f0c2776e7e2"]

line_bot_api = LineBotApi(YOUR_CHANNEL_ACCESS_TOKEN)
handler = WebhookHandler(YOUR_CHANNEL_SECRET)


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'


# メッセージリプライ
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    # ユーザからの検索ワードを取得
    word = event.message.text

    # 記事取得関数を呼び出し
    result = sc.getNews(word)

    # 応答メッセージ（記事検索結果）を送信
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=result)
    )


if __name__ == "__main__":
    #    app.run()
    port = int(os.getenv("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
