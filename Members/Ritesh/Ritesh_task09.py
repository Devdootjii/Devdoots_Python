# Day 9: JSON & Nested Data Processing
# Name: Ritesh
# What I learned today: Serialization with json.dump, deserialization with json.load, and nested dictionary traversal.
# Where I got stuck & fixed it: Traversed nested dictionary marks to aggregate values and persisted appended records.
import json 
FILE_NAME = "h4x_student.json"

print("========================================")
print("     JSON & NESTED DATA PROCESSOR       ")
print("========================================")
# Step 1: Initial Dataset (List of Dicts with Nested Marks)
initial_students = [
    {
        "name": "Divyash",
        "marks" : {
            "math" : 80,
            "sci" : 90
        }
    },
    {
        "name" : "Priya",
        "marks" : {
            "math" : 75,
            "sci" : 85
        }
    }
]
# Step 2: Write Data to students.json using json.dump
print("step 1 & 2 : Writing Initial records to h4x_Students.json....")
with open (FILE_NAME, "w", encoding="utf-8") as file : 
    json.dump(initial_students, file, indent=4)
print("Initial records saved successfully!\n")

 # Step 3: Read Data from students.json using json.load
print("Loading recods back form h4x_students.json....")
with open(FILE_NAME, "r", encoding="utf-8") as file:
    loaded_students = json.load(file)

# Step 4: Nested Data Access & Metrics Calculation
print("\n--- NESTED MARKS EVALUATION ---")
for student in loaded_students:
    s_name = student["name"]
    s_marks = student["marks"]
    
    total_marks = sum(s_marks.values())
    avg_marks = total_marks / len(s_marks)
    print(f"Students : {s_name}")
    print(f" Marks Breakdown : {s_marks}")
    print(f" Total Marks : {total_marks}")
    print(f" Average marks : {avg_marks:.2f}")
# Step 5: Append New Student Record and Update JSON File
print("\n----------------------------------------")
print("Appending new student record...")
new_student = {
    "name": "Ritesh",
    "marks": {
        "math": 92,
        "sci": 88
    }
}
# Append to in-memory list
loaded_students.append(new_student)
 # Persist updated list back to students.json  
with open(FILE_NAME, "w", encoding="utf-8") as file:
    json.dump(loaded_students, file, indent=4)
print(f"Record for '{new_student['name']}' appended and saved to {FILE_NAME}!") 
# Final Verification Read
with open(FILE_NAME, "r", encoding="utf-8") as file:
    updated_records = json.load(file)
print(f"\nTotal Records in JSON File Now: {len(updated_records)}")
print("========================================")
print("Audit Status: SUCCESSFUL")
print("========================================")
