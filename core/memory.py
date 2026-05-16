import sqlite3
import os

DB_PATH = r"E:\\Helix\\memory\\helix_memory.db"


class Memory:

    def __init__(self):
        self.conn = sqlite3.connect(DB_PATH, check_same_thread=False)
        self.cursor = self.conn.cursor()

        self.setup()

    def setup(self):
        self.cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS conversations (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                role TEXT,
                content TEXT
            )
            """
        )

        self.conn.commit()

    def save_message(self, role, content):
        self.cursor.execute(
            "INSERT INTO conversations (role, content) VALUES (?, ?)",
            (role, content)
        )

        self.conn.commit()

    def get_recent(self, limit=10):
        self.cursor.execute(
            "SELECT role, content FROM conversations ORDER BY id DESC LIMIT ?",
            (limit,)
        )

        return self.cursor.fetchall()  