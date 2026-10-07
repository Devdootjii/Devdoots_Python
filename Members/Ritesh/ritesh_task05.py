# Day 5: Functions, Arguments, Scope & Return Values
# Name: Ritesh
# What I learned today: Modular function design, passing parameters, returning values, and variable scoping.
# Where I got stuck & fixed it: Chained output of price calculation function into delivery status function.

# Function 1: Final Price Calculator
def calculate_final_price(price, discount_percent, tax_percent):
    discounted_price = price - (price * (discount_percent / 100))
    final_price = discounted_price + (discounted_price * (tax_percent / 100))
    return round(final_price, 2)

# Function 2: Delivery Status evaluator
def get_delivery_status(order_total):
    if order_total >=1000:
        return "eligible for free delivery"
    else:
        return " standard shipping applied ( Rs 50 Extra )"

    # Execution : Customer Datasets
c1_price =1200.0
c1_discount =10
c1_tax = 18

c2_price = 800.0
c2_discount = 5
c2_tax = 12

# processing calculations through functions
c1_final_price = calculate_final_price(c1_price , c1_discount, c1_tax)
c1_delivery_status = get_delivery_status(c1_final_price)

c2_final_price = calculate_final_price(c2_price, c2_discount, c2_tax)
c2_delivery_status = get_delivery_status(c2_final_price)

# Terminal Output

print("========================================")
print("   E-COMMERCE ORDER BILLING SYSTEM      ")
print("========================================")

print("--- CUSTOMER 01 INVOICE ---")
print(f"Original Price: Rs {c1_price}")
print(f"Final Bill Amount: Rs {c1_final_price}")
print(f"Delivery Status: {c1_delivery_status}")

print("--- CUSTOMER 02 INVOICE ---")
print(f"Original Price: Rs {c2_price}")
print(f"Final Bill Amount: Rs {c2_final_price}")
print(f"Delivery Status: {c2_delivery_status}")

print("========================================")
print("Audit Status: SUCCESSFUL")
 