from telegram import Update
from telegram.ext import ContextTypes
from services.rss import fetch_market_news

async def news_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    news = fetch_market_news()
    if update.callback_query:
        await update.callback_query.message.reply_text(news, parse_mode="HTML", disable_web_page_preview=True)
    else:
        await update.message.reply_text(news, parse_mode="HTML", disable_web_page_preview=True)
