# Solidify understanding of basic OOP concepts in 
# Python by implementing a system that tracks books in a library, 
# focusing on classes, object 
# instantiation, and method invocation.


class Book:
    def __init__(self, title, author, _is_checked_out):
        self.title = title
        self.author = author
        self.___is_checked_out = _is_checked_out

    def add_book(self):
        pass

    def return_book(self):
        self.return_book = True



class Library(Book):
    def __init__(self):
        self._books = []

    def add_book(self, title, author):
        self.title = title
        self.author = author

    def check_out_book(self, title):
        self.title = title

    def return_book(self, title):
        self.title = title

    def list_available_books(self):
        pass
