# Day 1: Control Flow & Logic
# Name: Balram Singh
# What I learned today: Typecasting, conditional statements (if-elif-else), and receipt formatting.
# Where I got stuck & fixed it: Ensured GST is calculated on discounted price instead of original amount.

# 1. Inputs
cart = float(input("Enter Total Cart Amount: "))

# Rule 1: Validation
if cart <= 0:
    print("Invalid Amount! Value must be greater than 0.")
    exit()

cust_type = input("Enter Customer Type (student, senior, regular): ").strip().lower()
is_vip = input("Is VIP Member? (yes/no): ").strip().lower()

# Rule 2: Base Discount
if cart >= 5000:
    base_discount = 20
elif cart >= 2000:
    base_discount = 10
else:
    base_discount = 0

# Rule 3: Additional Discounts
extra_discount = 0
reasons = []

if cust_type in ["student", "senior"]:
    extra_discount += 5
    reasons.append(cust_type.capitalize())

if is_vip == "yes" and cart > 1000:
    extra_discount += 5
    reasons.append("VIP")

# Rule 4: Final Math & Tax
total_discount_rate = base_discount + extra_discount
discount_amount = cart * (total_discount_rate / 100)
price_after_discount = cart - discount_amount
gst_tax = price_after_discount * 0.18
final_amount = price_after_discount + gst_tax

# Output Labels
extra_label = f"{extra_discount}% ({' + '.join(reasons)})" if reasons else "0%"
vip_label = "Yes" if is_vip == "yes" else "No"

# Receipt Print
print(f"""
=======================================
        SMART BILLING RECEIPT          
=======================================
Original Price     : ₹{cart:.2f}
Customer Type      : {cust_type.capitalize()}
VIP Member         : {vip_label}
=============================================
---------------------------------------
Base Discount      : {base_discount}%
Extra Discount     : {extra_label}
Total Discount Rate: {total_discount_rate}%
Discount Amount    : -₹{discount_amount:.2f}
---------------------------------------
Price After Discount: ₹{price_after_discount:.2f}
GST Tax (18%)      : +₹{gst_tax:.2f}
=======================================
FINAL PAYABLE AMOUNT: ₹{final_amount:.2f}
=======================================
Thank you for shopping with us!""")