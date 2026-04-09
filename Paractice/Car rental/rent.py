
from abc import ABC, abstractmethod
import sys
import csv

class Vehicle (ABC):
    def __init__(self, vehicle_id, price_per_day, is_rented=False):
        self.__vehicle_id = vehicle_id
        self._is_rented = is_rented
        self._price_per_day = price_per_day

    def get_vehicle_id(self):
        return self.__vehicle_id
    
    def is_available(self):
        if not self._is_rented:
            print("Yes, you can rent this car.")
        else:
            print("Sorry, This car is already rented to someone.")          

    def rent_vehicle(self):
        if self._is_rented:
            print(f"Vehicle is rented to you.")
        else:
            self._is_rented = True
            print("Vehicle rented sucessfully")
    
    def return_vehicle(self):
        if self._is_rented == False:
            print("Vehicle was not rented.")
        else:
            self._is_rented = False
            print("Vehicle returned successfully.")
    def __str__(self):
        return f"ID: {self.__vehicle_id} | Price/day: {self._price_per_day} | Rented: {self._is_rented}"

    @abstractmethod
    def calculate_rent(self, days):
        pass

class Car(Vehicle):
    def __init__(self,vehicle_id, price_per_day, brand, seating_capacity):
        self.brand = brand
        self.seating_capacity = seating_capacity
        super().__init__(vehicle_id, price_per_day)

    def calculate_rent(self, days):
        rent = self._price_per_day * days
        print(f"Your rent of car {self.get_vehicle_id()} for {days} is {rent}Rs.")

class Bike(Vehicle):
    def __int__(self, vehicle_id, price_per_day, engine_cc, helmet:bool):
        super().__init__(vehicle_id, price_per_day)
        self.helmet = helmet
        self.engine_cc = engine_cc


    def calculate_rent(self, days, helmet):
        rent = days * self._price_per_day
        if self.helmet:
            rent = days * self._price_per_day + days*50
        return rent
        

class Truck(Vehicle):
    def __init__(self, vehicle_id, price_per_day, load_capacity):
        super().__init__(vehicle_id, price_per_day)
        self.load_capacity = load_capacity
    def calculate_rent(self, days):
        rent = self._price_per_day * days + 500
        print(f"Your rent of car {self.get_vehicle_id()} for {days} is {rent}Rs.")

