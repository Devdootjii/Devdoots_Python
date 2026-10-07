# Day 5: Functions, Arguments & Return Values
# Name: Balram Singh
# What I learned today: functions banana, arguments pass karna aur return value handle karna
# Where I got stuck & fixed it: return value ko main execution me variables me store karna tha

# function 1: final price calculator
def calculate_final_price(price, discount_percent, tax_percent):
    # discount amount calculate karke minus kiya
    discount_amt = price * (discount_percent / 100)
    discounted_price = price - discount_amt
    
    # tax amount calculate karke add kiya
    tax_amt = discounted_price * (tax_percent / 100)
    final_price = discounted_price + tax_amt
    
    # 2 decimal places tak round karke return kiya
    return round(final_price, 2)

# function 2: delivery status evaluator
def get_delivery_status(order_total):
    if order_total >= 1000:
        return "ELIGIBLE FOR FREE EXPRESS DELIVERY"
    else:
        return "STANDARD SHIPPING APPLIED (Rs 50 Extra)"

# customer 1 input data
c1_price = 1200.0
c1_discount = 10
c1_tax = 18

# customer 2 input data
c2_price = 800.0
c2_discount = 5
c2_tax = 12

# function calling and return values store karna
c1_final_price = calculate_final_price(c1_price, c1_discount, c1_tax)
c1_status = get_delivery_status(c1_final_price)

c2_final_price = calculate_final_price(c2_price, c2_discount, c2_tax)
c2_status = get_delivery_status(c2_final_price)

# terminal report display
print("=" * 40)
print("   E-COMMERCE ORDER BILLING SYSTEM")
print("=" * 40)

print("\n--- CUSTOMER 01 INVOICE ---")
print("Original Price: Rs", c1_price)
print("Final Bill Amount: Rs", c1_final_price)
print("Delivery Status:", c1_status)

print("\n--- CUSTOMER 02 INVOICE ---")
print("Original Price: Rs", c2_price)
print("Final Bill Amount: Rs", c2_final_price)
print("Delivery Status:", c2_status)

print("\n" + "=" * 40)
print("Audit Status: SUCCESSFUL")