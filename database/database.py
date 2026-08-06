import os
import sqlite3
import logging
from config import DB_PATH

logger = logging.getLogger(__name__)

def get_connection():
    """Create and return a database connection, creating parent directory if needed."""
    os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)
    return sqlite3.connect(DB_PATH)

def init_db():
    """Initialize SQLite tables for user management."""
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                telegram_id INTEGER PRIMARY KEY,
                username TEXT,
                first_name TEXT,
                subscribed INTEGER DEFAULT 1,
                notification_pref TEXT DEFAULT 'daily',
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        conn.commit()
    logger.info("Database initialized successfully at %s", DB_PATH)

def add_or_update_user(telegram_id: int, username: str, first_name: str):
    """Register user or update details on interaction."""
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO users (telegram_id, username, first_name)
            VALUES (?, ?, ?)
            ON CONFLICT(telegram_id) DO UPDATE SET
                username = excluded.username,
                first_name = excluded.first_name
        """, (telegram_id, username, first_name))
        conn.commit()

def set_subscription(telegram_id: int, status: bool):
    """Update user notification subscription preference."""
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("""
            UPDATE users SET subscribed = ? WHERE telegram_id = ?
        """, (1 if status else 0, telegram_id))
        conn.commit()

def get_subscribed_users() -> list[int]:
    """Retrieve all user IDs with an active subscription status."""
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT telegram_id FROM users WHERE subscribed = 1")
        return [row[0] for row in cursor.fetchall()]

def get_stats() -> tuple[int, int]:
    """Retrieve total user count and active subscriber count."""
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT COUNT(*) FROM users")
        total = cursor.fetchone()[0]
        cursor.execute("SELECT COUNT(*) FROM users WHERE subscribed = 1")
        active = cursor.fetchone()[0]
        return total, active
