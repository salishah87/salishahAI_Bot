from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes
from chat import ask_openrouter
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("سلام! من بات هوش مصنوعی هستم. پیام خود را ارسال کنید.")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_message = update.message.text
    messages = [{"role": "user", "content": user_message}]
    try:
        response = ask_openrouter(messages)
        bot_reply = response['choices'][0]['message']['content']
    except Exception as e:
        bot_reply = str(e)
    await update.message.reply_text(bot_reply)

if __name__ == "__main__":
    import config
    application = ApplicationBuilder().token(config.BOT_TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), handle_message))
    application.run_polling()
