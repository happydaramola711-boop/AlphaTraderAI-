from telegram import Update
from telegram.ext import ContextTypes
from services.market import fetch_economic_calendar
from utils.helpers import get_random_tip

async def learn_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = (
        "<b>🎓 Educational Trading Center</b>\n\n"
        "• <b>Market Basics:</b> Fundamentals of pips, leverage, and margin.\n"
        "• <b>Technical Analysis:</b> Candlestick formations, chart patterns, and indicators.\n"
        "• <b>Risk Control:</b> Position sizing formulas to protect trading equity.\n\n"
        "<i>Use /tips to view key risk parameters instantly.</i>"
    )
    target = update.callback_query.message if update.callback_query else update.message
    await target.reply_text(text, parse_mode="HTML")

async def calendar_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    calendar = fetch_economic_calendar()
    target = update.callback_query.message if update.callback_query else update.message
    await target.reply_text(calendar, parse_mode="HTML")

async def tips_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    tip = get_random_tip()
    target = update.callback_query.message if update.callback_query else update.message
    await target.reply_text(tip, parse_mode="HTML")
