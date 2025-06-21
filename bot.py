from telegram.ext import ApplicationBuilder, CommandHandler
import os

async def start(update, context):
    await update.message.reply_text("صلي على محمد ﷺ")

app = ApplicationBuilder().token(os.environ["BOT_TOKEN"]).build()
app.add_handler(CommandHandler("start", start))

app.run_polling()
