# Day 8: Comprehensions & Lambda
# File: Members/Balram/balram_task08.py

numbers = [4, 9, 2, 7, 12, 5]

# a. sirf even numbers ki list
even_nums = [x for x in numbers if x % 2 == 0]
print("Even numbers:", even_nums)

# b. numbers ke squares ki list
squares = [x ** 2 for x in numbers]
print("Squares:", squares)

# c. dictionary (number: square)
num_dict = {x: x ** 2 for x in numbers}
print("Number dict:", num_dict)

# names list ko length ke hisaab se sort karna lambda se
names = ["amit", "rahul", "alexander", "mohit", "raj"]
sorted_names = sorted(names, key=lambda n: len(n))
print("Sorted names:", sorted_names)