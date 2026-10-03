# task 1: safe calculator
def safe_calculator(num1, num2):
    try:
        return num1 / num2
    except ZeroDivisionError:
        return "Error: Zero se divide nahi kar sakte!"
    except TypeError:
        return "Error: Dono inputs numbers (int/float) hone chahiye!"

# task 2: file logging
# append activity
with open("devdoots_activity.txt", "a") as file:
    file.write("[Balram]: Practiced Exception Handling and File I/O\n")

# safely read file
try:
    with open("devdoots_activity.txt", "r") as file:
        print(file.read())
except FileNotFoundError:
    print("Error: File nahi mili!")