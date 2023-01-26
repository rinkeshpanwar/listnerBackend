from fastapi import APIRouter
from schema import auth as authSchema
from crud.auth import AUTHCrud
from fastapi import status, Depends
from db.base import pwd_context
from jose import jwt, JWTError
from fastapi.responses import JSONResponse
from utils.utlis import create_access_token, oauth2_scheme, ALGORITHM, SECRET_KEY, TokenData
from fastapi.security import OAuth2PasswordRequestForm
from fastapi import Depends, HTTPException, status
from crud.auth import AUTHCrud

router = APIRouter()

@router.post("/token")
async def login_for_access_token(user: OAuth2PasswordRequestForm = Depends()):
    user_db = AUTHCrud.getUser(user.username)
    if len(user_db._items) == 0:
        return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content={"message": "user not found"})

    if not pwd_context.verify(user.password, user_db._items[0]["password"]):
        return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content={"message": "incorrect password"})

    token = create_access_token(data={"sub": user.username})

    return {"access_token": token, "token_type": "bearer"}

def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = TokenData(username=username)
    except JWTError:
        raise credentials_exception
    return token_data

@router.post("/signup", status_code=status.HTTP_201_CREATED)
def signup(user: authSchema.Createuser) -> authSchema.User:
    user_db = AUTHCrud.getUser(user.username)
    print("user in database",user_db)
    if len(user_db._items) > 0 :
        return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content={"message": "user already exist"})
    return AUTHCrud.createUser(user)

@router.get("/allUser")
def allUser():
    return AUTHCrud.getAllUsers()

@router.get("/myself", response_model=authSchema.User)
def mySelf(user = Depends(get_current_user)):
    return user