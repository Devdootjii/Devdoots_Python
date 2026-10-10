#day 08 task
#name = Khushi
#what I learned today : list comprehension, dictionary comprehension, set comprehension, lambda functions ,sorted+ lambda
#where I got stuck & fixed it : dictionary or list ka code likhne me confusion (: ka use ) or lambda functions samjhne me

numbers = [4,9,2,7,12,5]
even = [n for n in numbers if n % 2 == 0]
squares = [n * n for n in numbers]
square_dictionary = {n : n*n for n in numbers}

#sorted + lambda
names =["Anmol","Anshika","Priti","Jahanvi"]
result = sorted(names, key=lambda name: len(name))

print("Even numbers:", even)
print("Squares:",squares)
print("Square dictionary:",square_dictionary)
print("Sorted names:", result)
