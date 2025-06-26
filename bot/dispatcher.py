from bot.handlers.chat import chat_handler
from bot.handlers.image import image_handler
from bot.handlers.speech_to_text import voice_handler

def setup_handlers(app):
    app.add_handler(chat_handler)
    app.add_handler(image_handler)
    app.add_handler(voice_handler)
