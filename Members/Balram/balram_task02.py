# Day 2: Iteration & Loops
# Name: Balram Singh
# What I learned today: while loop aur break continue ka use
# Where I got stuck & fixed it: count aur total calculation me logic set kiya

total_rev = 0
count = 0
max_val = 0

print("DAILY TRANSACTION ENTRY SYSTEM")
print("Enter amount (-1 to exit):")

while True:
    amt = float(input("Enter Amount: "))

    # loop stop check
    if amt == -1:
        break

    # minus or zero amount skip
    if amt <= 0:
        print("Invalid transaction skipped!")
        continue

    # fraud alert check
    if amt >= 1000000:
        print("FRAUD ALERT: Suspicious transaction detected!")
        break

    # calculation logic
    total_rev = total_rev + amt
    count = count + 1

    if amt > max_val:
        max_val = amt

print("\nDAILY PERFORMANCE REPORT")
print("Total Transactions Processed:", count)
print("Total Revenue Generated:", total_rev)

if count > 0:
    avg = total_rev / count
    print("Average Transaction Value:", avg)
else:
    print("Average Transaction Value: 0")

print("Highest Transaction Value:", max_val)
print("Status: Batch Processed Successfully")