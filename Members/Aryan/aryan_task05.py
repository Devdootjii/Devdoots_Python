# Day 5: Functions, Arguments, Scope & Return Values
# Name: Aryan
# What I learned today: Functions, parameters, arguments and return values



#  Final Price Calculator
def calculate_final_price(price, discount_percent, tax_percent):
    discounted_price = price - (price * discount_percent / 100)
    final_price = discounted_price + (discounted_price * tax_percent / 100)
    return round(final_price, 2)


#  Delivery Status Evaluator
def get_delivery_status(order_total):
    if order_total >= 1000:
        return "ELIGIBLE FOR FREE EXPRESS DELIVERY"
    else:
        return "STANDARD SHIPPING APPLIED (₹50 Extra)"


# Customer 01
customer1_price = 1200
customer1_discount = 10
customer1_tax = 18

customer1_final = calculate_final_price(
    customer1_price,
    customer1_discount,
    customer1_tax
)


# Customer 02
customer2_price = 800
customer2_discount = 5
customer2_tax = 12

customer2_final = calculate_final_price(
    customer2_price,
    customer2_discount,
    customer2_tax
)


# Final Report
print("================================")
print("E-COMMERCE ORDER BILLING SYSTEM")
print("================================")

print("\n--- CUSTOMER 01 INVOICE ---")
print("Original Price: ₹", customer1_price)
print("Final Bill Amount: ₹", customer1_final)
print("Delivery Status:", get_delivery_status(customer1_final))

print("\n--- CUSTOMER 02 INVOICE ---")
print("Original Price: ₹", customer2_price)
print("Final Bill Amount: ₹", customer2_final)
print("Delivery Status:", get_delivery_status(customer2_final))

print("\n================================")
print("Audit Status: SUCCESSFUL")