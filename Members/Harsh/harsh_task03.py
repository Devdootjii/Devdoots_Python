# Day 3: Lists, Tuples & Slicing
# Name: Harsh Rajbhar
# What I learned today: lists, tuples aur slicing operations (list methods + [::-1])
# Where I got stuck & fixed it: tuple ki value badalne ki koshish ki thi, samajh aaya ki tuple immutable hai


Stor_info = ("STR-8092", "Electronics & Retail")
store_id, category = Stor_info          

#Price List (list = mutable)
prices = [1200, 450, 8900, 3200, 15000, 650]
original_prices = prices.copy()          

# List Operations 
prices.append(2500)                     
prices.remove(450)                      
prices.sort()                           

#Data Slicing 
top3 = prices[-3:][::-1]                 
lowest2 = prices[:2]                     
reversed_prices = prices[::-1]           

# Metrics
total = sum(prices)
average = sum(prices) / len(prices)
price_range = max(prices) - min(prices)

#Report
print("      STORE INVENTORY AUDIT REPORT")
print(f"Store ID       : {store_id}")
print(f"Category       : {category}")
print("====================")
print(f"Original Prices : {original_prices}")
print(f"After Updates   : {prices}")
print("====================")
print(f"Top 3 Premium Items  : {top3}")
print(f"Lowest 2 Budget Items : {lowest2}")
print(f"Reversed Price List  : {reversed_prices}")
print("====================")
print(f"Total Stock Value    : {total:.2f}")
print(f"Average Price / Item : {average:.2f}")
print(f"Price Range (Max-Min): {price_range:.2f}")
print("====================")
print("Audit Status: SUCCESSFUL")
print("====================")