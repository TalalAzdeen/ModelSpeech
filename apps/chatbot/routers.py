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
        def Chat_Text2Speech(text:str,api_key: str,file_type:str="wav",voice:str="alloy", speed=1):
            return self.__builder.text_to_speech_and_upload(text,api_key,file_type,voice,speed)
       
        
    def get_router(self):
        return self.router
