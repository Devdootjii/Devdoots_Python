# Task1: Safe_Calculator

def safe_calculator(num1, num2):
    try:
        result = num1 / num2

    except ZeroDivisionError:
        return ("Error: Cannot divide by zero!")

    except TypeError:
        return ("Error: Please enter numbers only!")

    else:
        return result

print("Task 1 Output:")
print(safe_calculator(10, 2))
print(safe_calculator(10, 0))
print(safe_calculator(10, "a"))

#================

# Task 2: File Handling

with open("devdoots_activity.txt", "a") as f:
    f.write("Khushi: Practiced exception handling and file I/O \n")

print("\nTask 2 output:")

try:
    with open("devdoots_activity.txt", "r") as f:
        print(f.read())

except FileNotFoundError:
 print("Error: File not found")