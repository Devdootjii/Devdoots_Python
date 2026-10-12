# Day 10 Task
# Name: Khushi
# what i learned: OOP, class or object, attribute, self, __init__(), methods, bonus(is_expensive()) 
#where i got stuck: self , methods or  bonus samjhne me
class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def total_value(self):
        return self.price * self.quantity

    def is_expensive(self):
        return self.total_value() > 5000

p1 = Product("Pen", 10, 3)
p2 = Product("Jeans", 5, 5)
p3 = Product("Kurti", 400, 2)

# product details
print("Product 1")
print("Name:", p1.name)
print("Price:", p1.price)
print("Quantity:", p1.quantity)
print("Total Value:", p1.total_value())
print("Expensive:", p1.is_expensive())

print("\nProduct 2")
print("Name:", p2.name)
print("Price:", p2.price)
print("Quantity:", p2.quantity)
print("Total Value:", p2.total_value())
print("Expensive:", p2.is_expensive())

print("\nProduct 3")
print("Name:", p3.name)
print("Price:", p3.price)
print("Quantity:", p3.quantity)
print("Total Value:", p3.total_value())
print("Expensive:", p3.is_expensive())
