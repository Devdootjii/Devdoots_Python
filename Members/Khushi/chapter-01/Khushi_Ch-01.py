#functions
#name: khushi
#where i stuck: tax nikalne me
def hra(basic_salary):
  hra = basic_salary * 20 / 100
  return(hra)

def tax(salary):
  if salary > 50000:
      tax_amount = salary * 10 / 100
  else:
      tax_amount = salary * 5 / 100
      return(tax_amount)

def netsalary(basic_salary, hra):
  total = basic_salary + hra
  netsalary = total - tax
  return(netsalary)

p2 = netsalary(50000)
p3 = netsalary(60000)
print("p2 netsalary:",p2)
print("p3 netsalary:",p3)
