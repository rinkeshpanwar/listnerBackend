from fastapi import APIRouter
from schema import auth as authSchema
from crud.auth import AUTHCrud
from fastapi import status
from fastapi.responses import ORJSONResponse

router = APIRouter()

@router.post("/signup", status_code=status.HTTP_201_CREATED)
def signup(user: authSchema.Createuser) -> authSchema.User:
    user_db = AUTHCrud.getUser(user.username)
    print("user in database",user_db)
    if len(user_db._items) > 0 :
        return ORJSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content={"message": "user already exist"})
    return AUTHCrud.createUser(user)

@router.get("/allUser")
def allUser():
    return AUTHCrud.getAllUsers()
