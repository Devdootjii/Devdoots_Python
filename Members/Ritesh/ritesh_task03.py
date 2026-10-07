# Day 3: Lists, Tuples & Slicing
# Name: Ritesh
# What I learned today: Tuples immutability, dynamic list methods (.append, .remove, .sort), and slicing operations.
# Where I got stuck & fixed it: Extracted top 3 items in descending order using combined slicing prices[-3:][::-1].

#Step1: Fixed Product Metadata using Tuple(Immutable)
from matplotlib.pyplot import step


STORE_INFO = ("STR-8092", "ELECTRONICS & RETAILS")

try:
    STORE_INFO[0] = " MODIFIIED-ID"
except TypeError:
 pass
# step 2 : Price List Management
original_prices = [ 1200 , 450 ,8900, 3200 , 15000 , 650 ]
prices = original_prices.copy()
# add new product Price (.append)
prices.append(2500)
# Out of stock item (minimum price value) ko remove karna (.remove)

min_item = min(prices)
prices.remove(min_item)

# prices list ko ascending oreder me sort karna 
prices.sort()

#step 3 : Data Slicing & analytics
# top  3 most expensive products ( hightesr to Lowest )
top_3_premium = prices[-3:][::-1]

#lowest 2 budgest products
lowest_2_budget = prices[:2]
#Reversed Price List using slicing syntax [::-1]
reversed_prices = prices[::-1]

# step 4: Metrics output 
total_stock_value = sum(prices)
average_prices = total_stock_value / len(prices)
price_range = max(prices) - min(prices)

#  terminal ooutput 
print("=======================================")
print("      STORE INVENTORY AUDIT REPORT     ")
print("=======================================")
print(f"Store ID       : {STORE_INFO[0]}")
print(f"Category       : {STORE_INFO[1]}")
print("---------------------------------------")
print(f"Original Prices : {original_prices}")
print(f"After Updates   : {prices}")
print("---------------------------------------")
print(f"Top 3 Premium Items  : {top_3_premium}")
print(f"Lowest 2 Budget Items : {lowest_2_budget}")
print("---------------------------------------")
print(f"Total Stock Value: {total_stock_value:.2f}")
print(f"Average Price / Item : {average_prices:.2f}")
print(f"Price Range (Max-Min): {price_range:.2f}")
print("=======================================")
print("Audit Status: SUCCESSFUL")
print("=======================================")
