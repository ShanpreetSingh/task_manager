import os
import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
from django.conf import settings
from .models import TelegramUser

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    username = update.effective_user.username or str(update.effective_user.id)
    
    TelegramUser.objects.update_or_create(
        chat_id=chat_id,
        defaults={'username': username}
    )
    
    await update.message.reply_text(
        f"Hello {username}! You've been registered in our system.\n"
        f"Your chat ID: {chat_id}"
    )

def setup_bot():
    if not settings.TELEGRAM_BOT_TOKEN:
        logging.warning("TELEGRAM_BOT_TOKEN not set - bot disabled")
        return
    
    application = Application.builder().token(settings.TELEGRAM_BOT_TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    
    logging.info("Starting Telegram bot")
    application.run_polling()