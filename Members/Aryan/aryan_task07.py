
# Day 7: Python Modules & Import System
# Name: Aryan
# What I learned today: Creating modules and importing functions


import calculator
import random
import math


# Calculator Operations
num1 = 20
num2 = 5

print("===== CALCULATOR MODULE =====")
print("Addition:", calculator.add(num1, num2))
print("Subtraction:", calculator.sub(num1, num2))
print("Multiplication:", calculator.mul(num1, num2))
print("Division:", calculator.div(num1, num2))

# Testing Division by Zero
print("Division by Zero:", calculator.div(num1, 0))


# Random Dice Roll
print("\n===== RANDOM DICE ROLL =====")
dice_roll = random.randint(1, 6)
print("Dice Result:", dice_roll)


# Square Root using Math Module
print("\n===== MATH MODULE =====")
number = 144
print("Number:", number)
print("Square Root:", math.sqrt(number))
