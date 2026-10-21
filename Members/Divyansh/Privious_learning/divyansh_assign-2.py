class BaseUser:
    def __init__(self,username,email):
        self.username=username
        self.email = email
    def get_profile(self):
        return f"User : {self.username} | Email : {self.email}"

class AdminUser(BaseUser):
    def __init__(self, username, email,permission_level):
        super().__init__(username, email)
        self.permission_level=permission_level

    def get_profile(self):
        return f"Admin : {self.username} | Email : {self.email} | Permission : {self.permission_level}"

user1=BaseUser("Div","kdivyansh453@gamail.com")
admin1=AdminUser("Dev","devdootji@gmail.com","Full Access!")    
print(user1.get_profile())
print(admin1.get_profile())