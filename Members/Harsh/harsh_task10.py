# Day 10: OOP Classes & Objects
# Name: Harsh Rajbhar
# What I learned today: class aur object banana, __init__, self, aur methods
# Where I got stuck & fixed it: method call mein () lagana zaroori hai

class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def total_value(self):
        return self.price * self.quantity

    def is_expensive(self):
        return self.total_value() > 5000

p1 = Product("pen", 10, 5)
p2 = Product("note_book", 400, 5)
p3 = Product("book", 1000, 6)

print(f"{p1.name} -> Total Value: {p1.total_value()}, Expensive: {p1.is_expensive()}")
print(f"{p2.name} -> Total Value: {p2.total_value()}, Expensive: {p2.is_expensive()}")
print(f"{p3.name} -> Total Value: {p3.total_value()}, Expensive: {p3.is_expensive()}")

print("==================================")
print("       Audit Status: SUCCESSFUL")
print("==================================")
