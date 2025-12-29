class UserRepository:
    def __init__(self):
        self.users = {}

    def save(self, user):
        self.users[user.user_id] = user

    def find_by_id(self, user_id):
        return self.users.get(user_id)

    def find_by_username(self, username):
        for user in self.users.values():
            if user.username == username:
                return user
        return None
