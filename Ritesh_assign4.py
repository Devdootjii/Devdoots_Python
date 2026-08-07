# Task 1 : safe division Utilty ( exception handling)
def safe_calculator(num1, num2):
    try:
        result = num1 / num2
        return f"Success: Result is {result}"
    except ZeroDivisionError:
        return "Error : No devide with Zero!!!"
    except TypeError:
        return "Error : Both Inputs numbers(int/float) are required !"
    
    # Task 2 : Devdoots activity Logger 
def log_and_read_activity():
    filename = "ritesh_devdoots_activity.txt"
    with open(filename,"a") as file:
     file.write("[Ritesh]: Practiced Exception Handling and file I/O\n")
    print(" Successfully add In Activity log\n")

    try:
        with open(filename,"r") as file:
            content = file.read()
            print("---- Activity Log Content ---")
            print(content)
    except FileNotFoundError:
        print(f"Error : '{filename}' File name's Not found!")

if __name__ == "__main__":
    print("---Task 1 Output ---")
    print(safe_calculator(10,2))

    print(safe_calculator(10,0))

    print(safe_calculator(10,"Devdoots"))

    print("--- Task 2 Output ---")
    log_and_read_activity()                