from abc import ABC, abstractmethod

class User:
    def __init__(self, id, name , email, logged_in):
        self.id = id
        self.name = name
        self.email = email
        self.logged_in = logged_in

    def login(self):
        if not self.logged_in:
            self.logged_in = True
            print("Logged in sucessfully")
        else:
            print("You are already logged in")
        
    def logout(self):
        if self.logged_in:
                self.logged_in = False
                print("Logged out sucessfully")
        else:
            print("You are already logged out")
             
class Customer(User):
    def __init__(self, id, name, email, current_ride):
        super().__init__(id, name, email)
        self.booking_history = []
        self.current_ride = None

    def book_ride(self, ride):
        self.current_ride = ride
        self.booking_history.append(ride)
        print("Ride booked sucessfully")

    
    def cancel_ride(self):
        if self.current_ride:
            self.current_ride.update_status("Cancelled!")
            print("Ride cancelled")
            self.current_ride = None


class Driver(User):
    def __init__(self, id, name, email, vehicle_name, available):
        super().__init__(id, name, email)
        self.vehicle_name = vehicle_name
        self.available = available
        self.current_ride = None

    def accept_ride(self, ride):
        self.current_ride = ride
        self.avaiable = False
        ride.driver = self
        ride.update_status("Accepted")
        print("Ride Accepted")


    def complete_ride(self):
        if self.current_ride:
            self.current_ride.update_status("Completed")
            self.available = True
            print("Ride Completed")
            self.current_ride = None

    def set_availability(self, status):
        self.available = status

class Admin(User):
    def __Init__(self, id, name, email):
        super().__init__(id, name , email)
        self.drivers = []

    def add_driver(self, id, name, email, vehicle):
        self.drivers.append((id, name, email, vehicle))
        print("Driver has been added into list")

        

    def remove_driver(self, name):
        new_list = []
        no_of_drivers = len(self.drivers)
        for driver in self.drivers:
            driver = driver[1]
            if driver != name:
                new_list.append(driver)
        if len(self.list) < no_of_drivers:
            print("driver has been removed from cart")
        else:
            print("driver not found")
        self.drivers = new_list
            



    def view_all_riders(self):
        for driver in self.drivers:
            print(f"Id: {driver[0]} Name: {driver[1]} Email: {driver[2]} Vehicle: {driver[3]}")

class Ride:
    ride_id = 1
    def __init__(self, ride_id, customer, driver, pickup, destination, distance, fare, status):
        self.ride_id = Ride.ride_id
        Ride.ride_id += 1
        self.customer = customer
        self.driver = driver
        self.pickup = pickup
        self.destination = destination
        self.distance = distance
        self.fare = fare
        self.status = "Availalbe"

    def calculate_fare(self, rate_per_km):
        fare = self.distance * rate_per_km
        print(f"Dear {self.customer}, you have a fare of {fare} from {self.pickup} to {self.destination}")
        self.status = "Reserved"

        

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
class WalletPayment(Payment):
    def pay(self, amount):
        print(f"Payment of {amount} done by 'Wallet'")






    










     


    