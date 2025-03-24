from fastapi import APIRouter
from pydantic import BaseModel
from typing import Optional


class FilterModelAI(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    language: Optional[str] = None
    isStandard: Optional[bool] = None
    gender: Optional[str] = None
    dialect: Optional[str] = None
    Type: Optional[str] = None


class AudioRequest(BaseModel):
    token: str
    message: str


class UserHandler:
    def __init__(self, builder):
        self.router = APIRouter()
        self.__builder = builder

        # تغليف الدوال غير المتعلقة بـ gradio
        @self.router.post("/generate-audio")
        def generate_audio(request: AudioRequest):
            return self.__builder.generate_audio(request.token, request.message)

        @self.router.post("/filter")
        def get_filter(filter_data: FilterModelAI, return_name: str):
            if not filter_data or not return_name:
                return {"error": "Invalid filter data or return name."}
            result = self.__builder.get_filter(filter_data, return_name)
            return result

        @self.router.post("/update-languages")
        def update_languages(category: str):
            return self.__builder.update_languages(category)

        @self.router.post("/update-dialects")
        def update_dialects(category: str, language: str):
            return self.__builder.update_dialects(category, language)

        @self.router.post("/update-models")
        def update_models(category: str, language: str, dialect: str):
            return self.__builder.update_models(category, language, dialect)

        @self.router.post("/ask-ai")
        def ask_ai(message: str, model: str = ""):
            return self.__builder.ask_ai(message, model)

       
        @self.router.post("/initialize-client")
        def initialize_client(modelAi: str, token: str, service: str, message: str):
            return self.__builder.initialize_client(modelAi, token, service, message)

        @self.router.post("/validate-input")
        def validate_input(message: str):
            return self.__builder.validate_input(message)

        @self.router.post("/send-request")
        def send_request(data: dict):
            return self.__builder.send_request(data)

        @self.router.post("/send-event-request")
        def send_event_request(data: dict, request: dict, result: dict, status_code: int):
            return self.__builder.send_event_request(data, request, result, status_code)

        # @self.router.post("/error-event-handler")
        # def error_event_handler(e: Exception, function_name: str = ""):
        #     return self.__builder.error_event_handler(e, function_name)
        @self.router.post("/handle_error")
        def handle_error(message: str, status_code: int):
            return self.__builder.handle_error(message, status_code)

    def get_router(self):
        return self.router
