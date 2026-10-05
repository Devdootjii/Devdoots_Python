# Day03
#Name : Divyansh
#what i learned: for loop , tuples,lists,builtin function
#where i stuck : Write the proper logic of for list with append
print(f"""
=======================================
      STORE INVENTORY AUDIT REPORT     
=======================================
""")
STORE_INFO = ("STR-8092","Electronic & Retail")
print(f"""
Store ID       : {STORE_INFO[0]}
Category       : {STORE_INFO[1]}
---------------------------------------
""")

Products =[1200,450,8900,3200,15000,650]
print(f"""
Original Prices : {Products}""")

item = int(input("Enter Updated Product Prices:"))
Products.append(item)
Products.sort()
print(f"""
After Updates   : {Products}
---------------------------------------
""")
Products.remove(min(Products))

maximum = Products[-3:]
minimum = Products[:2]
reversed_list = Products[::-1]
total=sum(Products)
Item_count=len(Products)
ave = total/Item_count
Range=max(Products) - min(Products)

print(f"""
Top 3 Premium Items  : {maximum}
Lowest 2 Budget Items : {minimum}
Reversed Price List   : {reversed_list}
---------------------------------------
Total Stock Value    : ₹{total:.2f}
Average Price / Item : ₹{ave:.2f}
Price Range (Max-Min): ₹{Range:.2f}
=======================================
Audit Status: SUCCESSFUL
=======================================
""")