import sys

try:
    cart_amount = float(input("Enter the cart amount: "))
except ValueError:
    print("Invalid Inputs! Value must be a number.")
    sys.exit()

if cart_amount <= 0:
    print("Invalid Inputs! Value must be greater than 0.")
    sys.exit()

customer_type = input("Enter customer Type ( student, senior, or regular): ").strip().lower()
is_vip = input("Is VIP Member? (yes or no): ").strip().lower()

if cart_amount >= 5000:
    base_discount = 20
elif cart_amount >= 2000:
    base_discount = 10
else:
    base_discount = 0

extra_discount = 0
extra_reasons = []

if customer_type == "student" or customer_type == "senior":
    extra_discount += 5
    extra_reasons.append(customer_type.capitalize())

if is_vip == "yes" and cart_amount > 1000:
    extra_discount += 5
    extra_reasons.append("VIP")

if extra_reasons:
    extra_text = f"{extra_discount}% (" + " + ".join(extra_reasons) + ")"
else:
    extra_text = "0%"

total_discount_rate = base_discount + extra_discount
discount_amount = cart_amount * (total_discount_rate / 100)
discounted_price = cart_amount - discount_amount
gst_tax = discounted_price * 0.18
final_payable_amount = discounted_price + gst_tax

print("\n=======================================")
print("        SMART BILLING RECEIPT          ")
print("=======================================")
print(f"Original Price     : ₹{cart_amount:.2f}")
print(f"Customer Type      : {customer_type.capitalize()}")
print(f"VIP Member         : {'Yes' if is_vip == 'yes' else 'No'}")
print("---------------------------------------")
print(f"Base Discount      : {base_discount}%")
print(f"Extra Discount     : {extra_text}")
print(f"Total Discount Rate: {total_discount_rate}%")
print(f"Discount Amount    : -₹{discount_amount:.2f}")
print("---------------------------------------")
print(f"Price After Discount: ₹{discounted_price:.2f}")
print(f"GST Tax (18%)      : +₹{gst_tax:.2f}")
print("=======================================")
print(f"FINAL PAYABLE AMOUNT: ₹{final_payable_amount:.2f}")
print("=======================================")
print("Thank you for shopping with us!\n")
