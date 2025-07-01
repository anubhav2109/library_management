import sqlite3

def get_connection():
    return sqlite3.connect("library.db")

def setup_database():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS books (
            book_id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            author TEXT,
            is_available INTEGER
        )
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS members (
            member_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            borrowed_books TEXT
        )
    """)
    conn.commit()
    conn.close()
