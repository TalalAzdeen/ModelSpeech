from fastapi import APIRouter, UploadFile, File, HTTPException
from pydantic import BaseModel
import uuid
import json
import os
import base64
from cryptography.hazmat.primitives.ciphers.aead import AESGCM

class UserHandler:
    def __init__(self, builder):
        self.router = APIRouter()
        self.__builder = builder

        # --- قاعدة البيانات والشركات المشفرة ---
        self.DB_FILE = "db.json"
        self.db_json = self.load_db()

        # --- إدارة الجلسات ---
        self.sessions = {}

        # ------------------ نماذج البيانات ------------------
        class CompanyInfo(BaseModel):
            company_name: str
            license: str
            employees: int
            services: list

        class SearchKeyRequest(BaseModel):
            encryption_key: str

        class SessionEndRequest(BaseModel):
            session_id: str

        # ------------------ دوال مساعدة ------------------
        def load_db():
            if os.path.exists(self.DB_FILE):
                with open(self.DB_FILE, "r", encoding="utf-8") as f:
                    return json.load(f)
            return {"encrypted_data_list": []}

        def save_db():
            with open(self.DB_FILE, "w", encoding="utf-8") as f:
                json.dump(self.db_json, f, indent=2, ensure_ascii=False)

        def encrypt_json(data: dict) -> dict:
            plaintext = json.dumps(data, ensure_ascii=False).encode('utf-8')
            key = AESGCM.generate_key(bit_length=256)
            aesgcm = AESGCM(key)
            nonce = os.urandom(12)
            ciphertext = aesgcm.encrypt(nonce, plaintext, associated_data=None)
            return {
                "encrypted_token": base64.urlsafe_b64encode(nonce + ciphertext).decode('utf-8'),
                "encryption_key": base64.urlsafe_b64encode(key).decode('utf-8')
            }

        def decrypt_json(encrypted_token_b64: str, encryption_key_b64: str) -> dict:
            data = base64.urlsafe_b64decode(encrypted_token_b64)
            key = base64.urlsafe_b64decode(encryption_key_b64)
            nonce = data[:12]
            ciphertext = data[12:]
            aesgcm = AESGCM(key)
            plaintext = aesgcm.decrypt(nonce, ciphertext, associated_data=None)
            return json.loads(plaintext.decode('utf-8'))

        # ------------------ API Routes ------------------

        # إضافة شركة مشفرة
        @self.router.post("/company/add")
        def api_add_company(company: CompanyInfo):
            encrypted_item = encrypt_json(company.dict())
            self.db_json["encrypted_data_list"].append(encrypted_item)
            save_db()
            return {"message": "Company added successfully", "encryption_key": encrypted_item["encryption_key"]}

        # البحث عن شركة
        @self.router.post("/company/find")
        def api_find_company(request: SearchKeyRequest):
            found_item = next(
                (item for item in self.db_json["encrypted_data_list"] if item["encryption_key"] == request.encryption_key),
                None
            )
            if not found_item:
                raise HTTPException(status_code=404, detail="Company not found")
            return decrypt_json(found_item["encrypted_token"], found_item["encryption_key"])

        # ------------------ خدمات Chat ------------------
        @self.router.post("/ChatText2Text")
        def Chat_Text2Text(message: str, key: str = "", session_id: str = None):
            if session_id and session_id not in self.sessions:
                return {"error": "Invalid session_id"}
            return self.__builder.ask_ai(message, key)

        @self.router.post("/ChatText2Speech")
        def Chat_Text2Speech(text: str, api_key: str, file_type: str = "wav", voice: str = "alloy", session_id: str = None):
            if session_id and session_id not in self.sessions:
                return {"error": "Invalid session_id"}
            return self.__builder.text_to_speech_and_upload(text, api_key, file_type)

        @self.router.post("/ChatSpeech2Text")
        async def Chat_Speech2Text(file: UploadFile = File(...), api_key: str = "", session_id: str = None):
            if session_id and session_id not in self.sessions:
                return {"error": "Invalid session_id"}
            audio_bytes = await file.read()
            return self.__builder.speech_to_text(audio_bytes, api_key)

        @self.router.post("/ChatEmbed")
        def Chat_Embed(text: str, api_key: str = "", session_id: str = None):
            if session_id and session_id not in self.sessions:
                return {"error": "Invalid session_id"}
            return self.__builder.text_to_embedding(text, api_key)

        # Health check
        @self.router.get("/health")
        def health_check():
            return {"status": "ok", "message": "API is running"}

        # ------------------ إدارة الجلسات ------------------
        @self.router.post("/session/create")
        def create_session():
            session_id = str(uuid.uuid4())
            self.sessions[session_id] = {"active": True}
            return {"session_id": session_id, "message": "Session created successfully"}

        @self.router.post("/session/end")
        def end_session(request: SessionEndRequest):
            if request.session_id not in self.sessions:
                return {"error": "Invalid session_id"}
            self.sessions.pop(request.session_id)
            return {"message": f"Session {request.session_id} ended successfully"}

        # حفظ الدوال المساعدة داخل الكلاس
        self.load_db = load_db
        self.save_db = save_db
        self.encrypt_json = encrypt_json
        self.decrypt_json = decrypt_json

    # دالة إرجاع الرواتر
    def get_router(self):
        return self.router

