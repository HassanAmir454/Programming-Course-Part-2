from abc import ABC, abstractmethod
class Book(ABC):
    def __init__(self, book_id, title, price):
        self._book_id = book_id
        self._title = title
        self._price = price

    def get_price(self):
        return self._price
    
    def get_id(self):
        return self._book_id
    
    def display_info(self):
        print(f"The price of book '{self._title}' have id {self._book_id} is {self._price} ")

    @abstractmethod
    def calculate_rent(self, days):
        pass
    
    @abstractmethod
    def book_type(self):
        pass

class PrintedBook(Book):
    def calculate_rent(self, days):
        
        rent = self._price * 0.02 *days
        if days > 7:
            print(f"The rent for printed book for {days} days is {rent+50}")
        else:
            print(f"The rent for printed book for {days} days is {rent}")

    def book_type(self):
        print("Book type is 'Printed book'.")

class EBook(Book):
    def calculate_rent(self, days):
        
        rent = self._price * 0.01 *days
        if days < 30:
            print(f"The rent for Ebook for {days} days is {rent}")
        else:
            print(f"You cannot take on rent for more than 30 days")

    def book_type(self):
        print("Book type is 'Ebook'.")

def display_info_all(bookss):
    if bookss =="":
        return
    for book in bookss:
        print("book", "\n")




    
    






# Create an abstract class Book.

# Attributes

# _book_id (protected)

# _title (protected)

# _price (protected)


# Concrete Methods

# get_price()

# display_info() → prints ID, title, price

# Abstract Methods (must be implemented by child classes)

# calculate_rent(days)

# book_type()

# 🔹 STEP 2 — Child Class 1: PrintedBook (Inheritance)

# Rules:

# Rent = days * 10

# Extra rule: If days > 7 → add late fee = 50

# Must:

# Inherit Book

# Implement all abstract methods

# Use _price, not private variables

# 🔹 STEP 3 — Child Class 2: EBook (Inheritance)

# Rules:

# Rent = days * 5

# No late fee

# Cannot be rented for more than 30 days

# Must:

# Inherit Book

# Implement all abstract methods

# 🔹 STEP 4 — Encapsulation Rules

# No direct access like book._price from main.py

# All actions must be done using methods

# _price is protected → usable in child classes only