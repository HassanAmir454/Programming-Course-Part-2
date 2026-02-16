class SchoolMember:
    def __init__(self, name , active):
        self.name = name 
        self.active = active

    def perform_role(self):
        print(f"{self.name} performance in scool is .....")

    




# Build a Smart School Management System using polymorphism.

# Requirements

# Base class SchoolMember

# Attributes: name, active

# Method: perform_role()

# Subclasses:

# Student → grade

# Teacher → subject

# Staff → department

# Create perform_all(members) function.

# Menu-driven program.