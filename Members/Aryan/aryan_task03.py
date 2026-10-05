# Day 3: Lists, Tuples & Slicing
# Name: Aryan
# What I learned today: Lists, tuples and slicing operations


STORE_INFO = ("STR-8092", "Electronics & Retail")
prices = [1200, 450, 8900, 3200, 15000, 650]
prices.append(2500)
prices.remove(450)
prices.sort()
top_3_expensive = prices[::-1][:3]
lowest_2_budget = prices[:2]
reversed_prices = prices[::-1]

# Inventory Metrics
total_inventory_value = sum(prices)
average_item_price = sum(prices) / len(prices)
price_range = max(prices) - min(prices)

# Final Audit Report
print("========================================")
print("      STORE INVENTORY AUDIT REPORT")
print("========================================")

print(f"Store ID       : {STORE_INFO[0]}")
print(f"Category       : {STORE_INFO[1]}")

print("----------------------------------------")


print(f"Top 3 Premium Items : {top_3_expensive}")
print(f"Lowest 2 Budget Items : {lowest_2_budget}")
print(f"Reversed Price List : {reversed_prices}")

print("----------------------------------------")

print(f"Total Stock Value  : ₹{total_inventory_value:.2f}")
print(f"Average Price/item : ₹{average_item_price:.2f}")
print(f"Price Range (Max-Min): ₹{price_range:.2f}")

print("----------------------------------------")
print("Audit Status: SUCCESSFUL")
print("========================================")