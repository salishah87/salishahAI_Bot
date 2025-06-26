from telegram.ext import Application
from bot.dispatcher import setup_handlers
from config.settings import TELEGRAM_TOKEN

async def main():
    app = Application.builder().token(TELEGRAM_TOKEN).build()
    setup_handlers(app)
    print("Bot started...")
    await app.run_polling()

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
