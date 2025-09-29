from fastapi import APIRouter
from pydantic import BaseModel
from typing import Optional


 


class UserHandler:
    def __init__(self, builder):
        self.router = APIRouter()
        self.__builder = builder

        @self.router.post("/ChatText2Text")
        def Chat_Text2Text(message: str, key: str = ""):
            return self.__builder.ask_ai(message,key)

       
        
    def get_router(self):
        return self.router
