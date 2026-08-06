import logging
from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    CallbackQueryHandler,
    ContextTypes
)

from config import BOT_TOKEN, LOG_FILE
from database.database import init_db
from utils.scheduler import setup_scheduler

# Import Handlers
from handlers.start import start_handler
from handlers.help import help_handler
from handlers.news import news_handler
from handlers.prices import crypto_handler, forex_handler
from handlers.analysis import analysis_handler
from handlers.education import learn_handler, calendar_handler, tips_handler
from handlers.alerts import subscribe_handler, unsubscribe_handler, settings_handler, about_handler
from handlers.admin import broadcast_handler, stats_handler, logs_handler

# Logging setup
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
    handlers=[
        logging.FileHandler(LOG_FILE),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

async def callback_router(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Router for inline keyboard callback data."""
    query = update.callback_query
    await query.answer()

    mapping = {
        "cmd_news": news_handler,
        "cmd_crypto": crypto_handler,
        "cmd_forex": forex_handler,
        "cmd_analysis": analysis_handler,
        "cmd_learn": learn_handler,
        "cmd_calendar": calendar_handler,
        "cmd_tips": tips_handler,
        "cmd_settings": settings_handler,
        "cmd_about": about_handler
    }

    handler = mapping.get(query.data)
    if handler:
        await handler(update, context)

def main():
    """Start and run @AlphaTraderAI99_bot."""
    init_db()

    app = ApplicationBuilder().token(BOT_TOKEN).build()

    # Public User Commands
    app.add_handler(CommandHandler("start", start_handler))
    app.add_handler(CommandHandler("help", help_handler))
    app.add_handler(CommandHandler("news", news_handler))
    app.add_handler(CommandHandler("crypto", crypto_handler))
    app.add_handler(CommandHandler("forex", forex_handler))
    app.add_handler(CommandHandler("analysis", analysis_handler))
    app.add_handler(CommandHandler("learn", learn_handler))
    app.add_handler(CommandHandler("calendar", calendar_handler))
    app.add_handler(CommandHandler("tips", tips_handler))
    app.add_handler(CommandHandler("subscribe", subscribe_handler))
    app.add_handler(CommandHandler("unsubscribe", unsubscribe_handler))
    app.add_handler(CommandHandler("settings", settings_handler))
    app.add_handler(CommandHandler("about", about_handler))

    # Restricted Admin Commands
    app.add_handler(CommandHandler("broadcast", broadcast_handler))
    app.add_handler(CommandHandler("stats", stats_handler))
    app.add_handler(CommandHandler("logs", logs_handler))

    # Inline Keyboard Handler
    app.add_handler(CallbackQueryHandler(callback_router))

    # Setup Scheduled Background Tasks
    setup_scheduler(app)

    logger.info("AlphaTraderAI99_bot engine initialized and listening...")
    app.run_polling()

if __name__ == "__main__":
    main()
