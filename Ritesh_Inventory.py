# List of Dictionaries
inventory = [
    {"name": "Laptop", "price": 50000, "stock": 5},
    {"name": "Mouse", "price": 500, "stock": 20},
    {"name": "Keyboard", "price": 1500, "stock": 10}
]


def calculate_total_inventory_value(items):
    total_value = 0

    for item in items:
        item_total = item["price"] * item["stock"]
        total_value += item_total

    return total_value


def save_and_read_report(inventory):
    try:
        total_value = calculate_total_inventory_value(inventory)

        # Write report to file
        with open("ritesh_inventory_report.txt", "w") as file:
            file.write("--- Smart Inventory Report ---\n")
            file.write(f"Total Inventory Value: INR {total_value}\n")

        print("Report file successfully saved.\n")

        # Read report from file
        with open("ritesh_inventory_report.txt", "r") as file:
            content = file.read()

        print("--- Terminal Output (Reading File) ---")
        print(content)

    except Exception as e:
        print(f"Something went wrong: {e}")


# Function call
save_and_read_report(inventory)
