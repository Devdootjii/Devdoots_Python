
# Day 9: JSON & Nested Data Processing
# Name: Aryan
# What I learned today: JSON handling and nested dictionaries


import json

# Initial student data
students = [
    {
        "name": "Amit",
        "marks": {
            "Maths": 85,
            "Science": 90
        }
    },
    {
        "name": "Riya",
        "marks": {
            "Maths": 78,
            "Science": 88
        }
    },
    {
        "name": "Rahul",
        "marks": {
            "Maths": 92,
            "Science": 84
        }
    }
]

# Save data to JSON file
with open("Members/Aryan/students.json", "w") as file:
    json.dump(students, file, indent=4)

print("Student data saved to JSON file.")


# Read JSON data
with open("Members/Aryan/students.json", "r") as file:
    students = json.load(file)

print("\n===== STUDENT MARKS REPORT =====")

for student in students:
    name = student["name"]
    maths_marks = student["marks"]["Maths"]
    science_marks = student["marks"]["Science"]

    total = maths_marks + science_marks
    average = total / 2

    print("Student:", name)
    print("Maths Marks:", maths_marks)
    print("Science Marks:", science_marks)
    print("Total Marks:", total)
    print("Average Marks:", round(average, 2))
    print("-" * 30)


# Add a new student record
new_student = {
    "name": "Aryan",
    "marks": {
        "Maths": 89,
        "Science": 93
    }
}

students.append(new_student)

# Save updated student data
with open("Members/Aryan/students.json", "w") as file:
    json.dump(students, file, indent=4)

print("\nNew student record added successfully.")

# Verify updated JSON data
with open("Members/Aryan/students.json", "r") as file:
    updated_students = json.load(file)

print("Total Student Records:", len(updated_students))
