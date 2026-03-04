from abc import ABC, abstractmethod

# Abstract class
class Payment(ABC):

    @abstractmethod
    def pay(self, amount):
        pass


# UPI class
class UPI(Payment):

    def pay(self, amount):
        print("Paid ₹" + str(amount) + " using UPI")


# Card class
class Card(Payment):

    def pay(self, amount):
        print("Paid ₹" + str(amount) + " using Card")


# Cash class
class Cash(Payment):

    def pay(self, amount):
        print("Paid ₹" + str(amount) + " using Cash")


# Main
mode = input("Payment Mode: ")
amount = int(input("Amount: "))

if mode.lower() == "upi":
    p = UPI()
elif mode.lower() == "card":
    p = Card()
else:
    p = Cash()

p.pay(amount)