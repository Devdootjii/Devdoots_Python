#"Devdoots Assignment 03 - Python OOPs Encapsulation & Abstraction            
class SecureBankAccount:
    def __init__(self, account_holder):
        self.account_holder = account_holder
        self.__balance = 5000  # Private balance
        self.__pin = 1234      # Private pin 

    def withdraw(self, entered_pin, amount):
        if entered_pin == self.__pin and amount <= self.__balance:
            self.__balance = self.__balance - amount
            return "Withdrawal successful!"
        else:
            return "Invalid PIN or Insufficient Balance"

    def change_pin(self, old_pin, new_pin):
        if old_pin == self.__pin and 1000 <= new_pin <= 9999:
            self.__pin = new_pin
            return "PIN successfully changed!"
        else:
            return "Invalid old PIN or new PIN must be 4 digits"

my_account = SecureBankAccount("Harsh User") 
print(my_account.change_pin(1234, 9999))
print(my_account.withdraw(1111, 1000))

# Task 2: Al Model Pipeline Blueprint (Abstraction Practice)
from abc import ABC, abstractmethod

class BaseAIModel(ABC):
    @abstractmethod
    def train_model(self, dataset_name):
        pass

    @abstractmethod
    def evaluate_accuracy(self):
        pass

class VisionModel(BaseAIModel):
    def train_model(self, dataset_name):
        return f"Training Vision Model on {dataset_name} image dataset..."

class NLPModel(BaseAIModel):
    def train_model(self, dataset_name):
        return f"Training NLP Model on {dataset_name} text dataset..."

        def evaluate_accuracy(self):
           return "NLP Model Sentiment Classification Accuracy: 88%"

