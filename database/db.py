import sqlite3
from pathlib import Path

DB_PATH = Path("db") / "slot.db"


def get_connection():
    DB_PATH.parent.mkdir(exist_ok=True)
    return sqlite3.connect(DB_PATH)


def create_database():
    conn = get_connection()
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

    cur.execute("""
    CREATE TABLE IF NOT EXISTS report_links (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        date_text TEXT NOT NULL,
        url TEXT NOT NULL UNIQUE,
        scraped INTEGER NOT NULL DEFAULT 0,
        created_at TEXT DEFAULT CURRENT_TIMESTAMP
    )
    """)

    conn.commit()
    conn.close()

    print("データベース作成完了")


def save_report_links(report_links):
    conn = get_connection()
    cur = conn.cursor()

    saved_count = 0

    for report in report_links:
        cur.execute("""
        INSERT OR IGNORE INTO report_links (date_text, url)
        VALUES (?, ?)
        """, (report.date_text, report.url))

        if cur.rowcount == 1:
            saved_count += 1

    conn.commit()
    conn.close()

    return saved_count


def count_report_links():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT COUNT(*) FROM report_links")
    count = cur.fetchone()[0]

    conn.close()
    return count


