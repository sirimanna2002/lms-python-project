# library_ui.py
from library import Library


def display_menu():
    print("\nLibrary Management System")
    print("1. Add Book")
    print("2. Display Books")
    print("3. Search Book")
    print("4. Borrow Book")
    print("5. Return Book")
    print("6. Exit")


class LibraryUI:
    def __init__(self):
        self.library = Library()

    def run(self):
        while True:
            display_menu()
            choice = input("Choose an option: ")
            if choice == '1':
                title = input("Enter the book title: ")
                author = input("Enter the author: ")
                self.library.add_book(title, author)
            elif choice == '2':
                self.library.display_books()
            elif choice == '3':
                search_term = input("Enter the title or author to search: ")
                self.library.search_book(search_term)
            elif choice == '4':
                title = input("Enter the title of the book to borrow: ")
                self.library.borrow_book(title)
            elif choice == '5':
                title = input("Enter the title of the book to return: ")
                self.library.return_book(title)
            elif choice == '6':
                print("Exiting the Library System. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")

# Run the Library System
if __name__ == "__main__":
    ui = LibraryUI()
    ui.run()