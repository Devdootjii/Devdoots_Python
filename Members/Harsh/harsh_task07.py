# Day 7: Modules & Import System
# Name: Harsh Rajbhar
# What I learned today: apna custom module banana aur import karna, math & random libraries
# Where I got stuck & fixed it: module ko same folder mein rakhna zaroori hai, warna import fail hota hai

import calculator
import math
import random

print("========================================")
print("   CALCULATOR MODULE TEST")
print("========================================")

# --- 4 operations (from calculator.py) ---
print(f"add(10, 5)  = {calculator.add(10, 5)}")
print(f"sub(10, 5)  = {calculator.sub(10, 5)}")
print(f"mul(10, 5)  = {calculator.mul(10, 5)}")
print(f"div(10, 5)  = {calculator.div(10, 5)}")
print(f"div(10, 0)  = {calculator.div(10, 0)}")     # zero division handling

# --- Bonus 1: Dice roll (random library) ---
print("\n--- BONUS ---")
dice = random.randint(1, 6)
print(f"Dice Roll: {dice}")

# --- Bonus 2: Square root (math library) ---
number = 64
print(f"Square Root of {number}: {math.sqrt(number)}")

print("\n========================================")
print("Audit Status: SUCCESSFUL")
