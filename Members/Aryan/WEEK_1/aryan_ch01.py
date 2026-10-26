def HRA(salary):
    hra = salary * 0.20
    return hra


def tax(salary):
    if salary >= 50000:
        tax_amount = salary * 0.1
    else:
        tax_amount = salary * 0.05

    return tax_amount


def net_salary(salary):
    net_salary = salary + HRA(salary) - tax(salary)
    return net_salary


print(net_salary(50000))
print(net_salary(40000))
print(net_salary(45000))