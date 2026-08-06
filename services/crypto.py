import requests
import logging
from config import COINGECKO_API

logger = logging.getLogger(__name__)

def fetch_crypto_prices() -> str:
    """Fetch cryptocurrency price snapshots from CoinGecko API."""
    url = f"{COINGECKO_API}/simple/price"
    params = {
        "ids": "bitcoin,ethereum,solana,binancecoin,ripple,cardano",
        "vs_currencies": "usd",
        "include_24hr_change": "true"
    }
    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()

        coins = {
            "bitcoin": ("Bitcoin", "₿"),
            "ethereum": ("Ethereum", "Ξ"),
            "solana": ("Solana", "◎"),
            "binancecoin": ("BNB", "🔶"),
            "ripple": ("XRP", "✕"),
            "cardano": ("Cardano", "₳")
        }

        output = "<b>₿ Crypto Market Snapshots</b>\n\n"
        for coin_id, (name, symbol) in coins.items():
            if coin_id in data:
                price = data[coin_id]["usd"]
                change = data[coin_id]["usd_24h_change"]
                trend = "🟢" if change >= 0 else "🔴"
                output += f"{symbol} <b>{name}:</b> ${price:,.2f} ({trend} {change:+.2f}%)\n"

        output += "\n<i>⚠️ Market data provided for educational purposes only.</i>"
        return output
    except Exception as e:
        logger.error("Error fetching crypto prices: %s", e)
        return "⚠️ Unable to fetch live crypto prices right now. Please try again later."
