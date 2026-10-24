# # P1 sum
a=[10,20,30,40,50]
total_sum=0
for i in a:
    total_sum+=i
print(f"Total sum is {total_sum}")

#P2 Maximum
maximum =0
for i in a:
    if i>maximum:
        maximum=i
print(f"Maximum is {maximum}")

#P3 Reverse
for i in range(len(a)-1,-1,-1):
    print(f"Reverse : {a[i]}")


#P4 Swap
temp =a[0]
a[0]=a[4]
a[4]=temp
print(f"swapped:{a}")

#P5 search
def search(a,target):
    for i in range(len(a)):
        if a[i] == target:
            return i
    return -1
result =search(a,99)
print("Search result for 99:",result)
print("Search result for 30:",search(a,30))

l =[3,8,5,12,7,4]
count =0 
for i in l:
    if i%2==0:
        count+=1
print("l:",l)
print("Total even no in l:",count)

#D1 debug

a=[10,20,30]
mx=0
for n in a:
    if n>mx:
        mx=n
print("Debug 1:",mx)

#D2 debug
a=[1,2,3]
for i in range(len(a)-1,1,-1):
    print("Debug 2:",a[i])

# R Practice 1
def sum_to(n):
    if n ==1:
        return 1
    return n+ sum_to(n-1)
print("Practice 1 'Sum':",sum_to(5))

# R Practice 2
def power(a,b):
    if b==0:
        return 1
    return a*power(a,b-1)
print("Practice 2 'Power':",power(2,3))