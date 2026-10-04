# Day 1: Control Flow & Logic
# Name: Khushi 
# what i learned today : input, typecasting, variable, comparison operators, comparison operators(and or not) if,else,elif
# where i got stuck and fixed it: multiple discount conditions  


# ---------- INPUT ----------
amount = float(input("Enter Cart Amount: ₹"))
customer = input("Customer Type (student/senior/regular): ").lower()
vip = input("VIP Member? (yes/no): ").lower()


# --------- INVALID AMOUNT ----------
if amount <= 0:
    print("Invalid Amount! Value must be greater than 0.")


else:
# ---------- BASE DISCOUNT ----------
    if amount >= 5000:
        base_discount = 20
    elif amount >= 2000:
        base_discount = 10 
    else:
        base_discount = 0

# --------- EXTRA DISCOUNT ----------
    extra_discount = 0

    if customer == "student" or customer == "senior":
        extra_discount += 5

    if vip == "yes" and amount > 1000:
        extra_discount += 5

# -------- TOTAL DISCOUNT ----------
    total_discount = base_discount + extra_discount

# --------- DISCOUNT AMOUNT ----------
    discount = amount * total_discount / 100

# -------- PRICE AFTER DISCOUNT ----------
    after_discount = amount - discount
    gst = after_discount * 18 / 100
    final = after_discount + gst

    # ---------- BILL / RECEIPT ----------

print("=======================================")
print("        SMART BILLING RECEIPT")
print("=======================================")

print("Original Price       : ₹", amount)
print("Customer Type        :", customer.title())
print("VIP Member           :", vip.title())

print("---------------------------------------")

print("Base Discount        :", base_discount, "%")
print("Extra Discount       :", extra_discount, "%")
print("Total Discount Rate  :", total_discount, "%")
print("Discount Amount      : -₹", discount)

print("---------------------------------------")

print("Price After Discount :", after_discount)
print("GST Tax (18%)        : +₹", gst)

print("=======================================")
print("FINAL PAYABLE AMOUNT :₹", final)
print("=======================================")

print("Thank you for shopping with us!")