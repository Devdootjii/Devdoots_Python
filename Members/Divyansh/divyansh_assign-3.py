from abc import ABC, abstractmethod
#encapsulation
class SecureBankAccount:
    def __init__(self,account_holder,initial_balance = 5000,initial_pin=1234):
        self.__balance=initial_balance
        self.__pin=initial_pin
        self.account_holder=account_holder
    def withdraw(self,enterd_pin,amount):
        if enterd_pin != self.__pin:
            return f"Error : Invalid Pin!"
        if amount > self.__balance:
            return "Error: Insufficient Balance!"
        self.__balance -=amount
        return f"Withdraw Sucessfully! Remaining Balance : {self.__balance}"
    def change_pin(self,old_pin,new_pin):
        if old_pin != self.__pin:
            self.__pin=new_pin
            return f"Error : Old PIN is Incorrect!"
        if len(str(new_pin)) != 4 or not str(new_pin).isdigit():
            return "Error: New PIN must be a 4-digit number!"
        self.__pin = new_pin
        return "PIN updated successfully"

#abstraction
class BaseAIModel(ABC):
    @abstractmethod
    def train_model(self,dataset_name):
        pass
    @abstractmethod
    def evaluate_accuracy(self):
        pass

class VisionModel(BaseAIModel):

    def train_model(self, dataset_name):
        return f"Training Computer Vision model on {dataset_name} dataset...."
    def evaluate_accuracy(self):
        return "Vision Model Accuracy: 94.5%"

class NLPModel(BaseAIModel):
    def train_model(self, dataset_name):
        return f"Training Computer Vision model on {dataset_name} dataset...."
    def evaluate_accuracy(self):
        return "Vision Model Accuracy: 88.5%"
        
print("----Task 1----")
user1=SecureBankAccount("Divyansh",initial_balance=5000,initial_pin=1234)
print(user1.withdraw(1234,500))
print(user1.withdraw(1256,500))

print(user1.change_pin(1234,4321))
print(user1.change_pin(4321,12))

print("----task 2-----")
vision_net = VisionModel()
print(vision_net.train_model("ImageNet"))
print(vision_net.evaluate_accuracy())

nlp_net = NLPModel()
print(nlp_net.train_model("IMDB Reviews"))
print(nlp_net.evaluate_accuracy())