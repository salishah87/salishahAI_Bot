from telegram.ext import MessageHandler, filters, ContextTypes
from telegram import Update
from core.chat_engine import get_ai_response
from users.models import register_user, log_message
from users.limits import check_and_update_limit

async def handle_chat(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.message.from_user
    await register_user(user.id, user.username)

    allowed = await check_and_update_limit(user.id)
    if not allowed:
        await update.message.reply_text("⛔ سقف استفاده روزانه‌ات تموم شده! فردا دوباره امتحان کن.")
        return

    user_input = update.message.text
    response = await get_ai_response(user_input, user.id)

    await update.message.reply_text(response)
    await log_message(user.id, user_input, response)

chat_handler = MessageHandler(filters.TEXT & ~filters.COMMAND, handle_chat)
