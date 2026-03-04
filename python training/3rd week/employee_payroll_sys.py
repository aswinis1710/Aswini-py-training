from abc import ABC, abstractmethod

# Abstract class
class Employee(ABC):

    @abstractmethod
    def calculate_salary(self):
        pass


# Permanent Employee
class PermanentEmployee(Employee):

    def calculate_salary(self):
        return 50000


# Contract Employee
class ContractEmployee(Employee):

    def calculate_salary(self):
        return 30000


# Main
emp_type = input("Employee Type: ")

if emp_type.lower() == "permanent":
    emp = PermanentEmployee()
else:
    emp = ContractEmployee()

print("Salary:", emp.calculate_salary())