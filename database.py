import sqlite3
from datetime import datetime
from pathlib import Path


DATABASE_PATH = Path("data/cipher_lab.db")


def initialize_database():
    DATABASE_PATH.parent.mkdir(exist_ok=True)

    connection = sqlite3.connect(DATABASE_PATH)

    connection.execute("""
        CREATE TABLE IF NOT EXISTS operations (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT NOT NULL,
            operation TEXT NOT NULL,
            message TEXT NOT NULL,
            key_value INTEGER NOT NULL,
            result TEXT NOT NULL
        )
    """)

    connection.commit()
    connection.close()


def log_operation(operation, message, key, result):
    connection = sqlite3.connect(DATABASE_PATH)

    connection.execute(
        """
        INSERT INTO operations
        (timestamp, operation, message, key_value, result)
        VALUES (?, ?, ?, ?, ?)
        """,
        (
            datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            operation,
            message,
            key,
            result,
        ),
    )

    connection.commit()
    connection.close()


def get_history():
    connection = sqlite3.connect(DATABASE_PATH)

    cursor = connection.execute("""
        SELECT timestamp, operation, key_value, message, result
        FROM operations
        ORDER BY id DESC
        LIMIT 50
    """)

    rows = cursor.fetchall()
    connection.close()

    return rows


def clear_history():
    connection = sqlite3.connect(DATABASE_PATH)

    connection.execute("DELETE FROM operations")

    connection.commit()
    connection.close()