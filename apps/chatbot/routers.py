# from fastapi import APIRouter

# class UserHandler:
#     def __init__(self,builder):
#         self.router = APIRouter()
#         self.__builder=builder
    

#         @self.router.get("/users")
#         def get_users():
#             return {"message": "List of users"}

#         @self.router.get("/users/{user_id}")
#         def get_user(user_id: int):
#             return {"message": f"User {user_id}"}

#     def  get_router(self):
    
#            return self.router

from fastapi import APIRouter
from pydantic import BaseModel, Field
from typing import Optional
import time


class FilterModelAI(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    language: Optional[str] = None
    isStandard: Optional[bool] = None
    gender: Optional[str] = None
    dialect: Optional[str] = None
    Type: Optional[str] = None
class UserHandler:
    def __init__(self, builder):
        self.router = APIRouter()
        self.__builder = builder

        # 🔹 دوال الـ API
        @self.router.get("/service-id")
        def get_service_id():
            return {"serviceId": self.__builder.get_serviceId()}

        @self.router.get("/space-id")
        def get_space_id():
            return {"spaceId": self.__builder.get_spaceid()}

        @self.router.post("/ask-ai")
        def ask_ai(message: str):
            return self.__builder.ask_ai(message)

        @self.router.post("/generate-audio")
        def generate_audio(token: str, message: str):
            return self.__builder.generate_audio(token, message)

        @self.router.post("/filter")
        def get_filter(filter_data: FilterModelAI):
            return {"filtered_data": filter_data.dict()}

        @self.router.get("/filter-options")
        def get_filter_options(category: Optional[str] = None):
            return self.__builder.get_filter(FilterModelAI(category=category), "language")
                 
            

    def get_router(self):
        return self.router

