# library_system.py

class Book:
    def __init__(self, title, author):
        """Initialize common book attributes"""
        self.title = title
        self.author = author

    def __str__(self):
        return f"Book: {self.title} by {self.author}"


class EBook(Book):
    def __init__(self, title, author, file_size):
        """Initialize EBook with title, author, and file size"""
        super().__init__(title, author)  # Call the base class constructor
        self.file_size = file_size

    def __str__(self):
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB"


class PrintBook(Book):
    def __init__(self, title, author, page_count):
        """Initialize PrintBook with title, author, and page count"""
        super().__init__(title, author)  # Call the base class constructor
        self.page_count = page_count

    def __str__(self):
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"


class Library:
    def __init__(self):
        """Initialize an empty list of books"""
        self.books = []

    def add_book(self, book):
        """Add a Book, EBook, or PrintBook to the library"""
        if isinstance(book, Book):
            self.books.append(book)
        else:
            print("Only instances of Book or its subclasses can be added.")

    def list_books(self):
        """Print details of all books in the library"""
        for book in self.books:
            print(book)
