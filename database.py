

import sqlite3
from pathlib import Path

# Default database location
DB_PATH = Path(__file__).parent / "database" / "training.db"
DB_PATH.parent.mkdir(parents=True, exist_ok=True)


# CREATE TABLE
def create_table(db_path=None):
    path = db_path or DB_PATH

    with sqlite3.connect(path) as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS messages (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                message TEXT NOT NULL,
                created_at TEXT DEFAULT CURRENT_TIMESTAMP
            )
        """)
    print("Messages table is ready!")


# CREATE - Insert a message
def add_message(name, message, db_path=None):
    path = db_path or DB_PATH

    with sqlite3.connect(path) as conn:
        cursor = conn.execute(
            "INSERT INTO messages (name, message) VALUES (?, ?)",
            (name, message)
        )
    return cursor.lastrowid


# READ - Retrieve all messages
def get_messages(db_path=None):
    path = db_path or DB_PATH

    with sqlite3.connect(path) as conn:
        conn.row_factory = sqlite3.Row
        rows = conn.execute(
            "SELECT * FROM messages ORDER BY id"
        ).fetchall()
        return [dict(row) for row in rows]


# UPDATE - Modify a message
def update_message(message_id, new_message, db_path=None):
    path = db_path or DB_PATH

    with sqlite3.connect(path) as conn:
        cursor = conn.execute(
            "UPDATE messages SET message = ? WHERE id = ?",
            (new_message, message_id)
        )
    return cursor.rowcount


# DELETE - Remove a message
def delete_message(message_id, db_path=None):
    path = db_path or DB_PATH

    with sqlite3.connect(path) as conn:
        cursor = conn.execute(
            "DELETE FROM messages WHERE id = ?",
            (message_id,)
        )
    return cursor.rowcount


if __name__ == "__main__":
    create_table()
