from telegram.ext import ApplicationBuilder, CommandHandler
import os

async def start(update, context):
    await update.message.reply_text("صلي على محمد ﷺ")

app = ApplicationBuilder().token(os.environ["8067374289:AAHmgMpF2Mhe7Scc1c8-g5ywYYlNdNEWF_Q"]).build()
app.add_handler(CommandHandler("start", start))

app.run_polling()
