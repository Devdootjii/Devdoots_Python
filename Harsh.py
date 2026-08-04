inventory_list = [
    {"name": "3D Environment Pack", "price": 1500, "stock": 20},
    {"name": "Physics Engine Pro", "price": 5000, "stock": 5},
    {"name": "Lighting Asset Bundle", "price": 800, "stock": 50}
]

def calculate_total_inventory_value(inventory_list):
    total_value = 0
    for product in inventory_list:
        item_total = product["price"] * product["stock"]
        total_value = total_value + item_total
        
    return total_value 

def save_report(total_value):
    try:
        file = open("inventory_report.txt", "w")
        file.write("Total Inventory Value: " + str(total_value))
        file.close()
        print("Report successfully save!")
        
    except Exception as error:
        print("File save karte waqt error aaya:", error)

calculated_total = calculate_total_inventory_value(inventory_list)
save_report(calculated_total)
