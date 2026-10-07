# Day 5: Functions, Arguments, Scope & Return
# Name: Divyansh
# What I learned today: functions, parameters/arguments, return value, local vs global scope
# Where I got stuck & fixed it: function ke local variable (price/final) ko bahar use kiya -> NameError; return value ko variable me store kiya

def claculate_final_price(price,discount_percent,tax_percent):
    discounted = price -(price * discount_percent/100)
    final = discounted+ (discounted *tax_percent/100)
    return round(final,2)


def get_delivery_status(order_total):
    if order_total >=1000:
        return "Eligible for free express delivery"
    else:
        return "Standerd shipping applied (Rs 50 extra)"
c1_price=1200
customer1 =claculate_final_price(price=c1_price,discount_percent=10,tax_percent=18)
customer1_status = get_delivery_status(customer1)
c2 = 800
customer2=claculate_final_price(price=c2,discount_percent=5,tax_percent=12)
c2_status=get_delivery_status(customer2)

print(f"""
========================================
   E-COMMERCE ORDER BILLING SYSTEM
========================================

--- CUSTOMER 01 INVOICE ---
Original Price: Rs {c1_price}
Final Bill Amount: Rs {customer1}
Delivery Status: {customer1_status}

--- CUSTOMER 02 INVOICE ---
Original Price: Rs {c1_price}
Final Bill Amount: Rs {c2_status}
Delivery Status: {c2_status}

========================================
Audit Status: SUCCESSFUL

""")