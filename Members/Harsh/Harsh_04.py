#Task 1: Safe Division Utility ka Blueprint

def self_calculator(num1,num2):
    try:
        ans=num1/num2

    except ZeroDivisionError:
        return "Error: Zero se divide nahi kar sakte"

    except TypeError:
        return "Error: Dono inputs numbers (int/float) hone chahiye!"
print(self_calculator(25,5))
print(self_calculator(645345,0))
print(self_calculator(44,"A"))

#Task 2: Devdoots Activity Logger (File I/O)    

def team_activity_logger():
    file_name = "Devdoots_activity.txt"
    
    with open(file_name, "a") as file:
        file.write("[Harsh]: Practiced Exception Handling File I/O\n")
        
    try:
        with open(file_name, "r") as file:
            content = file.read()
            print(content)        
            
    except FileNotFoundError:     
        print("Error: File nahi mili!")

team_activity_logger()


