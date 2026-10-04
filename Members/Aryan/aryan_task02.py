# Day 2: Iteration & Loops
# Name: Aryan
# What I learned today: While loops, break, continue and accumulator pattern


total_revenue = 0
transaction_count = 0
highest_transaction = 0
fraud_detected = False

#transaction process
while True:
    amount = input("Enter transaction amount:").strip()

    # Finish input on 'q'
    if amount.lower() == "q":
        break
    if amount == "-1":
        break

    amount = float(amount)

    # Skip invalid negative transactions
    if amount < 0:
        print("Invalid transaction ")
        continue

    #fraud transaction 
    if amount >=1000000:
        print("suspicious transaction detected")
        fraud_detected = True
        break

    # Accumulator Pattern
    total_revenue += amount
    transaction_count += 1

    # Track Highest Transaction
    if amount > highest_transaction:
        highest_transaction = amount

# Daily Performance Report
if not fraud_detected:
    print("\n========================================")
    print("       DAILY PERFORMANCE REPORT")
    print("========================================")

    print(f"Total Transactions Processed : {transaction_count}")
    print(f"Total Revenue Generated      : ₹{total_revenue:.2f}")

    # Zero Division Check
    if transaction_count > 0:
        average_transaction = total_revenue / transaction_count
    else:
        average_transaction = 0

    print(f"Average Transaction Value    : ₹{average_transaction:.2f}")
    print(f"Highest Transaction Value    : ₹{highest_transaction:.2f}")

    print("----------------------------------------")
    print("Status: Batch Processed Successfully!")
    print("========================================")

