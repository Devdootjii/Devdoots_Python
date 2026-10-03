#Day 1 = control flow and logic
#name = khushi yadav
#what i learned today =input , typecasting ,
#    variable , airthmatic operators , comparison operators ,logical operators (and or not)
# if ,elif , else 
#where i got stuck and fixed it : multiple discount conditions

amount = float(input("Enter Cart Amount: ₹"))
customer = input("Customer Type (student/senior/regular): ").lower()
vip = input("VIP Member? (yes/no): ").lower()

if amount <= 0:
    print("Invalid amount! value must be greater than 0.")
else:
    if amount >= 5000:
        base = 20
    elif amount >= 2000:
        base = 10
    else:
        base = 0

    extra = 0

    if customer == "student" or customer == "senior":
        extra += 5

    if vip == "yes" and amount > 1000:
        extra += 5

    total_discount = base + extra
    discount = amount * total_discount / 100
    after_discount = amount - discount
    gst = after_discount * 18 / 100
    final = after_discount + gst

    print("\n========== SMART BILLING RECEIPT ==========")
    print(f"Original Price     = ₹{amount:.2f}")
    print(f"Customer Type      = {customer.title()}")
    print(f"VIP Member         = {vip.title()}")
    print("-------------------------------------------")
    print(f"Base Discount      = {base}%")
    print(f"Extra Discount     = {extra}%")
    print(f"Total Discount     = {total_discount}%")
    print(f"Discount Amount    = -₹{discount:.2f}")
    print(f"Price After Discount= ₹{after_discount:.2f}")
    print(f"GST Tax (18%)      = +₹{gst:.2f}")
    print("===========================================")
    print(f"FINAL PAYABLE AMOUNT= ₹{final=.2f}")
    print("Thank you for shopping with us!")
