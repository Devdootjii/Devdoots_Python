# cell_id = "Divya-Prime"
# status = True
# print(f"{cell_id} is currently active:{status}")
# power=input("Enter EPM magnet power level:")


# cart_total =500
# if cart_total>= 500:
#     print(f"Hurray! Free Delivery")
# else:
#     print(f"Delivery Charge:50")


# usernames=["Khusi","Balram","Admin"]
# for name in usernames:
#     if name == "Admin":
#         print(f"Welcome {name}! Full Access Granted")
#     else:
#         print(f"Welcome {name}! Limited Access")

# def check_even_odd(number):
#     if number % 2 == 0:
#         return "Even"
#     else:
#         return "Odd"
# print(check_even_odd(10))
# print(check_even_odd(15))

# laptop_specs={
#     "brand":"HP",
#     "ram_gb":256,
#     "processor":"intel i5"
# }
# print(f"This is a {laptop_specs['brand']} with {laptop_specs['ram_gb']} GB RAM and {laptop_specs['processor']} processor.")

# try:
#     num1=int(input("Enter a number:"))
#     num2=int(input("Enter a number:"))
#     result= num1/num2
#     print(result)
# except ZeroDivisionError:
#     print(f"Error: Please do not enter 0 ")

# class UserAccount:
#     def __init__(self,username,role):
#         self.username= username
#         self.role= role

#     def get_access_info(self):
#         if self.role =="admin" :
#             return f"{self.username} has Full Access"
#         else:
#             return f"{self.username} has Basic Access"


# user1 = UserAccount("adimn_user","admin")
# user2 = UserAccount("normal_user","normal")

# print(user1.get_access_info())
# print(user2.get_access_info())

# class DevdootMember :
#     def __init__(self,name,skill):
#         self.name=name
#         self.skill=skill

#     def introduce(self):
#         return f"I am {self.name} and my skill is {self.skill}."

# memb1=DevdootMember("Divyansh","Lead TPM")
# memb2=DevdootMember("Khushi","Cloud Engineer")
# memb3=DevdootMember("Balram","Data Scientist")
# memb4=DevdootMember("Ritesh","Data Scientist")
# memb5=DevdootMember("Harsh Gautum","Full Stack Devloper")
# memb6=DevdootMember("Harsh Rajbhar","AI Engineer")

# print(memb1.introduce())
# print(memb2.introduce())
# print(memb3.introduce())
# print(memb4.introduce())
# print(memb5.introduce())
# print(memb6.introduce())

# Parent Class (Base Class)
# class DevdootMember:

#   def __init__(self, name):
#     self.name = name

#   def status(self):
#     return f"{self.name} is an active Devdoot member."


# # Child Class (Inherit kar rahi hai Parent Class ko)
# class AIEngineer(DevdootMember):

#   def __init__(self, name, model_specialization):
#     # Parent class ke __init__ ko call karna
#     super().__init__(name)
#     self.specialization = model_specialization

#   def show_work(self):
#     return f"{self.name} is training {self.specialization} models."


# # Object Creation
# engineer1 = AIEngineer("Harsh", "LLM Fine-Tuning")

# # Parent class ka method use karna (jo inherite hua hai)
# print(engineer1.status())

# # Child class ka apna method use karna
# print(engineer1.show_work())


# class BaseBot:
#     def __init__(self,bot_name):
#         self.bot_name=bot_name
#     def power_on(self):
#         return f"{self.bot_name} is Powered ON!"

# class DAIVYCell(BaseBot):
#     pass

# cell1 = DAIVYCell("Cell_01")
# print(cell1.power_on())
# print(DAIVYCell.__mro__)

# class Product :
#     def __init__(self,title,price):
#         self.title=title
#         self.price = price

#     def get_details(self):
#         return f"Product: {self.title} | Price: {self.price}"

# class DigitalProduct(Product):
#     def __init__(self, title, price,file_size_mb):
#         super().__init__(title, price)
#         self.file_size_mb=file_size_mb

#     def get_details(self):
#         return f"Digital Item: {self.title} | Price: {self.price} | Size : {self.file_size_mb}"


# ebook = DigitalProduct("Python master guide",299,15)

# print(ebook.get_details())

#encapsulation
# class APIService:
#     def __init__(self,service_name,__api_key):
#         self.service_name=service_name
#         self.__api_key=__api_key

#     def get_service_status(self):
#         return f"Service {self.service_name} is Active."

#     def get_masked_key(self):
#         return f"API key: {self.__api_key[-4:]}"

# service=APIService("Open AI","sk-123456789")

# print(service.get_masked_key())
# # print(service.__api_key)
# print(service.service_name)


#practice

# class SmartWallet:
#     def __init__(self,user_name,initial_balance=1000):
#         self.user_name=user_name
#         self.__balance=initial_balance
        
#     def add_funds(self,amount):
#         if amount > 0 :
#             self.__balance+=amount
#             return f"{amount} added successfully!"
#         return f"Invalid Amount!"

#     def pay_bill(self,amount):
#         if amount<= self.__balance:
#             self.__balance -= amount
#             return f"Payment of {amount} successful!"
#         return "Insufficient Balance!"

#     def check_balance(self):
#         return f"Wallet Owner: {self.user_name} | Current Balance : {self.__balance}"

# wallet = SmartWallet("Divyansh")

# print(wallet.add_funds(500))
# print(wallet.pay_bill(200))
# print(wallet.check_balance())

#practice drill

# class PhoneBattery:
#     def __init__(self,brand,__percentage=100):
#         self.brand=brand
#         self.__percentage=__percentage
#     def Use_phone(self,drain_amount):
#         self.__percentage -= drain_amount
#         if self.__percentage <0:
#             self.__percentage=0
#         return f"Used {drain_amount}%. Remaining:{self.__percentage}%"
#     def get_battery_status(self):
#         return f"{self.brand} Phone | Battery :{self.__percentage}"
# phone = PhoneBattery("Pixel")
# print(phone.Use_phone(30))
# print(phone.Use_phone(80))
# print(phone.get_battery_status())

#Abstraction

# from abc import ABC, abstractmethod

# class PaymentGateway(ABC):
#     @abstractmethod
#     def pay(self,amount):
#         pass

# class UPIPayment(PaymentGateway):
#     def pay(self,amount):
#         return f"Paid {amount} successfully via UPI!"

# upi = UPIPayment()
# print(upi.pay(500))


# try except 

# try:
#     user_input = int(input("Enter a number:"))
#     print("Your Calculation:",100/user_input)
# except ValueError:
#     print("Error! Please enter only numbers.")
# except ZeroDivisionError:
#     print("Error! division by 0 is not possible.")

# else:
#     print("Calculation successful!")

#file handling

# with open("activity_log.txt","a") as file:
#     file.write("Divyansh : Completed Exception Handling and File I/O practice!\n")
# try:
#     with open("activity_log.txt","r") as file:
#         content=file.read()
#         print(f"File content:{content}")
# except FileNotFoundError:
#     print("Error ! file don't exist")


# practice drill

# def build_pipeline(*metrics,**config):
#     print(f"Tracking Metrcis:{metrics}\nPipeline Config:{config}")

# build_pipeline("Accuracy", "F1-Score", lr=0.001, epochs=100)

# system_state = "OFFLINE"
# def start_training():
#   global system_state
#   system_state = "TRAINING"

# start_training()
# print(f"Current State: {system_state}") 

# to_percent = lambda x: x*100
# print(to_percent(0.85),"%")
# print(to_percent(0.123),"%")