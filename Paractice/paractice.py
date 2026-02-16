# Q1. Student Class

# Create a class Student with:

# attributes: name, roll_no, marks

# method display() that prints student details

# 👉 Create 2 objects and call display().
class Student:
    def __init__(self, name, roll_no, marks):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks
    def display(self):
        print(f"The roll no of student {self.name} is {self.roll_no} and he/she gained {self.marks} marks") 

data = Student("Hassan", 4854, 100)
print(data.display())
data = Student("Hussain", 4853, 101)
print(data.display())


# Q3. Vehicle System

# Base class: Vehicle

# attribute: speed

# method: show_speed()

# Subclasses:

# Car

# Bike

# Each subclass should inherit Vehicle and use show_speed().

class Vehicle:
    def __init__(self, speed):
        self.speed = speed
    def showSpeed(self):
        print(F"The speed is {self.speed} km/h")
    
class Car(Vehicle):
    pass
class Bike(Vehicle):
    pass

car = Car(120)
bike = Bike(70)

car.showSpeed()
bike.showSpeed()