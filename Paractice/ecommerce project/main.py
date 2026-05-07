# import json
# from model import Product, Customer, Admin, CreditCardPayment, PayPalPayment


# # ---------- LOAD PRODUCTS ----------
# def load_products():
#     with open("data.json", "r") as f:
#         data = json.load(f)

#     products = []
#     for p in data["products"]:
#         products.append(Product(p["id"], p["name"], p["price"], p["stock"]))
#     return products


# # ---------- SHOW PRODUCTS ----------
# def show_products(products):
#     print("\n📦 Available Products:")
#     for p in products:
#         print(f"{p.id}. {p.name} - ${p.price} (Stock: {p.stock})")


# # ---------- FIND PRODUCT ----------
# def find_product(products, product_id):
#     for p in products:
#         if p.id == product_id:
#             return p
#     return None


# # ---------- MAIN FLOW ----------
# def main():
#     products = load_products()

#     customer = Customer(1, "John", "john@email.com")
#     customer.login()

#     while True:
#         show_products(products)

#         choice = int(input("\nEnter product ID (0 to checkout): "))

#         if choice == 0:
#             break

#         product = find_product(products, choice)

#         if not product:
#             print("Invalid product ID")
#             continue

#         qty = int(input("Enter quantity: "))
#         customer.add_to_cart(product, qty)

#     # ---------- PAYMENT ----------
#     print("\n💳 Choose Payment Method:")
#     print("1. Credit Card")
#     print("2. PayPal")

#     pay_choice = int(input("Enter choice: "))

#     if pay_choice == 1:
#         payment = CreditCardPayment()
#     else:
#         payment = PayPalPayment()

#     order = customer.place_order(payment)

#     # ---------- OUTPUT ----------
#     print("\n✅ ORDER SUCCESSFUL")
#     print(f"Order ID: {order.order_id}")
#     print(f"Total Price: ${order.total_price}")
#     print(f"Status: {order.status}")

#     customer.logout()


# if __name__ == "__main__":
#     main()
# from model import *
# import json

# # Sample data
# def load_products():
#     with open("data.json", "r") as f:
#         data = json.load(f)

#     products = []
#     for p in data["products"]:
#         products.append(Product(p["id"], p["name"], p["price"], p["stock"]))
#     return products

# # Users
# customer = Customer(1, "Alice", "alice@example.com")
# admin = Admin(2, "Bob", "admin@example.com")


# def show_products(products):
#     print("\nAvailable Products:")
#     for p in products:
#         print(f"ID: {p.id}, Name: {p.name}, Price: {p.price}, Stock: {p.stock}")


# def customer_menu():
#     while True:
#         print("\n--- Customer Menu ---")
#         print("1. View Products")
#         print("2. Add to Cart")
#         print("3. View Cart")
#         print("4. Place Order")
#         print("5. Logout")

#         choice = input("Enter choice: ")

#         if choice == "1":
#             show_products()

#         elif choice == "2":
#             show_products()
#             pid = int(input("Enter product ID: "))
#             qty = int(input("Enter quantity: "))

#             product = next((p for p in products if p.id == pid), None)
#             if product:
#                 customer.add_to_cart(product, qty)
#             else:
#                 print("Product not found!")

#         elif choice == "3":
#             print("\nYour Cart:")
#             for item in customer.cart.items:
#                 print(f"{item[0].name} x {item[1]}")
#             print(f"Total: {customer.cart.calculate_total()}")

#         elif choice == "4":
#             print("Choose Payment Method:")
#             print("1. Credit Card")
#             print("2. PayPal")

#             pay_choice = input("Enter choice: ")

#             if pay_choice == "1":
#                 payment = CreditCardPayment()
#             elif pay_choice == "2":
#                 payment = PayPalPayment()
#             else:
#                 print("Invalid payment method")
#                 continue

#             order = customer.place_order(payment)
#             print(f"Order placed! Order ID: {order.order_id}")

#         elif choice == "5":
#             customer.logout()
#             break

#         else:
#             print("Invalid choice!")


# def admin_menu():
#     while True:
#         print("\n--- Admin Menu ---")
#         print("1. View Products")
#         print("2. Add Product")
#         print("3. Remove Product")
#         print("4. Update Stock")
#         print("5. Logout")

#         choice = input("Enter choice: ")

#         if choice == "1":
#             show_products()

#         elif choice == "2":
#             name = input("Enter product name: ")
#             price = float(input("Enter price: "))
#             stock = int(input("Enter stock: "))
#             pid = len(products) + 1

#             new_product = Product(pid, name, price, stock)
#             admin.add_product(products, new_product)

#         elif choice == "3":
#             pid = int(input("Enter product ID to remove: "))
#             admin.remove_product(products, pid)

#         elif choice == "4":
#             pid = int(input("Enter product ID: "))
#             qty = int(input("Enter new stock: "))

#             product = next((p for p in products if p.id == pid), None)
#             if product:
#                 admin.update_stock(product, qty)
#                 print("Stock updated!")
#             else:
#                 print("Product not found!")

