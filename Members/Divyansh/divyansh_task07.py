# Day 7: Modules & imports
# Name: Divyansh
# What I learned today: apna module banana, use import karna, aur math/random library
# Where I got stuck & fixed it: import line comment thi; calculator.py ke chaar functions import kiye

import calculator
import math
import random
print(calculator.add(2, 2))
print(calculator.sub(100, 2))
print(calculator.mul(6, 2))
print(calculator.div(16, 8))
print(calculator.div(2, 0))

dice_roll = random.randint(1, 6)
print("Dice roll:", dice_roll)
print("Square root of dice roll:", math.sqrt(dice_roll))
