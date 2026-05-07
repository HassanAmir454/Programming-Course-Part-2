from abc import ABC, abstractmethod

class User:
    def __init__(self, id, name, email, logged_in = False):
        self.id = id
        self.name = name
        self.email = email
        self.logged_in = logged_in
        
    
    def login(self):
        if not self.logged_in:
            self.logged_in = True
            print("Sucessfully Logged in!")
            

        else:
            print("login failed!")

        
    def logout(self):
        if self.logged_in:
            self.logged_in = False
            print("Logging out!")
            
        else:
            print("You are already logged out!")

class Customer(User):
    def __init__(self, id, name, email):
        super().__init__(id, name, email)
        self.cart = Cart()
        self.order_history = []

    def add_to_cart(self, product, quantity):
        if product.is_available(quantity):
            self.cart.add_item(product, quantity)
            print(f"Dear customer, your product {product} has been added to cart")
        else:
            print("Product not available in required quantity")
    
    def place_order(self, payment):
        total = self.cart.calculate_total()
        payment.pay(total)

        order = Order(self.cart.items, total)
        self.order_history.append(order)
        
        for product, quantity in self.cart.items:
            product.update_stock(quantity)
        self.cart.clear()
        return order

        
    
class Admin(User):
    def __init__(self, id, name, email):
        super().__init__(id, name, email)
    
    def add_product(self, products, product):
        products.append(product)
        print("Product has been added into list")

    def remove_product(self, products, product_id):
        new_product = []
        for p in products:
            if p.id != product_id:
                new_product.append(p)
        products[:] = new_product
    
    def update_stock(self, product, quantity):
        product.stock = quantity

class Product:
    def __init__(self, id, name, price, stock):
        self.id = id
        self.name = name
        self.price = price
        self.stock = stock
    def __repr__(self):
        return f"{self.name} (${self.price})"

    def update_stock(self, quantity):
        if self.stock >= quantity:
            self.stock -= quantity
            return True
        return False
    def add_stock(self, quantity):
        self.stock += quantity
        print("Stock has been added")

    def is_available(self, quantity):
        return self.stock >= quantity


class Cart:
    def __init__(self):
        self.items = []
    
    def add_item(self, product, quantity):
        self.items.append((product, quantity))
        print("Item has been added into cart")

    def remove_item(self, product_id):
        new_items = []
        orignal_len = len(self.items)
        for item in self.items:
            product = item[0]
            if product.id != product_id:
                new_items.append(item)
        if len(self.items) < orignal_len:
            print("Item has been removed from cart")
        else:
            print("Item not found")
        

    def calculate_total(self):
        total = 0
        for item in self.items:
            p = item[0]
            q = item[1]
            total += p.price * q
        return total
    
    def clear(self):
        self.items = []

class Order:
    order_counter = 1
    def __init__(self, items, total_price):
        self.order_id = Order.order_counter
        Order.order_counter += 1
        self.items = items
        self.total_price = total_price
        self.status = "Placed"

    def update_status(self, status):
        self.status = status

class Payment(ABC):
    @abstractmethod
    def pay(self, amount):
        pass
class CreditCardPayment(Payment):
    def pay(self, amount):
        print(f"Payment of {amount} done by 'Credit Card'")
class PayPalPayment(Payment):
    def pay(self, amount):
        print(f"Payment of {amount} done by 'Pay Pal'")





    

    






    






