import os
import sys
from dotenv import load_dotenv

# Load local environment variables from .env file (if present)
load_dotenv()

def get_required_env(var_name: str) -> str:
    """Retrieve an environment variable or crash immediately if missing."""
    val = os.getenv(var_name)
    if not val or not val.strip():
        print(f"CRITICAL ERROR: Environment variable '{var_name}' is missing.")
        print("Please configure it in your .env file or Railway runtime settings.")
        sys.exit(1)
    return val.strip()

# Zero-Fallback Security Injection
BOT_TOKEN = get_required_env("BOT_TOKEN")

try:
    ADMIN_ID = int(get_required_env("ADMIN_ID"))
except ValueError:
    print("CRITICAL ERROR: ADMIN_ID environment variable must be a valid integer.")
    sys.exit(1)

# Optional APIs & Public Endpoints
NEWS_API_KEY = os.getenv("NEWS_API_KEY", "").strip()
FOREX_API_KEY = os.getenv("FOREX_API_KEY", "").strip()
COINGECKO_API = os.getenv("COINGECKO_API", "https://api.coingecko.com/api/v3").strip()

# Directory Paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "database", "users.db")
LOG_FILE = os.path.join(BASE_DIR, "bot.log")
