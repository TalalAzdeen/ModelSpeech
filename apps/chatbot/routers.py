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
        @self.router.post("/ChatText2Speech")
        def Chat_Text2Speech(text: str,voice:str="alloy", speed=1,api_key: str = ""):
            return self.__builder.text_to_speech(text,voice,speed,api_key)
       
        
    def get_router(self):
        return self.router
