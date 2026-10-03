# Name : Aryan
# Day 01: Control Flow & Logic
# Task: Smart E-Commerce Billing System

import sys

# User Inputs
cart_amount = float(input("Enter Total Cart Amount: ₹"))
customer_type = input(
    "Enter Customer Type (student/senior/regular): "
).strip().lower()
vip_member = input("Are you a VIP Member? (yes/no): ").strip().lower()


#  Invalid Amount Check
if cart_amount <= 0:
    print("Invalid Amount! Value must be greater than 0.")
    sys.exit()


#  Base Discount
if cart_amount >= 5000:
    base_discount_rate = 20
elif cart_amount >= 2000:
    base_discount_rate = 10
else:
    base_discount_rate = 0


#  Special Additional Discounts
extra_discount_rate = 0

# Student OR Senior → Extra 5%
if customer_type == "student" or customer_type == "senior":
    extra_discount_rate += 5

# VIP AND Cart Amount > 1000 → Extra 5%
if vip_member == "yes" and cart_amount > 1000:
    extra_discount_rate += 5


# Total Discount
total_discount_rate = base_discount_rate + extra_discount_rate

discount_amount = cart_amount * total_discount_rate / 100

price_after_discount = cart_amount - discount_amount


#  GST Calculation
gst_rate = 18
gst_amount = price_after_discount * gst_rate / 100

final_payable_amount = price_after_discount + gst_amount


# Final Receipt
print("\n========================================")
print("          SMART BILLING RECEIPT")
print("========================================")
print(f"Original Price       : ₹{cart_amount:.2f}")
print(f"Customer Type        : {customer_type.title()}")
print(f"VIP Member           : {vip_member.title()}")
print("----------------------------------------")
print(f"Base Discount Rate   : {base_discount_rate}%")
print(f"Extra Discount Rate  : {extra_discount_rate}%")
print(f"Total Discount Rate  : {total_discount_rate}%")
print(f"Discount Amount      : ₹{discount_amount:.2f}")
print("----------------------------------------")
print(f"Price After Discount : ₹{price_after_discount:.2f}")
print(f"GST Rate             : {gst_rate}%")
print(f"GST Amount           : ₹{gst_amount:.2f}")
print("----------------------------------------")
print(f"FINAL PAYABLE AMOUNT : ₹{final_payable_amount:.2f}")
print("========================================")
print("Thank you for shopping with us")