from abc import ABC, abstractmethod

# Abstract class
class Patient(ABC):

    @abstractmethod
    def calculate_bill(self):
        pass


# InPatient class
class InPatient(Patient):

    def calculate_bill(self):
        return 20000


# Main
ptype = input("Patient Type: ")

if ptype.lower() == "inpatient":
    p = InPatient()
    print("Total Bill:", p.calculate_bill())