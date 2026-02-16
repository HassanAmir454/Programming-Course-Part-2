# Class Name:

# BankAccount

# Private Attributes (Encapsulation):

# __account_number → integer

# __balance → float

# Methods:

# 1️⃣ Getter

# get_balance() → returns balance

# 2️⃣ Setter / Transaction Methods

# deposit(amount) → adds to balance (only if amount > 0)

# withdraw(amount) → subtracts from balance (only if amount ≤ balance)

# 3️⃣ Display Method

# display_info() → prints account number and balance
#
#
# Step 1 — Convert BankAccount to Abstract Base Class

# Make BankAccount an abstract class

# Add two abstract methods (no implementation yet):

# calculate_interest() → every child class must define how interest is calculated

# account_type() → returns account type as string

# Goal: Force all child accounts to implement these methods.

# Step 2 — Create Child Classes

# You need two account types:

# SavingsAccount

# Inherits BankAccount

# Interest = 5% of balance

# Minimum balance = 1000

# Must implement abstract methods

# CurrentAccount

# Inherits BankAccount

# Interest = 0

# Overdraft allowed (balance can go below 0)

# Must implement abstract methods

# Step 3 — Implement Polymorphism

# Store all account objects in a single list

# Loop through the list and call the same methods:

# display_info()

# calculate_interest()

# account_type()

# Observe how the same method behaves differently for each account type

# Goal: Understand runtime polymorphism.

# Step 4 — Add Child-specific Behavior

# Modify withdraw() in SavingsAccount to prevent balance < 1000

# Modify withdraw() in CurrentAccount to allow negative balance

# Test both behaviors using the list from Step 3

# Goal: Combine encapsulation (private balance) with inheritance and polymorphism
from abc import ABC, abstractmethod
class BankAccount(ABC):
    def __init__(self, acc_no):
        self.__acc_no = acc_no
        self._balance = 0.0

    def get_balance(self):
        return self._balance
    
    def deposit(self, amount):
        if amount > 0:
            self._balance += amount

    def withdraw(self, amount):
        if amount <= self._balance:
            self._balance -= amount
        else:
            print("You didn't have susficient balance to with draw")
    
    @abstractmethod
    def calculate_interest(self):
        pass

    @abstractmethod
    def account_type(self):
        pass

    
    def display_info(self):
        print(f"Your account number {self.__acc_no} has amount {self._balance}")


class SavingsAccount(BankAccount):
    def calculate_interest(self):
        if self._balance > 1000:
            interest = (self._balance/100)*5
            print(f"Your intrest is 5% which is: {interest}")
        else:
            print("This is saving account your account must have minimum balance 1000")
    def account_type(self):
        print("This is saving account")
    def withdraw(self, amount):
        remaining = self._balance - amount
        if remaining > 1000:
            self._balance -= amount
        else:
            print("This is saving account your account must have minimum balance 1000")



class CurrentAccount(BankAccount):
    def calculate_interest(self):
        print("interest = 0")
    def account_type(self):
        print("This is current account")
    def withdraw(self, amount):
        self._balance -= amount


def Display_all_acc(Accounts):
    for account in Accounts:
        account.display_info()
            
        

    