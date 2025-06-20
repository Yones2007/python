import os
import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# إعداد التسجيل
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('صلي على محمد ﷺ')

def main():
    # الحصول على التوكن من متغيرات البيئة
    token = os.getenv('8067374289:AAHmgMpF2Mhe7Scc1c8-g5ywYYlNdNEWF_Q')
    if not token:
        logging.error("لم يتم تعيين TELEGRAM_BOT_TOKEN!")
        return

    # إنشاء التطبيق وإضافة المعالج
    application = Application.builder().token(token).build()
    application.add_handler(CommandHandler("start", start))

    # تشغيل البوت
    application.run_polling()

if __name__ == '__main__':
    main()
