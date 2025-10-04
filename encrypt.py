from fastapi import FastAPI, HTTPException, APIRouter
from pydantic import BaseModel
import json
import os
import base64
from cryptography.hazmat.primitives.ciphers.aead import AESGCM


DB_FILE = "db.json"


class CompanyInfo(BaseModel):
    key_service:str
    company_name: str
    license: str
    employees: int
    services: list[str]


class EncryptionKeyRequest(BaseModel):
    encryption_key: str


class CompanyHandler:
    def __init__(self):
        self.router = APIRouter()
        self.db_json = self.load_db()

        # --------- API Routes ----------
        @self.router.post("/add-company/")
        def add_company(company_info: CompanyInfo):
            encrypted_item = self.encrypt_json(company_info.dict())
            self.db_json["encrypted_data_list"].append(encrypted_item)
            self.save_db(self.db_json)
            return {"encryption_key": encrypted_item["encryption_key"]}

        @self.router.post("/get-company/")
        def get_company(data: EncryptionKeyRequest):
            found_item = next(
                (item for item in self.db_json["encrypted_data_list"] if item["encryption_key"] == data.encryption_key),
                None
            )
            if not found_item:
                raise HTTPException(status_code=404, detail="Company not found")
            decrypted_data = self.decrypt_json(found_item["encrypted_token"], found_item["encryption_key"])
            return {"company_info": decrypted_data}

    # --------- Database Methods ----------
    def load_db(self):
        if os.path.exists(DB_FILE):
            with open(DB_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        return {"encrypted_data_list": []}

    def save_db(self, db):
        with open(DB_FILE, "w", encoding="utf-8") as f:
            json.dump(db, f, indent=2, ensure_ascii=False)

    # --------- Encryption / Decryption ----------
    def encrypt_json(self, data: dict) -> dict:
        plaintext = json.dumps(data, ensure_ascii=False).encode('utf-8')
        key = AESGCM.generate_key(bit_length=256)
        aesgcm = AESGCM(key)
        nonce = os.urandom(12)
        ciphertext = aesgcm.encrypt(nonce, plaintext, associated_data=None)
        return {
            "encrypted_token": base64.urlsafe_b64encode(nonce + ciphertext).decode('utf-8'),
            "encryption_key": base64.urlsafe_b64encode(key).decode('utf-8')
        }

    def decrypt_json(self, encrypted_token_b64: str, encryption_key_b64: str) -> dict:
        data = base64.urlsafe_b64decode(encrypted_token_b64)
        key = base64.urlsafe_b64decode(encryption_key_b64)
        nonce = data[:12]
        ciphertext = data[12:]
        aesgcm = AESGCM(key)
        plaintext = aesgcm.decrypt(nonce, ciphertext, associated_data=None)
        return json.loads(plaintext.decode('utf-8'))

    def get_router(self):
        return self.router
