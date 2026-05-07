from abc import ABC, abstractmethod
import sys
import csv

class Vehicle(ABC):
    def __init__(self, name, price_per_day, wheels):
        self._name = name
        self._price_per_day = price_per_day
        self._wheels = wheels
    
    def display_info(self):
        print(f"{self._name, self._price_per_day, self._wheels}")
    
    def get_price(self):
        print(f"{self._price_per_day}")
        
    
    @abstractmethod
    def calculate_rent(self, days):
        pass
    @abstractmethod
    def vehicle_type(self):
        pass
        


