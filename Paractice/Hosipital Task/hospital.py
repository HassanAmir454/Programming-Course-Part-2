# HospitalMember (abstract)

# Attributes:

# name (str)

# onDuty (bool, default True)

# Abstract Method:

# perform_duty()

# Methods:

# toggle_duty() → switches onDuty between True/False

# Encapsulation:

# name should be private and accessed via getter/setter

# onDuty can be protected or public
# Subclasses (Inheritance + Polymorphism)

# Doctor:

# Attribute: specialization (str)

# perform_duty() → prints "Doctor {name} is treating patients in {specialization}"

# Nurse:

# Attribute: ward (str)

# perform_duty() → prints "Nurse {name} is assisting in {ward} ward"

# Technician:

# Attribute: equipment (str)

# perform_duty() → prints "Technician {name} is operating {equipment}"

# 3️⃣ Serialization / Deserialization

# Save all hospital members to a JSON file

# Load them back and restore their attributes

# 4️⃣ Menu-driven System
# 1 - Add Staff Member
# 2 - List Staff Members
# 3 - Perform Duties (polymorphism)
# 4 - Save to File
# 5 - Load from File
# 0 - Exit
from abc import ABC, abstractmethod
import csv

class HospitalMember(ABC):
    def __init__(self, name, onDuty: bool):
        self.__name = name
        self._onDuty = True

    def toggle_duty(self):
        if self._onDuty == True:
            self._onDuty = False
        elif self._onDuty == False:
            self._onDuty = True

    def get_name(self):
        return self.__name
    
    @abstractmethod
    def perform_duty(self):
        pass

class Doctor(HospitalMember):
    def __init__(self, name, specialization):
        super().__init__(name)
        self.specialization = specialization
    
    def perform_duty(self):
        print(f"Doctor {self.get_name()} is treating patients in {self.specialization}")

class Nurse(HospitalMember):
    def __init__(self, name, Ward):
        super().__init__(name)
        self.Ward = Ward
    
    def perform_duty(self):
        print(f"Nurse {self.get_name()} is assisting in {self.Ward} ward")

class Technician(HospitalMember):
    def __init__(self, name, equipment):
        super().__init__(name)
        self.equipment = equipment
    
    def perform_duty(self):
        print(f"Technician {self.get_name()} is operating {self.equipment}")
        


def add_members(members):
    try:
        with open("patients.cvs", "w") as file:
            writer = csv.writer(file)
            writer.writerow(["type", "name", "extra"])
        for member in members:
            if isinstance(member, Doctor):
                writer.writerow(["Doctor", member.get_name(), member.specialization])
            elif isinstance(member, Nurse):
                writer.writerow(["Nurse", member.get_name(), member.Ward])
            elif isinstance(member, Technician):
                writer.writerow(["Technician", member.get_name(), member.equipment])
    except:
        print("Something went wrong")

def read_members():
    members = []
    try:
        with open("patients.csv", "r") as file1:
            reader = csv.DictReader(file1)

            for row in reader:
                type_ = row(["type"])
                name = row(["name"])
                extra= row(["extra"])
            if type_ == "Doctor":
                member = Doctor(name, extra)
            elif type_ == "Nurse":
                member = Nurse(name, extra)
            elif type_ == "Technician":
                member = Technician(name, extra)
            
            members.append(member)
    except:
        print("Something went wrong")

def list_members(members):
    for member in members:
        print(f"{member[0]} is a {member[1]} in {member[2]}")
