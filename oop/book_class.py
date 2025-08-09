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
        print(f"{self.title} by {self.author}, published in {self.year}")
    
    def __repr__(self):
        print(f"Book('{self.title}', '{self.author}', {self.year})")

    def __del__(self):
        self.book.remove(self.title)
        print(f"Deleting {self.title}")
        