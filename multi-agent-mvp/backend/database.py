import sqlite3

def init_db():
    conn = sqlite3.connect("backend.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            status TEXT
        )
    """)
    conn.commit()
    conn.close()
