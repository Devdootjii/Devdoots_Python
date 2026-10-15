# Day 10: OOP Part 1 - Classes & Objects
# Name: Ritesh
# What I learned today: Class blueprints, __init__ constructor, instance methods with self, and object instantiation.
# Where I got stuck & fixed it: Referenced instance method self.total_value() inside bonus is_expensive method.

print("========================================")
print("     PRODUCT INVENTORY ENGINE (OOP)     ")
print("========================================")

# Step 1 & 2: Defining the Product Class with __init__ and Methods
class Product :
    def __init__(self , name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
# Method to calculate total inventory value
    def total_value(self):
     return self.price * self.quantity

# Bonus Method: Check if total value exceeds 5000
    def is_expensive(self):
     return self.total_value() > 5000

# Step 4: Instantiating 3 Product Objects
p1 = Product("Laptop", 55000, 2)
p2 = Product("Wireless Mouse", 850, 4)
p3 = Product("Mechanical Keyboard", 3200, 2)
products_list = [p1,p2,p3]
# Step 5 & 6: Displaying Product Details & Verification
print(f"{'Name':<22} | {'Price':<10} | {'Qty' :<5} | {'Total value':<12} | {'Expensive'}")
for product in products_list:
    val = product.total_value()
    expensive_status = product.is_expensive()
    print(f"{product.name:<22} | {product.price:<9.2f} | {product.quantity:<5} | {val:<11.2f} | {expensive_status}")

print("========================================")
print("Audit Status: SUCCESSFUL")
print("========================================")

