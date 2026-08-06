import feedparser
import logging

logger = logging.getLogger(__name__)

FEEDS = [
    "https://www.investing.com/rss/news_25.rss",
    "https://cointelegraph.com/rss"
]

def fetch_market_news(limit: int = 5) -> str:
    """Parse news RSS feeds for recent market updates."""
    articles = []
    for url in FEEDS:
        try:
            feed = feedparser.parse(url)
            for entry in feed.entries[:limit]:
                articles.append({
                    "title": entry.title,
                    "link": entry.link
                })
        except Exception as e:
            logger.error("Failed parsing RSS feed %s: %s", url, e)

    if not articles:
        return "📰 No news items currently available."

    output = "<b>📰 Latest Forex & Crypto Market News</b>\n\n"
    for idx, item in enumerate(articles[:limit], start=1):
        output += f"{idx}. <a href='{item['link']}'>{item['title']}</a>\n\n"

    return output
