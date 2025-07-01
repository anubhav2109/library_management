from utils.logger import log
from utils.db import get_connection

def return_book(library, member_id, book_id):
    try:
        member = next((m for m in library.members if m.member_id == member_id), None)
        book = next((b for b in library.books if b.book_id == book_id), None)

        if member and book and book_id in member.borrowed_books:
            member.borrowed_books.remove(book_id)
            borrowed = ",".join(map(str, member.borrowed_books))

            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute("UPDATE books SET is_available = 1 WHERE book_id = ?", (book_id,))
            cursor.execute("UPDATE members SET borrowed_books = ? WHERE member_id = ?",
                           (borrowed, member_id))
            conn.commit()
            conn.close()

            book.is_available = True
            log(f"{member.name} returned '{book.title}'")
        else:
            log("Cannot return. Check if borrowed or wrong IDs.")
    except Exception as e:
        log(f"Error returning book: {e}")
