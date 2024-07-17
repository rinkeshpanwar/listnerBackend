from datetime import datetime, timedelta
from jose import jwt
from fastapi.security import OAuth2PasswordBearer
from pydantic import BaseModel

COLLECTION = "COLLECTION"
USER_COLLECTION  = "users"
QUESTION_COLLECTION = "questions"
ANSWER_COLLECTION = "answers"

SECRET_KEY = "09d25e094faaFDSF6ca255FDSFDS6c818166b7a95342363b9FDSFS3f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
class TokenData(BaseModel):
    username: str = None
    id: int = None


def create_access_token(data: dict, expires_delta: timedelta = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(weeks=48)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt
