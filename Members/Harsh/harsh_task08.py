# Day 8: Comprehensions & Lambda Functions
# Name: Harsh Rajbhar
# What I learned today: list/dict/set comprehensions aur lambda functions
# Where I got stuck & fixed it: comprehension ka dhaancha (expr for item in list) samajhna tha

print("========================================")
print("   COMPREHENSIONS & LAMBDA DEMO")
print("========================================")

# --- Numbers list ---
numbers = [4, 9, 2, 7, 12, 5]
print(f"\nOriginal list: {numbers}")

# (a) Sirf even numbers (list comprehension + if filter)
evens = [n for n in numbers if n % 2 == 0]
print(f"(a) Even numbers: {evens}")

# (b) Har number ka square (list comprehension)
squares = [n * n for n in numbers]
print(f"(b) Squares: {squares}")

# (c) Number -> Square dictionary (dict comprehension)
squares_dict = {n: n * n for n in numbers}
print(f"(c) Squares dictionary: {squares_dict}")

# --- Names list sorted by length (sorted + lambda) ---
names = ["Rahul", "Aman", "Priya", "Zoya", "Om"]
print(f"\nNames: {names}")

sorted_names = sorted(names, key=lambda name: len(name))
print(f"Sorted by length: {sorted_names}")

print("\n========================================")
print("Audit Status: SUCCESSFUL")
