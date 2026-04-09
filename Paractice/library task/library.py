from abc import ABC, abstractmethod
import csv
class LibraryItem(ABC):
    def __init__(self, item_id, title, is_borrowed=False):
        self.__item_id = item_id
        self.title = title 
        self.is_borrowed = is_borrowed

    def get_item_id(self):
        return self.__item_id

    def borrow_item(self):
        if self.is_borrowed == False:
            print("Here you go!")
            self.is_borrowed = True
        else:
            print("Sorry, This book is not available.")
            
            
    def return_item(self):
        print("Thanks for returning the book")
        self.is_borrowed = False

    @abstractmethod
    def display_info(self):
        pass

class PrintedBook(LibraryItem):
    def __init__(self, item_id, title, author, pages):
        super().__init__(item_id, title)
        self.author = author
        self.pages = int(pages)
    
    def display_info(self):
        print(f"Printed Book: {self.title}")
        print(f"Author: {self.author}")
        print(f"Pages: {self.pages}")

class EBook(LibraryItem):
    def __init__(self, item_id, title, author, file_size):
        super().__init__(item_id, title)
        self.author = author
        self.file_size = file_size
    
    def display_info(self):
        print(f"EBook: {self.title}")
        print(f"Author: {self.author}")
        print(f"Size: {self.file_size}")

class AudioBook(LibraryItem):
    def __init__(self, item_id, title, narrator, duration):
        super().__init__(item_id, title)
        self.narrator = narrator
        self.duration = duration
    
    def display_info(self):
        print(f"AudioBook: {self.title}")
        print(f"Narrator: {self.narrator}")
        print(f"Duration: {self.duration}")


class Library:
    def __init__(self):
        self.items = []
    
    def add_item(self, item):
        self.items.append(item)
        print("Item added sucessfully")

    def list_items(self):
        for item in self.items:
            item.display_info()

    def find_item(self,item_id):
        for item in self.items:
            if item.get_item_id() == item_id:
                return item
        return None
    
    def borrow_item(self, item_id):
        item = self.find_item(item_id)
        if item:
            item.borrow_item()
        else:
            print("Item not found")

    def return_item(self, item_id):
        item = self.find_item(item_id)
        if not item:
            print("Thanks for returning")
            self.items.append(item)
        else:
            print("This item was not borrowed")
        
    def save_to_file(self):
        with open("books.csv", "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["type","id","title","borrowed","extra1","extra2"])
            for item in self.items:
                if isinstance(item, PrintedBook):
                    writer.writerow(["PrintedBook", item.get_item_id(), item.title, item.is_borrowed, item.author, item.pages])
                elif isinstance(item, EBook):
                    writer.writerow(["EBook", item.get_item_id(), item.title, item.is_borrowed, item.author, item.file_size])
                elif isinstance(item, AudioBook):
                    writer.writerow(["AudioBook", item.get_item_id(), item.title, item.is_borrowed, item.narrator, item.duration])
        print("Data saved successfully.")
    def load_from_file(self):
        self.items.clear()
        with open("books.csv", "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                item_type = row["type"]
                id = row["id"]
                title = row["title"]
                borrowed = row["borrowed"] == "True"
                extra1 = row["extra1"]
                extra2 = row["extra2"]
                if item_type == "PrintedBook":
                    item = PrintedBook(id, title, extra1, extra2)
                elif item_type == "EBook":
                    item = EBook(id, title, extra1, extra2)
                elif item_type == "AudioBook":
                    item = AudioBook(id, title, extra1, extra2)
                item._is_borrowed = borrowed
                self.items.append(item)





    


    
            






# 🧱 Step 1: Abstract Base Class

# Create abstract class:

# LibraryItem
# Attributes
# __item_id        (private)
# title
# is_borrowed
# Methods
# get_item_id()
# borrow_item()
# return_item()
# display_info()   (abstract method)

# This forces subclasses to implement their own display.

# 🧬 Step 2: Subclasses (Inheritance)
# 📚 PrintedBook

# Extra attributes:

# author
# pages

# Example display:

# Printed Book: Python Basics
# Author: John Smith
# Pages: 350
# 💻 EBook

# Extra attributes:

# author
# file_size

# Example display:

# EBook: Machine Learning Guide
# Author: Andrew Ng
# Size: 5MB
# 🎧 AudioBook

# Extra attributes:

# narrator
# duration

# Example display:

# AudioBook: Atomic Habits
# Narrator: James Clear
# Duration: 6 hours
# 🏢 Step 3: Library Class

# Create class:

# Library

# Attribute:

# items = []

# Methods:

# add_item(item)
# list_items()
# borrow_item(item_id)
# return_item(item_id)
# find_item(item_id)
# save_to_file()
# load_from_file()
# 💾 Step 4: Serialization (Save to CSV)

# File:

# books.csv

# Columns:

# type,id,title,borrowed,extra1,extra2

# Example:

# PrintedBook,101,Python Basics,False,John Smith,350
# EBook,102,AI Guide,False,Andrew Ng,5MB
# AudioBook,103,Atomic Habits,True,James Clear,6 hours

# Use:

# csv.writer
# 📥 Step 5: Deserialization (Load from CSV)

# Use:

# csv.DictReader

# Recreate objects:

# if type == "PrintedBook":
#     item = PrintedBook(...)

# elif type == "EBook":
#     item = EBook(...)

# elif type == "AudioBook":
#     item = AudioBook(...)

# Use isinstance() when saving.