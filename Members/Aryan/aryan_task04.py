# Day 4: Dictionaries & Sets
# Name: Aryan
# What I learned today: Dictionary operations, sets and key-value handling



# Customer Loyalty Database
customers = {
    "C101": 150,
    "C102": 320,
    "C103": 80,
    "C104": 500
}


# Add New Customer
customers["C105"] = 200


# Update Existing Customer
customers["C101"] += 50


# Category List With Duplicate Values
categories = [
    "Electronics",
    "Fashion",
    "Electronics",
    "Home",
    "Fashion",
    "Books"
]


# Remove Duplicate Categories
unique_categories = set(categories)


# Metrics
total_customers = len(customers)
total_loyalty_points = sum(customers.values())
customer_c102_points = customers.get("C102", 0)


# Final Audit Report
print("CUSTOMER LOYALTY & CATEGORY AUDIT")
print("Total Customers Registered:", total_customers)
print("Unique Store Categories:", unique_categories)
print("Customer C102 Points:", customer_c102_points)
print("Updated Customer C101 Points:", customers["C101"])
print("Total System Loyalty Points:", total_loyalty_points)
print("Audit Status: SUCCESSFUL")