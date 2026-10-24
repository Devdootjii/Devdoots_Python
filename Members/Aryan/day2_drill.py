# P1 - List ka sum 
a = [10, 20, 30, 40, 50]
total = 0

for n in a:
    total += n

print(total)


# P2 - List ka maximum 
a = [10, 20, 30, 40, 50]
mx = a[0]

for n in a:
    if n > mx:
        mx = n

print(mx)


# P3 - List ko reverse print 
a = [10, 20, 30, 40, 50]

for i in range(len(a) - 1, -1, -1):
    print(a[i], end=" ")

print()


# P4 - element ko swap 
a = [10, 20, 30, 40, 50]

a[0], a[4] = a[4], a[0]

print(a)


# P5 - Search function
def search(a, target):
    for i in range(len(a)):
        if a[i] == target:
            return i
    return -1

a = [10, 20, 30, 40, 50]

print(search(a, 30))
print(search(a, 99))


# P6 - Even numbers count 
a = [3, 8, 5, 12, 7, 4]
count = 0

for n in a:
    if n % 2 == 0:
        count += 1

print(count)


# D1 - program debug 
a = [10, 20, 30]
mx = a[0]

for n in a:
    if n > mx:
        mx = n

print(mx)


# D2 - debug 
a = [1, 2, 3]

for i in range(len(a) - 1, -1, -1):
    print(a[i], end=" ")

print()


# R1 
def sum_to(n):
    if n == 1:
        return 1
    return n + sum_to(n - 1)

print(sum_to(5))  


# R2 
def power(a, b):
    if b == 0:
        return 1
    return a * power(a, b - 1)

print(power(2, 3))  