def discount_rate(amount):
    if amount >= 5000:
        return 20
    elif amount >= 2000:
        return 10
    else:
        return 0

def final_price(price, discount_percent):
    discount = price * discount_percent / 100  
    final_price = price - discount
    return final_price

for amount in (6000, 3000, 5000, 500):
    rate = discount_rate(amount)     
    print(amount, "->", rate, "->", final_price(amount, rate))
