class SecureBankAccount:
    def __init__(self, account_holder, balance=5000, pin=1234):
        self.account_holder = account_holder
        
        self.__balance = balance
        self.__pin = pin

    def withdraw(self, entered_pin, amount):
        if entered_pin != self.__pin:
            print("Error: Invalid PIN entered! Please try again.")
            return

        if amount <= self.__balance:
            self.__balance -= amount
            print(f"Success: Withdrew ${amount}. Remaining balance: ${self.__balance}")
        else:
            print(f"Error: Insufficient funds! Current balance: ${self.__balance}")


# Creating an instance with default balance (5000) and PIN (1234)
acc = SecureBankAccount("Khushi")

# Test 1: Successful withdrawal with correct PIN and valid amount
acc.withdraw(1234, 2000)

# Test 2: Failed withdrawal due to incorrect PIN
acc.withdraw(9999, 500)

# Test 3: Failed withdrawal due to exceeding available balance
acc.withdraw(1234, 10000)