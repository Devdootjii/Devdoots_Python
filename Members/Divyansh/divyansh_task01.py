# Day 1: Control Flow & Logic
# Name: Divyansh
# What I learned today: if/elif/else aur logical operators se discount logic banana
# Where I got stuck & fixed it: "or" ki galti, aur discount rate vs discount amount ka confusion


Total_Cart_Amount = float(input("Enter Cart Value : "))
Coustomer_type = input("Choose coustomer type (student / senior / regular): ")
VIP = input("Are you a VIP (yes/no): ")

if Total_Cart_Amount <= 0:
    print("Invalid Amount! Value must be greater than 0.")

else:
    
    if Total_Cart_Amount >= 5000:
        Base_discount = 0.20
    elif Total_Cart_Amount >= 2000:
        Base_discount = 0.10
    else:
        Base_discount = 0.0

    Special_discount = 0.0
    if Coustomer_type == "student" or Coustomer_type == "senior":
        Special_discount = 0.05

    Extra_discount = 0.0
    if VIP == "yes" and Total_Cart_Amount > 1000:
        Extra_discount = 0.05

    total_discount = Base_discount + Special_discount + Extra_discount
    Discount_Amount = Total_Cart_Amount * total_discount
    Amount_After_Discount = Total_Cart_Amount - Discount_Amount
    GST = Amount_After_Discount * 0.18
    Final_payable = Amount_After_Discount + GST

    print("=======================================")
    print("        SMART BILLING RECEIPT")
    print("=======================================")
    print(f"{'Original Price':<20}: Rs.{Total_Cart_Amount:.2f}")
    print(f"{'Customer Type':<20}: {Coustomer_type}")
    print(f"{'VIP Member':<20}: {VIP}")
    print("---------------------------------------")
    print(f"{'Base Discount':<20}: {Base_discount * 100:.0f}%")
    print(f"{'Extra Discount':<20}: {Extra_discount * 100:.0f}%")
    print(f"{'Total Discount Rate':<20}: {total_discount * 100:.0f}%")
    print(f"{'Discount Amount':<20}: -Rs.{Discount_Amount:.2f}")
    print("---------------------------------------")
    print(f"{'Price After Discount':<20}: Rs.{Amount_After_Discount:.2f}")
    print(f"{'GST Tax (18%)':<20}: +Rs.{GST:.2f}")
    print("=======================================")
    print(f"FINAL PAYABLE AMOUNT: Rs.{Final_payable:.2f}")
    print("=======================================")
    print("Thank you for shopping with us!")