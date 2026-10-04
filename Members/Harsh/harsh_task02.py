# Day 2: Iteration & Loops

# --- Accumulators ---
total = 0
count = 0
highest = 0
fraud = False


print("     DAILY TRANSACTION ENTRY SYSTEM")

print("Enter Transaction Amount (type -1 to finish):")

while True:
    amount = float(input("Enter Amount: "))

    # 1. Stop signal
    if amount == -1:
        break

    # 2. Fraud detection
    if amount >= 1000000:
        print("FRAUD ALERT: Suspicious transaction detected! System locked.")
        fraud = True
        break

    # 3. Data cleaning
    if amount <= 0:
        print("Invalid Transaction Skipped!")
        continue

    # 4. Accumulators
    total = total + amount
    count = count + 1
    if amount > highest:
        highest = amount

# 5. Report (loop ke BAHAR)
if not fraud:
    if count > 0:
        average = total / count
    else:
        average = 0

    
    print("       DAILY PERFORMANCE REPORT")
    
    print(f"Total Transactions Processed : {count}")
    print(f"Total Revenue Generated      : {total:.2f}")
    print(f"Average Transaction Value    : {average:.2f}")
    print(f"Highest Transaction Value    : {highest:.2f}")
    print("Status: Batch Processed Successfully!")
    