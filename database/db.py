import sqlite3
from pathlib import Path

DB_PATH = Path("db") / "slot.db"

def create_database():
    DB_PATH.parent.mkdir(exist_ok=True)

    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS machine_data (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        date TEXT,
        machine TEXT,
        number INTEGER,
        games INTEGER,
        bb INTEGER,
        rb INTEGER,
        diff INTEGER
    )
    """)

    conn.commit()
    conn.close()

    print("データベース作成完了")


