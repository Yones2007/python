from flask import Flask, request
import telegram
import os

TOKEN = os.environ["BOT_TOKEN"]
bot = telegram.Bot(token=TOKEN)

app = Flask(__name__)

@app.route(f"/{TOKEN}", methods=["POST"])
def respond():
    update = telegram.Update.de_json(request.get_json(force=True), bot)

    if update.message and update.message.text == "/start":
        chat_id = update.message.chat.id
        bot.send_message(chat_id=chat_id, text="صلي على محمد")
    
    return "ok"

@app.route("/")
def index():
    return "Bot is running."

if __name__ == "__main__":
    app.run(port=int(os.environ.get("PORT", 5000)))