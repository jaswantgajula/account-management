import uuid
from models import User

class UserService:
    def __init__(self, repo):
        self.repo = repo

    def register_user(self, username, name):
        if self.repo.find_by_username(username):
            return None

        user_id = str(uuid.uuid4())  # placeholder for Snowflake
        user = User(user_id, username, name)
        self.repo.save(user)
        return user

    def get_profile(self, user_id):
        return self.repo.find_by_id(user_id)

    def update_bio(self, user_id, bio):
        user = self.repo.find_by_id(user_id)
        if user:
            user.bio = bio
        return user
