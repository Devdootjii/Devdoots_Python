# # 

# class SecureBankAccount:

#   def __init__(self, owner, initial_balance):
#     self.owner = owner  # Public variable
#     self.__balance = initial_balance  # Private variable (Double Underscore)

#   # Safe Method: Balance update karne ke liye
#   def deposit(self, amount):
#     if amount > 0:
#       self.__balance += amount
#       return f"₹{amount} deposited successfully!"
#     return "Invalid deposit amount."

#   # Getter Method: Balance check karne ke liye
#   def get_balance(self):
#     return f"Account Balance for {self.owner}: ₹{self.__balance}"


# # Object Creation
# acc = SecureBankAccount("Divyansh", 10000)

# # Public variable access
# print(acc.owner)  # Output: Divyansh

# # Safe method calls
# print(acc.deposit(2000))
# print(acc.get_balance())

# # Direct access Attempt (Yeh Error dega!):
# # print(acc.__balance)  # AttributeError: 'SecureBankAccount' object has no attribute '__balance'

try:
  num = int(input("Number dalo: "))
  result = 10 / num
  print(f"Result: {result}")

except ValueError:
  print("Galti: Aapne number ki jagah text daal diya!")

except ZeroDivisionError:
  print("Galti: Zero (0) se divide nahi kar sakte!")

except Exception as e:
  print(f"Koi anjaan error aayi: {e}")