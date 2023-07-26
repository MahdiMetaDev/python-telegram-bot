import os
from dotenv import load_dotenv
from typing import Final

from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

load_dotenv()

# bot information
TOKEN: Final = os.getenv("BOT_TOKEN")
BOT_USERNAME: Final = os.getenv("BOT_USERNAME")


# commands
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Hello, welcome to metanext bot.'
        ' what do you want me to do for you?')

async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')

# responses
def handle_response(text: str) -> str:
    processed: str = text.lower()

    if 'hello' in processed:
        return 'Hey there!'
    
    if 'how are you' in processed:
        return 'I am good!'
    
    return 'I do not understand what you wrote...'


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_type: str = update.message.chat.type
    text: str = update.message.text

    print(f'User ({update.message.chat.id}) in {message_type}: "{text}"')

    if message_type == 'group':
        if BOT_USERNAME in text:
            new_text: str = text.replace(BOT_USERNAME, '').strip()
            response: str = handle_response(new_text)
        else:
            return
    else:
        response: str = handle_response(text)
    
    print('Bot: ', response)

    await update.message.reply_text(response)


async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f'Update {update} caused error {context.error}')




if __name__ == "__main__":
    
    print('Starting bot...')
    app = ApplicationBuilder().token(token=TOKEN).build()

    # Commands
    app.add_handler(CommandHandler("hello", hello))
    app.add_handler(CommandHandler("start", start))

    # Messages
    app.add_handler(MessageHandler(filters.TEXT, handle_message))

    # Errors
    app.add_error_handler(error)
    
    # Polls the bot
    print('Polling...')
    app.run_polling(poll_interval=3)
