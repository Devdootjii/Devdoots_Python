#task2

product_list=[("Laptop",50000,4.5),("Mouse",500,3.8),("keyboard",1500,4.2),("Moniter",12000,4.7)]

for product in product_list:
    name=product[0]
    price=product[1]
    rating=product[2]

    if rating>= 4.0:
        print(f"Name:{name}, Rating:{rating}")

max_price =0
max_pro_name=""
for prodeuct in product_list:
    price=product[1]
    name=product[0]

    if price>max_price:
        max_price=price
        max_pro_name=name
print(f"Most coastly product :{max_pro_name} with price:{max_price}")