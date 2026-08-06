from telegram import InlineKeyboardButton, InlineKeyboardMarkup

def get_main_keyboard() -> InlineKeyboardMarkup:
    """Construct inline keyboard menu for the main dashboard."""
    keyboard = [
        [
            InlineKeyboardButton("📰 Latest News", callback_data="cmd_news"),
            InlineKeyboardButton("₿ Crypto Prices", callback_data="cmd_crypto")
        ],
        [
            InlineKeyboardButton("💹 Forex Market", callback_data="cmd_forex"),
            InlineKeyboardButton("📈 Market Analysis", callback_data="cmd_analysis")
        ],
        [
            InlineKeyboardButton("🎓 Learn Trading", callback_data="cmd_learn"),
            InlineKeyboardButton("📅 Economic Calendar", callback_data="cmd_calendar")
        ],
        [
            InlineKeyboardButton("💡 Trading Tips", callback_data="cmd_tips"),
            InlineKeyboardButton("⚙️ Settings", callback_data="cmd_settings")
        ],
        [
            InlineKeyboardButton("ℹ️ About", callback_data="cmd_about")
        ]
    ]
    return InlineKeyboardMarkup(keyboard)
