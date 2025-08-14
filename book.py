# book.py

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = True

    def __str__(self):
        status = "Available" if self.available else "Borrowed"
        return f"{self.title} by {self.author} - {status}"