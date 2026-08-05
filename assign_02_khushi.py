# HW - Team Devdoots Python Assignment 02
# Task: OOPs & Inheritance (Smart User Access System)

# Parent Class
class BaseUser:
    def __init__(self, username, email):
        self.username = username
        self.email = email

    def get_profile(self):
        return f"User: {self.username} | Email: {self.email}"


# Child Class inheriting BaseUser
class AdminUser(BaseUser):
    def __init__(self, username, email, permissions_level):
        # Call Parent Class constructor
        super().__init__(username, email)
        self.permissions_level = permissions_level

    # Method Overriding
    def get_profile(self):
        base_info = super().get_profile()
        return f"{base_info} | Role: Admin | Permissions: {self.permissions_level}"


# Testing the implementation
if __name__ == "__main__":
    try:
        print("---  Smart Role-Based User Access System 👤 ---\n")

        # BaseUser object
        user1 = BaseUser("khushi_yadav", "khushi@gmail.com")
        print("Standard User Profile:")
        print(user1.get_profile())

        print("-" * 50)

        # AdminUser object
        admin1 = AdminUser("devdoot_leader", "leader@devdoots.com", "Full Access")
        print("Admin User Profile (Overridden):")
        print(admin1.get_profile())

        print("\n HW-2 Code executed successfully!")

    except Exception as e:
        print(f" Error occurred: {e}")