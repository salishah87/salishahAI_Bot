import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes
from config import BOT_TOKEN
from bot.chat import handle_message

logging.basicConfig(level=logging.INFO)

async def message_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await handle_message(update, context)

def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, message_handler))

    print("Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
