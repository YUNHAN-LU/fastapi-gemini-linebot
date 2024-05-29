from fastapi import FastAPI , HTTPException, Request
from linebot import LineBotApi, WebhookHandler
from linebot.models import MessageEvent, TextMessage, TextSendMessage
from api.gemini import Gemini
import os

app = FastAPI()
line_bot_api = LineBotApi(os.getenv("LINE_CHANNEL_ACCESS_TOKEN"))
line_handler = WebhookHandler(os.getenv("LINE_CHANNEL_SECRET"))
working_status = os.getenv("DEFALUT_TALKING", default = "true").lower() == "true"
gemini = Gemini()


@app.post("/webhook")
async def callback(request:Request):
    # get X-Line-Signature header value
    signature = request.headers["X-Line-Signature"]
    # get request body as text
    body = await request.body()
    # handle webhook body
    try:
        line_handler.handle(body.decode(), signature)
    except:
        print(body, signature)
        raise HTTPException(400)
    return 'OK'


@line_handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
 
    if event.message.type != "text":
        return

    gemini.add_msg(f"HUMAN:{event.message.text}?\n")
    reply_msg = gemini.get_response().replace("AI:", "", 1)
    gemini.add_msg(f"AI:{reply_msg}\n")
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=reply_msg)
    )


if __name__ == "__main__":
    app.run()