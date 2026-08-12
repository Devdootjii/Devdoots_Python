product_list=[("Laptop",50000,4.5),("Mouse",500,3.8 ),("Keybord",1500,4.2),("Moniter",12000,4.7)]
for (name,price,rating) in product_list:
    if rating>=4.0:
        print(f"Name={name},Rating={rating}")
highest_price = 0
highest_name = ""
for (name,price,rating) in product_list: 
    if price >= highest_price:
        highest_price = price
        highest_name = name
print(f"Product={highest_name},Price={highest_price}")
