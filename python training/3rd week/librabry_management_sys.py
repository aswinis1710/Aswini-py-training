from abc import ABC, abstractmethod

# Abstract class
class LibraryItem(ABC):
    
    @abstractmethod
    def issue(self):
        pass


# Child class
class Book(LibraryItem):
    
    def __init__(self, name):
        self.name = name

    # Override method
    def issue(self):
        print("Book '" + self.name + "' issued for 14 days")


# Main
book_name = input("Book Name: ")

b = Book(book_name)
b.issue()