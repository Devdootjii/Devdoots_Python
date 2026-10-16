# Day 4: Dictionaries & Sets
# Name: Ritesh
# What I learned today: Dictionary key-value operations, safe lookup using .get(), and deduplication using sets.
# Where I got stuck & fixed it: Calculated total points sum across all customers using sum(loyalty_db.values()).
# Step 1: Customer Loyalty Database (Dictionary)
loyalty_db = {"C101": 150, "C102": 320, "C103": 80, "C104": 500}

# Step 2: Add New Customer
loyalty_db["C105"] = 200

# Step 3: Update Existing Customer
loyalty_db["C101"] = loyalty_db["C101"] + 50

# Step 4: Unique Category Extraction (Set)
raw_tags = ["Electronics", "Fashion", "Home", "Home", "Fashion", "Books"]
unique_categories = set(raw_tags)

# Step 5: Metrics
total_customers = len(loyalty_db)
total_points = sum(loyalty_db.values())
c102_points = loyalty_db.get("C102", 0)

# Terminal Output
print("CUSTOMER LOYALTY & CATEGORY AUDIT")
print("Total Customers Registered:", total_customers)
print("Unique Store Categories:", unique_categories)
print("Customer C102 Points:", c102_points)
print("Updated Customer C101 Points:", loyalty_db["C101"])
print("Total System Loyalty Points:", total_points)
print("Audit Status: SUCCESSFUL")

