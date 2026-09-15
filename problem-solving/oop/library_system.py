# 🟠 Problem 03 — Library System
# Create a small library management system using OOP.

# Create a class called Book with:
# title
# author
# is_available

# Then create a class called Library.

# The Library should maintain a collection of books and provide these methods:

# add_book(book)
# display_books()
# borrow_book(title)
# return_book(title)

# Rules
# When borrowing a book:

# If the book exists and is available → borrow it.
# If the book is already borrowed → display an appropriate message.
# If the book doesn't exist → display an appropriate message.

# When returning a book:

# If the book exists → make it available again.
# If it doesn't exist → display an appropriate message.
# Example
# book1 = Book("Clean Code", "Robert C. Martin")
# book2 = Book("Python Crash Course", "Eric Matthes")

# library = Library()

# library.add_book(book1)
# library.add_book(book2)

# library.borrow_book("Clean Code")
# library.display_books()

# library.return_book("Clean Code")
# Expected behavior

# Your program should be able to show something similar to:

# Clean Code - Robert C. Martin - Borrowed
# Python Crash Course - Eric Matthes - Available
# Requirements

# You must make the Library work with Book objects.

# Don't simply store book titles as strings.

class Book:
    def __init__(self, title, author, is_available=True):
        self.title = title
        self.author = author
        self.is_available = is_available


class Library:
    def __init__(self):
        self.books= []

    def add_book(self, book):
        self.books.append(book)

    def display_books(self):
        for book in self.books:
            status = "Available" if book.is_available else "Borrowed"
            print(f"title : {book.title}\nauthor : {book.author}\nstatus : {status}")

    def borrow_book(self, title):
        for book in self.books :
            if book.title == title:
                if book.is_available:
                    book.is_available = False
                    return
                else :
                    print(f"The book '{title}' is already borrowed.")
                    return
        print(f"The book '{title}' does not exist in the library.")

    def return_book(self, title):
        for book in self.books :
            if book.title == title:
                book.is_available = True
                return
        print(f"The book '{title}' does not exist in the library.")

# declare some books and a library
book1 = Book("Clean Code", "Robert C. Martin")
book2 = Book("Python Crash Course", "Eric Matthes")
book3 = Book("old man and the sea", "Ernest Hemingway")
# create a library
library = Library()
# add books to the library
library.add_book(book1)
library.add_book(book2)
library.add_book(book3)
# some testing
library.display_books()
# title : Clean Code
# author : Robert C. Martin
# status : Available
# title : Python Crash Course
# author : Eric Matthes
# status : Available
# title : old man and the sea
# author : Ernest Hemingway
# status : Available
library.borrow_book("Clean Code")
library.borrow_book("Clean Code")
# The book 'Clean Code' is already borrowed.
library.borrow_book("The Pragmatic Programmer")
# The book 'The Pragmatic Programmer' does not exist in the library.
library.return_book("The Pragmatic Programmer")
# The book 'The Pragmatic Programmer' does not exist in the library.
library.display_books()
# title : Clean Code
# author : Robert C. Martin
# status : Borrowed
# title : Python Crash Course
# author : Eric Matthes
# status : Available
# title : old man and the sea
# author : Ernest Hemingway
# status : Available
library.return_book("Clean Code")
library.display_books()
# title : Clean Code
# author : Robert C. Martin
# status : Available
# title : Python Crash Course
# author : Eric Matthes
# status : Available
# title : old man and the sea
# author : Ernest Hemingway
# status : Available
library.borrow_book("old man and the sea")
library.display_books()
# title : Clean Code
# author : Robert C. Martin
# status : Available
# title : Python Crash Course
# author : Eric Matthes
# status : Available
# title : old man and the sea
# author : Ernest Hemingway
# status : Borrowed

