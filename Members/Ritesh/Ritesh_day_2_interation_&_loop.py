# Day 2: Iteration & Loops
# Name: Ritesh
# What I learned today: Mastered while loops, break, continue, accumulator patterns and zero-division handling.
# Where I got stuck & fixed it: Handled zero division check when no valid transactions are entered before exit.
import sys
#accumulator variabales
total_revenue = 0.0
total_transactions = 0
highest_transaction = 0.0

print("=======================================")
print("     DAILY TRANSACTION ENTRY SYSTEM    ")
print("=======================================")
print("Enter transaction amount (Type -1 to finish):")
# USER INPUT LOOP
while true :
    try :
        amount = float(input("enter amount :"))
    except ValueError:
        print("invalid transaction skipped ! ( Please enter numbers only)")
        continue
    # exit Single check (-1)
    if amount == -1:
        break
    # Security & Fraud Detection Check (₹10,00,000 ya usse zyada)
    if amount >= 1000000: 
        print("FRAUD ALERT! Suspicious transaction detected! System locked. ")
        is_fraud_detected = True
        break

# Data Cleaning & Filtering (0 ya negative numbers)    
if amount <= 0:
    print("Invalid transaction skipped !!!")
    continue
# Valid Transaction Accumulation

total_revenue += amount
total_transactions += 1
if amount > highest_transaction:
    highest_transaction = amount
   
    # Agar fraud detect hua toh bina report dikhaye exit karna hai
if is_fraud_detected:
    sys.exit()
# Zero Division Check ke saath Average calculate karna
if total_transactions > 0:
    average_transaction = total_revenue / total_transactions
else::
    average_transaction = 0.0
# Performance Summary Report
print("\n=======================================")
print("       DAILY PERFORMANCE REPORT        ")
print("=======================================")
print(f"Total Transactions Processed : {total_transactions}")
print(f"Total Revenue Generated : {total_revenue:.2f}")
print(f"Average Transaction Value : {average_transaction:.2f}")
print(f"Highest Transaction Value : {highest_transaction:.2f}")
print("---------------------------------------")
print("Status: Batch Processed Successfully!")
print("=======================================")
 