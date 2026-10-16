def HRA(salary_amount):
    HRA_amount=salary_amount * 20/100
    return HRA_amount
def tax(salary_amount):
    if salary_amount>50000:
        tax_amount= salary_amount * 10/100
        return tax_amount
    else:
        tax_amount = salary_amount*5/100
        return tax_amount

def Salary_calculation(salary_amount):
    return salary_amount + HRA(salary_amount) -tax(salary_amount)

print(Salary_calculation(50000))