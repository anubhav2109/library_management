from utils.logger import log
from utils.db import get_connection

def borrow_book(library, member_id, book_id):
    try:
        member = next((m for m in library.members if m.member_id == member_id), None)
        book = next((b for b in library.books if b.book_id == book_id), None)

        if member and book and book.is_available:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute("UPDATE books SET is_available = 0 WHERE book_id = ?", (book_id,))
            borrowed = ",".join(map(str, member.borrowed_books + [book_id]))
            cursor.execute("UPDATE members SET borrowed_books = ? WHERE member_id = ?",
                           (borrowed, member_id))
            conn.commit()
            conn.close()

            member.borrowed_books.append(book_id)
            book.is_available = False
            log(f"{member.name} borrowed '{book.title}'")
        else:
            log("Cannot borrow. Either not available or invalid IDs.")
    except Exception as e:
        log(f"Error borrowing book: {e}")
