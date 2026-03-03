from abc import ABC, abstractmethod

# Abstract class
class Vehicle(ABC):

    @abstractmethod
    def calculate_rent(self, days):
        pass


# Car class
class Car(Vehicle):

    def calculate_rent(self, days):
        return days * 1000


# Bike class
class Bike(Vehicle):

    def calculate_rent(self, days):
        return days * 500


# Main
vehicle_type = input("Vehicle: ")
days = int(input("Days: "))

if vehicle_type.lower() == "car":
    v = Car()
else:
    v = Bike()

print("Total Rent:", v.calculate_rent(days))