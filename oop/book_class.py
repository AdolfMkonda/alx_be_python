# Master Python magic methods by implementing a 
# Book class that incorporates constructors (__init__), 
# destructors (__del__), and 
# the representation methods (__str__ and __repr__).

class Book:
    book = []
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
        self.book = self.book.append(title)
    
    def __str__(self):
        return f"{self.title} by {self.author}, published in {self.year}"
    
    def __repr__(self):
        return f"Book('{self.title}', '{self.author}', {self.year})"

    def __del__(self):
        self.book.remove(self.title)
        return f"Deleting {self.title}"
        