# task 1: encapsulation (banking)
class SecureBankAccount:
    def __init__(self, account_holder):
        self.account_holder = account_holder
        self.__balance = 5000
        self.__pin = 1234

    def withdraw(self, entered_pin, amount):
        if entered_pin == self.__pin:
            if amount <= self.__balance:
                self.__balance -= amount
                return f"Success! Balance left: {self.__balance}"
            else:
                return "Not enough balance!"
        else:
            return "Wrong PIN!"

    def change_pin(self, old_pin, new_pin):
        if old_pin == self.__pin:
            # check if new pin is 4 digits
            if len(str(new_pin)) == 4:
                self.__pin = new_pin
                return "PIN updated!"
            else:
                return "PIN must be 4 digits!"
        else:
            return "Old PIN is wrong!"


# task 2: abstraction (ai models)
from abc import ABC, abstractmethod

# base class
class BaseAIModel(ABC):
    @abstractmethod
    def train_model(self, dataset_name):
        pass

    @abstractmethod
    def evaluate_accuracy(self):
        pass

# child class 1
class VisionModel(BaseAIModel):
    def train_model(self, dataset_name):
        return f"Training image model on {dataset_name}"

    def evaluate_accuracy(self):
        return "Image model accuracy: 92%"

# child class 2
class NLPModel(BaseAIModel):
    def train_model(self, dataset_name):
        return f"Training text model on {dataset_name}"

    def evaluate_accuracy(self):
        return "Text sentiment accuracy: 89%"