# day8
#Name: Divyansh
# what i lerened: lambda,comprihension
# where i stuked: unable to undersand syntax and flow of code

# Part 1
num = [4, 9, 2, 7, 12, 5]
result=[n for n in num if n%2==0]
squ=[n*n for n in result]
dic={n : n*n for n in result}
print(f"Even numbers list :{result}")
print(f"Square numbers list :{squ}")
print(f"Square numbers Dict :{dic}")

#Part 2

names=["Mohan","Sohanji","Rohan","Rom"]
sort_names=sorted(names,key=lambda name:len(name))
print(f"Normal List: {names}")
print(f"Sorted List: {sort_names}")