def fetch_economic_calendar() -> str:
    """Return overview of key recurring macroeconomic events."""
    return (
        "<b>📅 Upcoming Major Economic Calendar Events</b>\n\n"
        "• <b>US Non-Farm Payrolls (NFP):</b> First Friday of every month\n"
        "• <b>FOMC Interest Rate Announcement:</b> Scheduled periodic releases\n"
        "• <b>US Consumer Price Index (CPI):</b> Monthly inflation indicator\n"
        "• <b>ECB Monetary Policy Statement:</b> Scheduled policy decisions\n\n"
        "<i>💡 High-impact news drives substantial volatility. Always apply risk parameters!</i>"
    )
