from model import *
import json

def load_drivers():
    with open("data.json", "r") as file:
        data = json.load(file)

    drivers = []
    for d in data["drivers"]:
        drivers.append(
            Driver(d["id"], d["name"], d["email"], d["vehicle_name"], d["available"])
        )
    return drivers

def save_drivers(drivers):
    data = {
        "drivers": [
            {"id" : d.id,
            "name" : d.name,
            "email" : d.email,
            "vehicle_name" : d.vehicle_name,
            "available" : d.available
        
        }
        for d in drivers
        ]
    }
    with open("data.json", "w") as file:
        json.dump(data, file, indent=4)

drivers = load_drivers()
rides = []

customer = Customer(1, "Alice", "alice@mail.com")
admin = Admin(2, "Admin", "admin@mail.com")

def customer_menu():
    while True:
        print("\n1. Book Ride\n2. View Current Ride\n3. Cancel Ride\n4. Logout")
        choice = input("Choice: ")

        if choice == "1":
            pickup = input("Pickup: ")
            destination = input("Destination: ")
            distance = int(input("Distance: "))

            ride = Ride(customer, pickup, destination, distance)

            driver = next((d for d in drivers if d.available), None)

            if driver:
                driver.accept_ride(ride)
                customer.book_ride(ride)
                rides.append(ride)
            else:
                print("No drivers available")

        elif choice == "2":
            if customer.current_ride:
                r = customer.current_ride
                print(f"{r.pickup} -> {r.destination}, Status: {r.status}")
            else:
                print("No active ride")

        elif choice == "3":
            customer.cancel_ride()

        elif choice == "4":
            break

def driver_menu(driver):
    while True:
        print("\n1. View Ride\n2. Complete Ride\n3. Toggle Availability\n4. Logout")
        choice = input("Choice: ")

        if choice == "1":
            if driver.current_ride:
                r = driver.current_ride
                print(f"{r.pickup} -> {r.destination}, Status: {r.status}")
            else:
                print("No ride assigned")

        elif choice == "2":
            driver.complete_ride()

        elif choice == "3":
            driver.available = not driver.available
            save_drivers(drivers)
            print("Availability changed")

        elif choice == "4":
            break

def admin_menu():
    while True:
        print("\n1. View Drivers\n2. Add Driver\n3. Remove Driver\n4. Logout")
        choice = input("Choice: ")

        if choice == "1":
            for d in drivers:
                print(d.id, d.name, d.vehicle_name, d.available)

        elif choice == "2":
            name = input("Name: ")
            email = input("Email: ")
            vehicle = input("Vehicle: ")

            new_id = max([d.id for d in drivers], default=0) + 1
            admin.add_driver(drivers, Driver(new_id, name, email, vehicle))
            save_drivers(drivers)

        elif choice == "3":
            did = int(input("Driver ID: "))
            admin.remove_driver(drivers, did)
            save_drivers(drivers)

        elif choice == "4":
            break


def main():
    while True:
        print("\n1. Customer\n2. Driver\n3. Admin\n4. Exit")
        choice = input("Choice: ")

        if choice == "1":
            customer_menu()

        elif choice == "2":
            did = int(input("Enter Driver ID: "))
            driver = next((d for d in drivers if d.id == did), None)
            if driver:
                driver_menu(driver)

        elif choice == "3":
            admin_menu()

        elif choice == "4":
            break


if __name__ == "__main__":
    main()


