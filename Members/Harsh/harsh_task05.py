# Day 5: Functions, Arguments, Scope & Return Values
# Name: Harsh Rajbhar
# What I learned today: functions banana, parameters/arguments aur return values
# Where I got stuck & fixed it: print ki jagah return use karna tha

# --- Function 1: Final Price Calculator ---
def calculate_final_price(price, discount_percent, tax_percent):
    discounted = price - (price * discount_percent / 100)
    final = discounted + (discounted * tax_percent / 100)
    return round(final, 2)

# --- Function 2: Delivery Status Evaluator ---
def get_delivery_status(order_total):
    if order_total >= 1000:
        return "ELIGIBLE FOR FREE EXPRESS DELIVERY"
    else:
        return "STANDARD SHIPPING APPLIED (Rs 50 Extra)"

# --- Main Execution ---
print("========================================")
print("   E-COMMERCE ORDER BILLING SYSTEM")
print("========================================")

# --- Customer 1 ---
c1_price = 1200.0
c1_final = calculate_final_price(c1_price, 10, 18)
print("\n--- CUSTOMER 01 INVOICE ---")
print(f"Original Price: Rs {c1_price}")
print(f"Final Bill Amount: Rs {c1_final}")
print(f"Delivery Status: {get_delivery_status(c1_final)}")

# --- Customer 2 ---
c2_price = 800.0
c2_final = calculate_final_price(c2_price, 5, 12)
print("\n--- CUSTOMER 02 INVOICE ---")
print(f"Original Price: Rs {c2_price}")
print(f"Final Bill Amount: Rs {c2_final}")
print(f"Delivery Status: {get_delivery_status(c2_final)}")

print("\n========================================")
print("Audit Status: SUCCESSFUL")
