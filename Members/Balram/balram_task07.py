# Day 7: Modules & Standard Library
# File: Members/Balram/balram_task07.py

import calculator
import random
import math

# custom module functions test karna
print("Add:", calculator.add(10, 5))
print("Sub:", calculator.sub(10, 5))
print("Mul:", calculator.mul(10, 5))
print("Div with zero check:", calculator.div(10, 0))

# random module se dice roll (1 se 6)
dice = random.randint(1, 6)
print("Dice roll:", dice)

# math module se square root
val = 36
print(f"Square root of {val}:", math.sqrt(val))