"""def final_price(price,discount):
    discount=price*discount/100
    result=price-discount
    return result

print(final_price(100,10))"""

def final_price(price,discount):
    return price -price*discount/100
    
print(final_price(200,10))

