import logging
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from database.database import get_subscribed_users
from services.rss import fetch_market_news

logger = logging.getLogger(__name__)

async def send_daily_update(application):
    """Broadcast morning market digest to subscribers."""
    subscribers = get_subscribed_users()
    if not subscribers:
        logger.info("Daily update skipped: No active subscribers found.")
        return

    news = fetch_market_news(limit=3)
    message = f"<b>🌅 Daily AlphaTraderAI Digest</b>\n\n{news}"

    for user_id in subscribers:
        try:
            await application.bot.send_message(
                chat_id=user_id,
                text=message,
                parse_mode="HTML",
                disable_web_page_preview=True
            )
        except Exception as e:
            logger.warning("Could not dispatch daily update to user %s: %s", user_id, e)

def setup_scheduler(app):
    """Configure and boot APScheduler background jobs."""
    scheduler = AsyncIOScheduler()
    scheduler.add_job(
        send_daily_update,
        trigger="cron",
        hour=8,
        minute=0,
        kwargs={"application": app}
    )
    scheduler.start()
    logger.info("APScheduler running: Daily update scheduled for 08:00 AM UTC.")
