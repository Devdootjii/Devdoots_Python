# Day 9: JSON & Nested Data
# File: Members/Balram/balram_task09.py

import json

# initial students data json format me
students_data = [
    {"name": "Amit", "marks": {"math": 80, "sci": 90}},
    {"name": "Rahul", "marks": {"math": 75, "sci": 85}}
]

file_name = "students.json"

# data ko json file me save karna
with open(file_name, "w") as f:
    json.dump(students_data, f, indent=4)
print("Data students.json me save ho gaya.")

# json file read karna
with open(file_name, "r") as f:
    loaded_data = json.load(f)

print("\n--- Students Records ---")
for student in loaded_data:
    name = student["name"]
    marks = student["marks"]
    total = marks["math"] + marks["sci"]
    avg = total / 2
    print(f"Student: {name} | Total Marks: {total} | Average: {avg:.2f}")

# naya student record add karna
new_student = {"name": "Mohit", "marks": {"math": 88, "sci": 92}}
loaded_data.append(new_student)

# updated data wapas file me save karna
with open(file_name, "w") as f:
    json.dump(loaded_data, f, indent=4)
print("\nNaya record add karke file update kar di gayi hai.")