from telegram import Update
from telegram.ext import ContextTypes
from services.crypto import fetch_crypto_prices
from services.forex import fetch_forex_overview

async def crypto_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    content = fetch_crypto_prices()
    target = update.callback_query.message if update.callback_query else update.message
    await target.reply_text(content, parse_mode="HTML")

async def forex_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    content = fetch_forex_overview()
    target = update.callback_query.message if update.callback_query else update.message
    await target.reply_text(content, parse_mode="HTML")
