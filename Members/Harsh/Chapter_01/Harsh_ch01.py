def calculate_hra(salary):
    hra=salary*20/100
    return hra 

def calculate_tax(salary):
    if salary>50000:
        tax=salary*10/100
    else:
        tax=salary*5/100
        return tax

def net_salary(salary):
    hra=calculate_hra(salary)
    tax=calculate_tax(salary)

    return salary + hra - tax

for s in [40000, 50000, 80000]:
    print(s, "->", net_salary(s))
