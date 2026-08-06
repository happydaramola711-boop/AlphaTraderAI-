from telegram import Update
from telegram.ext import ContextTypes
from database.database import add_or_update_user
from utils.keyboards import get_main_keyboard

async def start_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    add_or_update_user(user.id, user.username or "", user.first_name)

    welcome_text = (
        f"👋 Welcome to <b>AlphaTraderAI</b>, {user.first_name}!\n\n"
        "Your AI-powered assistant for Forex and Crypto news, price insights, technical analysis, and risk management education.\n\n"
        "Choose an option from the menu below to get started:"
    )

    await update.message.reply_text(
        text=welcome_text,
        reply_markup=get_main_keyboard(),
        parse_mode="HTML"
    )
