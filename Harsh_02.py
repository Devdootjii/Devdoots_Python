class BaseUser:
    def __init__(self, username, email):
        self.username = username
        self.email = email
        
    def get_profile(self):
        return f"User: {self.username} | Email: {self.email}"

class AdminUser(BaseUser):
    def __init__(self, username, email, permissions_level):
        self.permissions_level = permissions_level
        super().__init__(username, email)
        
    def get_profile(self):
        return f"ADMIN: {self.username} | Email: {self.email} | Permissions: {self.permissions_level}"

normal_user = BaseUser("Rohan", "rohan@email.com")
admin_user = AdminUser("Harsh", "harshrajbhar666@gmail.com", "SuperAdmin")

print(normal_user.get_profile())
print(admin_user.get_profile())
