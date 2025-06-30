from models.book import Book
from models.member import Member
from utils.logger import log

class Library:
    def __init__(self):
        self.books = []
        self.members = []

    def add_book(self, title, author):
        book_id = len(self.books) + 1
        book = Book(book_id, title, author)
        self.books.append(book)
        log(f"Added book: {title} by {author}")

    def register_member(self, name):
        member_id = len(self.members) + 1
        member = Member(member_id, name)
        self.members.append(member)
        log(f"Registered member: {name}")

    def borrow_book(self, member_id, book_id):
        member = self.get_member_by_id(member_id)
        book = self.get_book_by_id(book_id)
        if member and book and book.is_available:
            member.borrowed_books.append(book.book_id)
            book.is_available = False
            log(f"{member.name} borrowed '{book.title}'")
        else:
            log("Cannot borrow book. Either not available or member not found.")

    def return_book(self, member_id, book_id):
        member = self.get_member_by_id(member_id)
        book = self.get_book_by_id(book_id)
        if member and book and book_id in member.borrowed_books:
            member.borrowed_books.remove(book_id)
            book.is_available = True
            log(f"{member.name} returned '{book.title}'")
        else:
            log("Cannot return book. Check if it was borrowed.")

    def get_book_by_id(self, book_id):
        return next((b for b in self.books if b.book_id == book_id), None)

    def get_member_by_id(self, member_id):
        return next((m for m in self.members if m.member_id == member_id), None)

    def list_books(self):
        for book in self.books:
            status = "Available" if book.is_available else "Borrowed"
            print(f"[{book.book_id}] {book.title} by {book.author} - {status}")

    def list_members(self):
        for member in self.members:
            print(f"[{member.member_id}] {member.name} - Borrowed: {member.borrowed_books}")
