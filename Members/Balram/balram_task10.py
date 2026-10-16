# Product class define karna
class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    # Price aur quantity multiply karke total nikalna
    def total_value(self):
        return self.price * self.quantity

    # Clean detail print karne ke liye method
    def display_details(self):
        print(f"Item: {self.name} | Price: Rs.{self.price} | Quantity: {self.quantity} | Subtotal: Rs.{self.total_value()}")


# --- Proof of Work (PoW) Execution Block ---
if __name__ == "__main__":
    # 3 alag-alag product objects instantiate karna
    item1 = Product("Wireless Mouse", 750, 4)
    item2 = Product("Mechanical Keyboard", 2800, 2)
    item3 = Product("USB-C Hub", 1200, 5)

    inventory = [item1, item2, item3]

    print("Inventory Items:")
    grand_total = 0
    for product in inventory:
        product.display_details()
        grand_total += product.total_value()

    print(f"\nGrand Total Stock Value: Rs.{grand_total}")