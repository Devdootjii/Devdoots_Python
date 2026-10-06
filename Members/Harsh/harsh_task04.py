# Day 4: Dictionaries & Sets
# Name: Harsh Rajbhar
# What I learned today: dictionary operations aur set se duplicate hatana
# Where I got stuck & fixed it: dict values ka sum calculate karna tha

loyalty_db = {"C101": 150, "C102": 320, "C103": 80, "C104": 500}

loyalty_db["C105"] = 200

loyalty_db["C101"] = loyalty_db["C101"] + 50

raw_tags = ["Electronics", "Fashion", "Electronics", "Home", "Fashion", "Books"]

unique_categories = set(raw_tags)

total_cust = len(loyalty_db)
total_points = sum(loyalty_db.values())
c102_points = loyalty_db.get("C102", 0)

print("CUSTOMER LOYALTY & CATEGORY AUDIT")
print("Total Customers Registered:", total_cust)
print("Unique Store Categories:", unique_categories)
print("Customer C102 Points:", c102_points)
print("Updated Customer C101 Points:", loyalty_db["C101"])
print("Total System Loyalty Points:", total_points)
print("Audit Status: SUCCESSFUL")
