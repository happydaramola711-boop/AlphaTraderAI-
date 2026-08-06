import requests
import logging

logger = logging.getLogger(__name__)

def fetch_forex_overview() -> str:
    """Fetch major Forex pair market rates."""
    url = "https://open.er-api.com/v6/latest/USD"
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        rates = response.json().get("rates", {})

        pairs = ["EUR", "GBP", "JPY", "AUD", "CAD", "CHF"]
        output = "<b>💹 Major Forex Market Summary (Base: USD)</b>\n\n"

        for currency in pairs:
            if currency in rates:
                output += f"• <b>USD/{currency}:</b> {rates[currency]:.4f}\n"

        output += "\n<i>⚠️ Market insights are non-advisory and purely educational.</i>"
        return output
    except Exception as e:
        logger.error("Error fetching Forex data: %s", e)
        return "⚠️ Unable to retrieve Forex exchange rates at this time."
