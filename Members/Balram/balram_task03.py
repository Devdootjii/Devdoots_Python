# Day 3: Lists, Tuples & Slicing
# Name: Balram Singh
# What I learned today: list slicing aur tuple ke basic operations
# Where I got stuck & fixed it: negative index slicing ka concept samajhna tha

# store info fixed tuple
STORE_INFO = ("STR-8092", "Electronics & Retail")

# initial price list
prices = [1200, 450, 8900, 3200, 15000, 650]

# new item add kiya
prices.append(2500)

# remove minimum price item
chota_price = min(prices)
prices.remove(chota_price)

# sort list
prices.sort()

# slicing syntax
top_3 = prices[-3:]
low_2 = prices[:2]

# basic stats calculation
total_val = sum(prices)
item_count = len(prices)
avg_price = total_val / item_count
p_range = max(prices) - min(prices)

print("STORE INVENTORY AUDIT REPORT")
print("Store ID:", STORE_INFO[0])
print("Category:", STORE_INFO[1])
print("Updated Prices:", prices)
print("Top 3 Premium Items:", top_3[::-1])
print("Lowest 2 Budget Items:", low_2)
print("Total Stock Value:", total_val)
print("Average Price / Item:", avg_price)
print("Price Range (Max-Min):", p_range)
print("Audit Status: SUCCESSFUL")