from models.library import Library

def main():
    library = Library()

    while True:
        print("\n--- Library System Menu ---")
        print("1. Add Book")
        print("2. Register Member")
        print("3. Borrow Book")
        print("4. Return Book")
        print("5. List Books")
        print("6. List Members")
        print("7. Exit")
        
        choice = input("Choose option: ")
        
        if choice == "1":
            title = input("Enter book title: ")
            author = input("Enter author name: ")
            library.add_book(title, author)
        elif choice == "2":
            name = input("Enter member name: ")
            library.register_member(name)
        elif choice == "3":
            member_id = int(input("Enter member ID: "))
            book_id = int(input("Enter book ID: "))
            library.borrow_book(member_id, book_id)
        elif choice == "4":
            member_id = int(input("Enter member ID: "))
            book_id = int(input("Enter book ID: "))
            library.return_book(member_id, book_id)
        elif choice == "5":
            library.list_books()
        elif choice == "6":
            library.list_members()
        elif choice == "7":
            print("Exiting...")
            break
        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main()
