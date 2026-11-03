#Problam=1
#List Comprehensions

x = int(input())
y = int(input())
z = int(input())
n = int(input())

print([[i, j, k]
       for i in range(x + 1)
       for j in range(y + 1)
       for k in range(z + 1)
       if i + j + k != n])

#Problam=2
#Runner-Up Score

n = int(input())
arr = list(map(int, input().split()))

print(sorted(set(arr))[-2])

#Problam=3
#Finding the Percentage

n = int(input())
d = {}
for _ in range(n):
    parts = input().split()
    d[parts[0]] = [float(p) for p in parts[1:]]

q = input()
print(f"{sum(d[q]) / len(d[q]):.2f}")

#Problam=4
#Nested Lists

n = int(input())
students = []
for _ in range(n):
    name = input()
    grade = float(input())
    students.append([name, grade])

grades = sorted(set(g for name, g in students))
second = grades[1]

names = sorted(name for name, g in students if g == second)
print("\n".join(names))
