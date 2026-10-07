#day05 task completed
#name = Khushi
#what i learned today: function, function calling, parameters,arguments,return,local and global variables,code reuasablilty
#Where I got stuck and fixed it: Ye samajhne mein thodi problem hui ki ek function ka answer (return value)  doosre function ke andar kaise jaata hai fir code ko line by line dry-run karke samajh liya ki final_bill1 seedha delivery status check karne ke liye kaise use ho raha hai.

def calculate_final_price(price, discount_percent, tax_percent):
    discount_amount = price * discount_percent / 100
    discounted_price = price - discount_amount
    tax_amount = discounted_price * tax_percent / 100
    final_price = discounted_price + tax_amount
    return round(final_price, 2)

def get_delivery_status(order_total):
    if order_total >= 1000:
        return "ELIGIBLE FOR FREE EXPRESS DELIVERY"
    else:
        return "STANDARD SHIPPING APPLIED (Rs 50 Extra)"

print("========================================")
print(" E-COMMERCE ORDER BILLING SYSTEM")
print("========================================")

# Customer 1
price1 = 1200
discount1 = 10
tax1 = 18

final_bill1 = calculate_final_price(price1, discount1, tax1)
status1 = get_delivery_status(final_bill1)

print("--- CUSTOMER 01 INVOICE ---")
print("Original Price: Rs", float(price1))
print("Final Bill Amount: Rs", final_bill1)
print("Delivery Status:", status1)

# Customer 2
price2 = 800
discount2 = 5
tax2 = 12
final_bill2 = calculate_final_price(price2, discount2, tax2)
status2 = get_delivery_status(final_bill2)

print("--- CUSTOMER 02 INVOICE ---")
print("Original Price: Rs", float(price2))
print("Final Bill Amount: Rs", final_bill2)
print("Delivery Status:", status2)
print("========================================")
print("Audit Status: SUCCESSFUL")
