import ModuleExample
from ECommerce.Shopping import calc_shopping_cart
#we use classes to define new types
class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
    def display(self):
        print(f"{self.first_name} {self.last_name}")
    def greet_user(self):
        print(f"Hello {self.first_name} {self.last_name}")

person1 = Person("John", "Doe")
person1.display()

#inheritance
class Employee:
    def run(self):
        print("This is an employee class")

class Developer(Employee):
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
    def display(self):
         print(f"{self.first_name} {self.last_name}")


person2 = Developer("John", "Doe")
person2.display()
person2.run()

print(ModuleExample.name)
print(calc_shopping_cart())