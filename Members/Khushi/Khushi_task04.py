# Day 4: Dictionaries & Sets
# Name: Khushi 
# What I learned today: dictionary ,dictonary updatr,sets,data aggregayion
# Where I got stuck & fixed it: dict values ka sum calculate karna

# customer loyalty database
loyalty_db = {
    "C101": 150, 
    "C102": 320,
    "C103": 80,
    "C104": 500
}

# new customer add
loyalty_db["C105"] = 200

# existing customer point update
loyalty_db["C101"] = loyalty_db["C101"] + 50

# raw category list with duplicates
raw_tags = [
    "Electronics",
    "Fashion",
    "Electronics",
    "Home",
    "Fashion",
    "Books"
]

# set filtering unique values
unique_categories = set(raw_tags)

# metrics calculation
total_cust = len(loyalty_db)
total_points = sum(loyalty_db.values())
c102_points = loyalty_db.get("C102", 0)

print("CUSTOMER LOYALTY & CATEGORY AUDIT")
print("Total Customers Registered:", total_cust)
print("Unique Store Categories:", unique_categories)
print("Customer C102 Points:", c102_points)
print("Upd:ated customer 101 points:", loyalty_db["C101"])
print("Total system loyalty points:", total_points)
print("Audit status: SUCCESSFUL")
