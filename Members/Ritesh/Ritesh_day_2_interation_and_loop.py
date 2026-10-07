# Day 2: Iteration & Loops
# Name: Ritesh
# What I learned today: while loop, break on termination/fraud, continue for skipping invalid data, and accumulator pattern.
# Where I got stuck & fixed it: Ensured -1 is handled before <= 0 condition so break executes properly instead of continue.

#Accumulators initialize karna (Loop ke bahar)
total_revenue = 0.0
total_transactions = 0
highest_transaction = 0.0

#  HEADER PRINT 
print("=======================================")
print("     DAILY TRANSACTION ENTRY SYSTEM    ")
print("=======================================")
print("Enter transaction amount (Type -1 to finish):")

#Runtime User Input Loop
while True:
    try:
        amount = float(input("Enter Amount: "))
    except ValueError:
        print("Invalid transaction skipped!")
        continue
    #Termination Signal Check (-1)
    if amount == -1:
        break
    #Security & Fraud Detection (>= 10,00,000)
    if amount >= 1000000:
        print(" FRAUD ALERT: Suspicious transaction detected! System locked.")
        exit()
        #Data Cleaning & Filtering (0 ya negative except -1)
    if amount <= 0:
        print("Invalid transaction skipped!")
        continue
    #Accumulators Update (Sirf valid entries ke liye)

    total_revenue += amount
    total_transactions += 1
    if amount > highest_transaction:
        highest_transaction = amount
        #Average Calculation with Zero Division Protection
if total_transactions > 0:
    average_transaction = total_revenue / total_transactions
else: 
    average_transaction = 0.0  
    #  Terminal Report
    print("=======================================")
print("       DAILY PERFORMANCE REPORT        ")
print("=======================================")
print(f"Total Transactions Processed : {total_transactions}")
print(f"Total Revenue Generated : {total_revenue:.2f}")
print(f"Average Transaction Value : {average_transaction:.2f}")
print(f"Highest Transaction Value : {highest_transaction:.2f}")
print("---------------------------------------")
print("Status: Batch Processed Successfully!")
print("=======================================")

