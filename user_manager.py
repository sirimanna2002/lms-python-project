# user_management.py
class UserManager:
    def __init__(self):
        self.users = []

    def add_user(self, user):
        self.users.append(user)

    def list_users(self):
        for user in self.users:
            print(user)
