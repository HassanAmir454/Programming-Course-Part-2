class Vehicle:
    def __init__(self, vehicleName, status=False):
        self.vehicleName = vehicleName
        self.status = status

    def start(self):
        if self.status:
            print(f"{self.vehicleName} engine already starts...")
        else:
            self.status = True
            print(f"{self.vehicleName} engigne starts...")
        
    def stop(self):
        if self.status:
            self.status = False
            print(f"{self.vehicleName} engine off")
        else:
            print(f"{self.vehicleName} is already off")
                
    def operate(self):
        print(f"{self.vehicleName} is currently {self.status}")
        return self.status
        
class Car(Vehicle):
    def __init__(self, vehicleName, fuelLevel):
        super().__init__(vehicleName)
        self.fuelLevel = fuelLevel

    def operate(self):
        if self.fuelLevel > 1:
            print("You can drive the car")
        else:
            print("Car haven't enough fuel to operate.")

class Bike(Vehicle):
    def __init__(self, vehicleName, gear):
        super().__init__(vehicleName)
        self.gear = gear

    def operate(self):
        if self.gear:
            print("Bike cannot able to operate because it is in gear")
        else:
            print("Bike is ready to operate.")

class ElectricScooter(Vehicle):
    def __init__(self, vehicleName, batteryLevel):
        super().__init__(vehicleName)
        self.batteryLevel = batteryLevel


    def operate(self):
        if self.batteryLevel < 1 :
            print("Electric scooter cannot able to operate because batteryLevel is low")
        else:
            print("ElectricScooter is ready to operate.")

        
def operate_vehicles(vehicles):
    if not vehicles:
        print("There is no vehicle to operate")
    else:
        for vehicle in vehicles:
            print("- ", end="")
            vehicle.operate()

    
    
    


            









# Create a base class Vehicle

# Attributes: vehicleName, status

# Methods: start(), stop(), operate()

# Create subclasses: 

# Car → attribute: fuelLevel

# Bike → attribute: gear

# ElectricScooter → attribute: batteryLevel

# Each subclass must override operate().

# Create two files:

# vehicle.py → all classes + operate_vehicles()

# main.py → menu system

# Menu
# 1 - Add Vehicle
# 2 - Operate Vehicles
# 0 - Exit