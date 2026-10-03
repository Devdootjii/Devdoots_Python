
print("        SMART BILLING RECEIPT")

amount = float(input("Enter Total Cart Amount: "))
customer_type = input("Customer Type (student/senior/regular): ").lower()
vip = input("Is VIP Member? (yes/no): ").lower()

if amount <= 0:
    print("Invalid Amount! Value must be greater than 0.")
else:
    if amount >= 5000:
        base_discount = 20
    elif amount >= 2000:
        base_discount = 10
    else:
        base_discount = 0

    extra_discount = 0
    if customer_type == "student" or customer_type == "senior":
        extra_discount = extra_discount + 5
    if vip == "yes" and amount > 1000:
        extra_discount = extra_discount + 5

    total_discount = base_discount + extra_discount
    discount_amount = amount * total_discount / 100
    price_after = amount - discount_amount
    gst = price_after * 0.18
    final_amount = price_after + gst

    print(f"Original Price      : ₹{amount:.2f}")
    print(f"Customer Type       : {customer_type.title()}")
    print(f"VIP Member          : {vip.title()}")
    print(f"Total Discount Rate : {total_discount}%")
    print(f"Discount Amount     : -₹{discount_amount:.2f}")
    print(f"Price After Discount: ₹{price_after:.2f}")
    print(f"GST Tax (18%)       : +₹{gst:.2f}")
    print(f"FINAL PAYABLE AMOUNT: ₹{final_amount:.2f}")
    print("Thank you for shopping with us!")
