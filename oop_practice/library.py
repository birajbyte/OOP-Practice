# Build two classes: Book (a simple object with data) 
# and Library (a container that holds Book objects and can search them).
class Book:
    def __init__(self,title,author):
        self.title = title
        self.author = author

class Library:
    def __init__(self,name):
        self.name = name
        self.books = []
    
    def add_book(self,book):
        self.books.append(book)

    def list_books(self):
        if not self.books:
            print(f"Add books in {self.name}")
            return
        for book in self.books:
            print(f"{book.author}:{book.title}")

    def find_by_author(self):
        if not self.books:
            print(f"Add books in {self.name}")
            return
        author = input("Enter author name ").lower()
        for book in self.books:
            if book.author.lower() == author:
                print(f"Books of author {book.author}:{book.title}")
book1 = Book("Python Basics", "John")
book2 = Book("OOP Guide", "Alice")
book3 = Book("ML Intro", "Bob")
book4 = Book("Deep Learning", "Alice")  
book5 = Book("Data Science", "John") 

library = Library("City Library")
library.add_book(book1)
library.add_book(book2)
library.add_book(book3)
library.add_book(book4)
library.add_book(book5)
library.list_books()
library.find_by_author()






        

