# library.py
import os
from book import Book
import csv


class Library:
    _instance = None  # Singleton instance
    CSV_PATH = r'C:\Users\DELL\OneDrive\Desktop\Library Management System\List_of_Books.csv'

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Library, cls).__new__(cls)
            cls._instance.books = []
            # Import books from csv when creating the instance
            cls._instance.import_books_from_csv(cls.CSV_PATH)
        return cls._instance
    
    def import_books_from_csv(self, filename):
        try:
            if not os.path.exists(filename):
                print(f"Warning: File not found at {filename}")
                return
                
            with open(filename, 'r', encoding='ANSI') as file:
                csv_reader = csv.DictReader(file)
                imported_count = 0
                for row in csv_reader:
                    # Skip if title or author is missing
                    if 'Book-Title' in row and 'Book-Author' in row:
                        title = row['Book-Title'].strip()
                        author = row['Book-Author'].strip()
                        # Check if book already exists
                        if not any(book.title.lower() == title.lower() for book in self.books):
                            new_book = Book(title, author)
                            self.books.append(new_book)
                            imported_count += 1
                print(f"Successfully imported {imported_count} books from the library database")
        except Exception as e:
            print(f"Error importing books: {str(e)}")
            print("Please check if the CSV file path is correct and the file is not corrupted")

    def display_books(self):
        if not self.books:
            print("No books in the library.")
            print("Please check if the CSV file path is correct: ")
            print(self.CSV_PATH)
        else:
            print("\n" + "="*80)
            print("                               Library Collection")
            print("="*80)
            print(f"{'No.':<5}{'Title':<40}{'Author':<25}{'Status':<10}")
            print("-"*80)
            for index, book in enumerate(self.books, start=1):
                status = "Available" if book.available else "Borrowed"
                # Truncate long titles and authors
                title = book.title[:37] + "..." if len(book.title) > 37 else book.title
                author = book.author[:22] + "..." if len(book.author) > 22 else book.author
                print(f"{index:<5}{title:<40}{author:<25}{status:<10}")
            print("="*80)
            print(f"Total Books: {len(self.books)}")

    def add_book(self, title, author):
        # Check if book already exists
        if any(book.title.lower() == title.lower() for book in self.books):
            print(f"Book '{title}' already exists in the library!")
            return

        # Add the book to the in-memory list
        new_book = Book(title, author)
        self.books.append(new_book)

        # Append the new book to the CSV file
        try:
            row_number = 1  # Start row number at 1
            if os.path.exists(self.CSV_PATH):
                with open(self.CSV_PATH, 'r', encoding='ANSI') as file:  # Use ANSI for ANSI files
                    csv_reader = csv.reader(file)
                    # Skip the header if it exists and count rows
                    row_count = sum(1 for _ in csv_reader)  # Count all rows
                    row_number = row_count + 1  # Next row number

            with open(self.CSV_PATH, 'a', newline='', encoding='ANSI') as file:  # Use ANSI for ANSI files
                csv_writer = csv.writer(file)
                # Write the new book data as a row
                csv_writer.writerow([row_number,title, author,])
            print(f"Book '{title}' added successfully and saved to the CSV file!")
        except Exception as e:
            print(f"Error saving book to CSV: {str(e)}")


    def search_book(self, search_term):
        search_term = search_term.lower()
        found_books = [book for book in self.books if search_term in book.title.lower() or search_term in book.author.lower()]
        if found_books:
            print("\nSearch Results:")
            for index, book in enumerate(found_books, start=1):
                print(f"{index}. {book}")
        else:
            print("No books found matching your search criteria.")

    def borrow_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                if book.available:
                    book.available = False
                    print(f"You have successfully borrowed '{book.title}'.")
                    return
                else:
                    print(f"Sorry, '{book.title}' is currently borrowed.")
                    return
        print("Book not found in the library.")

    def return_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                if not book.available:
                    book.available = True
                    print(f"Thank you for returning '{book.title}'.")
                    return
                else:
                    print(f"'{book.title}' is already marked as available.")
                    return
        print("Book not found in the library.")

