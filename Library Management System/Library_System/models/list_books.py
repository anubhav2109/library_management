def list_books(library):
    try:
        for book in library.books:
            status = "Available" if book.is_available else "Borrowed"
            print(f"[{book.book_id}] {book.title} by {book.author} - {status}")
    except Exception as e:
        from utils.logger import log
        log(f"Error listing books: {e}")
