import os
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

def start(update: Update, context: CallbackContext):
    update.message.reply_text('صلي على محمد ﷺ')

def main():
    token = os.environ.get('8067374289:AAHmgMpF2Mhe7Scc1c8-g5ywYYlNdNEWF_Q')
    if not token:
        print("Error: TELEGRAM_BOT_TOKEN not set!")
        return
    
    updater = Updater(token)
    
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler("start", start))
    
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()