class RentalCompany:
    
    def __init__(self):
        self.vehicles = []
    
    def add_vehicle(self, vehicle):
        self.vehicles.append(vehicle)
        print("Vehicle added sucessfully")

    def list_vehicles(self):
        for vehicle in self.vehicles:
            print(vehicle)
        
    def find_vehicle(self, vehicle_id):
        for vehicle in self.vehicles:
            if vehicle.get_vehicle_id() == vehicle_id:
                return vehicle
        return None

    def rent_vehicle(self, vehicle_id):
        vehicle = self.find_vehicle(vehicle_id)
        if vehicle:
            vehicle.rent_vehicle()
        else:
            print("Vehicle not found")

    def return_vehicle(self, vehicle_id):
        vehicle = self.find_vehicle(vehicle_id)
        if vehicle:
            vehicle.return_vehicle()
        else:
            print("Vehicle not found.")
    
    def calculate_rent(self, vehicle_id, days):
        vehicle = self.find_vehicle(vehicle_id)
        if vehicle:
            rent = vehicle.calculate_rent(days)
            print("Total Rent:", rent)
        else:
            print("Vehicle not found.")
    
    def save_to_file(self):
        with open("vehicles.csv", "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["type", "id", "price", "rented", "extra1", "extra2"])
            for vehicle in self.vehicles:
                if isinstance(vehicle, Car):
                    writer.writerow(["Car", vehicle.get_vehicle_id(),
                                     vehicle._price_per_day,
                                     vehicle._is_rented,
                                     vehicle.brand,
                                     vehicle.seating_capacity])
                elif isinstance(vehicle, Bike):
                    writer.writerow(["Bike", vehicle.get_vehicle_id(),
                                     vehicle._price_per_day,
                                     vehicle._is_rented,
                                     vehicle.engine_cc,
                                     vehicle.helmet])
                elif isinstance(vehicle, Truck):
                    writer.writerow(["Truck", vehicle.get_vehicle_id(),
                                     vehicle._price_per_day,
                                     vehicle._is_rented,
                                     vehicle.load_capacity, ""])
            print("Data saved successfully.")
    def load_from_file(self):
        self.vehicles.clear()
        try:
            with open("vehicles.csv", "r") as file:
                reader = csv.DictReader(file)

                for row in reader:
                    vtype = row["type"]
                    vid = row["id"]
                    price = int(row["price"])
                    rented = row["rented"] == "True"

                    if vtype == "Car":
                        vehicle = Car(vid, price, row["extra1"], int(row["extra2"]))

                    elif vtype == "Bike":
                        vehicle = Bike(vid, price, int(row["extra1"]), row["extra2"] == "True")

                    elif vtype == "Truck":
                        vehicle = Truck(vid, price, int(row["extra1"]))

                    vehicle._is_rented = rented
                    self.vehicles.append(vehicle)

            print("Data loaded successfully.")

        except FileNotFoundError:
            print("No file found.")
        
    

        


    





# vehicles = []

# Methods:

# add_vehicle(vehicle)

# list_vehicles()

# rent_vehicle(vehicle_id)

# return_vehicle(vehicle_id)

# calculate_vehicle_rent(vehicle_id, days)

# save_to_file()

# load_from_file()
    




    
# 🚐 Truck

# Extra attributes:

# load_capacity

# Rent Formula:
# price_per_day * days
# + 500 heavy-duty fee (fixed)

    



    




    


#engine_cc

# helmet_included (True/False)

# Rent Formula:
# price_per_day * days
# + 50 per day if helmet included

          
# Extra attributes:

# seating_capacity

# brand

# Rent Formula:
# price_per_day * days


# It must include:
# 🔒 Encapsulation

# __vehicle_id (private)

# _is_rented (protected)

# _price_per_day (protected)

# 🧠 Methods

# get_vehicle_id()

# is_available()

# rent_vehicle()

# return_vehicle()

# calculate_rent(days) → ABSTRACT METHOD

# This forces polymorphism.

# 🧠 Rules

# If vehicle is already rented → cannot rent again

# If vehicle is not rented → cannot return

# 🧱 STEP 2 — Create Subclasses (Inheritance + Polymorphism)

# Create:

# 🚘 Car

# Extra attributes:

# seating_capacity

# brand

# Rent Formula:
# price_per_day * days

# 🏍 Bike

# Extra attributes:

# engine_cc

# helmet_included (True/False)

# Rent Formula:
# price_per_day * days
# + 50 per day if helmet included

# 🚐 Truck

# Extra attributes:

# load_capacity

# Rent Formula:
# price_per_day * days
# + 500 heavy-duty fee (fixed)

# 🧱 STEP 3 — Company Class (Composition)

# Create a class:

# RentalCompany


# This class will manage vehicles.

# Attributes:

# vehicles = []

# Methods:

# add_vehicle(vehicle)

# list_vehicles()

# rent_vehicle(vehicle_id)

# return_vehicle(vehicle_id)

# calculate_vehicle_rent(vehicle_id, days)

# save_to_file()

# load_from_file()

# 🧱 STEP 4 — Use isinstance()

# When saving to file:

# if isinstance(vehicle, Car):


# You must detect the type and store:

# type,id,price,is_rented,extra1,extra2


# Example:

# Car,101,2000,False,5,Toyota
# Bike,202,800,True,150,True
# Truck,303,5000,False,10

# 🧱 STEP 5 — Serialization (CSV)
# Save:

# Type

# ID

# Price

# Rental status

# Extra attributes

# Load:

# Read type

# Create correct object

# Append to list

# 🧱 STEP 6 — Build Menu System (main.py)

# Menu must have:

# 1 - Add Vehicle
# 2 - List Vehicles
# 3 - Rent Vehicle
# 4 - Return Vehicle
# 5 - Calculate Rent
# 6 - Save Data
# 7 - Load Data
# 0 - Exit

# 🧠 VERY IMP


