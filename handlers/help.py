from telegram import Update
from telegram.ext import ContextTypes

async def help_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    help_text = (
        "<b>📖 AlphaTraderAI Command Directory</b>\n\n"
        "/start - Launch main interactive dashboard\n"
        "/help - Display command directory\n"
        "/news - Fetch latest Forex & Crypto market news\n"
        "/crypto - Top cryptocurrency price updates\n"
        "/forex - Major Forex pair rate overview\n"
        "/analysis - Educational technical market structure\n"
        "/learn - Trading guides and foundational tips\n"
        "/calendar - Upcoming macroeconomic events\n"
        "/tips - Random risk management tips\n"
        "/subscribe - Enable daily digests\n"
        "/unsubscribe - Disable daily digests\n"
        "/settings - Manage user notification options\n"
        "/about - Information regarding AlphaTraderAI"
    )
    await update.message.reply_text(help_text, parse_mode="HTML")
