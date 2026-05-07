from vehicles import Vehicle 
from abc import ABC, abstractmethod

class Bikes(Vehicle):
    def vehicle_type(self):
        print(f"{self._name} is a Bike")
        
    def calculate_rent(self, days):
        if days > 3:
            discount = self._price_per_day * 0.5
            rent = (self._price_per_day*days) - discount
            print(f" Rent = {rent}")
        else:
            rent = (self._price_per_day*days)
            print(f" Rent = {rent}")