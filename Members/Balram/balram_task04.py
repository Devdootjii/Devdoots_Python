# Day 4: Dictionaries & Sets
# Name: Balram Singh
# What I learned today: dictionary aur set ka basic use
# Where I got stuck & fixed it: dict values ka sum nikalna tha

# customer loyalty points database
loyalty_db = {"C101": 150, "C102": 320, "C103": 80, "C104": 500}

# new customer add kiya
loyalty_db["C105"] = 200

# existing customer point update
loyalty_db["C101"] = loyalty_db["C101"] + 50

# raw category list with duplicates
raw_tags = ["Electronics", "Fashion", "Electronics", "Home", "Fashion", "Books"]

# set filtering unique values
unique_categories = set(raw_tags)

# metrics calculation
total_cust = len(loyalty_db)
total_points = sum(loyalty_db.values())
c102_points = loyalty_db.get("C102", 0)

# Exact output print as given in Task 4 document
print("CUSTOMER LOYALTY & CATEGORY AUDIT\n")
print("Total Customers Registered:", total_cust)
print("Unique Store Categories:", unique_categories)
print("Customer C102 Points:", c102_points)
print("Updated Customer C101 Points:", loyalty_db["C101"])
print("Total System Loyalty Points:", total_points)
print("Audit Status: SUCCESSFUL")