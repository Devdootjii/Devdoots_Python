 # Products data:  tuple list
products = [("Laptop", 50000, 4.5),("Mouse", 500, 3.8),("Keyboard", 1500, 4.2),("Monitor", 12000, 4.7)]

#Part-A: Products with Rating >= 4.0
print("Products with rating 4.0 or higher:")
for name, price, rating in products:
    if rating >= 4.0:
        print(name)
print("\n" + "="*30 + "\n")

#Part-B: Manual Max Price Search (Without max() function) 

max_product = products[0]
for product in products:

    if product[1] > max_product[1]:
        max_product = product

print(f"Most Expensive Product: {max_product[0]} (Price: rupees{max_product[1]})")