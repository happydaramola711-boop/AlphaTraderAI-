import os
from telegram import Update
from telegram.ext import ContextTypes
from config import ADMIN_ID, LOG_FILE
from database.database import get_stats, get_subscribed_users

async def broadcast_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id != ADMIN_ID:
        return

    if not context.args:
        await update.message.reply_text("⚠️ Usage: /broadcast <your message>")
        return

    message = " ".join(context.args)
    subscribers = get_subscribed_users()
    sent_count = 0

    for uid in subscribers:
        try:
            await context.bot.send_message(
                chat_id=uid,
                text=f"📢 <b>Announcement:</b>\n\n{message}",
                parse_mode="HTML"
            )
            sent_count += 1
        except Exception:
            pass

    await update.message.reply_text(f"✅ Broadcast delivered to {sent_count}/{len(subscribers)} subscribers.")

async def stats_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id != ADMIN_ID:
        return

    total, active = get_stats()
    await update.message.reply_text(
        f"📊 <b>Bot Metrics</b>\n\nTotal Registered Users: {total}\nActive Subscribers: {active}",
        parse_mode="HTML"
    )

async def logs_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id != ADMIN_ID:
        return

    if os.path.exists(LOG_FILE):
        with open(LOG_FILE, "r", encoding="utf-8") as f:
            lines = f.readlines()[-30:]
        await update.message.reply_text(
            f"📄 <b>Recent Application Logs:</b>\n\n<code>{''.join(lines)}</code>",
            parse_mode="HTML"
        )
    else:
        await update.message.reply_text("No active log file found.")
