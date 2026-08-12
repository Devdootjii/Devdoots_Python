cart = [
    {"item": "sensor", "price": 1200, "qty": 2},
    {"item": "Microcontroller", "price": 2500, "qty": 1},
    {"item": "Motor", "price": 450, "qty": 4}
]

def generate_bill(cart, coupon_code):
    subtotal = 0
    for item in cart:
        subtotal += item["price"] * item["qty"]
    if coupon_code == "DEVDOOT10":
        discount = subtotal * 0.10
    else:
        discount = 0
    discounted_amount = subtotal - discount
    gst = discounted_amount * 0.18
    final_amount = discounted_amount + gst

    receipt = f"""
Subtotal: ${subtotal:.2f}
Discount: ${discount:.2f}
GST (18%): ${gst:.2f}
Final Amount: ${final_amount:.2f}
"""
    return receipt

bill = generate_bill(cart, "DEVDOOT10")
print(bill)
