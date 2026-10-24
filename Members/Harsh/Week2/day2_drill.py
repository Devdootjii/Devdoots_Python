#P1:sum

a = [10, 20, 30, 40, 50]
total = 0
for n in a:
    total = total + n      
print(total)               

#P2:max

a=[]
size=int(input("Enter size of list:"))
for i in range(size):
    val=int(input("Enter Numbers:"))
    a.append(val)

max=a[0]
for i in range(size):
    if a[i]>max:
        max=a[i]
print("Max Number=",max)

#p3:Reverse

a=[10,20,30,40,50]
rev=[]

for i in range(len(a)-1,-1,-1):
    rev.append(a[i])
    print(rev)


#P4: Swap
a=[10,20,30,40,50]
num=a[0]
a[0]=a[4]
a[4]=num
print(a)


a=[10,20,30,40,50]
a.reverse()
print(a)

#P5 · Search

def search(a, target):
    for i in range(len(a)):
        if a[i]==target:      
            return i             
    return -1                   

a = [10, 20, 30, 40, 50]
print(search(a, 30))   
print(search(a, 99)) 


#P6 · Count
nums=[3, 8, 5, 12, 7, 4]
for num in nums:
    if num%2==0:
        print(nums)

#R-Practice 1
def factorial(n):
    if n <= 1:                 
        return 1
    return n * factorial(n - 1)   

print(factorial(5))            

#R-Practice 2

def power(a,b):
    if b==0:                 
        return 1
    return a * power(a, b-1)  

print(power(2,3))            


