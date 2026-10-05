# Day 3: smart inventery and price audit manager
# Name: Khushi 
# What i learned today: I learned about lists and list methods, tuples , slicing and aggregations
# Where I got stuck & fixed it: I was confused about slicing, but I understood it using indexes.

# Store information
STORE_INFO = ("STR-8092", "Electronics & Retail")
print("Store ID:", STORE_INFO[0])
print("Category:", STORE_INFO[1])

# product prices list
prices = [1200, 450, 8900, 3200, 15000, 650]
print("Original Prices:", prices)

# Add a new price
prices.append(2500)
print("after add new price:", prices)

# Remove out of stock price
prices.remove(450)
print("after removing price:", prices)

# Sort prices
prices.sort()
print("after sorting:", prices)

# Get the top 3 expensive prices
top_3 = prices[-3:]
print("Top 3 most expensive products :", top_3)

# Get lowest 2 prices
lowest_2 = prices[:2]
print("lowest 2 budget products:", lowest_2)

# Reverse price list
reversed_prices = prices[::-1]
print("reversed price list:", reversed_prices)

# Calculate total price
total_value = sum(prices)
print("Total stock value:", total_value)

# Calculate average price
average_price = sum(prices) / len(prices)
print("Average Price:", average_price)

# Calculate price range
price_range = max(prices) - min(prices)
print("Price range:", price_range)

# report
print("=======================================")
print("      STORE INVENTORY AUDIT REPORT")
print("=======================================")

print("Store ID:", STORE_INFO[0])
print("Category:", STORE_INFO[1])

print("--------------------------------------")

print("Original prices:", [1200, 450, 8900, 3200, 15000, 650])
print("After updates:", prices)


print("top 3 premium items:", top_3)
print("lowest 2 budget items:", lowest_2)

print("---------------------------------------")

print(f"Total Stock Value: {total_value:.2f}")
print(f"Average Price / Item: {average_price:.2f}")
print("Price Range: {price_range:.2f}")

print("========================")
print("Audit Status: SUCCESSFUL")
print("======================{=")
