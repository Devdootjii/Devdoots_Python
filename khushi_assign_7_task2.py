#product ={
#  "product" : "monitor",
#  "price"   : 12000,
#  "quantity" : 2
#}
#print(product["price"])
#print(product["quantity"])
#total = product["price"] * product["quantity"]
#print(total)
#product ={
#  "product" : "keyboard",
#  "price"  :  800,
#  "quantity" : 3
#}

#print(product["price"])
#print(product["quantity"])
#total = product["price"]* product["quantity"]
#print(total)

#product = {
#   "product" :"keyboard",
#   "price" : 1500, 
#   "quantity" : 2
#}
#print(product["product"])
# print(product["price"])
# print(product["quantity"])
# total = product["price"]* product["quantity"]
# print(total)

#cart = [
#    {
#       "product" : "monitor",

#      "price" : 12000,

#       "quantity" :2

#     },

#{

#       "product" : "mouse",

#"price" : 450,

#      "quantity" : 4

#     }
#      ]
#monitor_total = cart[0]["price"] * cart[0]["quantity"]
#mouse_total = cart[1]["price"] * cart[1]["quantity"]
#subtotal = monitor_total + mouse_total
#print(subtotal)

#coupon_code ="DEVDOOT10"
#if coupon_code == "DEVDOOT10":
#  discount = subtotal * 10/100
#  after_discount = subtotal - discount
#  print(after_discount)

# gst = after_discount * 18/100
#  final_bill = after_discount + gst
#  print(final_bill)
#def generate_bill(cart, coupon_code):
#    print("Billing started")
#generate_bill(cart, coupon_code)

#def generate_bill(cart, coupon_code):
#   monitor_total = cart[0]["price"] * cart[0]["quantity"]
#    mouse_total = cart[1]["price"] * cart[1]["quantity"]
#    subtotal = monitor_total + mouse_total

#    print(subtotal)
#generate_bill(cart, coupon_code) 

cart = [
    {
        "product": "monitor",
        "price": 12000,
        "quantity": 2
    },
    {
        "product": "mouse",
        "price": 450,
        "quantity": 4
    }
]


def generate_bill(cart, coupon_code):

    monitor_total = cart[0]["price"] * cart[0]["quantity"]
    mouse_total = cart[1]["price"] * cart[1]["quantity"]

    subtotal = monitor_total + mouse_total
    print(subtotal)

    if coupon_code == "DEVDOOT10":
        discount = subtotal * 10 / 100

    after_discount = subtotal - discount

    gst = after_discount * 18 / 100

    final_bill = after_discount + gst

    print("Subtotal:", subtotal)
    print("Discount:", discount)
    print("After Discount:", after_discount)
    print("GST:", gst)
    print("Final Bill:", final_bill)


coupon_code = "DEVDOOT10"

generate_bill(cart, coupon_code)   


