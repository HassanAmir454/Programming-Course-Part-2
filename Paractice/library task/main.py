# main.py
from library import Library, PrintedBook, EBook, AudioBook

def main():
    library = Library()

    while True:
        print("\n--- Smart Library System ---")
        print("1 - Add Item")
        print("2 - List All Items")
        print("3 - Borrow Item")
        print("4 - Return Item")
        print("5 - Save Library")
        print("6 - Load Library")
        print("0 - Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            item_type = input("Item type (PrintedBook/EBook/AudioBook): ")
            item_id = input("Enter item ID: ")
            title = input("Enter title: ")

            if item_type == "PrintedBook":
                author = input("Enter author: ")
                pages = input("Enter number of pages: ")
                item = PrintedBook(item_id, title, author, pages)
            elif item_type == "EBook":
                author = input("Enter author: ")
                size = input("Enter file size (MB): ")
                item = EBook(item_id, title, author, size)
            elif item_type == "AudioBook":
                narrator = input("Enter narrator: ")
                duration = input("Enter duration (minutes): ")
                item = AudioBook(item_id, title, narrator, duration)
            else:
                print("Invalid item type!")
                continue

            library.add_item(item)

        elif choice == "2":
            library.list_items()

        elif choice == "3":
            item_id = input("Enter item ID to borrow: ")
            library.borrow_item(item_id)

        elif choice == "4":
            item_id = input("Enter item ID to return: ")
            library.return_item(item_id)

        elif choice == "5":
            library.save_to_file()

        elif choice == "6":
            library.load_from_file()

        elif choice == "0":
            print("Exiting Smart Library. Goodbye!")
            break

        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()