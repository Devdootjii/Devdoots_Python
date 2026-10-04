# Day 2: Iteration & Loops
# Name: Divyansh
# What I learned today: while loop, break, continue aur accumulator pattern
# Where I got stuck & fixed it: while loop and proper indentation
count=0
average=0
highest=0
total=0
fraud =False
print(f"""
=======================================
     DAILY TRANSACTION ENTRY SYSTEM    
=======================================
Enter transaction amount (Type -1 to finish):""")
while True:
    Amount=float(input("Enter Amount:"))  
    if Amount == -1:
        break
    if Amount == 0 or Amount<0:
        print(f"⚠️ Invalid transaction skipped!")
        continue
    if Amount >= 1000000:
        print("Fraud Detected:Suspicious transaction detected! System locked.")
        fraud=True
        break

    total+=Amount
    count+=1
    if Amount > highest: 
        highest = Amount
if not fraud:
    if count > 0:
        average = total / count
    else:
        average = 0

    print(f"""
=======================================
       DAILY PERFORMANCE REPORT        
=======================================
Total Transactions Processed : {count}
Total Revenue Generated      : {total:.2f}
Average Transaction Value    : ₹{average:.2f}
Highest Transaction Value    : ₹{highest:.2f}
---------------------------------------
Status: Batch Processed Successfully!
=======================================
""")

