import random

TRADING_TIPS = [
    "⚠️ <b>Risk Management:</b> Never risk more than 1% to 2% of your account capital on a single trade.",
    "📊 <b>Plan Your Trade:</b> Establish your Entry, Stop Loss, and Take Profit before entering a position.",
    "🧠 <b>Psychology:</b> Avoid revenge trading following a loss. Stick strictly to your trading rules.",
    "📉 <b>Trend Trading:</b> Align your positions with the higher timeframe direction to increase probability."
]

def get_random_tip() -> str:
    """Return a random risk management tip."""
    return random.choice(TRADING_TIPS)