#         elif choice == "5":
#             admin.logout()
#             break

#         else:
#             print("Invalid choice!")


# def main():
#     while True:
#         print("\n=== E-Commerce System ===")
#         print("1. Login as Customer")
#         print("2. Login as Admin")
#         print("3. Exit")

#         choice = input("Enter choice: ")

#         if choice == "1":
#             customer.login()
#             customer_menu()

#         elif choice == "2":
#             admin.login()
#             admin_menu()

#         elif choice == "3":
#             print("Goodbye!")
#             break

#         else:
#             print("Invalid choice!")


# if __name__ == "__main__":
#     main()

import json
from model import *

# -------------------------------
# Load products from data.json
# -------------------------------
def load_products():
    """
    Reads product data from data.json
    and converts it into Product objects
    """
    with open("data.json", "r") as file:
        data = json.load(file)

    product_list = []
    for item in data["products"]:
        product = Product(
            item["id"],
            item["name"],
            item["price"],
            item["stock"]
        )
        product_list.append(product)

    return product_list


# -------------------------------
# Save products back to data.json
# -------------------------------
def save_products(products):
    """
    Converts Product objects back to JSON
    and saves them into data.json
    """
    data = {
        "products": [
            {
                "id": p.id,
                "name": p.name,
                "price": p.price,
                "stock": p.stock
            }
            for p in products
        ]
    }

    with open("data.json", "w") as file:
        json.dump(data, file, indent=4)


# Load products at start
products = load_products()

# Create users
customer = Customer(1, "Alice", "alice@example.com")
admin = Admin(2, "Bob", "admin@example.com")


# -------------------------------
# Display all products
# -------------------------------
def show_products():
    print("\nAvailable Products:")
    for p in products:
        print(f"ID: {p.id}, Name: {p.name}, Price: {p.price}, Stock: {p.stock}")


# -------------------------------
# Customer Menu
# -------------------------------
def customer_menu():
    while True:
        print("\n--- Customer Menu ---")
        print("1. View Products")
        print("2. Add to Cart")
        print("3. View Cart")
        print("4. Place Order")
        print("5. Logout")

        choice = input("Enter choice: ")

        # View products
        if choice == "1":
            show_products()

        # Add item to cart
        elif choice == "2":
            show_products()
            pid = int(input("Enter product ID: "))
            qty = int(input("Enter quantity: "))

            product = next((p for p in products if p.id == pid), None)
            if product:
                customer.add_to_cart(product, qty)
            else:
                print("Product not found!")

        # View cart
        elif choice == "3":
            print("\nYour Cart:")
            for item in customer.cart.items:
                print(f"{item[0].name} x {item[1]}")
            print(f"Total: {customer.cart.calculate_total()}")

        # Place order
        elif choice == "4":
            print("Choose Payment Method:")
            print("1. Credit Card")
            print("2. PayPal")

            pay_choice = input("Enter choice: ")

            if pay_choice == "1":
                payment = CreditCardPayment()
            elif pay_choice == "2":
                payment = PayPalPayment()
            else:
                print("Invalid payment method")
                continue

            order = customer.place_order(payment)
            print(f"Order placed! Order ID: {order.order_id}")

            # Save updated stock after order
            save_products(products)

        # Logout
        elif choice == "5":
            customer.logout()
            break

        else:
            print("Invalid choice!")


# -------------------------------
# Admin Menu
# -------------------------------
def admin_menu():
    while True:
        print("\n--- Admin Menu ---")
        print("1. View Products")
        print("2. Add Product")
        print("3. Remove Product")
        print("4. Update Stock")
        print("5. Logout")

        choice = input("Enter choice: ")

        # View products
        if choice == "1":
            show_products()

        # Add new product
        elif choice == "2":
            name = input("Enter product name: ")
            price = float(input("Enter price: "))
            stock = int(input("Enter stock: "))

            pid = max([p.id for p in products], default=0) + 1
            new_product = Product(pid, name, price, stock)

            admin.add_product(products, new_product)
            save_products(products)  # persist change

        # Remove product
        elif choice == "3":
            pid = int(input("Enter product ID to remove: "))
            admin.remove_product(products, pid)
            save_products(products)

        # Update stock
        elif choice == "4":
            pid = int(input("Enter product ID: "))
            qty = int(input("Enter new stock: "))

            product = next((p for p in products if p.id == pid), None)
            if product:
                admin.update_stock(product, qty)
                print("Stock updated!")
                save_products(products)
            else:
                print("Product not found!")

        # Logout
        elif choice == "5":
            admin.logout()
            break

        else:
            print("Invalid choice!")


# -------------------------------
# Main Menu (Entry Point)
# -------------------------------
def main():
    while True:
        print("\n=== E-Commerce System ===")
        print("1. Login as Customer")
        print("2. Login as Admin")
        print("3. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            customer.login()
            customer_menu()

        elif choice == "2":
            admin.login()
            admin_menu()

        elif choice == "3":
            print("Goodbye!")
            break

        else:
            print("Invalid choice!")


# Run program
if __name__ == "__main__":
    main()