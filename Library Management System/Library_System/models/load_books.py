from models.book import Book
from utils.db import get_connection

def load_books(library):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT book_id, title, author, is_available FROM books")
    rows = cursor.fetchall()
    for book_id, title, author, is_available in rows:
        book = Book(book_id, title, author)
        book.is_available = bool(is_available)
        library.books.append(book)
    conn.close()
