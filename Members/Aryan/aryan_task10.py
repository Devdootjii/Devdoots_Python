# Day 10: OOP - Classes and Objects
# Name: Aryan
# What I learned today: Classes, Objects, Constructors and Methods


class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def total_value(self):
        return self.price * self.quantity

    def is_expensive(self):
        return self.total_value() > 5000


# Creating three product objects
p1 = Product("Keyboard", 1200, 2)
p2 = Product("Laptop", 45000, 1)
p3 = Product("Mouse", 500, 4)


# Product 1 details
print(f"\nProduct Name: {p1.name}")
print(f"Price: ₹{p1.price}")
print(f"Quantity: {p1.quantity}")
print(f"Total Value: ₹{p1.total_value()}")
print(f"Is Expensive: {p1.is_expensive()}")


# Product 2 details
print(f"\nProduct Name: {p2.name}")
print(f"Price: ₹{p2.price}")
print(f"Quantity: {p2.quantity}")
print(f"Total Value: ₹{p2.total_value()}")
print(f"Is Expensive: {p2.is_expensive()}")


# Product 3 details
print(f"\nProduct Name: {p3.name}")
print(f"Price: ₹{p3.price}")
print(f"Quantity: {p3.quantity}")
print(f"Total Value: ₹{p3.total_value()}")
print(f"Is Expensive: {p3.is_expensive()}")