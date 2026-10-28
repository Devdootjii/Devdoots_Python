# P1
even_squares=[n*n for n in range(11) if n% 2==0]
print(even_squares)

# P2
names =["Riya","Aman","Khushi","ABCDE"]
print([n for n in names if len(n)==5])

# PYQ 1

big = lambda x,y: x if x>y else y
print("Bigger is:",big(3,5))

# PYQ 2
print(sorted(["aaa","a","aa"], key=len))

