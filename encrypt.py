from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import json
import os
import base64
from cryptography.hazmat.primitives.ciphers.aead import AESGCM

# ------------------ إعداد FastAPI ------------------
app = FastAPI(title="Company Info Encryption API")
router = APIRouter()

DB_FILE = "db.json"

# ------------------ قاعدة البيانات ------------------
def load_db():
    if os.path.exists(DB_FILE):
        with open(DB_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return {"encrypted_data_list": []}

def save_db(db):
    with open(DB_FILE, "w", encoding="utf-8") as f:
        json.dump(db, f, indent=2, ensure_ascii=False)

db_json = load_db()

# ------------------ التشفير وفك التشفير ------------------
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

# ------------------ نماذج البيانات ------------------
class CompanyInfo(BaseModel):
    company_name: str
    license: str
    employees: int
    services: list[str]

class EncryptionKeyRequest(BaseModel):
    encryption_key: str

# ------------------ واجهات API ------------------
@router.post("/add-company/")
def add_company(company_info: CompanyInfo):
    encrypted_item = encrypt_json(company_info.dict())
    db_json["encrypted_data_list"].append(encrypted_item)
    save_db(db_json)
    return {"encryption_key": encrypted_item["encryption_key"]}

@router.post("/get-company/")
def get_company(data: EncryptionKeyRequest):
    found_item = next(
        (item for item in db_json["encrypted_data_list"] if item["encryption_key"] == data.encryption_key),
        None
    )
    if not found_item:
        raise HTTPException(status_code=404, detail="Company not found")
    decrypted_data = decrypt_json(found_item["encrypted_token"], found_item["encryption_key"])
    return {"company_info": decrypted_data}

def get_router():
        return router
