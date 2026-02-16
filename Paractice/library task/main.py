from library import Book, PrintedBook, EBook, display_info_all

def main():
    books = []

    while True:
        print("\n===== Library Menu =====")
        print("1) Add Printed Book")
        print("2) Add EBook")
        print("3) Display All Books")
        print("4) Calculate Rent")
        print("0) Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            book_id = int(input("Enter book id: "))
            title = input("Enter title: ")
            price = float(input("Enter price: "))
            books.append(PrintedBook(book_id, title, price))
            print("Printed Book added")

        elif choice == "2":
            book_id = int(input("Enter book id: "))
            title = input("Enter title: ")
            price = float(input("Enter price: "))
            books.append(EBook(book_id, title, price))
            print("EBook added")

        elif choice == "3":
            if not books:
                print("No books available")
            for book in books:
                book.display_info()
                book.book_type()

        elif choice == "4":
            book_id = int(input("Enter book id: "))
            days = int(input("Enter number of days: "))
            found = False

            for book in books:
                if book.get_id() == book_id:
                    book.calculate_rent(days)
                    found = True
                    break

            if not found:
                print("Book not found")

        elif choice == "0":
            print("Exiting program")
            break

        else:
            print("Invalid choice")

main()
