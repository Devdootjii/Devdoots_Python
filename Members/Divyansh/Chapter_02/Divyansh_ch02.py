def discount_rate(amount):
    if amount >=5000 :
        return 20
    elif amount >=2000:
        return 10
    else:
        return 0

def final_price(price,discount_percent):
    return price- price*discount_percent/100
amount = 6000
rate= discount_rate(amount)
print(final_price(amount,rate))
amount1 = 3000
rate= discount_rate(amount1)
print(final_price(amount1,rate))
amount2 = 5000
rate= discount_rate(amount2)
print(final_price(amount2,rate))
amount3 = 500
rate= discount_rate(amount3)
print(final_price(amount3,rate))