from models.book import Book
from utils.logger import log
from utils.db import get_connection

def add_book(library, title, author):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO books (title, author, is_available) VALUES (?, ?, 1)",
                       (title, author))
        conn.commit()
        book_id = cursor.lastrowid
        conn.close()

        book = Book(book_id, title, author)
        library.books.append(book)
        log(f"Added book: {title} by {author}")
    except Exception as e:
        log(f"Error adding book: {e}")
