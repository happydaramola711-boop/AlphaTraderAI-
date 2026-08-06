from telegram import Update
from telegram.ext import ContextTypes
from database.database import set_subscription

async def subscribe_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    set_subscription(user_id, True)
    await update.message.reply_text("✅ You have subscribed to daily market updates.")

async def unsubscribe_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    set_subscription(user_id, False)
    await update.message.reply_text("❌ You have unsubscribed from daily market updates.")

async def settings_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = (
        "<b>⚙️ Notification Preferences</b>\n\n"
        "Manage your active subscription using shortcuts:\n"
        "• Enable Daily Updates: /subscribe\n"
        "• Disable Daily Updates: /unsubscribe"
    )
    target = update.callback_query.message if update.callback_query else update.message
    await target.reply_text(text, parse_mode="HTML")

async def about_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = (
        "<b>🤖 About AlphaTraderAI (@AlphaTraderAI99_bot)</b>\n\n"
        "AlphaTraderAI is a trading assistance bot designed for educational resources, pricing updates, and market news.\n\n"
        "⚠️ <i>Disclaimer: AlphaTraderAI is strictly educational. It does not issue financial advice, guarantee returns, or execute trades.</i>"
    )
    target = update.callback_query.message if update.callback_query else update.message
    await target.reply_text(text, parse_mode="HTML")
