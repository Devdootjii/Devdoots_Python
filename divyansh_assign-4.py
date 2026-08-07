# task 1 

def safe_calculator(num1,num2):
    try:
        result=num1/num2
        return result
    except ZeroDivisionError:
        return ("Division by 0 is not possible!")
    except TypeError:
        return ("Plese enter numbers only!")

print(safe_calculator(2,0))
print(safe_calculator(2,2))

# task 2

with open("devdoots_activity.txt","a") as file:
    file.write("Divyansh:Practice Exception Handling and File I/O\n")

try:
    with open("devdoots_activity.txt","r") as file:
        content=file.read()    
        print(f"File content:{content}")
except FileNotFoundError:
    print("File does not exsist!")