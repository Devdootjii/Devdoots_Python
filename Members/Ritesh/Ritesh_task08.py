# Day 8: Comprehensions & Lambda Functions
# Name: Ritesh
# What I learned today: List and dictionary comprehensions, and custom sorting using lambda functions.
# Where I got stuck & fixed it: Configured key parameter in sorted() using lambda to sort names by string length.

print("========================================")
print("     COMPREHENSIONS & LAMBDA ENGINE     ")
print("========================================")

#input dataset
numbers = [9,4,2,7,12,5]
print(f"Original Numbers : {numbers}")

# a) list comprehension : only even numbers
even_numbers = [ num for num in numbers if num % 2 == 0]
print(f"Even Numbers : {even_numbers}")

# b) List comprehension : each numbers square
squared_numbers = { num ** 2 for num in numbers}
print(f"Squared Numbers : {squared_numbers}")

# c) Dictionary Comprehension: Number to Square Mapping (number: square)
number_square_dict = { num: num ** 2 for num in numbers}
print(f"Number-Square Map : { number_square_dict}")

print("\n----------------------------------------")
print("        CUSTOM LAMBDA SORTING           ")
print("----------------------------------------")
# Lambda Function: Names List ko length ke hisaab se sort karna
names =["Ritesh", "Balram", "Divyansh", "Aryan","harsh","Khushi","Om"]
print(f"Original names : {names}")

# sorted() ke saath lambda key use karke string length par sort kiya
sorted_names_by_len = sorted(names, key=lambda name : len(name))
print(f"Sorted by Length : {sorted_names_by_len}")
print("========================================")
print("Audit Status: SUCCESSFUL")
print("========================================")