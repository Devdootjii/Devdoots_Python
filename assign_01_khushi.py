# Team Devdoots - python_assign_01
# File name: assign_01_khushi.py

inventory = [
    {"name": "Laptop", "price": 50000, "stock": 5},
    {"name": "mouse", "price": 500, "stock": 20},
    {"name": "keyboard", "price": 1200, "stock": 10}
]

def calculate_total_inventory_value(items):
    return sum(item["price"] * item["stock"] for item in items)

try:
    total = calculate_total_inventory_value(inventory)
    print(" Smart Inventory & Audit Logger ")
    
    for item in inventory:
        print(f"{item['name']} - rupees{item['price']} x {item['stock']}")
    
    print(f"Total Value: rupees{total}")

    # File logging
    with open("inventory_audit.txt", "a") as file:
        file.write(f"Total inventory value: rupees{total}\n")
    
    print("Log saved to 'inventory_audit.txt'")

except Exception as e:
    print(f"Error: {e}")