# parent class
class BaseUser:
    def __init__(self, username, email):
        self.username = username
        self.email = email

    def get_profile(self):
        return f"User: {self.username} | Email: {self.email}"

# child class
class AdminUser(BaseUser):
    def __init__(self, username, email, permissions_level):
        super().__init__(username, email)
        self.permissions_level = permissions_level

    # override method
    def get_profile(self):
        return f"ADMIN: {self.username} | Email: {self.email} | Permissions: {self.permissions_level}"

# testing
user1 = BaseUser("Balram", "balram@email.com")
admin1 = AdminUser("Ritesh", "ritesh@email.com", "Full Access")

# print profiles
print(user1.get_profile())
print(admin1.get_profile())