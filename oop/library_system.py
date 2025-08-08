# Deepen your understanding of inheritance 
# and composition in Python by creating a system 
# that models a library with different types of books.

class Book:
    books = []

    def __init__(self, title, author, file_size):
        self.title = title
        self.author = author
        self.file_size = file_size

class EBook(Book):
    def __init_subclass__(cls):
        return super().file_size()


class PrintBook(Book):
    def __str__(self, page_count):
        self.page_count = page_count

class Library(Book, EBook, PrintBook):
    def __init__(self, title, author):
        pass

    def add_book(self, book):
        self.books.append(book)

    def list_books(self):
        return f"PrintBook: {self.title} {self.author}, Page Count: {self.page_count}"