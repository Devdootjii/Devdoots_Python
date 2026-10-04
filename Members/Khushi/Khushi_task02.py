#day-2 : iteration and loops
#name : Khushi
#what i learned : while loop, for loop and range , break statement , continue statement , accumulator pattern
#where i got stuck & fixed it : while true, or accumulator ka logic me confusion espasially -1 ka logic samjhne me or range me 


total = 0
count = 0
highest = 0

while True:
    amount = int(input("Enter transaction amount: "))

    if amount == -1:
     break

    if amount <= 0:
      print("Invalid transaction skipped!")
      continue

    # Fraud check
    if amount >= 1000000:
      print("Fraud Alert! Transaction is too large.")
      break
    # Valid transaction
    total += amount
    count += 1

    if amount > highest:
       highest = amount


print("\n----- Daily Transaction Report -----")
print("Total revenue:", total)
print("Valid transactions:", count)
print("Highest transaction:", highest)

if count > 0:
    average = total / count
    print("Average Transaction:", average)
else:
    print("No valid transactions")

    print("-------------------------------------")
    print("status: Batch Processed Successfully")
    print("-------------------------------------")