from telegram import Update
from telegram.ext import ContextTypes
from services.ai import generate_educational_analysis

async def analysis_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    analysis = generate_educational_analysis()
    target = update.callback_query.message if update.callback_query else update.message
    await target.reply_text(analysis, parse_mode="HTML")
