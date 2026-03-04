from abc import ABC, abstractmethod

# Abstract Class
class BankAccount(ABC):
    
    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance   # Encapsulation

    def get_balance(self):
        return self.__balance

    @abstractmethod
    def calculate_interest(self):
        pass


# Child Class
class SavingsAccount(BankAccount):

    def calculate_interest(self):   # Polymorphism
        return self.get_balance() * 0.04


# Main
name = input("Name: ")
balance = float(input("Balance: "))

acc = SavingsAccount(name, balance)

print("Balance:", acc.get_balance())
print("Interest:", acc.calculate_interest())