from fastapi import FastAPI
from repository import UserRepository
from service import UserService

app = FastAPI()

repo = UserRepository()
service = UserService(repo)

@app.post("/register")
def register(username: str, name: str):
    user = service.register_user(username, name)
    if not user:
        return {"error": "Username already exists"}
    return {"user_id": user.user_id}

@app.get("/user/{user_id}")
def get_profile(user_id: str):
    user = service.get_profile(user_id)
    if not user:
        return {"error": "User not found"}
    return {
        "username": user.username,
        "name": user.name,
        "bio": user.bio
    }

@app.put("/user/{user_id}/bio")
def update_bio(user_id: str, bio: str):
    user = service.update_bio(user_id, bio)
    if not user:
        return {"error": "User not found"}
    return {"message": "Bio updated"}
