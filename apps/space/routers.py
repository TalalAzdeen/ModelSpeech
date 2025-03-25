from fastapi import APIRouter
from pydantic import BaseModel
from typing import Optional


 

class SpaceHandler:
    def __init__(self, builder):
        self.router = APIRouter()
        self.__builder = builder

     
        @self.router.post("/createspace_compoent")
        def createspace_compoent(description, ram=20, cpu_cores=3, disk_space=4,
                     is_gpu=True, is_global=True, bandwidth=4):
            return self.__builder.createspace_compoent(description,ram, cpu_cores, disk_space,
                     is_gpu, is_global, bandwidth)
        

        @self.router.post("/updatespace_compoent")
        def createspace_compoent(description, ram=20, cpu_cores=3, disk_space=4,
                     is_gpu=True, is_global=True, bandwidth=4):
            return self.__builder.createspace_compoent(description,ram, cpu_cores, disk_space,
                     is_gpu, is_global, bandwidth)

        
        # @self.router.post("/error-event-handler")
        # def error_event_handler(e: Exception, function_name: str = ""):
        #     return self.__builder.error_event_handler(e, function_name)
        @self.router.post("/handle_error")
        def handle_error(message: str, status_code: int):
            return self.__builder.handle_error(message, status_code)

    def get_router(self):
        return self.router
