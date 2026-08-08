# product data
products = [
    {"name": "Laptop", "price": 45000, "stock": 5},
    {"name": "Mouse", "price": 500, "stock": 15},
    {"name": "Keyboard", "price": 1200, "stock": 10}
]

# calc total value
def calculate_total_inventory_value():
    total = 0
    for item in products:
        total = total + (item["price"] * item["stock"])
    return total

# error handling
try:
    # get input
    check = int(input("Inventory check karne ke liye 1 dabaye: "))
    
    if check == 1:
        total_val = calculate_total_inventory_value()
        
        # write to txt file
        file = open("inventory_report.txt", "w")
        file.write("Total Inventory Value: " + str(total_val))
        file.close()
        
        # read and print
        file = open("inventory_report.txt", "r")
        print(file.read())
        file.close()
    else:
        print("wrong number!")

except ValueError:
    print("bro do not type text , only number !")