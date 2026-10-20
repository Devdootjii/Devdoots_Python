# Day 10 
# Name: Divaynsh
# waht i lerened : class and oops concepts
# where i stuck : understanding ho to print output
class Product:
    def __init__(self,name,price,quantity):
        self.name =name
        self.price=price
        self.quantity=quantity

    def total_value(self):
        return self.quantity * self.price

p1=Product("Pen",10,5)
print(f"Name of Product:{p1.name}")
print(f"Price of Product:{p1.price}")
print(f"Qunatity of Product:{p1.quantity}")
print(f"Total value of Product:{p1.total_value()}\n")

p2=Product("Notebook",30,3)
print(f"Name of Product:{p2.name}")
print(f"Price of Product:{p2.price}")
print(f"Qunatity of Product:{p2.quantity}")
print(f"Total value of Product:{p2.total_value()}")
