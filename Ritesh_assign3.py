#task 1
class secureBankAccount:
    def __init__(self,account_holder):
        self.account_holder=account_holder
        self.__balance=5000
        self.__pin=123

    def withdraw(self,entered_pin,amount):
        if entered_pin==self.__pin and amount <=self.__balance:
            self.__balance=self.__balance-amount
            return"withdraw successfull"
        return" invalid amount "
    def change_pin(self,old_pin,new_pin):
        if old_pin==self.__pin and 1000<= new_pin <= 9999:
            self.__pin=new_pin
            return"Pin Successfully Changed"
        return"New pin must be 4 digits"

my_account=secureBankAccount("Ritesh") 
print("Test 1:", my_account.withdraw(7777,1000))   
print("Test 2:", my_account.change_pin(8765,9999))

# task 2
from abc import ABC,abstractmethod
class BaseAImodel:
    @abstractmethod
    def train_model(self,dataset_name):
        pass
    @abstractmethod
    def evaluate_accuracy(self):
        pass

class VisionModel(BaseAImodel):
    def train_model(self, dataset_name):
        return f"Traning Vision Model on {dataset_name} image dataset....."
    def evaluate_accuracy(self):
        return "Vision Model Accuracy: 85%"

class nplmodel(BaseAImodel):
    def train_model(self, dataset_name):
        return f"Traning nplmodel on {dataset_name} Text dataset......"
    def evaluate_accuracy(self):
        return "nplmodel sentiment classification accuracy:95% "
    
    
        