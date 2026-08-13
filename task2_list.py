# prduct list
prodcts = [("Laptop", 50000, 4.5), ("Mouse", 500, 3.8), ("Keyboard", 1500, 4.2), ("Monitor", 12000, 4.7)]

# part a - filter
for p in prodcts:
    if p[2] >= 4.0:
        print(f"{p[0]} rating achi hai")

# part b - manual max search
max_prce = 0
exp_item = ""

for p in prodcts:
    if p[1] > max_prce:
        max_prce = p[1]
        exp_item = p[0]

print(f"Sabse mehanga: {exp_item} price {max_prce}")