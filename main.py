import os
from dotenv import load_dotenv
from typing import Final

from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

load_dotenv()

TOKEN: Final = os.getenv("BOT_TOKEN")

async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')

app = ApplicationBuilder().token(token=TOKEN).build()

app.add_handler(CommandHandler("hello", hello))

if __name__ == "__main__":
    app.run_polling()
