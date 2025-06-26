from telegram.ext import MessageHandler, filters, ContextTypes
from telegram import Update
from core.chat_engine import get_ai_response

async def handle_chat(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_input = update.message.text
    user_id = update.message.from_user.id
    response = await get_ai_response(user_input, user_id)
    await update.message.reply_text(response)

chat_handler = MessageHandler(filters.TEXT & ~filters.COMMAND, handle_chat)
