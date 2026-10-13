# Day 7: Modules & Standard Libraries
# Name: Ritesh
# What I learned today: Custom module creation, importing helper functions, and using math and random libraries.
# Where I got stuck & fixed it: Handled division by zero gracefully inside the custom calculator module.
import math
import random
import h4x_calculator

print("========================================")
print("     MODULAR CALCULATOR ENGINE          ")
print("========================================")

# Step 1: Testing Custom Calculator Functions
num1 = 70 
num2 = 130

print(f"inputs: a = {num1}, b = {num2}")
print("Addition  :", h4x_calculator.add(num1, num2))
print("Subtraction :" , h4x_calculator.sub(num1, num2))
print("Multiplication :" , h4x_calculator.mul(num1, num2))
print("Division :" , h4x_calculator.div(num1, num2))

# Step 2: Testing Zero Division Error Handling
print("\n--- Zero Division Test ---")
zero_result = h4x_calculator.div(10, 0)
print("Division by 0  :", zero_result)

# step 3 : Bonus Standard libraries Operations
print("\n--- Bonus Library Operations ---")
# Math: Square root calculation
val = 49
sqrt_val = math.sqrt(val)
print(f"Square root of {val} (math.sqrt) : {sqrt_val}")
# Random: Dice roll simulation (1 to 6)
dice_roll = random.randint(1, 6)
print(f"Simulated Dice Roll (random.randint(1, 6)) : {dice_roll}")

print("========================================")
print("Audit Status: SUCCESSFUL")
print("========================================")