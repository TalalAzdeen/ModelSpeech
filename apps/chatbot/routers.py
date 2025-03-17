from fastapi import APIRouter

class UserHandler:
    router = APIRouter()

    @router.get("/users")
    def get_users():
        return {"message": "List of users"}

    @router.get("/users/{user_id}")
    def get_user(user_id: int):
        return {"message": f"User {user_id}"}
