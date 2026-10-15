# Day 9: JSON & Nested Data
# Name: Harsh Rajbhar
# What I learned today: json.dump / json.load aur nested dictionaries
# Where I got stuck & fixed it: nested value nikalna (student["marks"]["math"])

import json

print("========================================")
print("   STUDENT JSON PROCESSOR")
print("========================================")

# --- Step 1: Data structure (list of dicts, nested marks) ---
students = [
    {"name": "Amit", "marks": {"math": 80, "sci": 90}},
    {"name": "Priya", "marks": {"math": 95, "sci": 88}}
]

# --- Step 2: Write data to file (json.dump) ---
with open("students.json", "w") as file:
    json.dump(students, file, indent=4)
print("\n[Step 2] Data written to students.json")

# --- Step 3: Read data back (json.load) ---
with open("students.json", "r") as file:
    loaded = json.load(file)
print(f"[Step 3] Loaded {len(loaded)} students from file")

# --- Step 4: Nested access + total/average calculation ---
print("\n--- Marks Report ---")
for student in loaded:
    marks = student["marks"]
    total = marks["math"] + marks["sci"]
    average = total / len(marks)
    print(f"{student['name']} -> Total: {total}, Average: {average}")

# --- Step 5: Add a new record and save back ---
new_student = {"name": "Harsh", "marks": {"math": 88, "sci": 92}}
loaded.append(new_student)

with open("students.json", "w") as file:
    json.dump(loaded, file)
print("\n[Step 5] New student added and file updated")

print("\n========================================")
print("Audit Status: SUCCESSFUL")
