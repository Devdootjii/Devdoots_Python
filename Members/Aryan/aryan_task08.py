
# Day 8: Comprehensions & Lambda Functions
# Name: Aryan
# What I learned today: List, Dictionary, Set Comprehensions and Lambda Functions



numbers = [4, 9, 2, 7, 12, 5]


#List Comprehensions

# Extract even numbers
even_numbers = [number for number in numbers if number % 2 == 0]
print("Even Numbers:", even_numbers)

#  Calculate squares of all numbers
squares = [number ** 2 for number in numbers]
print("Squares:", squares)

# Create a dictionary of numbers and their squares
number_squares = {number: number ** 2 for number in numbers}
print("Number-Square Dictionary:", number_squares)


#  Set Comprehension

# Extract unique square values
unique_squares = {number ** 2 for number in numbers}
print("Unique Squares:", unique_squares)


# Lambda Function with sorted()

names = ["Aryan", "Ravi", "Amit", "Priyanshu", "Raj"]

# Sort names according to their length
sorted_names = sorted(names, key=lambda name: len(name))

print("Original Names:", names)
print("Names Sorted by Length:", sorted_names)
