from telegram import Update
from telegram.ext import CallbackContext
from core.chat import ask_openrouter
from db.chatlog import save_chat

def handle_message(update: Update, context: CallbackContext):
    user_input = update.message.text
    user_id = update.effective_user.id

    try:
        reply = ask_openrouter(user_input, user_id)
        update.message.reply_text(reply)

        # ذخیره در دیتابیس
        save_chat(user_id, user_input, reply)

    except Exception as e:
        update.message.reply_text("❌ خطا در ارتباط با هوش مصنوعی.")
        print(f"Error: {e}")
