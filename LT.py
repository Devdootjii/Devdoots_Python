#task 2
def process_products():
    products =[
        ("Laptop", 50000, 4.5),
        ("Mouse", 500, 3.8),
        ("Keyboard", 1500, 4.2),
        ("Monitor", 12000, 4.7)
    ]
    print("--- Products rating >=4.0 ---")
    if rating >= 4.0:
        print(f"- {name} (Rating: {rating})")
        highest_product = products[0]
    for item in products:
        if item[1] > highest_product[1]:
            highest_product= item 
            print("\n--- Most Expansive Product ---")
            print(f"Products: {highest_product[0]} | Price : INR {highest_product[1]}")
