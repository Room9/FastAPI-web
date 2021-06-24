import base64
import hashlib

from passlib.context import CryptContext
from my_settings     import SECRET

pwd_cxt = CryptContext(schemes=["bcrypt"], deprecated="auto")

def bcrypt(password: str):
    return pwd_cxt.hash(password)

def verify(hashed_password, plain_password):
    return pwd_cxt.verify(plain_password, hashed_password)

def create_hash(id: str, email: str):
    hasher = hashlib.sha256()
    user_string = id + email + SECRET['KEY']
    hasher.update(bytes(user_string, 'utf-8'))
    hashed = base64.urlsafe_b64encode(hasher.digest())
    return hashed
