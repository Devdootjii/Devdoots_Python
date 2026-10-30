#Naya concept
nums=[1,2,3,4,5,6]
squares=[n*n for n in nums]

even=[n for n in nums if n%2==0]

print(squares)   
print(even) 

double = lambda x: x * 2
print(double(5))

#P1

nums=[4, 16, 36, 64, 100]
squares=[n*n for n in nums]
[n*n for n in range(1, 11) if n % 2 == 0]

print(squares)   
print(even)

#P2

names = ["Riya", "Aman", "Khushi"]

res = [name for name in names if len(name) == 6]
print(res)

#PYQ:1
bigger = lambda a, b: a if a > b else b

print(bigger(3, 7))

#PYQ:2
words = ["aaa", "a", "aa"]
res = sorted(words, key=lambda w: len(w))

print(res)



