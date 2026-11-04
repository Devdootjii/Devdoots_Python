n = int(input())
l = []

for i in range(n):
    name = input()
    marks = float(input())
    l.append([name, marks])

m = sorted(set(x[1] for x in l))[1]

for x in sorted(l):
    if x[1] == m:
        print(x[0])