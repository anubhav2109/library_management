from models.library import Library
from models.add_book import add_book
from models.register_member import register_member
from models.borrow_book import borrow_book
from models.return_book import return_book
from models.list_books import list_books
from models.list_members import list_members

from models.load_books import load_books
from models.load_members import load_members
from utils.db import setup_database

def main():
    setup_database()

    library = Library()
    load_books(library)
    load_members(library)

    while True:
        print("\n--- Library System Menu ---")
        print("1. Add Book")
        print("2. Register Member")
        print("3. Borrow Book")
        print("4. Return Book")
        print("5. List Books")
        print("6. List Members")
        print("7. Exit")
        
        choice = input("Choose Option: ")
        
        if choice == "1":
            title = input("Enter Book Title: ")
            author = input("Enter Author Name: ")
            add_book(library, title, author)
        elif choice == "2":
            name = input("Enter Member Name: ")
            register_member(library, name)
        elif choice == "3":
            member_id = int(input("Enter Member ID: "))
            book_id = int(input("Enter Book ID: "))
            borrow_book(library, member_id, book_id)
        elif choice == "4":
            member_id = int(input("Enter Member ID: "))
            book_id = int(input("Enter Book ID: "))
            return_book(library, member_id, book_id)
        elif choice == "5":
            list_books(library)
        elif choice == "6":
            list_members(library)
        elif choice == "7":
            print("Exiting...")
            break
        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main()
