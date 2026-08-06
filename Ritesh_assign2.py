# BaseUser (Parent Class)
class BaseUser:
    def __init__(self, username, email):
        self.username = username
        self.email = email

    # Normal profile method
    def get_profile(self):
        return f"User: {self.username} | Email: {self.email}"


# AdminUser (Child Class inheriting BaseUser)
class AdminUser(BaseUser):
    def __init__(self, username, email, permissions_level):
        super().__init__(username, email)  # Parent constructor call
        self.permissions_level = permissions_level

    # Method Overriding
    def get_profile(self):
        return f"ADMIN: {self.username} | Email: {self.email} | Permissions: {self.permissions_level}"


# Execution Block
if __name__ == "__main__":
    # BaseUser object
    user1 = BaseUser(username="ritesh_dev", email="ritesh@devdoots.com")

    # AdminUser object 
    admin1 = AdminUser(
        username="divyansh_tpm", 
        email="divyansh@devdoots.com", 
        permissions_level="Full Access"
    )

    # Outputs
    print("--- Base User Output ---")
    print(user1.get_profile())

    print("\n--- Admin User Output ---")
    print(admin1.get_profile())